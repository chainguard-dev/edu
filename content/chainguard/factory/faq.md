---
title: "Chainguard Factory FAQs"
linktitle: "FAQs"
type: "article"
description: "Frequently asked questions about Chainguard Factory, the automated build system that monitors and updates thousands of open source projects for enhanced security"
lead: "Chainguard Factory is the automated infrastructure that continuously transforms thousands of open source projects into containers, libraries, and VMs with enhanced security posture and the latest patches."
date: 2025-07-17T08:49:31+00:00
lastmod: 2025-07-23T15:09:59+00:00
draft: false
tags: ["Chainguard Containers", "Chainguard VMs"]
images: []
menu:
  docs:
    parent: "chainguard-factory"
weight: 010
toc: true
---

## What is the Chainguard Factory?

The Chainguard Factory refers to all the engineering and automation work that goes into building, publishing, and maintaining the software packaged in Chainguard's products. This includes continuously monitoring, testing, and updating thousands of open source projects that make up Chainguard containers, libraries, and VMs.

## How does Chainguard keep its software up to date?

Chainguard uses automated systems to vigilantly monitor for new releases using
the GitHub API, [the Release Monitoring project](https://release-monitoring.org),
[PyPI](https://pypi.org/), [Maven
Central](https://mvnrepository.com/repos/central) and the [npm
registry](https://docs.npmjs.com/about-the-public-npm-registry). When a new
release is detected, automation opens a pull request, patches the relevant
software, and kicks off a suite of tests. If issues arise, AI analyzes logs and
suggests fixes before human engineers review and approve changes. This process
ensures prompt, high-quality updates.

## How often are Chainguard packages, containers, and VMs updated?

Updates happen constantly and at high speed. There are over 1,500 containers, plus VMs, and libraries – each of which is updated daily as needed, depending on upstream changes and security events.

## What happens when a core dependency (like Go, OpenSSL, or glibc) is updated?

Updates to foundational packages require cascading rebuilds of all dependent packages and images. For updates to core dependencies, this results in rebuilds of hundreds, or even thousands, of packages and containers. Major updates like these receive additional engineering focus to ensure a smooth transition.

## How does Chainguard handle software that goes End-of-Life (EOL) upstream?

After a package goes EOL, it is no longer supported upstream, and updates will cease in the Wolfi repository. However, customers benefit from an extended EOL Grace Period with Chainguard OS, during which Chainguard continues to build old versions for an additional timeframe.

## How are CVEs (security advisories) managed?

Chainguard uses the [grype](https://github.com/anchore/grype) security scanner to detect when a CVE affects one of its packages. Automation flags these CVEs for investigation by engineers. If determined to be a false positive, the status is set to `Not Affected`; if real, the issue is resolved by patching or updating dependencies and the status changes to `Fixed`.

## How does Chainguard prevent malware or malicious updates?

The factory analyzes code for known malware and checks for unexpected changes in software behavior, such as new network connections not mentioned in changelogs. This helps detect subverted upstream projects or supply chain attacks (like the recent XZ utils incident) before they affect customers.

## What infrastructure is used for building?

GitHub is used for source code management, but our builds execute on Kubernetes clusters for scalability and observability. The build environment is hardened following SLSA (Supply-chain Levels for Software Artifacts) and OpenSSF security guidelines, reinforcing both integrity and provenance.

## What is the role of automation, AI, and human engineers?

Automation and AI enable high-velocity operations, handling the bulk of routine updates and testing. However, due to the complexity and variability of open source, human engineers with diverse technological expertise play a critical role in resolving exceptions, complex updates, and security events.

## Why is the Chainguard Factory important for customers?

The factory enables Chainguard to reliably convert open source into ready-to-use, highly secure containers, VMs, and libraries, giving customers timely access to updates while minimizing their security risk and operational overhead.
