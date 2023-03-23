---
title : "Agent Installation Requirements"
description: "Chainguard Enforce Agent Installation Requirements"
type: "article"
date: 2023-03-22 13:21:51 +0000 UTC
draft: false
images: []
weight: 799
---

The Chainguard Enforce Agent is installed into each of your Kubernetes clusters as a `StatefulSet` consisting of 2 pod relicas in their own namespace called `gulfstream`. The Enforce Agent is a statically compiled binary, requires minimal system resources,  and can be installed using a variety of tools. It supports a number of different Certified Kubernetes distributions and versions.

If you are using a managed GKE or EKS cluster, consider installing Enforce in agentless (also referred to as SaaS) mode by following this guide: [Set Up Chainguard Enforce Cloud Account Associations](https://edu.chainguard.dev/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/cloud-account-associations/). This installation method also supports additional workload discovery like Google Cloud Run, AWS ECS, and AWS AppRunner, and does not consume any resources in your Kubernetes clusters.

## Supported Kubernetes Versions

Enforce is supported for the current stable set of Kubernetes [point releases](https://kubernetes.io/releases/), as well as versions that are within the upstream [support period](https://kubernetes.io/releases/patch-releases/#support-period).

## Agent Resource Requirements

The Chainguard Enforce Agent uses the following Kubernetes resource requests and limits:


|            |CPU     |Memory |
|------------|--------|-------|
|**Requests**|     50m|   50Mi|
|**Limits**  |       1| 1000Mi|

Note that pods can use more resources than requested, but will not exceed the specified limits. As a general benchmark, an Enforce Agent pod handling 40 requests per second will consume 250-300MB of RAM.

## Private Cluster Requirements

The Chainguard Enforce Agent is required when running Enforce with private Kubernetes clusters, or when using managed GKE or EKS clusters that do not have exposed public API endpoints (the latter are also considered private to Enforce). 

### Network Access

The Enforce Agent running in either scenario must be able to reach our public Enforce SaaS endpoints. Refer to the Enforce [Network Requirements](https://edu.chainguard.dev/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/network-requirements/#cidr-ranges) page for a list of CIDR ranges to add to your firewalls.

### Service Accounts

Clusters using the Enforce Agent are required to have [Service Account Token Volume Projection](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#service-account-token-volume-projection) and [Service Account Issuer Discovery](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#service-account-issuer-discovery) enabled.

Consult our [Connect Kubernetes Clusters to Enforce](https://edu.chainguard.dev/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/how-to-connect-kubernetes-clusters/#chainguard-enforce-agent) page for details on how to validate your cluster configuration supports these service account settings.

### Limitations of Private Clusters

When running in private clusters, the agent needs to be re-installed under two circumstances:

* If the service account issuer signing key is rotated
* At least every 25 days

This is accomplished by running `chainctl cluster install --private` once again.

## Installing Enforce Agent 

To install the Enforce Agent, you can use one of the following supported methods depending on your infrastructure configuration.

### chainctl

You can use [chainctl](https://edu.chainguard.dev/chainguard/chainguard-enforce/chainctl-docs/), which is a CLI tool to interact with, query, and manage Enforce in your clusters.

For more details on how to use `chainctl` to install Enforce consult our [Enforce Installation with `chainctl`](https://edu.chainguard.dev/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/alternative-installation-methods/#install-with-chainctl) page.

### YAML

You can also install Enforce Agent using YAML manifests directly. Consult the [Declarative Option 1 — Install with YAML](https://edu.chainguard.dev/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/alternative-installation-methods/#declarative-option-1--install-with-yaml) section of the Installation guide to determine which method of generating the required YAML files is appropriate for your environment.

### Helm

The Enforce Agent can also be installed using a [Helm chart](https://edu.chainguard.dev/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/alternative-installation-methods/#declarative-option-2--install-with-a-helm-chart). As noted on that page, if you choose this method, be sure to include the additional `auth:` fields as part of your `values.yaml` file.

## Supported Kubernetes Versions Matrix

The Enforce agent is known to work with the following Kubernetes versions and configurations:

|Provider      |Kubernetes Version|CPU Arch|Runtime|
|--------------|------------------|--------|-------|
| AWS (EKS)    | 1.22, 1.23, 1.24, 1.25, 1.26 | x86_64 |containerd|
| Google (GKE) | 1.22, 1.23, 1.24, 1.25, 1.26 | x86_64 |gVisor, containerd |
| Kubernetes (upstream) | 1.22, 1.23, 1.24, 1.25, 1.26 | x86_64 |gVisor, containerd |