---
title: "Guarded Entrypoint trust boundary"
linktitle: "Trust boundary"
type: "article"
description: "What the Guarded Entrypoint wrapper connects to, what it never does, and what is visible in the image configuration."
date: 2026-10-06T17:41:00+00:00
lastmod: 2026-10-07T21:37:50+00:00
draft: false
tags: ["Chainguard Containers", "Custom Assembly", "Conceptual", "Reference"]
images: []
menu:
  docs:
    parent: "guarded-entrypoint"
weight: 40
toc: true
---

> **Note**: Guarded Entrypoint is in beta. To use it, contact Chainguard customer support to enable it for your organization.

This page states what the [Guarded Entrypoint](/chainguard/containers/custom-assembly/guarded-entrypoint/overview/) wrapper connects to, what it never does, and what anyone who can pull your image can read.

## What the wrapper connects to

The wrapper connects only to the endpoints that your configuration names:

* **Vault:** the address in `VAULT_ADDR`.
* **Consul:** the address in `CONSUL_HTTP_ADDR`. When it isn't set, the default is `127.0.0.1:8500`.
* **Google Secret Manager:** `secretmanager.googleapis.com` and Google's token endpoints. The wrapper authenticates with Application Default Credentials, so it also contacts the GCE or GKE metadata server, which it always reaches directly. Credentials of an external account type add their own source URL.
* **Preflight targets:** the TCP targets that your `preflight` checks name.
* **Proxies:** if you set `HTTPS_PROXY`, the wrapper sends Secret Manager requests and requests to an `https://` Vault address through it. The wrapper never uses a proxy for Consul.

If you build an egress allowlist from this list, include the Google endpoints when you use Secret Manager.

The wrapper makes no connection to Chainguard.

## What the wrapper never does

* It doesn't run code that you upload. The wrapper starts your application and, if you set `command_override`, the command you list.
* It doesn't send telemetry. It sends no data to Chainguard of any kind.
* It doesn't write a resolved secret value to its logs. It replaces a value that it resolved or expanded with `***` in every log line.
* It doesn't send a Vault or Consul credential anywhere except the address you configure, and it doesn't follow redirects when it reads from either. A Secret Manager credential goes to Google's token endpoints and to Secret Manager.

## What is visible in the image

Anyone who can pull the image can read its configuration, for example with `docker inspect`. The configuration includes the following:

| Item | Visible | Notes |
| --- | --- | --- |
| Secret references, such as `cg+vault://secret/data/orders#db_password` | Yes | A reference names where a secret lives. It isn't the secret. Treat the paths as metadata that your organization is willing to share with anyone who can pull the image. |
| Resolved secret values | No | The wrapper resolves them when the container starts, in the container's memory. They are never written to the image. |
| `command_override` text | Yes | Described in the next section. |
| Preflight targets and settings | Yes | The targets are stored in the image configuration. |
| Fail mode | Only when `open` | A repo with `fail_mode: closed` has no setting in its image configuration. |

The settings are stored in image environment variables whose names start with `GUARDED_`. This prefix is reserved for the wrapper. The API rejects an `environment` key that starts with it.

A running container is a different case. The resolved values are in the application's environment, so anyone who can read the process's environment can read them.

## Keep secrets out of command_override

The text of `command_override` is stored in the image configuration. Anyone who can pull the image can read it. Don't write a secret into `command` as a literal.

Put a `${VAR}` reference in `command` instead, and supply the value in the environment. For example, use `${DB_PASSWORD}`, and set `DB_PASSWORD` to a `cg+vault://` reference. The image then holds the reference and not the secret.

An expanded value is visible in the application's command line while the container runs. Anything that can read `/proc/PID/cmdline` can read it, and the wrapper can't prevent that. Prefer to have your application read a secret from its environment.

## The escape hatch

The wrapper honors `GUARDED_DISABLE` before it resolves a reference, runs a preflight check, or reads any other setting. This holds even when the wrapper's settings in the image are malformed. `GUARDED_DISABLE` counts as set unless its value, lowercased and trimmed, is empty, `0`, `false`, `no`, or `off`. A value of `1` or `true` turns the wrapper off. A value of `0` or `false` leaves it on. When the wrapper is off, it makes no network connection.

Anyone who can set environment variables on a container can set `GUARDED_DISABLE`. The wrapper then doesn't resolve references or run checks, and your application starts with the literal `cg+...` values. A repo with `fail_mode: closed` doesn't prevent this.

The same people can override other settings. Every `GUARDED_` setting that Chainguard stores in the image can be overridden from the deployment's environment. So can `VAULT_ADDR` and `CONSUL_HTTP_ADDR`. Pointing `VAULT_ADDR` at another server sends the service account token to that server. Control who can change the environment of your deployments as you would control who can change any other part of the deployment.

For how to use the escape hatch, refer to [Troubleshoot a wrapped container](/chainguard/containers/custom-assembly/guarded-entrypoint/troubleshooting/).

## Learn more

* [Guarded Entrypoint for Custom Assembly](/chainguard/containers/custom-assembly/guarded-entrypoint/overview/)
* [How Guarded Entrypoint works](/chainguard/containers/custom-assembly/guarded-entrypoint/how-it-works/)
