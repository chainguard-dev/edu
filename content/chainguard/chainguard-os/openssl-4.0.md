---
title : "OpenSSL 4.0 Configuration"
lead: ""
description: "OpenSSL 4.0 Configuration"
type: "article"
date: 2026-09-10T00:48:23+00:00
lastmod: 2026-09-11T00:00:00+00:00
draft: false
weight: 040
menu:
  docs:
    parent: "chainguard-os"
    identifier: "Chainguard OpenSSL 4.0"
toc: true
table_layout: auto
---

This is a summary of available algorithms in Chainguard OpenSSL 4.0
(non-fips) and Chainguard FIPS Provider for OpenSSL 3.6.

The majority of the available algorithms are not enabled by default and are
only available with manual overrides, configuration, and reduction of
default security level of 2, to a lower value. Those that are
available in FIPS also require manual overrides and configuration.

The v4.0 and FIPS v3.6 columns read as follows:

- **Default**: negotiated by default under the shipped Chainguard OS
  crypto policy. For key exchange groups, **First** marks the most
  preferred group and **Preshare** the group whose key share is sent
  in the first ClientHello.
- **Available**: works, but only with manual configuration.
- **Non-TLS only**: the elliptic curve works for keys, signatures and
  certificates, but has no TLS supported group and so cannot be used
  in TLS.
- Blank: not available.

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

## TLS Cipher Suites

| Value | Cipher Suite | v4.0 | FIPS v3.6 | PQC |
|---|---|---|---|---|
| TLSv1.3 | | | | |
| 0x13,0x01 | TLS_AES_128_GCM_SHA256 | Default | Default | Yes |
| 0x13,0x02 | TLS_AES_256_GCM_SHA384 | **First** | **First** | Yes |
| 0x13,0x03 | TLS_CHACHA20_POLY1305_SHA256 | Default |  | Yes |
| TLSv1.2 | | | | |
| 0xC0,0x23 | TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256 | Available | Available |  |
| 0xC0,0x24 | TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384 | Available | Available |  |
| 0xC0,0x27 | TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 | Available | Available |  |
| 0xC0,0x28 | TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 | Available | Available |  |
| 0xC0,0x2B | TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 | Default | Default |  |
| 0xC0,0x2C | TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 | **First** | **First** |  |
| 0xC0,0x2F | TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 | Default | Default |  |
| 0xC0,0x30 | TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 | **First** | **First** |  |
| 0xC0,0x37 | TLS_ECDHE_PSK_WITH_AES_128_CBC_SHA256 | Available | Available |  |
| 0xC0,0x38 | TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384 | Available | Available |  |
| 0xC0,0xAC | TLS_ECDHE_ECDSA_WITH_AES_128_CCM | Available | Available |  |
| 0xC0,0xAD | TLS_ECDHE_ECDSA_WITH_AES_256_CCM | Available | Available |  |
| 0xCC,0xA8 | TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 | Default |  |  |
| 0xCC,0xA9 | TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256 | Default |  |  |
| 0xCC,0xAC | TLS_ECDHE_PSK_WITH_CHACHA20_POLY1305_SHA256 | Available |  |  |

## TLS Supported Groups

| Value | Supported Group | v4.0 | FIPS v3.6 | PQC |
|---|---|---|---|---|
| PQC TLSv1.3 | | | | |
| 512 | MLKEM512 | Available | Available | Yes |
| 513 | MLKEM768 | Available | Available | Yes |
| 514 | MLKEM1024 | Default | **First** | Yes |
| 4587 | SecP256r1MLKEM768 | Default | Default | Yes |
| 4588 | X25519MLKEM768 | **First** | Default | Yes |
| 4589 | SecP384r1MLKEM1024 | Default | Default | Yes |
| TLSv1.2 & TLSv1.3 | | | | |
| 23 | secp256r1 | Default | Default |  |
| 24 | secp384r1 | Default | Preshare |  |
| 25 | secp521r1 | Default | Default |  |
| 26, 31 | brainpoolP256r1 | Default |  |  |
| 27, 32 | brainpoolP384r1 | Default |  |  |
| 28, 33 | brainpoolP512r1 | Default |  |  |
| 29 | x25519 | Preshare |  |  |
| 30 | x448 | Default |  |  |

The brainpool rows combine two codepoints each: the first one (`brainpoolP256r1`, `brainpoolP384r1`, `brainpoolP512r1`) is what TLS 1.2 negotiates, the second one (`brainpoolP256r1tls13`, `brainpoolP384r1tls13`, `brainpoolP512r1tls13`) is the TLS 1.3 name of the same curve.

## TLS SignatureScheme

| Value | Signature Scheme | v4.0 | FIPS v3.6 | PQC |
|---|---|---|---|---|
| PQC TLSv1.3 | | | | |
| 0x0904 | mldsa44 | Default | Default | Yes |
| 0x0905 | mldsa65 | Default | Default | Yes |
| 0x0906 | mldsa87 | Default | Default | Yes |
| TLSv1.2 & TLSv1.3 | | | | |
| 0x0401 | rsa_pkcs1_sha256 | Default | Default |  |
| 0x0403 | ecdsa_secp256r1_sha256 | Default | Default |  |
| 0x0501 | rsa_pkcs1_sha384 | Default | Default |  |
| 0x0503 | ecdsa_secp384r1_sha384 | Default | Default |  |
| 0x0601 | rsa_pkcs1_sha512 | Default | Default |  |
| 0x0603 | ecdsa_secp521r1_sha512 | Default | Default |  |
| 0x0804 | rsa_pss_rsae_sha256 | Default | Default |  |
| 0x0805 | rsa_pss_rsae_sha384 | Default | Default |  |
| 0x0806 | rsa_pss_rsae_sha512 | Default | Default |  |
| 0x0807 | ed25519 | Default | Default |  |
| 0x0808 | ed448 | Default | Default |  |
| 0x0809 | rsa_pss_pss_sha256 | Default | Default |  |
| 0x080A | rsa_pss_pss_sha384 | Default | Default |  |
| 0x080B | rsa_pss_pss_sha512 | Default | Default |  |
| 0x081A | ecdsa_brainpoolP256r1tls13_sha256 | Default |  |  |
| 0x081B | ecdsa_brainpoolP384r1tls13_sha384 | Default |  |  |
| 0x081C | ecdsa_brainpoolP512r1tls13_sha512 | Default |  |  |

## Elliptic Curves

| OID | Elliptic Curve | v4.0 | FIPS v3.6 |
|---|---|---|---|
| 1.2.840.10045.3.1.7 | prime256v1 (P-256, secp256r1) | Default | Default |
| 1.3.36.3.3.2.8.1.1.7 | brainpoolP256r1 | Default |  |
| 1.3.36.3.3.2.8.1.1.11 | brainpoolP384r1 | Default |  |
| 1.3.36.3.3.2.8.1.1.13 | brainpoolP512r1 | Default |  |
| 1.3.132.0.10 | secp256k1 | Non-TLS only |  |
| 1.3.132.0.34 | secp384r1 (P-384) | Default | Default |
| 1.3.132.0.35 | secp521r1 (P-521) | Default | Default |
