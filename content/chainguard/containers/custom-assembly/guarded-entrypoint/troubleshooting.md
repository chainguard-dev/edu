---
title: "Troubleshoot a wrapped container"
linktitle: "Troubleshooting"
type: "article"
description: "How to recover a container that fails to start under Guarded Entrypoint, what the wrapper's exit codes mean, and how a refused build appears in chainctl."
date: 2026-10-06T17:41:00+00:00
lastmod: 2026-10-07T21:37:50+00:00
draft: false
tags: ["Chainguard Containers", "Custom Assembly", "Troubleshooting", "Debugging"]
images: []
menu:
  docs:
    parent: "guarded-entrypoint"
weight: 30
toc: true
---

> **Note**: Guarded Entrypoint is in beta. To use it, contact Chainguard customer support to enable it for your organization.

This page covers two kinds of problems. A container that is built with [Guarded Entrypoint](/chainguard/containers/custom-assembly/guarded-entrypoint/overview/) can fail to start. A build can also fail because Chainguard refuses to wrap an image.

## First move: set GUARDED_DISABLE

When a wrapped container fails to start, set the `GUARDED_DISABLE` environment variable on the container and redeploy. The wrapper then starts the image's original entrypoint and arguments without doing anything else. You don't need to rebuild the image.

With Kubernetes, set the variable on the deployment:

```shell
kubectl set env deployment/$DEPLOYMENT GUARDED_DISABLE=1
```

With Docker, pass it to `docker run`:

```shell
docker run -e GUARDED_DISABLE=1 cgr.dev/$ORGANIZATION/$REPO:latest
```

`GUARDED_DISABLE` counts as set unless its value, lowercased and trimmed, is empty, `0`, `false`, `no`, or `off`. A value of `1` or `true` turns the wrapper off. A value of `0` or `false` leaves it on. The wrapper checks `GUARDED_DISABLE` before it reads any other setting. This means that a malformed setting in the image doesn't stop it from working.

When `GUARDED_DISABLE` is set, the wrapper does the following:

* It doesn't resolve secret references. Your application sees the literal `cg+...` values.
* It doesn't run preflight checks.
* It doesn't apply `command_override`. The image's original ENTRYPOINT and CMD run.
* It makes no network connections.

If the container then starts, the wrapper or its settings might have caused the failure. Remove the variable after you fix the configuration and Chainguard rebuilds the image.

If the container still fails, the cause isn't necessarily the application or the deployment. With `GUARDED_DISABLE` set, your application receives the literal `cg+...` values, and the preflight checks don't run. An application that needs its secrets can fail for that reason.

With `GUARDED_DISABLE` set, an image whose only command comes from `command_override` exits with code `124` instead of starting.

Anyone who can set environment variables on a container can set `GUARDED_DISABLE`. This is true for a repo with `fail_mode: closed` too. Refer to [Guarded Entrypoint trust boundary](/chainguard/containers/custom-assembly/guarded-entrypoint/trust-boundary/).

## Find out why the container stopped

Start with the container's exit code. For a Kubernetes pod, `kubectl describe pod` shows it under `Last State`. For Docker, run the following command:

```shell
docker inspect --format '{{.State.ExitCode}}' $CONTAINER
```

Then read the container's logs. The wrapper writes JSON messages to standard error, one object per line, and each message names the setting or variable that failed. It never logs a secret value:

```shell
kubectl logs $POD
```

For a pod in a restart loop, add `--previous` to read the logs of the container that stopped.

For more detail, set `GUARDED_ENTRYPOINT_LOG` on the container to `debug`. The levels are `debug`, `info`, `warn`, and `quiet`.

### Exit codes before the application starts

The wrapper uses the following exit codes when it stops the container before your application runs. Once the application starts, the container exits with the application's exit code.

