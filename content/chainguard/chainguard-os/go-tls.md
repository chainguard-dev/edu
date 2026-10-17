---
title: "Go TLS Configuration"
lead: ""
description: "Go TLS Configuration"
type: "article"
date: 2026-09-10T00:48:23+00:00
lastmod: 2026-09-28T14:00:04+00:00
draft: false
weight: 41
menu:
  docs:
    parent: "chainguard-os"
    identifier: "Go TLS Configuration"
toc: true
table_layout: auto
---

This is a summary of available algorithms in Go upstream TLS configuration,
and the Chainguard Hardening changes to these.

Chainguard hardened TLS removes non-default, legacy, and deprecated
algorithms to align with the [Chainguard Hardened OpenSSL](https://edu.chainguard.dev/chainguard/chainguard-os/openssl-4.0/) configuration.
Everything it removes was already disabled by default in upstream Go, so
default configurations don't use any of it, and all of it has already been
removed from Chainguard Hardened OpenSSL.

- **Go 1.27**: Chainguard builds offer hardened TLS as an opt-in. Without
  opting in, they behave like upstream Go 1.27.
- **Go 1.28**: Chainguard builds support only hardened TLS. Removed
  algorithms can't be enabled.

Hardened TLS affects only applications that opt in to insecure settings:

- Applications that rely on the `tlsrsakex`, `tls3des`, `tls10server`,
  `tlssha1`, or `x509sha1` GODEBUG settings. Upstream Go has already removed
  all of these except `tlssha1`.
- Applications that set `Config.MaxVersion` to TLS 1.1 or earlier.
- Applications that list only removed cipher suites in `Config.CipherSuites`,
  without any that are still available.

All of these settings are insecure.

In the tables below, **Default** means enabled by default, **Available** means
supported but enabled only through configuration, and **Removed** means not
supported.

The tables are presented in the format similar to the [IANA TLS
Parameters](https://www.iana.org/assignments/tls-parameters).

For more information about Transport Layer Security (TLS) please see the following references:

- [NIST PQC](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [RFC10024](https://www.rfc-editor.org/info/rfc10024/)
- [draft-ietf-tls-mldsa](https://www.ietf.org/archive/id/draft-ietf-tls-mldsa-05.html)
- [RFC10015](https://www.rfc-editor.org/rfc/rfc10015.html)
- [BCP 195](https://www.rfc-editor.org/info/bcp195/)
- [RFC 9846](https://www.rfc-editor.org/info/rfc9846/)
- [RFC 5246](https://www.rfc-editor.org/info/rfc5246/)
- [NIST SP 800-52 Rev. 2](https://csrc.nist.gov/pubs/sp/800/52/r2/final)
- [RFC 9151](https://www.rfc-editor.org/info/rfc9151/)
- [draft-becker-cnsa2-tls-profile](https://datatracker.ietf.org/doc/draft-becker-cnsa2-tls-profile/)

## TLS Versions

| Value | Version | Go 1.27 | Go 1.27 Hardened | Go 1.28 |
|---|---|---|---|---|
| 0x0304 | TLSv1.3 | Default | Default | Default |
| 0x0303 | TLSv1.2 | Default | Default | Default |
| 0x0302 | TLSv1.1 | Available | Removed |  |
| 0x0301 | TLSv1.0 | Available | Removed |  |

In Go 1.27, TLS 1.0 and 1.1 are only enabled when `Config.MinVersion` is set below `VersionTLS12`.
Go 1.27 Hardened removes TLS 1.0 and 1.1, and Go 1.28 won't support them.

## TLS Cipher Suites

| Value | Cipher Suite | Go 1.27 | Go 1.27 Hardened | Go 1.28 |
|---|---|---|---|---|
| TLSv1.3 | | | | |
| 0x13,0x01 | TLS_AES_128_GCM_SHA256 | Default | Default | Default |
| 0x13,0x02 | TLS_AES_256_GCM_SHA384 | Default | Default | Default |
| 0x13,0x03 | TLS_CHACHA20_POLY1305_SHA256 | Default | Default | Default |
| TLSv1.2 | | | | |
| 0x00,0x05 | TLS_RSA_WITH_RC4_128_SHA | Available | Removed |  |
| 0x00,0x0A | TLS_RSA_WITH_3DES_EDE_CBC_SHA | Available | Removed |  |
| 0x00,0x2F | TLS_RSA_WITH_AES_128_CBC_SHA | Available | Removed |  |
| 0x00,0x35 | TLS_RSA_WITH_AES_256_CBC_SHA | Available | Removed |  |
| 0x00,0x3C | TLS_RSA_WITH_AES_128_CBC_SHA256 | Available | Removed |  |
| 0x00,0x9C | TLS_RSA_WITH_AES_128_GCM_SHA256 | Available | Removed |  |
| 0x00,0x9D | TLS_RSA_WITH_AES_256_GCM_SHA384 | Available | Removed |  |
| 0xC0,0x07 | TLS_ECDHE_ECDSA_WITH_RC4_128_SHA | Available | Removed |  |
| 0xC0,0x09 | TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA | Default | Default | Default |
| 0xC0,0x0A | TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA | Default | Default | Default |
| 0xC0,0x11 | TLS_ECDHE_RSA_WITH_RC4_128_SHA | Available | Removed |  |
| 0xC0,0x12 | TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA | Available | Removed |  |
| 0xC0,0x13 | TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA | Default | Default | Default |
| 0xC0,0x14 | TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA | Default | Default | Default |
| 0xC0,0x23 | TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256 | Available | Available | Available |
| 0xC0,0x27 | TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 | Available | Available | Available |
| 0xC0,0x2B | TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 | Default | Default | Default |
| 0xC0,0x2C | TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 | Default | Default | Default |
| 0xC0,0x2F | TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 | Default | Default | Default |
| 0xC0,0x30 | TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 | Default | Default | Default |
| 0xCC,0xA8 | TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 | Default | Default | Default |
| 0xCC,0xA9 | TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256 | Default | Default | Default |

## TLS Supported Groups

| Value | Supported Group | Go 1.27 | Go 1.27 Hardened | Go 1.28 |
|---|---|---|---|---|
| PQC TLSv1.3 | | | | |
| 514 | MLKEM1024 | Available | Removed |  |
| 4587 | SecP256r1MLKEM768 | Default | Default | Default |
| 4588 | X25519MLKEM768 | Default | Default | Default |
| 4589 | SecP384r1MLKEM1024 | Default | Default | Default |
| TLSv1.2 & TLSv1.3 | | | | |
| 23 | secp256r1 | Default | Default | Default |
| 24 | secp384r1 | Default | Default | Default |
| 25 | secp521r1 | Default | Default | Default |
| 29 | x25519 | Default | Default | Default |

## TLS SignatureScheme

| Value | Signature Scheme | Go 1.27 | Go 1.27 Hardened | Go 1.28 |
|---|---|---|---|---|
| PQC TLSv1.3 | | | | |
| 0x0904 | mldsa44 | Default | Default | Default |
| 0x0905 | mldsa65 | Default | Default | Default |
| 0x0906 | mldsa87 | Default | Default | Default |
| TLSv1.2 & TLSv1.3 | | | | |
| 0x0401 | rsa_pkcs1_sha256 | Default | Default | Default |
| 0x0403 | ecdsa_secp256r1_sha256 | Default | Default | Default |
| 0x0501 | rsa_pkcs1_sha384 | Default | Default | Default |
| 0x0503 | ecdsa_secp384r1_sha384 | Default | Default | Default |
| 0x0601 | rsa_pkcs1_sha512 | Default | Default | Default |
| 0x0603 | ecdsa_secp521r1_sha512 | Default | Default | Default |
| 0x0804 | rsa_pss_rsae_sha256 | Default | Default | Default |
| 0x0805 | rsa_pss_rsae_sha384 | Default | Default | Default |
| 0x0806 | rsa_pss_rsae_sha512 | Default | Default | Default |
| 0x0807 | ed25519 | Default | Default | Default |
| TLSv1.2 | | | | |
| 0x0201 | rsa_pkcs1_sha1 | Available | Removed |  |
| 0x0203 | ecdsa_sha1 | Available | Removed |  |

In Go 1.27, SHA-1 signatures in the TLS 1.2 handshake require `GODEBUG=tlssha1=1`. In TLS 1.3, `rsa_pkcs1_*` and SHA-1 schemes are accepted only for signatures in certificates.

## Elliptic Curves

| OID | Elliptic Curve | Go 1.27 | Go 1.27 Hardened | Go 1.28 |
|---|---|---|---|---|
| 1.2.840.10045.3.1.7 | prime256v1 (P-256, secp256r1) | Default | Default | Default |
| 1.3.132.0.33 | secp224r1 (P-224) | Available | Removed |  |
| 1.3.132.0.34 | secp384r1 (P-384) | Default | Default | Default |
| 1.3.132.0.35 | secp521r1 (P-521) | Default | Default | Default |

In Go 1.27, P-224 certificates can only be used with TLS 1.2 and earlier, because TLS 1.3 ECDSA signature schemes are bound to P-256, P-384 and P-521.
