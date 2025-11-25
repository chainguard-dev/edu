---
title: "Verify that Chainguard FIPS Containers are Configured to Use FIPS Modules"
linktitle: "FIPS Verification"
description: "Learn how to verify that Chainguard FIPS Containers are properly configured to use various FIPS modules."
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

Chainguard offers hundreds of FIPS container image variants covering language runtimes (Go, Java, Python, Node.js, .NET, PHP, C/C++), databases, web servers, and Kubernetes components. These images use NIST-validated cryptographic modules including the OpenSSL FIPS provider, Bouncy Castle FIPS, and BoringCrypto. Refer to Chaingaurd's [FIPS Commitment](https://www.chainguard.dev/legal/fips-commitment) for a full list of the modules used in Chaingaurd FIPS Images, as well as their respective CMVP certificates and SBOM indicators.

This guide outlines how to verify that Chainguard's FIPS images are properly configured to use these FIPS modules.

## Why Verify FIPS Configuration?

FIPS (Federal Information Processing Standards) 140 is a U.S. government standard that specifies security requirements for cryptographic modules. Organizations in regulated industries—including federal agencies, defense contractors, healthcare organizations, and financial services—must verify that their containers are correctly using FIPS-validated modules to maintain compliance.

These verification steps help you:

- Confirm FIPS modules are active and operational
- Validate compliance for audit purposes
- Troubleshoot configuration issues
- Generate evidence for compliance documentation


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
	✓ Self-test KAT_Digest SHA1 ... passed.
	✓ Self-test KAT_Digest SHA2 ... passed.
	✓ Self-test KAT_Digest SHA3 ... passed.
	✓ Self-test KAT_Cipher AES_GCM ... passed.
	✓ Self-test KAT_Cipher AES_ECB_Decrypt ... passed.
	✓ Self-test Continuous_RNG_Test RNG ... passed.
	✓ Self-test KAT_Signature RSA ... passed.
	✓ Self-test KAT_Signature ECDSA ... passed.
	✓ Self-test KAT_Signature DSA ... passed.
	✓ Self-test KAT_KDF TLS13_KDF_EXTRACT ... passed.
	✓ Self-test KAT_KDF TLS13_KDF_EXPAND ... passed.
	✓ Self-test KAT_KDF TLS12_PRF ... passed.
	✓ Self-test KAT_KDF PBKDF2 ... passed.
	✓ Self-test KAT_KDF SSHKDF ... passed.
	✓ Self-test KAT_KDF KBKDF ... passed.
	✓ Self-test KAT_KDF HKDF ... passed.
	✓ Self-test KAT_KDF SSKDF ... passed.
	✓ Self-test KAT_KDF X963KDF ... passed.
	✓ Self-test KAT_KDF X942KDF ... passed.
	✓ Self-test DRBG HASH ... passed.
	✓ Self-test DRBG CTR ... passed.
	✓ Self-test DRBG HMAC ... passed.
	✓ Self-test KAT_KA DH ... passed.
	✓ Self-test KAT_KA ECDH ... passed.
	✓ Self-test KAT_AsymmetricCipher RSA_Encrypt ... passed.
	✓ Self-test KAT_AsymmetricCipher RSA_Decrypt ... passed.
	✓ Self-test KAT_AsymmetricCipher RSA_Decrypt ... passed.

	✓ 29 out of 29 self-tests passed.
	✓ Check FIPS cryptographic module is available... passed.
	✓ Check FIPS approved only mode (EVP_default_properties_is_fips_enabled)... passed.
	✓ Check non-approved algorithm blocked (HMAC-MD5)... passed.

Digests available for non-security use as per FIPS 140-3 I.G. 2.4.A (fips=no):
	✓  MD5
	✓  SHA1

Available approved algorithms for security purposes (fips=yes):
	✗ MD5
	✓ SHA-1
	✓ SHA-2
	✓ SHA-3
	✓ DSA
	✓ RSA
	✓ ECDSA
	✗ Ed25519
	✗ DetECDSA
	✗ ML-DSA
	✗ SLH-DSA
	✗ ML-KEM
	✗ X25519MLKEM768
	✗ SecP256r1MLKEM768

Public OpenSSL API (libssl.so & libcrypto.so):
	name:     	OpenSSL 3.6.0 1 Oct 2025
	version:  	3.6.0

FIPS cryptographic module provider details (fips.so):
	name:     	OpenSSL FIPS Provider
	version:  	3.1.2
	build:    	3.1.2

Locate applicable CMVP certificate(s) at: CMVP #4985
```

This output confirms that OpenSSL in the `python-fips` image is properly configured to use its FIPS module. 


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

Note that this example worked because the `jre-fips` image's entrypoint is `/usr/bin/java`, so it executes `java org.bouncycastle.entropy.util.DumpInfo` within the container. 

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


## Related Resources

- [Chainguard FIPS Images](https://images.chainguard.dev/directory?fips=true) - Browse all available FIPS-validated container images
- [NIST CMVP Certificate Search](https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search) - Verify cryptographic module certifications
- [OpenSSL FIPS Test Tool](https://github.com/chainguard-dev/openssl-fips-test) - Source code and documentation for the verification tool
