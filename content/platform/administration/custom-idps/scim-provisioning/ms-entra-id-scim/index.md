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
* An Entra ID account with Global Administrator or Application Administrator permissions. Without these, you cannot register applications or assign users to them.
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
  --default-role=viewer \
  -o json
```

`chainctl` installs the provider in your organization automatically when you belong to only one. If you have access to more than one, add `--parent=<organization_id>` to choose where it is installed.

This `create` command includes two options specific to SCIM linking with Entra ID:

* `--oidc-correlation-rule=oid_equals_external_id` links each login to its provisioned user by the Entra ID `oid` claim. It is immutable — to change it, delete and recreate the identity provider. Confirm it appears in the command's JSON output, and keep that output as your record of the setting.
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

* **Secret token**: The bare `cgscim_...` token. Do not add a `Bearer` prefix — Entra ID adds the scheme itself.

Click **Test connection** to confirm the URL and token — the test must succeed — then **Save**.

### Map externalId to objectId

Navigate to the **Attribute mapping** tab and select **Users**. Edit the mapping whose **Target attribute** is **`externalId`**, and change its **Source attribute** from the default (`mailNickname`) to **`objectId`** (`objectId` is in the source-attribute dropdown). Leave the mapping type as **Direct**, then click **Apply**.

Entra ID doesn't apply any change on this page, including added or deleted mappings, until you click **Save** at the bottom of the **Attribute mapping** page. Click **Save** after the edits in this section.

{{< note >}}
Make this change before provisioning any user, including with **Provision on demand**. `objectId` is the value the identity provider matches against at login, so a user provisioned under the default `mailNickname` mapping isn't linked when they log in. If you've already provisioned users, refer to [A user logged in but wasn't linked](#a-user-logged-in-but-wasnt-linked). Map `externalId` only to `objectId` — a user-editable or non-unique attribute could link a login to the wrong identity.
{{< /note >}}

Keep the default `emails[type eq "work"].value` mapping in place; Chainguard stores it. Entra ID's default mappings also use value filters on other attributes, such as `addresses[type eq "work"].streetAddress` and `phoneNumbers[type eq "work"].value`. Chainguard accepts these without storing them, so you can leave them or delete them.

Chainguard stores `userName`, `externalId`, `displayName`, `active`, and the `name` sub-attributes (`givenName`, `familyName`, and `formatted`). It accepts other mapped attributes, such as `title` and the enterprise extension attributes, without storing them, so Entra ID reports them as synced even though Chainguard keeps no copy. Delete mappings you don't need to keep the sync quiet.

Keep the plain-path mappings. Entra ID uses the `userName` mapping, which has matching precedence 1, to look up an existing Chainguard user before it creates one. `active` maps through the default expression `Switch([IsSoftDeleted], , "False", "True", "True", "False")`, which inverts `IsSoftDeleted` so that a user Entra ID soft-deletes or unassigns arrives at Chainguard as inactive — this is what drives deactivation. Leave the mappings on the **Groups** tab at their defaults.

### Provision users under their email address

By default, `userName` maps from `userPrincipalName`. If your users' `userPrincipalName` and email addresses use different domains, change the `userName` mapping's **Source attribute** from `userPrincipalName` to **`mail`** so Chainguard provisions each user under their email address, then click **Save**.

{{< note >}}
Set this before provisioning any user. Changing it later renames the existing Chainguard users to the new value — the same users, linked the same way, because linking uses `externalId`.

Entra ID only syncs a user that has a value for the `userName` source attribute. A user with no `mail` value is skipped, and **Provision on demand** reports the user as skipped because it has no value for the matching attribute. Make sure every user you assign has a `mail` value.
{{< /note >}}

### Assign users and turn on provisioning

Under the application's **Users and groups**, assign the users to provision. Assigning a group to the application requires Entra ID P1 or P2; without it, Entra ID shows "Groups are not available for assignment due to your Active Directory plan level", and you assign users individually.

On the **Provisioning** page, set **Provisioning Mode** to **Automatic**, and under **Settings** set **Scope** to **Sync only assigned users and groups**. Then set **Provisioning Status** to **On** and click **Save** to begin.

Entra ID runs its provisioning cycle about every 40 minutes. While testing, use **Provision on demand** to push a user immediately. It shows each step — import, scope, match, and perform action — and **View details** on a step lists the attribute values Entra ID sent and any error Chainguard returned.

## Verify the integration

Provision a user, then query the SCIM API to confirm the user's `externalId` is their `objectId` — a lowercase GUID, not a mail nickname. Replace `<scim_token>` and `<scim_base_url>` with the bearer token and SCIM base URL from the `token generate` command.

```sh
curl -s -H "Authorization: Bearer <scim_token>" "<scim_base_url>/Users?count=5"
```

Then have that user log in at [console.chainguard.dev](https://console.chainguard.dev): click **Use Your Identity Provider**, then **Use Your Organization Name**, enter your organization name, and click **Login with Provider**. The first login must go through this browser flow for linking to complete. Afterward the user is linked to their provisioned record. Enabling SCIM clears the identity provider's default role, so a provisioned user has no role in your organization until you grant one, for example with a role binding or with a [group mapping](/platform/administration/custom-idps/grant-roles-from-groups/).

## Push groups to grant roles

Entra ID can push the groups you assign to the SCIM application to Chainguard. Chainguard matches each pushed group against your group-to-role mappings and grants the mapped roles to the group's members as role bindings. These bindings persist between logins, unlike the session-scoped roles that [claim-based group mappings](#grant-roles-from-the-groups-claim-instead) grant, and they appear in `chainctl iam role-bindings list`.

You manage these bindings from Entra ID. To change who holds a role, change the group's membership in Entra ID; Chainguard rejects manual edits to a binding that SCIM manages.

### Assign the group to the SCIM application

Under the SCIM application's **Users and groups**, click **Add user/group** and assign the group. Assigning a group requires Entra ID P1 or P2. Entra ID pushes the group with its members, and provisions each member as a Chainguard user. Entra ID pushes membership only for users who are in scope for the application, which assigning the group takes care of.

Leave the mappings on the **Attribute mapping** page's **Groups** tab at their defaults. Chainguard identifies each group by its Entra ID Object ID, which the default mapping sends as `externalId`, so renaming a group in Entra ID doesn't affect the roles it grants.

To push the group immediately instead of waiting for the next provisioning cycle, use **Provision on demand**, select the group, and select the members to include. Provisioning a group on demand with no members selected pushes the group alone; its members follow on the next cycle.

### Map the group to a role

Store your organization's UIDP in the `ORGANIZATION` variable:

```sh
export ORGANIZATION=$(chainctl iam organizations list -o json | jq -r '.items[0].id')
```

This command stores the first organization in the list. If you belong to more than one organization, run `echo $ORGANIZATION` and confirm that it's the organization you're configuring.

Then map the group to a Chainguard role. Replace `<group_object_id>` with the group's **Object ID** from the Entra admin center under **Groups**, and `<role_name>` with the role to grant, such as `viewer` or `editor`:

```sh
chainctl iam external-group-role-mappings create \
  --external-group-id "<group_object_id>" \
  --role <role_name> \
  --scope $ORGANIZATION \
  --idp ${IDP}
