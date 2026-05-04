---
title : "Overview of Chainguard Repository"
linktitle: "Overview"
lead: "The Chainguard Repository is a single, policy-aware endpoint for all artifacts that Chainguard builds and distributes — libraries, containers, VMs, and OS."
description: "Chainguard Repository Overview"
type: "article"
date: 2026-03-16T08:48:23+00:00
lastmod: 2026-03-24T00:48:23+00:00
draft: false
weight: 010
---

The Chainguard Repository is a single, policy-aware endpoint for all artifacts that Chainguard builds and distributes. It gives your organization one place to pull open source artifacts, configure security policies that govern how they are consumed, and monitor coverage and policy enforcement across your environment.

All artifacts served through the Chainguard Repository are either rebuilt by Chainguard from verifiable source in a SLSA L2-compliant build environment, or sourced from upstream public registries and protected by configurable policies. As Chainguard builds more artifacts from source, your organization's risk shrinks automatically — without any changes to your configuration or developer workflows.

## Artifact types

As of this writing, the Chainguard Repository contains the following artifact types:

| Artifact type | Description |
| ----- | ----- |
| [Chainguard JavaScript Libraries](/chainguard/libraries/javascript/overview/) | Open source language dependencies rebuilt from source for JavaScript (npm). |

## Endpoints

Each artifact type is accessible via its own endpoint:

| Artifact type | Endpoint |
| ----- | ----- |
| Libraries for JavaScript | `libraries.cgr.dev/javascript` |

See each artifact type's documentation for authentication and configuration details.


## Policies for Libraries

The Chainguard Repository includes a policy engine that lets you define rules governing which artifacts can be consumed and under what conditions. Policies are configured once in the Chainguard Console and enforced automatically across your environment.

For language dependencies, policies apply to both Chainguard-built packages and upstream packages served via the optional fallback to public registries (npm). Available policies include:

* **Upstream fallback** — Control whether packages not yet built by Chainguard can be sourced from the upstream public registry.  
* **Cooldown** — When upstream fallback is enabled, block newly published package versions for a defined period before they can be pulled, giving the security community time to detect threats. The cooldown is configurable (0 to 3650 days) with a default of 7 days. The cooldown is applied globally across all packages to prevent dependency resolution errors.

> **Note**: Chainguard recommends a 7-day cooldown when enabling upstream fallback, to block a large share of malicious packages identified shortly after publication. Shorter cooldown periods increase the risk of pulling malicious or compromised upstream packages before the broader ecosystem can detect and report them.

All upstream packages are checked against public malware identifier feeds, and any package with a known malware idenitifier is blocked before being served.


## **Management**

The Chainguard Console is the central interface for configuring policies and monitoring artifact activity across your organization. Learn more in [Using the Chainguard Console](/chainguard/chainguard-images/how-to-use/images-directory/).

Access the Console at [console.chainguard.dev](https://console.chainguard.dev).


## **Learn more**

* [Chainguard Repository for JavaScript Libraries](/chainguard/libraries/chainguard-repository/)  

