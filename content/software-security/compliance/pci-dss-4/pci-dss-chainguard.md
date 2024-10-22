---
title: "Simplify Your Path to PCI DSS 4.0 Compliance with Chainguard"
description: "Chainguard Images reduce the time and effort for establishing PCI DSS 4.0 compliance"
lead: "Chainguard Images reduce the time and effort for establishing PCI DSS 4.0 compliance"
type: "article"
date: 2024-08-21T14:05:09+00:00
lastmod: 2024-08-21T14:05:09+00:00
contributors: []
draft: false
tags: ["compliance", "PCI DSS 4.0", "standards"]
images: []
menu:
  docs:
    parent: "pci-dss-4"
weight: 005
toc: true
---

Compliance with PCI DSS 4.0, or Payment Card Industry Data Security Standard, requires adherence to strong security standards. Rigorous requirements must be met in order to secure your networks, systems, storage, and access according to the guidelines.

Chainguard doesn't build images specifically for PCI DSS, but our images can help you meet the requirements in many ways, easing your burden in the process of achieving compliance. Securing your software supply chain provides a solid foundation for minimizing vulnerabilities.

All Chainguard Images save time and costs required to triage, patch, and remediate CVEs. They are created by and officially maintained by Chainguard engineers. Our images are designed to be minimal, removing unnecessary software that is not specifically used. This eliminates a number of potential attack vectors.

On top of this, you must authenticate into Chainguard to use Chainguard Images, giving you reassurance of the provenance of your images. They include digitally signed [build-time SBOMs](/chainguard/chainguard-images/working-with-images/retrieve-image-sboms/) (software bill of materials) documenting and attesting to the full provenance.

Our FIPS-compliant [Federal Information Processing Standard](../../../chainguard/chainguard-images/working-with-images/fips-images.md) images, combined with  STIG-hardened (Security Technical Implementation Guide) configurations, provide an even stronger foundation for meeting the requirements of PCI DSS even because they are hardened further to meet the more stringent FedRAMP requirements.


## What are STIG-Hardened FIPS Images?

STIG-hardened FIPS images are pre-configured container images that have been secured according to the Security Technical Implementation Guide (STIG) standards set by the Defense Information Systems Agency (DISA). These images meet stringent federal security requirements, combining FIPS-compliant encryption with robust security configurations that protect against vulnerabilities and threats. By using STIG-hardened FIPS images, organizations ensure that their systems adhere to federal encryption standards and best practices for cybersecurity, making them particularly valuable in environments that require high levels of security.

## How do Chainguard Images Help?

One of the main requirements of PCI DSS is to maintain a vulnerability management program. PCI DSS requires you to scan for vulnerabilites once every three months (Requirement 11.3.1) and triage and address all vulnerabilities (Requirement 11.3.11). Chainguard protects you from malicious attacks by supplying you with images where CVEs have already been dealt with, removing vulnerabilities for you.

PCI DCC requires that you catalog and classify vulnerabilities bespoke and third-party software (Requirements 6.3.1 and 6.3.2). You must fix all critical and high vulnerabilities and have a plan of action for the rest (Requirement 11.4.4). Chainguard does that for you.

Vulnerability scanners can be noisy and sifting through false positives while cataloging true vulnerabilities can be tedious work. Providing justifications for vulnerabilities that aren't applicable takes time, and that is after investigating them thoroughly.

Chainguard Images are carefully engineered to contain low-to-no CVEs. Organizations can use them as their source to build their applications on. The benefits of our solution are:

- **You’re secured by default** : Our Images contain low-to-no CVEs. Check out our I[mages Directory](https://images.chainguard.dev) yourself. ‍
- [**Extensive scanner partnerships**](https://www.chainguard.dev/scanners): We partner with the industry-leading scanners such as Snyk, Crowdstrike, and Wiz. ‍
- **SBOM for all Chainguard Images**: Get full transparency into the packages actually used in our images and ultimately run in your environment. ‍
- **Less ongoing human overhead**: Every new Chainguard Image version is carefully scanned and any addressable CVEs are fixed. ‍
-  **Trust in our industry leading [CVE SLA]**(https://www.chainguard.dev/cve-sla): We are committed to supplying secure software and commit to fixing CVEs so you don’t have to.


## Browse all CMMC 2.0 Articles

- [Introduction to PCI DSS 4.0](/software-security/compliance/pci-dss-4/intro-pci-dss-4/)
- [Overview of PCI DSS 4.0 Practices/Requirements](/software-security/compliance/pci-dss-4/pci-dss-practices/)
- (Current article) How Chainguard Can Help With CMMC 2.0


**[Get started with Chainguard FIPS Images today!](https://images.chainguard.dev/?category=fips?utm_source=docs)**