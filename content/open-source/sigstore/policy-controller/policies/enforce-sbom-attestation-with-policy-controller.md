---
title: "Enforce SBOM attestation with Policy Controller"
aliases:
- /open-source/sigstore/policy-controller/enforce-sbom-attestation-with-policy-controller/
type: "article"
description: "Enforce SBOM attestation with Policy Controller"
lead: "Enforce SBOM attestation with Policy Controller"
date: 2023-03-17T13:11:29+08:29
lastmod: 2024-05-10T13:11:29+08:29
draft: false
images: []
menu:
  docs:
    parent: "policy-controller"
weight: 006
toc: true
---

This guide demonstrates how to use the [Sigstore Policy Controller](https://docs.sigstore.dev/policy-controller/overview/) to verify image attestations before admitting an image into a Kubernetes cluster. In this guide, you will create a `ClusterImagePolicy` that checks the existence of a SBOM attestation attached to a container image, and then test the admission controller by running a `registry.enforce.dev/chainguard/node` image with SBOM attestations.

## Prerequisites

To follow along with this guide, you will need the following:

* A Kubernetes cluster with administrative access. You can set up a local cluster using [**kind**](https://kind.sigs.k8s.io/docs/user/quick-start/#installation) or use an existing cluster.
* **kubectl** — to work with your cluster. Install `kubectl` for your operating system by following the official [Kubernetes kubectl documentation](https://kubernetes.io/docs/tasks/tools/#kubectl).
* [Sigstore Policy Controller](https://docs.sigstore.dev/policy-controller/overview/) installed in your cluster. Follow our [How To Install Sigstore Policy Controller](/open-source/sigstore/policy-controller/how-to-install-policy-controller/) guide if you do not have it installed, and be sure to label any namespace that you intend to use with the `policy.sigstore.dev/include=true` label.

Once you have everything in place you can continue to the first step and confirm that the Policy Controller is working as expected.

## Step 1 - Checking the Policy Controller is Denying Admission

Before creating a `ClusterImagePolicy`, check that the Policy Controller is deployed and that your `default` namespace is labeled correctly. Run the following to check that the deployment is complete:

```bash
kubectl -n cosign-system wait --for=condition=Available deployment/policy-controller-webhook && \
kubectl -n cosign-system wait --for=condition=Available deployment/policy-controller-policy-webhook
```

When both deployments are finished, verify the `default` namespace is using the Policy Controller:

```
kubectl get ns -l policy.sigstore.dev/include=true
```

You should receive output like the following:

```
NAME      STATUS   AGE
default   Active   24s
```

Once you are sure that the Policy Controller is deployed and your `default` namespace is configured to use it, run a pod to make sure admission requests are handled and denied by default:

```bash
kubectl run --image k8s.gcr.io/pause:3.9 test
```

Since there is no `ClusterImagePolicy` defined yet, the Policy Controller will deny the admission request with a message like the following:

```
Error from server (BadRequest): admission webhook "policy.sigstore.dev" denied the request: validation failed: no matching policies: spec.containers[0].image
k8s.gcr.io/pause@sha256:7031c1b283388d2c2e09b57badb803c05ebed362dc88d84b480cc47f72a21097
```

In the next step, you will define a policy that verifies Chainguard Images have a SBOM attestation and apply it to your cluster.

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
  name: must-have-spdx-cue
  annotations:
    catalog.chainguard.dev/title: Enforce SBOM attestation
    catalog.chainguard.dev/description: Enforce a signed SPDX SBOM attestation from a custom key
    catalog.chainguard.dev/labels: attestation,cue
spec:
  images:
    - glob: "**"
  authorities:
    - name: my-authority
      keyless:
        identities:
          - issuer: "https://token.actions.githubusercontent.com"
            subject: "https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main"
      attestations:
        - name: must-have-spdx-attestation
          predicateType: https://spdx.dev/Document
          policy:
            type: cue
            data: |
              predicateType: "https://spdx.dev/Document"
```

The `glob: **` line, working in combination with the `authorities` and `policy` sections, will allow any image that has at least a SBOM attestation with predicate type `https://spdx.dev/Document` to be admitted into your cluster.

Save the file and then apply the policy:

```bash
kubectl apply -f /tmp/cip.yaml
```

You will receive output showing the policy is created:

```
clusterimagepolicy.policy.sigstore.dev/must-have-spdx-cue created
```

Now run the `k8s.gcr.io/pause:3.9` image which does not have a SBOM attestation:

```bash
kubectl run --image k8s.gcr.io/pause:3.9 noattestedimage
```

Since the image does not contain any attached SBOM, you will receive a message that the pod was rejected:

```
Error from server (BadRequest): admission webhook "policy.sigstore.dev" denied the request: validation failed: failed policy: demo: spec.containers[0].image
k8s.gcr.io/pause:3.9 no matching attestations with type https://spdx.dev/Document
```

Finally, we run `registry.enforce.dev/chainguard/node` image which contains a SBOM attestation of type `https://spdx.dev/Document`:

```bash
kubectl run --image registry.enforce.dev/chainguard/node mysbomattestedimage
```

Since the image has now a SBOM attestation, you will receive a message that the pod was created successfully:

```
pod/mysbomattestedimage created
```

Delete the pod once you're done experimenting with it:

```
kubectl delete pod mysbomattestedimage
```

To learn more about how the Policy Controller uses Cosign to verify and admit images, review the [Cosign](https://docs.sigstore.dev/cosign/overview/) Sigstore documentation.
