---
title: "Error messages"
linktitle: "Error messages"
description: "Understand the errors Chainguard Libraries returns when a package or version is blocked, and how they appear across language ecosystems and package managers."
type: "article"
date: 2026-08-11T00:00:00+00:00
lastmod: 2026-08-11T00:00:00+00:00
draft: false
images: []
weight: 055
tags: ["Libraries", "Product"]
---

Chainguard Libraries applies security controls to every package it serves through the
Repository: malware and greyware scanning, and configurable policies such as a
cooldown period. When a package or version is blocked by one of these controls,
Chainguard does not serve it and the pull fails with a `409` error.

A `409` means the package or version is blocked, for one of the reasons below. This page explains the
reasons and how different package managers behave.

## Error types

### Blocked packages due to policies or malware 

A `409` error is returned for one of the following reasons:

* **Malware or greyware detected**: The version is on Chainguard's malware and greyware block list, either from a public advisory (MAL ID) or from Chainguard's own source code scanning.
* **Malware scan pending**: A newly published version has not completed malware scanning yet.
* **Policy block**: The version is blocked by a policy configured by your organization, such as a cooldown policy.

To resolve a blocked package due to one of these reasons, you can choose a version that is not blocked, wait for a pending scan or cooldown to complete, or configure an [override](/chainguard/chainguard-repository/library-policies/) to allow an exception for a specific package or version.

**Note**: During dependency resolution, `npm` reports a blocked version as a
`403` (rather than a `409`) and surfaces the reason. See the
[Package manager behavior](#package-manager-behavior) section below.

### Access and authentication errors

The following errors indicate access or authentication issues.

| Error | Meaning | Next steps |
| -- | -- | -- |
| Not authenticated (`401`) | Your pull token is missing or expired. | Reconfigure access. See [Access Chainguard Libraries](/chainguard/libraries/access/). |
| Missing entitlement (`403`) | Your organization is not entitled to the specific ecosystem. | See [Manage library entitlements](/chainguard/libraries/access/#manage-library-entitlements). |
| Package does not exist (`404`) | The requested package or version does not exist. | Confirm whether the package name and version exists on the public upstream registry. |

## Package manager behavior for blocked packages

**Note**: `npm` is the only package manager below that surfaces the block reason. All others surface the `409` error code.

| Ecosystem | Package manager | Behavior on blocked packages |
| -- | -- | -- |
| JavaScript | `npm` | Surfaces the reason in both cases: `E409` (`409 Conflict`) for a direct pull, and a `403` for a blocked dependency reached during resolution. |
| JavaScript | `pnpm` | Treats the `409` as transient and retries (about 70 seconds) before failing with `ERR_PNPM_FETCH_409`. See the [pnpm retry settings](https://pnpm.io/settings#fetchretries). |
| JavaScript | `yarn` | Fails with the `409` error. |
| Python | `pip` | Reports `No matching distribution found`, the same message as a genuinely missing package. Run `pip -v` to see the `409` (`Could not fetch URL .../simple/<package>/: 409 Client Error: Conflict for url: ... - skipping`). |
| Python | `uv` | Fails with `HTTP status client error (409 Conflict)`. |
| Python | `poetry` | Fails with `409 Client Error: Conflict`. |
| Java | `Maven` | Fails with `status code: 409, reason phrase: Conflict`. |
| Java | `Gradle` | Fails with `Received status code 409 from server: Conflict`. |

To find out why a specific version is blocked, see
[Library policies](/chainguard/chainguard-repository/library-policies/).

If your build tool or repository manager pulls from a public registry as a
fallback, it may fetch a blocked package and bypass Chainguard's controls.
Chainguard recommends pulling all of your open source packages through the
[Chainguard Repository](/chainguard/libraries/overview/#upstream-fallback-and-controls) only.

## Learn more

* [View blocked malware in the Console](/chainguard/libraries/browse/#view-malware-information)
* [Library policies, overrides, and cooldown](/chainguard/chainguard-repository/library-policies/)
* [Access Chainguard Libraries](/chainguard/libraries/access/)
