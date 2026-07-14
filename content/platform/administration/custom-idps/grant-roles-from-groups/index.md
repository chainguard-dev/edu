---
title: "Grant Chainguard Roles from Identity Provider Groups"
linktitle: "Map IdP Groups to Roles"
lead: ""
description: "How to map groups from a custom identity provider to Chainguard roles so access follows group membership."
type: "article"
date: 2026-07-01T08:48:45+00:00
lastmod: 2026-07-01T08:48:45+00:00
draft: false
tags: ["Chainguard Containers", "Procedural"]
images: []
weight: 007
---

Chainguard can grant roles based on a user's groups in your identity provider (IdP). You map an IdP group to a Chainguard role once, and from then on any user who logs in with that group in their token receives the role for that session. Access follows group membership, so you manage who gets what in your IdP instead of assigning roles to each user in Chainguard.

This guide covers Okta and Microsoft Entra ID. The Chainguard-side steps (2 through 4) are the same for both providers; only how you emit group membership in Step 1 differs.

## Prerequisites

To complete this guide, you need the following:

- A custom identity provider (such as [Okta](/platform/administration/custom-idps/idp-providers/okta/) or [Microsoft Entra ID](/platform/administration/custom-idps/idp-providers/ms-entra-id/)) already configured for login to Chainguard. If you haven't set one up yet, refer to our guide [Using Custom Identity Providers to Authenticate to Chainguard](/platform/administration/custom-idps/custom-idps/).
- An IAM role that can manage identity providers and role-bindings in your organization, such as the `owner` role.
- [`chainctl` installed](/chainguard/chainctl-usage/how-to-install-chainctl/) on your local machine. You must also authenticate with `chainctl auth login`.

The rest of this guide refers to your organization and identity provider by their UIDPs, stored in the `ORGANIZATION` and `IDENTITY_PROVIDER` environment variables. Retrieve and set them with the following commands.

Store your organization's UIDP in the `ORGANIZATION` variable:

```sh
export ORGANIZATION=$(chainctl iam organizations list -o json | jq -r '.items[0].id')
```

Store your identity provider's UIDP in the `IDENTITY_PROVIDER` variable:

```sh
export IDENTITY_PROVIDER=$(chainctl iam identity-providers list -o json | jq -r '.items[0].id')
```

These commands select the first result each list returns. If your account can access more than one organization or identity provider, replace `.items[0]` with a filter that matches the one you want, or set each variable to the UIDP directly.

## How IdP group mappings work

Before you configure any mappings, it helps to understand how group-derived roles behave:

- **Mappings are additive.** A mapping grants a role on top of whatever access a user already has. It never removes existing access.
- **Group-derived roles are session-scoped, not standing grants.** They apply to the logged-in session and are re-evaluated at each login. They do not appear in `chainctl iam role-bindings list` or the Console's role-bindings view. Instead, each login that resolves group-derived roles emits a Chainguard CloudEvent recording the roles granted, along with the identity provider and groups they came from. To observe effective group-derived access, [subscribe to Chainguard's CloudEvents stream](/platform/administration/cloudevents/events-example/).

    As a result, no single command or view answers "who holds a group-derived role right now?" The CloudEvents stream is a log of each login as it happens, not a current-state table. During an access review or an incident, reconstruct effective access by combining that event history with current group membership in your IdP and the mappings from `chainctl iam external-group-role-mappings list`.
- **Changes take effect within an hour.** A session that includes group-derived roles is short-lived by design. Its access token lasts at most one hour, and no refresh token is issued, so when the token expires the user logs in again and that login re-reads their current group membership. As a result:
    - Removing a user from a group takes effect at their next login, within one hour.
    - Deleting or changing a mapping takes effect within one hour, because Chainguard reads mappings fresh on every login.
    - A user whose access is only group-derived re-authenticates at least hourly.

## Step 1: Emit group membership from your IdP

Configure your identity provider to include the user's group memberships in the OIDC token it issues to Chainguard. The exact Console steps differ by provider and change over time, so follow your provider's own documentation. This guide relies only on the result:

