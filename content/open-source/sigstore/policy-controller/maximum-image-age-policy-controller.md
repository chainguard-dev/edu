---
title: "Maximum container image age with Policy Controller"
type: "article"
description: "Maximum container image age with Policy Controller"
lead: "Maximum container image age with Policy Controller"
date: 2023-03-02T13:11:29+08:29
lastmod: 2023-03-02T13:11:29+08:29
draft: false
images: []
menu:
  docs:
    parent: "policy-controller"
weight: 006
toc: true
terminalImage: policy-controller/base:latest
---

This guide demonstrates how to use the [Sigstore Policy Controller](https://docs.sigstore.dev/policy-controller/overview/) to verify image signatures before admitting an image into a Kubernetes cluster. In this guide, you will create a `ClusterImagePolicy` that checks the maximum age of a container image verifying that isn’t older than 30 days. For that, we’ll attempt to create two distroless images one older than 30 days and a fresh one.

## Prerequisites

To follow along with this guide outside of the terminal that is embedded on this page, you will need the following:

* A Kubernetes cluster with administrative access. You can set up a local cluster using [**kind**](https://kind.sigs.k8s.io/docs/user/quick-start/#installation) or use an existing cluster.
* **kubectl** — to work with your cluster. Install `kubectl` for your operating system by following the official [Kubernetes kubectl documentation](https://kubernetes.io/docs/tasks/tools/#kubectl).
* [Sigstore Policy Controller](https://docs.sigstore.dev/policy-controller/overview/) installed in your cluster. Follow our [How To Install Sigstore Policy Controller](https://edu.chainguard.dev/open-source/sigstore/policy-controller/how-to-install-policy-controller/) guide if you do not have it installed, and be sure to label any namespace that you intend to use with the `policy.sigstore.dev/include=true` label.

If you are using the terminal that is embedded on this page, then all the prerequisites are installed for you. Note that it may take a minute or two for the Kubernetes cluster to finish provisioning. If you receive any errors while running commands, retry them after waiting a few seconds.

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
kubectl run --image ghcr.io/distroless/static myoldimage
```

Since there is no `ClusterImagePolicy` defined yet, the Policy Controller will allow the admission request.

In the next step, you will define a policy that verifies Chainguard Images has an age below 30days and apply it to your cluster.

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
  name: maximum-image-age-rego
  annotations:
    catalog.chainguard.dev/title: Maximum image age
    catalog.chainguard.dev/description: |
      This checks that the maximum age an image is allowed to
      have is 30 days old.  This is measured using the container
      image's configuration, which has a "created" field.

      Some build tools may fail this check because they build
      reproducibly, and use a fixed date (e.g. the Unix epoch)
      as their creation time, but many of these tools support
      specifying SOURCE_DATE_EPOCH, which aligns the creation
      time with the date of the source commit.

    catalog.chainguard.dev/labels: rego
spec:
  images: [{ glob: "**" }]
  authorities: [{ static: { action: pass } }]
  mode: enforce
  policy:
    fetchConfigFile: true
    type: "rego"
    data: |
      package sigstore

      nanosecs_per_second = 1000 * 1000 * 1000
      nanosecs_per_day = 24 * 60 * 60 * nanosecs_per_second

      # Change this to the maximum number of days to allow.
      maximum_age = 30 * nanosecs_per_day

      isCompliant[response] {
        created := time.parse_rfc3339_ns(input.config[_].created)

        response := {
          "result" : time.now_ns() < created + maximum_age,
          "error" : "Image exceeds maximum allowed age."
        }
      }
```

The `glob: **` line, working in combination with the `authorities` and `policy` sections, will allow any image that has been built in the last 30 days to be admitted into your cluster.

The `fetchConfigFile` options instruct the Policy Controller to check the image configuration looking for the age of the image. The rest of fields are:

* `authorities`: this setting tells the Policy Controller to skip any verification looking for the presence of an image signature.
* `mode`: this blocks the creation of any image older than 30days.
* `policy.data`: contains the rego policy itself that verifies when the image has been created.

Save the file and then apply the policy:

```bash
kubectl apply -f /tmp/cip.yaml
```

You will receive output showing the policy is created:

```
clusterimagepolicy.policy.sigstore.dev/maximum-image-age-rego created
```

Now run the `cgr.dev/chainguard/static` image again:

```bash
kubectl run --image cgr.dev/chainguard/static mydailyfreshimage
```

Since the image is built on daily basis, you will receive a message that the pod was created successfully:

```
pod/mydailyfreshimage created
```

However, if we now create a pod using our old image `myoldimage`, PolicyController rejects the admission request with a message like the following:

```
Error from server (BadRequest): admission webhook "policy.sigstore.dev" denied the request: validation failed: ghcr.io/distroless/static@sha256:a9650a15060275287ebf4530b34020b8d998bd2de9aea00d113c332d8c41eb0b failed evaluating rego policy for type ClusterImagePolicy: policy is not compliant for query 'isCompliant = data.sigstore.isCompliant' with errors: Image exceeds maximum allowed age.
```

Delete the pod once you're done experimenting with it:

```
kubectl delete pod mydailyfreshimage
```

To learn more about how the Policy Controller uses Cosign to verify and admit images, review the [Cosign](https://docs.sigstore.dev/cosign/overview/) Sigstore documentation.

## Options for Continuous Verification

While it is useful to use the Policy Controller to manage admission into a cluster, once a workload is running any vulnerability or policy violations that occur after containers are running will not be detected.

[Chainguard Enforce](/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/understanding-continuous-verification/) is designed to address this issue by continuously verifying whether a container or cluster contains any vulnerabilities or policy violations over time. This includes what packages are deployed, SBOMs (software bills of materials), provenance, signature data, and more.

If you're interested in learning more about Chainguard Enforce, you can request access to the product by selecting **Chainguard Enforce for Kubernetes** on the [inquiry form](https://www.chainguard.dev/get-demo?utm_source=docs).
