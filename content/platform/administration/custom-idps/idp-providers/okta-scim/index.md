---
title: "How to provision users into Chainguard from Okta with SCIM"
linktitle: "Okta SCIM Provisioning"
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

The Chainguard platform supports SCIM 2.0 provisioning from Okta. With SCIM enabled, Okta creates, updates, and deactivates Chainguard users as you assign and unassign them, and each provisioned user is linked to their single sign-on (SSO) login automatically.

This guide covers the Okta-specific setup. For provisioning behavior, token lifecycle, and limits, refer to [Provision Chainguard Users with SCIM](/chainguard/administration/custom-idps/scim-provisioning/).

## Prerequisites

To complete this guide, you need the following:

* Okta already configured for login to Chainguard through an OIDC app integration. If you haven't set that up yet, refer to our guide on [How to integrate Okta SSO with Chainguard](/chainguard/administration/custom-idps/idp-providers/okta/).
* The [common prerequisites](/chainguard/administration/custom-idps/scim-provisioning/#prerequisites) for SCIM provisioning: an IAM role that can manage identity providers, two owners with directly assigned role bindings, and an authenticated `chainctl`.

The rest of this guide refers to your identity provider by its UIDP, stored in the `IDENTITY_PROVIDER` environment variable:

```sh
export IDENTITY_PROVIDER=$(chainctl iam identity-providers list -o json | jq -r '.items[0].id')
```

If you belong to more than one organization, set the variable to the UIDP of the provider you are configuring instead.

## Step 1: Generate the SCIM token

Okta authenticates to Chainguard's SCIM endpoint with a bearer token. Generate it:

```sh
chainctl iam identity-providers scim token generate $IDENTITY_PROVIDER
```

The command prints the token to standard output and the SCIM endpoint URL to standard error. The token is shown exactly once, so paste it into Okta (Step 2) right away. Lifetime options and rotation are covered in [Provision Chainguard Users with SCIM](/chainguard/administration/custom-idps/scim-provisioning/#the-scim-token).

## Step 2: Create the Okta provisioning app

Okta hosts SCIM provisioning on an app integration, but SCIM cannot be added to the OIDC app integration you use for login. Create a second app integration that exists only to carry provisioning: in the Okta Admin Console, navigate to **Applications** > **Applications**, click **Create App Integration**, and choose **SAML 2.0**. Complete the wizard with placeholder values; Chainguard does not consume the SAML assertion, and sign-in stays on your existing OIDC app. On the new app's **General** tab, set **Provisioning** to **SCIM**.

Then open the app's **Provisioning** tab and configure the SCIM connection:

* **SCIM connector base URL**: the endpoint printed in Step 1.
* **Unique identifier field for users**: `userName`.
* **Authentication mode**: **HTTP Header**, with `Bearer <token>` as the value.

Two configuration details:

* The HTTP Header value is sent exactly as you type it, so it must be `Bearer <token>`, including the word `Bearer` and a space; a bare token fails authentication.
* Enable the provisioning actions you want Chainguard to receive: under **Provisioning** > **To App**, check **Create Users**, **Update User Attributes**, and **Deactivate Users**. Leave group push off; Chainguard's SCIM endpoint accepts user provisioning only.

Use **Test API Credentials** to confirm the URL and token before saving. Provisioning itself stays off until Step 3.

## Step 3: Enable provisioning

```sh
chainctl iam identity-providers scim enable $IDENTITY_PROVIDER
```

Chainguard now accepts provisioning requests from Okta. If the command is refused with a message about owner-tier identities, your organization doesn't yet have two directly assigned owners; see the [common prerequisites](/chainguard/administration/custom-idps/scim-provisioning/#prerequisites).

## Step 4: Assign users and verify

1. In Okta, assign a user to the provisioning app integration from Step 2. Okta provisions them immediately.
2. Have that user log in to Chainguard through Okta and confirm they have access. A provisioned user connects to their login by matching the SCIM `externalId` against the login token's subject; with Okta, both default to the Okta user ID, so they align without configuration.
3. In Okta, deactivate the user or remove their assignment, and confirm their next login is refused.
4. Reactivate them and confirm login works again.

## Troubleshooting

**A user logged in but wasn't linked.** A provisioning mismatch does not produce an error; the login proceeds as a normal, unlinked user. Confirm the user is assigned to the provisioning app and was provisioned (check the app's assignment and Okta's provisioning logs), and that the app sends the default Okta user ID as `externalId`.

**Test API Credentials fails.** Confirm the base URL is the endpoint printed by `token generate` and that the HTTP Header value is `Bearer <token>` — including the word `Bearer` and a space. The URL and token must come from the same `token generate` run.

**Provisioning requests receive HTTP 429.** Provisioning writes are rate limited; Okta retries on its own schedule, so bulk assignments complete without intervention. See [Limits](/chainguard/administration/custom-idps/scim-provisioning/#limits).

## Related resources

* [Provision Chainguard Users with SCIM](/chainguard/administration/custom-idps/scim-provisioning/)
* [Grant Chainguard Roles from Identity Provider Groups](/chainguard/administration/custom-idps/grant-roles-from-groups/)
* [How to integrate Okta SSO with Chainguard](/chainguard/administration/custom-idps/idp-providers/okta/)
* [Overview of the Chainguard IAM Model](/chainguard/administration/iam-organizations/overview-of-chainguard-iam-model/)
