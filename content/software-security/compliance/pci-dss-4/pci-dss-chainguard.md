---
title: "Simplify Your Path to PCI DSS 4.0 Compliance with Chainguard"
description: "Chainguard Images reduce the time and effort for establishing PCI DSS 4.0 compliance"
lead: "Chainguard Images reduce the time and effort for establishing PCI DSS 4.0 compliance"
type: "article"
date: 2024-08-09T19:10:09+00:00
lastmod: 2024-08-15T19:10:09+00:00
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

Compliance with PCI DSS 4.0 requires adherence to strong security standards. Rigorous requirements must be met in order to secure your networks, systems, storage, and access according to the guidelines.

Chainguard doesn't build images specifically for PCI DSS, but our images can help you meet the requirements in many ways, easing your burden in the process of achieving compliance. Securing your software supply chain provides a solid foundation for minimizing vulnerabilities.

All Chainguard Images are created by and officially maintained by Chainguard engineers. They are designed to be minimal, removing unnecessary software that is not specifically used. This eliminates a number of potential attack vectors. On top of this, you must authenticate into Chainguard to use Chainguard Images, giving you reassurance of the provenance of your images. They include digitally signed [build-time SBOMs](/content/chainguard/chainguard-images/working-with-images/retrieve-image-sboms/) (software bill of materials) documenting and attesting to the full provenance.

Our FIPS-compliant (Federal Information Processing Standard) images, combined with  STIG-hardened (Security Technical Implementation Guide) configurations, provide an even stronger foundation for meeting the requirements of PCI DSS even because they are hardened further to meet the more stringent FedRAMP requirements.


## What are STIG-Hardened FIPS Images?

STIG-hardened FIPS images are pre-configured container images that have been secured according to the Security Technical Implementation Guide (STIG) standards set by the Defense Information Systems Agency (DISA). These images meet stringent federal security requirements, combining FIPS-compliant encryption with robust security configurations that protect against vulnerabilities and threats. By using STIG-hardened FIPS images, organizations ensure that their systems adhere to federal encryption standards and best practices for cybersecurity, making them particularly valuable in environments that require high levels of security.

## How do Chainguard Images Help?

This chart enumerates some of the ways that using Chainguard Images helps you achieve PCI DSS compliance:

| PCI DSS Goals | How Chainguard Images can help |
|-----------------------|------------------------|
| **Build and maintain a secure network and systems** | Use containers with hardened networking and intentionally-limited connectivity |
| **Protect account data** | Eliminate potential attack vectors that could be used to access your system and your data |
| **Maintain a vulnerability management program** | Protect yourself from malicious attacks by using images where CVEs have been dealt with, removing vulnerabilities |
| **Implement strong access control measures** | Restrict access to system components and to only authenticated users with permission to access and download Chainguard Images |
| **Maintain an information security policy** | Maintain and limit your security risk using images with known provenance |


## Browse all CMMC 2.0 Articles

- [Introduction to PCI DSS 4.0](/software-security/compliance/pci-dss-4/intro-pci-dss-4/)
- [Overview of PCI DSS 4.0 Practices/Requirements](/software-security/compliance/pci-dss-4/pci-dss-practices/)
- (Current article) How Chainguard Can Help With CMMC 2.0


**[Get started with Chainguard FIPS Images today!](https://images.chainguard.dev/?category=fips?utm_source=docs)**