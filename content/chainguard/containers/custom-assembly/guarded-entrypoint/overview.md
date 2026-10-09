---
title: "Guarded Entrypoint for Custom Assembly"
linktitle: "Guarded Entrypoint overview"
type: "article"
description: "How Guarded Entrypoint lets a Custom Assembly image resolve secrets, run preflight checks, and override its command at container start, and how to turn it on."
date: 2026-10-06T17:41:00+00:00
lastmod: 2026-10-09T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Custom Assembly", "Configuration", "Procedural"]
images: []
menu:
  docs:
    parent: "guarded-entrypoint"
weight: 5
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

* A Custom Assembly repo. Refer to the [Custom Assembly overview](/chainguard/containers/custom-assembly/overview/) to create one.
* A role that lets you edit Custom Assembly repos. Refer to the [Custom Assembly permissions requirements](/chainguard/containers/custom-assembly/overview/#custom-assembly-permissions-requirements).
* The latest [`chainctl`](/platform/chainctl-usage/how-to-install-chainctl/). Run `chainctl update` to update it. An older `chainctl` drops the Guarded Entrypoint keys when it reads a repo, so a teammate who edits the repo with an older version can turn the feature off without noticing. Update every copy of `chainctl` that edits the repo.
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

Secret references go in the existing `environment` key. For details on each key, refer to [How Guarded Entrypoint works](/chainguard/containers/custom-assembly/guarded-entrypoint/how-it-works/).

To turn it on interactively, open the repo's manifest in your editor:

```shell
chainctl images repos build edit --repo $REPO --parent $ORGANIZATION
```

Add the keys you need. The following manifest turns on Guarded Entrypoint and resolves one secret from Vault:

```yaml
guarded_entrypoint: true
environment:
  VAULT_ADDR: https://vault.example.com:8200
  VAULT_K8S_ROLE: orders-service
  DB_PASSWORD: cg+vault://secret/data/orders#db_password
```

Keep the keys that are already in the manifest. Applying a manifest replaces the repo's stored configuration, so removing a key from the manifest removes it from the repo.

Save and close the editor. `chainctl` shows a diff and asks you to confirm. After you confirm, Chainguard rebuilds the repo's images with the wrapper as their entrypoint.

To apply a manifest without an editor, put it in a file and use `apply`:

```shell
chainctl images repos build apply -f build.yaml --repo $REPO --parent $ORGANIZATION --yes
```

The `--yes` flag skips the confirmation prompt. To preview the change first, use `--dry-run` in place of `--yes`. The command prints the diff and exits with a non-zero status when it finds a change to apply. In a pipeline, pass `--yes` to apply or `--dry-run` to preview, and pass `--parent` so `chainctl` doesn't prompt you to choose a group. A structured `--output` format on its own doesn't suppress the confirmation prompt.

`chainctl` checks the manifest before it sends anything to the API. For example, it rejects `preflight` without `guarded_entrypoint`.

For more on `edit` and `apply`, refer to [Using chainctl to manage Custom Assembly resources](/chainguard/containers/custom-assembly/custom-assembly-chainctl/).

### Check the result

To list the builds, run the following command:

```shell
chainctl images repos build list --repo $REPO --parent $ORGANIZATION
```

When Chainguard refuses to wrap an image, or when two bindings conflict, Chainguard records the build as a failure and the `Reason` column shows why. The column is empty for an ordinary build failure. To read a reason in full, run `chainctl images repos build logs --repo $REPO --parent $ORGANIZATION` and select the failed build. For the reasons that relate to Guarded Entrypoint, refer to [Entrypoints the wrapper refuses](/chainguard/containers/custom-assembly/guarded-entrypoint/troubleshooting/#entrypoints-the-wrapper-refuses).

To confirm that a rebuilt image uses the wrapper, check its entrypoint. The first element is `/usr/bin/guarded-entrypoint`. What follows depends on the image. For an image with a command, it is that command. For a shell fragment, it is `/bin/sh -c` and the fragment. For a service bundle, it is `/bin/s6-svscan /sv`. An image that has only a CMD has the wrapper alone:

```shell
crane config cgr.dev/$ORGANIZATION/$REPO:latest | jq '.config.Entrypoint'
```

### Turn off Guarded Entrypoint

To remove the wrapper from the image, edit the manifest and delete `guarded_entrypoint`, `fail_mode`, `preflight`, and `command_override`. The API rejects the other three keys when `guarded_entrypoint` is not set. Also remove any `cg+...` values from `environment`. Without the wrapper, they ship as literal strings. The next rebuild produces an image with its original entrypoint.

To bypass the wrapper on a running container without a rebuild, refer to [Troubleshoot a wrapped container](/chainguard/containers/custom-assembly/guarded-entrypoint/troubleshooting/).

## Turn on Guarded Entrypoint with the API

The Chainguard API accepts the same four fields. They are `guardedEntrypoint`, `failMode`, `preflight`, and `commandOverride` on the repo's `customOverlay`. For general guidance on authenticating and calling the API, refer to [Using the Chainguard API](/platform/api/api-v2-tutorial/).

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

The request merges into the repo's stored overlay. The API builds an update mask from the fields in the request body, so only the fields you send change:

* A field you leave out keeps its stored value. You can't turn Guarded Entrypoint off by leaving its fields out.
* The request replaces `environment` and `preflight` as a whole. The example request sets the repo's environment variables to the two it lists and removes the others, so include every variable you want to keep.

To replace the whole overlay with exactly what you send, add `?update_mask=custom_overlay` to the URL. Use this form to turn Guarded Entrypoint off, with a body that leaves out the four fields.

The API validates the request with the rules in [API errors](#api-errors).

## Use Guarded Entrypoint with Custom Assembly Overlays

An overlay can carry the same four fields. This lets you apply Guarded Entrypoint to some of a repo's tags, or to many repos at once. Refer to the [overview of Custom Assembly Overlays](/chainguard/containers/custom-assembly/overlays/overview/) for overlays, bindings, and tag selectors.

Guarded Entrypoint has its own enrollment, separate from Custom Assembly Overlays. Contact Chainguard customer support to enable Guarded Entrypoint. Setting the fields on a repo with `chainctl images repos build edit`, as described earlier on this page, needs only Guarded Entrypoint.

A repo uses its own configuration or overlay bindings, not both. The overlay examples that follow use a different repo from the one you configured with `build edit`. Attaching an overlay to a repo that has its own configuration fails with the error `repository custom overlay and overlay binding not allowed`. Setting a configuration on a repo that has bindings fails the same way.

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

export TAG_REPO=my-tagged-python

chainctl images overlays attach \
  --overlay startup \
  --repo $TAG_REPO \
  --parent $ORGANIZATION \
  --all
```

For the other selectors, refer to [Managing Custom Assembly Overlays with chainctl](/chainguard/containers/custom-assembly/overlays/chainctl/).

Through the API, create the overlay with `POST /registry/v2beta1/overlays/$ORG_ID` and bind it with `POST /registry/v2beta1/overlayBindings/$TAG_REPO_UID`, where `$TAG_REPO_UID` is the UID of a repo that has no configuration of its own. The overlay's `config` takes the same fields as the repo's `customOverlay`:

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
  "$API/registry/v2beta1/overlayBindings/$TAG_REPO_UID" \
  -d '{
    "overlay": "startup",
    "tagSelector": { "kind": "KIND_ALL" }
  }'
```

### How the fields combine across bindings

A tag can match several bindings. Chainguard layers them from the broadest to the most specific. Bindings that apply to every repo in your organization (all-repos bindings) come first, in the order all, variant, exact. The repo's own bindings come next, in the same order. A repo's own binding always wins over an all-repos binding. Each of the four fields combines in its own way:

| Field | When several bindings match one tag |
| --- | --- |
| `guarded_entrypoint` | The wrapper is on if any matching binding sets it to `true`. A more specific binding can't turn it off. |
| `fail_mode` | The most specific binding that sets it wins. A binding that leaves it unset uses the value from a broader binding. |
| `command_override` | The most specific binding that sets it wins. A binding that leaves it unset uses the value from a broader binding. |
| `preflight` | The checks accumulate. Checks from broader bindings run first, and identical entries are dropped. |

Each overlay that sets `fail_mode`, `command_override`, or `preflight` must also set `guarded_entrypoint: true` itself, even when a broader binding already sets it.

The limit of 32 preflight entries applies to each overlay. The combined list for a tag can be longer.

Any organization that has Guarded Entrypoint enabled can set `fail_mode: open`. It needs no separate approval.

#### Pin a tag to fail closed

A broader binding can set `fail_mode: open`, and a tag inherits that value. To keep one tag fail-closed, bind an overlay to that tag on the repo itself with a more specific selector, and set `fail_mode: closed` in it. An all-repos binding can't override a repo's own binding.

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

Two bindings of the same kind can match the same tag. Chainguard rejects the second binding when it is created if the two overlays set `fail_mode` or `command_override` to different values. Identical values merge.

The same check runs when you update an overlay, against every repo the overlay is bound to, and when you update a binding's selector. The error for an overlay update differs from the error for a new binding. Refer to [API errors](#api-errors). To fix a conflict, make the two overlays agree, or bind them to selectors that don't match the same tags.

## API errors

The API validates the Guarded Entrypoint fields the same way for repos and for overlays. In the messages, `<prefix>` is `custom_overlay` when you set the fields on a repo, and `config` when you set them on an overlay. On the overlay path, the API adds the text `Invalid argument: config:` and a space to the start of each `InvalidArgument` message. For `FailedPrecondition` errors on either path, the API adds `Precondition failed:` and a space, except where the table shows the message without it. In a message, `[i]` is the index of the entry in the list, starting at 0.

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
| Preflight value contains `,` or `=` | `InvalidArgument` | `<prefix>.preflight[i]: rpc error: code = InvalidArgument desc = tcp "a:1,b:2" must not contain ',' or '='` (the message names the field that holds the character) |
| `command_override.mode` is a number that isn't a declared mode | `InvalidArgument` | `<prefix>.command_override: rpc error: code = InvalidArgument desc = mode "99" must be "default", "prepend", or "override"` |
| `prepend` or `override` with an empty `command` | `InvalidArgument` | `<prefix>.command_override: rpc error: code = InvalidArgument desc = mode "prepend" requires a non-empty command` |
| `command` entry contains a NUL byte | `InvalidArgument` | `<prefix>.command_override: rpc error: code = InvalidArgument desc = command[i] contains a NUL byte` |
| `command` entry has a `${` with no closing `}` | `InvalidArgument` | `<prefix>.command_override: rpc error: code = InvalidArgument desc = command[i] has an unterminated ${ reference` |
| `command` entry has a `${...}` reference with an invalid variable name | `InvalidArgument` | `<prefix>.command_override: rpc error: code = InvalidArgument desc = command[i] has an invalid variable name in a ${...} reference` |
| `fail_mode` is a number that isn't a declared mode | `InvalidArgument` | `<prefix>.fail_mode must be one of "closed" or "open", got "99"` |
| `environment` key starts with `GUARDED_` | `InvalidArgument` | `environment variable "GUARDED_DISABLE" uses reserved prefix 'GUARDED_'` |
| `environment` key starts with `CHAINGUARD_` | `InvalidArgument` | `environment variable "CHAINGUARD_X" uses reserved prefix 'CHAINGUARD_'` |
| Version 1 repo API: `sync_config.apko_overlay.environment` key starts with `GUARDED_` | `InvalidArgument` | `sync_config.apko_overlay.environment: variable "..." uses reserved prefix 'GUARDED_'` |
| Overlay or binding path: organization is not enrolled in Custom Assembly Overlays | `FailedPrecondition` | `Precondition failed: this organization is not enrolled in Custom Assembly Overlays. Contact your Chainguard account team to enroll.` |
| Overlay or binding path: the repo has its own configuration, or a repo with bindings gets one | `FailedPrecondition` | `repository custom overlay and overlay binding not allowed` |
| Overlay path: `config` sets a field that overlays don't support | `InvalidArgument` | `config may set only contents.packages, contents.runtime_repositories, contents.runtime_keyring, environment, annotations, accounts, certificates.additional, guarded_entrypoint, command_override, preflight, and fail_mode` |
| Overlay path: `config` sets nothing | `InvalidArgument` | `config must set at least one customization field` |
| Binding path: two bindings of one kind that match the same tag set different `fail_mode` or `command_override` values | `FailedPrecondition` | `Precondition failed: overlay config does not merge commutatively with co-matching binding(s): binding "..." (overlay "...", selector ALL) on fields [fail_mode]` |
| Overlay update: the new config conflicts with a co-matching binding on a repo the overlay is bound to | `FailedPrecondition` | `Precondition failed: overlay config update does not merge commutatively with co-bound overlay(s): binding "..." and binding "..." (overlay "...") on repo "..." conflict on fields [fail_mode]`, or `Precondition failed: overlay config update conflicts with the overlay of a co-matching binding outside your visible scope or beyond the inspected repos` |

The binding and overlay conflict errors also carry the violation type `OVERLAY_BINDING_CONFLICT`. The message names the bindings and the fields that conflict. A `command_override` conflict lists `command_override` in the fields.

The enum fields take enum names in JSON. A request with an enum name that doesn't exist fails when the API parses it, before the checks in the table run. A preflight `onFailure` value that isn't declared is treated as `fail`.

The `custom_overlay` and `config` prefixes show up in the message text only. In JSON requests, the fields are `customOverlay` and `config`.

## Learn more

* [How Guarded Entrypoint works](/chainguard/containers/custom-assembly/guarded-entrypoint/how-it-works/)
* [Guarded Entrypoint examples](/chainguard/containers/custom-assembly/guarded-entrypoint/examples/)
* [Troubleshoot a wrapped container](/chainguard/containers/custom-assembly/guarded-entrypoint/troubleshooting/)
* [Guarded Entrypoint trust boundary](/chainguard/containers/custom-assembly/guarded-entrypoint/trust-boundary/)
* [Overview of Chainguard Custom Assembly](/chainguard/containers/custom-assembly/overview/)
