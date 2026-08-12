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

Chainguard Repository applies security controls to every package it serves:
malware and greyware scanning, and configurable policies such as a cooldown
period. When a package is blocked by one of these controls,
Chainguard withholds it and returns an error that includes the reason.

This page explains what those errors mean, and how they appear across language
ecosystems and package managers.

## Error types

### Policy and malware blocks

| Error | Meaning | Next steps |
| -- | -- | -- |
| Malware or greyware detected (`409`) | The version is on Chainguard's block list, either from a public advisory (MAL ID) or from Chainguard's own source code scanning. | Choose a version that is not blocked, or [override](/chainguard/chainguard-repository/library-policies/) for a deliberate exception. |
| Malware scan pending (`409`) | An new upstream version has not completed malware scanning yet, so it is not served. | Wait for the scan to complete. |
| Policy block (`409`) | The version is blocked by a policy configured by your organization. This may include a cooldown policy, a custom package block list, or other policies. | Wait for the cooldown window to pass if applicable, or [override](/chainguard/chainguard-repository/library-policies/) the policy block. |

**Note**: `npm` will display a `403` error code instead of a `409` for any resolved dependencies that are blocked. See more details in the [Package manager behavior](#package-manager-behavior) section below.

### Operational errors

The following errors indicate access or authentication issues.

| Error | Meaning | Next steps |
| -- | -- | -- |
| Not authenticated (`401`) | Your pull token is missing or expired. | Reconfigure access. See [Access Chainguard Libraries](/chainguard/libraries/access/). |
| Missing entitlement (`403`) | Your organization is not entitled the specific ecosystem. | See [Manage library entitlements](/chainguard/libraries/access/#manage-library-entitlements). |
| Package does not exist (`404`) | The requested package or version does not exist. | Confirm whether the package name and version exists on the public upstream registry. |

## Package manager behavior

Package managers vary in how they output error codes and response bodies. The table below explains variances in behavior based on the ecosystem and package manager in use.

| Ecosystem | Package manager | Behavior |
| -- | -- | -- |
| JavaScript | `npm` | A blocked version that is requested directly surfaces a `409` with the reason. For any transitive dependencies that are blocked, `npm` surfaces a `403` with the reason. |
| JavaScript | `pnpm` | Blocked versions surface a `409` with the reason. `pnpm` treats a `409` with retry behavior. See the [pnpm documentation on retries](https://pnpm.io/settings#fetchretries) for more details.|
| JavaScript | `yarn` | Blocked versions surface a `409` with the reason.  |
| Python | `pip` | Blocked versions surface a 409 *without* the reason. A blocked version usually appears as `Could not find a version that satisfies the requirement`. |
| Python | `uv` | Blocked versions surface a `409` with the reason. For example, `HTTP status client error (409 Conflict)`. |
| Python | `poetry` | Blocked versions surface a `409` with the reason. For example, `409 Client Error: Conflict for url`. |
| Java | `Maven` | Blocked versions surface a 409 *without* the reason. For example, `Received status code 409 from server`. |
| Java | `Gradle` | Blocked versions surface a 409 *without* the reason. For example, `...Received status code 409 from server: Conflict`. |

If your build tool or repository manager pulls from a public registry, it may fetch a blocked artifact from that
fallback and bypass Chainguard's controls. We recommend pulling all
open source dependencies through the
[Chainguard Repository](/chainguard/libraries/overview/#upstream-fallback-and-controls) and limiting public registry access.

## Learn more

* [View blocked malware in the Console](/chainguard/libraries/browse/#view-malware-information)
* [Library policies, overrides, and cooldown](/chainguard/chainguard-repository/library-policies/)
* [Access Chainguard Libraries](/chainguard/libraries/access/)
