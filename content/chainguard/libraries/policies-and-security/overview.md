---
title: "Chainguard Libraries policies and security overview"
linktitle: "Policies overview"
description: "Understand how Chainguard Libraries evaluates, verifies, and controls dependencies across supported ecosystems."
type: "article"
date: 2025-06-05T09:00:00+00:00
lastmod: 2026-08-28T16:31:04+00:00
draft: false
tags: ["Chainguard Libraries", "Policy", "Overview"]
weight: 051
toc: true
---

Learn how to verify Chainguard Library integrity, identify and remediate vulnerabilities, protect against malicious behavior, and apply configurable policies across Chainguard-built packages and protected upstream fallback packages.

* [Chainguard Library policies](/chainguard/chainguard-repository/library-policies/): Create and enforce rules that control which package versions your organization can pull, including cooldown settings, blocklists, allowlists, and deliberate exceptions.
* [Verification](/chainguard/libraries/policies-and-security/verification/): Use `chainctl libraries verify` to confirm which dependencies were built by Chainguard and review their signed provenance and software bills of materials (SBOMs).
* [CVE remediation](/chainguard/libraries/policies-and-security/cve-remediation/): Learn how Chainguard backports selected high- and critical-severity fixes to supported library versions and how to identify and use remediated releases.
* [Vulnerability scanners](/chainguard/libraries/policies-and-security/scanners/): Learn how common vulnerability scanners work with Chainguard Libraries and how to interpret findings for Chainguard-built and remediated dependencies.
