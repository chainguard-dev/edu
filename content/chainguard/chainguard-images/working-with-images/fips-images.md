---
title: "FIPS-enabled Chainguard Images"
linktitle: "FIPS Images"
aliases: 
- /chainguard/chainguard-images/fips-images
- /chainguard/chainguard-images/images-features/fips-images
type: "article"
description: "A conceptual overview of Chainguard's FIPS-enabled Images."
date: 2024-02-08T15:56:52-07:00
lastmod: 2024-02-08T15:56:52-07:00
draft: false
tags: ["IMAGES", "PRODUCT", "CONCEPTUAL"]
images: []
menu:
  docs:
    parent: "concepts"
weight: 050
toc: true
---

One of the primary requirements of federal compliance frameworks — including [FedRAMP](https://www.fedramp.gov/program-basics/) — is to use FIPS-validated cryptography. Chainguard offers FIPS-enabled versions of a number of its Images. This article provides a high-level overview of what FIPS is and what to expect from Chainguard’s FIPS-enabled Images.

[Federal Information Processing Standards](https://www.nist.gov/itl/publications-0/federal-information-processing-standards-fips) (FIPS) are publicly announced standards developed by the National Institute of Standards and Technology (NIST) in accordance with the Federal Information Security Management Act (FISMA) and approved by the Secretary of Commerce. FIPS compliance ensures that cryptographic security services within applications meet strict security and integrity standards, and are implemented and configured correctly.

‍Chainguard warranties the following with respect to Chainguard container images:

Chainguard’s FIPS Images available to be delivered in compliance with FIPS specifications are listed [here](https://images.chainguard.dev/?category=fips)  (each a "Chainguard FIPS Image"). Images will be made available in compliance with FIPS specifications provided a customer’s applicable order form designates the purchase of Chainguard FIPS images.

The Chainguard FIPS images contain FIPS-validated software cryptographic modules. Entropy must be provided as specified in its cryptographic policy. The cryptographic module may provide non-approved algorithms, which will result in operating in FIPS non-approved mode. The cryptographic FIPS modules currently provided are:

‍- OpenSSL FIPS Provider (CMVP [#4282](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4282))
- Bouncy Castle FIPS Java API (CMVP [#4743](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4743), CMVP [#4616](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4616))
- Chainguard CPU Time Jitter RNG Entropy Source (Entropy Certificate [#E191](https://csrc.nist.gov/projects/cryptographic-module-validation-program/entropy-validations/certificate/191))

These may be updated occasionally; for further information, contact <fips-contact@chainguard.dev>.

Additional guidance is available for specific images, like these:

- [go-fips](https://images.chainguard.dev/directory/image/go-fips/overview)
- [node-fips](https://images.chainguard.dev/directory/image/node-fips/overview)
- [jdk-fips](https://images.chainguard.dev/directory/image/jdk-fips/overview)

You can find more at: [https://images.chainguard.dev/?category=fips](https://images.chainguard.dev/?category=fips).

All of Chainguard's FIPS Images have [STIGs](/chainguard/chainguard-images/working-with-images/image-stigs/).

‍Chainguard will take commercially reasonable efforts to ensure applications utilize FIPS-validated cryptographic modules for any cryptographic operations, provided that the parties acknowledge and agree that certain behaviors or functionalities within such applications, which are beyond the direct control of Chainguard, may not fully adhere to FIPS requirements. In the event there are common vulnerabilities and exposures identified, the Chainguard SLA will apply.

‍If Customer requests an image not currently available as a Chainguard FIPS Image, Chainguard will use commercially reasonable efforts to determine if such request is feasible. For further information, contact <fips-contact@chainguard.dev>.

## Learn more

We encourage you to check our list of FIPS Images in the [Chainguard Images Directory](https://images.chainguard.dev/). After navigating to the directory, you can either click the **FIPS** tag in the left-hand sidebar menu to filter out any non-FIPS Images, or use the search function to find every Image with "fips" in its name. Additionally, we encourage you to check out the documentation for [the OpenSSL FIPS module](https://www.openssl.org/docs/manmaster/man7/fips_module.html) and the [Bouncy Castle FIPS Crypto package](https://www.bouncycastle.org/about/bouncy-castle-fips-faq/) to better understand how they work.

Chainguard's FIPS Images are not included in our free tier of Developer Images. If you'd like access to one or more of our FIPS-ready Images, please [contact us](https://www.chainguard.dev/contact?utm_source=docs).
