---
title: "Overview of Chainguard OS"
linktitle: "Overview"
type: "article"
description: "Chainguard OS Overview"
lead: "Get to know the OS behind Chainguard"
date: 2025-06-03T08:49:31+00:00
lastmod: 2025-06-03T08:49:31+00:00
draft: false
tags: ["Chainguard OS", "Product"]
images: []
menu:
  docs:
    parent: "chainguard-os"
weight: 010
toc: true
---

Chainguard OS was built in house to enable a more secure, agile, and efficient software distribution model, so that downstream products like container images could benefit from our organization's approach. 

Chainguard OS adheres to four key principles:
* Continuous Integration and Delivery
* Nano Updates and Rebuilds
* Minimal, Hardened, Immutable Artifacts
* Delta Minimization

On this page, we'll discuss each of these components and how Chainguard OS differs from the operating system status quo.

## Continuous Integration and Continuous Delivery (CI/CD)

Chainguard OS emphasizes the continuous integration, testing, and release of upstream software packages, ensuring a streamlined and efficient development pipeline through automation.

Chainguard OS was built to privilege CI/CD of software artifacts so that thousands of independent (or loosely dependent) open source projects could be more securely built into hundreds of thousands of versioned "packages." Unlike traditional distros, there is no major OS version (such as RHEL7 or Ubuntu 22.04 LTS) with a pinned catalog of packages; every available package is always installable with Chainguard OS while also accepting a wide range of packaging ecosystems, including all of the language-specific package managers beyond Chainguard OS’s own package manager.

Leveraging event-driven automation, Chainguard OS ensures that every package in the catalog has a “release monitor” capturing new upstream releases right away. This monitor triggers automatic package recompiles, quality assurance and acceptance testing, security scanning, and publication. Chainguard container images that include that package will automatically benefit from updates due to our [multi-layer approach](/chainguard/chainguard-images/overview/#why-multi-layer-container-images) that ships updated versions to relevant images. These packsges are also published to public and private registries at the same time.

With Chainguard OS, users can rely on products that take advantage of an ever-growing catalog of open source and enterprise software packages. Rather than picking a favorite version of every software project every couple of years and attempting to maintain that for a decade or more, Chainguard OS takes a different approach: it enables [continuous support and EOL](/chainguard/chainguard-images/about/versions/) for the same versions that the upstream project maintainers recommend.

## Nano Updates and Rebuilds

Favoring incremental updates and rebuilds over major release upgrades, Chainguard OS supports smoother transitions that minimize disruptive changes. Our goal is for engineers adopting Chainguard products to never have to think about major OS version upgrades that dominate a roadmap for months at a time every two years. Through continuously introduced daily nano upgrades, paced through staging and testing gates, any offending regression can be readily pinpointed, reported, and addressed in subsequent updates hours or days later.

Both minor “updates” and major “upgrades” are simultaneously delivered through Chainguard OS. Chainguard Containers offer clear, firm, and distinct boundaries for each application, so that updates and upgrades are cleaner. 

Chainguard OS takes advantage of the ephemeral application layer of container images being separate from the persistent storage and unique configuration data; it is able to simultaneously instantiate new containers running the updated and upgraded application and destroy the previous instantiation running the down-level application version. In this way, updates (patches) and upgrades (major changes) are introduced instantly, and rollbacks to previous versions can be done by launching the previous container’s image.

## Minimal, Hardened, Immutable Artifacts

Chainguard OS produces container images that are minimal in scope, stripped of non-essential components, and hardened for secure use in production environments. The resulting artifacts are immutable and designed to include only the dependencies necessary for a given application to run.

Unlike traditional Linux distributions, which aim to be general-purpose and include a wide range of libraries and utilities, Chainguard OS builds _application systems_: minimal containers tailored to the specific runtime requirements of a single application. Optional complementary tools and packages can be added as needed, but they are not included by default.

This design reduces the system's overall attack surface, improves performance by eliminating unused software, and supports strict control over what is present in a given execution environment. All images are produced through hardened build processes and are validated against defined security policies.

## Delta Minimization

Chainguard OS maintains a close alignment with upstream open source projects. Extra patches are introduced only when necessary, such as for addressing critical issues or applying hardening measures, and are kept in place only until equivalent changes are integrated upstream.

This approach reduces long-term maintenance overhead and avoids divergence from upstream. Chainguard OS implements frequent, incremental updates (what we call [nano updates, discussed in the section above](/chainguard/chainguard-os/overview/#nano-updates-and-rebuilds)) that closely track upstream releases. These updates are designed to preserve the intent and behavior of the original software while delivering improvements and security fixes on an almost daily cadence.

By integrating changes continuously and aligning with upstream maintainers’ development cycles, Chainguard OS ensures compatibility and reduces the risk of regressions. This model also helps downstream consumers benefit from the most recent updates without requiring wholesale system upgrades.

## Advantages of Chainguard OS

Chainguard OS is a minimal Linux-based operating system designed to support more secure deployment of containerized applications. It integrates tightly with Chainguard tooling to provide measurable improvements in vulnerability management, compliance, and software supply chain integrity.

### Vulnerability Management
Chainguard OS minimizes exposure to known vulnerabilities by automating detection, triage, and remediation processes. It continuously rebuilds included applications and dependencies using up-to-date toolchains and a hardened image pipeline. The OS includes only essential packages, reducing the attack surface.

### Continuous Compliance
The system architecture and toolchain used in Chainguard OS support the automation of compliance efforts. By consistently regenerating software artifacts in a controlled environment, Chainguard OS ensures that applications and their dependencies remain compliant with common security and regulatory frameworks.

### Software Supply Chain Security
All software components in Chainguard OS are built from source in the [Chainguard Factory](https://www.youtube.com/watch?v=iU9hmW6hrGs) — a hardened build environment that conforms to [SLSA](https://slsa.dev/) standards. This process mitigates risks of tampering in the build and delivery pipeline. The system also generates cryptographically verifiable artifacts, including signed Software Bills of Materials ([SBOMs](/open-source/sbom/what-is-an-sbom/)) and provenance metadata.

### Operational Efficiency
By integrating upstream open source updates directly into the build and delivery process, Chainguard OS reduces the need for manual patching and vulnerability triage. Engineering teams can allocate resources toward feature development rather than maintenance overhead.

## System Architecture and Design Philosophy
Traditional Linux distributions often bundle a broad set of packages and features, which can introduce unnecessary complexity and security risk. Chainguard OS adopts a minimal and purpose-built approach, optimized for containerized environments.

The operating system is built to take advantage of modern containerization practices and supports declarative, reproducible builds. Combined with automated tooling, this design enables consistent delivery of secure, traceable container images.

Chainguard OS is not intended as a general-purpose distribution; instead, it serves as a foundational layer for secure application workloads, particularly in environments that require strict controls on software provenance, compliance, and runtime behavior.