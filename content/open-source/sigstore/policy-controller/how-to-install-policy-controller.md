---
title: "How to Install Sigstore Policy Controller"
type: "article"
description: "Install the Sigstore Policy Controller into a Kubernetes Cluster"
lead: "Installing Sigstore Policy Controller"
date: 2023-02-21T13:11:29+08:29
lastmod: 2023-02-21T13:11:29+08:29
draft: false
images: []
menu:
  docs:
    parent: "policy-controller"
weight: 005
toc: true
terminalImage: policy-controller/install:latest
---

The [Sigstore Policy Controller](https://docs.sigstore.dev/policy-controller/overview/) is a Kubernetes [admission controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) that can verify image signatures and policies. You can define policies using the [CUE](https://cuelang.org/) or [Rego](https://www.openpolicyagent.org/docs/latest/policy-language/) policy languages.

This guide will demonstrate how to install the Policy Controller in your Kubernetes cluster and enable policy enforcement.

## Prerequisites

To follow along with this guide outside of the terminal that is embedded on this page, you will need the following:

* A Kubernetes cluster with administrative access. You can set up a local cluster using [**kind**](https://kind.sigs.k8s.io/docs/user/quick-start/#installation) or use an existing cluster.
* **kubectl** — to work with your cluster. Install `kubectl` for your operating system by following the official [Kubernetes kubectl documentation](https://kubernetes.io/docs/tasks/tools/#kubectl).
* The [Helm](https://helm.sh) command line tool to install the Policy Controller.

If you are using the terminal that is embedded on this page, then all the prerequsites are installed for you.

Once you have everything in place you can continue to the next step and install the Policy Controller.

## Step 1 — Creating the `cosign-system` Kubernetes Namespace

The first step that you need to complete is to create a Kubernetes `namespace` for the Policy Controller to run in. Call it `cosign-system` and run the following command to create it:

```bash
kubectl create namespace cosign-system
```

Now you can move on to the next step, which is installing the Policy Controller into the namespace you just created.

## Step 2 — Installing the Policy Controller

In this step we'll use the `helm` command line tool to install the Policy Controller.

First, add the [Sigstore Helm Repository](https://sigstore.github.io/helm-charts) to your system with the following command:

```bash
helm repo add sigstore https://sigstore.github.io/helm-charts
```

You should receive output like this:

```
"sigstore" has been added to your repositories
```

Next, update your local Helm repository information using the `helm repo update` comand:

```bash
helm repo update
```

You'll receive output like the following:

```
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "sigstore" chart repository
Update Complete. ⎈Happy Helming!⎈
```

Now install the Policy Controller into the `cosign-system` namespace that you created in the first step of this guide:

```bash
helm install policy-controller -n cosign-system sigstore/policy-controller --devel
```

The `--devel` flag will include any alpha, beta, or release candidate versions of a chart. You can specify a particular version with the `--version` flag if you prefer.

It may take a few minutes for your cluster to deploy all of the manifests needed for the Policy Controller. Check the status of your cluster using the `kubectl wait` command like this:

```bash
kubectl -n cosign-system wait --for=condition=Available deployment/policy-controller-webhook && \
kubectl -n cosign-system wait --for=condition=Available deployment/policy-controller-policy-webhook
```

Once the Policy Controller deployments are done you will receive output like the following:

```
deployment.apps/policy-controller-webhook condition met
deployment.apps/policy-controller-policy-webhook condition met
```

A full list of the resources that the Policy Controller deploys into your cluster is available at the end of this guide in [Appendix 1 — Resource Types](#appendix-1--resource-types).

You have now deployed the Policy Controller into your cluster. The next step is to enable it for the namespaces that you want to enforce policies in.

## Step 3 — Enabling the Policy Controller

Now that you have the Policy Controller installed into your cluster, the next step is to decide which namespaces should use it. By default, namespaces must opt-in to enforcement, so you will need to label any namespace that you will use with the Policy Controller.

Run the following command to include the `default` namespace in image validation and policy enforcement:

```bash
kubectl label namespace default policy.sigstore.dev/include=true
```

Apply the same label to any other namespace that you want to use with the Policy Controller.

Now you can test enforcement by running a sample pod:

```bash
kubectl run --image cgr.dev/chainguard/nginx:latest nginx
```

The Policy Controller will deny the admission request with a message like the following:

```
Error from server (BadRequest): admission webhook "policy.sigstore.dev" denied the request: validation failed: no matching policies: spec.containers[0].image
cgr.dev/chainguard/nginx@sha256:628a01724b84d7db2dc3866f645708c25fab8cce30b98d3e5b76696291d65c4a
```

## Continuous Verification with Chainguard Enforce

While it is useful to use the Policy Controller to manage admission into a cluster, once a workload is running any vulnerability or policy violations that occur after containers are running will not be detected.

[Chainguard Enforce](/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/understanding-continuous-verification/) is designed to address this issue by continuously verifying whether a container or cluster contains any vulnerabilities or policy violations over time. This includes what packages are deployed, SBOMs (software bills of materials), provenance, signature data, and more.

If you're interested in learning more about Chainguard Enforce, you can request access to the product by selecting **Chainguard Enforce for Kubernetes** on the [inquiry form](https://www.chainguard.dev/get-demo?utm_source=docs).

## Appendix 1 — Resource Types

A complete Policy Controller installation consists of the following resources in a cluster:

| Type |Name |
|----------|-----|
| ClusterRole                    | `policy-controller-policy-webhook` |
|                                | `policy-controller-webhook` |
| ClusterRoleBinding             | `policy-controller-policy-webhook` |
|                                | `policy-controller-webhook` |
| ConfigMap                      | `config-image-policies` |
|                                | `config-policy-controller` |
|                                | `policy-controller-policy-webhook-logging` |
|                                | `policy-controller-webhook-logging` |
| CustomResourceDefinition       | `clusterimagepolicies.policy.sigstore.dev` |
| Deployment                     | `policy-controller-policy-webhook` |
|                                | `policy-controller-webhook` |
| MutatingWebhookConfiguration   | `defaulting.clusterimagepolicy.sigstore.dev` |
|                                | `policy.sigstore.dev` |
| Role                           | `policy-controller-policy-webhook` |
|                                | `policy-controller-webhook` |
| RoleBinding                    | `policy-controller-policy-webhook` |
|                                | `policy-controller-webhook` |
| Secret                         | `policy-webhook-certs` |
|                                | `webhook-certs` |
| Service                        | `policy-webhook` |
|                                | `policy-controller-policy-webhook-metrics` |
|                                | `policy-controller-webhook-metrics` |
|                                | `webhook` |
| ServiceAccount                 | `policy-controller-policy-webhook` |
|                                | `policy-controller-webhook` |
| ValidatingWebhookConfiguration | `validating.clusterimagepolicy.sigstore.dev` |
|                                | `policy.sigstore.dev` |
