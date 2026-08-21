---
title: "Authentication options for chainctl"
linktitle: "Authentication options"
aliases:
- /chainguard/chainctl-usage/authentication-options/
type: "article"
description: "Learn the login flows chainctl supports, including interactive browser login, headless device-code login, social login providers, and assumable identities."
lead: "chainctl supports several ways to authenticate to the Chainguard platform, so you can log in from a laptop, a browserless server, or a CI/CD pipeline."
date: 2026-08-21T00:00:00+00:00
lastmod: 2026-08-21T00:00:00+00:00
draft: false
tags: ["chainctl"]
images: []
menu:
  docs:
    parent: "chainctl-usage"
toc: true
weight: 020
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

`chainctl` outputs an eight-character code and a URL, [`https://auth.chainguard.dev/activate`](https://auth.chainguard.dev/activate). Open the URL in a browser on any device, enter the code, and complete the login. You can then use Chainguard from the headless device.

The `--headless` code is valid for 900 seconds.

## Select an identity provider with --social-login

To authenticate with a specific default identity provider, pass the `--social-login` flag. The value must be one of `email`, `google`, `github`, or `gitlab`:

```sh
chainctl auth login --social-login github
```

You can also set a default provider in your configuration with the `default.social-login` setting. See [Manage your chainctl configuration](/platform/chainctl-usage/manage-chainctl-config/).

> Note: If your organization has configured a custom identity provider, authenticate with `--org-name` or `--identity-provider` instead. See [custom identity providers](/platform/administration/custom-idps/custom-idps/).

## Assumable identities for CI/CD

Assumable identities let automation tools like GitHub Actions or AWS Lambda connect to and manage Chainguard resources without interactive login. See the [guide on assumable identities](/platform/administration/assumable-ids/assumable-ids/).

## Pull tokens

Pull tokens are ideal for pulling images and libraries and can be long-lived. You can create them in the Chainguard Console or with `chainctl`. See [authenticating to the Chainguard registry](/chainguard/containers/chainguard-registry/authenticating/#authenticating-with-a-pull-token).
