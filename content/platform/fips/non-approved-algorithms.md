---
aliases:
- /chainguard/fips/non-approved-algorithms/
title: "FIPS and non-approved algorithms"
linktitle: "FIPS and non-approved algorithms"
type: "article"
description: "Technical deep-dive into Chainguard FIPS images access to non-approved algorithms such as MD5 and SHA1"
date: 2025-10-28T08:00:00+00:00
lastmod: 2026-09-01T16:56:22+00:00
draft: false
tags: ["FIPS", "MD5"]
images: []
weight: 040
toc: true
---

## Overview

FIPS cryptographic modules implement cryptographically strong protection of data at rest and in transit. NIST's position on this is very clear ([source](https://csrc.nist.gov/projects/cryptographic-module-validation-program)):

> Non-validated cryptography is viewed as providing no protection to the information or data — in effect the data would be considered unprotected plaintext. If the agency specifies that the information or data be cryptographically protected, then FIPS 140-2 or FIPS 140-3 is applicable. In essence, if cryptography is required, then it must be validated. Should the cryptographic module be revoked, use of that module is no longer permitted.

## NIST guidance on non-approved algorithm usage

As part of the FIPS collection of publications, NIST publishes [FIPS 140-3 Implementation Guidance](https://csrc.nist.gov/projects/cryptographic-module-validation-program/fips-140-3-ig-announcements) (FIPS 140 I.G.). The Cryptographic Module Validation Program (CMVP) requirements for the FIPS 140-3 include ISO standards, SP 800 series documents as well as the FIPS 140-3 I.G. The full set of documents and diagram are available from the [NIST Information Technology Laboratory Computer Security Resource Center](https://csrc.nist.gov/Projects/cryptographic-module-validation-program/fips-140-3-standards).

The FIPS 140-3 I.G. 2.4.A "Definition and Use of a non-Approved Security Function" is three pages long, and must be read in conjungtion with all other relevant NIST & ISO publications. It provides many examples, exceptions, and carve outs that at times let you use non-approved algorithms as part of higher level approved services. For example, some algorithms might not be safe to use directly, but with appropriate safeguards can be cryptographically secure. This is often the case with complex protocols such as TLS, which combines cryptographic primitives in a safe way.

Skipping to additional comments, let's focus on these statements (current edition, refer to the current [FIPS 140-3 I.G.](https://csrc.nist.gov/projects/cryptographic-module-validation-program/fips-140-3-ig-announcements) for any changes).

### FIPS 140-3 I.G. 2.4.A additional comment

The vendor must provide clear documentation and reasoning as to why the non-approved cryptographic algorithms can be used in an approved mode, that is, not being used to meet the requirements of FIPS 140-3 sections 6 and 7. It is at the discretion of the CMVP to determine if such usage of an algorithm fits within the guidance laid out in this implementation guidance (IG).

In addition, attempts to make use of this IG to include algorithms in the approved mode will not be accepted unless all of the following are met:

1) the algorithm is not used whatsoever to meet any FIPS 140-3 requirements;
1) the algorithm does not access or share CSPs in a way that counters the requirements of this IG;
1) the algorithm is either:
   1) not intended to be used as a security function (for example, interoperability or for memory wear leveling);
   1) redundant to an approved algorithm (such as double encryption);
   1) a cryptographic or mathematical operation applied for “good measure” but not for providing sound security (that is XORing a CSP with a secret value, using a proprietary algorithm, or using non-approved algorithms to obfuscate stored CSPs which are considered plaintext);
1) the algorithm’s non-approved use and purpose (from 3, above) is unambiguous to the operator and can’t be easily confused for a security function.

### Chainguard FIPS commitment

As documented in the [Chainguard FIPS commitment](https://www.chainguard.dev/legal/fips-commitment), our FIPS images enable only approved services and algorithms by default. This simplifies reasoning, audit and testing about what is or isn't a security function, since we are using only approved services. For example, Chainguard [gradle-fips](https://images.chainguard.dev/directory/image/gradle-fips/versions) has been modified to use an approved keystore to store build settings. While not a security function, this ensured that no unapproved keystore could leak into the build process and testing.

All cases of usage that might be related to a security function are also made to only use approved services. This includes but is not limited to:

* encryption / decryption
* digital signature creation and verification
* random number generation
* message authentication code
* key derivation functions
* key encapsulation methods
* key exchange

The one functionality that errs on the side of non-security function is calculating a digest alone, not part of MAC, HMAC, Merkle tree, integrity scheme, or digital signatures. Specifically, MD4, MD5, and SHA1 are universally deprecated and disallowed as part of security schemes, and yet they remain widely used for non-security functionality.

Examples of such non-security usage are:

* Webpack 4 uses MD4 to precompute perfect hashtables from trusted input at build time, refer to [this issue](https://github.com/webpack/webpack/issues/14560).
* Yarn, .ZIP, JAR, PDF require MD5 as part of the frozen fileformats they use
* Amazon S3 supports many algorithms for object integrity checking over trusted channel, including MD5 and SHA1, refer to [the official docs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity-upload.html). Many client implementations default to MD5.
* Google Cloud Storage can use CRC32C or MD5, and clients typically default to MD5 for object integrity during uploads [docs](https://docs.cloud.google.com/storage/docs/data-validation)
* RC4 primitives are used for obfuscating PDF files - no longer carrying any cryptographic protection, but required to open historical PDF documents
* AES-ECB insecure when used directly, but is used by QUIC and DTLSv1.3 protocols for non-security obfuscation of public information
* SHA-1 is still widely used for hash addressable content and lookup tables, for example `apk-tools` and git.

In all of the above use cases digest calculation does not provide any security functionality, it is meant to detect accidental corruption or improve speed. Overall, data is typically protected by SHA2-256 and is transmitted over a secure and authenticated TLS channel.

One alternative to migrating away from MD5 is to choose a specialist function explicitly designed for non-security purposes with significantly higher performance, such as [XXHASH](https://xxhash.com/). In most cases, non-security functionality should upgrade from CRC32C, MD5, SHA1 to XXHASH3.

However, if you need interoperability with existing formats and services *and* it is established that digest usage is for non-security purposes, you must use the insecure digests. Chainguard is integrating support for such use cases for MD5 and SHA1 across our FIPS images. Each language and application implementation is very different and specific, documented below.

Although SHA1 is currently approved, it is already deprecated by RFCs. NIST is deprecating SHA1 by 2030.  The implementations below are forward-looking and attempt to address access to MD5 today and SHA1 in the future.

SHA1 is available as approved in Chainguard FIPS Provider for OpenSSL versions 3.0.9, 3.1.2 and 3.4.0. It is non-approved starting in version 3.6.0. The below guidance will apply to SHA1 as well, likely beginning in 2027.

## Access to non-approved algorithms with Chainguard Legacy Approved provider for OpenSSL

Chainguard FIPS and non-FIPS images are configured to use a legacy provider that exposes the above mentioned algorithms for non-security purposes. At runtime one can choose to disable them with an environment variable `CHAINGUARD_LEGACY_APPROVED=0`. This provider enables all OpenSSL applications to uniformally access legacy algorithms for non-security purposes. They do remain blocked from being used inside the FIPS module boundary for security purposes such as protecting data at rest or in transit.

## All other projects

If you have queries about this guidance, or any other packages, projects, languages or ecosystems, in the feedback section on this page select "No" and please fill in feedback, or please [open a support ticket](https://support.chainguard.dev/).
