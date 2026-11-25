---
title: "Guarded Entrypoint examples"
linktitle: "Examples"
type: "article"
description: "Example Custom Assembly manifests that use Guarded Entrypoint to inject secrets, wait for a dependency, override a command, fail open, and trust a mounted CA in a Java service."
date: 2026-10-06T17:41:00+00:00
lastmod: 2026-10-21T19:24:54+00:00
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

This page has five example manifests for [Guarded Entrypoint](/chainguard/containers/custom-assembly/guarded-entrypoint/overview/), and the deployment settings that go with the truststore examples. Each manifest is complete for `chainctl images repos build edit` or `chainctl images repos build apply`. None of them contains a literal secret. Each secret is a reference that the wrapper resolves when the container starts.

Applying a manifest replaces the repo's stored configuration. If your repo already has other customizations, such as packages, add the Guarded Entrypoint keys to your existing manifest instead of replacing it.

The examples use the following variables:

```shell
export REPO=my-custom-app
export ORGANIZATION=example.com
```

To try an example, save it as `build.yaml`. Preview the change, then apply it:

```shell
chainctl images repos build apply -f build.yaml --repo $REPO --parent $ORGANIZATION --dry-run
chainctl images repos build apply -f build.yaml --repo $REPO --parent $ORGANIZATION --yes
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

The image stores the references and the addresses. It doesn't store the secrets. To read from Consul with a token, set `CONSUL_HTTP_TOKEN` or `CONSUL_HTTP_TOKEN_FILE` on the deployment, not in the manifest. A token in the manifest would be visible to anyone who can pull the image. `VAULT_TOKEN`, if you set it, takes precedence over the Kubernetes login, and `CONSUL_HTTP_TOKEN_FILE` wins over `CONSUL_HTTP_TOKEN`. A token can't be a `cg+` reference.

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

* The first check tries to connect to `db.internal:5432` for up to 60 seconds, and pauses one second between attempts. Each attempt has its own timeout. If the connection never succeeds, the container stops with exit code 122.
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

In `override` mode, the wrapper starts `command` alone. The wrapper drops the image's ENTRYPOINT and CMD, and any arguments you pass at run time. The wrapper expands `${PORT}` from the container's environment, so a deployment can change the port by setting `PORT`. The image needs no shell, because the wrapper starts `python` directly.

To keep the image's own command and add arguments in front of it, use `mode: prepend` instead. Refer to [Command override](/chainguard/containers/custom-assembly/guarded-entrypoint/how-it-works/#command-override).

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

Use `open` only for variables that aren't credentials. An unresolved variable holds a value that anyone with access to the image configuration can read. For a password or a token, keep the default of `closed`. Refer to [Fail mode](/chainguard/containers/custom-assembly/guarded-entrypoint/how-it-works/#fail-mode).

## Trust a mounted CA in a Java service

A Java service calls another service in its cluster. The called service's certificate comes from a CA that the cluster mounts into your container as a file, such as an OpenShift service CA that rotates. The image doesn't contain this CA, so the TLS handshake fails with a certificate path error, such as `PKIX path building failed`.

The following manifest writes a truststore at start. It holds the image's CAs and every certificate in `/etc/service-ca`:

```yaml
guarded_entrypoint: true
truststore:
  - sources:
      - /etc/service-ca
    output: /truststore/cacerts
```

The deployment mounts the CA and a writable directory for the store. It runs with a read-only root filesystem, so the store goes in an `emptyDir` volume:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: orders
spec:
  replicas: 1
  selector:
    matchLabels:
      app: orders
  template:
    metadata:
      labels:
        app: orders
    spec:
      containers:
        - name: orders
          image: cgr.dev/example.com/my-custom-jre:latest
          args: ["-jar", "/app/orders.jar"]
          securityContext:
            readOnlyRootFilesystem: true
          volumeMounts:
            - name: service-ca
              mountPath: /etc/service-ca
              readOnly: true
            - name: truststore
              mountPath: /truststore
      volumes:
        - name: service-ca
          configMap:
            name: service-ca-bundle
        - name: truststore
          emptyDir: {}
```

To check the result, read the wrapper's `truststore written` line, which counts the certificates in the store (`certs`) and the ones your sources added (`added`):

```shell
kubectl logs deployment/orders | grep '"msg":"truststore written"'
```

```output
{"time":"...","level":"INFO","msg":"truststore written","src":"guarded-entrypoint","setting":"GUARDED_TRUSTSTORE_0","path":"/truststore/cacerts","certs":119,"added":1}
```

The wrapper writes the store on every start. When the CA rotates, restart the pods so that the new CA takes effect.

On a FIPS image with a read-only root filesystem, also mount an `emptyDir` volume at `/tmp`. Refer to [Mount the volumes](/chainguard/containers/custom-assembly/guarded-entrypoint/how-it-works/#mount-the-volumes).

## Set the truststore at deploy time

Set `GUARDED_TRUSTSTORE_0` in the container's environment on a wrapped image that Chainguard rebuilt with wrapper 0.2.385 or later. Check the `version` field on the wrapper's `ready` log line. The following settings read the CA from `/certificates` and write the store to `/tmp/cacerts`, on a container with a read-only root filesystem and an `emptyDir` volume at `/tmp`:

```yaml
env:
  - name: GUARDED_TRUSTSTORE_0
    value: source=/certificates,output=/tmp/cacerts
securityContext:
  readOnlyRootFilesystem: true
volumeMounts:
  - name: ca
    mountPath: /certificates
    readOnly: true
  - name: tmp
    mountPath: /tmp
```

For the rules, refer to [Set a truststore at deploy time](/chainguard/containers/custom-assembly/guarded-entrypoint/how-it-works/#set-a-truststore-at-deploy-time).

To keep the `USE_SYSTEM_CA_CERTS` setting from an Eclipse Temurin image, set it to a non-empty value and mount your CA files at `/certificates`:

```yaml
env:
  - name: USE_SYSTEM_CA_CERTS
    value: "1"
```

For the rules, refer to [Temurin compatibility](/chainguard/containers/custom-assembly/guarded-entrypoint/how-it-works/#temurin-compatibility).

## Learn more

* [Guarded Entrypoint for Custom Assembly](/chainguard/containers/custom-assembly/guarded-entrypoint/overview/)
* [How Guarded Entrypoint works](/chainguard/containers/custom-assembly/guarded-entrypoint/how-it-works/)
* [Troubleshoot a wrapped container](/chainguard/containers/custom-assembly/guarded-entrypoint/troubleshooting/)
