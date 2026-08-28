---
title: "Manage and update dependencies"
linktitle: "Dependency maintenance"
description: "Manage Chainguard Libraries for Java dependencies after setup, including verification, cache refreshes, and checksum changes."
type: "article"
date: 2025-03-25T08:04:00+00:00
lastmod: 2026-08-28T19:09:28+00:00
draft: false
tags: ["Chainguard Libraries", "Java"]
images: []
menu:
  docs:
    parent: "java"
    identifier: "Java Management"
weight: 053
toc: true
---

Chainguard Libraries for Java operates transparently after configuring your [repository manager](/chainguard/libraries/java/global-configuration/) or [your build tool](/chainguard/libraries/java/build-configuration/), automatically providing security-enhanced versions of your Maven dependencies. After you configure Chainguard Libraries for Java, use this page for recurring maintenance tasks.

Chainguard Libraries serves Chainguard-built artifacts when they are available. When [upstream fallback](/chainguard/libraries/overview/#upstream-fallback-and-controls) is enabled, an artifact that Chainguard has not yet built may first be served through Chainguard’s upstream tier. With [build pinning](/chainguard/libraries/build-pinning/), the exact package version remains pinned to the artifact tier your organization first received, so a previously downloaded upstream artifact is not immediately replaced when Chainguard publishes a built equivalent.

Existing artifacts may already be present in a developer’s local Maven cache or in a repository manager cache, so a previously downloaded upstream artifact is not automatically replaced just because a Chainguard-built equivalent becomes available.

The following sections detail optional management, maintenance, and auditing
steps on the repository manager and the build tool.

<a id="java-verification"></a>

## Verify dependencies

Use `chainctl libraries verify` to check whether an artifact comes from Chainguard Libraries:

```bash
chainctl libraries verify path/to/artifact.jar
```

For Java, run verification against the individual JAR files in the local Maven repository cache before assembling a fat JAR or other bundled artifact. The verifier identifies artifacts using their checksums and provenance information; it cannot reliably trace merged classes in a fat JAR back to their source JARs.

For command options, permissions, and supported artifact types, refer to the [Verification documentation](/chainguard/libraries/verification/).

### Inspect artifacts in a repository manager

If your organization uses a repository manager, you can inspect the Chainguard proxy or remote repository to audit which artifacts were retrieved through Chainguard Libraries. Use the repository manager’s package or browsing view to locate an artifact and compare its coordinates, file name, size, checksum, and available metadata.

Refer to the [Verification page](/chainguard/libraries/verification/) for more information on verifying artifacts in a repository manager.

## Refresh cached artifacts

The number of available artifacts in Chainguard Libraries for Java increases
over time. If an artifact was already retrieved from the Maven Central
Repository and is available in your repository manager or local repository it is
not automatically replaced with the equivalent Chainguard Library version.

To adopt a newer Chainguard-built artifact, refer to the [build pinning documentation](/chainguard/libraries/build-pinning/#adopt-a-chainguard-build-after-removing-a-pin) for instructions on removing existing pinned versions.

Refreshing cached artifacts may also be necessary to solve other issues, such as stale or corrupted artifacts or metadata, repository configuration changes, and resolution troubleshooting. To refresh the same artifact your organization is already using:

1. Remove the affected artifact from the developer’s local Maven cache.
1. If applicable, remove the affected artifact from the repository manager’s proxy cache, following your organization’s cache-management procedure.
1. Run the build again so Maven requests the artifact from the configured Chainguard Libraries repository.
1. Verify the resulting JARs with `chainctl libraries verify`.

If an exact package version is pinned, Chainguard continues to serve the pinned artifact after the cache is refreshed.

Prefer removing only the affected artifact or dependency subtree. Avoid broadly deleting production or shared caches unless you understand the operational impact and have a recovery plan.

### Prepare for checksum changes

A checksum identifies the exact bytes of a library artifact. Chainguard-built artifacts have different checksums from upstream artifacts with the same Maven coordinates and version because they are rebuilt in a secured environment.

During initial migration, if your project records checksums or integrity values, update those values as part of the migration or cache refresh, then run your normal tests and verification checks. For a full migration sequence, including cache and project-configuration handling, refer to the [migration guide for Chainguard Libraries for Java](/chainguard/libraries/java/migration/).

For organizations that use Chainguard's [upstream fallback](/chainguard/libraries/overview/#upstream-fallback-and-controls), build pinning keeps the exact artifact previously served for that package version. This prevents a later Chainguard rebuild from unexpectedly changing the checksum. You must remove the pin to adopt a newer Chainguard build. Refer to [Build pinning](/chainguard/libraries/build-pinning/) for more information.

## Security and policy guidance

Refer to the following pages for topics broader than routine dependency maintenance:

- [CVE remediation for Chainguard Libraries](/chainguard/libraries/cve-remediation/) for remediated library versions and upgrade guidance.
- [Chainguard Libraries policies](/chainguard/chainguard-repository/library-policies/) for upstream fallback, cooldown, and package-serving policy.
- [Error messages](/chainguard/libraries/errors/) and the [Chainguard Libraries FAQ](/chainguard/libraries/faq/) for troubleshooting and edge cases.
