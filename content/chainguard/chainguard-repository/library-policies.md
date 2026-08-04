---
title: "Chainguard Libraries policies"
linktitle: "Library Policies"
description: "Configure and enforce policies that control which Chainguard Libraries package versions your organization can pull"
type: "article"
date: 2026-07-31T00:00:00+00:00
lastmod: 2026-08-03T18:16:45+00:00
draft: false
tags: ["Chainguard Libraries"]
menu:
  docs:
    parent: "libraries"
    weight: 003
toc: true
---

Chainguard Libraries policies enable you to filter and restrict package versions pulled through Chainguard Repository.

Policies can delay newly published upstream packages, block specific packages or versions, and allow deliberate exceptions to an otherwise denied package. Policies apply to an ecosystem and are evaluated when packages are pulled. Users with the Owner role can create, enable, disable, and list library policies. These policies apply to all packages pulled through Chainguard Repository. The [upstream fallback](/chainguard/libraries/overview/#upstream-fallback-and-controls) must be enabled for an ecosystem in order to use policies.

One custom policy per ecosystem can be enabled at a time. This policy should include all the rules you need, which may include a cooldown period, package block rules, and any overrides.

> **Note**: [Upstream fallback](/chainguard/libraries/overview/#upstream-fallback-and-controls) must be enabled for an ecosystem before you can use library policies. Library policies require `chainctl` v0.2.313 or newer; refer to the [`chainctl` documentation](/get-started/getting-started-with-chainctl/#update-chainctl-to-the-latest-release) for instructions on updating.

## Policy types and definitions

This page uses the following terms:

* **Policy**: A reusable set of rules that determines whether a package or version is allowed.
* **Ecosystem**: The package ecosystem to which a policy applies: Java, JavaScript, or Python.
* **Preview mode**: Records what a policy would block without preventing package installs.
* **Enforce mode**: Blocks packages that violate the policy.

Chainguard Libraries supports the following types of policies:

* **Cooldown**: Delays upstream newly published package versions for a set number of days after the upstream registry publish date.
* **Block**: Deny a package or version outright. Use a block rule when your organization never wants to allow a package or version.
* **Override**: Permit a package or version that would otherwise be denied by a cooldown policy or malware and greyware blocking. Use an override when you need a specific, deliberate exception.
    * An override policy takes precedence over a block policy.

## Identify packages with a purl

Library policies use [package URLs](https://spdx.github.io/spdx-spec/v3.0.1/annexes/pkg-url-specification/), or purls, to identify packages across ecosystems:

* Python: `pkg:pypi/<name>`
    * Example: `pkg:pypi/requests`
* JavaScript: `pkg:npm/<name>` or `pkg:npm/%40<scope>/<name>` for scoped packages
    * Example: `pkg:npm/lodash` or `pkg:npm/%40angular/core`
* Java: `pkg:maven/<group>/<artifact>`
    * Example: `pkg:maven/com.fasterxml.jackson.core/jackson-databind`

Omit the version to match all versions of the package.

Append `@<version>` to target one version. For example:

* `pkg:pypi/requests@2.31.0`
* `pkg:npm/lodash@4.17.20`, `pkg:npm/%40angular/core@17.0.0`
* `pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.15.0`

## Manage policies

### Preview a policy

To understand the impact before enforcing a policy, use `--mode=PREVIEW` with the `chainctl libraries policy enable` command. In preview mode, installs continue to succeed, but Chainguard records *what would have been blocked* over the last 30 days if the policy had been enforced.

In the following example, a policy called `3day-cooldown` has already been created. To preview what would have been blocked if that policy had been enforced, run this command:

```bash
chainctl libraries policy enable 3day-cooldown --ecosystem=JAVASCRIPT --mode=PREVIEW
```

This returns a list of successful installs that would have been blocked by this policy over the last 30 days.

### Enable a policy

After creating a policy, use `--mode=ENFORCE` to enable it for the ecosystem where you want to apply it. For example:

```bash
chainctl libraries policy create --name=disable-cooldown --cooldown-days=0
chainctl libraries policy enable disable-cooldown --ecosystem=JAVASCRIPT --mode=ENFORCE
```

### Describe a policy

To see a policy in detail, use `describe`. For example, to see the details of a policy named `disable-cooldown`:

```bash
chainctl libraries policy describe disable-cooldown
```

This command returns a list of what is included in the policy, such as [blocked packages](#block-a-package-or-version), [packages on your allowlist](#override-a-blocked-package), and the [cooldown policy](#create-and-enable-a-cooldown-policy).

### List policies and verify bindings

To verify which policy is active and its cooldown settings, run the following:

```bash
chainctl libraries policy binding list
```

To list all available policies, including policies that are not active, run the following:

```bash
chainctl libraries policy list
```

Prior to `chainctl` version 0.2.291, cooldown policies were enabled via the `chainctl entitlements command`. Cooldown policies configured prior to this version of `chainctl` are migrated under the new `chainctl libraries policies` system.

## Cooldown policies

The default cooldown period is 7 days. You cannot change the default policy, but you can create and enable a new policy to replace the default.

### Create and enable a cooldown policy

When upstream fallback is enabled, users with the Owner role can create and enable a cooldown policy with `chainctl`. The cooldown period provides an additional layer of defense on top of malware and greyware scanning, giving the broader security community time to surface threats that may not be immediately detectable.

In the following example, a 10-day cooldown policy is created, then it is enforced on the JavaScript ecosystem:

```bash
chainctl libraries policy create --name=js-cooldown --cooldown-days=10
chainctl libraries policy enable js-cooldown --ecosystem=JAVASCRIPT --mode=ENFORCE
```

#### Preview a cooldown policy

To understand the impact before enforcing a policy, use `--mode=PREVIEW`. In preview mode, installs continue to succeed, but Chainguard records what *would have been blocked* if the policy were enforced.

### Disable cooldown

To disable the cooldown, set it to 0. In the example below, the policy is created, then it is enforced on the Java ecosystem:

```bash
chainctl libraries policy create --name=no-cooldown --cooldown-days=0
chainctl libraries policy enable no-cooldown --ecosystem=JAVA --mode=ENFORCE
```

## Block policies

### Block a package or version

Create a custom policy with one or more `--block` entries to deny packages explicitly. Block rules are helpful if your organization has deliberately decided not to allow certain packages. To understand the impact before enforcing a block, [use `--mode=PREVIEW`](#preview-a-policy).

For example, if your organization standardizes on React and wants to prevent teams from pulling in Angular, you can add a `--block` entry for each Angular package you want to deny. In the following example, a policy called `team-policy` has previously been created, and this command is run to update the policy to add blocks of specific Angular packages:

```bash
chainctl libraries policy update team-policy \
  --block=purl=pkg:npm/%40angular/core \
  --block=purl=pkg:npm/%40angular/common \
  --block=purl=pkg:npm/%40angular/router
chainctl libraries policy enable team-policy --ecosystem=JAVASCRIPT --mode=ENFORCE
```

To block one specific version, include the version in the purl. For example, if a particular release is flagged with a known vulnerability that you want to block within your organization, you can block just the affected version while allowing the other versions. Use a command like the following:

```bash
chainctl libraries policy update team-policy \
  --block=purl=pkg:npm/ua-parser-js@0.7.29
chainctl libraries policy enable team-policy --ecosystem=JAVASCRIPT --mode=ENFORCE
```

To block all versions of a package, omit the version. For example, the following command updates the existing `team-policy` to add a block of all versions of a package:

```bash
chainctl libraries policy update team-policy \
  --block=purl=pkg:pypi/<name>
chainctl libraries policy enable team-policy --ecosystem=PYTHON --mode=ENFORCE
```

You can also combine `block` rules with a custom cooldown in the same policy. The following example creates a policy that blocks `colourama`, a typosquat of the `colorama` package. In addition, a cooldown is included:

```bash
chainctl libraries policy create --name=team-policy \
  --cooldown-days=2 \
  --block=purl=pkg:pypi/colourama
chainctl libraries policy enable team-policy --ecosystem=PYTHON --mode=ENFORCE
```

### Check blocked packages

Use `chainctl libraries packages blocked` to review what a policy has blocked. By default, this shows pull events that were blocked under any enforced policies. For example:

```bash
chainctl libraries packages blocked --ecosystem=JAVASCRIPT
```

If you have policies enabled in Preview mode, you can check successful pulls that *would have been blocked* in the last 30 days if the policy were to be enforced. For example:

```bash
chainctl libraries policy enable example-policy --ecosystem=JAVASCRIPT --mode=PREVIEW
chainctl libraries packages blocked --mode=PREVIEW --ecosystem=JAVASCRIPT
```

Replace `example-policy` with the name of the policy you want to preview.

## Override policies

### Override a blocked package

Use `--allow` to permit a package that has been blocked by a policy or by malware and greyware scanning.

Override policies takes precedence over block policies.

### Override cooldown for a package version

A cooldown override is useful when a newly published version includes an urgent fix and you need it before the cooldown window expires. For example:

```bash
chainctl libraries policy update team-policy \
    --allow='purl=pkg:npm/undici@8.4.1,override-cooldown=true,justification="urgent patch"'
```

If the new version pulls in transitive dependencies that are also blocked under a cooldown policy, those transitive packages must be overridden too.

### Override malware or greyware blocking

A malware override should be used sparingly and only after your security team has explicitly reviewed the package. A justification is required when you set `override-malware=true`.

```bash
chainctl libraries policy update team-policy \
  --allow='purl=pkg:npm/node-ipc@10.1.3,override-malware=true,justification="approved in SEC-1234"'
```

## Troubleshooting and FAQ

### Why does `chainctl` return "Invalid argument: enable takes no arguments"?

Prior to `chainctl` v0.2.313, when enabling a policy, you needed to include the `--policy` flag to pass in the policy name. In v.0.2.313 and later, you do not need to include a flag. For example, to enable a policy called `3day-cooldown`, run the following command: `chainctl libraries policy enable 3day-cooldown`. [Update `chainctl` to the latest version](/get-started/getting-started-with-chainctl/#update-chainctl-to-the-latest-release) to use this functionality.
