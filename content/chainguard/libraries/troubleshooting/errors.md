---
title: "Error messages"
linktitle: "Error messages"
description: "Understand the errors Chainguard Libraries returns when a package or version is blocked, and how they appear across language ecosystems and package managers."
type: "article"
date: 2026-08-11T00:00:00+00:00
lastmod: 2026-09-01T13:45:43+00:00
draft: false
images: []
weight: 082
tags: ["Libraries", "Product"]
aliases:
  - /chainguard/libraries/errors/
---

Chainguard Libraries applies security controls to every package it serves through the
Chainguard Repository: malware and greyware scanning, and configurable policies such as a
cooldown period. When one of these controls blocks a package or version, Chainguard
withholds it and the install fails.

Chainguard also surfaces errors for other reasons, such as a missing entitlement or
invalid authentication.

**Note**: If your build tool or repository manager pulls from a public registry as a
fallback, it may fetch a blocked package and bypass Chainguard's controls. Chainguard
recommends pulling all open source packages through the
[Chainguard Repository](/chainguard/libraries/introduction/overview/#upstream-fallback-and-controls) only.

## Why a package or version is blocked

Chainguard blocks a package or version for one of the following reasons:

* **Malware or greyware detected**: The package or version is on Chainguard's malware and greyware block list, either from a public advisory (MAL ID) or from Chainguard's own source code scanning.
* **Malware scan pending**: A newly published version has not completed malware scanning yet.
* **Policy block**: The version is blocked by a policy configured by your organization, such as a cooldown policy.

To resolve a blocked package, choose a version that is not blocked, wait for a pending scan
or cooldown period to pass, or configure an
[override](/chainguard/chainguard-repository/library-policies/) to allow an exception for a
specific package or version.

## Package manager behavior

How a blocked package appears during development will depend on the package manager and language ecosystem:

* **`npm`** surfaces the block reason directly, reporting a blocked version as a `403` with the reason (for example, `MALWARE_DETECTED`).
* **Other package managers** (such as `pnpm`, `yarn`, `pip`, `uv`, `poetry`, `Maven`, and `Gradle`) typically report a blocked version as a `not found` or `no matching version found` error. When an entire package (all of its versions) is blocked for malware, a `409` error surfaces across most package managers.

## Other errors

The following errors indicate problems with authentication, entitlements, or a nonexistent package.

| Error | Meaning | Next steps |
| -- | -- | -- |
| Not authenticated (`401`) | Your pull token is missing or expired. | Reconfigure access. See [Access Chainguard Libraries](/chainguard/libraries/introduction/access/). |
| Missing entitlement (`403`) | Your organization is not entitled to the specific ecosystem. | See [Manage library entitlements](/chainguard/libraries/introduction/access/#manage-library-entitlements). |
| Package does not exist (`404`) | The requested package or version does not exist. | Confirm that the package name and version exist on the public upstream registry. |

## Learn more

* [View blocked malware in the Console](/chainguard/libraries/introduction/browse/#view-malware-information)
* [Library policies, overrides, and cooldown](/chainguard/chainguard-repository/library-policies/)
* [Access Chainguard Libraries](/chainguard/libraries/introduction/access/)
* [Manage build pinning](/chainguard/libraries/policies-and-security/build-pinning/)
