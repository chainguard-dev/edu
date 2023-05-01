---
title: "Installing the Chainguard Enforce Agent"
linktitle: "Installation"
aliases:
- /chainguard/chainguard-enforce/chainguard-enforce-kubernetes/alternative-installation-methods/
type: "article"
lead: ""
description: "Installing the Chainguard Enforce Agent with chainctl, YAML, Helm"
date: 2022-11-04T15:56:52-07:00
lastmod: 2022-12-20T15:56:52-07:00
draft: false
tags: ["Enforce", "Product", "Procedural"]
images: []
menu:
  docs:
    parent: "chainguard-enforce"
weight: 010
toc: true
---

> _This document relates to Chainguard Enforce. In order to follow along, you will need access to Chainguard Enforce. You can request access through selecting **Chainguard Enforce** on the [inquiry form](https://www.chainguard.dev/contact?utm_source=docs)._

There are currently three recommended approaches to installing the Chainguard Enforce Agent. This guide will walk you through each of these approaches.

Our [getting started guide](/chainguard/chainguard-enforce/chainguard-enforce-user-onboarding/) provides more detailed information on how to set up Chainguard Enforce, and this document provides a reference for three alternative methods to align best with your team's existing Kubernetes workflow.

Our first method will be installation with `chainctl`, the command line tool for working with Chainguard products.

The second two methods are two approaches to declarative installs, which define the entirety of the Chainguard Enforce Agent resources as static Kubernetes manifests. Static manifests created for declarative installs allow for greater flexibility for how they're ultimately applied to the cluster, and can be adapted to fit most Kubernetes deployment workflows. These two examples we'll be covering are installation via "raw" YAML, and via a Helm Chart.

## Prerequisites

You'll need access to Chainguard Enforce (sign up via the [inquiry form](https://www.chainguard.dev/contact?utm_source=docs)), with a group and cluster already set up.

Regardless of the method you choose, you'll need `chainctl` installed, which you can achieve by following our [How to Install `chainctl` tutorial](/chainguard/chainguard-enforce/how-to-install-chainctl/).

## Install with `chainctl`

To install with `chainctl`, first authenticate into `chainctl` before running a command.

```sh
chainctl auth login
```

With your cluster already set up, you'll install the Chainguard Enforce Agent with `chainctl`. For GKE, EKS, and AKS cloud infrastructure, use the next command.

```sh
chainctl cluster install --group=$GROUP_ID --context $CLUSTER
```

If you are using a _private_ or on-prem cluster, run the command  with the `--private` flag as in the next command.

```sh
chainctl cluster install --group=$GROUP_ID --private --context $CLUSTER
```

Be sure to replace the `$GROUP_ID` and `$CLUSTER` variables with the appropriate IAM Group ID, and name of your Kubernetes cluster, respectively. To check the ID of your Chainguard Enforce group(s), you can list out relevant groups and thier IDs in a table.

```sh
chainctl iam groups ls -o table
```

The output will display the ID of the group you have been invited to or have created. To learn more about groups and permissions in Chainguard Enforce, reveiw our [How to Manage IAM Groups in Chainguard Enforce](/chainguard/chainguard-enforce/iam-groups/how-to-manage-iam-groups-in-chainguard-enforce/) guide.

If you would like more detail about installing the Chainguard Enforce Agent with `chainctl`, or on getting onboarded to Chainguard Enforce, check out our [Getting Started guide](/chainguard/chainguard-enforce/chainguard-enforce-user-onboarding/).

## Install with a Declarative Method

The Chainguard Enforce Agent can be installed declaratively with either YAML or Helm. In order to install this way, you'll need to authenticate first.

### Required Authentication for Declarative Installations

When installing the Chainguard Enforce Agent declaratively, this step must be taken to set up the Agent's authentication and authorization to the Chainguard Enforce Platform. This step ensures the agent knows _how_ it should authenticate to the platform, and _where_ it should authenticate (which [group](/chainguard/chainguard-enforce/iam-groups/how-to-manage-iam-groups-in-chainguard-enforce/)).

Generate the relevant invite code(s) for your cluster or clusters using the following:

```bash
# $GROUP is the IAM group name where clusters using this code will register
INVITE_CODE=$(chainctl iam invite create $GROUP --cluster -ojson | jq -r '.code')
```

For a full overview of the invite code, and how it relates to IAM in Chainguard Enforce, see [our guide on managing groups in Chainguard Enforce](/chainguard/chainguard-enforce/iam-groups/how-to-manage-iam-groups-in-chainguard-enforce/).

#### Additional Authentication for Private Clusters

This step is only required if you're installing on a _private_ cluster. A _private_ cluster is one without a public issuer, which effectively means any cluster that is __not__ GKE, AKS, or EKS.

If you're on a _private_ cluster and still want to use declarative installs (for example, to bulk install across a fleet of on-prem clusters), this step needs to be taken to fulfil the agent's authentication flow.

Currently, the best supported method requires using GCP Service Accounts (GSA). To set up a minimally scoped GSA, follow the [GCP documentation on the subject](https://cloud.google.com/endpoints/docs/openapi/service-account-authentication#gcloud). This can also be done with standard IAC tooling.

Using the created GSA, we'll collect the required information:

```bash
# This is the name of the GSA created in the previous step
GSA_NAME="$SA_NAME:$PROJECT_ID.iam.gserviceaccount.com"

# This is the GSA key file created in the previous step
GSA_KEY=$(cat "$FILENAME.json")
```

This information will be used to configure your installation in later steps.

### Declarative Option 1 — Install with YAML

Defining Kubernetes manifests through YAML provides convenience of not needing to add parameters on the command line, more ease with maintenance through tracking changes in source control, and the ability to add more complexity. If you are already using YAML to deploy Kubernetes, you can install the Chainguard Enforce Agent directly through remotely fetching and modifying the Chainguard Enforce Agent manifest.

You have two options to install the Enforce Agent with YAML, either using `chainctl` or `curl`.

**Please note** that as you will be pulling down manifests, we recommend that you _always inspect_ the contents of these remotely fetched files!

#### YAML Option 1 — Install with `chainctl`

If you would like to work directly with the Chainguard command line tool, you can install the Agent directly into you cluster with `chainctl`.

Install `chainctl` if you have not done so already by following the [How to Install `chainctl` guide](/chainguard/chainguard-enforce/how-to-install-chainctl/).

With the tool installed, authenticate into `chainctl`.

```sh
chainctl auth login
```

Next, fetch the latest YAML representing the Enforce Agent's Kubernetes resources and save it to an `enforce-agent.yaml` file. Make sure you are in a relevant working directory.

```sh
chainctl cluster print-config > enforce-agent.yaml
```

With this YAML fetched, you are ready to [add our authentication details](#add-authentication-details-to-yaml) to your config file.

#### YAML Option 2 — Install with `curl`

If you would like to use `curl` to install YAML, you can do so by pulling down the latest YAML that represents the Enforce Agent's Kubernetes resources, and saving it to a new `enforce-agent.yaml` file. Make sure you are in a relevant working directory.

```sh
curl -s 'https://dl.enforce.dev/{mcp,tenant}.yaml' > enforce-agent.yaml
```

With this YAML fetched, you are ready to [add our authentication details](#add-authentication-details-to-yaml) to your config file, in the next step.

#### Add Authentication Details to YAML

At this point, we can now define how our agent should authenticate with the Chainguard Enforce Platform, with the details we set up the [required authentication](#required-authentication-for-declarative-installations).

With the required authentication pre-provisioned, append the following to the `enforce-agent.yaml` created in the previous step. This format is appropriate for a cluster in GKE, AKS, or EKS.

```bash
cat >> enforce-agent.yaml <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: mcp-creds
  namespace: gulfstream
stringData:
  inviteCode: $INVITE_CODE

  # Optionally, add some descriptive metadata that will be applied to your
  # cluster upon initial registration.  Note that this will not update existing
  # clusters, which can be done via chainctl.
  cluster-name: "my-cluster"
  cluster-description: "a more detailed description of this cluster."
EOF
```

> **Warning**: `mcp-creds` contains sensitive information. If compromised, it could allow unauthorized access to the Chainguard Enforce Platform. We recommend controlling access to it as you would with other platform secrets.

If you're using a _private_ or on-prem cluster, be sure to include the required `auth` components that you set up in the [additional authentication step](#additional-authentication-for-private-clusters).

```bash
cat >> enforce-agent.yaml <<EOF
---
apiVersion: v1
kind: Secret
metadata:
  name: mcp-creds
  namespace: gulfstream
stringData:
  inviteCode: $INVITE_CODE
  gcp-svc-acct-path: "/var/run/sts/gcp.json"
  gcp-svc-acct-name: $GSA_NAME
  gcp.json: $GSA_KEY

  # Optionally, add some descriptive metadata that will be applied to your
  # cluster upon initial registration.  Note that this will not update existing
  # clusters, which can be done via chainctl.
  cluster-name: "my-cluster"
  cluster-description: "a more detailed description of this cluster."
EOF
```

Once the required authentication is set up, the Chainguard Enforce Agent can be installed with any valid Kubernetes installer. We'll use `kubectl` to demonstrate:

```bash
kubectl apply -f enforce-agent.yaml
```

> **Note**: The `enforce-agent.yaml` includes CRDs, which when applied simultaneously with `kubectl` may fail to register before being applied. As a workaround, you may need to run the command twice. In a production scenario, you should split the resources up, or rely on the applying agent (such as Flux or ArgoCD) to handle the ordering.

We've demonstrated the declarative raw YAML install using a single file `enforce-agent.yaml`. In practice, you should feel free to structure the manifests according to your existing Kubernetes deployment workflows.

### Declarative Option 2 — Install with a Helm Chart

If you are already comfortable with the [Helm](https://helm.sh) ecosystem, you may opt to install the Chainguard Enforce Agent with Helm.

Begin by adding the Helm Chart repository.

```bash
helm repo add chainguard https://chainguard-dev.github.io/helm-charts
```

Next, sync its contents.

```bash
helm repo update
```

Before installing the Chart, ensure that the [required authentication](#required-authentication-for-declarative-installations) steps are completed. With your authentication information in hand, create a new `values.yaml` with the required invite code if you are using GKE, AKS, or EKS.

```bash
cat > values.yaml <<EOF
inviteCode: $INVITE_CODE
EOF
```

If you're using a _private_ or on-prem cluster, be sure to include the additional required `auth` components.

```bash
cat > values.yaml <<EOF
inviteCode: $INVITE_CODE

auth:
  gcp:
    serviceAccount:
      email: $GSA_NAME
      key: $GSA_KEY
EOF
```

With the required authentication information included in the `values.yaml` file, you can use the Chart to install the Chainguard Enforce Agent.

```bash
helm upgrade -i enforce-agent chainguard/enforce-agent -f values.yaml
```

The full list of configuration options available are located in the [Chainguard Helm Charts repository](https://github.com/chainguard-dev/helm-charts).

## Next Steps

With the Chainguard Enforce Agent installed in your cluster, continue learning about Enforce by reading the [Getting Started Guide](/chainguard/chainguard-enforce/chainguard-enforce-user-onboarding/), learn how to [manage policies with `chainctl`](/chainguard/chainguard-enforce/policies/chainguard-policies-cli/), or follow the tutorial on [how to detect the Log4Shell vulnerability with Enforce](/chainguard/chainguard-enforce/concepts/detect-log4shell-demo/).
