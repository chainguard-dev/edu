---
title: "Create an Assumable Identity to Authenticate from Azure"
linktitle: "Azure"
lead: ""
description: "Procedural tutorial outlining how to create a Chainguard identity that can be assumed by an Azure workload using a managed identity."
type: "article"
date: 2026-05-15T00:00:00+00:00
lastmod: 2026-05-15T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Procedural"]
images: []
weight: 011
---

> **Note:** If you're authenticating from a workload running in Azure
> Kubernetes Service (AKS), refer to the
> [Kubernetes identity guide](/chainguard/administration/assumable-ids/identity-examples/kubernetes-identity/)
> instead.

Chainguard's [_assumable identities_](/chainguard/administration/assumable-ids/assumable-ids/)
are identities that can be assumed by external applications or workflows in
order to perform certain tasks that would otherwise have to be done by a human.

This procedural tutorial outlines how to create an identity that can be assumed
by an Azure workload — such as a VM, Container App, or Function — using an
[Azure managed identity](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview)
and then used to interact with the Chainguard API.

## Prerequisites

To complete this guide, you will need the following.

- `chainctl` — the Chainguard command line interface tool — installed on your
  local machine. Follow our guide on
  [How to Install `chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/)
  to set this up.
- The [Azure CLI (`az`)](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli),
  authenticated with `az login`.
- An Azure subscription, and permission to register applications in your Entra
  ID tenant. App registration is enabled for all users in most tenants. If
  it's disabled in yours, ask an administrator to pre-register the
  application and share its client ID with you.
- To follow the Terraform example, [`terraform`](https://developer.hashicorp.com/terraform/install)
  installed locally.

## Find your Tenant ID

Each Entra ID tenant has its own OIDC issuer URL, which has the following
format:

```
https://login.microsoftonline.com/<tenant-id>/v2.0
```

Retrieve the tenant ID of your current Azure session with:

```shell
az account show --query tenantId --output tsv
```

## Create the Entra ID Application

Register an Entra ID application to serve as the audience for tokens issued
to managed identities in your tenant. We'll grant it no API permissions and
expose no scopes — its only purpose is to provide a unique, tenant-specific
`aud` claim that Chainguard's STS can match on.

```shell
az ad app create \
  --display-name chainguard-audience \
  --sign-in-audience AzureADMyOrg
```

Note down the `appId` from the output — this is the client ID we'll use as the
token audience. Substitute it for `<client-id>` in the following commands.

Configure the application to issue v2.0 access tokens and to register
`api://<client-id>` as an identifier URI, so that Entra ID will resolve it as
a valid scope when requesting tokens.

```shell
az ad app update \
  --id <client-id> \
  --requested-access-token-version 2 \
  --identifier-uris "api://<client-id>"
```

Then create a service principal for the application. Entra ID requires this
in order to recognise the application as a valid token resource when a
managed identity requests a token for it.

```shell
az ad sp create --id <client-id>
```

## Create the Managed Identity

If you don't already have a
[user-assigned managed identity](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-manage-user-assigned-managed-identities)
to bind the Chainguard identity to, create one now. Substitute
`<resource-group>` and `<location>` (e.g. `eastus`) for your own values.

```shell
az identity create \
  --name chainguard-identity \
  --resource-group <resource-group> \
  --location <location>
```

Note down the `principalId` from the output — we'll use this as the subject of
the Chainguard identity in the next step. Note the `clientId` too, as the
workload will need it later to request a token.

## Create the Assumable Identity

This guide outlines two methods for creating the Chainguard identity: one
using `chainctl` over a command-line interface, and another using Terraform.

### CLI

Run this `chainctl` command to create the identity and bind it to the
`registry.pull` role. Substitute `<tenant-id>` with the tenant ID you
retrieved earlier, `<principal-id>` with the managed identity's principal ID,
and `<client-id>` with the application's client ID.

```shell
chainctl iam id create azure-identity \
  --identity-issuer="https://login.microsoftonline.com/<tenant-id>/v2.0" \
  --subject="<principal-id>" \
  --audience="<client-id>" \
  --role=registry.pull
```

This will return the [UIDP (unique identity path)](/chainguard/administration/cloudevents/events-reference/#uidp-identifiers)
of the identity, which we'll use when assuming it in the next section.

If you need to retrieve the UIDP later, list the identity with this command:

```shell
chainctl iam identities list --name=azure-identity
```

### Terraform

You can also create the application registration, managed identity, and
Chainguard identity together with the
[Chainguard Terraform provider](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest)
and the
[AzureRM](https://registry.terraform.io/providers/hashicorp/azurerm/latest)
and
[AzureAD](https://registry.terraform.io/providers/hashicorp/azuread/latest)
providers.

Substitute `<org-name>` with your Chainguard organization name,
`<resource-group>` with your Azure resource group, and `<location>` with the
Azure region you want to deploy into.

```hcl
terraform {
  required_providers {
    azurerm    = { source = "hashicorp/azurerm" }
    azuread    = { source = "hashicorp/azuread" }
    chainguard = { source = "chainguard-dev/chainguard" }
  }
}

provider "azurerm" {
  features {}
}

data "azurerm_client_config" "current" {}
data "azuread_client_config" "current" {}

# A permission-free Entra ID application registration. Its sole purpose is
# to provide a unique audience for tokens exchanged with Chainguard's STS.
resource "azuread_application" "chainguard_audience" {
  display_name = "chainguard-audience"
  owners       = [data.azuread_client_config.current.object_id]

  api {
    requested_access_token_version = 2
  }

  lifecycle {
    ignore_changes = [identifier_uris]
  }
}

# A service principal — required for Entra ID to recognise the application
# as a valid token audience when a managed identity requests a token.
resource "azuread_service_principal" "chainguard_audience" {
  client_id = azuread_application.chainguard_audience.client_id
  owners    = [data.azuread_client_config.current.object_id]
}

# Register api://<client-id> as the identifier URI so Entra ID resolves
# it as a valid resource for token requests.
resource "azuread_application_identifier_uri" "chainguard_audience" {
  application_id = azuread_application.chainguard_audience.id
  identifier_uri = "api://${azuread_application.chainguard_audience.client_id}"
}

# A user-assigned managed identity that will assume the Chainguard identity.
# Attach this to any Azure workload that supports managed identities
# (VMs, Container Apps, Functions, etc).
resource "azurerm_user_assigned_identity" "chainguard" {
  name                = "chainguard-identity"
  resource_group_name = "<resource-group>"
  location            = "<location>"
}

data "chainguard_group" "org" {
  name = "<org-name>"
}

resource "chainguard_identity" "azure" {
  parent_id   = data.chainguard_group.org.id
  name        = "azure-identity"
  description = "Assumed by Azure workloads via the chainguard-identity managed identity."

  claim_match {
    issuer   = "https://login.microsoftonline.com/${data.azurerm_client_config.current.tenant_id}/v2.0"
    subject  = azurerm_user_assigned_identity.chainguard.principal_id
    audience = azuread_application.chainguard_audience.client_id
  }
}

data "chainguard_role" "registry_pull" {
  name = "registry.pull"
}

resource "chainguard_rolebinding" "registry_pull" {
  identity = chainguard_identity.azure.id
  role     = data.chainguard_role.registry_pull.items[0].id
  group    = data.chainguard_group.org.id
}

output "chainguard_identity_id" {
  value = chainguard_identity.azure.id
}

output "token_audience" {
  value = "api://${azuread_application.chainguard_audience.client_id}"
}

output "managed_identity_client_id" {
  value = azurerm_user_assigned_identity.chainguard.client_id
}
```

The `chainguard_identity_id` output provides the identity's UIDP. The
`token_audience` and `managed_identity_client_id` outputs provide the values
your workload will need to request a managed identity token and exchange it
with Chainguard.

For a full end-to-end example of using this pattern from an Azure Container
App, see the
[`image-copy-acr` example](https://github.com/chainguard-demo/platform-examples/tree/main/image-copy-acr)
in Chainguard's public `platform-examples` repository.

## Assume the Identity

Attach the managed identity to the Azure workload you want to authenticate
from. For example, to attach it to an existing VM:

```shell
az vm identity assign \
  --name <vm-name> \
  --resource-group <resource-group> \
  --identities <managed-identity-resource-id>
```

From inside the workload, request a token from the
[Azure Instance Metadata Service (IMDS)](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-to-use-vm-token)
for the audience you configured on the application. Substitute `<client-id>`
with the application's client ID, and `<managed-identity-client-id>` with the
`clientId` of the managed identity.

```shell
AZURE_TOKEN=$(curl -sSf \
  -H "Metadata: true" \
  "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=api://<client-id>&client_id=<managed-identity-client-id>" \
  | jq -r .access_token)
```

The following sections outline two methods for using the Azure token to
interact with Chainguard: one using `chainctl`, and another by exchanging
the token directly with the Chainguard STS over the API.

### CLI

Use the Azure token to log in with `chainctl`. Substitute `<identity-id>`
with the UIDP of the Chainguard identity created earlier.

```shell
chainctl auth login \
  --identity <identity-id> \
  --identity-token "${AZURE_TOKEN}"
```

Now you can issue `chainctl` commands under this assumed identity. For
instance, you could list the container image repositories available to your
organization:

```shell
chainctl image repo list
```

To pull images from the Chainguard registry with Docker, configure a
credential helper with `chainctl`. Provide the same identity and token:

```shell
chainctl auth configure-docker \
  --identity <identity-id> \
  --identity-token "${AZURE_TOKEN}"
```

You can now pull images with `docker`. Substitute `<org-name>` with your
Chainguard organization name and `<image>` with an image available to your
organization.

```shell
docker pull cgr.dev/<org-name>/<image>:latest
```

### API

If `chainctl` isn't installed in the workload, you can exchange the Azure
token for a Chainguard API token directly. Substitute `<identity-id>` with
the UIDP of the Chainguard identity created earlier.

```shell
API_TOKEN=$(curl -sSf \
  -H "Authorization: Bearer ${AZURE_TOKEN}" \
  "https://issuer.enforce.dev/sts/exchange?aud=https://console-api.enforce.dev&identity=<identity-id>" \
  | jq -r .token)
```

Use the API token to interact with the Chainguard API. For instance, to list
the container image repositories available to your organization:

```shell
curl -sSf -H "Authorization: Bearer ${API_TOKEN}" \
  https://console-api.enforce.dev/registry/v1/repos | jq -r .items[].name
```

If you're authenticating from Go, the
[Chainguard SDK](https://pkg.go.dev/chainguard.dev/sdk) and the
[Azure SDK for Go](https://pkg.go.dev/github.com/Azure/azure-sdk-for-go) can
do the token exchange for you. The
[`image-copy-acr` example](https://github.com/chainguard-demo/platform-examples/tree/main/image-copy-acr)
demonstrates this pattern.

## Clean Up

Delete the Chainguard identity.

```shell
chainctl iam id delete <identity-id>
```

Delete the managed identity.

```shell
az identity delete \
  --name chainguard-identity \
  --resource-group <resource-group>
```

Delete the Entra ID application registration. This will also remove the
associated service principal.

```shell
az ad app delete --id <client-id>
```

## Learn more

For more information about how assumable identities work in Chainguard, check
out our [conceptual overview of assumable identities](/chainguard/administration/assumable-ids/assumable-ids/).
