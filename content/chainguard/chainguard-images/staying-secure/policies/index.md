---
aliases:
- /chainguard/administration/policies/
title: "Container Pull Policies"
linktitle: "Container Pull Policies"
type: "article"
description: "Configure and enforce policies that control which Chainguard container and artifact versions your organization can pull, using chainctl or the Chainguard Console"
date: 2026-05-21T08:48:45+00:00
lastmod: 2026-05-21T08:48:45+00:00
draft: false
tags: ["Overview"]
images: []
toc: true
weight: 025
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

## Available policies

Chainguard ships a set of system policies that are available to every organization. The list below describes each one and its configurable parameters. To confirm which policies are available to you and see their full definitions, use `chainctl policies list` and `chainctl policies describe` as shown under [Usage](#usage).

### no-eol

The `no-eol` policy denies any image whose primary package has reached its end-of-life (EOL) date. An image is allowed when it has no recorded EOL date, or when that date is still in the future. This policy takes no parameters.

```shell
chainctl policies enable --policy=no-eol --mode=DRY_RUN --parent=$ORGANIZATION
```

### cooldown

The `cooldown` policy denies images that are newer than a minimum age, measured from the image's build timestamp. Use it to hold off on adopting a version until it has been published long enough to shake out early regressions. An image is allowed once its age is greater than or equal to the configured number of days.

It accepts one parameter, `days`, an integer number of days an image must exist before it is allowed. The default is `7`, and accepted values range from `1` to `365`.

```shell
chainctl policies enable --policy=cooldown --mode=DRY_RUN --param=days=14 --parent=$ORGANIZATION
```

### support-window

The `support-window` policy requires an image's primary package to have a minimum remaining support period, measured as the span between the package's release date and its EOL date. An image is allowed when that span is greater than or equal to the configured number of months, or when the package has no recorded EOL date.

It accepts one parameter, `months`, an integer minimum number of months of support. The default is `6`, and accepted values range from `1` to `24`.

```shell
chainctl policies enable --policy=support-window --mode=DRY_RUN --param=months=12 --parent=$ORGANIZATION
```

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

Disable a policy:

```shell
chainctl policies disable --policy=no-eol --parent=$ORGANIZATION
```

## Checking whether an image is allowed

Before you depend on a specific image (pinning it in a deployment, promoting it through an environment, or adding it to a base image), you often want to know whether your active policies will let it through. `chainctl policies check` answers that for one image on demand, without waiting for a pull to happen.

Pass a full image reference, by tag or by digest:

```shell
chainctl policies check cgr.dev/$ORGANIZATION/python:latest
```

The reference identifies the organization and repository; a tag is resolved to its current digest, and a digest is used as-is. The image is then evaluated against every policy active for that organization, and each result is printed:

```output
  POLICY  |  MODE   | PARAMETERS | RESULT
----------|---------|------------|---------
 cooldown | DRY_RUN | days=7     | DENIED
 no-eol   | ENFORCE |            | ALLOWED
```

Read the table per policy. The image is blocked at pull time only when a policy in `ENFORCE` mode returns `DENIED`. A `DENIED` from a `DRY_RUN` policy is reported here but would not block a real pull; it is a preview of what enforcing that policy would do. If no policies apply to the image, the command says so rather than printing a table.

Because the check evaluates against the policies you have enabled right now, it reflects your current configuration, not a historical record. To review outcomes from pulls that already happened, use [policy decisions](#policy-decisions) instead.

`check` is also built for automation. Its exit status is non-zero whenever any policy returns `DENIED` or `ERROR`, regardless of that policy's mode, so you can gate a CI pipeline on it:

```shell
chainctl policies check cgr.dev/$ORGANIZATION/python@sha256:abc... || echo "image violates a policy"
```

Note that a `DRY_RUN` denial also produces a non-zero exit, so a passing `check` is stricter than what enforcement alone would block, which is useful as an early warning while you stage policies.

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

## Granting an exception with an override

Once a policy is enforcing, it blocks every image that violates it. Sometimes you need to let one specific image through anyway: a known-good build that trips a policy, an artifact approved through a separate review, or an urgent fix that cannot wait for the policy itself to change. An override is an admin-granted waiver that flips a `DENIED` result to `ALLOWED` for one policy and one image, without disabling the policy or changing its binding. Every other image stays subject to the policy.

An override is deliberate and attributable. It applies to exactly one policy and one image digest, requires a reason, and records who created it and when. The engine applies it after evaluation, so the recorded decision still reflects the policy's verdict while the override is what ultimately allows the pull.

Creating an override requires the `policies.override.create` capability, which is typically held by organization owners.

Waive a policy for a specific image, identified by digest, with a reason:

```shell
chainctl policies override create \
  --policy=no-eol \
  --digest=sha256:abc123... \
  --reason="approved exception, ticket OPS-42" \
  --parent=$ORGANIZATION
```

The `--digest` value must be a manifest digest rather than a tag, so the waiver targets one exact artifact. A given policy and image can carry at most one override; to change an existing one, delete it and create it again.

Review the active overrides for an organization to see what has been waived, by whom, and why:

```shell
chainctl policies override list --parent=$ORGANIZATION
```

```output
 OVERRIDE ID  | POLICY |       TARGET        |           REASON           |    CREATED BY     |       CREATED AT
--------------|--------|---------------------|----------------------------|-------------------|-------------------------
 <id>         | no-eol | image sha256:abc12… | approved exception, OPS-42 | alice@example.com | 2026-06-28 14:30:00 UTC
```

When the exception is no longer needed, delete the override to restore the policy's result for that image. Use `chainctl policies override list` to find the ID:

```shell
chainctl policies override delete <override-id>
```

Once deleted, the image is again subject to whatever the policy decides.

## Known issues

Policies are in open beta, and we are continuously working to improve the experience. The items below are current limitations you may run into when working with overrides, along with the workaround for each.

### An override is not effective immediately

After you create an override, it does not take effect right away. The platform caches policy decisions, and it takes a short while for that cache to refresh before the override is applied. If a pull is still blocked immediately after you create an override, wait a moment and try again.

### A single image can require two overrides

Pulling an image with a client such as Docker involves two separate requests: a manifest pull followed by an image pull. Both requests are now evaluated against your policies, and they resolve to different digests, so a single `docker pull` can produce two `DENIED` decisions. An override targets one digest, so waiving only the first digest still leaves the second one blocked.

To work around this, create an override for each denied digest. First attempt the pull so both decisions are recorded, then use [policy decisions](#policy-decisions) to find the digests that were blocked:

```shell
chainctl policies decision list --parent=$ORGANIZATION --result=DENIED
```

```output
 REPOSITORY |     DIGEST     |  POLICY  |   MODE   | RESULT | PULLED ON
------------|----------------|----------|----------|--------|------------
 curl       | sha256:609aeb… | cooldown | ENFORCED | DENIED | 2026-07-02
 curl       | sha256:db532b… | cooldown | ENFORCED | DENIED | 2026-07-02
```

Create an override for each of the denied digests:

```shell
chainctl policies override create \
  --policy=cooldown \
  --digest=sha256:609aeb... \
  --reason="approved exception, ticket OPS-42" \
  --parent=$ORGANIZATION

chainctl policies override create \
  --policy=cooldown \
  --digest=sha256:db532b... \
  --reason="approved exception, ticket OPS-42" \
  --parent=$ORGANIZATION
```

With both digests waived, the pull is allowed. Remember that the override is subject to the cache refresh described above, so allow a short delay before retrying the pull.

See `chainctl policies --help` or the [chainctl reference pages](/chainguard/chainctl) for more information.
