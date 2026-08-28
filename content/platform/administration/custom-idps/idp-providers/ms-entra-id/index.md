---
title: "How to integrate Microsoft Entra ID SSO with Chainguard"
linktitle: "Microsoft Entra ID"
aliases:
- /chainguard/chainguard-enforce/authentication/example-idps/azure-ad/
- /chainguard/administration/custom-idps/azure-ad/
- /chainguard/administration/custom-idps/ms-entra-id/
- /chainguard/administration/custom-idps/idp-providers/ms-entra-id/
lead: ""
description: "Procedural tutorial on how to register a Microsoft Entra ID application and integrate it with the Chainguard platform."
type: "article"
date: 2023-04-17T08:48:45+00:00
lastmod: 2026-08-27T10:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Procedural"]
images: []
weight: 020
---

The Chainguard platform supports single sign-on (SSO) authentication for users. By default, users can log in with GitHub, GitLab, and Google, but SSO support lets users bring their own identity provider for authentication.

This guide outlines how to register a Microsoft Entra ID (formerly Azure Active Directory) application and integrate it with Chainguard. After completing this guide, you'll be able to log in to Chainguard using Entra ID and you'll no longer be limited to the default SSO options.

{{< note >}}
If you plan to use SCIM provisioning, check out our guide on [how to provision users into Chainguard from Microsoft Entra ID with SCIM](/platform/administration/custom-idps/scim-provisioning/ms-entra-id-scim/) instead. That guide covers SSO as well, and it creates the identity provider with the correlation rule SCIM linking depends on. The correlation rule is immutable, so adding it later means deleting and recreating your identity provider.
{{< /note >}}

## Prerequisites

To complete this guide, you need the following:

* `chainctl` installed on your system. Follow our guide on [How to install `chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/) if you don't already have this installed.
* Owner permissions on the Chainguard organization where you want to install the identity provider.
* An Entra ID account with [Global Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) or [Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator) permissions. Without one of these roles, you can't register applications or assign users to them.
* A workforce Entra ID tenant. External ID (CIAM) tenants use a different application model, and this guide doesn't cover them.

## Create a Microsoft Entra ID application

Log in to the [Microsoft Entra admin center](https://entra.microsoft.com), navigate to **Entra ID** > **App registrations**, and click **New registration**. Configure the application as follows:

* **Name**: Set the name to "Chainguard" (or similar) so users recognize this application is for authentication to Chainguard.
* **Supported account types**: Select **Single tenant only** so that only your organization can use this application to authenticate to Chainguard.
* **Redirect URI**: Set the platform to **Web** and the URI to the following.

    ```URI
    https://issuer.enforce.dev/oauth/callback
    ```

Click **Register**. From the application's **Overview** tab, note the **Application (client) ID** and the **Directory (tenant) ID**.

Next, open **Manage** > **Certificates & secrets**, click **New client secret**, add a description, set an expiration, and click **Add**. Note the secret's **Value**.

> **Warning**: Entra ID shows the secret's **Value** only once, and SSO through this application stops working when the secret expires. Record the expiration date so you can rotate the secret before then.

You'll need all three of the values you noted — the client ID, the tenant ID, and the client secret — in the next section.

### Restrict who can log in

By default, any user in your tenant can authenticate through this application. To limit access to specific users and groups, open **Entra ID** > **Enterprise applications** and select the application you just registered. On its **Properties** page, set **Assignment required?** to **Yes**. Then, under **Users and groups**, assign the users or groups you want to have access.

Users can't log in to Chainguard unless they have access to the application, so grant access before directing them to log in.

## Configure Chainguard to use Microsoft Entra ID

Now that your Microsoft Entra ID application is ready, you can create the custom identity provider.

First, log in to Chainguard with `chainctl`, using an OIDC provider like Google, GitHub, or GitLab to bootstrap your account.

```sh
chainctl auth login
```

Note that you can use this bootstrap account as a [backup account](/chainguard/administration/custom-idps/custom-idps/#backup-accounts) — that is, an account you can use to log in if you ever lose access to your primary account. However, if you prefer to remove this role-binding after configuring the custom IdP, you can do so.

You also need the ID of the Chainguard organization where you want to install the identity provider. Your choice doesn't affect how your users authenticate, but it does determine who has permission to modify the SSO configuration.

To retrieve a list of the Chainguard organizations you belong to, along with their IDs, run the following command.

```sh
chainctl iam organizations ls -o table
```

```output
                    ID                    |    NAME    | STATUS |           DESCRIPTION
------------------------------------------|------------|--------|----------------------------------
 591**********************************c43 | sample_org | ready  | A sample Chainguard organization
 . . .                                    | . . .      | . . .  | . . .
```

Note the `ID` value for your chosen organization.

With this information in hand, create a new identity provider with the following commands. Replace `<application_client_id>`, `<client_secret>`, and `<directory_tenant_id>` with the values from your Entra ID application, and `<organization_id>` with the organization ID you just noted.

```sh
export NAME=entra-id
export CLIENT_ID=<application_client_id>
export CLIENT_SECRET=<client_secret>
export ORG=<organization_id>
export TENANT_ID=<directory_tenant_id>
export ISSUER="https://login.microsoftonline.com/${TENANT_ID}/v2.0"
chainctl iam identity-providers create \
  --configuration-type=OIDC \
  --parent=${ORG} \
  --name=${NAME} \
  --oidc-issuer=${ISSUER} \
  --oidc-client-id=${CLIENT_ID} \
  --oidc-client-secret=${CLIENT_SECRET} \
  --oidc-additional-scopes=email \
  --oidc-additional-scopes=profile \
  --default-role=viewer
```

{{< note >}}
Customers using Azure Government Cloud should set `ISSUER="https://login.microsoftonline.us/${TENANT_ID}/v2.0"` instead.
{{< /note >}}

Pass `--oidc-additional-scopes` once per scope; comma-separating the scopes doesn't work.

The `--default-role` option defines the default role granted to users registering with this identity provider. This example specifies the `viewer` role, but depending on your needs you might choose `editor` or `owner`. If you don't include this option, `chainctl` prompts you to specify the role interactively. For more information, refer to the [IAM and security section](/chainguard/administration/custom-idps/custom-idps/#iam-and-security) of our Introduction to Custom Identity Providers in Chainguard tutorial.

You can refer to our [Generic integration guide](/chainguard/administration/custom-idps/custom-idps/#generic-integration-guide) in our Introduction to Custom Identity Providers doc for more information about the `chainctl iam identity-providers create` command and its required options.

## Log in to Chainguard with the Entra ID identity provider

To log in to the Chainguard Console with the new identity provider you just created, navigate to [console.chainguard.dev/auth/login](https://console.chainguard.dev/auth/login), enter your Chainguard organization's name into the **Email or organization** box, and click **Continue**. This opens a new window with the Microsoft Entra ID login flow, where you can complete the login process.

You can also use the custom identity provider to log in through `chainctl`. To do this, run the `chainctl auth login` command and add the `--identity-provider` option followed by the identity provider's ID value:

```sh
chainctl auth login --identity-provider <idp_id>
```

The ID value appears in the `ID` column of the table returned by the `chainctl iam identity-providers create` command you ran previously. You can also retrieve this table at any time by running `chainctl iam identity-providers ls -o table` when logged in.

To have Entra ID create and deactivate Chainguard user accounts automatically as you assign and unassign them, check out our guide on [how to provision users into Chainguard from Microsoft Entra ID with SCIM](/platform/administration/custom-idps/scim-provisioning/ms-entra-id-scim/).
