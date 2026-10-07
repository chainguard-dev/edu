---
title: "Guarded Entrypoint examples"
linktitle: "Examples"
type: "article"
description: "Example Custom Assembly manifests that use Guarded Entrypoint to inject secrets, wait for a dependency, override a command, and fail open."
date: 2026-10-06T17:41:00+00:00
lastmod: 2026-10-07T19:01:58+00:00
draft: false
tags: ["Chainguard Containers", "Custom Assembly", "Procedural", "Configuration"]
images: []
menu:
  docs:
    parent: "guarded-entrypoint"
weight: 20
toc: true
---

> **Note**: Guarded Entrypoint is in beta. To use it, contact Chainguard customer support to enable it for your organization.

This page has four example manifests for [Guarded Entrypoint](/chainguard/containers/custom-assembly/guarded-entrypoint/). Each one is a complete manifest for `chainctl images repos build edit` or `chainctl images repos build apply`. None of them contains a literal secret. Each secret is a reference that the wrapper resolves when the container starts.

Applying a manifest replaces the repo's stored configuration. If your repo already has other customizations, such as packages, add the Guarded Entrypoint keys to your existing manifest instead of replacing it.

The examples use the following variables:

```shell
export REPO=my-custom-app
```

To try an example, save it as `build.yaml`. Preview the change, then apply it:

```shell
chainctl images repos build apply -f build.yaml --repo $REPO --dry-run
chainctl images repos build apply -f build.yaml --repo $REPO --yes
```

The first command prints the diff and exits with a non-zero status when it finds a change. The second command applies the manifest and starts a rebuild.

## Inject secrets from Vault or Consul into a Java application

A Java application reads its database password and an API address from its environment. Today the team adds `envconsul` to a derived image to supply them. With Guarded Entrypoint, the references are part of the Custom Assembly repo.

```yaml
guarded_entrypoint: true
environment:
  VAULT_ADDR: https://vault.example.com:8200
  VAULT_K8S_ROLE: orders-service
  DB_PASSWORD: cg+vault://secret/data/orders#db_password
  CONSUL_HTTP_ADDR: https://consul.example.com:8501
  ORDERS_API_URL: cg+consul://apps/orders/api-url
```

When the container starts, the wrapper does the following:

1. Logs in to Vault with the Kubernetes auth method as the `orders-service` role. It reads the `db_password` field of the `orders` secret, in the `secret` KV version 2 mount, into `DB_PASSWORD`.
1. Reads the `apps/orders/api-url` key from Consul into `ORDERS_API_URL`.
1. Starts the Java application with both variables resolved.

The image stores the references and the addresses. It doesn't store the secrets. To read from Consul with a token, set `CONSUL_HTTP_TOKEN` or `CONSUL_HTTP_TOKEN_FILE` on the deployment, not in the manifest. A token in the manifest would be visible to anyone who can pull the image.

The default `fail_mode` is `closed`. If Vault or Consul can't serve a reference, the container stops with exit code 121 and the application doesn't start.

## Wait for a dependency before starting

An application fails when its database isn't ready at start. The following manifest holds the container until the database accepts connections, and then checks that a mounted file exists:

```yaml
guarded_entrypoint: true
preflight:
  - tcp: db.internal:5432
    timeout: 60s
    interval: 1s
    on_failure: fail
  - path: /run/secrets/tls-ready
    timeout: 10s
    on_failure: continue
```

The wrapper runs the checks in order, after it resolves secrets and before it starts the application:

* The first check tries to connect to `db.internal:5432` once a second for up to 60 seconds. If the connection never succeeds, the container stops with exit code 122.
* The second check waits up to 10 seconds for `/run/secrets/tls-ready` to exist. With `on_failure: continue`, the wrapper logs a warning and starts the application if the file never appears.

A target can read from the environment. The following entry waits for the address in the `CACHE_ADDR` variable, which you set on the deployment:

```yaml
guarded_entrypoint: true
preflight:
  - tcp: ${CACHE_ADDR}
    timeout: 30s
```

If `CACHE_ADDR` isn't set, the check fails.

## Override the command on a shell-less Python image

A Python image has no shell and ships with both an ENTRYPOINT and a CMD. The application needs a different command, and both defaults must go. Without Guarded Entrypoint, you build a derived image to do this.

```yaml
guarded_entrypoint: true
environment:
  PORT: "8080"
command_override:
  mode: override
  command:
    - python
    - /app/main.py
    - --port
    - ${PORT}
```

In `override` mode, the wrapper starts `command` alone. The image's ENTRYPOINT and CMD, and any arguments you pass at run time, are dropped. The wrapper expands `${PORT}` from the container's environment, so a deployment can change the port by setting `PORT`. The image needs no shell, because the wrapper starts `python` directly.

To keep the image's own command and add arguments in front of it, use `mode: prepend` instead. See [Command override](/chainguard/containers/custom-assembly/guarded-entrypoint/how-it-works/#command-override).

Don't pass a secret on the command line. The expanded value is visible in the process's command line. Have the application read a secret from its environment, and use a [secret reference](/chainguard/containers/custom-assembly/guarded-entrypoint/how-it-works/#secret-references) to supply it.

## Fail open for a value that isn't a credential

An application reads a feature-flag address from Consul. The application has a built-in default, so it can start when Consul is down. The following manifest sets the repo to fail open:

```yaml
guarded_entrypoint: true
fail_mode: open
environment:
  CONSUL_HTTP_ADDR: https://consul.example.com:8501
  FEATURE_FLAGS_URL: cg+consul://apps/web/feature-flags-url
```

If Consul can't serve the key, the application starts anyway. `FEATURE_FLAGS_URL` keeps the literal value `cg+consul://apps/web/feature-flags-url`, and the wrapper logs a warning for it. The application must handle that value, for example by falling back to its default when the value starts with `cg+`.

Use `open` only for variables that aren't credentials. An unresolved variable holds a value that anyone with access to the image configuration can read. For a password or a token, keep the default of `closed`. See [Fail mode](/chainguard/containers/custom-assembly/guarded-entrypoint/how-it-works/#fail-mode).

## Learn more

* [Guarded Entrypoint for Custom Assembly](/chainguard/containers/custom-assembly/guarded-entrypoint/)
* [How Guarded Entrypoint works](/chainguard/containers/custom-assembly/guarded-entrypoint/how-it-works/)
* [Troubleshoot a wrapped container](/chainguard/containers/custom-assembly/guarded-entrypoint/troubleshooting/)
