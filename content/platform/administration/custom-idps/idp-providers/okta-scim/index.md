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

Chainguard can create and deactivate user accounts based on your identity provider (IdP). Connect your IdP's SCIM provisioning once; from then on, assigning a user to the application provisions them, and deactivating or unassigning them cuts their Chainguard access. Accounts follow your IdP, so you manage who has access in one place instead of onboarding and offboarding users in Chainguard by hand.

SCIM provisioning manages accounts, not roles. To grant roles from IdP group membership, use [group mappings](/chainguard/administration/custom-idps/grant-roles-from-groups/); the two are independent, and you can use either or both.

This guide covers Okta. For Microsoft Entra ID, refer to the companion Entra ID SCIM provisioning guide.

## Prerequisites

To complete this guide, you need the following:

* A custom identity provider (such as Okta) already configured for login to Chainguard. If you haven't set one up yet, refer to our guides on [Using Custom Identity Providers](/chainguard/administration/custom-idps/custom-idps/) and [How to integrate Okta SSO with Chainguard](/chainguard/administration/custom-idps/idp-providers/okta/).
* An IAM role that can manage identity providers in your organization, such as the owner role.
* Two owners with directly assigned role bindings in your organization. Enabling SCIM requires this, so that access to your organization never depends entirely on the IdP that SCIM controls. Roles held through group mappings don't count toward the two: they are granted per-session at login, which is exactly what an IdP outage takes away. If your organization manages access through groups, this is the step to check first: many such organizations have only their creator as a directly assigned owner.
* `chainctl` installed on your local machine. Follow our guide on [How to install `chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/) if you don't already have this installed. You must also authenticate with `chainctl auth login`.

The rest of this guide refers to your identity provider by its UIDP, stored in the `IDENTITY_PROVIDER` environment variable. Retrieve and set it with the following command:

```sh
export IDENTITY_PROVIDER=$(chainctl iam identity-providers list -o json | jq -r '.items[0].id')
```

An organization has exactly one identity provider, so for most accounts this returns it directly. If you belong to more than one organization, the list contains each organization's provider; set the variable to the UIDP of the one you are configuring.

## How SCIM provisioning works

Before you connect anything, it helps to understand how provisioning behaves:

* **Provisioning creates records, logins create accounts.** When your IdP provisions a user, Chainguard stores a provisioning record. The user's Chainguard account is created the first time they log in, exactly as it would be without SCIM, and connects to their provisioning record automatically. Users who have logged in before are connected at their next login, with no re-registration; their existing access is unaffected.
* **Matching is by `externalId`, never by email.** A provisioned user connects to a login by matching the SCIM `externalId` your IdP sends against the subject of the login token. With Okta, both default to the Okta user ID, so they align without configuration. Email addresses are never used for matching.
* **Deactivation takes effect at the user's next login or token refresh.** When your IdP deactivates or unassigns a provisioned user, their current access token runs out on its own schedule (up to an hour), and every attempt to log in or refresh after the deactivation is refused. Reactivating the user in your IdP restores their ability to log in; it does not restore any role bindings that were removed while they were deactivated.
* **Provisioning does not assign roles.** A provisioned user who logs in gets the identity provider's default role, plus any group-mapped roles and role bindings they hold, same as any other user.
* **Enabling SCIM locks no one out.** Users who aren't provisioned log in exactly as before. Provisioning adds lifecycle control for the users your IdP sends; it doesn't restrict the rest.

## Step 1: Generate the SCIM token

Your IdP authenticates to Chainguard's SCIM endpoint with a bearer token. Generate it:

```sh
chainctl iam identity-providers scim token generate $IDENTITY_PROVIDER
```

The command prints the token to standard output and the SCIM endpoint URL and expiry to standard error. The token is shown exactly once (Chainguard stores only a digest), so paste it into your IdP (Step 2) right away. If you lose it, create a replacement with the `regenerate` command shown in [Manage provisioning](#manage-provisioning).

Tokens expire after one year by default. Set a different lifetime with `--expires-in` (up to two years), or issue a non-expiring token with `--never-expires`.

Generating a token does not start provisioning; that is a separate, explicit step (Step 3).

## Step 2: Connect Okta

Okta hosts SCIM provisioning on an app integration, but SCIM cannot be added to the OIDC app integration you use for login. Create a second app integration that exists only to carry provisioning: in the Okta Admin Console, navigate to **Applications** > **Applications**, click **Create App Integration**, and choose **SAML 2.0**. Complete the wizard with placeholder values — Chainguard does not consume the SAML assertion, and sign-in stays on your existing OIDC app. On the new app's **General** tab, set **Provisioning** to **SCIM**.

Then open the app's **Provisioning** tab and configure the SCIM connection:

* **SCIM connector base URL**: the endpoint printed in Step 1.
* **Unique identifier field for users**: `userName`.
* **Authentication mode**: **HTTP Header**, with `Bearer <token>` as the value.

Two details to get right:

* The HTTP Header value is sent exactly as you type it, so it must be `Bearer <token>`, including the word `Bearer` and a space; a bare token fails authentication.
* Enable the provisioning actions you want Chainguard to receive: under **Provisioning** > **To App**, check **Create Users**, **Update User Attributes**, and **Deactivate Users**.

Use **Test API Credentials** to confirm the URL and token before saving. Provisioning itself stays off until Step 3.

## Step 3: Enable provisioning

```sh
chainctl iam identity-providers scim enable $IDENTITY_PROVIDER
```

Chainguard now accepts provisioning requests from your IdP. If the command is refused with a message about owner-tier identities, your organization doesn't yet have two directly assigned owners; see [Prerequisites](#prerequisites).

## Step 4: Assign users and verify

1. In Okta, assign a user to the provisioning app integration from Step 2. Okta provisions them immediately.
2. Have that user log in to Chainguard through your IdP and confirm they have access.
3. In Okta, deactivate the user or remove their assignment, and confirm their next login is refused.
4. Reactivate them and confirm login works again.

## Manage provisioning

* **Rotate the token.** Replace the token while your IdP keeps working through the change. The previous token keeps authenticating for the overlap window (default one hour, up to 24) while you paste the new one into your IdP:

```sh
chainctl iam identity-providers scim token regenerate $IDENTITY_PROVIDER --overlap 1h
```

* **Revoke the token.** If the token may be exposed, revoke it. This immediately invalidates the current token and any overlap token:

```sh
chainctl iam identity-providers scim token revoke $IDENTITY_PROVIDER
```

Provisioning requests fail until you regenerate a replacement; revoking contains a compromise without turning provisioning off. If you want an immediate replacement instead of a stop, regenerate with `--overlap 0`.

* **Turn provisioning off.** Disabling stops Chainguard from accepting provisioning requests. It doesn't invalidate the token, and already provisioned users are unaffected:

```sh
chainctl iam identity-providers scim disable $IDENTITY_PROVIDER
```

* **Delete a user in your IdP.** If your IdP sends a SCIM delete (distinct from deactivation), Chainguard removes the provisioning record entirely and deactivates the user's account.

Token lifecycle and the on/off switch are independent: rotating or revoking a token never disables provisioning, and disabling never invalidates a token.

## Limits

* Provisioning write requests (create, update, deactivate) are rate limited per organization and per source address. Past the limit, requests receive HTTP 429 with a `Retry-After` header; IdPs retry on their own schedule.
* Request bodies on writes are capped at 256 KiB, comfortably above any standard SCIM user payload.

## Related resources

* [Grant Chainguard Roles from Identity Provider Groups](/chainguard/administration/custom-idps/grant-roles-from-groups/)
* [Using Custom Identity Providers to Authenticate to Chainguard](/chainguard/administration/custom-idps/custom-idps/)
* [How to integrate Okta SSO with Chainguard](/chainguard/administration/custom-idps/idp-providers/okta/)
* [Overview of the Chainguard IAM Model](/chainguard/administration/iam-organizations/overview-of-chainguard-iam-model/)
