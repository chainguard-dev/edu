---
title: "How Guarded Entrypoint works"
linktitle: "How it works"
type: "article"
description: "What the Guarded Entrypoint wrapper does at container start: secret references, fail mode, preflight checks, command override, and variable expansion."
date: 2026-10-06T17:41:00+00:00
lastmod: 2026-10-06T17:41:00+00:00
draft: false
tags: ["Chainguard Containers", "Custom Assembly", "Conceptual", "Reference"]
images: []
menu:
  docs:
    parent: "guarded-entrypoint"
weight: 10
toc: true
---

{{< beta feature="Guarded Entrypoint" access="every organization that has Custom Assembly" feedback="true" >}}

This page describes what the Guarded Entrypoint binary does when a container starts. The page calls the binary the wrapper. To turn Guarded Entrypoint on, see [Guarded Entrypoint for Custom Assembly](/chainguard/containers/custom-assembly/guarded-entrypoint/).

## What the wrapper does

When you turn on Guarded Entrypoint, Chainguard rebuilds the image with `/usr/bin/guarded-entrypoint` as the first element of its entrypoint. The image's original entrypoint follows it. Chainguard stores your settings in environment variables in the image configuration. The names of these variables start with `GUARDED_`. You can see them with `docker inspect`. The `GUARDED_` prefix is reserved, and the API rejects it in your own `environment` keys.

On every start, the wrapper runs these steps in order:

1. **Check for the escape hatch.** If `GUARDED_DISABLE` is set, the wrapper starts the original entrypoint and does nothing else. See [Troubleshoot a wrapped container](/chainguard/containers/custom-assembly/guarded-entrypoint/troubleshooting/).
1. **Resolve secret references.** The wrapper replaces every environment value of the form `cg+BACKEND://REF` with the secret it names.
1. **Resolve the command.** The wrapper applies `command_override`, if you set one, and expands `${VAR}` in it.
1. **Run preflight checks.** The wrapper waits for the TCP endpoints and paths you listed.
1. **Start your application.** The application runs as the wrapper's child process.

While the application runs, the wrapper forwards every signal it can catch to the application and reaps orphaned processes. When the application exits, the wrapper exits with the same exit code. If a signal kills the application, the wrapper exits with 128 plus the signal number.

The wrapper writes its own messages as JSON, one object per line, to standard error. Set `GUARDED_ENTRYPOINT_LOG` on the container to `debug`, `info`, `warn`, or `quiet` to change the level. The wrapper never logs a resolved secret value. It replaces any value it resolved or expanded with `***` in its log lines.

### What the wrapper doesn't do

* It doesn't resolve references in the container's arguments. It resolves only environment values. Kubernetes expands `$(VAR)` in `args` before the wrapper runs, so `--password=$(DB_PASSWORD)` reaches the application as the literal `cg+...` reference. Have the application read secrets from its environment, or pass them through `command_override`, which expands after resolution.
* It doesn't renew or revoke Vault leases. It reads each secret once, at startup.
* It doesn't run code that you upload. It runs your application and, if you set `command_override`, the command you list.
* It doesn't connect to Chainguard. See [Guarded Entrypoint trust boundary](/chainguard/containers/custom-assembly/guarded-entrypoint/trust-boundary/).

## Secret references

A secret reference is an environment variable whose value has the form `cg+BACKEND://REF`. Put references in the `environment` key of the repo's manifest. The wrapper also resolves references in variables that you set in your pod spec or `docker run` command.

