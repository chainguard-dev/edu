---
title: "Alternative Enforce Agent Installation Methods"
type: "article"
lead: ""
description: "Alternative installation methods and instructions."
date: 2022-11-04T15:56:52-07:00
lastmod: 2022-11-04T15:56:52-07:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-enforce-kubernetes"
weight: 700
toc: true
---

While the `chainctl` approach outlined in [user
onboarding](./chainguard-enforce-user-onboarding.md) is a valid and well
supported method of installing the Chainguard Enforce Agent, some may prefer
alternative methods to better align with their existing Kubernetes workflows.

We'll refer to these alternative methods as various flavors of Declarative
Installs. In other words, the entirety of the Chainguard Enforce Agent resources
are defined as static Kubernetes manifests.

Static manifests created for Declarative Installs allow for great flexibility
for how they're ultimately applied to the cluster, and can be easily adapted to
fit most Kubernetes deployment workflows.

The two examples we'll cover are: "raw" yaml, and a helm chart.

## Raw YAML

First, we'll fetch the latest YAML representing the Chainguard Enforce Agent's
Kubernetes resources:

```bash
# Option 1: chainctl
chainctl cluster print-config > enforce-agent.yaml

# Option 2: remote
curl -s 'https://dl.enforce.dev/{mcp,tenant}.yaml' > enforce-agent.yaml
```

> Note: We always recommend inspecting the contents of remotely fetched
manifests!

Before proceeding, we must first define how our agent should authenticate with
the Chainguard Enforce Platform, and which [group](./how-to-manage-iam-groups-in-chainguard-enforce.md)
to register under. To do this, we first set up the [required authentication](#required-authentication).

> Note: Before proceeding, ensure the [required
authentication](#required-authentication) steps are
completed.

Once the required authentication is pre-provisioned, append the following to
the `enforce-agent.yaml` created in the previous step:

```bash
cat >> enforce-agent.yaml <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: mcp-creds
  namespace: gulfstream
stringData:
  code: $INVITE_CODE
EOF
```

> Warning: `mcp-creds` contains sensitive information. If compromised it could
allow unauthorized access to the Chainguard Enforce Platform. We recommend
controlling access to it as you would with other platform secrets.

Alternatively, if you're using an on-prem cluster, be sure to include the
additional required `auth` components:

```bash
cat >> enforce-agent.yaml <<EOF
---
apiVersion: v1
kind: Secret
metadata:
  name: mcp-creds
  namespace: gulfstream
stringData:
  code: $INVITE_CODE
  gcp-svc-acct-path: "/var/run/sts/gcp.json"
  gcp-svc-acct-name: $GSA_NAME
  gcp.json: $GSA_KEY
EOF
```

Once the required authentication is set up, the Chainguard Enforce Agent can be
installed with any valid Kubernetes installer, we'll use `kubectl` to
demonstrate:

```bash
kubectl apply -f enforce-agent.yaml
```

> Note: The `enforce-agent.yaml` includes CRDs, which when applied all in one
shot with `kubectl` may fail to register before being applied. To "workaround"
this you may need to run the command twice. In a "real world" scenario you
should split the resources up, or rely on the applying agent (ie Flux or ArgoCD)
to handle the ordering.

Up till now we've demonstrated the declarative raw yaml install using a single
file: `enforce-agent.yaml`. However, in practice the structure of this doesn't
matter, and you should feel free to structure the manifests according to your
existing Kubernetes deployment workflows.

## Helm Chart

A [helm](https://helm.sh) chart is provided for those already comfortable with
the helm ecosystem.

Begin by adding the cart repository and syncing it's contents:

```bash
helm repo add chainguard https://chainguard-dev.github.io/helm-charts

helm repo update
```

Before installing the chart, ensure that the [required
authentication](#required-authentication)
steps are completed. With the information in hand, create a new `values.yaml`
with the required invite code:

```bash
cat > values.yaml <<EOF
code: $INVITE_CODE
EOF
```

Alternatively, if you're using an on-prem cluster, be sure to include the
additional required `auth` components:

```bash
cat > values.yaml <<EOF
code: $INVITE_CODE

auth:
  gcp:
    serviceAccount:
      email: $GSA_NAME
      key: $GSA_KEY
EOF
```

With the required authentication information in the `values.yaml`, the chart can
then be installed using:

```bash
helm upgrade -i enforce-agent chainguard/enforce-agent -f values.yaml
```

The full list of configuration options available are located in the [charts repo](https://github.com/chainguard-dev/helm-charts).

### Required authentication

When installing the Chainguard Enforce Agent declaratively, an additional step
must be taken to setup the Agent's authentication and authorization to the
Chainguard Enforce Platform. This step ensures the agent knows _how_ it should
authenticate to the platform, and _where_ it should authentication (which
[group](./how-to-manage-iam-groups-in-chainguard-enforce.md)).

Depending on the destination cluster, the information required will vary.

#### Required: The cluster invite code

Generate the cluster(s) invite code using the following:

```bash
# $GROUP is the IAM group where clusters using this code will register
INVITE_CODE=$(chainctl iam invite create $GROUP --cluster -ojson | jq -r '.code')
```

> Note: For a full overview of the invite code, and how it relates to IAM in
Chainguard Enforce, see [here](./how-to-manage-iam-groups-in-chainguard-enforce.md).

#### Optional: The issuer information

This step is only required if you're installing on a "private" cluster. A
private cluster is one without a public issuer, which effectively means any
cluster that is __not__ GKE, AKS, or EKS.

If you're on a "private" cluster and still want to use declarative installs (for
example, to bulk install across a fleet of on-prem clusters), an additional step
needs to be taken to fulfil the agent's authentication flow.

Currently, the best supported method requires using GCP Service Accounts (GSA).
To set up a minimally scoped GSA, follow the GCP documentation [here](https://cloud.google.com/endpoints/docs/openapi/service-account-authentication#gcloud).
This can also be done with standard IAC tooling.

Using the created GSA, we'll collect the required information:

```bash
# This is the name of the GSA created in the previous step
GSA_NAME="$SA_NAME:$PROJECT_ID.iam.gserviceaccount.com"

# This is the GSA key file created in the previous step
GSA_KEY=$(cat "$FILENAME.json")
```
