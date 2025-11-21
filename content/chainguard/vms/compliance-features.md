---
title: "Chainguard VMs Compliance Features"
linktitle: "Compliance"
description: "Learn about supported compliance features for Chainguard VMs"
type: "article"
date: 2025-11-20T08:04:00+00:00
lastmod: 2025-11-20T15:09:59+00:00
draft: false
tags: ["Chainguard VMs", "Compliance"]
menu:
  docs:
    parent: "vms"
weight: 005
toc: true
---

Chainguard VMs provide pre-hardened, audit-ready Linux virtual machine images designed for regulated and high-assurance environments (federal, defense, healthcare, financial services, and suppliers to those sectors). These images combine the following features:

| Feature                             | Description |
|:------------------------------------| :---- |
| **FIPS 140-3 validated cryptography**     | [NIST](https://www.nist.gov/) CMVP-validated software modules and [SP 800-90B](https://csrc.nist.gov/pubs/sp/800/90/b/final) compliant entropy, with runtime guardrails blocking non-FIPS crypto. |
| **STIG hardening**                  | Pre-configured to DISA [STIG](https://edu.chainguard.dev/chainguard/chainguard-images/features/image-stigs/) controls; delivered as production-ready images. |
| **CIS benchmark compliance**        | [CIS](https://www.cisecurity.org/cis-benchmarks/cis-benchmarks-faq) Level 1 hardened variants; hybrid STIG \+ CIS baseline. |
| **Secure Boot**                     | Secure Boot enabled by default across AWS, Azure, GCP, and on-prem. |
| **Compliance evidence & reporting** | FIPS certificates, OpenSSL docs, Security Content Automation Protocol (SCAP) scan results, and POA\&M-ready artifacts. |
| **CVE remediation SLA**             | 7 days for critical CVEs, 14 days for high, medium, and low. |

Chainguard FIPS 140-3 validated and hardened VM images serve as ready-to-use replacements for standard operating systems across AWS, Azure, and GCP, allowing organizations to maintain existing infrastructure and workflows while achieving immediate compliance. This guide outlines the compliance features of Chainguard VMs and how they can help reduce engineering toil for your organization.

## FIPS 140-3 Validated Cryptography

Chainguard VMs include FIPS 140-3 validated software cryptographic modules, backed by a NIST Cryptographic Module Validation Program (CMVP) certificate.

* **Validated modules**
    * Cryptographic modules are validated under FIPS 140-3 and integrated directly into the base image.
    * The images contain SP 800-90B compliant entropy sources for strong, standards-aligned randomness.
* **Runtime guardrails**
    * Guardrails prevent the use of non-FIPS-approved cryptography at runtime (for example, enforcing FIPS-approved ciphers and modes only).
* **Documentation for auditors**
    * FIPS integration documentation, including OpenSSL certificates and details on module configuration, is shipped as part of the deliverables to streamline audit review and ATO packages.

This setup allows teams to consume an OS image that is already FIPS-conformant at the platform layer rather than building and validating crypto modules in-house.

## STIG Hardening

Chainguard VMs provide variants hardened to DISA Security Technical Implementation Guide (STIG) requirements which are used across U.S. federal and defense environments.

* 2000+ relevant system controls are pre-configured and validated in the image, not delivered as a checklist that the customer must implement.
* Images are designed as ready-to-use replacements for existing Linux OS images, enabling STIG-compliant baselines without re-architecting existing infrastructure.

Chainguard can also provide SCAP scan outputs aligned with STIG requirements, helping teams demonstrate compliance with control requirements during audits.

## CIS Benchmark Compliance

For organizations standardizing on CIS controls, Chainguard offers images hardened to **CIS Level 1** benchmarks. Chainguard VMs use a hybrid baseline combining CIS L1 benchmarks with STIG requirements and industry-recognized secure defaults to provide defense-in-depth hardening.

This allows security and Governance, Risk, and Compliance teams to map infrastructure posture to both internal CIS-based policies and external STIG-based requirements without maintaining parallel baselines.

## Secure Boot

All Chainguard VM images support **Secure Boot enabled by default** across:

* AWS
* Microsoft Azure
* Google Cloud Platform
* On-premises platforms supporting Secure Boot

Secure Boot ensures only cryptographically signed and trusted components participate in the boot chain, preventing tampering with early-boot components such as the bootloader and kernel.

## Compliance Evidence and Reporting

Chainguard VMs are designed to simplify the generation of compliance artifacts often required in audits, ATO processes, and customer security reviews.

Available artifacts include:

* FIPS module documentation and integration details, including OpenSSL certificate documentation.
* SCAP/OpenSCAP scan results for STIG and CIS benchmarks.
* Plans of Action and Milestones (POA\&M) to support risk tracking and remediation planning.

By shipping this evidence with the images, Chainguard significantly shortens the time required to build audit packages and meet regulatory reporting needs.

## Vulnerability Management and Lifecycle

Chainguard VMs are built and maintained with an explicit [**CVE remediation SLA**](https://www.chainguard.dev/legal/cve-policy):

* **Critical CVEs**: patched within **7 days**
* **High, medium, and low CVEs**: patched within **14 days**

Chainguard VM images are updated regularly and made available to customers within these SLA windows, leaving them with a minimal, hardened footprint which reduces the volume of installed software and minimizes the attack surface. This leaves customers with a much smaller and more manageable CVE count.

This lifecycle management shifts ongoing compliance from a perpetual engineering project to a managed image-consumption model.
