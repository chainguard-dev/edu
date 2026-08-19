---
title: "Manage build pinning for Chainguard Libraries"
type: "article"
linktitle: "Build pinning"
description: "Use build pinning to keep library artifacts stable across rebuilds."
date: 2026-08-19T08:04:00+00:00
lastmod: 2026-08-19T17:53:10+00:00
draft: false
tags: ["Chainguard Libraries", "Build pinning"]
menu:
  docs:
    parent: libraries
weight: 8
toc: true
---

Chainguard Libraries can serve a package version as either a Chainguard-built artifact or an [upstream artifact that is scanned and proxied through Chainguard](/chainguard/libraries/overview/#upstream-fallback-and-controls). Chainguard-built artifacts may have different checksums for the same version of the upstream artifact. If your lockfile records an upstream checksum and Chainguard later builds that package, your package manager can fail with integrity errors upon dependency resolution.

Build pinning keeps library artifacts stable when Chainguard publishes a new build of a package version you previously pulled from the scanned upstream fallback. Chainguard-built artifacts are always the default and take priority when available. Pinning only affects the exact package version already pinned. When enabled, Chainguard remembers which upstream versions your organization pulled and continues serving those specific versions even if a new Chainguard build is available, until you remove the pin. Moving to a different version of the package is unaffected; since that version was never pinned, it resolves fresh and Chainguard’s build is served by default.

This feature is enabled by default.

> Note: Build pinning does not override Chainguard policy or malware controls. If a pinned upstream package is blocked by a policy or by malware scanning, the request will return an error.

## Prerequisites

Before getting started, you need:

* An [entitlement to Chainguard Libraries with upstream fallback enabled](/chainguard/libraries/access/#manage-library-entitlements)
* [`chainctl` installed and authenticated](/platform/chainctl-usage/how-to-install-chainctl/)
* A working configuration using Chainguard Libraries - a package manager configured to pull from Chainguard Libraries directly or a repository manager that proxies Chainguard Libraries

## Pin builds

Your package versions are automatically pinned after you run an install for your project. Use this workflow when adopting build pinning:

1. Run an install for your project.
1. Confirm that pins appear: Run `chainctl libraries cache list`.
1. Commit the resulting lockfile if it changed.
1. When you are ready to adopt newer Chainguard builds, remove pins for the affected packages.
1. Regenerate or update the lockfile and run your normal build and test commands.

## View pinned builds

To list pins for your organization:

```bash
chainctl libraries cache list
```

The output includes the package, version, serving tier, whether the pin is active, and when the artifact was observed.

## Remove pins

After removing pins, regenerate or update your lockfile.

### Preview the change

Use `--dry-run` to preview which pins would be removed:

```bash
chainctl libraries cache zap --dry-run
```

### Remove all pins

To remove all pins for an ecosystem:

```bash
chainctl libraries cache zap --ecosystem javascript
```

After the zap, affected package versions resolve again, prioritizing Chainguard builds for any package versions that may have previously been pulled from Chainguard’s upstream fallback. Any new Chainguard-built artifacts may result in changes in a package version’s checksums. The zap does not override malware or policy blocks.

### Remove specific package pins

To remove a specific package pin:

```bash
chainctl libraries cache zap --package <PACKAGE>
```

To narrow the operation to one package version, include the `--version` flag: `--version <VERSION>`.

To skip the confirmation prompt in scripts or automation, include the `--yes` flag.

## Opt out of build pins

To stop recording and enforcing pins for an ecosystem, run the following command:

```bash
chainctl libraries cache opt-out --ecosystem javascript
```

## Adopt a Chainguard build after removing a pin

To move a package from an upstream-sourced artifact to a Chainguard-built one, you must force a fetch after the zap. Note that if Chainguard has not rebuilt a package, the following steps will re-pin to upstream again.

First, force a fresh install:

{{< tabs >}}

{{% tab title="Java" %}}

Java (Maven):

```bash
mvn dependency:purge-local-repository -DmanualInclude="<groupId>:<artifactId>:<version>"
mvn install
```

Java (Gradle):

```bash
./gradlew build --refresh-dependencies
```

{{% /tab %}}

{{% tab title="JavaScript" %}}

JavaScript (npm):

```bash
rm -rf node_modules package-lock.json
npm install
```

{{% /tab %}}

{{% tab title="Python" %}}

Python (pip):

```bash
pip install --no-cache-dir --force-reinstall <package>==<version>
```

{{% /tab %}}

{{< /tabs >}}

Next, confirm that the package now resolves to a Chainguard build:

```bash
chainctl libraries cache list --package <PACKAGE> --live
```

After confirming the change, commit the updated lockfile and run your normal install again.

## Troubleshooting and FAQ

### Does build-pinning apply under the Chainguard-only policy?

No. You must have upstream fallback enabled in order to use build pinning.

### What happens to my pins when I switch policies?

Going from `CHAINGUARD_AND_UPSTREAM` (upstream fallback enabled) to `CHAINGUARD` (fallback disabled) stops pins from being served, but the pin records aren’t deleted. They persist until the cache is manually zapped. Switching back to `CHAINGUARD_AND_UPSTREAM` later can resurrect old pins unexpectedly.