```

You can map only a role you hold yourself. Chainguard never creates an `owner` or `support` role binding through SCIM: it accepts a mapping to either role, but a pushed group grants neither.

### Verify the role bindings

To confirm that the group reached Chainguard, list the groups Entra ID has pushed. The output shows each group's name and member count, so you can check it before anyone logs in:

```sh
chainctl iam identity-providers scim groups list ${IDP}
```

Chainguard creates a member's role binding only after that member has logged in to Chainguard at least once, and that first login applies it immediately. After that, membership changes in Entra ID take effect as soon as Entra ID pushes them, and a mapping you create for a group Chainguard already has takes effect within about five minutes, without another login.

Have a member of the group log in to Chainguard, then list the role bindings in your organization:

```sh
chainctl iam role-bindings list --parent $ORGANIZATION -o table
```

The output includes a binding with the mapped role and `SCIM` in the **MANAGED BY** column. The binding's **NAME / EMAIL** column is empty, so identify the member by their identity ID instead. To look up that ID, replace `<user_principal_name>` with the member's `userName` in Chainguard, which is their user principal name unless you [provision users under their email address](#provision-users-under-their-email-address):

```sh
chainctl iam identity-providers scim users list ${IDP} -o json \
  | jq -r '.[] | select(.user_name == "<user_principal_name>") | .identity_id'
