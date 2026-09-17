---
aliases:
- /chainguard/fips/verify-fips/
title: "Verify that Chainguard FIPS containers are configured to use FIPS modules"
linktitle: "FIPS verification"
description: "Learn how to verify that Chainguard FIPS containers are properly configured to use various FIPS modules."
type: "article"
date: 2025-11-23T08:04:00+00:00
lastmod: 2025-11-23T15:09:59+00:00
draft: false
tags: ["FIPS", "Chainguard Containers", "Reference"]
menu:
  docs:
    parent: "fips"
weight: 045
toc: true
---

Chainguard offers hundreds of FIPS container image variants covering language runtimes (Go, Java, Python, Node.js, .NET, PHP, C/C++), databases, web servers, and Kubernetes components. These images use NIST-validated cryptographic modules including the OpenSSL FIPS provider, Bouncy Castle FIPS, and BoringCrypto. Refer to Chainguard's [FIPS Commitment](https://www.chainguard.dev/legal/fips-commitment) for a full list of the modules used in Chainguard FIPS Images, as well as their respective CMVP certificates and SBOM indicators.

This guide outlines how to verify that Chainguard's FIPS images are properly configured to use these FIPS modules.

## Why verify FIPS configuration?

FIPS (Federal Information Processing Standards) 140 is a U.S. government standard that specifies security requirements for cryptographic modules. Organizations in regulated industries—including federal agencies, defense contractors, healthcare organizations, and financial services—must verify that their containers are correctly using FIPS-validated modules to maintain compliance.

These verification steps help you:

- Confirm FIPS modules are active and operational
- Validate compliance for audit purposes
- Troubleshoot configuration issues
- Generate evidence for compliance documentation

## SBOM indicators

Container images include packages with `NIST-` prefix indicating applicable certification. These also provide URLs to the certificates in the APK database and the SPDX SBOM. The following prefixes are in use:

- `NIST-CMVP-5132` indicates a validated cryptoprographic module with the certificate [#5132](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/5132)
- `NIST-ESV-191` indicates a validated entropy source with the certificate [#E191](https://csrc.nist.gov/projects/cryptographic-module-validation-program/entropy-validations/certificate/191)
- `NIST-CMVP-5523-optin` indicates a validated optional cryptographic module with the certificate [#5523](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/5132) that can be opted into at runtime.
- `NIST-CMVP-4743-UPDATE` indicates a non-validated module that is expected to be submitted to NIST for an update. See [FedRAMP](https://www.fedramp.gov/2026/reference/cryptographic-module-use/) documentation for more information.
- `NIST-MIP-module-name` indicates a non-validated submitted module only available in fips-mip images showcasing [Modules in process](https://csrc.nist.gov/projects/cryptographic-module-validation-program/modules-in-process/modules-in-process-list) containing future FIPS module development

## OpenSSL

Because most software relies on OpenSSL for cryptographic operations, all of Chainguard's FIPS container images ship OpenSSL in FIPS mode.

You can verify whether OpenSSL is properly configured to use its FIPS module with [the `openssl-fips-test` tool](https://github.com/chainguard-dev/openssl-fips-test). This tool, developed by Chainguard and included in all of our FIPS container images, prints the public API version, the FIPS module version, and the executed self tests.

When run on a system using the OpenSSL Project FIPS provider, `openssl-fips-test` returns a summary of available algorithms, which is useful to compare different CMVP modules and the algorithms they offer. It also retrieves FIPS module information and returns a CMVP search URL where one can find applicable certificates.

You can use the `openssl-fips-test` tool to check whether any Chainguard Container is properly configured to use its FIPS module with a command like the following. Be sure to replace `$ORGANIZATION` with the name of your own organization and [`python-fips`](https://images.chainguard.dev/directory/image/python-fips/overview) with any FIPS image your organization has access to:

```shell
docker run -it --entrypoint openssl-fips-test cgr.dev/$ORGANIZATION/python-fips
```

```output
Checking OpenSSL lifecycle assurance.

    ✓ Self-test KAT_Integrity HMAC ... passed.
    ✓ Self-test Module_Integrity HMAC ... passed.
    ✓ Self-test KAT_Digest SHA2 ... passed.
    ✓ Self-test KAT_Digest SHA3 ... passed.
    ✓ Self-test KAT_Cipher AES_GCM ... passed.
    ✓ Self-test KAT_Cipher AES_ECB_Decrypt ... passed.
    ✓ Self-test KAT_Signature RSA ... passed.
    ✓ Self-test KAT_Signature ECDSA ... passed.
    ✓ Self-test KAT_Signature DetECDSA ... passed.
    ✓ Self-test KAT_Signature EDDSA ... passed.
    ✓ Self-test KAT_Signature EDDSA ... passed.
    ✓ Self-test KAT_Signature ML-DSA ... passed.
    ✓ Self-test KAT_Signature SLH-DSA ... passed.
    ✓ Self-test KAT_Signature SLH-DSA ... passed.
    ✓ Self-test KAT_KDF TLS13_KDF_EXTRACT ... passed.
    ✓ Self-test KAT_KDF TLS13_KDF_EXPAND ... passed.
    ✓ Self-test KAT_KDF TLS12_PRF ... passed.
    ✓ Self-test KAT_KDF PBKDF2 ... passed.
    ✓ Self-test KAT_KDF KBKDF ... passed.
    ✓ Self-test KAT_KDF KBKDF_KMAC ... passed.
    ✓ Self-test KAT_KDF HKDF ... passed.
    ✓ Self-test KAT_KDF SSKDF ... passed.
    ✓ Self-test KAT_KDF X963KDF ... passed.
    ✓ Self-test KAT_KDF X942KDF ... passed.
    ✓ Self-test DRBG HASH ... passed.
    ✓ Self-test DRBG CTR ... passed.
    ✓ Self-test DRBG HMAC ... passed.
    ✓ Self-test KAT_KA DH ... passed.
    ✓ Self-test KAT_KA ECDH ... passed.
    ✓ Self-test KAT_AsymmetricKeyGeneration ML-KEM ... passed.
    ✓ Self-test KAT_AsymmetricKeyGeneration ML-DSA ... passed.
    ✓ Self-test KAT_AsymmetricKeyGeneration SLH-DSA ... passed.
    ✓ Self-test KAT_KEM KEM_Encap ... passed.
    ✓ Self-test KAT_KEM KEM_Decap ... passed.
    ✓ Self-test KAT_KEM KEM_Decap_Reject ... passed.

    ✓ 35 out of 35 self-tests passed.
    ✓ Check FIPS cryptographic module is available... passed.
    ✓ Check FIPS approved only mode (EVP_default_properties_is_fips_enabled)... passed.
    ✓ Check non-approved algorithm blocked (HMAC-MD5)... passed.

Digests available for non-security use as per FIPS 140-3 I.G. 2.4.A (fips=no):
    ✓ MD5
    ✓ SHA1

Available approved algorithms for security purposes (provider=fips,fips=yes):
    ✗ MD5
    ✗ SHA-1
    ✓ SHA-2
    ✓ SHA-3
    ✗ DSA
    ✓ RSA
    ✓ ECDSA
    ✓ Ed25519
    ✓ DetECDSA
    ✓ ML-DSA
    ✓ SLH-DSA
    ✓ ML-KEM
    ✓ X25519MLKEM768
    ✓ SecP256r1MLKEM768
    ✓ SecP384r1MLKEM1024

Public OpenSSL API (libssl.so & libcrypto.so):
    name:       OpenSSL 3.6.4 25 Aug 2026
    version:    3.6.4

FIPS cryptographic module provider details (fips.so):
    name:       Chainguard FIPS Provider for OpenSSL
    version:    3.6.0
    build:      3.6.0-r4

Locate applicable certificate(s) at: CMVP #5523 (with entropy #E191)

Lifecycle assurance satisfied.
```

This output confirms that OpenSSL in the `python-fips` image is properly configured to use its FIPS module.

### OpenSSL FIPS 140-3 enforcement quick checks

[NIST SP 800-131A](https://csrc.nist.gov/pubs/sp/800/131/a/r2/final) requires HMAC to use approved digest and keys of at least 112 bits long (14 characters) for security purposes.

Success scenario is HMAC with a 14 characters long key and a SHA256 digest:

```sh
openssl mac -macopt key:14charslongkey -macopt digest:sha256 -in /dev/null HMAC
```

```output
0DB994567D50545AC5A44823F82AAE06B1A21B99F8DD0A42B3D572B1AF62F182
```

Negative test is HMAC with a short key, and a SHA256 digest:

```sh
# openssl mac -macopt key:shortkey -macopt digest:sha256 -in /dev/null HMAC
MAC parameter error
801B86DD147F0000:error:1C800069:Provider routines:hmac_setkey:invalid key length:providers/implementations/macs/hmac_prov.c:173:
```

Cryptographically insecure digests are also rejected:

```sh
# openssl mac -macopt key:14charslongkey -macopt digest:md5 -in /dev/null HMAC
MAC parameter error
808B8049E17F0000:error:0308010C:digital envelope routines:inner_evp_generic_fetch:unsupported:crypto/evp/evp_fetch.c:355:FIPS internal library context, Algorithm (md5 : 0), Properties (<null>)
```

The above checks can also be performed in other programming languages for images that systems that use OpenSSL to power FIPS cryptography, for example python, node, php, perl and similar.

In non-fips images, all of the above commands are successful.

### OpenSSL FIPS 140-3 tamper test

Cryptographic modules are required to perform startup self-tests, and
must enter error state and stop all cryptoraphic services upon
failure. One of the startup self-tests is intergity check of the
cryptographic module itself. To observe this one can tamper with the
fips.so module itself, or tamper with the expected module HMAC value.

```sh
echo 'module-mac = 00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00' >> /etc/ssl/fipsmodule.cnf
```

After tampering with the module integrity mac:

```output
# openssl-fips-test
Checking OpenSSL lifecycle assurance.

    ✓ Self-test KAT_Integrity HMAC ... passed.
    ✗ Self-test Module_Integrity HMAC ... FAILED.
    ✗ Check FIPS cryptographic module is available... FAILED.
    ✓ Check FIPS approved only mode (EVP_default_properties_is_fips_enabled)... passed.
    ✓ Check non-approved algorithm blocked (HMAC-MD5)... passed.

Failed to retrieve cryptographic module version information
```

And previously approved and successful operations now fail, for example HMAC with a long key and SHA2 fails, when the fips module integrity check has been tampered with:

```
# openssl mac -macopt key:14charslongkey -macopt digest:sha256 -in /dev/null HMAC
Invalid MAC name HMAC
mac: Use -help for summary.
80DB6818FB7F0000:error:0308010C:digital envelope routines:inner_evp_generic_fetch:unsupported:crypto/evp/evp_fetch.c:376:Global default library context, Algorithm (HMAC : 0), Properties (<null>)
```

If application continues to operate, even when the fips module has been tampered with or removed, this indicates that the given application and algorithms have stopped using the FIPS module, are not using OpenSSL, or have fallbacks. For example, applications might preffer OpenSSL when it is operation, but have fallbacks to other libraries or have statically compiled alternative implementations of algorithms.

### Opt in to different FIPS provider versions

Images that contain `NIST-CMVP-5523-optin` or `NIST-CMVP-5132-optin`
SBOM indicator packages offer ability to switch between different
versions of validated CMVP modules at runtime.

- `NIST-CMVP-5523-optin` enables opt-into Chainguard v3.6 module with `OPENSSL_CONF_INCLUDE=/etc/ssl-3.6.0` environment variable
- `NIST-CMVP-5132-optin` enables opt-into Chainguard v3.4 module with `OPENSSL_CONF_INCLUDE=/etc/ssl-3.4.0` environment variable

For example:

```sh
export OPENSSL_CONF_INCLUDE=/etc/ssl-3.6.0
```

```output
export OPENSSL_CONF_INCLUDE=/etc/ssl-3.6.0
openssl-fips-test
...
FIPS cryptographic module provider details (fips.so):
    name:       Chainguard FIPS Provider for OpenSSL
    version:    3.6.0
    build:      3.6.0-r4
```

```sh
export OPENSSL_CONF_INCLUDE=/etc/ssl-3.4.0
```

```output
export OPENSSL_CONF_INCLUDE=/etc/ssl-3.4.0
openssl-fips-test
...
FIPS cryptographic module provider details (fips.so):
    name:       Chainguard FIPS Provider for OpenSSL
    version:    3.4.0
    build:      3.4.0-r5
```

## Bouncy Castle FIPS Java API

All of Chainguard's Java FIPS images support FIPS 140-3 compliance using Bouncy Castle FIPS cryptographic modules.

To verify whether Bouncy Castle FIPS is operating correctly, you can execute its `DumpInfo` command. The following example shows how you can do this with the [`jre-fips`](https://images.chainguard.dev/directory/image/jre-fips/overview) container image:

```shell
docker run -it --rm cgr.dev/$ORGANIZATION/jre-fips org.bouncycastle.util.DumpInfo
```

```output
Version Info: BouncyCastle Security Provider (FIPS edition) v2.1.1
FIPS Ready Status: READY
Native Ready Status: READY
Native Variant: vaesf
Native Build Date: 2024-11-15T15:56:42
Native Support: AES/CBC AES/CFB AES/CTR AES/ECB AES/GCM DRBG NRBG SHA2
Module SHA-256 HMAC: …
```

Note that this example worked because the `jre-fips` image's entrypoint is `/usr/bin/java`, so it executes `java org.bouncycastle.util.DumpInfo` within the container.

> **Note:** You can find a Chainguard container image's entrypoint in its [**Specifications** tab](https://images.chainguard.dev/directory/image/jre-fips/specifications) within the Containers Directory.

## BoringCrypto

Some of Chainguard's FIPS container images — including [`envoy-fips`](https://images.chainguard.dev/directory/image/envoy-fips/overview) and others that ship `envoy-fips` forks — use [BoringCrypto](https://boringssl.googlesource.com/boringssl/+/master/crypto/fipsmodule/FIPS.md), Google's fork of OpenSSL.

Chainguard FIPS images that use BoringCrypto list the version of the module in use in their `version` output:

```shell
docker run -it --rm cgr.dev/$ORGANIZATION/envoy-fips --version
```

```output
envoy  version: dc2d3098ae5641555f15c71d5bb5ce0060a8015c/1.36.2/Modified/RELEASE/BoringSSL-FIPS-2023042800
```

You can contrast this with the `version` output of the standard, non-FIPS `envoy` image:

```shell
docker run -it --rm cgr.dev/$ORGANIZATION/envoy --version
```

```output
envoy  version: dc2d3098ae5641555f15c71d5bb5ce0060a8015c/1.36.2/Modified/RELEASE/BoringSSL
```

This output shows that although it still uses BoringSSL, the non-FIPS `envoy` container image doesn't use the FIPS-enabled BoringSSL module.

Chainguard also ships the `envoy-fips` container image with `bssl-test_fips`. This tool prints useful information, including whether FIPS mode is on and which version of the module is in use:

```shell
docker run -it --rm --entrypoint /usr/bin/bssl-test_fips cgr.dev/$ORGANIZATION/envoy-fips
```

```output
Module version: 2023042800
About to AES-CBC encrypt . . .
  got . . .
About to AES-CBC decrypt . . .
  got . . .
About to AES-GCM seal . . .
  got . . .
About to AES-GCM open . . .
  got . . .
About to 3DES-CBC encrypt . . .
  got . . .
About to 3DES-CBC decrypt . . .
  got . . .
About to SHA-1 hash . . .
  got . . .
About to SHA-256 hash . . .
  got . . .
About to SHA-512 hash . . .
  got . . .
About to generate RSA key
About to RSA sign . . .
  got . . .
About to RSA verify . . .
About to generate P-256 key
About to compute key-agreement Z with P-256:
  got . . .
About to ECDSA sign . . .
About to seed CTR-DRBG with . . .
  generated . . .
About to run HKDF
  got . . .
About to run TLS v1.0 KDF
  got . . .
About to run TLS v1.2 KDF
  got . . .
About to run TLS v1.3 KDF
  got . . .
About to compute FFDH key-agreement:
  got . . .
PASS
```

## Troubleshooting

If verification checks fail, consider these common issues:

- **OpenSSL not in FIPS mode**: Ensure you're using a `-fips` tagged image variant
- **Missing FIPS configuration**: Check that the `OPENSSL_CONF` environment variable is set correctly
- **Module integrity failures**: Re-pull the container image to ensure it hasn't been modified
- **Incorrect image variant**: Verify you're using the FIPS variant of the image (e.g., `python-fips` not `python`)

For additional support, contact Chainguard support or consult the FIPS documentation.

## Related resources

- [Chainguard FIPS Images](https://images.chainguard.dev/directory?fips=true) - Browse all available FIPS-validated container images
- [NIST CMVP Certificate Search](https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search) - Verify cryptographic module certifications
- [OpenSSL FIPS Test Tool](https://github.com/chainguard-dev/openssl-fips-test) - Source code and documentation for the verification tool
