---
title: "Enforcement with OPA Gatekeeper"
linktitle: "OPA Gatekeeper"
type: "article"
description: "How to enforce best practices and ensure compliance with OPA Gatekeeper."
date: 2025-09-02T10:00:00-00:00
lastmod: 2025-09-02T10:00:00-00:00
draft: false
tags: ["Chainguard Containers"]
images: []
weight: 005
toc: true
---

[Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/) is an
admission controller that enforces policies in Kubernetes clusters. This
article describes how it can be leveraged to ensure resources follow best
practices related to the use of Chainguard Containers.

## Prerequisites

To follow the examples in this guide, you will need the following:
- `kubectl` - the command line interface tool for Kubernetes.
- Administrative access to a Kubernetes cluster where [OPA Gatekeeper is
  already installed](https://open-policy-agent.github.io/gatekeeper/website/docs/install).

## Ensure Images are Pulled From Allowed Repositories

You can use the `K8sAllowedReposV2` constraint from the [Gatekeeper
Library](https://github.com/open-policy-agent/gatekeeper-library) to
ensure that images are only pulled from a list of allowed repositories.

Firstly, add the template to your cluster.

```shell
kubectl create -f https://raw.githubusercontent.com/open-policy-agent/gatekeeper-library/refs/heads/master/library/general/allowedreposv2/template.yaml
```

Then, create a constraint that only allows images hosted in `cgr.dev`. If you
are mirroring Chainguard images into your own registries then you could replace
this with your own URLs.

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
    # In certain managed Kubernetes solutions, you may not be able to control
    # where images provided by the platform are hosted.
    excludedNamespaces:
      - "kube-system"
  parameters:
    allowedImages:
      - "cgr.dev/*"
EOF
```

You should receive an error when you try to create a non-compliant pod.

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

```txt
Error from server (Forbidden): error when creating "STDIN": admission webhook "validation.gatekeeper.sh" denied the request: [repo-is-cgr-dev] container <nginx> has an invalid image <nginx>, allowed images are ["cgr.dev/*"]
```

## Ensure Images are Referenced By Digest

Chainguard Containers are updated frequently to incorporate CVE fixes and
package updates. The tags are highly mutable, meaning that the underlying image
changes frequently, even for very specific tags like `v1.2.3-r1`.

To prevent the risk of updates introducing breaking changes, you can pull by
digest to ensure the use of a specific image.

The `K8sImageDigests` constraint from the [Gatekeeper
Library](https://github.com/open-policy-agent/gatekeeper-library) can be used to
mandate this practice inside a Kubernetes cluster.

Firstly, add the template to your cluster.

```shell
kubectl create -f https://raw.githubusercontent.com/open-policy-agent/gatekeeper-library/refs/heads/master/library/general/imagedigests/template.yaml
```

Then, create the constraint.

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
    # In certain managed Kubernetes solutions, you may not be able to control
    # whether images provided by the platform are referenced by digest.
    excludedNamespaces:
      - "kube-system"
EOF
```

You should receive an error when you try to create a non-compliant pod.

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

## Warn First, Deny Later

When introducing new constraints into a cluster, it is a good idea to configure
them with [`enforcementAction:
warn`](https://open-policy-agent.github.io/gatekeeper/website/docs/violations/#warn-enforcement-action)
initially to avoid blocking existing workloads.

Then, when a user creates a non-compliant resource, they will get a warning like
this one, giving them a signal that they should update their configuration.

```
Warning: [container-image-must-have-digest] container <nginx> uses an image without a digest <cgr.dev/chainguard/nginx>
```

You can also find non-compliant resources that exist in the cluster by looking
at the constraint's violations.

```shell
kubectl get k8simagedigests container-image-must-have-digest -o json | jq -r '.status.violations[]'
```

```json
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

Once all the violations have been addressed, you can remove `enforcementAction:
warn` and Gatekeeper will start to block the creation of resources that violate
the constraint.

## Learn more

If you'd like to learn more about Gatekeeper, we encourage you to refer to the
[official
documentation](https://open-policy-agent.github.io/gatekeeper/website/docs/).