| Code | Meaning | What to check |
| --- | --- | --- |
| `120` | A Guarded Entrypoint setting is invalid. | Check the setting that the log message names. |
| `121` | Secret resolution failed. This includes a `${VAR}` in the command that names a variable that isn't set. | Check the backend address, credentials, and reference. Check that each `${VAR}` has a value. |
| `122` | A preflight check failed. | Check that the target is reachable from the container, and consider a longer `timeout`. |
| `123` | There is no command to run. | Check that the image has an entrypoint or CMD, or that `command_override` sets a command. |
| `124` | `GUARDED_DISABLE` is set and there is no command to run. | Pass a command, or check that the image has an entrypoint or CMD. |
| `125` | The wrapper itself failed, for example when it couldn't fork a process. | Check the container's resource limits. |
| `126` | The command exists but can't be run. | Check the execute permission, that the command is not a directory, and that a script's `#!` interpreter exists. |
| `127` | The command wasn't found. | Check that the first element of `command` is on the container's `PATH`, or use an absolute path. |

Your own application can also exit with any code from `120` to `127`. To tell the two apart, look in the logs for a wrapper error line just before the container exited.

With `fail_mode: open`, only the configuration errors described in [Fail mode](/chainguard/containers/custom-assembly/guarded-entrypoint/how-it-works/#fail-mode) stop the container with exit code `121`.

### A container whose entrypoint is an init system

An image whose entrypoint is an init system that must run as PID 1, such as systemd or s6-overlay, doesn't work under the wrapper. The container behaves in one of two ways:

* It exits with code `1` at start, and systemd prints `Explicit --user argument required to run as user manager.`
* It exits with code `129` when you stop it.

To fix it, set `GUARDED_DISABLE` on the deployment, or turn off Guarded Entrypoint for the repo. Refer to [Init systems aren't supported](/chainguard/containers/custom-assembly/guarded-entrypoint/how-it-works/#init-systems-arent-supported).

## Entrypoints the wrapper refuses

When Chainguard can't wrap an image, the rebuild of that image fails. Chainguard doesn't ship a broken image. Instead, the build records a failure and its reason.

To find the failure, list the repo's builds:

```shell
chainctl images repos build list --repo $REPO --parent $ORGANIZATION
```

The `Result` column shows the failure, and the `Reason` column shows why. Chainguard fills the `Reason` column only for failures that it records outside a build, such as these refusals and binding conflicts. It is empty for an ordinary build failure. The failed build has no tags in the `Tags` column. For the full text, run `chainctl images repos build logs --repo $REPO --parent $ORGANIZATION` and select the failed build. Without a terminal, for example in a pipeline, pass `--build-id` with the build's ID. The output has this form:

```output
guarded entrypoint refused for tags [latest] (digest sha256:...): the environment sets GUARDED_DISABLE; the tags are not rebuilt and are dropped from the repo's active tag list until the refusal is resolved
detail: set in the base image environment
```

The optional second line, `detail: ...`, gives more information. If the repo sets `command_override`, the detail also says that `command_override` is not applied.

The text after the digest is the reason. It is one of the following:

| Reason | Meaning |
| --- | --- |
| `the environment sets GUARDED_DISABLE` | The image's environment sets `GUARDED_DISABLE`. The detail says where it is set. |
| `the listed wrapper version does not read every GUARDED_* setting` | The repo's `contents.packages` pins `guarded-entrypoint` or `guarded-entrypoint-fips` to a release that is too old for the repo's settings. The detail names the first release that reads them all. |

The tags named in the message aren't rebuilt until you resolve the refusal. A tag that isn't rebuilt doesn't receive package updates, including CVE fixes, until then. To resolve it, do one of the following:

* For the wrapper version reason, remove the `guarded-entrypoint` or `guarded-entrypoint-fips` pin from the repo's `contents.packages` list.
* Turn off Guarded Entrypoint for the repo. Refer to [Turn off Guarded Entrypoint](/chainguard/containers/custom-assembly/guarded-entrypoint/overview/#turn-off-guarded-entrypoint).
* With Custom Assembly Overlays, bind the overlay that sets `guarded_entrypoint` only to the tags that Chainguard doesn't refuse.

To check ahead of time whether an image is supported, refer to [Supported and refused entrypoints](/chainguard/containers/custom-assembly/guarded-entrypoint/how-it-works/#supported-and-refused-entrypoints).

## Learn more

* [How Guarded Entrypoint works](/chainguard/containers/custom-assembly/guarded-entrypoint/how-it-works/)
* [Guarded Entrypoint examples](/chainguard/containers/custom-assembly/guarded-entrypoint/examples/)
* [Guarded Entrypoint trust boundary](/chainguard/containers/custom-assembly/guarded-entrypoint/trust-boundary/)
