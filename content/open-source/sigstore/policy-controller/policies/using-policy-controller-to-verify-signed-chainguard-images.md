---
title: "Verify Signed Chainguard Images"
aliases:
- /open-source/sigstore/policy-controller/using-policy-controller-to-verify-signed-chainguard-images/
type: "article"
description: "Using Policy Controller to Verify Signed Chainguard Images"
lead: "Verify Chainguard Images with Policy Controller"
date: 2023-02-22T13:11:29+08:29
lastmod: 2024-05-10T13:11:29+08:29
draft: false
tags: ["policy-controller", "Procedural", "Policy", "Chainguard Images"]
images: []
menu:
  docs:
    parent: "policy-controller"
weight: 006
toc: true
---

This guide demonstrates how to use the [Sigstore Policy Controller](https://docs.sigstore.dev/policy-controller/overview/) to verify image signatures before admitting an image into a Kubernetes cluster. In this guide, you will create a `ClusterImagePolicy` that checks for a keyless Cosign image signature, and then test the admission controller by running a signed `nginx` image.

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
kubectl run --image cgr.dev/chainguard/nginx:latest nginx
```

Since there is no `ClusterImagePolicy` defined yet, the Policy Controller will deny the admission request with a message like the following:

```
Error from server (BadRequest): admission webhook "policy.sigstore.dev" denied the request: validation failed: no matching policies: spec.containers[0].image
cgr.dev/chainguard/nginx@sha256:628a01724b84d7db2dc3866f645708c25fab8cce30b98d3e5b76696291d65c4a
```

In the next step, you will define a policy that verifies Chainguard Images are signed and apply it to your cluster.

## Step 2 — Creating a `ClusterImagePolicy`

Now that you have the Policy Controller running in your cluster, and have the `default` namespace configured to use it, you can now define a `ClusterImagePolicy` to admit images.

Open a new file with `nano` or your preferred editor:

```shell
nano /tmp/cip.yaml
```

Copy the following policy to the `/tmp/cip.yaml` file:

```yaml
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

The `glob: cgr.dev/chainguard/**` line, working in combination with the `authorities` section, will allow any image in the `cgr.dev/chainguard` image registry that has a [keyless signature](https://docs.sigstore.dev/signing/overview/) to be admitted into your cluster.

The `- keyless` options instruct the Policy Controller what to check for when it examines the signature on any image from the `cgr.dev/chainguard` registry. The specific fields are:

* `url`: this setting tells the Policy Controller where to find the Certificate Authority (CA) that issued an image signature.
* `issuer`: the [issuer field](https://github.com/sigstore/fulcio/blob/main/docs/oid-info.md#1361415726411--issuer) contains the URI of the OpenID Connect (OIDC) Identity Provider that digitally signed the identity token.
* `subject`: the [subject field](https://github.com/sigstore/fulcio/blob/main/docs/certificate-specification.md#issued-certificate) must contain a URI or an email address that identifies where the signed image originated.
* `ctlog`: this setting tells the Policy Controller which [Certificate Transparency log](/open-source/sigstore/rekor/an-introduction-to-rekor/#transparency-log) to query when it is validating a signature.

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

In the background, the Policy Controller queries the specified `ctlog` from the policy that you created to find a record in the log that matches the image being requested (`cgr.dev/chainguard/nginx:latest`). The Policy Controller ensures that the SHA256 hash of the image matches the hash that is recorded in the certificate issued by the OIDC `issuer` when the image was first signed. Finally, the Policy Controller verifies the issued certificate was signed by the specified Certiciate Authority's (`https://fulcio.sigstore.dev`) root signing certificate. Once the Policy Controller verifies the signature of the image's hash in the transparency log matches the computed hash of the image, and the certificate's validity based on the CA chain of trust, it will admit the pod into the cluster.

Delete the pod once you're done experimenting with it:

```
kubectl delete pod nginx
```

To learn more about how the Policy Controller uses Cosign to verify and admit images, review the [Cosign](https://docs.sigstore.dev/cosign/overview/) Sigstore documentation.
