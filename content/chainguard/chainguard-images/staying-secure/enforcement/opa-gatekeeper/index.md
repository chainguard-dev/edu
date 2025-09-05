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

Note that  you may not be able to control where images provided by the platform are hosted in certain managed Kubernetes solutions.

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
```txt
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


## Learn More

By combining OPA Gatekeeper with Chainguard container images, you gain a powerful way to enforce security and compliance across your Kubernetes clusters. Gatekeeper ensures that only container images meeting your defined policies are deployed, while Chainguard Containers provide a minimal, hardened foundation to reduce risk from the start. Together, they help teams ship software more securely and confidently, without slowing down development.

If you'd like to learn more about Gatekeeper, we encourage you to refer to the [official documentation](https://open-policy-agent.github.io/gatekeeper/website/docs/).
