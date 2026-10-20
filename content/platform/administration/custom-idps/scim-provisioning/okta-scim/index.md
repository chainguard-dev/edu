---
title: "How to provision users into Chainguard from Okta with SCIM"
linktitle: "Okta SCIM configuration"
lead: ""
description: "Procedural tutorial on how to set up SCIM provisioning from Okta to the Chainguard platform."
type: "article"
date: 2026-08-14T00:00:00+00:00
lastmod: 2026-10-15T00:00:00+00:00
draft: false
tags: ["Procedural"]
images: []
weight: 20
---

The Chainguard platform supports SCIM 2.0 provisioning from Okta. With SCIM enabled, Okta creates, updates, and deactivates Chainguard users as you assign and unassign them, and Chainguard links each provisioned user to their single sign-on (SSO) login automatically.

This guide covers the Okta-specific setup. For provisioning behavior, token lifecycle, and limits, refer to [Provision Chainguard users with SCIM](/platform/administration/custom-idps/scim-provisioning/scim-overview/).

## Prerequisites

To complete this guide, you need the following:

* Okta already configured for login to Chainguard through an OIDC app integration. If you haven't set that up yet, refer to our guide on [How to integrate Okta SSO with Chainguard](/platform/administration/custom-idps/idp-providers/okta/).
* The [prerequisites for SCIM provisioning](/platform/administration/custom-idps/scim-provisioning/scim-overview/#prerequisites): an IAM role that can manage identity providers, at least one owner who can sign in and holds the owner role directly, and an authenticated `chainctl`.

The rest of this guide refers to your identity provider by its UIDP, stored in the `IDENTITY_PROVIDER` environment variable:

```sh
export IDENTITY_PROVIDER=$(chainctl iam identity-providers list -o json | jq -r '.items[0].id')
```

Organizations generally have one identity provider, so the list usually holds a single entry and the `.items[0].id` filter selects it. If the list holds more than one — because you belong to several organizations, or your organization has several providers — run `chainctl iam identity-providers list` on its own and set `IDENTITY_PROVIDER` to the UIDP of the provider you are configuring.

## Step 1: Enable provisioning and generate the SCIM token

First, generate the bearer token Okta authenticates with:

```sh
chainctl iam identity-providers scim token generate $IDENTITY_PROVIDER
```

The `token generate` command prints the token to standard output and the SCIM endpoint URL to standard error. Chainguard shows the token exactly once, so keep both values for Step 2. Our guide [Provision Chainguard users with SCIM](/platform/administration/custom-idps/scim-provisioning/scim-overview/#the-scim-token) outlines lifetime options and rotation.

Next, enable SCIM for your identity provider:

```sh
chainctl iam identity-providers scim enable $IDENTITY_PROVIDER
```

Generate the token first: `scim enable` fails with `etag: etag is required` if the identity provider has no token issued yet. If it instead fails with a message about owner-tier identities, your organization has no owner who can sign in and holds the owner role directly; refer to the [prerequisites for SCIM provisioning](/platform/administration/custom-idps/scim-provisioning/scim-overview/#prerequisites).

Enabling SCIM clears the identity provider's default role. If you set one with `--default-role`, the **DEFAULT ROLE** column in `chainctl iam identity-providers list` is empty afterward.

## Step 2: Create the Okta provisioning app

Okta hosts SCIM provisioning on an app integration, but you cannot add SCIM to the OIDC app integration you use for login. This means you must create a second app integration that exists only to carry provisioning.

In the Okta Admin Console, navigate to the **Applications** landing page, click **Create App Integration**, and choose **SAML 2.0**. Chainguard doesn't use the SAML assertion, and sign-in stays on your existing OIDC app, so the wizard's SAML settings need only well-formed URLs. Enter placeholder values like `https://example.com/sso` for **Single sign-on URL** and `https://example.com/saml` for **Audience URI (SP Entity ID)**, and leave the other settings at their defaults. On the new app's **General** tab, under **App Settings**, set **Provisioning** to **SCIM**.

Then open the app's **Provisioning** tab, select **Integration**, and click **Edit** to configure the SCIM connection:

* **SCIM connector base URL**: the endpoint printed in Step 1.
* **Unique identifier field for users**: `userName`.
* **Supported provisioning actions**: select **Push New Users**, **Push Profile Updates**, and **Push Groups**. You need **Push Groups** only if you plan to grant roles from Okta groups, as described in [Step 5](#step-5-push-groups-to-grant-roles).
* **Authentication Mode**: select **HTTP Header**, then paste the bare `cgscim_...` token into the **Bearer** field. Do not add a `Bearer` prefix — Okta supplies the scheme itself, and a prefixed value fails authentication.

Use **Test API Credentials** to confirm the URL and token, then save.

### Error authenticating: No results for users returned

Okta's connection test reads the SCIM endpoint and expects to find a user it recognizes there. A newly enabled Chainguard endpoint has no users yet, so on a first-time setup the test fails with this message. Despite the wording, authentication succeeded; the missing user is what blocks the save.

A workaround is to create the first user directly, then run the test again. Replace `<scim_token>` and `<scim_endpoint_url>` with the bearer token and endpoint URL for your identity provider, and `<okta_username>` and `<okta_user_id>` with the details of a real user you intend to provision.

```sh
curl -X POST \
  -H "Authorization: Bearer <scim_token>" \
  -H "Content-Type: application/scim+json" \
  -d '{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "userName": "<okta_username>",
    "externalId": "<okta_user_id>",
    "active": true
  }' \
  "<scim_endpoint_url>/Users"
```

Set `externalId` to the user's Okta ID — the `00u...` value in the page URL when you open that user under **Directory** > **People**. Okta's test rejects an arbitrary value even though the endpoint returns the user, so this is not a field you can fill with a placeholder. `externalId` is also what Chainguard matches against at login, and a wrong value leaves the user unlinked with no error, so seed a real user you intend to provision.

## Step 3: Enable provisioning actions

With the integration saved, select **To App** in the **Provisioning** tab, click **Edit**, and enable **Create Users**, **Update User Attributes**, and **Deactivate Users**. These options appear only after you save the connection, and only for the actions you checked under **Supported provisioning actions** in Step 2.

## Step 4: Assign users and verify

In Okta, assign a user to the provisioning app integration you created in Step 2. Okta provisions them immediately. Have that user log in to Chainguard through Okta and confirm they have access. A provisioned user connects to their login by matching the SCIM `externalId` against the login token's subject; with Okta, both default to the Okta user ID, so they align without configuration.

To confirm the rest of the lifecycle, deactivate that user in Okta or remove their assignment, and confirm that Chainguard refuses their next login. Then reactivate them and confirm that they can log in again.

## Step 5: Push groups to grant roles

Okta can also push groups to Chainguard. Chainguard matches each pushed group against your group-to-role mappings and grants the mapped roles to the group's members as role bindings. These bindings persist between logins, unlike the session-scoped roles that [claim-based group mappings](/platform/administration/custom-idps/grant-roles-from-groups/) grant, and they appear in `chainctl iam role-bindings list`.

You manage these bindings from Okta. To change who holds a role, change the group's membership in Okta; Chainguard rejects manual edits to a binding that SCIM manages.

### Map the group to a role

Store your organization's UIDP in the `ORGANIZATION` variable:

```sh
export ORGANIZATION=$(chainctl iam organizations list -o json | jq -r '.items[0].id')
```

This command stores the first organization in the list. If you belong to more than one organization, run `echo $ORGANIZATION` and confirm that it's the organization you're configuring.

Then map the Okta group to a Chainguard role. Replace `<okta_group_name>` with the group's name exactly as it appears in Okta, and `<role_name>` with the role to grant, such as `viewer` or `editor`:

```sh
chainctl iam external-group-role-mappings create \
  --external-group-id "<okta_group_name>" \
  --role <role_name> \
  --scope $ORGANIZATION \
  --idp $IDENTITY_PROVIDER
```

You can map only a role you hold yourself. Chainguard never grants `owner` or `support` through SCIM: it accepts a mapping to either role, but the mapping grants no access.

{{< note >}}
Okta doesn't send a stable identifier for groups, so Chainguard identifies a group by its name the first time it is pushed, matched exactly including case. If you rename the group in Okta, the mapping keeps working under the original name, so keep using the original name in mappings. You can't reuse the original name for a new group until you unlink the original with **Delete the group in the target app**.
{{< /note >}}

### Push the group from Okta

To push the group from Okta, follow these steps:

1. If you set up the provisioning app before group push was available, open its **Provisioning** tab, select **Integration**, click **Edit**, and select **Push Groups** under **Supported provisioning actions**.
2. On the provisioning app's **Assignments** tab, click **Assign** > **Assign to Groups**, and assign the group. Okta pushes group membership only for users assigned to the app, and assigning the group also provisions its members as Chainguard users.
3. On the **Push Groups** tab, click **Push Groups** > **Find groups by name**, and enter the group's name.
4. Leave **Push group memberships immediately** selected, and click **Save**.

The group's **Push Status** changes to **Active** once Okta has pushed it.

### Verify the role bindings

To confirm that the group reached Chainguard, list the groups Okta has pushed. The output shows each group's name and member count, so you can check it before anyone logs in:

```sh
chainctl iam identity-providers scim groups list $IDENTITY_PROVIDER
```

Chainguard creates a member's role binding only after that member has logged in to Chainguard at least once, and that first login applies it immediately. After that first login, new mappings and membership changes in Okta take effect within about five minutes, without another login.

To confirm that Okta provisioned the group's members, list the users it has pushed. Members who haven't logged in yet show `no` in the **LOGGED IN** column:

```sh
chainctl iam identity-providers scim users list $IDENTITY_PROVIDER
```

Have a member of the group log in to Chainguard through Okta, then list the role bindings in your organization:

```sh
chainctl iam role-bindings list --parent $ORGANIZATION
```

The output includes a binding with the mapped role and `SCIM` in the **MANAGED BY** column. The binding's **NAME / EMAIL** column is empty, so identify the member by their identity ID instead. To look up that ID, replace `<okta_username>` with the member's Okta username:

```sh
chainctl iam identity-providers scim users list $IDENTITY_PROVIDER -o json \
  | jq -r '.[] | select(.user_name == "<okta_username>") | .identity_id'
```

The binding's **IDENTITY** column matches this value. If the command prints `null`, the member hasn't logged in to Chainguard yet.

To confirm that removal works, remove the member from the group in Okta, then list the role bindings again. Chainguard deletes the binding within about five minutes.

If you assigned the member to the provisioning app only through the group, removing them from the group also deactivates their Chainguard user. Okta deactivates the user without sending a membership removal, so Chainguard keeps their group membership, and the user can get the group's role back a few minutes after they're reactivated. To prevent this, open the **Push Groups** tab and select **Push now** from the group's **Push Status** menu before you reactivate the user. Okta then sends the group's current membership, and Chainguard removes the user from the group.

### Retire a group

To stop granting roles from a group, open the **Push Groups** tab and select **Unlink pushed group** from the group's **Push Status** menu. Okta offers two options:

* **Delete the group in the target app**: Chainguard deletes the group and removes the roles that only this group granted.
* **Leave the group in the target app**: Okta sends nothing, so the group and its roles stay as they were. Members you later remove from the group in Okta keep their roles.

Deleting a group doesn't deprovision its members. To remove a member's Chainguard access, unassign them from the provisioning app.

## Troubleshooting

### A user logged in but wasn't linked

A provisioning mismatch does not produce an error; the login proceeds as a normal, unlinked user. Confirm that you assigned the user to the provisioning app and that Okta provisioned them (check the app's assignment and Okta's provisioning logs), and that the app sends the default Okta user ID as `externalId`.

### Test API Credentials fails

If the message is "No results for users returned," refer to [Error authenticating: No results for users returned](#error-authenticating-no-results-for-users-returned) in Step 2. Otherwise, confirm the base URL is the endpoint printed by `token generate` and that the **Bearer** field holds the correct `cgscim_...` token. The URL and token must come from the same `token generate` run.

### Provisioning requests receive HTTP `429`

Chainguard rate limits provisioning writes; Okta retries on its own schedule, so bulk assignments complete without intervention. For more information, refer to the [Limits section](/platform/administration/custom-idps/scim-provisioning/scim-overview/#limits).

## Related resources

* [Provision Chainguard users with SCIM](/platform/administration/custom-idps/scim-provisioning/scim-overview/)
* [Grant Chainguard roles from identity provider groups](/platform/administration/custom-idps/grant-roles-from-groups/)
* [How to integrate Okta SSO with Chainguard](/platform/administration/custom-idps/idp-providers/okta/)
* [Overview of the Chainguard IAM model](/platform/administration/iam-organizations/overview-of-chainguard-iam-model/)
