---
title : "Overview of Chainguard Repository"
linktitle: "Overview"
aliases:
- /chainguard/administration/policies/
- /platform/administration/policies/
lead: "The Chainguard Repository is a single, policy-aware endpoint for all artifacts that Chainguard builds and distributes — libraries, containers, VMs, and OS."
description: "Chainguard Repository Overview"
type: "article"
date: 2026-03-16T08:48:23+00:00
lastmod: 2026-03-24T00:48:23+00:00
draft: false
weight: 010
---

The Chainguard Repository is a single, policy-managed experience for pulling artifacts that Chainguard either builds or distributes. It gives your organization one place to pull open source artifacts, configure security policies that govern how they are consumed, and monitor coverage and policy enforcement across your environment.

All artifacts served through the Chainguard Repository are either rebuilt by Chainguard from verifiable source in a SLSA L2-compliant build environment, or sourced from upstream public registries with configurable policy controls. As Chainguard builds more artifacts from source, your organization's risk shrinks automatically without any changes to your configuration or developer workflows.

## Artifact types

As of this writing, the Chainguard Repository contains the following artifact types:

| Artifact type | Description |
| ----- | ----- |
| [Chainguard Libraries for JavaScript](/chainguard/libraries/javascript/overview/) | Open source language dependencies rebuilt from source for JavaScript (npm). |
| [Chainguard Libraries for Java](/chainguard/libraries/java/overview/) | Open source language dependencies rebuilt from source for Java (Maven). |
| [Chainguard Libraries for Python](/chainguard/libraries/python/overview/) | Open source language dependencies rebuilt from source for Python (PyPI). |

## Endpoints

Each artifact type is accessible via its own endpoint:

| Artifact type | Endpoint |
| ----- | ----- |
| Libraries for [JavaScript](/chainguard/libraries/javascript/overview/) | `https://libraries.cgr.dev/javascript/` |
| Libraries for [Java](/chainguard/libraries/java/overview/) | `https://libraries.cgr.dev/java/` |
| Libraries for [Python](/chainguard/libraries/python/overview/) | `https://libraries.cgr.dev/python/` |

See each artifact type's documentation for authentication and configuration details.

## Policies for Libraries

The Chainguard Repository includes a policy engine that lets you define rules governing which artifacts can be consumed and under what conditions. Policies can be configured in the Chainguard Console or with `chainctl`, and are enforced automatically across your environment.

For language dependencies, policies apply to both Chainguard-built packages and upstream packages served via the optional fallback to public registries. Available policies include:

* **Upstream fallback**: Control whether packages not yet built by Chainguard can be sourced from the upstream public registry.
* **Cooldown**: When upstream fallback is enabled, block newly published package versions for a defined period before they can be pulled, giving the security community time to detect threats. The cooldown is configurable (0 to 3650 days) with a default of 7 days. It is applied globally across all packages to prevent dependency resolution errors.

All upstream packages are checked against public malware identifier feeds, and any package with a known malware idenitifier is blocked before being served.

> **Note**: With fallback enabled, Chainguard's malware and greyware scanning covers upstream packages, which addresses the primary risk a cooldown period is meant to mitigate. A cooldown period can still add a small buffer against issues the broader community surfaces after publication and is applied globally across your organization, but it also adds operational complexity and can introduce breakage. Choose a cooldown policy based on your own risk tolerance and priorities.

See [Libraries Overview](/chainguard/libraries/overview/#upstream-fallback-and-controls) for more information.

## Policies for Chainguard Containers

As with Libraries, you can also set policies for Chainguard Containers to define rules governing which container images can be consumed and under what conditions. Policies can be configured in the Chainguard Console or with `chainctl`, and are enforced automatically across your environment.

Available policies include:

* **no-eol**: Prevent end-of-life container images from being used.
* **cooldown**: Block newly published container image versions for a defined period before they can be pulled, giving the security community time to detect threats. The cooldown is configurable (0 to 3650 days) with a default of 7 days. It is applied globally across all packages to prevent dependency resolution errors.

> **Note**: Chainguard recommends a 7-day cooldown when enabling upstream fallback, to block a large share of malicious packages identified shortly after publication. Shorter cooldown periods increase the risk of pulling malicious or compromised upstream packages before the broader ecosystem can detect and report them.

The packages that make up Chainguard Images are checked against public malware identifier feeds, and any package with a known malware idenitifier is remediated before being used in any image.

See [Container Pull Policies](/chainguard/chainguard-images/staying-secure/policies/) for more information.

## Management

The Chainguard Console and `chainctl` can be used for configuring and managing policies across your organization. Learn more in [Using the Chainguard Console](/platform/console/images-directory/) and [Get Started with chainctl](/get-started/getting-started-with-chainctl/).

Access the Console at [console.chainguard.dev](https://console.chainguard.dev).

## Learn more

* [Chainguard Libraries for JavaScript](/chainguard/libraries/javascript/overview/)
* [Chainguard Libraries for Java](/chainguard/libraries/java/overview/)
* [Chainguard Libraries for Python](/chainguard/libraries/python/overview/)
