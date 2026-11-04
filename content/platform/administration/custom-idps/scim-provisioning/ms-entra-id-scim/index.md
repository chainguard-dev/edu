---
title: "How to provision users into Chainguard from Microsoft Entra ID with SCIM"
linktitle: "Microsoft Entra ID SCIM configuration"
lead: ""
description: "Procedural tutorial on how to set up SCIM provisioning and SSO from Microsoft Entra ID to the Chainguard platform."
type: "article"
date: 2026-08-11T00:00:00+00:00
lastmod: 2026-10-02T14:38:42+00:00
draft: false
tags: ["Procedural"]
images: []
weight: 30
---

The Chainguard platform supports SCIM 2.0 provisioning from Microsoft Entra ID. With SCIM enabled, Entra ID creates, updates, and deactivates Chainguard users as you assign and unassign them in your directory, and Chainguard links each provisioned user to their single sign-on (SSO) identity the first time they log in.

This guide outlines how to register an Entra ID application for SSO, create a Chainguard identity provider for it, and configure an Entra ID enterprise application for SCIM provisioning. Set up SSO first, since provisioning links users to their SSO logins. For provisioning behavior, token lifecycle, and limits, refer to [Provision Chainguard users with SCIM](/platform/administration/custom-idps/scim-provisioning/scim-overview/).

## Prerequisites

To complete this guide, you need the following:

