---
title: "Enable PKCE for OAuth Token Exchange"
linktitle: "Enable PKCE"
lead: ""
description: "How to add PKCE to your custom identity provider's OAuth token exchange with Chainguard, either alongside a client secret or as a secret-free public client."
type: "article"
date: 2026-07-30T08:48:45+00:00
lastmod: 2026-07-30T08:48:45+00:00
draft: false
tags: ["Chainguard Containers", "Procedural"]
images: []
weight: 020
---

You can add PKCE (Proof Key for Code Exchange, commonly referred to as "pixy") to the OAuth token exchange between Chainguard and your custom identity provider (IdP). PKCE is a security extension to OAuth that adds an extra layer of protection against authorization code interception during login, and it is required by the OAuth 2.1 standard.

Chainguard supports two configurations, depending on your needs:

- **Client ID + client secret + PKCE** — In this configuration, PKCE is layered on top of your existing confidential client setup. This is additive: you keep your client ID and client secret.
- **Client ID + PKCE only, no client secret** — This is the newer "public client" model where PKCE replaces the client secret entirely, and is the approach OAuth 2.1 requires going forward.

Enabling PKCE is optional. If you leave PKCE disabled or optional on your IdP, your login behavior remains unchanged and you don't need to take any action.

## Prerequisites

To follow this guide, you need:

- A custom identity provider (such as [Okta](/platform/administration/custom-idps/idp-providers/okta/), [Microsoft Entra ID](/platform/administration/custom-idps/idp-providers/ms-entra-id/), or [Ping Identity](/platform/administration/custom-idps/idp-providers/ping-id/)) already configured for login to Chainguard. If you haven't set one up yet, refer to our guide [Using Custom Identity Providers to Authenticate to Chainguard](/platform/administration/custom-idps/custom-idps/).
- An IAM role that can manage identity providers in your Chainguard organization, such as the `owner` role.
- [`chainctl` installed](/chainguard/chainctl-usage/how-to-install-chainctl/) on your local machine. You must also authenticate with `chainctl auth login`.

The rest of this guide refers to your identity provider by its UIDP, stored in the `IDENTITY_PROVIDER` environment variable. Retrieve and set it with the following command:

```sh
export IDENTITY_PROVIDER=$(chainctl iam identity-providers list -o json | jq -r '.items[0].id')
```

This command selects the first identity provider the list returns. If your account can access more than one identity provider, replace `.items[0]` with a filter that matches the one you want, or set the variable to the UIDP manually.

## Option 1: Client ID + client secret + PKCE

This option adds PKCE on top of an existing confidential client setup. You keep using your client ID and client secret, and PKCE is layered on as an additional protection.

To enable it, complete the following steps:

1. In your identity provider, locate the application registration used for your Chainguard integration.
2. Enable PKCE for that application. This is typically a toggle or checkbox labeled "Require PKCE" or similar.
3. Update your identity provider configuration on the Chainguard platform to turn on PKCE:

    ```sh
    chainctl iam identity-providers update $IDENTITY_PROVIDER --oidc-pkce-enabled
    ```

    You can also set this at creation time by including the `--oidc-pkce-enabled` flag with [`chainctl iam identity-providers create`](/platform/chainctl/chainctl-docs/chainctl_iam_identity-providers_create/).

> **Note**: Complete steps 1 and 2 before you run the command in step 3. When you enable PKCE on the Chainguard side, we check your IdP's configuration and reject it if your IdP explicitly advertises that it doesn't support PKCE. Not all IdPs advertise this either way, so a successful command doesn't guarantee that your IdP is configured correctly.

## Option 2: Client ID + PKCE only, no client secret

Unlike Option 1, this usually isn't a setting you can toggle on or off. Most IdPs tie "public client" (no secret) behavior to the *type* of application you've registered, not just a PKCE setting. To go secret-free, the application must be a type your IdP treats as a public client.

Whether you can change an existing application's type depends on your identity provider. Some providers, including Okta, don't allow it: a "Web" app in Okta is confidential and always expects a secret, even with PKCE enabled. If your provider won't let you convert an existing application, you can instead register a new application as a public client type from the start, then create a matching identity provider configuration in Chainguard that includes the `--oidc-pkce-enabled` flag and omits the `--oidc-client-secret` flag.

To switch an existing application, complete the following steps:

1. In your identity provider, locate the application registration used for your Chainguard integration and change its type to a public client type, such as **Native** or **SPA** in Okta, or the equivalent for your IdP.
2. Confirm that PKCE is required for that application.
3. Update your identity provider configuration on the Chainguard platform to remove the client secret and turn on PKCE:

    ```sh
    chainctl iam identity-providers update $IDENTITY_PROVIDER --oidc-client-secret="" --oidc-pkce-enabled
    ```

    You must explicitly set the `--oidc-client-secret` field to `""` to clear it. The configured IdP must always have either a client secret or PKCE enabled.

> **Note**: Complete steps 1 and 2 before you run the command in step 3. When you enable PKCE on the Chainguard side, we check your IdP's configuration and reject it if your IdP explicitly advertises that it doesn't support PKCE. Not all IdPs advertise this either way, so a successful command doesn't guarantee that your IdP is configured correctly.

## Verify that PKCE is enabled

After completing either option, confirm that Chainguard has PKCE enabled for your identity provider:

```sh
chainctl iam identity-providers list -o json | jq '.items[] | {name, pkce: .oidc.pkce_enabled}'
```

If PKCE is enabled, your provider reports `"pkce": true`. You can also run `chainctl iam identity-providers list -o table` and look for `PKCE Enabled` in the `CONFIGURATION` column.

This checks the Chainguard side of the configuration only. Chainguard never returns client secrets in command output, so these commands can't confirm that a secret has been removed.

Next, test a login from end to end:

```sh
chainctl auth login --identity-provider=$IDENTITY_PROVIDER
```

You can also log in with your organization name:

```sh
chainctl auth login --org-name=example.com
```

A successful login completes the browser redirect and returns an authenticated session. If you have any questions or issues, contact your Customer Success Team or Support, and we'll help confirm your configuration is working correctly.
