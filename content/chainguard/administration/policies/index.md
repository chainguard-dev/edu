---
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

## Policy decisions

Every time an image is pulled and evaluated against an active policy, the platform records the outcome as a *decision*. A decision is the result of evaluating a single image digest against a single policy at pull time. It captures the policy, the digest, the mode the policy ran under (`ENFORCE` or `DRY_RUN`), the outcome (`ALLOWED`, `DENIED`, or `ERROR`), a reason when one is available, and the day the pull happened.

Decisions are recorded for all evaluations, regardless of mode or outcome. Together they form an audit log of what your policies did against real pull traffic. Use them to answer questions like "why was this image blocked?", "what has this policy decided over the past month?", and "what would this policy block if I enforced it?".

This is distinct from `chainctl policies check`, which evaluates one image against your active policies on demand. Decisions are the historical record of evaluations that already happened during real pulls.

List the decisions recorded for your organization:

```shell
chainctl policies decision list --parent=$ORGANIZATION
```

```output
 REPOSITORY |     DIGEST     |  POLICY  |   MODE   | RESULT  | PULLED ON
------------|----------------|----------|----------|---------|------------
 nginx      | sha256:1a2b3c… | cooldown | DRY_RUN  | DENIED  | 2026-06-28
 nginx      | sha256:4d5e6f… | no-eol   | ENFORCED | DENIED  | 2026-06-28
 bash       | sha256:7a8b9c… | no-eol   | ENFORCED | ALLOWED | 2026-06-27
```

Narrow the results with filters. To see only the pulls a policy denied, filter by outcome:

```shell
chainctl policies decision list --parent=$ORGANIZATION --result=DENIED
```

You can also restrict to a single policy, a single mode (`ENFORCE` or `DRY_RUN`), a time window, or a single image, and request JSON for further processing. The `--since` flag takes a number of days with a `d` suffix (for example `7d`), and `--repo` accepts an image as `REPO` or `REPO:TAG`:

```shell
chainctl policies decision list --parent=$ORGANIZATION --policy=no-eol --mode=ENFORCE --since=30d -o json
chainctl policies decision list --parent=$ORGANIZATION --repo=nginx:latest
```

Decisions are deduplicated per day, so repeated pulls of the same digest under the same policy and outcome appear once for that day rather than once per pull.

## Example: staging a policy with dry run

`DRY_RUN` decisions let you measure a policy's impact before it can block anything. Because a `DRY_RUN` binding records outcomes without blocking pulls, you can enable a policy, watch what it would have denied against your real traffic, and only promote it to `ENFORCE` once the results match your expectations.

First, enable the policy in `DRY_RUN` mode:

```shell
chainctl policies enable --policy=no-eol --mode=DRY_RUN --parent=$ORGANIZATION
```

Let your normal pull traffic flow for a representative period. Then review what the policy denied while in dry run. Use `--since` to limit the review to a recent window, here the last seven days:

```shell
chainctl policies decision list --parent=$ORGANIZATION --policy=no-eol --mode=DRY_RUN --result=DENIED --since=7d
```

Each `DENIED` row is a pull that would have been blocked under `ENFORCE`. Inspect the digests to confirm the policy is catching what you intend and nothing critical to your workloads. If the results look wrong, adjust the policy's parameters or disable it; if they look right, promote the binding to enforcement:

```shell
chainctl policies enable --policy=no-eol --mode=ENFORCE --parent=$ORGANIZATION
```

After promoting, keep reviewing decisions to confirm enforcement behaves as expected. The same command now returns `ENFORCE`-mode rows for the pulls the policy is actively blocking.

See `chainctl policies --help` or the [chainctl reference pages](/chainguard/chainctl) for more information.