---
title: "How to provision users into Chainguard from Microsoft Entra ID with SCIM"
linktitle: "Microsoft Entra ID SCIM Provisioning"
lead: ""
description: "Procedural tutorial on how to set up SCIM provisioning and SSO from Microsoft Entra ID to the Chainguard platform."
type: "article"
date: 2026-08-11T00:00:00+00:00
lastmod: 2026-08-11T00:00:00+00:00
draft: false
tags: ["Procedural"]
images: []
weight: 040
---

{{< beta feature="SCIM user provisioning" >}}

The Chainguard platform supports SCIM 2.0 provisioning from Microsoft Entra ID. With SCIM enabled, Entra ID creates, updates, and deactivates Chainguard users as you assign and unassign them in your directory, and each provisioned user is linked to their single sign-on (SSO) identity the first time they log in.

This guide outlines how to register an Entra ID application for SSO, create a Chainguard identity provider for it, and configure an Entra ID enterprise application for SCIM provisioning. Set up SSO first, since provisioning links users to their SSO logins. For provisioning behavior, token lifecycle, and limits, refer to [Provision Chainguard Users with SCIM](/chainguard/administration/custom-idps/scim-provisioning/).

## Prerequisites

To complete this guide, you will need the following.

* `chainctl` installed on your system. Follow our guide on [How to install `chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/) if you don't already have this installed.
* Owner permissions on the Chainguard organization where you will install the identity provider.
* The [common prerequisites](/chainguard/administration/custom-idps/scim-provisioning/#prerequisites) for SCIM provisioning, including two owners with directly assigned role bindings in your organization.
* An Entra ID account with Global Administrator or Application Administrator permissions. Without these you will not be able to register applications or assign users to them.
* An Entra ID P1 or P2 license. The **Automatic** provisioning mode used below requires one.
* A workforce Entra ID tenant. External ID (CIAM) tenants use a different application model and are not covered here.

## Register the Entra ID application for SSO

Log in to the [Microsoft Entra admin center](https://entra.microsoft.com), navigate to **Identity** > **Applications** > **App registrations**, and click **New registration**. Configure the application as follows.

* **Name**: Set the name to "Chainguard" (or similar) so users recognize this application is for authentication to Chainguard.
* **Supported account types**: Select **Single tenant** so that only your organization can use this application to authenticate to Chainguard.
* **Redirect URI**: Set the platform to **Web** and the URI to `https://issuer.enforce.dev/oauth/callback`.

Click **Register**. From the application's **Overview** tab, note the **Application (client) ID** and the **Directory (tenant) ID**.

Then open **Certificates & secrets**, click **New client secret**, set a description and expiration, and note the secret **Value**. The Value is shown only once, and SSO stops working when the secret expires. You'll need all three values in the next step.

## Create the Chainguard identity provider

Log in to Chainguard with `chainctl`, using an OIDC provider like Google, GitHub, or GitLab to bootstrap your account.

```sh
chainctl auth login
```

This bootstrap account can serve as a [backup account](/chainguard/administration/custom-idps/custom-idps/#backup-accounts) if you ever lose access to your primary login.

Retrieve the ID of the organization where you want to install the identity provider.

```sh
chainctl iam organizations ls -o table
```

Then create the identity provider, substituting the three values from the previous step and your organization ID.

```sh
export NAME=entra-id
export CLIENT_ID=<your application/client id here>
export CLIENT_SECRET=<your client secret here>
export ORG=<your organization id here>
export TENANT_ID=<your directory/tenant id here>
export ISSUER="https://login.microsoftonline.com/${TENANT_ID}/v2.0"
chainctl iam identity-providers create \
  --configuration-type=OIDC \
  --parent=${ORG} \
  --name=${NAME} \
  --oidc-issuer=${ISSUER} \
  --oidc-client-id=${CLIENT_ID} \
  --oidc-client-secret=${CLIENT_SECRET} \
  --oidc-correlation-rule=oid_equals_external_id \
  --oidc-additional-scopes=email \
  --oidc-additional-scopes=profile \
  --default-role=viewer \
  -o json
```

Two options are specific to SCIM linking with Entra ID:

* `--oidc-correlation-rule=oid_equals_external_id` links each login to its provisioned user by the Entra ID `oid` claim. It is immutable — to change it, delete and recreate the identity provider. Confirm it appears in the command's JSON output, and keep that output as your record of the setting.
* `--oidc-additional-scopes=profile` is required: Entra ID includes the `oid` claim only when `profile` is requested. Pass `--oidc-additional-scopes` once per scope.

Note the identity provider's `id` from the output, then enable SCIM and generate a provisioning token for it.

```sh
export IDP=<identity provider id from the output above>
chainctl iam identity-providers scim enable ${IDP}
chainctl iam identity-providers scim token generate ${IDP}
```

The `token generate` command prints the **SCIM base URL** for the identity provider and a **bearer token** beginning with `cgscim_`. Note both now — the token is shown only once. To replace or revoke it later, use the `scim token regenerate` and `scim token revoke` commands described in [Provision Chainguard Users with SCIM](/chainguard/administration/custom-idps/scim-provisioning/#manage-provisioning).

## Configure the Entra ID enterprise application for SCIM

Provisioning runs from a separate non-gallery enterprise application. In the Entra admin center, navigate to **Identity** > **Applications** > **Enterprise applications** and click **New application**. Click **Create your own application**, name it (for example, "Chainguard SCIM"), select **Integrate any other application you don't find in the gallery (Non-gallery)**, and click **Create**.

### Connect to the SCIM endpoint

Open the application's **Connectivity** page and configure the connection.

* **Select authentication method**: **Bearer authentication**.
* **Tenant URL**: The SCIM base URL from the previous step with `?aadOptscim062020` appended, which opts Entra ID into SCIM 2.0-compliant behavior.
* **Secret token**: The bare `cgscim_...` token. Do not add a `Bearer` prefix — Entra ID adds the scheme itself.

Click **Test connection** to confirm the URL and token — a successful test is required — then **Save**.

### Map externalId to objectId

Open the **Attribute mapping** page and select the **Users** tab. Edit the mapping whose **Target attribute** is **`externalId`**, and change its **Source attribute** from the default (`mailNickname`) to **`objectId`** (`objectId` is in the source-attribute dropdown). Leave the mapping type as **Direct**, then click **Apply**.

**_NOTE:_** Make this change before provisioning any user, including with **Provision on demand**, and do not change it afterward. `objectId` is the value the identity provider matches against at login; changing it after users exist leaves those users permanently unlinked. Map `externalId` only to `objectId` — a user-editable or non-unique attribute could link a login to the wrong identity.

Leave `userName` mapped from `userPrincipalName` — it is the matching attribute — and leave `active` unmapped, since Entra ID manages it. You may keep other default mappings; Chainguard ignores attributes it doesn't use. If the application shows a **Provision Microsoft Entra ID Groups** mapping, disable it; Chainguard's SCIM endpoint accepts user provisioning only.

### Assign users and turn on provisioning

Under the application's **Users and groups**, assign the users or groups to provision.

On the **Provisioning** page, set **Provisioning Mode** to **Automatic**, and under **Settings** set **Scope** to **Sync only assigned users and groups**.

Confirm the `externalId` mapping shows `objectId` before you provision anyone, including with **Provision on demand** (see the note in the previous section). Then set **Provisioning Status** to **On** and click **Save** to begin.

Entra ID runs its provisioning cycle about every 40 minutes. While testing, use **Provision on demand** to push a single user immediately.

## Verify the integration

Provision one user, then query the SCIM API to confirm the user's `externalId` is their `objectId` — a lowercase GUID, not a mail nickname.

```sh
curl -s -H "Authorization: Bearer <your cgscim_ token>" "<your SCIM base URL>/Users?count=5"
```

Then have that user log in at [console.chainguard.dev](https://console.chainguard.dev): click **Use Your Identity Provider**, then **Use Your Organization Name**, enter your organization name, and click **Login with Provider**. The first login must go through this browser flow for linking to complete. Afterward the user appears in your organization with the identity provider's default role.

## Deactivation and deletion

Unassigning a user from the application, disabling their account, or deleting them causes Entra ID to deactivate or delete the corresponding Chainguard identity on its next provisioning cycle. A user deactivated before their first login is rejected at login. For immediate offboarding, use **Provision on demand** on the affected user rather than waiting for the cycle.

## Troubleshooting

**A user logged in but wasn't linked.** A correlation mismatch does not error — the login proceeds as a normal, unlinked user. Confirm the identity provider was created with `--oidc-correlation-rule=oid_equals_external_id` and `profile` in its scopes (check the saved `create` output), that the user's `externalId` is their `objectId` GUID, and that the user has logged in through the browser flow above.

**Login fails, or the identity provider isn't offered.** This is an SSO problem, not SCIM. Recheck the redirect URI, issuer, and client ID from the SSO application.

**Test Connection fails.** Confirm the Tenant URL is the SCIM base URL with `?aadOptscim062020` appended and the Secret Token is the bare `cgscim_...` value. The URL and token must come from the same `token generate` run.

**Provisioning is quarantined.** Entra ID pauses provisioning after repeated errors. Fix the error shown in the provisioning logs and restart provisioning.

## Related resources

* [Provision Chainguard Users with SCIM](/chainguard/administration/custom-idps/scim-provisioning/)
* [Grant Chainguard Roles from Identity Provider Groups](/chainguard/administration/custom-idps/grant-roles-from-groups/)
* [Overview of the Chainguard IAM Model](/chainguard/administration/iam-organizations/overview-of-chainguard-iam-model/)