The `cg+` prefix is reserved. A value without it, such as a bare `vault://` or `consul://` URI, passes through to your application as a plain string. A value with the prefix must resolve. A malformed reference, an unknown backend, a failed lookup, or a secret that contains a NUL byte stops the container before the application starts, unless you set [fail mode](#fail-mode) to `open`.

| Backend | Reference | Reads |
| --- | --- | --- |
| Vault | `cg+vault://PATH[?version=N]#KEY` | One field, `KEY`, of the secret at the Vault API path `PATH` |
| Consul | `cg+consul://KEY` | The whole value of one key in the Consul key-value store |
| Google Secret Manager | `cg+gsm://projects/P/secrets/S/versions/V` | One version of a secret. `V` is a version number, `latest`, or an alias. |

The wrapper retries HTTP 429 and 5xx responses and connection errors up to three times, with backoff. Resolution has a budget of 30 seconds in total.

### Vault references

`PATH` is the path of the Vault API request, as in `envconsul` and Vault Agent templates. For a KV version 2 mount, the path includes `/data/`. The wrapper does not look up mounts or insert it. `#KEY` is required.

| Reference | Reads |
| --- | --- |
| `cg+vault://secret/data/app#password` | KV version 2 mount `secret`, secret `app`, latest version |
| `cg+vault://secret/data/app?version=3#password` | The same secret, version 3 |
| `cg+vault://kv/app#password` | KV version 1 mount `kv`, secret `app` |

A string value is set as is. A number, boolean, null, object, or array is set as its compact JSON text. A key that the secret lacks is an error.

The wrapper reads its Vault settings from the container's environment. They must be literal values, not references.

| Variable | Meaning |
| --- | --- |
| `VAULT_ADDR` | Required. For example, `https://vault.example.com:8200`. An `http://` address sends the token in the clear. |
| `VAULT_TOKEN` | A token to read with. It takes precedence over Kubernetes authentication. |
| `VAULT_K8S_ROLE` | Without `VAULT_TOKEN`, log in with the Kubernetes auth method as this role. |
| `VAULT_K8S_MOUNT` | The Kubernetes auth mount path. The default is `kubernetes`. |
| `VAULT_K8S_TOKEN_PATH` | The service account token to log in with. The default is `/var/run/secrets/kubernetes.io/serviceaccount/token`. |
| `VAULT_NAMESPACE` | The Vault Enterprise or HCP namespace. |
| `VAULT_CACERT` | A PEM bundle, at most 1 MiB, that verifies Vault's certificate in place of the system roots. |

With neither `VAULT_TOKEN` nor `VAULT_K8S_ROLE`, resolution fails with `no Vault credentials`. Use Kubernetes authentication where you can. A `VAULT_TOKEN` in the image or the pod spec is a long-lived secret that anything that can read the spec can see. The wrapper doesn't follow redirects, so `VAULT_ADDR` must name the active Vault node or a load balancer in front of it. Auth methods other than tokens and Kubernetes aren't supported.

### Consul references

`KEY` is one or more segments separated by `/`. A segment can contain letters, digits, and `. _ ~ @ : + = , -`. A key that ends in `/`, an empty segment, a `.` or `..` segment, a query, and a fragment are all invalid. A key stored with no value resolves to an empty string.

The wrapper reads its Consul settings from the container's environment, as the `consul` command does. They must be literal values.

| Variable | Meaning |
| --- | --- |
| `CONSUL_HTTP_ADDR` | `HOST:PORT`, `http://HOST:PORT`, or `https://HOST:PORT`. The default is `127.0.0.1:8500`. |
| `CONSUL_HTTP_SSL` | Set to `true` to use HTTPS with a bare `HOST:PORT`. |
| `CONSUL_HTTP_TOKEN` | The token to read with. Without a token, the read is anonymous. |
| `CONSUL_HTTP_TOKEN_FILE` | A file that holds the token. It wins over `CONSUL_HTTP_TOKEN`. |
| `CONSUL_CACERT` | A PEM file of CAs to trust in place of the system roots. Mount the file in the container. |

The wrapper sends the token only in the `X-Consul-Token` header, doesn't follow redirects, and doesn't use a proxy. It doesn't support `unix://` addresses, `CONSUL_CAPATH`, client certificates, `CONSUL_TLS_SERVER_NAME`, `CONSUL_HTTP_SSL_VERIFY`, `CONSUL_HTTP_AUTH`, or Consul Enterprise namespaces and partitions.

### Google Secret Manager references

The wrapper authenticates with Application Default Credentials. `/versions/latest` is the default version. The wrapper supports only global secrets. A regional secret, `projects/P/locations/L/secrets/S`, is an invalid reference. A service account needs only secret access.

## Fail mode

`fail_mode` sets what happens when a secret reference can't be resolved. It takes one of two values.

| Value | When a reference can't be resolved |
| --- | --- |
| `closed` | The container stops with exit code 121 before your application starts. This is the default. |
| `open` | Your application starts anyway. The variable keeps its literal `cg+...` value, and the wrapper logs one warning for it. |

With `open`, a lookup that fails, missing credentials, a secret that contains a NUL byte, and the 30-second budget running out all leave the reference in place. The warning looks like the following:

```json
{"time":"...","level":"WARN","msg":"secret unresolved, continuing","src":"guarded-entrypoint","name":"DB_PASSWORD","fail_mode":"open","error":"DB_PASSWORD: secret resolution timed out after 30s (context deadline exceeded)"}
```

An unresolved variable is not a secret. Your application sees the literal `cg+...` reference, and anyone who can read the image configuration or the pod spec knows that value. Don't choose `open` for a variable that your application uses as a password, token, or other credential. During an outage the application would start with a known value as its credential.

`open` covers a store that can't serve a reference. It doesn't cover a reference that can never resolve. These configuration errors still stop the container with exit code 121:

* A malformed reference
* An unknown backend, such as a `cg+gms://` typo
* A reference that the backend rejects by its shape
* A `${VAR}` in the command that names a variable that is unset or that `open` left unresolved

A repo that sets `fail_mode: open` has `GUARDED_FAIL_MODE=open` in its image environment. A `closed` repo's image carries no setting.

## Preflight checks

A preflight check waits for a dependency before your application starts. Each entry in `preflight` has the following keys:

| Key | Meaning | Default |
| --- | --- | --- |
| `tcp` | A `host:port` to wait for a TCP connection to. | None |
| `path` | A filesystem path to wait for. | None |
| `timeout` | The total time to wait for this check, as a Go duration such as `30s` or `2m`. A value of `0` means the default, not forever. | `30s` |
| `interval` | The pause between attempts, as a Go duration. | `500ms` |
| `on_failure` | `fail` stops the container with exit code 122. `continue` logs a warning and moves on. | `fail` |

Set exactly one of `tcp` and `path` in each entry. The wrapper expands `${VAR}` in both from the resolved environment. A target that expands to nothing, or to an empty host, fails at once. An overlay or repo can hold at most 32 entries. Values can't contain `,` or `=`.

The checks run in order, after secret resolution. Because a preflight target is not scrubbed from logs, don't use a variable that holds a secret in one.

## Command override

`command_override` changes what the wrapper starts. It has two keys: `mode` and `command`. The wrapper receives the image's own arguments, which are its original ENTRYPOINT followed by its CMD, or the arguments that you pass when you run the container. The `mode` sets how `command` combines with them.

| Mode | What the wrapper starts |
| --- | --- |
| `default` | `command` only when the container passes no arguments. Otherwise, the container's arguments. |
| `prepend` | `command` followed by the container's arguments. |
| `override` | `command` alone. The image's ENTRYPOINT and CMD, and any arguments passed at run time, are dropped. |

`default` is the mode when you leave `mode` out. The `prepend` and `override` modes require a non-empty `command`.

The image's ENTRYPOINT and CMD are the same in every mode. The mode only changes what the wrapper starts. To replace both an ENTRYPOINT and a CMD, use `override`.

The wrapper looks up the first element of `command` on the container's `PATH`. Use an absolute path when the lookup matters.

An empty `command` with `command_override` set is a setting. It means "default mode, no command". When you use tag-based Custom Assembly, it cancels the override from a broader binding.

`command` is stored in the image configuration and is visible to anyone who can pull the image. Don't put a secret in it as a literal. Use a `${VAR}` reference, as the next section describes. See also [Guarded Entrypoint trust boundary](/chainguard/containers/custom-assembly/guarded-entrypoint/trust-boundary/).

## Variable expansion

The wrapper expands variables in each `command` entry and in preflight `tcp` and `path` values. It expands from the environment after secret references resolve.

* `${NAME}` expands to the value of `NAME`. A name starts with a letter or `_` and continues with letters, digits, or `_`.
* `$$` is a literal `$`.
* Any other `$` stays as it is. `$NAME` is not expanded.
* A `${NAME}` whose variable is not set stops the container with exit code 121 in a command, and fails the check in a preflight. It never expands to an empty string. A variable that is set and empty expands to nothing.
* The wrapper never expands the container's own arguments.

The wrapper doesn't support shell forms such as `${NAME:-default}`. The API rejects a `${...}` reference with an invalid name. To pass a `$` to a shell that runs in the image, write `$$`. For example, the following command override passes `${PORT:-8080}` to `sh` unchanged. It needs an image that includes a shell:

```yaml
guarded_entrypoint: true
command_override:
  mode: override
  command:
    - sh
    - -c
    - exec my-app --port $${PORT:-8080}
```

The wrapper never expands a variable that `open` left unresolved. An expanded value is visible in the application's command line to anything that can read the process's `/proc/PID/cmdline`. The wrapper can't hide it there.

## Supported and refused entrypoints

The wrapper wraps entrypoints that run one program. It refuses an entrypoint it can't preserve. In that case the build fails with a message that names the reason, instead of producing an image with a broken entrypoint.

The wrapper refuses these entrypoints:

* An entrypoint that is a shell fragment.
* An entrypoint that is a service bundle, which runs a supervisor over several processes.

The lists of the supported and refused entrypoints for each image come from a generated report. See the [lists of supported and refused entrypoints](https://PLACEHOLDER.invalid/guarded-entrypoint-supported-and-refused-lists). <!-- PLACEHOLDER: replace this URL when the generated lists are published. -->

For how a refusal appears in `chainctl`, see [Entrypoints the wrapper refuses](/chainguard/containers/custom-assembly/guarded-entrypoint/troubleshooting/#entrypoints-the-wrapper-refuses).

## Learn more

* [Guarded Entrypoint examples](/chainguard/containers/custom-assembly/guarded-entrypoint/examples/)
* [Troubleshoot a wrapped container](/chainguard/containers/custom-assembly/guarded-entrypoint/troubleshooting/)
* [Guarded Entrypoint trust boundary](/chainguard/containers/custom-assembly/guarded-entrypoint/trust-boundary/)
