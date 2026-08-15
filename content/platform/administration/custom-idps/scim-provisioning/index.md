---
title: "Provision Chainguard Users with SCIM"
linktitle: "SCIM User Provisioning"
lead: ""
description: "How SCIM provisioning to the Chainguard platform behaves, and how to manage the provisioning connection over its lifetime."
type: "article"
date: 2026-08-14T00:00:00+00:00
lastmod: 2026-08-14T00:00:00+00:00
draft: false
tags: ["Conceptual", "Procedural"]
images: []
weight: 012
---

{{< beta feature="SCIM user provisioning" >}}

Chainguard can create and deactivate user accounts based on your identity provider (IdP). Connect your IdP's SCIM provisioning once; from then on, assigning a user to the application provisions them, and deactivating or unassigning them removes their Chainguard access. Accounts follow your IdP, so access is managed in one place.

Chainguard's SCIM provisioning manages accounts, not roles. To grant roles from IdP group membership, use [group mappings](/chainguard/administration/custom-idps/grant-roles-from-groups/); the two are independent, and you can use either or both. Chainguard's SCIM endpoint accepts user provisioning only: group provisioning over SCIM is not yet available, so leave your IdP's SCIM group push turned off.

This page explains how provisioning behaves and how to manage the connection over its lifetime. To connect a specific identity provider, follow its guide:

* [Okta SCIM provisioning](/chainguard/administration/custom-idps/idp-providers/okta-scim/)
* [Microsoft Entra ID SCIM provisioning](/chainguard/administration/custom-idps/idp-providers/ms-entra-id-scim/)

## How SCIM provisioning works

Provisioning behaves the same way for every provider:

* **Provisioning creates records, logins create accounts.** When your IdP provisions a user, Chainguard stores a provisioning record. The user's Chainguard account is created the first time they log in, exactly as it would be without SCIM, and connects to their provisioning record automatically. Users who have logged in before are connected at their next login, with no re-registration; their existing access is unaffected.
* **Matching is by `externalId`, never by email.** A provisioned user connects to a login by matching the SCIM `externalId` your IdP sends against the subject of the login token. Each provider guide covers how to make the two align. Email addresses are never used for matching.
* **Deactivation takes effect at the user's next login or token refresh.** When your IdP deactivates or unassigns a provisioned user, their current access token runs out on its own schedule (up to an hour), and every attempt to log in or refresh after the deactivation is refused. Reactivating the user in your IdP restores their ability to log in; it does not restore any role bindings that were removed while they were deactivated.
* **Provisioning does not assign roles.** A provisioned user who logs in gets the identity provider's default role, plus any group-mapped roles and role bindings they hold, same as any other user.
* **Enabling SCIM does not restrict other logins.** Users who aren't provisioned log in exactly as before; provisioning adds lifecycle control only for the users your IdP sends.

## Prerequisites

The provider guides share the following prerequisites:

* A custom identity provider already configured for login to Chainguard. If you haven't set one up yet, refer to our guide on [Using Custom Identity Providers](/chainguard/administration/custom-idps/custom-idps/).
* An IAM role that can manage identity providers in your organization, such as the owner role.
* Two owners with directly assigned role bindings in your organization. Enabling SCIM requires this, so that access to your organization never depends entirely on the IdP that SCIM controls. Roles held through group mappings don't count toward the two: they are granted per-session at login, which an IdP outage would interrupt. Organizations that manage access through groups often have only their creator as a directly assigned owner, so check this first.
* `chainctl` installed on your local machine. Follow our guide on [How to install `chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/) if you don't already have this installed. You must also authenticate with `chainctl auth login`.

The commands below refer to your identity provider by its UIDP, stored in the `IDENTITY_PROVIDER` environment variable. Retrieve and set it with the following command:

```sh
export IDENTITY_PROVIDER=$(chainctl iam identity-providers list -o json | jq -r '.items[0].id')
```

An organization has exactly one identity provider, so for most accounts this returns it directly. If you belong to more than one organization, the list contains each organization's provider; set the variable to the UIDP of the one you are configuring.

## The SCIM token

Your IdP authenticates to Chainguard's SCIM endpoint with a bearer token. Generate it:

```sh
chainctl iam identity-providers scim token generate $IDENTITY_PROVIDER
```

The command prints the token to standard output and the SCIM endpoint URL and expiry to standard error. The token is shown exactly once (Chainguard stores only a digest), so paste it into your IdP right away. If you lose it, create a replacement with the `regenerate` command shown in [Manage provisioning](#manage-provisioning).

Tokens expire after one year by default. Set a different lifetime with `--expires-in` (up to two years), or issue a non-expiring token with `--never-expires`.

Generating a token does not start provisioning; enabling provisioning is a separate step.

## Enabling and disabling provisioning

```sh
chainctl iam identity-providers scim enable $IDENTITY_PROVIDER
```

Chainguard now accepts provisioning requests from your IdP. If the command is refused with a message about owner-tier identities, your organization doesn't yet have two directly assigned owners; see [Prerequisites](#prerequisites).

Disabling stops Chainguard from accepting provisioning requests. It doesn't invalidate the token, and already provisioned users are unaffected:

```sh
chainctl iam identity-providers scim disable $IDENTITY_PROVIDER
```

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

* **Delete a user in your IdP.** If your IdP sends a SCIM delete (distinct from deactivation), Chainguard removes the provisioning record entirely and deactivates the user's account.

Token lifecycle and the on/off switch are independent: rotating or revoking a token never disables provisioning, and disabling never invalidates a token.

## Limits

* Provisioning write requests (create, update, deactivate) are rate limited per organization and per source address. Past the limit, requests receive HTTP 429 with a `Retry-After` header; IdPs retry on their own schedule.
* Request bodies on writes are capped at 256 KiB, which is larger than any standard SCIM user payload.

## Related resources

* [Okta SCIM provisioning](/chainguard/administration/custom-idps/idp-providers/okta-scim/)
* [Microsoft Entra ID SCIM provisioning](/chainguard/administration/custom-idps/idp-providers/ms-entra-id-scim/)
* [Grant Chainguard Roles from Identity Provider Groups](/chainguard/administration/custom-idps/grant-roles-from-groups/)
* [Using Custom Identity Providers to Authenticate to Chainguard](/chainguard/administration/custom-idps/custom-idps/)
* [Overview of the Chainguard IAM Model](/chainguard/administration/iam-organizations/overview-of-chainguard-iam-model/)
