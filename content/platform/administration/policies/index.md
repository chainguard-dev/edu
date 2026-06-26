---
aliases:
- /chainguard/administration/policies/
title: "Policies"
linktitle: "Policies"
type: "article"
description: "Configure and enforce policies that control which Chainguard image and artifact versions your organization can pull, using chainctl or the Chainguard Console"
date: 2026-05-21T08:48:45+00:00
lastmod: 2026-05-21T08:48:45+00:00
draft: false
tags: ["Overview"]
images: []
menu:
  docs:
    parent: "administration"
toc: true
weight: 008
---

Policies enable you to filter and restrict Chainguard artifact updates. You do this by defining policies that control and restrict versions that will be pulled from Chainguard.

{{< beta feature="Policies" enroll="true" >}}

## Definitions

This is how policies uses the following terms.

- **Policy** — A reusable rule that determines whether an image is allowed. Each policy has a name, a description, and the resource types it applies to. Policies apply to registry repositories.
- **Binding** — A link between a policy and an organization. While a binding exists, the policy is active for image pulls under that organization. Without a binding, the policy has no effect.
- **Mode** — A binding's mode controls what happens when the policy denies an image:
  - `ENFORCE` — Block the pull.
  - `DRY_RUN` — Allow the pull but record the violation.

The default mode for new bindings is `DRY_RUN`.

## Usage

Policies are managed using `chainctl`. System policies are shipped with the platform.

See which policies are available to your organization:

```shell
chainctl policies list --parent=$ORGANIZATION
```

Inspect a policy to see its full definition and configurable parameters before enabling it:

```shell
chainctl policies describe --policy=$POLICY --parent=$ORGANIZATION
```

See which policies are currently active:

```shell
chainctl policies binding list --parent=$ORGANIZATION
```

Activate a policy in `DRY_RUN` mode. This example activates the "no end-of-life" artifacts policy. Chainguard recommends that you roll out policies using `DRY_RUN` mode first and track for a time to be certain it has the impact you intend before moving to `ENFORCE`.

```shell
chainctl policies enable --policy=no-eol --mode=DRY_RUN --parent=$ORGANIZATION
```

Some policies accept parameters. Use `--param=KEY=VALUE` to supply them:

```shell
chainctl policies enable --policy=cooldown --mode=DRY_RUN --param=days=7 --parent=$ORGANIZATION
```

Promote a policy to `ENFORCE`:

```shell
chainctl policies enable --policy=no-eol --mode=ENFORCE --parent=$ORGANIZATION
```

Check the results of specific policies on an image, including `DRY_RUN` policies which wouldn't cause the registry to block a pull:

```shell
chainctl policies check cgr.dev/$ORGANIZATION/bash:latest
```

```output
  POLICY  |  MODE   | RESULT
----------|---------|---------
 cooldown | DRY_RUN | DENIED
 no-eol   | DRY_RUN | ALLOWED
```

Disable a policy:

```shell
chainctl policies disable --policy=no-eol --parent=$ORGANIZATION
```

See `chainctl policies --help` or the [chainctl reference pages](/chainguard/chainctl) for more information.