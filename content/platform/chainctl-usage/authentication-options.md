---
title: "Authentication options for chainctl"
linktitle: "Authentication options"
aliases:
- /chainguard/chainctl-usage/authentication-options/
type: "article"
description: "Learn the login flows chainctl supports, including interactive browser login, headless device-code login, social login providers, and assumable identities."
lead: "chainctl supports several ways to authenticate to the Chainguard platform, so you can log in from a laptop, a browserless server, or a CI/CD pipeline."
date: 2026-08-21T00:00:00+00:00
lastmod: 2026-10-01T17:08:58+00:00
draft: false
tags: ["chainctl"]
images: []
menu:
  docs:
    parent: "chainctl-usage"
toc: true
weight: 20
---

There are several ways to authenticate to the Chainguard platform with `chainctl`, each suited to a different environment:

* **Interactive login**: Good for everyday interactive use, but needs a browser that the current shell can launch.
* **Headless login**: Also good for interactive use. It still requires a browser, but not from within the current shell or even the current device.
* **Social login**: Lets you choose which default identity provider (email, Google, GitHub, or GitLab) to authenticate with.
* **Assumable identities**: Designed for CI/CD and require no interaction, but they need more setup and aren't ideal outside automation.
* **Pull tokens**: Ideal for pulling images and libraries, and they can be long-lived.

## Interactive browser login

To authenticate to the Chainguard platform, run the following command:

```sh
chainctl auth login
```

A browser window opens and prompts you to log in through your chosen OIDC flow. Select the account you want to log in as, and then you can begin managing your Chainguard resources.

## Headless device-code login

If the shell can't launch a browser—for example, on a container or a remote server—use the `--headless` option to log in through a device-code flow:

```sh
chainctl auth login --headless
```

`chainctl` prints a single URL with a one-time code embedded in it:

```output
Visit this URL on any device with a browser to authenticate: https://issuer.enforce.dev/oauth?headless_code=<code>
```

Open the URL in a browser on any device and complete the login. You don't type the code anywhere. If you also pass `--social-login`, the URL includes a `connection` parameter that names the provider.

`chainctl` waits about 10 minutes for the browser login to finish, and then you can use Chainguard from the headless device. If time runs out, `chainctl` exits with a `timed out waiting` error. Run the command again to get a new URL.

### Headless mode persists after you use it

When you pass `--headless`, `chainctl` saves headless as your default login mode and tells you so:

```output
Saving "headless" as default auth mode to chainctl configuration. To disable: chainctl config unset auth.mode
```

From then on, `chainctl auth login` uses the device flow even without `--headless`, and so does any command that logs you in again after your token expires. Instead of opening a browser, the command prints a URL and waits for you to complete the login. If you miss the URL, the command can look like it has stopped responding.

To return to browser login, remove the setting:

```sh
chainctl config unset auth.mode
```

## Select an identity provider with --social-login

To authenticate with a specific default identity provider, pass the `--social-login` flag. The value must be one of `email`, `google`, `github`, or `gitlab`:

```sh
chainctl auth login --social-login github
```

You can also set a default provider in your configuration with the `default.social-login` setting. See [Manage your chainctl configuration](/platform/chainctl-usage/manage-chainctl-config/).

> Note: If your organization has configured a custom identity provider, authenticate with `--org-name` or `--identity-provider` instead. See [custom identity providers](/platform/administration/custom-idps/custom-idps/).

Which provider you authenticate with also determines who manages your multi-factor authentication. To move it to a new device, see [Change or reset your MFA device](/get-started/mfa-devices/).

## Assumable identities for CI/CD

Assumable identities let automation tools like GitHub Actions or AWS Lambda connect to and manage Chainguard resources without interactive login. See the [guide on assumable identities](/platform/administration/assumable-ids/assumable-ids/).

## Pull tokens

Pull tokens are ideal for pulling images and libraries and can be long-lived. You can create them in the Chainguard Console or with `chainctl`. See [authenticating to the Chainguard registry](/chainguard/containers/registry/authenticating/#authenticating-with-a-pull-token).

A pull token is a pair of values that most tools consume as a username and a password. `chainctl` labels that pair differently in each output format, so refer to [pull token output formats and credential names](/platform/chainctl-usage/pull-token-output/) to map the labels to each other.

## Troubleshoot chainctl login

The following sections cover the most common reasons `chainctl auth login` fails or stalls. After you apply a fix, confirm that you're logged in:

```sh
chainctl auth status
```

### Login prints a URL instead of opening a browser

If `chainctl auth login` prints a URL and waits, your configuration is probably set to headless mode. Check the `auth` section of your configuration:

```sh
chainctl config view
```

If it shows `mode: headless`, either complete the login at the printed URL or [return to browser login](#headless-mode-persists-after-you-use-it).

### Login hangs or fails behind a TLS-inspecting proxy

Corporate proxies that decrypt and inspect TLS traffic, such as Netskope or Zscaler, can break `chainctl` login. The login might wait indefinitely, or fail with an error such as `context deadline exceeded`, `missing selected ALPN property`, or `timed out validating the new token`. Run the command with `--log-level=debug` to see which request fails.

Ask your network administrator to exempt these hosts from TLS inspection:

* `issuer.enforce.dev` and `console-api.enforce.dev`, which every login needs
* `auth.chainguard.dev` and `chainguard.us.auth0.com`, which social login also needs

For the full list of hosts that Chainguard tools use, see [Network requirements](/chainguard/containers/registry/network-requirements/).

If the proxy mishandles HTTP/2, downgrade the login's STS requests to HTTP/1.x:

```sh
chainctl auth login --sts-http1-downgrade
```

This flag affects only STS requests. Other `chainctl` commands still need encrypted HTTP/2 through the proxy, so treat the flag as a workaround until your network administrator adds the exemption.

### Organization not found or not verified

If login fails with an error that the organization is "not found, is not verified, or does not have an IDP configured," `chainctl` couldn't match the organization name you entered. Enter your organization's verified domain, such as `example.com`, rather than its display name. To skip the prompt, pass the domain with `--org-name`:

```sh
chainctl auth login --org-name=example.com
```

If your organization uses a custom identity provider, you can pass its ID with `--identity-provider` instead. See [custom identity providers](/platform/administration/custom-idps/custom-idps/).