- The token carries a claim listing the user's groups, named whatever you set in Step 2. That value format is what you supply as `--external-group-id` in Step 3. This guide uses `groups`.
- The token carries only the groups you map, not every group a user belongs to. The IdP drops oversized group sets from the token, as described in [Limits](#limits).

| Provider | Configuring the groups claim | Values you map on |
| :---- | :---- | :---- |
| Okta | [Customize tokens with a groups claim](https://developer.okta.com/docs/guides/customize-tokens-groups-claim/main/) | Group names (for example, `app-admins`) |
| Microsoft Entra ID | [Configure group claims](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-fed-group-claims) | Group Object IDs (GUIDs), by default |

To use group display names in Entra ID instead of GUIDs, configure the claim to emit cloud-group display names. This requires restricting the claim to groups assigned to the application, which is also the recommended way to stay under the group limit.

## Step 2: Point Chainguard at the groups claim

Update the identity provider you use to log in so Chainguard requests the groups claim and knows which claim carries group membership:

```sh
chainctl iam identity-providers update $IDENTITY_PROVIDER \
  --oidc-additional-scopes=groups \
  --oidc-groups-claim=groups
```

- `--oidc-additional-scopes=groups` tells Chainguard to request the groups claim.
- `--oidc-groups-claim=groups` tells Chainguard which claim carries group membership, using the name from Step 1. An empty value turns group mapping off for this provider.

## Step 3: Map a group to a role

Create a mapping from an IdP group to a Chainguard role:

```sh
chainctl iam external-group-role-mappings create \
  --external-group-id "GROUP" \
  --role editor \
  --scope $ORGANIZATION \
  --idp $IDENTITY_PROVIDER
```

- `--external-group-id` is the value the IdP emits: the group name for Okta (for example, `app-admins`), or the group Object ID (GUID) for Entra ID.
- `--role` is the role to grant, by name or UIDP, such as `viewer` or `editor`.
- `--scope` is the UIDP of the organization where the role applies.
- `--idp` is the identity provider that owns the mapping.

To review the mappings you've configured, run the `list` subcommand:

```sh
chainctl iam external-group-role-mappings list --parent $ORGANIZATION
```

## Step 4: Verify the mapping

1. Have a user who belongs to the mapped group log in to Chainguard through your IdP.
2. Confirm that the user can perform actions the granted role allows. This access doesn't appear in `chainctl iam role-bindings list`, because it's session-scoped.
3. Have a user who doesn't belong to a mapped group log in and confirm that they receive no additional access.

## Manage access

Once mappings are in place, you can adjust access by changing group membership within your identity provider, or by changing the mappings themselves:

- **Grant more than one role to a group.** Create one mapping per role for the same group. The capabilities combine.
- **Remove one user's group-derived access.** Remove that user from the group in your IdP, or unassign them from the application. Only that user is affected; everyone else in the group keeps the mapped role.
- **Remove a role from everyone in a group.** Delete the mapping. This revokes the mapped role for all users in that group and leaves their other access intact:

    ```sh
    chainctl iam external-group-role-mappings delete $MAPPING_ID
    ```

    Be sure to replace `$MAPPING_ID` with the mapping's UIDP, which you can find by running the `chainctl iam external-group-role-mappings list` command shown in Step 3.

- **Remove every mapping for an identity provider.** When offboarding a provider, delete all of its mappings in one command. `chainctl` asks you to confirm first; include the `--yes` flag to skip the prompt:

    ```sh
    chainctl iam external-group-role-mappings delete --all --idp $IDENTITY_PROVIDER
    ```

    This revokes the mapped roles for all users across that IdP's groups and leaves their other access intact. You can't delete an identity provider while any mappings still exist, so you must complete this cleanup step before you remove the provider.

Each of these changes takes effect at the affected user's next login, within one hour.

### Revoke access urgently

When you need to revoke a user's access immediately, as with a compromised account or a departing employee, deleting the mapping alone is not enough. A session that already resolved the group-derived role keeps it until the access token expires, up to an hour, and that token can't be revoked mid-session. The fix is to stop the user from re-deriving the role at their next login:

1. In your identity provider, disable the user's account or remove them from the mapped group. This prevents their next login from granting the role.
2. Delete the mapping if you also want to revoke the role for everyone else in the group.

The existing session still expires on its own within the hour, and the IdP change blocks re-authorization after that.

## Limits

Identity providers cap how many groups a token can carry. Past that limit, the IdP stops sending the inline `groups` claim. This means Chainguard no longer receives the user's groups, and their mappings don't resolve. Keep the emitted set small by sending only the groups you map:

- **Okta:** Filter the groups claim in Step 1 so the token carries only the groups you map rather than every group a user belongs to.
- **Microsoft Entra ID:** Entra ID omits the `groups` claim once a user belongs to more than 200 groups (the JWT and OIDC limit; the SAML limit is 150). Past the limit, Entra ID emits an overage claim (`_claim_names` and `_claim_sources`) that points to Microsoft Graph instead of the inline list, and Chainguard doesn't follow it. Avoid the overage by emitting only groups assigned to the application, as described in Step 1, or by using fewer, coarser groups for access.

## Related resources

- [Using Custom Identity Providers to Authenticate to Chainguard](/platform/administration/custom-idps/custom-idps/)
- [How To Integrate Okta SSO with Chainguard](/platform/administration/custom-idps/idp-providers/okta/)
- [How To Integrate Microsoft Entra ID SSO with Chainguard](/platform/administration/custom-idps/idp-providers/ms-entra-id/)
- [Overview of the Chainguard IAM Model](/platform/administration/iam-organizations/overview-of-chainguard-iam-model/)
- [Manage Identity and Access with chainctl](/chainguard/chainctl-usage/chainctl-iam/)
- [Subscribe to Chainguard Events](/platform/administration/cloudevents/events-example/)