* `chainctl` installed on your system. Follow our guide on [How to install `chainctl`](/platform/chainctl-usage/how-to-install-chainctl/) if you don't already have this installed.
* Owner permissions on the Chainguard organization where you want to install the identity provider.
* The [prerequisites for SCIM provisioning](/platform/administration/custom-idps/scim-provisioning/scim-overview/#prerequisites), including at least one owner who can sign in and holds the owner role directly.
* An Entra ID account with Global Administrator or Application Administrator permissions. Without these, you can't register applications or assign users to them.
* An Entra ID P1 or P2 license. The **Automatic** provisioning mode this guide uses requires one.
* A workforce Entra ID tenant. External ID (CIAM) tenants use a different application model, and this guide doesn't cover them.

## Register the Entra ID application for SSO

Log in to the [Microsoft Entra admin center](https://entra.microsoft.com), navigate to **Entra ID** > **App registrations**, and click **New registration**. Configure the application as follows.

* **Name**: Set the name to "Chainguard" (or similar) so users recognize this application is for authentication to Chainguard.
* **Supported account types**: Select **Single tenant** so that only your organization can use this application to authenticate to Chainguard.
* **Redirect URI**: Set the platform to **Web** and the URI to `https://issuer.enforce.dev/oauth/callback`.

Click **Register**. From the application's **Overview** tab, note the **Application (client) ID** and the **Directory (tenant) ID**.

Then open **Certificates & secrets**, click **New client secret**, set a description and expiration, and note the secret **Value**. Entra ID shows the Value only once, and SSO stops working when the secret expires. You'll need all three values in the next step.

## Create the Chainguard identity provider

These steps use `chainctl`. To create the identity provider in the Chainguard Console instead, follow the "Create an identity provider" section of [Manage custom identity providers in the Chainguard Console](/platform/administration/custom-idps/manage-idps-in-console/#create-an-identity-provider) and choose the **Microsoft Entra ID (oid = externalId)** correlation rule, then return to [Configure the Entra ID enterprise application for SCIM](#configure-the-entra-id-enterprise-application-for-scim). The Console generates the SCIM token when you turn on SCIM syncing, as described in the "Turn on SCIM syncing" section of the same [Console page](/platform/administration/custom-idps/manage-idps-in-console/#turn-on-scim-syncing).

Log in to Chainguard with `chainctl`, using an OIDC provider like Google, GitHub, or GitLab to bootstrap your account.

```sh
chainctl auth login
```

This bootstrap account can serve as a [backup account](/platform/administration/custom-idps/custom-idps/#backup-accounts) if you ever lose access to your primary login.

If you belong to more than one organization, retrieve the ID of the one where you want to install the identity provider.

```sh
chainctl iam organizations ls -o table
```

Then create the identity provider. Replace `<application_client_id>`, `<client_secret>`, and `<directory_tenant_id>` with the three values from the previous step.

```sh
export NAME=entra-id
export CLIENT_ID=<application_client_id>
export CLIENT_SECRET=<client_secret>
export TENANT_ID=<directory_tenant_id>
export ISSUER="https://login.microsoftonline.com/${TENANT_ID}/v2.0"
chainctl iam identity-providers create \
  --configuration-type=OIDC \
  --name=${NAME} \
  --oidc-issuer=${ISSUER} \
  --oidc-client-id=${CLIENT_ID} \
  --oidc-client-secret=${CLIENT_SECRET} \
  --oidc-correlation-rule=oid_equals_external_id \
  --oidc-additional-scopes=email \
  --oidc-additional-scopes=profile \
  -o json
```

`chainctl` installs the provider in your organization automatically when you belong to only one. If you have access to more than one, add `--parent=<organization_id>` to choose where to install it.

This `create` command includes two options specific to SCIM linking with Entra ID:

* `--oidc-correlation-rule=oid_equals_external_id` links each login to its provisioned user by the Entra ID `oid` claim. It's immutable — to change it, delete and recreate the identity provider. Confirm it appears in the command's JSON output, and keep that output as your record of the setting.
* `--oidc-additional-scopes=profile` is required: Entra ID includes the `oid` claim only when you request `profile`. Pass `--oidc-additional-scopes` once per scope.

Set an environment variable to the identity provider's `id` from the previous command's output:

```sh
export IDP=<idp_id>
```

Then generate a provisioning token:

```sh
chainctl iam identity-providers scim token generate ${IDP}
```

The `token generate` command prints the **SCIM base URL** for the identity provider and a **bearer token** beginning with `cgscim_`. Note both now — Chainguard shows the token only once. To replace or revoke it later, use the `scim token regenerate` and `scim token revoke` commands described in [Provision Chainguard users with SCIM](/platform/administration/custom-idps/scim-provisioning/scim-overview/#manage-provisioning).

Following that, enable SCIM for the IdP:

```sh
chainctl iam identity-providers scim enable ${IDP}
```

The order of these commands is important: you must generate the token first, as `scim enable` fails with `etag: etag is required` if the identity provider has no token issued yet.

Enabling SCIM clears the identity provider's default role. If you set one with `--default-role`, the **DEFAULT ROLE** column in `chainctl iam identity-providers list` is empty afterward.

## Configure the Entra ID enterprise application for SCIM

Provisioning runs from a separate non-gallery enterprise application. In the Entra admin center, navigate to **Entra ID** > **Overview**. Click **+ Add** and select **Enterprise applications**. Click **Create your own application**, name it (for example, "Chainguard SCIM"), select **Integrate any other application you don't find in the gallery (Non-gallery)**, and click **Create**.

### Connect to the SCIM endpoint

Open the enterprise application's **Overview** page, navigate to the **Provisioning** tab, and click **+ New configuration**. From there, configure the connection:

* **Select authentication method**: **Bearer authentication**.
* **Tenant URL**: The SCIM base URL from the previous step with `?aadOptscim062020` appended, which opts Entra ID into SCIM 2.0-compliant behavior.
    * To illustrate, the URL should have the following structure:

        ```url
        https://scim.enforce.dev/scim/v2/<organization_id>/<idp_id>?aadOptscim062020
        ```

* **Secret token**: The bare `cgscim_...` token. Don't add a `Bearer` prefix — Entra ID adds the scheme itself.

Click **Test connection** to confirm the URL and token — the test must succeed — then **Save**.

### Map externalId to objectId

While still in the Provisioning seciton, navigate to **Attribute mapping** and select **Users**. Click the **`externalId`** mapping and change its **Source attribute** from the default (`mailNickname`) to **`objectId`** (`objectId` is in the source-attribute dropdown). Leave the mapping type as **Direct**, then click **Apply**.

{{< note >}}
Make this change before provisioning any user, including with **Provision on demand**, and don't change it afterward. `objectId` is the value the identity provider matches against at login; changing it after users exist leaves those users permanently unlinked. Map `externalId` only to `objectId` — a user-editable or non-unique attribute could link a login to the wrong identity.
{{< /note >}}

Leave the other mappings at their defaults. `userName` maps from `userPrincipalName`, which is the attribute Chainguard matches on. `active` maps through the default expression `Switch([IsSoftDeleted], , "False", "True", "True", "False")`, which inverts `IsSoftDeleted` so that a user Entra ID soft-deletes or unassigns arrives at Chainguard as inactive — this is what drives deactivation.

If you plan to grant roles from Entra ID groups, leave the **Provision Microsoft Entra ID Groups** mapping enabled and follow [Push groups to grant roles](#push-groups-to-grant-roles) after you verify the integration. Otherwise, set its **Enabled** option to **No**.

### Assign users and turn on provisioning

Under the application's **Users and groups**, assign the users or groups to provision.

On the **Provisioning** page, set **Provisioning Mode** to **Automatic**, and under **Settings** set **Scope** to **Sync only assigned users and groups**. Then set **Provisioning Status** to **On** and click **Save** to begin.

Entra ID runs its provisioning cycle about every 40 minutes. While testing, use **Provision on demand** to push a user immediately.

## Verify the integration

Provision a user, then query the SCIM API to confirm the user's `externalId` is their `objectId` — a lowercase GUID, not a mail nickname. Replace `<scim_token>` and `<scim_base_url>` with the bearer token and SCIM base URL from the `token generate` command.

```sh
curl -s -H "Authorization: Bearer <scim_token>" "<scim_base_url>/Users?count=5"
```

Then have that user log in at [console.chainguard.dev](https://console.chainguard.dev). They enter your organization name in the **Email or organization** box and click **Continue**, and the Console detects your organization's identity provider and sends them to Entra ID to sign in. The first login must go through this browser flow for linking to complete.

The user is now linked but holds no role in your organization, so the Console asks them to join an organization. To grant roles, follow [Push groups to grant roles](#push-groups-to-grant-roles) or [Grant roles from the groups claim](#grant-roles-from-the-groups-claim).

## Push groups to grant roles

Entra ID can also provision groups to Chainguard. Chainguard matches each provisioned group against your group-to-role mappings and grants the mapped roles to the group's members as role bindings. These bindings persist between logins, unlike the session-scoped roles that [claim-based group mappings](#grant-roles-from-the-groups-claim) grant, and they appear in `chainctl iam role-bindings list`.

You manage these bindings from Entra ID. To change who holds a role, change the group's membership in Entra ID; Chainguard rejects manual edits to a binding that SCIM manages.

### Check the group attribute mapping

In the SCIM enterprise application, navigate to **Provisioning**, open the **Provisioning** page, select **Mappings**, and select **Provision Microsoft Entra ID Groups**. Confirm the following settings:

* **Enabled** is set to **Yes**.
* The **`externalId`** mapping uses **`objectId`** as its source. Chainguard identifies a group by its `externalId`, so each mapping you create later uses the group's Object ID.

Both are the defaults. Leave the other group mappings unchanged, and click **Save** if you changed anything.

{{< note >}}
Because the mapping uses the group's Object ID, renaming a group in Entra ID doesn't affect its role mappings. The Object ID is the same value Entra ID emits in the groups claim, so a mapping you already created for [claim-based group mappings](#grant-roles-from-the-groups-claim) also applies to the provisioned group.
{{< /note >}}

### Map the group to a role

Store your organization's ID in the `ORGANIZATION` variable:

```sh
export ORGANIZATION=$(chainctl iam organizations list -o json | jq -r '.items[0].id')
```

This command stores the first organization in the list. If you belong to more than one organization, run `echo $ORGANIZATION` and confirm that it's the organization you're configuring.

Then map the Entra ID group to a Chainguard role. Replace `<group_object_id>` with the group's **Object ID**, which you can find in the Entra admin center under **Entra ID** > **Groups**, and `<role_name>` with the role to grant, such as `viewer` or `editor`:

```sh
chainctl iam external-group-role-mappings create \
  --external-group-id "<group_object_id>" \
  --role <role_name> \
  --scope $ORGANIZATION \
  --idp $IDP
```

You can map only a role you hold yourself. Chainguard never grants `owner` or `support` through SCIM: it accepts a mapping to either role, but the mapping grants no access.

### Assign and provision the group

Under the SCIM enterprise application's **Users and groups**, click **+ Add user/group** and assign the group. With **Scope** set to **Sync only assigned users and groups**, Entra ID provisions the group and its members together, so the group's members also become Chainguard users.

Entra ID doesn't provision the members of nested groups. It does create a nested group in Chainguard, but with no members, so mapping it grants no roles. Assign each group that should grant a role directly to the application.

Entra ID provisions the group on its next cycle, which can take up to about 40 minutes. To provision it immediately, open **Provision on demand**, search for the group, select up to five members to provision, and click **Provision**. If you don't select any members, Entra ID provisions the group without them, and Chainguard grants no roles from it.

### Verify the role bindings

To confirm that the group reached Chainguard, list the groups Entra ID has provisioned. The output shows each group's External Id and member count, so you can check it before anyone logs in:

```sh
chainctl iam identity-providers scim groups list $IDP
```

The group's External Id is its Object ID, the same value you mapped in [Map the group to a role](#map-the-group-to-a-role).

Chainguard creates a member's role binding only after that member has logged in to Chainguard at least once, and that first login applies it immediately. After that first login, new mappings and membership changes take effect within about five minutes of reaching Chainguard. Entra ID sends membership changes on its next provisioning cycle, so allow up to about 40 minutes. **Provision on demand** sends new members immediately, but not removals.

Have a member of the group log in to Chainguard through Entra ID, then list the role bindings in your organization:

```sh
chainctl iam role-bindings list --parent $ORGANIZATION
```

The output includes a binding with the mapped role and `SCIM` in the **MANAGED BY** column. The binding's **NAME / EMAIL** column is empty, so identify the member by their identity ID instead. To look up that ID, replace `<user_principal_name>` with the member's user principal name:

```sh
chainctl iam identity-providers scim users list $IDP -o json \
  | jq -r '.[] | select(.user_name == "<user_principal_name>") | .identity_id'
```

The binding's **IDENTITY** column matches this value. If the command prints `null`, the member hasn't logged in to Chainguard yet.

To confirm that removal works, remove the member from the group in Entra ID. After the next provisioning cycle, list the role bindings again. Don't rely on **Provision on demand** here: provisioning the group skips members who are no longer in it, and provisioning the user doesn't update the group.

If you assigned the member to the application only through the group, removing them from the group also takes them out of provisioning scope, and Entra ID deactivates their Chainguard user.

### Retire a group

To stop granting roles from a group, remove the group from the SCIM enterprise application's **Users and groups**. On its next cycle, Entra ID deletes the group in Chainguard, and Chainguard removes the roles that only this group granted.

Removing the group also takes its members out of provisioning scope, unless they're assigned to the application another way, so Entra ID deactivates their Chainguard users too.

## Grant roles from the groups claim

You can also grant Chainguard roles from the groups claim in the login token, with or without SCIM. Chainguard grants these roles per session at login, and they don't appear in `chainctl iam role-bindings list`. To set this up, follow [Grant Chainguard roles from identity provider groups](/platform/administration/custom-idps/grant-roles-from-groups/).

Group membership reaches Chainguard only in tokens issued for the SSO application you registered in [Register the Entra ID application for SSO](#register-the-entra-id-application-for-sso), not the SCIM enterprise application. Assigning a group to the SCIM application provisions its members but doesn't add the group to their login tokens. If you limit the groups claim to groups assigned to the application, assign each mapped group to the SSO application as well. For the full list of Entra ID settings, refer to [Microsoft Entra ID](/platform/administration/custom-idps/grant-roles-from-groups/#microsoft-entra-id) in the group mapping guide.

Entra ID emits group Object IDs (GUIDs) rather than display names in the groups claim. As a result, a group-to-role mapping displays the group as a GUID, such as `aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee`, in both `chainctl` and the Console's group-mapping tab. To find which group an Object ID refers to, look it up in the Entra admin center under **Groups**. To display readable names instead, configure the groups claim to emit cloud-group display names.

## Deactivation and deletion

Unassigning a user from the application, disabling their account, or deleting them causes Entra ID to deactivate or delete the corresponding Chainguard identity on its next provisioning cycle. Chainguard rejects the login of a user deactivated before they ever logged in. For immediate offboarding, use **Provision on demand** on the affected user rather than waiting for the cycle.

## Troubleshooting

### A user logged in but wasn't linked

A correlation mismatch doesn't produce an error — the login proceeds as a normal, unlinked user. Confirm that you created the identity provider with `--oidc-correlation-rule=oid_equals_external_id` and `profile` in its scopes (check the saved `create` output), that the user's `externalId` is their `objectId` GUID, and that the user has logged in through the browser flow described earlier.

### Login fails, or the identity provider isn't offered

This is an SSO problem, not SCIM. Recheck the redirect URI, issuer, and client ID from the SSO application.

### Test connection fails

Confirm that the **Tenant URL** is the SCIM base URL with `?aadOptscim062020` appended and that the **Secret token** is the bare `cgscim_...` value. The URL and token must come from the same `token generate` run.

### Provisioning is quarantined

Entra ID pauses provisioning after repeated errors. Fix the error shown in the provisioning logs and restart provisioning.

## Related resources

* [Provision Chainguard users with SCIM](/platform/administration/custom-idps/scim-provisioning/scim-overview/)
* [Grant Chainguard roles from identity provider groups](/platform/administration/custom-idps/grant-roles-from-groups/)
* [Overview of the Chainguard IAM model](/platform/administration/iam-organizations/overview-of-chainguard-iam-model/)
