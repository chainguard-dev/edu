---
title: "Chainguard FIPS Containers"
linktitle: "FIPS Containers"
aliases: 
- /chainguard/chainguard-images/fips-images
- /chainguard/chainguard-images/images-features/fips-images
- /chainguard/chainguard-images/working-with-images/fips-images/
- /chainguard/chainguard-images/features/fips-images/
type: "article"
description: "A conceptual overview of Chainguard FIPS Containers."
date: 2024-02-08T15:56:52-07:00
lastmod: 2025-05-24T09:58:00+00:00
draft: false
tags: ["Chainguard Containers", "Product", "FIPS"]
images: []
menu:
  docs:
    parent: "features"
weight: 005
toc: true
---

## What is FIPS? 
One of the primary requirements of federal compliance frameworks — including [FedRAMP](https://www.fedramp.gov/) — is to use FIPS-validated cryptography. To help customers meet these requirements, Chainguard offers FIPS-enabled versions of many images. This article provides a high-level overview of what FIPS is, what to expect from Chainguard FIPS Containers, featuring a kernel-independent design, and how Chainguard FIPS images stand out from alternatives.


[Federal Information Processing Standards](https://www.nist.gov/itl/publications-0/federal-information-processing-standards-fips) (FIPS) are publicly announced standards developed by the National Institute of Standards and Technology (NIST) in accordance with the Federal Information Security Management Act (FISMA) and approved by the Secretary of Commerce. FIPS compliance ensures that cryptographic security services within applications meet strict security and integrity standards, and are implemented and configured correctly.

## What To Expect from Chainguard FIPS Containers

‍Chainguard warranties are listed on the [FIPS Commitment](https://www.chainguard.dev/legal/fips-commitment) page. It also includes tables of relevant certifications as well as SBOM indicators of package names and versions.

## Chainguard Kernel-Independent FIPS Containers

Cryptographic protection relies on the secure implementation of a trusted algorithm and a random bit generator that cannot be reasonably predicted at any greater accuracy than random chance. Traditionally, to achieve this compliance requirement, developers were required to provision dedicated hardware and VMs with the host kernel configured in FIPS mode. This is because containers historically accessed the entropy source provided by a certified kernel. In cloud native or shared environments, this requirement significantly increased operational complexity by forcing a dependence on a limited set of FIPS-enabled kernels. 

Chainguard FIPS Containers remove this friction with a novel design that replaces a kernel entropy source with a userspace one. This implementation enables developers to deploy FIPS workloads using any of the latest kernels, hardware, and instance types. Chainguard FIPS Containers thus unlock the ability to run FIPS workloads on developer machines, existing CI/CD deployments, and even on readily available non-FIPS managed cloud offerings. All this can be done using the latest userspace runtimes like NodeJS, Python, Go, PHP, .NET, and C/C++, among others. Under Chainguard’s novel design, the container image for a given FIPS application can be entirely self-contained, minimal, and distroless.

Note: There are some workloads that require a kernel SP 800-90B entropy source or a kernel FIPS module. These include but are not limited to Chainguard FIPS container images shipping Java, k8s CNI plugins, LUKS2 full-disk encryption, and StrongSwan VPN. These use cases will continue to require a kernel in FIPS mode.

Read our full blog about [Chainguard's Kernel-Independent FIPS Containers](https://www.chainguard.dev/unchained/kernel-independent-fips-images).

## Developer Guidance for Available FIPS Containers

Additional guidance is available for specific container images, like these:

- [go-fips](https://images.chainguard.dev/directory/image/go-fips/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-working-with-images-fips-images)
- [node-fips](https://images.chainguard.dev/directory/image/node-fips/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-working-with-images-fips-images)
- [jdk-fips](https://images.chainguard.dev/directory/image/jdk-fips/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-working-with-images-fips-images)

You can find a full list Chainguard FIPS Containers at: [https://images.chainguard.dev/?category=fips](https://images.chainguard.dev/?category=fips).

All of Chainguard's FIPS Containers have [STIGs](/chainguard/chainguard-images/working-with-images/image-stigs/).

‍Chainguard will take commercially reasonable efforts to ensure applications utilize FIPS-validated cryptographic modules for any cryptographic operations, provided that the parties acknowledge and agree that certain behaviors or functionalities within such applications, which are beyond the direct control of Chainguard, may not fully adhere to FIPS requirements. In the event there are common vulnerabilities and exposures identified, the Chainguard SLA will apply.

‍If Customer requests an image not currently available as a Chainguard FIPS Container, Chainguard will use commercially reasonable efforts to determine if such request is feasible. For further information, contact <fips-contact@chainguard.dev>.

## Learn more

We encourage you to check our list of FIPS Containers in the [Chainguard Containers Directory](https://images.chainguard.dev/?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-working-with-images-fips-images). After navigating to the directory, you can either click the **FIPS** tag in the left-hand sidebar menu to filter out any non-FIPS Containers, or use the search function to find every container image with "fips" in its name. Additionally, we encourage you to check out the documentation for [the OpenSSL FIPS module](https://www.openssl.org/docs/manmaster/man7/fips_module.html) and the [Bouncy Castle FIPS Crypto package](https://www.bouncycastle.org/about/bouncy-castle-fips-faq/) to better understand how they work.

Chainguard's FIPS Containers are not included in our free tier of Starter container images. If you'd like access to one or more of our FIPS-ready container images, please [contact us](https://www.chainguard.dev/contact?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement).

