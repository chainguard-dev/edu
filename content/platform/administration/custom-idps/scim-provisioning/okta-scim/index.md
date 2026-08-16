---
title: "How to provision users into Chainguard from Okta with SCIM"
linktitle: "Okta SCIM configuration"
lead: ""
description: "Procedural tutorial on how to set up SCIM provisioning from Okta to the Chainguard platform."
type: "article"
date: 2026-08-14T00:00:00+00:00
lastmod: 2026-08-14T00:00:00+00:00
draft: false
tags: ["Procedural"]
images: []
weight: 039
---

{{< beta feature="SCIM user provisioning" >}}

The Chainguard platform supports SCIM 2.0 provisioning from Okta. With SCIM enabled, Okta creates, updates, and deactivates Chainguard users as you assign and unassign them, and Chainguard links each provisioned user to their single sign-on (SSO) login automatically.

This guide covers the Okta-specific setup. For provisioning behavior, token lifecycle, and limits, refer to [Provision Chainguard users with SCIM](/platform/administration/custom-idps/scim-provisioning/scim-overview/).

## Prerequisites

To complete this guide, you need the following:

* Okta already configured for login to Chainguard through an OIDC app integration. If you haven't set that up yet, refer to our guide on [How to integrate Okta SSO with Chainguard](/platform/administration/custom-idps/idp-providers/okta/).
* The [prerequisites for SCIM provisioning](/platform/administration/custom-idps/scim-provisioning/scim-overview/#prerequisites): an IAM role that can manage identity providers, two owners with directly assigned role bindings, and an authenticated `chainctl`.

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

Generate the token first: `scim enable` fails with `etag: etag is required` if the identity provider has no token issued yet. If it instead fails with a message about owner-tier identities, your organization doesn't yet have two directly assigned owners; refer to the [prerequisites for SCIM provisioning](/platform/administration/custom-idps/scim-provisioning/scim-overview/#prerequisites).

## Step 2: Create the Okta provisioning app

Okta hosts SCIM provisioning on an app integration, but you cannot add SCIM to the OIDC app integration you use for login. This means you must create a second app integration that exists only to carry provisioning.

In the Okta Admin Console, navigate to **Applications and Resources** > **Applications**, click **Create App Integration**, and choose **SAML 2.0**. Complete the wizard with placeholder values; Chainguard does not consume the SAML assertion, and sign-in stays on your existing OIDC app. On the new app's **General** tab, set **Provisioning** to **SCIM**.

Then open the app's **Provisioning** tab, select **Integration**, and click **Edit** to configure the SCIM connection:

* **SCIM connector base URL**: the endpoint printed in Step 1.
* **Unique identifier field for users**: `userName`.
* **Supported provisioning actions**: check **Push New Users** and **Push Profile Updates**. Leave **Push Groups** unchecked; Chainguard's SCIM endpoint accepts user provisioning only.
* **Authentication Mode**: select **HTTP Header**, then paste the bare `cgscim_...` token into the **Bearer** field. Do not add a `Bearer` prefix — Okta supplies the scheme itself, and a prefixed value fails authentication.

Use **Test API Credentials** to confirm the URL and token, then save.

### Error authenticating: No results for users returned

Okta's connection test reads the SCIM endpoint and expects to find a user it recognizes there. A newly enabled Chainguard endpoint has no users yet, so on a first-time setup the test fails with this message. Despite the wording, authentication succeeded; the missing user is what blocks the save.

A workaround is to create the first user directly, then run the test again:

```sh
curl -X POST \
  -H "Authorization: Bearer <your cgscim_ token>" \
  -H "Content-Type: application/scim+json" \
  -d '{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "userName": "<the user's Okta username>",
    "externalId": "<the user's Okta ID>",
    "active": true
  }' \
  "<your SCIM endpoint URL>/Users"
```

Set `externalId` to the user's Okta ID — the `00u...` value in the page URL when you open that user under **Directory** > **People**. Okta's test rejects an arbitrary value even though the endpoint returns the user, so this is not a field you can fill with a placeholder. `externalId` is also what Chainguard matches against at login, and a wrong value leaves the user unlinked with no error, so seed a real user you intend to provision.

## Step 3: Enable provisioning actions

With the integration saved, select **To App** in the **Provisioning** tab, click **Edit**, and enable **Create Users**, **Update User Attributes**, and **Deactivate Users**. These options appear only after you save the connection, and only for the actions you checked under **Supported provisioning actions** in Step 2.

## Step 4: Assign users and verify

In Okta, assign a user to the provisioning app integration you created in Step 2. Okta provisions them immediately. Have that user log in to Chainguard through Okta and confirm they have access. A provisioned user connects to their login by matching the SCIM `externalId` against the login token's subject; with Okta, both default to the Okta user ID, so they align without configuration.

To confirm the rest of the lifecycle, deactivate that user in Okta or remove their assignment, and confirm that Chainguard refuses their next login. Then reactivate them and confirm that they can log in again.

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
