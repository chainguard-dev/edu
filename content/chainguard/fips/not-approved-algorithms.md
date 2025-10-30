---
title: "FIPS and non-approved MD5"
linktitle: "FIPS and MD5"
type: "article"
description: "Technical deep-dive into Chainguard FIPS images access to non-approved algorithms such as MD5 and SHA1"
date: 2025-10-28T08:00:00+00:00
lastmod: 2025-10-28T08:00:00+00:00
draft: false
tags: ["FIPS", "MD5"]
images: []
weight: 040
toc: true
---

## Overview

FIPS cryptographic modules implement cryptographically strong protection of data at rest and in transit. The NIST position on this is very [clear](https://csrc.nist.gov/projects/cryptographic-module-validation-program):

> Non-validated cryptography is viewed as providing no protection to the information or data — in effect the data would be considered unprotected plaintext. If the agency specifies that the information or data be cryptographically protected, then FIPS 140-2 or FIPS 140-3 is applicable. In essence, if cryptography is required, then it must be validated. Should the cryptographic module be revoked, use of that module is no longer permitted.

## NIST guidance on non-approved algorithm usage

As part of FIPS collection of publications, NIST publishes [FIPS 140-3 Implementation Guidance](https://csrc.nist.gov/projects/cryptographic-module-validation-program/fips-140-3-ig-announcements) (FIPS 140 I.G.). The Cryptogrpahic Module Validation Programme (CMVP) requirements for the FIPS 140-3 include ISO standards, SP 800 series documents as well as the FIPS 140-3 I.G. The full set of documents and diagram are shown [here](https://csrc.nist.gov/Projects/cryptographic-module-validation-program/fips-140-3-standards).

The FIPS 140-3 I.G. 2.4.A "Definition and Use of a non-Approved Security Function" is three pages long, and must be read in conjungtion with all other relevant NIST & ISO publications. It provides many examples, exceptions and carve outs that at times let you use non-approved algorithms as part of higher level approved services. For example, some algorithms might not be safe to use directly, but with appropriate safeguards can be cryptographically secure. This is often the case with complex protocols such as TLS, which combines cryptographic primitives in a safe way.

Skipping to additional comments, let's focus on these statements (current edition, see the current [FIPS 140-3 I.G.](https://csrc.nist.gov/projects/cryptographic-module-validation-program/fips-140-3-ig-announcements) for any changes).

> The vendor must provide clear documentation and reasoning as to why the non-approved cryptographic algorithms can be used in an approved mode, i.e., not being used to meet the requirements of FIPS 140-3 sections 6 and 7. It is at the discretion of the CMVP to determine if such usage of an algorithm fits within the guidance laid out in this IG.

> In addition, attempts to make use of this IG to include algorithms in the approved mode will not be accepted unless all of the following are met:
> 1) the algorithm is not used whatsoever to meet any FIPS 140-3 requirements;
> 2) the algorithm does not access or share CSPs in a way that counters the requirements of this IG;
> 3) the algorithm is either:
>   i) not intended to be used as a security function (e.g. interoperability or for memory wear leveling);
>   ii) redundant to an approved algorithm (e.g. double encryption);
>   iii) a cryptographic or mathematical operation applied for “good measure” but not for providing sound security (e.g. XORing a CSP with a secret value, using a proprietary algorithm, or using non-approved algorithms to obfuscate stored CSPs which are considered plaintext);
> 4) the algorithm’s non-approved use and purpose (from 3) above) is unambiguous to the operator and can’t be easily confused for a security function.

