---
title: "Guarded Entrypoint trust boundary"
linktitle: "Trust boundary"
type: "article"
description: "What the Guarded Entrypoint wrapper connects to, what it never does, and what is visible in the image configuration."
date: 2026-10-06T17:41:00+00:00
lastmod: 2026-10-06T17:41:00+00:00
draft: false
tags: ["Chainguard Containers", "Custom Assembly", "Conceptual", "Reference"]
images: []
menu:
  docs:
    parent: "guarded-entrypoint"
weight: 40
toc: true
---

{{< beta feature="Guarded Entrypoint" access="every organization that has Custom Assembly" feedback="true" >}}

This page states what the [Guarded Entrypoint](/chainguard/containers/custom-assembly/guarded-entrypoint/) wrapper connects to, what it never does, and what anyone who can pull your image can read.

## What the wrapper connects to

The wrapper connects only to the endpoints that you configure:

* The secret backends that your references name: Vault, Consul, or Google Secret Manager.
* The TCP targets that your `preflight` checks name.

The wrapper makes no connection to Chainguard.

## What the wrapper never does

* It doesn't run code that you upload. The wrapper starts your application and, if you set `command_override`, the command you list.
* It doesn't send telemetry. It sends no data to Chainguard of any kind.
* It doesn't write a resolved secret value to its logs. It replaces a value that it resolved or expanded with `***` in every log line.
* It doesn't send a backend credential anywhere except the backend address you configure. It doesn't follow redirects when it reads from Vault or Consul.

## What is visible in the image

Anyone who can pull the image can read its configuration, for example with `docker inspect`. The configuration includes the following:

| Item | Visible | Notes |
| --- | --- | --- |
| Secret references, such as `cg+vault://secret/data/orders#db_password` | Yes | A reference names where a secret lives. It isn't the secret. Treat the paths as metadata that your organization is willing to share with anyone who can pull the image. |
| Resolved secret values | No | The wrapper resolves them when the container starts, in the container's memory. They are never written to the image. |
| `command_override` text | Yes | See the next section. |
| Preflight targets and settings | Yes | The targets are stored in the image configuration. |
| Fail mode | Yes | The setting is stored in the image configuration. |

The settings are stored in image environment variables whose names start with `GUARDED_`. This prefix is reserved for the wrapper. The API rejects an `environment` key that starts with it.

A running container is a different case. The resolved values are in the application's environment, so anyone who can read the process's environment can read them.

## Keep secrets out of command_override

The text of `command_override` is stored in the image configuration. Anyone who can pull the image can read it. Don't write a secret into `command` as a literal.

Put a `${VAR}` reference in `command` instead, and supply the value in the environment. For example, use `${DB_PASSWORD}`, and set `DB_PASSWORD` to a `cg+vault://` reference. The image then holds the reference and not the secret.

An expanded value is visible in the application's command line while the container runs. Anything that can read `/proc/PID/cmdline` can see it, and the wrapper can't prevent that. Prefer to have your application read a secret from its environment.

## The escape hatch

The wrapper honors `GUARDED_DISABLE` before it resolves a reference, runs a preflight check, or reads any other setting. This holds even when the wrapper's settings in the image are malformed. When `GUARDED_DISABLE` is set, the wrapper makes no network connection.

Anyone who can set environment variables on a container can set `GUARDED_DISABLE`. The wrapper then doesn't resolve references or run checks, and your application starts with the literal `cg+...` values. A repo with `fail_mode: closed` doesn't prevent this. Control who can change the environment of your deployments as you would control who can change any other part of the deployment.

For how to use the escape hatch, see [Troubleshoot a wrapped container](/chainguard/containers/custom-assembly/guarded-entrypoint/troubleshooting/).

## Learn more

* [Guarded Entrypoint for Custom Assembly](/chainguard/containers/custom-assembly/guarded-entrypoint/)
* [How Guarded Entrypoint works](/chainguard/containers/custom-assembly/guarded-entrypoint/how-it-works/)
