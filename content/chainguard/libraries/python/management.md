---
title: "Manage and update dependencies"
linktitle: "Dependency maintenance"
description: "Manage Chainguard Libraries for Python dependencies after setup, including package updates, verification, and monitoring security improvements"
type: "article"
date: 2025-03-25T08:04:00+00:00
lastmod: 2026-08-28T19:09:28+00:00
draft: false
tags: ["Chainguard Libraries", "Python"]
images: []
menu:
  docs:
    parent: "python"
    identifier: "Python Management"
weight: 053
toc: true
---

Chainguard Libraries for Python operates transparently after completing the
[repository manager
configuration](/chainguard/libraries/python/global-configuration/) or [build
tool configuration](/chainguard/libraries/python/build-configuration/),
automatically providing security-enhanced versions of your PyPI dependencies.
After setup, most package retrieval happens through your configured package
index or repository manager. Use this page for recurring maintenance tasks and
for deciding where to troubleshoot when a dependency changes.

Chainguard Libraries serves Chainguard-built artifacts when they are available.
When [upstream
fallback](/chainguard/libraries/overview/#upstream-fallback-and-controls) is
enabled, an artifact that Chainguard has not yet built may first be served
through Chainguard’s upstream tier. With [build
pinning](/chainguard/libraries/build-pinning/), the exact package version
remains pinned to the artifact tier your organization first received, so a
previously downloaded wheel or source distribution is not immediately replaced
when Chainguard publishes a built equivalent.

A package may already be present in a developer’s `pip`, `uv`, or Poetry cache,
in a repository manager cache, or a container layer. A cached package is not
automatically replaced just because a Chainguard-built equivalent becomes
available.

For Python, a single package version can resolve to different wheels depending
on the Python version and platform. The pinned file, selected artifact, and
resulting hash may therefore vary by environment; test and update hashes for
each supported environment when applicable.

## Verify dependencies

Use `chainctl libraries verify` to check whether an artifact comes from
Chainguard Libraries.

To verify an installed virtual environment:

```bash
chainctl libraries verify --detailed .venv/
```

For additional verification commands, command options, permissions, and
supported artifact types, refer to the [Verification
documentation](/chainguard/libraries/verification/).

### Inspect artifacts in a repository manager

If your organization uses a repository manager, you can inspect the Chainguard
proxy or remote repository to audit which artifacts were retrieved through
Chainguard Libraries. Use the repository manager’s package or browsing view to
locate an artifact and compare its coordinates, file name, size, checksum, and
available metadata.

Refer to the [Verification page](/chainguard/libraries/verification/) for more
information on verifying artifacts in a repository manager.

## Refresh cached artifacts

The number of available artifacts in Chainguard Libraries for Python increases
over time. If an artifact was already retrieved from the PyPI
Repository and is available in your repository manager or local repository it is
not automatically replaced with the equivalent Chainguard Library version.

To adopt new Chainguard-built artifacts, refer to the [build pinning
documentation](/chainguard/libraries/build-pinning/#adopt-a-chainguard-build-after-removing-a-pin)
for instructions on removing existing pinned versions.

Refreshing cached artifacts may also be necessary to solve other issues, such as
stale or corrupted artifacts or metadata, repository configuration changes, and
resolution troubleshooting. To refresh the same artifact your organization is
already using:

1. Confirm that the project and CI/CD environment use the intended Chainguard
   index or repository manager endpoint.
1. Update the dependency or dependency constraint with your package manager.
1. Run the project’s tests and security checks.
1. Review and commit the resulting lockfile or hash-pinned requirements changes.

If an exact package version is pinned, Chainguard continues to serve the pinned
artifact after the cache is refreshed.

For a more fine-grained approach you can also delete subsections of local
repositories and the proxy repositories.

### Prepare for package hash changes

A hash identifies the exact bytes of a downloaded Python artifact.
Chainguard-built artifacts have different hashes from the equivalent upstream
artifacts because they are rebuilt in a secure environment.

During initial migration, if your project uses hash-pinned lockfiles, update
those values with [the `chainctl libraries update-hashes`
command](/platform/chainctl/chainctl-docs/chainctl_libraries_update-hashes/),
then run your normal tests and verification checks. For a full migration
sequence, including cache and project-configuration handling, refer to the
[migration guide for Chainguard Libraries for
Python](/chainguard/libraries/python/migration/).

For organizations that use Chainguard's [upstream
fallback](/chainguard/libraries/overview/#upstream-fallback-and-controls),
build pinning keeps the exact artifact previously served for that package
version. This prevents a later Chainguard rebuild from unexpectedly changing the
hash. You must remove the pin to adopt a newer Chainguard build. Refer to [Build
pinning](/chainguard/libraries/build-pinning/) for more information.
