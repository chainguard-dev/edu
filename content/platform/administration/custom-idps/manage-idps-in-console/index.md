---
title: "Manage custom identity providers in the Chainguard Console"
linktitle: "Manage IdPs in the Console"
lead: ""
description: "How to create, update, and delete a custom identity provider in the Chainguard Console, map IdP groups to roles, and set up SCIM provisioning."
type: "article"
date: 2026-10-21T08:48:45+00:00
lastmod: 2026-10-21T08:48:45+00:00
draft: false
tags: ["Chainguard Containers", "Procedural"]
images: []
weight: 15
---

Rather than using `chainctl`, you can manage your organization's custom identity provider (IdP) from [the Chainguard Console](/platform/console/). The Console lets you create, update, and delete the identity provider, map IdP groups to Chainguard roles, and set up SCIM provisioning.

The Console manages one identity provider per organization. If you need more than one, or want to script these tasks, use the [`chainctl iam identity-providers` commands](/platform/chainctl/chainctl-docs/chainctl_iam_identity-providers/) instead.

## Prerequisites

To follow this guide, you need the following:

- An OIDC application registered with your identity provider, and its issuer URL, client ID, and client secret. To register one, follow the guide for your provider, such as [Okta](/platform/administration/custom-idps/idp-providers/okta/) or [Microsoft Entra ID](/platform/administration/custom-idps/idp-providers/ms-entra-id/), up to the step where you configure Chainguard. For any other provider, follow the [generic integration guide](/platform/administration/custom-idps/custom-idps/#generic-integration-guide).
- A role in your Chainguard organization with the identity provider capabilities, such as the `owner` role. Setting up SCIM also requires the `identity_providers.scim.manage` capability. Without the required capability, the Console shows the matching buttons as unavailable.

## Open the Identity Provider page

1. Log in to the [Chainguard Console](https://console.chainguard.dev).
2. In the left-hand navigation menu, click **Settings**.
3. In the **Settings** menu, click **Identity Provider**.

The **Identity Provider** page has three tabs:

- **IdP details** lets you create, update, or delete an identity provider and shows its configuration.
- **SCIM syncing** lets you set up SCIM provisioning. This tab becomes available after you create an identity provider.
- **Groups** lets you map IdP groups to Chainguard roles. This tab becomes available after you turn on group-based role mapping for the identity provider.

## Create an identity provider

1. On the **IdP details** tab, click **Create identity provider**.
2. Fill in the form. The following table describes each field.
3. Click **Create**. The button becomes available when every required field contains a valid entry.

| Field | Required | Description |
| :---- | :---- | :---- |
| **Name** | Yes | A name for the identity provider, up to 64 characters. It can contain lowercase letters, numbers, spaces, periods, hyphens, and underscores. |
| **Description** | No | Further context on the identity provider. |
| **Issuer** | Yes | The issuer URL of your identity provider. |
| **Client ID** | Yes | The client ID of the OIDC application. |
| **Client secret** | Yes | The client secret of the OIDC application. |
| **Default role** | Yes | The role that users who log in through this identity provider receive by default, such as `viewer`. For more about this choice, refer to [IAM and security](/platform/administration/custom-idps/custom-idps/#iam-and-security). |
| **Scopes** | Yes | The scopes Chainguard requests from your identity provider. The form requires `openid` and `email`. |
| **Correlation rule** | Yes | How Chainguard matches logins to users provisioned with SCIM. Keep the default, **Subject (sub = externalId)**, unless your identity provider is Microsoft Entra ID, in which case choose **Microsoft Entra ID (oid = externalId)** and add the `profile` scope. You can't change this value after you create the identity provider. |
| **Enable group-based role mapping** | No | Select this to grant roles based on your users' IdP groups. Selecting it shows the **Groups claim** field. |
| **Groups claim** | Conditional | Required if you selected **Enable group-based role mapping**. The name of the token claim in which your identity provider sends group memberships, such as `groups`. |

When you select **Enable group-based role mapping**, the Console adds the `groups` scope to **Scopes**. Microsoft Entra ID rejects that scope, so the Console doesn't add it when your issuer is an Entra ID URL, and it blocks the form if you add it yourself. Entra ID sends the groups claim without the scope.

After you create the identity provider, users can log in with it. Refer to [Authenticate with `chainctl`](/platform/administration/custom-idps/custom-idps/#authenticate-with-chainctl) and [Authenticate with the Chainguard Console](/platform/administration/custom-idps/custom-idps/#authenticate-with-the-chainguard-console). The Console doesn't display the identity provider's ID, which `chainctl auth login --identity-provider` requires. To find the ID, run `chainctl iam identity-providers list`. If your organization is [verified](/platform/administration/iam-organizations/verified-orgs/), users can log in with the organization name instead.

## Update an identity provider

1. On the **IdP details** tab, click **Update**.
2. Edit the fields you need to change. You can edit every field except **Correlation rule**.
3. Click **Update**.

The **Client secret** field is empty when the form opens, because Chainguard doesn't display the existing secret. Leave it empty to keep the current secret. To rotate the secret, enter the new value.

If the identity provider uses Microsoft Entra ID and its scopes include `groups`, the form shows a warning and blocks **Update** until you remove `groups` from **Scopes**.

## Map IdP groups to roles

Group mappings grant Chainguard roles to users based on the groups your identity provider sends. Before you create mappings, configure your identity provider to send a groups claim, as described in the "Step 1: Emit group membership from your IdP" section of [Grant Chainguard roles from identity provider groups](/platform/administration/custom-idps/grant-roles-from-groups/#step-1-emit-group-membership-from-your-idp). That guide also explains how mapped roles behave and how quickly changes take effect.

To turn on group mappings, [update the identity provider](#update-an-identity-provider): select **Enable group-based role mapping** and enter the **Groups claim**. Then open the **Groups** tab.

### Add a group mapping

1. On the **Groups** tab, click **Add group mapping**.
2. In **IdP group name**, enter the group value your identity provider sends: the group name for Okta, or the group Object ID for Entra ID unless you configured it to send names.
3. In **Chainguard role**, select the role to grant. You can map a group only to a role that you hold yourself.
4. Click **Add group mapping**.

To grant a group more than one role, add one mapping for each role.

### Set the default role

The **Default Chainguard role** card on the **Groups** tab sets the role for users who don't match any group mapping. Select a role, or select **No role** to grant nothing to unmatched users. The Console saves the change right away.

### Delete group mappings

To delete one mapping, hover over its row on the **Groups** tab, click the delete icon, type the group name to confirm, and click **Delete group mapping**. Users in that group stop receiving the role.

To delete every mapping for the identity provider, go to the **IdP details** tab and click **Reset group mappings**. Type `reset mappings` to confirm, and click **Reset group mappings**. Users then receive only the default role.

## Set up SCIM provisioning

SCIM provisioning lets your identity provider create and deactivate users in Chainguard. Before you start, read [Provision Chainguard users with SCIM](/platform/administration/custom-idps/scim-provisioning/scim-overview/), which explains how provisioning works and what it requires. In particular, your organization needs an owner who can log in and whose `owner` role is assigned directly, not through SCIM or a group mapping.

### Turn on SCIM syncing

1. On the **SCIM syncing** tab, click **Enable**. The Console generates a token and turns on provisioning.
2. Copy the **SCIM endpoint** and **Bearer token** values. The Console shows the token only once.
3. Click **Continue**.
4. Enter the endpoint and token in your identity provider, following the [Okta](/platform/administration/custom-idps/scim-provisioning/okta-scim/) or [Microsoft Entra ID](/platform/administration/custom-idps/scim-provisioning/ms-entra-id-scim/) SCIM guide.

While SCIM is on, the identity provider's default role is optional. Users without one get no role until a group mapping or role binding grants one.

### Rotate the token

1. On the **SCIM syncing** tab, enter the number of hours in **Token overlap (Hours)**. The current token keeps working for that long while you update your identity provider. The default is 1, the maximum is 24, and 0 switches to the new token immediately.
2. Click **Regenerate token**.
3. Copy the new token and enter it in your identity provider.

### Revoke the token

If you think the token is exposed, click **Revoke token** on the **SCIM syncing** tab and confirm. Revoking immediately invalidates every SCIM token for the identity provider, including one still active from a rotation. Provisioning stops until you regenerate a token and enter it in your identity provider.

### Turn off SCIM syncing

On the **SCIM syncing** tab, click **Disable** and confirm. Chainguard refuses provisioning requests until you click **Enable** again. Existing users, groups, and role assignments stay in place.

## Delete an identity provider

Deleting an identity provider stops provisioning from it and revokes access for anyone whose membership depends on it. You can't undo the deletion. Before you delete it, make sure someone can still log in to your organization another way, such as with a [backup account](/platform/administration/custom-idps/custom-idps/#backup-accounts).

1. On the **IdP details** tab, click **Delete**.
2. Type `delete <idp_name>` to confirm, replacing `<idp_name>` with the identity provider's name.
3. Click **Delete IdP**.

## Related resources

- [Using custom identity providers to authenticate to Chainguard](/platform/administration/custom-idps/custom-idps/)
- [Grant Chainguard roles from identity provider groups](/platform/administration/custom-idps/grant-roles-from-groups/)
- [Provision Chainguard users with SCIM](/platform/administration/custom-idps/scim-provisioning/scim-overview/)
- [`chainctl iam identity-providers` reference](/platform/chainctl/chainctl-docs/chainctl_iam_identity-providers/)
