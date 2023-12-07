---
title: "Configuring Enforcer Options"
linktitle: "Enforcer Options"
aliases:
- /chainguard/chainguard-enforce/chainguard-enforce-kubernetes/configure-enforcer-options-during-installation/
- /chainguard/chainguard-enforce/reference/configure-enforcer-options-during-installation/
type: "article"
lead: ""
description: "Installing Chainguard with chainctl configuring your Enforcer Options"
draft: false
tags: ["Enforce", "Product", "Procedural"]
images: []
menu:
  docs:
    parent: "installation"
weight: 20
toc: true
---

There is currently a limited list of enforcer options that can be configured when installing Chainguard into a current Kubernetes cluster. This guide will walk you through each of these Enforcer configuration settings.

Our [getting started guide](/chainguard/chainguard-enforce/chainguard-enforce-user-onboarding/) provides more detailed information on how to set up Chainguard Enforce, and this document provides a reference on how to configure different behaviors for your cluster.

We will use `chainctl`, the command line tool for working with Chainguard products, which you can install using our [installation guide](/chainguard/chainguard-enforce/how-to-install-chainctl/).

## Enforcer Options

The list of available Enforcer options are detailed below:

* `webhook_fail_open`: is a flag to enable/disable a fail open behavior for the Enforcer webhooks. Default is set to `false`.
* `enable_cip_cache`: is a flag to enable/disable cluster image policy (CIP) caching. Default is set to `false`.
* `namespace_enforcement_mode`: defines the behavior of the Enforcer webhook's label selector. This option accepts two possible values: `opt-out` and `opt-in`. `opt-in` sets a behavior to the Enforcer webhooks where only labeled (`policy.sigstore.dev/include=true`) namespaces will be verified to enforce the defined policies. `opt-out` sets an opposite behavior to the Enforcer webhooks where only labeled (`policy.sigstore.dev/exclude=true`) namespaces will be **excluded** from any verification related to the defined policies. Default is set to `opt-in`.

## Install with `chainctl`

To install with `chainctl`, first authenticate into `chainctl` before running a command.

```sh
chainctl auth login
```

With your cluster already set up, you'll install the Chainguard Enforce Agent with `chainctl` and use the flag `--opt` to set any of your Enforcer specific settings.

For this example on GKE, EKS, or AKS cloud infrastructure, we enable our cluster webhook to fail open by using the next command.

```sh
chainctl cluster install --group=$GROUP_ID --context $CLUSTER --opt=webhook_fail_open=true
```

In this next example using a _private_ or on-prem cluster, we configure our Chainguard cluster to enable the cluster image policy (CIP) cache and a failing open behavior for the Enforce webhooks.

```sh
chainctl cluster install --group=$GROUP_ID --private --context $CLUSTER --opt=webhook_fail_open=true --opt=enable_cip_cache=true
```

Be sure to replace the `$GROUP_ID` and `$CLUSTER` variables with the appropriate [IAM Group ID](/chainguard/chainguard-enforce/iam-groups/how-to-manage-iam-groups-in-chainguard-enforce/), and name of your Kubernetes cluster, respectively.

If you would like more detail about installing the Chainguard Enforce Agent with `chainctl`, or on getting onboarded to Chainguard Enforce, check out our [Getting Started guide](/chainguard/chainguard-enforce/chainguard-enforce-user-onboarding/).

## Next Steps

With Chainguard installed in your cluster, continue learning about Enforce by reading the [Getting Started Guide](/chainguard/chainguard-enforce/chainguard-enforce-user-onboarding/), learn how to [manage policies with `chainctl`](/chainguard/chainguard-enforce/policies/chainguard-policies-cli/), or follow the tutorial on [how to detect the Log4Shell vulnerability with Enforce](/chainguard/chainguard-enforce/concepts/detect-log4shell-demo/).