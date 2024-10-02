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

One of the primary requirements of federal compliance frameworks — including [FedRAMP](https://www.fedramp.gov/program-basics/) — is to use FIPS-validated cryptography. Chainguard offers FIPS-enabled versions of a number of its Images. This article provides a high-level overview of what FIPS is and how Chainguard's FIPS-enabled Images are built.


## What is FIPS?

The [Federal Information Processing Standards](https://www.nist.gov/itl/publications-0/federal-information-processing-standards-fips), or FIPS, is a set of standards vendors must adhere to when providing data processing services to the US and Canadian governments. FIPS was developed by the National Institute of Standards and Technology (NIST), an agency within the United States Department of Commerce. 

NIST has published a number of different FIPS standards. The FIPS standard that concerns Chainguard Images is the 140 series which specify requirements for cryptographic modules. Currently, there are two active FIPS 140 standards: FIPS 140-2 and 140-3. FIPS 140-2 is scheduled to expire on September 21, 2026 as the industry transitions to the newer 140-3 standard. 

## Chainguard FIPS Images

Chainguard's FIPS Images are not themselves validated. Instead, most of Chainguard's FIPS-ready Images ship with a validated redistribution of [OpenSSL's FIPS provider module](https://www.openssl.org/docs/manmaster/man7/fips_module.html). The exceptions include our Java-based Images, which is explained further at the end of this section.

Because standard OpenSSL is not validated for FIPS, the OpenSSL FIPS module was designed for compatibility with OpenSSL so that products using the OpenSSL API can be converted to use FIPS-validated cryptography. Specifically, version 3.0 of the OpenSSL FIPS module has been validated for FIPS 140-2. 

Chainguard submitted a request for [Cryptographic Module Validation Program (CMVP)](https://csrc.nist.gov/projects/cryptographic-module-validation-program) validation for our redistribution of OpenSSL’s FIPS provider module to NIST.  This submission to the CMVP allows Chainguard to redistribute a FIPS-validated module in Wolfi and Chainguard Images. As of this writing, this redistribution is derived from the OpenSSL 3.0.9 FIPS module sources.

By including this redistribution of the OpenSSL FIPS module, Chainguard is able to provide Images that use FIPS-validated cryptography until the official certificate comes through. You can find the submission status on [NIST’s Modules in Process list](https://csrc.nist.gov/Projects/cryptographic-module-validation-program/modules-in-process/Modules-In-Process-List). We also run tests on each of our FIPS Images to ensure the given application is configured with FIPS-validated cryptography end-to-end. Note that Chainguard's FIPS Images use these modules by default, so there aren't any build flags users need to enable to apply this feature.

Additionally, Chainguard is already prepared for the migration to FIPS 140-3 in the near future because we provide the OpenSSL 3.1 module required for certification. It is expected that the certification process for this module will begin in 2024.

### Regarding Java-based FIPS Images
As mentioned previously, Chainguard provides several FIPS-ready Images that are based on Java. However, this presents some challenges because Java applications generally don't leverage OpenSSL for cryptography and there isn't another cryptographic library serving as a widely-used standard for Java applications. For these reasons, Chainguard's Java-based Images instead ship with the [FIPS variant of the Bouncy Castle Crypto package](https://www.bouncycastle.org/about/bouncy-castle-fips-faq/), a Java implementation of cryptographic algorithms. 

Some Java applications may bundle their own cryptographic libraries at the application level. In these cases, Chainguard can only build a FIPS-enabled Image if the bundled libraries are FIPS-compliant or the applications in question support use with FIPS-compliant variants like Bouncy Castle's. Other Java applications do not bundle cryptographic libraries, instead relying on the bundled cryptography providers from the JRE.

If the underlying JRE/JDK on the host system is FIPS compliant, then theoretically, the application could also be considered FIPS compliant. However, without explicit support or documentation for FIPS compliance, there is no guarantee that the application will consistently use these FIPS-compliant features. You can refer to the [Java Cryptography Architecture documentation](https://docs.oracle.com/en/java/javase/21/security/java-cryptography-architecture-jca-reference-guide.html#GUID-2BCFDD85-D533-4E6C-8CE9-29990DEB0190) for more information.

The full FIPS compliance of a Java application and its related image depends heavily on the application itself, specifically how it is architected and what it supports.

## A note about FIPS compliance

To ensure your organization is FIPS compliant, you'll need to do more than just install the OpenSSL module. Your organization's software must also be correctly configured to use only approved cryptographic algorithms. 

In order to help customers ensure their applications are running in FIPS mode, Chainguard provides [`openssl-fips-test`](https://github.com/chainguard-dev/openssl-fips-test), a useful utility in our FIPS-enabled Images that allows you to verify that the OpenSSL FIPS module is properly installed and configured. When called, this utility will run a series of tests to make sure only the approved algorithms are active and will return an error if the FIPS module is not correctly configured.

Be aware that this tool can only detect whether or not OpenSSL is properly configured. This tool does not validate whether any other element in an overall delivered configuration is, or is not, FIPS 140-2/140-3 compliant. It only tests whether OpenSSL is properly configured and makes use of the FIPS module correctly. Any applications and languages must be built to use the [OpenSSL Cryptographic library](https://www.openssl.org/docs/man3.0/man7/crypto.html) (also known as `libcrypto`) in order for the OpenSSL FIPS configuration to be useful.

You will need to pay attention to how you deploy your Chainguard Images. For example, sometimes people configure installations via Helm in a way that copies an application from an image and deploys it, which would mean that you cannot ensure the code or configuration are unchanged and could put you into a state of non-compliance.


## Learn more

We encourage you to check our list of FIPS Images in the [Chainguard Images Directory](https://images.chainguard.dev/). After navigating to the directory, you can either click the **FIPS** tag in the left-hand sidebar menu to filter out any non-FIPS Images, or use the search function to find every Image with "fips" in its name. Additionally, we encourage you to check out the documentation for [the OpenSSL FIPS module](https://www.openssl.org/docs/manmaster/man7/fips_module.html) and the [Bouncy Castle FIPS Crypto package](https://www.bouncycastle.org/about/bouncy-castle-fips-faq/) to better understand how they work.

Chainguard's FIPS Images are not included in our free tier of Developer Images. If you'd like access to one or more of our FIPS-ready Images, please [contact us](https://www.chainguard.dev/contact?utm_source=docs).