As documented in the [Chainguard FIPS Commitment](https://www.chainguard.dev/legal/fips-commitment), our FIPS images enable only approved services and algorithms by default. This simplifies reasoning, audit and testing about what is or isn't a security function, if everything uses approved only services. For example, Chainguard [gradle-fips](https://www.chainguard.dev/legal/fips-commitment) has been modified to use an approved keystore to store build settings. It is not a security function, but it was easier to do that, than enable non-approved keystore usage which could then leak into the build process and testing.

All cases of usage that might be related to a security function also are made to use approved only services, this includes but not limited to:
* encryption / decryption
* digital signature creation and verfication
* random number generation
* message authentication code
* key derivation functions
* key encapsulation methods
* key exchange

The one functionality that errs on the side of non-security function is calculating a digest alone, not part of MAC, HMAC, merkle-tree, integrity scheme, or digital signatures. Specificaly, MD4, MD5, and SHA1 are universally deprecated and dissallowed as part of security schemes, and yet they remain widely used for non-security functionality.

Examples of such non-security usage are:
* Webpack 4 uses MD4 to precompute perfect hashtables from trusted input at build time [issue](https://github.com/webpack/webpack/issues/14560)
* Amazon S3 supports many algorithms for object integrity checking over trusted channel, including MD5 and SHA1 [docs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity-upload.html). Many client implementations default to MD5.
* Google Bucket storage can use CRC32C or MD5, and clients typically default to MD5 for object integrity during uploads [docs](https://docs.cloud.google.com/storage/docs/data-validation)
* PDF document identifiers require MD5 by standard, and no newer version of standards or documents exist [pull request](https://github.com/py-pdf/pypdf/pull/3438)

In all of the above use cases digest calculation does not provide any security functionality, it is meant to detect accidental corruption or provide speed ups. Overall, data is typically protected by SHA2-256 and is transmitted over a secure and authenticated TLS channel.

Note that using CRC32C or MD5 doesn't even provide performance gains, as specialist functions exist for non-security purposes with significantly higher performace, such as [XXHASH](https://xxhash.com/). In most cases, non-security functionality should upgrade from CRC32C, MD5, SHA1 to XXHASH3.

However, if you need interoperability with existing formats and services **and** it is established that digest usage is for non-security purposes, you must use the insecure digests. Chainguard is integrating support for such use cases for MD5 and SHA1 across our FIPS images. Each language and application implementation is very different and specific, documented below.

Although SHA1 is currently approved, it is already deprecated by RFCs and NIST is deprecating SHA1 by 2030, thus below implementations are forward looking and attempt to address access to MD5 today and SHA1 in the future.

SHA1 is available as approved in Chainguard FIPS Provider for OpenSSL versions 3.0.9, 3.1.2 and 3.4.0. It is non-approved starting in version 3.6.0. The below guidance will apply to SHA1 as well likely in 2027.

## Access to MD5 for non-security purposes

### OpenSSL FIPS and MD5

In Chainguard FIPS images, OpenSSL operates in approved only mode and has the default property query string set to `fips=yes` for all algorithms and services, such as message digests, HMAC, and so on.

MD5 is available as a non-approved service. You can request access to it on opt-in basis using a `?fips=yes` (prefer fips implementation if there is one, and fallback to a non-fips one) or `-fips` (disregard request for a fips implementation, and return any available one) property query strings via the C API or via command line options to calculate message digests. Usage of these digests in higher level algorithms is blocked. For example `openssl dgst` calculation is possible, yet `openssl dsgst -sign, -verify, -hmac` is blocked.

Examples:

```shell
$ echo chainguard | openssl dgst -md5
Error setting digest
801B3D417B7F0000:error:0308010C:digital envelope routines:inner_evp_generic_fetch:unsupported:crypto/evp/evp_fetch.c:375:Global default library context, Algorithm (MD5 : 89), Properties ()
801B3D417B7F0000:error:03000086:digital envelope routines:evp_md_init_internal:initialization error:crypto/evp/digest.c:271:
```

```shell
$ printf chainguard | openssl dgst -propquery '?fips=yes' -md5
MD5(stdin)= f8d689ee8221617c032b0e71f9c597ac
```

Note that calculating HMAC is still blocked:

```shell
$ printf chainguard | openssl dgst -propquery '?fips=yes' -md5 -hmac averylonghmackey
Error setting context
80AB9D605C7F0000:error:0308010C:digital envelope routines:inner_evp_generic_fetch:unsupported:crypto/evp/evp_fetch.c:341:FIPS internal library context, Algorithm (md5 : 0), Properties (<null>)
```

There are some caveats and bypasses, some digital signature algorithms allow signing raw data, or prehashed values. In such cases, one can out of band calculate MD5 hash, padded it according to PKCSv1.5 and RSA2048 modulus size and execute raw RSA signing operation. Such a service is non-approved, and is unable to know that it is abused to sign an MD5 hash instead of SHA256. Please don't do this (your FIPS auditors will make you change it). Higher level one shot EVP APIs typically accept a message to sign, and perform hashing and padding internally and correctly block creating MD5 signatures. This again highlights that FIPS is about consent, one has to try to use FIPS cryptography intentionally.

If there is C/C++ software that uses OpenSSL APIs and needs access to MD5 and doesn't support `-fips` property query string, please open a support request for Chainguard engineering to look into adding support.

### Python FIPS and MD5

The Python standard library has a keyword argument to specify using a digest for security purposes, see these [docs](https://docs.python.org/3/library/hashlib.html#hashlib.md5).

Here are examples:

```python
>>> import hashlib
>>> hashlib.md5(b"chainguard").hexdigest()
Traceback (most recent call last):
  File "<python-input-12>", line 1, in <module>
    hashlib.md5(b"chainguard").hexdigest()
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
_hashlib.UnsupportedDigestmodError: [digital envelope routines] unsupported
```

```python
>>> hashlib.md5(b"chainguard", usedforsecurity=False).hexdigest()
'f8d689ee8221617c032b0e71f9c597ac'
```

If this usage is needed in any of the imported libraries, you can use [mock](https://docs.python.org/3/library/unittest.mock.html#where-to-patch) techniques to patch the code to pass the correct argument.

Alternatively submit upstream fixes to correct the code. Here are some examples contributed by Chainguardians:
* Google Cloud Platform storage [pull request](https://github.com/googleapis/python-storage/pull/1522)
* PyPDF project [pull requst](https://github.com/py-pdf/pypdf/pull/3438)

If there are Python projects that need MD5 access in FIPS mode and currently do not use `usedforsecurity=False` please open a support request for Chainguard engineering to look into adding support.

### Python pyca/cryptography FIPS and MD5

If you are compiling pycryptography or installing it from PyPI, it may come with a vendored and statically linked copy of a cryptographic library and will not operate in FIPS mode. In such cases, all usage of it may be non-approved.

If you install pycryptography through [custom assembly](https://edu.chainguard.dev/chainguard/chainguard-images/features/ca-docs/custom-assembly/), it will be linked with Chainguard OpenSSL and will correctly enforce FIPS compliance and operating in approved mode.

### .NET FIPS and MD5

.NET upstream chooses to always fetch the MD5 algorithm with `-fips` property query string. To verify that MD5 is blocked for security purposes, you must test calcualting HMAC-MD5 or attempting to create or verify a digital signature with MD5.

See dotnet/runtime [source code](https://github.com/dotnet/runtime/blob/25800e6537cd47a0a0533fb63bb0fa60d600ec45/src/native/libs/System.Security.Cryptography.Native/pal_evp.c#L290).

### Go FIPS and MD5

MD5 was deprecated before the Go language was created. The MD5 implementation at [crypto/md5](https://pkg.go.dev/crypto/md5) states that it should not be used for security purposes.

Currently Chainguard offers two Go FIPS toolchains. Both of them are based on the [microsoft/go](https://github.com/microsoft/go) toolchain and use OpenSSL FIPS at runtime:

* The [go-fips](https://images.chainguard.dev/directory/image/go-fips/overview) image always allows MD5 usage.

* The [go-msft-fips](https://images.chainguard.dev/directory/image/go-msft-fips/overview) image always blocks MD5 usage.

There are a few codepaths in the Go standard library where MD5 is used for authentication. Chainguard is working to correctly block these, and unify the two toolchains into one.

### Java FIPS and MD5

Currently all Java FIPS implementations in Chainguard FIPS images are powered by BouncyCastle FIPS as a JAR on the module path. This currently requires loading Sun crypto provider which currently always allows MD5.

Chainguard is working on using jlink to integrate BouncyCastle FIPS into the runtime image, to eliminate the Sun dependency. Then it will be possible to control MD5 access with BouncyCastle specific security properties. This guidance will be updated when the situation changes.

If blocking behavior is required, ensure to request implementation from the `BCFIPS` provider, or check for `BCFIPS` provider, as it has higest priority in the `java.security` hardened configuration.

### Node FIPS and MD5

Currently under investigation.

### PostgreSQL and MD5

Currently under investigation.

## All other projects

If you have queries about this guidance, or any other packages, projects, languages or ecosystems, click "No" below and fill in feedback, or please open a support ticket.
