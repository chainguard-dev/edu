---
title: "Kubernetes Policy Enforcement with OPA Gatekeeper"
linktitle: "OPA Gatekeeper"
type: "article"
description: "How to enforce best practices and ensure compliance with OPA Gatekeeper."
date: 2025-09-02T10:00:00-00:00
lastmod: 2025-09-02T10:00:00-00:00
draft: false
tags: ["Chainguard Containers", "Overview", "Policy"]
images: []
weight: 005
toc: true
---

[Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/) is an admission controller that enforces policies in Kubernetes clusters. This
article describes how it can be leveraged to ensure resources follow best practices related to the use of Chainguard Containers.


## Prerequisites

To follow the examples in this guide, you will need the following:
- `kubectl` — the command line interface tool for Kubernetes — installed on your local machine.
- Administrative access to a Kubernetes cluster where [OPA Gatekeeper is already installed](https://open-policy-agent.github.io/gatekeeper/website/docs/install).


## Ensure Images are Pulled From Allowed Repositories

You can use the [`K8sAllowedReposV2` constraint](https://github.com/open-policy-agent/gatekeeper-library/tree/master/library/general/allowedreposv2) from the [Gatekeeper Library](https://github.com/open-policy-agent/gatekeeper-library) to ensure that images are only pulled from a list of allowed repositories.

To configure this constraint, add the constraint template to your cluster.

```shell
kubectl create -f https://raw.githubusercontent.com/open-policy-agent/gatekeeper-library/refs/heads/master/library/general/allowedreposv2/template.yaml
```

Then, create a constraint that only allows images hosted in `cgr.dev`. Note that if you are mirroring Chainguard container images into a different registry, then you could replace this with your own URLs:

```shell
kubectl create -f - <<EOF
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sAllowedReposv2
metadata:
  name: repo-is-cgr-dev
spec:
  match:
    kinds:
      - apiGroups: [""]
        kinds: ["Pod"]
    excludedNamespaces:
      - "kube-system"
  parameters:
    allowedImages:
      - "cgr.dev/*"
EOF
```

Note that you may not be able to control where images provided by the platform are hosted in certain managed Kubernetes solutions.

To test that this constraint is working correctly, try to create a non-compliant pod:

```shell
kubectl create -f - <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: nginx-disallowed
spec:
  containers:
    - name: nginx
      image: nginx
EOF
```
```output
Error from server (Forbidden): error when creating "STDIN": admission webhook "validation.gatekeeper.sh" denied the request: [repo-is-cgr-dev] container <nginx> has an invalid image <nginx>, allowed images are ["cgr.dev/*"]
```

This example tries to create a pod using a container image downloaded from the Docker Hub registry, not Chainguard's registry. As this output indicates, attempting to create a non-compliant pod resulted in an error, and the request was denied.


## Ensure Images are Referenced By Digest

Chainguard Containers are updated frequently to incorporate CVE fixes and package updates. The tags for Chainguard's container images are highly mutable, meaning that the underlying image changes frequently, even for very specific tags like `v1.2.3-r1`.

To prevent the risk of updates introducing breaking changes, you can pull by digest to ensure the use of a specific image.

The [`K8sImageDigests` constraint](https://github.com/open-policy-agent/gatekeeper-library/tree/master/library/general/imagedigests) from the [Gatekeeper Library](https://github.com/open-policy-agent/gatekeeper-library) can be used to mandate this practice inside a Kubernetes cluster.

Add the template to your cluster:

```shell
kubectl create -f https://raw.githubusercontent.com/open-policy-agent/gatekeeper-library/refs/heads/master/library/general/imagedigests/template.yaml
```

Then create the constraint:

```shell
kubectl create -f - <<EOF
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sImageDigests
metadata:
  name: container-image-must-have-digest
spec:
  match:
    kinds:
      - apiGroups: [""]
        kinds: ["Pod"]
    excludedNamespaces:
      - "kube-system"
EOF
```

Be aware that in certain managed Kubernetes solutions, you may not be able to control whether images provided by the platform are referenced by digest.

To test the constraint, try to create a non-compliant pod:

```shell
kubectl create -f - <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: nginx-disallowed
spec:
  containers:
    - name: nginx
      image: cgr.dev/chainguard/nginx
EOF
```
```output
Error from server (Forbidden): error when creating "STDIN": admission webhook "validation.gatekeeper.sh" denied the request: [container-image-must-have-digest] container <nginx> uses an image without a digest <cgr.dev/chainguard/nginx>
```

This example attempts to create a pod using the `nginx` Chainguard container image, but does not pull the image by its digest as required by the constraint. As the output indicates, the attempt resulted in an error and the request was denied.


## Warn First, Deny Later

When introducing new constraints into a cluster, it is a good idea to initially configure them with [`enforcementAction: warn`](https://open-policy-agent.github.io/gatekeeper/website/docs/violations/#warn-enforcement-action) so as to avoid blocking existing workloads.

This way, when a user creates a non-compliant resource, they will get a warning like the following example. This gives the user a signal that they should update their configuration.

```output
Warning: [container-image-must-have-digest] container <nginx> uses an image without a digest <cgr.dev/chainguard/nginx>
```

You can also find non-compliant resources that exist in the cluster by reviewing the constraint's violations:

```shell
kubectl get k8simagedigests container-image-must-have-digest -o json | jq -r '.status.violations[]'
```
```output
{
  "enforcementAction": "warn",
  "group": "",
  "kind": "Pod",
  "message": "container <nginx> uses an image without a digest <cgr.dev/chainguard/nginx>",
  "name": "nginx-disallowed",
  "namespace": "default",
  "version": "v1"
}
```

Once all the violations have been addressed, you can remove `enforcementAction: warn` and Gatekeeper will start to block the creation of resources that violate the constraint.


## Ensure Images Are Signed By Chainguard

This will require having [Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/) external data enabled.

### Install Ratify

```shell
helm repo add ratify https://notaryproject.github.io/ratify
# download the notary verification certificate
curl -sSLO https://raw.githubusercontent.com/deislabs/ratify/main/test/testdata/notation.crt
helm install ratify \
    ratify/ratify \
    --namespace gatekeeper-system \
    --set-file notationCerts={./notation.crt} \
    --set featureFlags.RATIFY_CERT_ROTATION=true \
    --set policy.useRego=true
```

### Create a Verifier

The [verifier](https://ratify.dev/docs/reference/custom%20resources/verifiers) will set up the cosign verification. This example uses the public Chainguard images.

```yaml
apiVersion: config.ratify.deislabs.io/v1beta1
kind: Verifier
metadata:
  name: verifier-cosign-chainguard
spec:
  name: cosign
  artifactTypes: application/vnd.dev.cosign.artifact.sig.v1+json
  parameters:
    trustPolicies:
      - name: chainguard-public
        scopes:
          - "cgr.dev/chainguard/*"
        tLogVerify: true
        keyless:
          ctLogVerify: true
          certificateOIDCIssuer: "https://token.actions.githubusercontent.com"
          certificateIdentity: "https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main"
```

### Create the Policy

Create the Ratify [policy](https://ratify.dev/docs/reference/custom%20resources/policies/#policy). This defines a policy evaluating the verification results for a subject.

```yaml
apiVersion: config.ratify.deislabs.io/v1beta1
kind: Policy
metadata:
  name: ratify-policy
spec:
  type: config-policy
  parameters:
    artifactVerificationPolicies:
      "application/vnd.dev.cosign.artifact.sig.v1+json": "any"
      default: "any"
```

### Create the Constraint Template

By default, a Gatekeeper [constraint template](https://open-policy-agent.github.io/gatekeeper/website/docs/constrainttemplates) uses Rego v0 syntax. This enables v1 syntax. If you want to use v0 syntax the policy will need to be updated. This example also adds an exempt images array to allow specific non-signed images.

```yaml
apiVersion: templates.gatekeeper.sh/v1
kind: ConstraintTemplate
metadata:
  name: k8srequiredimagesignatures
spec:
  crd:
    spec:
      names:
        kind: K8sRequiredImageSignatures
      validation:
        openAPIV3Schema:
          type: object
          properties:
            exemptImages:
              type: array
              items:
                type: string
  targets:
    - target: admission.k8s.gatekeeper.sh
      code:
        - engine: Rego
          source:
            version: "v1"
            rego: |
              package k8srequiredimagesignatures

              default exemptions := []

              exemptions := input.parameters.exemptImages

              all_images contains val.image if {
                  containers := object.get(input.review.object.spec.template.spec, "containers", [])
                  initContainers := object.get(input.review.object.spec.template.spec, "initContainers", [])
                  ephContainers := object.get(input.review.object.spec.template.spec, "ephemeralContainers", [])

                  vals := array.concat(containers, array.concat(initContainers, ephContainers))
                  some val in vals
              }

              ratify_response(image) = resp if {
                      resp := external_data({
                        "provider": "ratify-provider",
                        "keys": [image],
                      })
              }

              responses contains {"image": resp[0], "data": resp[1]} if {
                some image in all_images
                not image in exemptions

                rat_resp := ratify_response(image)
                resp := rat_resp.responses[_]
              }

              violation contains {"msg": msg} if {
                some resp in responses
              	resp.data.system_error != ""
              	msg := sprintf("image %q verification system error: %v", [resp.image, resp.data.system_error])
              }

              violation contains {"msg": msg} if {
                some resp in responses
              	count(resp.data.responses) == 0
              	msg := sprintf("image %q returned no verification response", [resp.image])
              }

              violation contains {"msg": msg} if {
                some resp in responses
                not resp.data.isSuccess
              	reason := object.get(resp.data, "message", "verification failed")
              	msg := sprintf("image %q is not signed by Chainguard: %v", [resp.image, reason])
              }

              violation contains {"msg": msg} if {
                some resp in responses
              	err := resp.data.errors[_]
                err[0] == resp.image
              	msg := sprintf("image %q verification error: %v", [resp.image, err[1]])
              }
```

### Create the Constraint

The constraint ties the constraint template to the Kubernetes kinds you define.

```yaml
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sRequiredImageSignatures
metadata:
  name: require-signed-images
spec:
  match:
    kinds:
      - apiGroups: [""]
        kinds: ["Pod"]
      - apiGroups: ["apps"]
        kinds: ["Deployment", "StatefulSet", "DaemonSet", "ReplicaSet"]
  parameters:
    exemptImages:
      - "registry.k8s.io/pause:3.9"

```

### Try Deploying a Chainguard Image


```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-chainguard
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx-chainguard
  template:
    metadata:
      labels:
        app: nginx-chainguard
    spec:
      containers:
        - name: nginx
          image: cgr.dev/chainguard/nginx:latest
          ports:
            - containerPort: 8080
```

This should successfully create a deployment.

### Try Deploying a non-Chainguard Image

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-unsigned
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx-unsigned
  template:
    metadata:
      labels:
        app: nginx-unsigned
    spec:
      containers:
        - name: nginx
          image: nginx:latest
          ports:
            - containerPort: 80

```

You will get an error like this explaining that the deployment was blocked because the image was not signed by Chainguard.

```output
Error from server (Forbidden): error when creating "bad-deployment.yaml": admission webhook "validation.gatekeeper.sh" denied the request: [require-signed-images] image "docker.io/library/nginx@sha256:7150b3a39203cb
5bee612ff4a9d18774f8c7caf6399d6e8985e97e28eb751c18" is not signed by Chainguard: verification failed
```

## Learn More

By combining OPA Gatekeeper with Chainguard container images, you gain a powerful way to enforce security and compliance across your Kubernetes clusters. Gatekeeper ensures that only container images meeting your defined policies are deployed, while Chainguard Containers provide a minimal, hardened foundation to reduce risk from the start. Together, they help teams ship software more securely and confidently, without slowing down development.

If you'd like to learn more about Gatekeeper, we encourage you to refer to the [official documentation](https://open-policy-agent.github.io/gatekeeper/website/docs/).