```

The binding's **IDENTITY** column matches this value. If the command prints `null`, the member hasn't logged in to Chainguard yet, or their login wasn't linked; refer to [A user logged in but wasn't linked](#a-user-logged-in-but-wasnt-linked).

To confirm that removal works, remove the member from the group in Entra ID and use **Provision on demand** on the group, then list the role bindings again. Chainguard deletes the binding as soon as Entra ID pushes the change. A member of several mapped groups keeps a role until they leave the last group that grants it.

### Retire a group

To stop granting roles from a group, remove the group from the SCIM application's **Users and groups**. On its next push, Entra ID deletes the group in Chainguard, and Chainguard removes the roles that only this group granted.

Deleting a group doesn't deprovision its members, and it doesn't delete the group's role mappings. If you assign the same Entra ID group to the application again, its mappings apply again. To stop a mapping from granting access permanently, delete it with `chainctl iam external-group-role-mappings delete`.

### Grant roles from the groups claim instead

You can instead grant roles from the groups claim in each user's login token, as described in [Grant Chainguard roles from identity provider groups](/platform/administration/custom-idps/grant-roles-from-groups/). These roles last only for the user's session and don't appear as role bindings.

The groups claim comes from the SSO application you registered in [Register the Entra ID application for SSO](#register-the-entra-id-application-for-sso), not the SCIM enterprise application. Assigning a group to the SCIM application doesn't add the group to users' login tokens. If you limit the groups claim to groups assigned to the application, assign each mapped group to the SSO application as well. For the full list of Entra ID settings, refer to [Microsoft Entra ID](/platform/administration/custom-idps/grant-roles-from-groups/#microsoft-entra-id) in the group mapping guide.

Entra ID emits group Object IDs (GUIDs) rather than display names in the groups claim. As a result, a group-to-role mapping displays the group as a GUID, such as `aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee`, in both `chainctl` and the console's group-mapping tab. To find which group an Object ID refers to, look it up in the Entra admin center under **Groups**. To display readable names instead, configure the groups claim to emit cloud-group display names.

## Deactivation and deletion

Unassigning a user from the application, disabling their account, or deleting them causes Entra ID to deactivate or delete the corresponding Chainguard identity on its next provisioning cycle. Chainguard rejects the login of a user deactivated before they ever logged in. For immediate offboarding, use **Provision on demand** on the affected user rather than waiting for the cycle.

## Troubleshooting

### A user logged in but wasn't linked

A correlation mismatch does not error — the login proceeds as a normal, unlinked user. The user reaches the Chainguard Console but is asked to create an organization or sees no organization, and in your organization's user list they still show **Pending sign-in**. Roles from group mappings don't apply to an unlinked user.

Confirm that you created the identity provider with `--oidc-correlation-rule=oid_equals_external_id` and `profile` in its scopes (check the saved `create` output), that the user's `externalId` is their `objectId` GUID, and that the user has logged in through the browser flow described earlier.

If the user's `externalId` is their mail nickname, the `externalId` mapping still uses the default source. Change it to `objectId` as described in [Map externalId to objectId](#map-externalid-to-objectid), then use **Provision on demand** on the user; the **Perform action** step shows `externalId` updated to the GUID. Have the user log out of the Chainguard Console and log in again. That login links them, and their roles apply.

### Login fails, or the identity provider isn't offered

This is an SSO problem, not SCIM. Recheck the redirect URI, issuer, and client ID from the SSO application.

### A user isn't provisioned

**Provision on demand** reports the user as skipped, or the user never appears in Chainguard. The source attribute of the `userName` mapping — `userPrincipalName` by default, or `mail` if you remapped it — has no value for that user. Set the attribute on the user in Entra ID, then provision the user again.

### Provisioning fails with a `400` error

The error names `invalidPath`. A mapping's **Target attribute** names an attribute that isn't part of the SCIM user schema, such as a misspelled or custom attribute. Correct or delete the mapping, click **Save** on the **Attribute mapping** page, and provision the user again.

### Provisioning reports a `409` error

Entra ID shows the error code `SystemForCrossDomainIdentityManagementServiceIncompatibleFiltering` for these errors. Chainguard's message is in the **Web Response** of the provisioning log entry.

* **The message names `uniqueness` for a user:** Chainguard already has this user, for example because an earlier create succeeded but Entra ID didn't receive the response. Run **Provision on demand** for the user. Entra ID looks the user up first and links the existing record.
* **The message says the change would deactivate the organization's last active privileged owner:** Entra ID tried to deactivate the only remaining owner of your organization, and Chainguard kept them active. Grant the owner role to another person directly with a role binding, then provision the user again.
* **The message names `uniqueness` for a group and says its correlation key is already provisioned to a group with another name:** Chainguard already has this group under the name it had before it was renamed in Entra ID, and Entra ID no longer has the record linked, for example because the provisioning configuration or the application was recreated. In Entra ID, rename the group to the name in the message and use **Provision on demand** on the group, which links the existing record. Then rename the group back and provision it again.

### Test connection fails

Confirm the Tenant URL is the SCIM base URL with `?aadOptscim062020` appended and the Secret token is the bare `cgscim_...` value. The URL and token must come from the same `token generate` run.

**Provisioning is quarantined.** Entra ID pauses provisioning after repeated errors. Fix the error shown in the provisioning logs and restart provisioning.

## Related resources

* [Provision Chainguard users with SCIM](/platform/administration/custom-idps/scim-provisioning/scim-overview/)
* [Grant Chainguard roles from identity provider groups](/platform/administration/custom-idps/grant-roles-from-groups/)
* [Overview of the Chainguard IAM model](/platform/administration/iam-organizations/overview-of-chainguard-iam-model/)
