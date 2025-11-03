---
title: "Kubernetes Policy Enforcement with Kyverno"
linktitle: "Kyverno"
type: "article"
description: "How to enforce best practices and ensure compliance with Kyverno."
date: 2025-09-26T10:00:00-00:00
lastmod: 2025-09-26T10:00:00-00:00
draft: false
tags: ["Chainguard Containers", "Overview", "Policy"]
images: []
weight: 010
toc: true
contentType: "integration"
---

[Kyverno](https://kyverno.io/) is an admission controller that enforces policies in Kubernetes clusters. This article describes how it can be leveraged to ensure resources follow best practices related to the use of Chainguard Containers.

## Prerequisites

To follow the examples in this guide, you will need the following:

- `kubectl` — the command line interface tool for Kubernetes — installed on your local machine.
- Administrative access to a Kubernetes cluster where [Kyverno is already installed](https://kyverno.io/docs/installation/).

## Ensure Images are Pulled from Allowed Repositories

You can use the [`ClusterPolicy` policy type](https://kyverno.io/docs/policy-types/cluster-policy/) to ensure that images are only pulled from a list of allowed repositories.

Create file named `restrict-image-registries.yaml` with the following content:

```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: restrict-image-registries
spec:
  rules:
    - name: validate-registries
      match:
        any:
          - resources:
              kinds:
                - Pod
      validate:
        failureAction: Enforce
        message: "Invalid image registry. Images must be hosted in cgr.dev."
        pattern:
          spec:
            =(ephemeralContainers):
              - image: "cgr.dev/*"
            =(initContainers):
              - image: "cgr.dev/*"
            containers:
              - image: "cgr.dev/*"
```

This defines a policy that only allows images hosted in `cgr.dev`. Note that if you've set up a different registry to function as [a pull-through cache for your Chainguard container images](/chainguard/chainguard-images/chainguard-registry/pull-through-guides/), you could replace this with your own registry.

If you need to support more than one registry, you can define multiple values with a pattern like `cgr.dev/* | your.internal.repo/*`.

Apply the policy with `kubectl`:

```shell
kubectl apply -f restrict-image-registries.yaml
```

To test that the policy works correctly, try to create a non-compliant pod:

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

This example manifest attempts to create a pod using a container image downloaded from the Docker Hub registry, not Chainguard's registry. As this output indicates, attempting to create a non-compliant pod results in an error, and the request is denied:

```output
Error from server: error when creating "STDIN": admission webhook "validate.kyverno.svc-fail" denied the request:

resource Pod/default/nginx-disallowed was blocked due to the following policies

restrict-image-registries:
  validate-registries: 'validation error: Invalid image registry. Images must be hosted
    in cgr.dev. rule validate-registries failed at path /spec/containers/0/image/'
```

To clean up, delete the policy:

```shell
kubectl delete -f restrict-image-registries.yaml
```

## Ensure Images are Referenced by Digest

Chainguard Containers are updated frequently to incorporate CVE fixes and package updates. The tags for Chainguard's container images are highly mutable, meaning that the underlying image changes frequently, even for very specific tags like `v1.2.3-r1`.

To prevent the risk of updates introducing breaking changes, you can [pull by digest](/chainguard/chainguard-images/how-to-use/container-image-digests/) to ensure the use of a specific image. When using Kyverno, you can use a `ClusterPolicy` policy to ensure that images are only referenced by digest.

Create `require-image-digest.yaml` with this content:

```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: require-image-digest
spec:
  rules:
    - name: require-image-digest
      match:
        any:
          - resources:
              kinds:
                - Pod
      validate:
        failureAction: Enforce
        message: "cgr.dev images must use digests."
        foreach:
          - list: "request.object.spec.containers[?starts_with(image, 'cgr.dev')]"
            pattern:
              image: "*@*"
          - list: "request.object.spec.?initContainers[?starts_with(image, 'cgr.dev')] || []"
            pattern:
              image: "*@*"
          - list: "request.object.spec.?ephemeralContainers[?starts_with(image, 'cgr.dev')] || []"
            pattern:
              image: "*@*"
```

This is a slightly more advanced example that only applies the rule to images hosted in `cgr.dev`. If you want to enforce this for any image in the cluster than you could simplify the `validate` section like this:

```yaml
validate:
  failureAction: Enforce
  message: "Images must use digests."
  pattern:
    spec:
      =(ephemeralContainers):
        - image: "*@*"
      =(initContainers):
        - image: "*@*"
      containers:
        - image: "*@*"
```

Apply the policy to the cluster:

```shell
kubectl apply -f require-image-digest.yaml
```

To test the policy, try to create a non-compliant pod:

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

This example attempts to create a pod using the `nginx` Chainguard container image, but does not pull the image by its digest as required by the policy. As the output indicates, the attempt resulted in an error and the request was denied:

```output
Error from server: error when creating "STDIN": admission webhook "validate.kyverno.svc-fail" denied the request:

resource Pod/default/nginx-disallowed was blocked due to the following policies

require-image-digest:
  require-image-digest: 'validation failure: validation error: cgr.dev images must
    use digests. rule require-image-digest failed at path /image/'
```

To clean up, delete the `require-image-digest` policy:

```shell
kubectl delete -f require-image-digest.yaml
```

## Verify Image Signatures

Chainguard signs all container images to ensure supply chain security and enable verification of image authenticity. These cryptographic signatures allow you to confirm that your container images come from Chainguard and haven’t been tampered with.

You can use a `verifyImages` rule in a `ClusterPolicy` to ensure that images are signed by Chainguard.

To begin, retrieve the IDs of the `catalog_syncer` and `apko_builder` identities for your organization as described [on this page](/chainguard/chainguard-images/how-to-use/verifying-chainguard-images-and-metadata-signatures-with-cosign/#chainguards-signing-identities).

Next, create `verify-image-signatures.yaml` with this content. Be sure to replace `<catalog-syncer-id>` and `<apko-builder-id>` with the appropriate values:

```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: verify-image-signatures
spec:
  webhookConfiguration:
    timeoutSeconds: 30
  rules:
    - name: verify-image-signatures
      match:
        any:
          - resources:
              kinds:
                - Pod
      verifyImages:
        - imageReferences:
            - "cgr.dev/*"
          failureAction: Enforce
          attestors:
            - entries:
                - keyless:
                    subjectRegExp: "^https://issuer.enforce.dev/(<catalog-syncer-id>|<apko-builder-id>)$"
                    issuer: "https://issuer.enforce.dev"
                    rekor:
                      url: https://rekor.sigstore.dev
```

Apply the policy to the cluster:

```shell
kubectl apply -f verify-image-signatures.yaml
```

To test the policy, try creating a pod using the public Chainguard `nginx` container image:

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

Public images in `cgr.dev/chainguard` are signed by different identities than the images in your organization. Therefore, this operation is blocked:

```output
Error from server: error when creating "STDIN": admission webhook "mutate.kyverno.svc-fail" denied the request:

resource Pod/default/nginx-disallowed was blocked due to the following policies

verify-image-signatures:
  verify-image-signatures: 'failed to verify image cgr.dev/chainguard/nginx:latest:
    .attestors[0].entries[0].keyless: subject mismatch: expected ^https://issuer.enforce.dev/(...|...)$,
    received https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main'
```

To clean up, delete the policy:

```shell
kubectl delete -f verify-image-signatures.yaml
```

## Audit First, Enforce Later

When introducing new policies into a cluster, it is a good idea to initially configure rules with [`failureAction: Audit`](https://kyverno.io/docs/policy-types/cluster-policy/validate/#failure-action) so as to avoid blocking existing workloads.

If you also set `spec.emitWarning: true`, users will receive a warning when they create a non-compliant resource, like the following example:

```output
Warning: policy require-chainguard-image-vendor.require-chainguard-image-vendor: validation failure: Only Chainguard Containers and images based on Chainguard Containers are allowed.
pod/nginx-disallowed created
```

This gives the user a signal that they should update their configuration without disrupting their deployment.

You can also find non-compliant resources that exist in the cluster by reviewing the [`PolicyReport` resources](https://kyverno.io/docs/policy-reports/) created by Kyverno:

```shell
kubectl get policyreport -o json | jq -r '.items[] | .metadata.ownerReferences as $resource | .results[] | select(.result == "fail") | {resource: $resource, result: .}'
```

```json
{
  "resource": [
    {
      "apiVersion": "v1",
      "kind": "Pod",
      "name": "nginx-disallowed",
      "uid": "56c269d6-3295-4484-9ac8-1969c99e89c0"
    }
  ],
  "result": {
    "message": "validation failure: Only Chainguard Containers and images based on Chainguard Containers are allowed.",
    "policy": "require-chainguard-image-vendor",
    "properties": {
      "process": "background scan"
    },
    "result": "fail",
    "rule": "require-chainguard-image-vendor",
    "scored": true,
    "source": "kyverno",
    "timestamp": {
      "nanos": 0,
      "seconds": 1758879437
    }
  }
}
```

Once all the failures have been addressed, you can switch to `failureAction: Enforce` and Kyverno will start to block the creation of resources that violate the policy.

## Learn More

By combining Kyverno with Chainguard Containers, you gain a powerful way to enforce security and compliance across your Kubernetes clusters. Kyverno ensures that only container images meeting your defined policies are deployed, while Chainguard Containers provide a minimal, hardened foundation to reduce risk from the start. Together, they help teams ship software more securely and confidently, without slowing down development.

If you'd like to learn more about Kyverno, we encourage you to refer to the [official documentation](https://kyverno.io/docs/).
