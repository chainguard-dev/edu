---
title: "How Chainguard creates container images with low-to-no CVEs"
linktitle: "Low-to-no CVEs"
description: "The three practices behind the low CVE counts in Chainguard Containers — minimal package sets, nightly rebuilds, and security advisories — and how to verify them with a scanner yourself"
type: "article"
tags: ["Video", "Chainguard Containers"]
date: 2024-05-31T12:21:01+00:00
lastmod: 2026-09-09T00:00:00+00:00
draft: false
images: []
weight: 070
toc: true
aliases:
- /chainguard/chainguard-images/videos/zerocve/
- /chainguard/chainguard-images/about/zerocve/
- /chainguard/containers/videos/zerocve/
- /chainguard/containers/about/zerocve/
- /chainguard/chainguard-images/videos/beyond_zero_pytorch_2024/
- /chainguard/chainguard-images/about/beyond_zero_pytorch_2024/
- /chainguard/containers/videos/beyond_zero_pytorch_2024/
- /chainguard/containers/about/beyond_zero_pytorch_2024/
- /chainguard/containers/concepts/beyond_zero_pytorch_2024/
---

Chainguard Containers typically report few or no CVEs when scanned, which raises a fair question about whether those findings are being suppressed. They are not. Scanners read Chainguard Containers exactly as they read any other container, and they report whatever they find. The low counts are instead the product of three practices: shipping less software, rebuilding nightly, and publishing security advisories that tell scanners what a given finding means.

This article explains each practice, and describes how to verify the results independently.

## Scanners do report CVEs in Chainguard Containers

Scanning a current container usually returns a short list of findings, or none at all:

```sh
grype cgr.dev/chainguard/jre:latest
```

Scanning an older build of the same container returns considerably more. Any digest works for this comparison, including whichever one your own Dockerfiles pin today. The following example uses a build published in October 2024:

```sh
grype cgr.dev/chainguard/jre@sha256:43afe3cb7331f517eff19667939fb84c1e7aed283608e752007cfbbf9b4252d1
```

```output
NAME                    INSTALLED  FIXED-IN   TYPE  VULNERABILITY        SEVERITY
. . .
openjdk-23-jre          23.0.1-r0  23.0.2-r0  apk   GHSA-46mv-5cpj-wjxv  Unknown
zlib                    1.3.1-r4   1.3.2-r0   apk   GHSA-h858-mf2m-8jf4  Unknown
```

The key point is that CVE counts on Chainguard Containers are a function of how recently the container was built. Vulnerabilities are disclosed against software that has already been published, so any given build accumulates findings as it ages. The `FIXED-IN` column records the practical consequence — most of what a scanner finds in an old build has a newer package version that resolves it.

A pinned digest never changes. That is the purpose of pinning, and also its cost. Pair it with tooling that moves the pin, such as [Digestabot](/chainguard/containers/security-and-compliance/updating-containers/digestabot/), and refer to [Considerations for image updates](/chainguard/containers/security-and-compliance/updating-containers/considerations-for-image-updates/) for guidance on planning the cadence.

For current CVE data on a specific container and tag, refer to that container's entry in the [Chainguard Containers directory](https://images.chainguard.dev/directory?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-containers-concepts-zerocve).

## Practice 1: shipping less software

Software that isn't in the container cannot carry a vulnerability. Most Chainguard containers are [distroless](/chainguard/containers/concepts/getting-started-distroless/): they hold the application, its runtime dependencies, and little else. Most do not include a shell, a package manager, or the general-purpose utilities that a conventional base image carries in case they are needed.

That default is not absolute. Some containers do ship a shell or additional packages, either because the application requires them or for compatibility with common workflows. The standard Node.js container includes `busybox` and `npm` for that reason, whereas the Python container has no shell at all. Chainguard's slim variants pare those compatibility packages back.

Shipping fewer packages is what makes the other two practices manageable. A container with a few dozen packages leaves only a few dozen to track, patch, and triage.

Two related pages cover the tradeoffs this creates. [Chainguard Container variants](/chainguard/containers/concepts/container-variants/) explains both the development variants, which add a shell and package manager for build stages and debugging, and the slim variants. [Debugging distroless container images](/chainguard/containers/troubleshooting/debugging-distroless-images/) covers working with a container that has no shell.

## Practice 2: rebuilding nightly

Chainguard tracks upstream releases and rebuilds its containers nightly, so a patched package reaches a published container without waiting for a release cycle. Keeping software current is unglamorous work, and it accounts for most of the effort involved: the majority of known vulnerabilities in a running system have already been fixed upstream and have not been picked up.

The practical consequence is that each fix arrives as a new build. Pulling the same digest for six months means running six-month-old software regardless of how quickly Chainguard patched it, which is why the [container lifecycle](/chainguard/containers/concepts/lifecycle-and-eol/versions/) and update tooling matter as much as the container contents do.

## Practice 3: publishing security advisories

The first two practices address most findings. The third handles the remainder: findings that are genuine but already resolved, and findings that were never applicable to begin with.

A Chainguard security advisory is a machine-readable record, issued per package and per CVE, that scanners read alongside their own vulnerability data. Each advisory records one of several determinations: the CVE is fixed as of a given package version; the package is not affected, for instance because the vulnerability only reaches Windows code paths and the package is built for Linux; a fix is pending upstream; or a fix is not planned. Scanners that consume these records filter their output accordingly and report more accurate results.

Advisories are published in several places:

- The [Security Advisories page](https://images.chainguard.dev/security/?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-containers-concepts-zerocve) in the Containers directory, for browsing by CVE or container.
- [`wolfi-dev/advisories`](https://github.com/wolfi-dev/advisories) on GitHub, where each package's advisories live as YAML.
- Alpine-style `secdb` JSON feeds, for scanners and automation.

[How to use Chainguard Security Advisories](/chainguard/containers/security-and-compliance/security-advisories/how-to-use/) covers reading and consuming them, and [How Chainguard issues Security Advisories](/chainguard/containers/security-and-compliance/security-advisories/how-chainguard-issues/) walks through an advisory's life from disclosure to remediation, including the feed URLs.

An advisory is not a mechanism for dismissing a finding. It records a determination about a specific package version, and scanners remain free to disagree. [False positives and false negatives with container image scanners](/chainguard/containers/security-and-compliance/working-with-scanners/false-results/) explains how both arise and how to tell them apart.

## What this means in practice

- Scan the build you are actually running, by digest, rather than a tag that may have moved.
- Expect findings to accumulate on any container you pin and stop updating. This reflects the software aging rather than any change in the scan.
- Consult the advisory before triaging a finding. It may already record the CVE as fixed or not applicable.

The following video demonstrates the same three practices, including a scan of an old container image against a current one:

{{< youtube Fuw9lYX6Ne8 >}}

{{< blurb/free-tier-message >}}

## Related reading

- [How Chainguard issues Security Advisories](/chainguard/containers/security-and-compliance/security-advisories/how-chainguard-issues/) — the stages of an advisory, and where to get the feeds.
- [Getting started with distroless containers](/chainguard/containers/concepts/getting-started-distroless/) — what minimal containers leave out, and what that changes.
- [Chainguard Containers product release lifecycle](/chainguard/containers/concepts/lifecycle-and-eol/versions/) — which versions Chainguard actively patches.
- [Keeping containers updated](/chainguard/containers/security-and-compliance/updating-containers/) — tooling that moves your pins as new builds ship.
