---
title : "Chainguard Repository"
lead: "The Chainguard Repository is a single, policy-aware endpoint for all artifacts that Chainguard builds and distributes — libraries, containers, VMs, and OS."
description: "Chainguard Repository Overview"
type: "article"
date: 2026-03-16T08:48:23+00:00
lastmod: 2026-03-17T00:48:23+00:00
draft: false
weight: 032
---

The Chainguard Repository is a single, policy-aware endpoint for all artifacts that Chainguard builds and distributes. It gives your organization one place to pull open source artifacts, configure security policies that govern how they are consumed, and monitor coverage and policy enforcement across your environment.

All artifacts served through the Chainguard Repository are either rebuilt by Chainguard from verifiable source in a SLSA L2-compliant build environment, or sourced from upstream public registries and protected by configurable policies. As Chainguard builds more artifacts from source, your organization's risk shrinks automatically — without any changes to your configuration or developer workflows.

## Artifact types

As of this writing, the Chainguard Repository contains the following artifact types:

| Artifact type | Description |
| ----- | ----- |
| [Chainguard JavaScript Libraries](/chainguard/libraries/chainguard-repository/) | Open source language dependencies rebuilt from source for JavaScript (npm). |
| [Chainguard OS Packages](/chainguard/chainguard-images/features/packages/private-apk-repos/#chainguard-os-packages) | The full set of packages built by Chainguard and used to create Chainguard containers. |


## Endpoints

Each artifact type is accessible via its own endpoint:

| Artifact type | Endpoint |
| ----- | ----- |
| Libraries for JavaScript | `libraries.cgr.dev/javascript` |
| OS Packages | `apk.cgr.dev/<organization-name>` |

See each artifact type's documentation for authentication and configuration details.


## Policies for Libraries

The Chainguard Repository includes a policy engine that lets you define rules governing which artifacts can be consumed and under what conditions. Policies are configured once in the Chainguard Console and enforced automatically across your environment.

For language dependencies, policies apply to both Chainguard-built packages and upstream packages served via the optional fallback to public registries (npm). Available policies include:

* **Upstream fallback** — Control whether packages not yet built by Chainguard can be sourced from the upstream public registry.  
* **Cooldown** — Block newly published upstream packages for a defined period before they can be pulled, giving the security community time to detect threats. A 7-day cooldown blocks 47% of malicious packages.  
* **CVE blocking** — Prevent packages with known critical vulnerabilities from being pulled.  
* **License enforcement** — Restrict dependencies to approved licenses.  
* **End-of-life prevention** — Block packages that have reached end-of-life status.

All packages — whether Chainguard-built or sourced from upstream — are also scanned for malware before being served. Any package with a detected malware identifier is blocked.


## Use case for OS Packages

This is for large customers who already build your own container images from packages using tools like Bazel, Dockerfiles, and `ruies_apko` and want to use a wider set of packages from Chainguard. Chainguard OS Packages makes over 400,000 built packages into your private APK repository.


## **Console**

The Chainguard Console is the central interface for configuring policies and monitoring artifact activity across your organization. Learn more in [Using the Chainguard Console](/chainguard/chainguard-images/how-to-use/images-directory/).

Access the Console at [console.chainguard.dev](https://console.chainguard.dev).


## **Learn more**

* [Chainguard Repository for JavaScript Libraries](/chainguard/libraries/chainguard-repository/)  
* [Chainguard OS Packages](/chainguard/chainguard-images/features/packages/private-apk-repos/#chainguard-os-packages/)