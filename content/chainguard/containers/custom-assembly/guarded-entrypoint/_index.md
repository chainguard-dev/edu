---
title: "Guarded Entrypoint for Custom Assembly"
linktitle: "Guarded Entrypoint"
type: "article"
description: "How Guarded Entrypoint lets a Custom Assembly image resolve secrets, run preflight checks, and override its command at container start, and how to turn it on."
date: 2026-10-06T17:41:00+00:00
lastmod: 2026-10-07T19:01:58+00:00
draft: false
tags: ["Chainguard Containers", "Custom Assembly", "Configuration", "Procedural"]
images: []
menu:
  docs:
    parent: "features"
    identifier: "guarded-entrypoint"
weight: 70
toc: true
---

> **Note**: Guarded Entrypoint is in beta. To use it, contact Chainguard customer support to enable it for your organization.

Guarded Entrypoint lets a Custom Assembly image run startup logic without a derived image build. You declare the logic as part of your Custom Assembly configuration. Chainguard builds it into the image and signs the result.

This page explains what Guarded Entrypoint is and how to turn it on. The other pages in this section cover the details:

* [How Guarded Entrypoint works](/chainguard/containers/custom-assembly/guarded-entrypoint/how-it-works/)
* [Guarded Entrypoint examples](/chainguard/containers/custom-assembly/guarded-entrypoint/examples/)
* [Troubleshoot a wrapped container](/chainguard/containers/custom-assembly/guarded-entrypoint/troubleshooting/)
* [Guarded Entrypoint trust boundary](/chainguard/containers/custom-assembly/guarded-entrypoint/trust-boundary/)

## What Guarded Entrypoint is

Many applications need to do some work before they start. They read secrets into environment variables, wait for a database to accept connections, or change the command they run.

A Chainguard image gives you one way to change its entrypoint: build a new image on top of it. That derived image is no longer the image Chainguard signs and rebuilds. Scanners report the difference, and the image does not pick up Chainguard's rebuilds unless you rebuild it too.

Guarded Entrypoint removes the need for the derived build. When you turn it on for a Custom Assembly repo, Chainguard sets the image's entrypoint to a small binary that Chainguard builds, `/usr/bin/guarded-entrypoint`. When the container starts, the binary does the following:

1. Resolves secret references in the container's environment.
2. Runs the preflight checks you configured.
3. Starts your application as its child process.

The binary forwards signals to your application and exits with your application's exit code. The image you deploy is the image Chainguard built, with your startup settings stored in its configuration.

## Prerequisites

Before you start, you need the following:

* A Custom Assembly repo. See the [Custom Assembly overview](/chainguard/containers/custom-assembly/overview/) to create one.
* A role that lets you edit Custom Assembly repos. See the [Custom Assembly permissions requirements](/chainguard/containers/custom-assembly/overview/#custom-assembly-permissions-requirements).
* The latest [`chainctl`](/platform/chainctl-usage/how-to-install-chainctl/). Run `chainctl update` to update it.
* Guarded Entrypoint enabled for your organization. It's a beta feature, so contact Chainguard customer support to enable it. Until then, the API rejects `guarded_entrypoint` with the error in [API errors](#api-errors).

The examples on this page use the following environment variables. Set them to match your organization and repo:

```shell
export ORGANIZATION=example.com
export REPO=my-custom-python
```

## Turn on Guarded Entrypoint with chainctl

A repo's Custom Assembly configuration is a YAML manifest. Guarded Entrypoint adds four keys to it:

| Key | Meaning |
| --- | --- |
| `guarded_entrypoint` | Set to `true` to wrap the image's entrypoint. Every other key in this table requires it. |
| `fail_mode` | `closed` (the default) or `open`. Sets what happens when a secret reference can't be resolved. |
| `preflight` | A list of checks to run before the application starts. |
| `command_override` | A command to run in place of, or in front of, the image's own command. |

Secret references go in the existing `environment` key. For details on each key, see [How Guarded Entrypoint works](/chainguard/containers/custom-assembly/guarded-entrypoint/how-it-works/).

To turn it on interactively, open the repo's manifest in your editor:

```shell
chainctl images repos build edit --repo $REPO
```

Add the keys you need. The following manifest turns on Guarded Entrypoint and resolves one secret from Vault:

```yaml
guarded_entrypoint: true
environment:
  VAULT_ADDR: https://vault.example.com:8200
  VAULT_K8S_ROLE: orders-service
  DB_PASSWORD: cg+vault://secret/data/orders#db_password
```

Keep the keys that are already in the manifest. Applying a manifest replaces the repo's stored configuration, so a key you remove from the manifest is removed from the repo.

Save and close the editor. `chainctl` shows a diff and asks you to confirm. After you confirm, Chainguard rebuilds the repo's images with the wrapper as their entrypoint.

To apply a manifest without an editor, put it in a file and use `apply`:

```shell
chainctl images repos build apply -f build.yaml --repo $REPO --yes
```

The `--yes` flag skips the confirmation prompt. To preview the change first, use `--dry-run` in place of `--yes`. The command prints the diff and exits with a non-zero status when it finds a change to apply. In a pipeline, pass `--yes` to apply or `--dry-run` to preview. A structured `--output` format on its own doesn't suppress the confirmation prompt.

`chainctl` checks the manifest before it sends anything to the API. For example, it rejects `preflight` without `guarded_entrypoint`.

For more on `edit` and `apply`, see [Using chainctl to manage Custom Assembly resources](/chainguard/containers/custom-assembly/custom-assembly-chainctl/).

### Check the result

A build normally takes less than 20 minutes. To see the builds, run the following command:

```shell
chainctl images repos build list --repo $REPO
```

When a build fails, the `Reason` column shows why. To read the reason in full, run `chainctl images repos build logs --repo $REPO` and select the failed build. For the reasons that relate to Guarded Entrypoint, see [Entrypoints the wrapper refuses](/chainguard/containers/custom-assembly/guarded-entrypoint/troubleshooting/#entrypoints-the-wrapper-refuses).

To confirm that a rebuilt image uses the wrapper, check its entrypoint. The first element is `/usr/bin/guarded-entrypoint`, followed by the image's original entrypoint:

```shell
crane config cgr.dev/$ORGANIZATION/$REPO:latest | jq '.config.Entrypoint'
```

### Turn off Guarded Entrypoint

To remove the wrapper from the image, edit the manifest and delete `guarded_entrypoint`, `fail_mode`, `preflight`, and `command_override`. The API rejects the other three keys when `guarded_entrypoint` is not set. The next rebuild produces an image with its original entrypoint.

To bypass the wrapper on a running container without a rebuild, see [Troubleshoot a wrapped container](/chainguard/containers/custom-assembly/guarded-entrypoint/troubleshooting/).

## Turn on Guarded Entrypoint with the API

The Chainguard API accepts the same four fields. They are `guardedEntrypoint`, `failMode`, `preflight`, and `commandOverride` on the repo's `customOverlay`. For general guidance on authenticating and calling the API, see [Using the Chainguard API](/platform/api/api-v2-tutorial/).

The API's enum fields take enum names. `failMode` is `FAIL_MODE_CLOSED` or `FAIL_MODE_OPEN`. A `commandOverride` `mode` is `MODE_DEFAULT`, `MODE_PREPEND`, or `MODE_OVERRIDE`. A preflight `onFailure` is `ON_FAILURE_FAIL` or `ON_FAILURE_CONTINUE`.

The following request turns on Guarded Entrypoint for a repo, with a fail-open setting and one preflight check:

```shell
export TOKEN=$(chainctl auth token)
export API=https://console-api.enforce.dev
export REPO_UID=YOUR_REPO_UID

curl -s -X PATCH -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  "$API/registry/v2/repos/$REPO_UID" \
  -d '{
    "customOverlay": {
      "guardedEntrypoint": true,
      "failMode": "FAIL_MODE_OPEN",
      "preflight": [
        {
          "tcp": "db.internal:5432",
          "timeout": "60s",
          "interval": "1s",
          "onFailure": "ON_FAILURE_FAIL"
        }
      ],
      "environment": {
        "CONSUL_HTTP_ADDR": "https://consul.example.com:8501",
        "FEATURE_FLAGS_URL": "cg+consul://apps/web/feature-flags-url"
      }
    }
  }'
```

Send every customization you want the repo to keep, not only the Guarded Entrypoint fields. The API validates the request with the rules in [API errors](#api-errors).

## Use Guarded Entrypoint with tag-based Custom Assembly

An overlay can carry the same four fields. This lets you apply Guarded Entrypoint to some of a repo's tags, or to many repos at once. See the [overview of tag-based Custom Assembly](/chainguard/containers/custom-assembly/tag-based-custom-assembly/) for overlays, bindings, and tag selectors.

Tag-based Custom Assembly is a separate feature with its own enrollment. To use Guarded Entrypoint on overlays and bindings, your organization needs both features enabled. Contact your Chainguard account team to enable tag-based Custom Assembly. Contact Chainguard customer support to enable Guarded Entrypoint. Setting the fields on a repo with `chainctl images repos build edit`, as described earlier on this page, needs only Guarded Entrypoint.

Write the overlay as a YAML file in the same shape as a repo manifest, create the overlay from it, and bind it to tags:

```shell
cat > startup.yaml <<EOF
guarded_entrypoint: true
fail_mode: closed
preflight:
  - tcp: db.internal:5432
    timeout: 60s
    interval: 1s
EOF

chainctl images overlays create startup --parent $ORGANIZATION -f startup.yaml

chainctl images overlays attach \
  --overlay startup \
  --repo $REPO \
  --parent $ORGANIZATION \
  --all
```

For the other selectors, see [Managing tag-based Custom Assembly with chainctl](/chainguard/containers/custom-assembly/tag-based-custom-assembly/chainctl/).

Through the API, create the overlay with `POST /registry/v2beta1/overlays/$ORG_ID` and bind it with `POST /registry/v2beta1/overlayBindings/$REPO_UID`. The overlay's `config` takes the same fields as the repo's `customOverlay`:

```shell
export ORG_ID=YOUR_ORG_ID

curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  "$API/registry/v2beta1/overlays/$ORG_ID" \
  -d '{
    "name": "startup",
    "config": {
      "guardedEntrypoint": true,
      "failMode": "FAIL_MODE_CLOSED",
      "preflight": [
        { "tcp": "db.internal:5432", "timeout": "60s", "interval": "1s" }
      ]
    }
  }'

curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  "$API/registry/v2beta1/overlayBindings/$REPO_UID" \
  -d '{
    "overlay": "startup",
    "tagSelector": { "kind": "KIND_ALL" }
  }'
```

### How the fields combine across bindings

A tag can match several bindings. Chainguard layers them from the broadest selector to the most specific: all, then variant, then exact. Each of the four fields combines in its own way:

| Field | When several bindings match one tag |
| --- | --- |
| `guarded_entrypoint` | The wrapper is on if any matching binding sets it to `true`. A more specific binding can't turn it off. |
| `fail_mode` | The most specific binding that sets it wins. A binding that leaves it unset uses the value from a broader binding. |
| `command_override` | The most specific binding that sets it wins. A binding that leaves it unset uses the value from a broader binding. |
| `preflight` | The checks accumulate. Checks from broader bindings run first, and identical entries are dropped. |

Each overlay that sets `fail_mode`, `command_override`, or `preflight` must also set `guarded_entrypoint: true` itself, even when a broader binding already sets it.

The limit of 32 preflight entries applies to each overlay. The combined list for a tag can be longer.

Any organization can set `fail_mode: open`.

#### Pin a tag to fail closed

A broader binding can set `fail_mode: open`, and a tag inherits that value. To keep one tag fail-closed, bind an overlay to that tag with a more specific selector, and set `fail_mode: closed` in it.

For example, an all binding uses an overlay that sets fail-open:

```yaml
guarded_entrypoint: true
fail_mode: open
```

An exact binding on the `3.13` tag uses an overlay that sets fail-closed:

```yaml
guarded_entrypoint: true
fail_mode: closed
```

The `3.13` tag is fail-closed. Every other tag is fail-open. If the open value comes from the tag's own exact binding, change that binding's overlay instead.

#### Cancel a broader command override

An empty `command` with `command_override` set means "default mode, no command". It counts as set, so it cancels the override from a broader binding. To drop the override on one tag, bind an overlay like the following to that tag with a more specific selector:

```yaml
guarded_entrypoint: true
command_override:
  mode: default
```

#### Bindings of the same kind

Two bindings of the same kind can match the same tag. Chainguard rejects the second binding when it is created if the two overlays set `fail_mode` or `command_override` to different values. Identical values merge. An update to an overlay gets the same check against every repo the overlay is bound to.

The failed request returns the error described in [API errors](#api-errors). To fix it, make the two overlays agree, or bind them to selectors that don't match the same tags.

## API errors

The API validates the Guarded Entrypoint fields the same way for repos and for overlays. In the messages, `<prefix>` is `custom_overlay` when you set the fields on a repo, and `config` when you set them on an overlay. On the overlay path, the API adds the text `Invalid argument: config:` and a space to the start of each `InvalidArgument` message. In a message, `[i]` is the index of the entry in the list, starting at 0.

| Trigger | Code | Message |
| --- | --- | --- |
| `guarded_entrypoint: true` on an organization that doesn't have Guarded Entrypoint enabled. Contact Chainguard customer support to get access. | `PermissionDenied` | `using <prefix>.guarded_entrypoint is not allowed` |
| `preflight` set without `guarded_entrypoint` | `InvalidArgument` | `<prefix>.preflight requires guarded_entrypoint` |
| `command_override` set without `guarded_entrypoint` | `InvalidArgument` | `<prefix>.command_override requires guarded_entrypoint` |
| `fail_mode` set without `guarded_entrypoint` | `InvalidArgument` | `<prefix>.fail_mode requires guarded_entrypoint` |
| More than 32 preflight entries | `InvalidArgument` | `<prefix>.preflight: at most 32 entries` |
| Preflight entry with neither or both of `tcp` and `path` | `InvalidArgument` | `<prefix>.preflight[i]: rpc error: code = InvalidArgument desc = exactly one of tcp or path is required` |
| Preflight `timeout` or `interval` is not a Go duration | `InvalidArgument` | `<prefix>.preflight[i]: rpc error: code = InvalidArgument desc = timeout "abc": time: invalid duration "abc"` |
| Preflight `timeout` or `interval` is negative | `InvalidArgument` | `<prefix>.preflight[i]: rpc error: code = InvalidArgument desc = timeout "-5s" must be non-negative` |
| Preflight `on_failure` is not `fail` or `continue` | `InvalidArgument` | `<prefix>.preflight[i]: rpc error: code = InvalidArgument desc = on_failure "ignore" must be "fail" or "continue"` |
| Preflight value contains `,` or `=` | `InvalidArgument` | `<prefix>.preflight[i]: rpc error: code = InvalidArgument desc = tcp "a:1,b:2" must not contain ',' or '='` (the message names the field that holds the character) |
| `command_override.mode` is not `default`, `prepend`, or `override` | `InvalidArgument` | `<prefix>.command_override: rpc error: code = InvalidArgument desc = mode "silent" must be "default", "prepend", or "override"` |
| `prepend` or `override` with an empty `command` | `InvalidArgument` | `<prefix>.command_override: rpc error: code = InvalidArgument desc = mode "prepend" requires a non-empty command` |
| `command` entry contains a NUL byte | `InvalidArgument` | `<prefix>.command_override: rpc error: code = InvalidArgument desc = command[i] contains a NUL byte` |
| `command` entry has a `${` with no closing `}` | `InvalidArgument` | `<prefix>.command_override: rpc error: code = InvalidArgument desc = command[i] has an unterminated ${ reference` |
| `command` entry has a `${...}` reference with an invalid variable name | `InvalidArgument` | `<prefix>.command_override: rpc error: code = InvalidArgument desc = command[i] has an invalid variable name in a ${...} reference` |
| `fail_mode` is not `closed` or `open` | `InvalidArgument` | `<prefix>.fail_mode must be one of "closed" or "open", got "maybe"` |
| `environment` key starts with `GUARDED_` | `InvalidArgument` | `environment variable "GUARDED_DISABLE" uses reserved prefix 'GUARDED_'` |
| `environment` key starts with `CHAINGUARD_` | `InvalidArgument` | `environment variable "CHAINGUARD_X" uses reserved prefix 'CHAINGUARD_'` |
| Version 1 repo API: `sync_config.apko_overlay.environment` key starts with `GUARDED_` | `InvalidArgument` | `sync_config.apko_overlay.environment: variable "..." uses reserved prefix 'GUARDED_'` |
| Overlay path: organization is not enrolled in tag-based Custom Assembly | `FailedPrecondition` | `Precondition failed: this organization is not enrolled in tag-based Custom Assembly. Contact your Chainguard account team to enroll.` |
| Overlay path: `config` sets a field that overlays don't support | `InvalidArgument` | `config may set only contents.packages, contents.runtime_repositories, contents.runtime_keyring, environment, annotations, accounts, certificates.additional, guarded_entrypoint, command_override, preflight, and fail_mode` |
| Overlay path: `config` sets nothing | `InvalidArgument` | `config must set at least one customization field` |
| Binding path: two bindings of one kind that match the same tag set different `fail_mode` or `command_override` values | `FailedPrecondition` | `overlay config does not merge commutatively with co-matching binding(s): binding "..." (overlay "...", selector ALL) on fields [fail_mode]` |

On the binding path, the error response also carries the violation type `OVERLAY_BINDING_CONFLICT`. The message names the binding and the fields that conflict. A `command_override` conflict lists `command_override` in the fields.

The `custom_overlay` and `config` prefixes show up in the message text only. In JSON requests, the fields are `customOverlay` and `config`.

## Learn more

* [How Guarded Entrypoint works](/chainguard/containers/custom-assembly/guarded-entrypoint/how-it-works/)
* [Guarded Entrypoint examples](/chainguard/containers/custom-assembly/guarded-entrypoint/examples/)
* [Troubleshoot a wrapped container](/chainguard/containers/custom-assembly/guarded-entrypoint/troubleshooting/)
* [Guarded Entrypoint trust boundary](/chainguard/containers/custom-assembly/guarded-entrypoint/trust-boundary/)
* [Overview of Chainguard Custom Assembly](/chainguard/containers/custom-assembly/overview/)
