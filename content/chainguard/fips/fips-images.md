---
title: "Chainguard FIPS Containers"
linktitle: "FIPS Containers"
aliases: 
- /chainguard/chainguard-images/fips-images
- /chainguard/chainguard-images/images-features/fips-images
- /chainguard/chainguard-images/working-with-images/fips-images/
- /chainguard/chainguard-images/features/fips-images/
type: "article"
description: "Learn about Chainguard's FIPS-validated container images for federal compliance, featuring kernel-independent design and simplified deployment for FedRAMP and government requirements"
date: 2024-02-08T15:56:52-07:00
lastmod: 2025-07-23T15:09:59+00:00
draft: false
tags: ["Chainguard Containers", "FIPS"]
images: []
menu:
  docs:
    parent: "features"
weight: 020
toc: true
---

## What is FIPS?

[Federal Information Processing Standards](https://www.nist.gov/itl/publications-0/federal-information-processing-standards-fips) (FIPS) are standards developed by the National Institute of Standards and Technology (NIST) in accordance with the Federal Information Security Management Act (FISMA). FIPS compliance ensures that cryptographic security services within applications meet strict security and integrity standards, and are implemented and configured correctly.

Chainguard provides FIPS-validated container images to help organizations meet federal compliance requirements, including [FedRAMP](https://www.fedramp.gov/) and Department of Defense security frameworks. These FIPS-enabled containers feature a kernel-independent design that simplifies deployment while maintaining compliance.

## What To Expect from Chainguard FIPS Containers

Chainguard offers 400+ FIPS image variants covering language runtimes (Go, Java, Python, Node.js, .NET, PHP, C/C++), databases, web servers, and Kubernetes components. These images use NIST-validated cryptographic modules including the OpenSSL FIPS provider (CMVP Certificate [#4282](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4282)) and Bouncy Castle FIPS for Java.

All FIPS images include STIG hardening, daily builds with zero-to-minimal CVEs under SLA, and build-time SBOMs. Chainguard's warranties and certification details are on the [FIPS Commitment](https://www.chainguard.dev/legal/fips-commitment) page.

## Kernel-Independent FIPS Architecture

Traditionally, FIPS-compliant containers required the host kernel to be configured in FIPS mode to provide a validated entropy source. This limited deployment options and prevented testing on developer machines.

Chainguard FIPS Containers use a userspace entropy source (the Jitterentropy library with SP 800-90B validation) instead of relying on the kernel. This allows FIPS containers to run on any recent Linux kernel, including developer workstations, standard CI/CD environments, and cloud platforms like GKE, AWS Bottlerocket, and Azure Linux.

**Limitations**: Some workloads (certain Kubernetes CNI plugins, LUKS2 encryption, StrongSwan VPN) still require a kernel configured in FIPS mode. As of August 2025, Java-based FIPS images support kernel-independent operation.

For technical details, see [Kernel-Independent FIPS Containers](https://www.chainguard.dev/unchained/kernel-independent-fips-images).

## Using FIPS Containers

FIPS images are available for language runtimes (Go, Java, Node.js, Python, .NET, PHP), databases (PostgreSQL, Elasticsearch, Redis), web servers (nginx, HAProxy), Kubernetes components, and monitoring tools. View the complete catalog at [images.chainguard.dev/?category=fips](https://images.chainguard.dev/?category=fips).

All Chainguard FIPS Containers include [STIG hardening](/chainguard/chainguard-images/working-with-images/image-stigs/) in addition to FIPS validation. For images not currently available with FIPS, [contact Chainguard](https://www.chainguard.dev/contact) to discuss custom requirements.

## Additional Resources

- [FIPS Commitment](https://www.chainguard.dev/legal/fips-commitment) - Warranties and certifications
- [Frequently Asked Questions](/chainguard/fips/faqs/) - Common FIPS questions
- [OpenSSL FIPS module documentation](https://www.openssl.org/docs/manmaster/man7/fips_module.html)
- [Bouncy Castle FIPS Crypto package](https://www.bouncycastle.org/about/bouncy-castle-fips-faq/)

Chainguard FIPS Containers are not included in the free tier. To request access, [contact Chainguard](https://www.chainguard.dev/contact).

