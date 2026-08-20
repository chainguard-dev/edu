---
title : "Using custom identity providers to authenticate to Chainguard"
linktitle: "Authenticate with custom IdPs"
aliases:
- /chainguard/chainguard-enforce/authentication/custom-idps/
- /chainguard/administration/custom-idps/custom-idps/
lead: "Chainguard custom IdPs"
description: "An introduction to and overview of Chainguard's custom IdP support features"
type: "article"
date: 2023-04-17T08:48:45+00:00
lastmod: 2026-08-20T18:38:14+00:00
draft: false
tags: ["Chainguard Containers", "Overview"]
images: []
weight: 005
---

The Chainguard platform supports Single Sign-on (SSO) authentication for users. By default, users can log in with GitHub, GitLab, and Google, but SSO support allows users to bring their own identity provider for authentication. This is helpful when your organization mandates using a corporate identity provider — like Okta or Azure Active Directory — to authenticate to SaaS products.

## Usage

Once an administrator has [configured an identity provider](#setup-and-administration) and set up their organization, users can authenticate at the command line and in the web console using the identity provider’s organization.

### Authenticate with `chainctl`

[`chainctl`, the Chainguard command line interface (CLI)](/chainguard/chainctl/), supports SSO authentication by supplying the identity provider organization name as a flag or by setting it as a default in configuration. To use a flag to authenticate using SSO, pass the `--identity-provider` flag to `chainctl auth login`.

```sh
export IDP_ID=<your identity provider id here>
chainctl auth login --identity-provider=$IDP_ID
```

You can retrieve all your identity provider's unique IDs by running `chainctl iam identity-providers list`.

Note that you can also use the [`--headless` option](/chainguard/administration/iam-organizations/overview-of-chainguard-iam-model/#using-the-headless-login-flow) to log in with a custom IdP in an environment that doesn't have a browser installed, such as a container or a remote server. By including this option, `chainctl` will output a special URL. You can then navigate to the URL in another device's browser to log in with your custom IdP.

To log in with a custom IdP using the `--headless` option, you would run a command like the following:

```sh
chainctl auth login --headless --identity-provider=$IDP_ID
```

Then you can use the URL in this command's output to complete the login flow from another device's browser.

> **Note**: As of this writing (September 2024), using the headless login flow with a custom IdP is still an experimental feature. Please reach out to us through your customer success manager or the support portal to report any feedback. Also, until this feature becomes enabled by default, you must enable it yourself with the following command:

```sh
chainctl config set auth.device-flow chainguard
```

### Setting a default identity provider

As an alternative to remembering identity provider IDs, you can set the default identity provider by editing the `chainctl` configuration file. You can do so with the following command.

```sh
chainctl config edit
```

This will open your system's default text editor where you can edit the local `chainctl` config. Add the following lines to this file.

```yaml
default:
  identity-provider: <your identity provider id here>
```

Then save and close the file. If your system's default editor is `nano`, for example, you can do so by pressing `CTRL + X`, `Y`, and then `ENTER`.

You can also set this with a single command using the `chainctl config set` subcommand, as in this example.

```sh
chainctl config set default.identity-provider <your identity provider id here>
```

Once set, the configured identity provider will be used automatically any time you run `chainctl auth login`.

### Authenticate with `chainctl` using a verified organization

If your organization is [verified](/chainguard/administration/iam-organizations/verified-orgs/), you can use your organization name instead of the ID of your identity provider to authenticate.

```sh
chainctl auth login --org-name example.com
```

You can add your organization's name to your `chainctl` config to make this a default setting.

```yaml
defaults:
  org-name: example.com
```

To learn more about working with your `chainctl` config, you can read our doc on [How to manage `chainctl` configuration](/chainguard/chainctl-usage/manage-chainctl-config/).

### Authenticate with the Chainguard Console

To authenticate with the Chainguard Console, [open the login screen](https://console.chainguard.dev?feature.emailAuth=true). Then, select one of the following options:

- To use your organization's SSO, enter your Organization or email address and click **Continue**.
- To use a third-party identity provider, click the corresponding option from the list.
- To use your email and a password, enter your email and click **Continue**.

<center><img src="/platform/administration/custom-idps/custom-idps/cg-all-signin-24.png" alt="Screenshot showing an example Chainguard login box, with all described options shown." style="width:600px;"></center>

In each of these cases, you will be redirected to an external identity provider to authenticate and then returned to the Chainguard Console. If you are using your email and a password, authentication is handled by and credentials are stored with [Auth0](https://auth0.com/).

## Setup and administration

Chainguard SSO supports OpenID Connect (OIDC) compatible identity providers. In addition, identity providers must support the following:

- The `authorization code` grant type (sometimes called the `authorization code` *flow*).
- The standard `openid`, `email`, and `profile` scopes. Note that the Chainguard platform [will partially function](https://openid.net/specs/openid-connect-basic-1_0.html#Scopes) with only the `openid` scope, but full functionality requires the `email` and `profile` scopes as well.

Customer-managed identity providers must also have a public, unauthenticated OIDC discovery endpoint.

Typically, identity providers enable you to set up SSO by creating a specific resource on the provider's platform. For example, Ping Identity requires you to [add an application](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html), while Okta has you create [an app integration](https://help.okta.com/en-us/content/topics/apps/apps_apps.htm).

To set up SSO for your identity provider, you must configure one of these resources to use OIDC so that the Chainguard platform can interact with the provider. Following that, you have to configure the Chainguard platform to use that application.

### Confidential and public applications

OAuth classifies client applications as either confidential or public, and most identity providers use this terminology when you register an application. The classification determines whether your application authenticates with a client secret.

- **Confidential applications** can store credentials securely, so they authenticate with a client secret. A web application backed by a server is the typical example, and identity providers usually label these as "Web" applications.
- **Public applications** can't store credentials securely, because their code runs where the user can reach it. Native, mobile, desktop, and single-page applications fall here, and identity providers usually label these as "Native" or "SPA" applications.

A public application has no secret to prove its identity, so it uses PKCE (Proof Key for Code Exchange) instead. PKCE binds the authorization code to the client that requested it, so an intercepted code is useless to anyone else.

Chainguard supports both models:

- **Confidential**: a client ID and client secret. The integration guides describe this setup, and you can also [add PKCE on top of the client secret](/platform/administration/custom-idps/enabling-pkce/).
- **Public**: a client ID and PKCE, with no client secret. OAuth 2.1 requires this model for public clients going forward.

Identity providers usually tie this classification to the application *type* you select at registration rather than to a separate setting, and some don't let you change the type afterward. If you want a public application, choose the matching type when you first register it. For the underlying definitions, refer to [section 2.1 of RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749#section-2.1); your identity provider's documentation names the application types it offers.

### Integration guides for supported identity providers

We have [published guides for multiple platforms](/chainguard/administration/custom-idps/), including Okta and Ping Identity. If you aren’t using one of these identity providers, you can complete the following Generic Integration Guide to configure your provider to work with Chainguard. However, be aware that Chainguard does not actively support identity providers other than the ones listed previously. If you are using an alternate identity provider, we encourage you to contact us to learn more.

### Generic integration guide

For a generic OIDC-compatible identity provider, start by creating an OIDC application. If possible, set as much metadata as possible for the application so that your users can identify this application as the Chainguard platform. The following assets and details can be helpful to include in the metadata:

- The Console homepage is [console.chainguard.dev/](https://console.chainguard.dev)
- Our terms of service can be found at [chainguard.dev/terms-of-service](https://www.chainguard.dev/terms-of-service)
- Our terms of use can be found at [chainguard.dev/terms-of-use](https://www.chainguard.dev/terms-of-use)
- Our privacy policy is located at [chainguard.dev/privacy-notice](https://www.chainguard.dev/privacy-notice)
- You can also add a Chainguard logo icon here to help your users visually identify this integration. The icon from the [Chainguard Console](https://console.chainguard.dev/logo512.png) will be suitable for most platforms

Next, configure your OIDC application as follows:

- Set redirect URI to `https://issuer.enforce.dev/oauth/callback`
- Restrict grant types to **authorization code** only. It is critical that your application does not support "client credentials", "device code", "implicit" or other grant types (sometimes called “flows”)
- Restrict response types to only authorization codes (sometimes called just “code”)
- Enable “openid”, “email” and “profile” scopes for application
- Set PKCE to **optional**. Chainguard supports PKCE for the OAuth token exchange, so you can also set it to **required** if you [enable PKCE on the Chainguard side](/platform/administration/custom-idps/enabling-pkce/). Don't disable PKCE if you plan to enable it for Chainguard.

Finally, configure a set of client credentials and make note of the following details to configure Chainguard:

- The issuer URL
- Client ID
- Client Secret

Next, use `chainctl` to log in to Chainguard with an OIDC provider (such as Google, GitHub, or GitLab) to bootstrap your account.

```sh
chainctl auth login
```

The bootstrap account can use any supported IdP -- for example you may choose to temporarily use a personal Google account. You can leave this account active as a [backup account](/chainguard/administration/custom-idps/custom-idps/#backup-accounts) or, if you prefer, you can delete the account by removing the role-binding after configuring the custom IdP.

Create a new identity provider using the details you noted from your OIDC application. Be sure to update the details in the following example `export` commands to align with your own application/client ID, client secret, and issuer URL.

```sh
export NAME=my-sso-identity-provider
export CLIENT_ID=<your application/client id here>
export CLIENT_SECRET=<your client secret here>
export ISSUER=<your issuer url here>
export ORG=<your organization UIDP here>
chainctl iam identity-provider create \
  --configuration-type=OIDC \
  --oidc-client-id=${CLIENT_ID} \
  --oidc-client-secret=${CLIENT_SECRET} \
  --oidc-issuer=${ISSUER} \
  --oidc-additional-scopes=email \
  --oidc-additional-scopes=profile \
  --parent=${ORG} \
  --default-role=viewer \
  --name=${NAME}
```

The `oidc-issuer`, `oidc-client-id`, and `oidc-issuer-secret` values are required when setting up an OIDC configuration with `chainctl`. You must also include a unique name for each custom IdP account.

Be aware that if you don't include the `--parent` or `--default-role` options in the command, you will be prompted to select these values interactively

- The `--parent` option specifies which Chainguard IAM organization your identity provider will be installed under.
- The `--default-role` option defines the default role granted to users registering with this identity provider. The previous example specifies the `viewer` role, but depending on your needs you might choose `editor` or `owner`. For more information, refer to the [IAM and Security section](#iam-and-security).

You can retrieve a list of all your Chainguard organizations — along with their UIDPs — with the following command.

```shell
chainctl iam organizations ls -o table
```

```output
                         ID                       |    NAME    | DESCRIPTION
--------------------------------------------------------+------------+---------------------
  59156e77fb23e1e5ebcb1bd9c5edae471dd85c43           | sample_org |
  . . .                                              | . . .      |
```

Your organization selection won’t affect how your users authenticate but will have implications on who has permission to modify the SSO configuration.

## Managing existing identity providers

Identity providers can be managed via `chainctl` using the `chainctl iam identity-provider` subcommand.

To create new providers, you can use the `create` subcommand.

```sh
chainct iam identity-provider create
```

To list out every configured identity provider, run the `list` subcommand.

```sh
chainctl iam identity-provider list
```

This will return a list of details for each of your identity providers, including their names and unique IDs.

To modify an existing identity provider, use the `update` subcommand.

```sh
chainctl iam identity-provider update
```

This can be useful for rotating client credentials.

Lastly, to delete an identity provider, run the `delete` subcommand.

```sh
chainctl iam identity-provider delete
```

For more details, check out the [`chainctl` documentation for these commands](/chainguard/chainctl/chainctl-docs/chainctl_iam_identity-providers/).

## IAM and security

Once an identity provider has been created on the Chainguard platform, any user that can authenticate with that identity provider will be able to use it to access the Chainguard platform. It’s important to note that users can do so even if they have no IAM capabilities with the IAM organization at which the identity provider is defined. Identity providers give access to the Chainguard platform, but not the specific IAM organization where the identity provider is defined.

The IAM capabilities `identity_providers.create`, `identity_providers.update`, `identity_providers.list` and `identity_providers.delete` control which users can read and manipulate identity providers. The built-in roles `viewer`, `editor` and `owner` have the following capabilities related to identity providers.

| **Role** | **Capabilities** |
|----------|----------|
| `viewer`   | `identity_providers.list`   |
| `editor`   | `identity_providers.list`   |
| `owner`   | `identity_providers.create`, `identity_providers.list`, `identity_providers.update`, `identity_providers.delete`   |

## Backup accounts

In the case of an outage or misconfiguration of your identity provider, it can be helpful to have an authentication mechanism to the Chainguard platform outside of your SSO identity provider for recovery purposes. To this end, you can use one of our OIDC login providers (currently Google, GitHub, or GitLab) to create a backup account.

As an OIDC login account needs to be set up to bootstrap the SSO identity provider initially, it’s possible to keep this account as a backup account in case you need it for recovery. However, the nature of these OIDC provider accounts is such that it is difficult to share them as a backup resource since they’re often tied to a single user.

Instead of relying on an account with an OIDC login provider, you can alternatively set up an assumable identity to use as a backup account. Refer to our [conceptual guide on assumable identities](/chainguard/administration/iam-organizations/assumable-ids/) to learn more.
