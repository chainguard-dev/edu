---
title: "Using Policy Controller to Verify Signed Chainguard Images"
type: "article"
description: "Using Policy Controller to Verify Signed Chainguard Images"
lead: "Verify Chainguard Images with Policy Controller"
date: 2023-02-22T13:11:29+08:29
lastmod: 2023-02-22T13:11:29+08:29
draft: false
images: []
menu:
  docs:
    parent: "policy-controller"
weight: 006
toc: true
terminalImage: policy-controller/base:latest
---

This guide demonstrates how to use the [Sigstore Policy Controller]([Sigstore Policy Controller](https://docs.sigstore.dev/policy-controller/overview/)) to verify image signatures for any [Chainguard Image](https://www.chainguard.dev/chainguard-images). To learn how to use the Policy Controller to enforce image signatures, you will create a `ClusterImagePolicy` that checks for a keyless Cosign signature on an image, and then test running a signed `nginx` image.

## Prerequisites

To follow along with this guide outside of the terminal that is embedded on this page, you will need the following:

* A Kubernetes cluster with administrative access. You can set up a local cluster using [**kind**](https://kind.sigs.k8s.io/docs/user/quick-start/#installation) or use an existing cluster.
* **kubectl** — to work with your cluster. Install `kubectl` for your operating system by following the official [Kubernetes kubectl documentation](https://kubernetes.io/docs/tasks/tools/#kubectl).
* [Sigstore Policy Controller](https://docs.sigstore.dev/policy-controller/overview/) installed in your cluster. Follow our [How To Install Sigstore Policy Controller](https://edu.chainguard.dev/open-source/sigstore/policy-controller/how-to-install-policy-controller/) guide if you do not have it installed, and be sure to label any namespace that you intend to use with the `policy.sigstore.dev/include=true` label.

If you are using the terminal that is embedded on this page, then all the prerequsites are installed for you.

Once you have everything in place you can continue to the next step and create a sample policy to check for signed Chainguard images.

## Step 1 - Checking the Policy Controller is Denying Admission

Before creating a `ClusterImagePolicy`, check that the Policy Controller is deployed and that your `default` namespace is labeled correctly. Run the following to check that the deployment is complete:

```bash
kubectl -n cosign-system wait --for=condition=Available deployment/policy-controller-webhook && \
kubectl -n cosign-system wait --for=condition=Available deployment/policy-controller-policy-webhook
```

When both deployments are finished, verify the `default` namespace is using the Policy Controller:

```
k get ns -l policy.sigstore.dev/include=true
```

You should receive output like the following:

```
NAME      STATUS   AGE
default   Active   24s
```

Once you are sure that the Policy Controller is deployed and your `default` namespace is configured to use it, run a pod to make sure admission requests are handled and denied by default:

```bash
kubectl run --image cgr.dev/chainguard/nginx:latest nginx
```

Since there is no `ClusterImagePolicy` defined yet, the Policy Controller will deny the admission request with a message like the following:

```
Error from server (BadRequest): admission webhook "policy.sigstore.dev" denied the request: validation failed: no matching policies: spec.containers[0].image
cgr.dev/chainguard/nginx@sha256:628a01724b84d7db2dc3866f645708c25fab8cce30b98d3e5b76696291d65c4a
```

In the next step you will define a policy that verifies Chainguard images are signed and apply it to your cluster.

## Step 2 — Creating a `ClusterImagePolicy`

Now that you have the Policy Controller running in your cluster, and have the `default` namespace configured to use it, you can now define a `ClusterImagePolicy` to admit images.

Open a new file with `nano` or your preferred editor:

```shell
nano /tmp/cip.yaml
```

Copy the following policy to the `/tmp/cip.yaml` file:

```yaml
# Copyright 2022 Chainguard, Inc.
# SPDX-License-Identifier: Apache-2.0

apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: chainguard-images-are-signed
  annotations:
    catalog.chainguard.dev/title: Chainguard Images
    catalog.chainguard.dev/description: Enforce Chainguard images are signed
    catalog.chainguard.dev/labels: chainguard
spec:
  images:
    - glob: cgr.dev/chainguard/**
  authorities:
    - keyless:
        url: https://fulcio.sigstore.dev
        identities:
          - issuer: https://token.actions.githubusercontent.com
            subject: https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main
      ctlog:
        url: https://rekor.sigstore.dev
```

The `glob: cgr.dev/chainguard/**` line in combination with the `authorities` section will allow any image in the `cgr.dev/chainguard` image registry that has a [keyless signature](https://docs.sigstore.dev/cosign/keyless/) to be admitted into your cluster.

Save the file and then apply the policy:

```bash
kubectl apply -f /tmp/cip.yaml
```

You will receive output showing the policy is created:

```
clusterimagepolicy.policy.sigstore.dev/chainguard-images-are-signed created
```

Now run the `cgr.dev/chainguard/nginx:latest` image again:

```bash
kubectl run --image cgr.dev/chainguard/nginx:latest nginx
```

Since the image matches the policy, you will receive a message that the pod was created successfully:

```
pod/nginx created
```

Delete the pod once you're done experimenting with it:

```
kubectl delete pod nginx
```

To learn more about how the Policy Controller uses Cosign to verify and admits images, review the [Cosign](https://docs.sigstore.dev/cosign/overview/) Sigstore documentation.

## Options for Continuous Verification

While it is useful to use the Policy Controller to manage admission into a cluster, once a workload is running any vulnerability or policy violations that occur after containers are running will not be detected.

[Chainguard Enforce](/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/understanding-continuous-verification/) is designed to address this issue by continuously verifying whether a container or cluster contains any vulnerabilities or policy violations over time. This includes what packages are deployed, SBOMs (software bills of materials), provenance, signature data, and more.

If you're interested in learning more about Chainguard Enforce, you can request access to the product by selecting **Chainguard Enforce for Kubernetes** on the [inquiry form](https://www.chainguard.dev/get-demo?utm_source=docs).