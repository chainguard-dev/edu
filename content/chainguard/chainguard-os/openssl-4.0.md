---
title : "Chainguard OpenSSL 4.0 configuration"
lead: ""
description: "Chainguard OpenSSL 4.0 configuration"
type: "article"
date: 2026-09-10T00:48:23+00:00
lastmod: 2026-09-10T00:48:23+00:00
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

The majority of the available algorithms are not enabled default and are
only available with manual overrides, configuration, and reduction of
default security level of 2, to a lower value. Those that are
available in FIPS also require manual overrides and configuration. The
Default columns represent algorithms that are negotiated by default.

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

| TLS Cipher Suite / value | TLS Cipher Suite / description | Non-FIPS / Available | Non-FIPS / Default | FIPS / Available | FIPS / Default |
|---|---|---|---|---|---|
| 0x00,0x67 | TLS_DHE_RSA_WITH_AES_128_CBC_SHA256 |  |  | Yes |  |
| 0x00,0x6B | TLS_DHE_RSA_WITH_AES_256_CBC_SHA256 |  |  | Yes |  |
| 0x00,0x6C | TLS_DH_anon_WITH_AES_128_CBC_SHA256 |  |  | Yes |  |
| 0x00,0x6D | TLS_DH_anon_WITH_AES_256_CBC_SHA256 |  |  | Yes |  |
| 0x00,0x9E | TLS_DHE_RSA_WITH_AES_128_GCM_SHA256 |  |  | Yes |  |
| 0x00,0x9F | TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 |  |  | Yes |  |
| 0x00,0xA6 | TLS_DH_anon_WITH_AES_128_GCM_SHA256 |  |  | Yes |  |
| 0x00,0xA7 | TLS_DH_anon_WITH_AES_256_GCM_SHA384 |  |  | Yes |  |
| 0x13,0x01 | TLS_AES_128_GCM_SHA256 | Yes | Yes | Yes | Yes |
| 0x13,0x02 | TLS_AES_256_GCM_SHA384 | Yes | Yes | Yes | Yes |
| 0x13,0x03 | TLS_CHACHA20_POLY1305_SHA256 | Yes | Yes |  |  |
| 0xC0,0x09 | TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA | Yes |  |  |  |
| 0xC0,0x0A | TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA | Yes |  |  |  |
| 0xC0,0x13 | TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA | Yes |  |  |  |
| 0xC0,0x14 | TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA | Yes |  |  |  |
| 0xC0,0x23 | TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256 | Yes |  | Yes |  |
| 0xC0,0x24 | TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384 | Yes |  | Yes |  |
| 0xC0,0x27 | TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 | Yes |  | Yes |  |
| 0xC0,0x28 | TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 | Yes |  | Yes |  |
| 0xC0,0x2B | TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 | Yes | Yes | Yes | Yes |
| 0xC0,0x2C | TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 | Yes | Yes | Yes | Yes |
| 0xC0,0x2F | TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 | Yes | Yes | Yes | Yes |
| 0xC0,0x30 | TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 | Yes | Yes | Yes | Yes |
| 0xC0,0x9E | TLS_DHE_RSA_WITH_AES_128_CCM |  |  | Yes |  |
| 0xC0,0x9F | TLS_DHE_RSA_WITH_AES_256_CCM |  |  | Yes |  |
| 0xC0,0xA2 | TLS_DHE_RSA_WITH_AES_128_CCM_8 |  |  | Yes |  |
| 0xC0,0xA3 | TLS_DHE_RSA_WITH_AES_256_CCM_8 |  |  | Yes |  |
| 0xC0,0xAC | TLS_ECDHE_ECDSA_WITH_AES_128_CCM | Yes |  | Yes |  |
| 0xC0,0xAD | TLS_ECDHE_ECDSA_WITH_AES_256_CCM | Yes |  | Yes |  |
| 0xC0,0xAE | TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8 | Yes |  | Yes |  |
| 0xC0,0xAF | TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8 | Yes |  | Yes |  |
| 0xCC,0xA8 | TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 | Yes | Yes |  |  |
| 0xCC,0xA9 | TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256 | Yes | Yes |  |  |

## TLS Supported Groups

| TLS Supported Group / value | TLS Supported Group / description | Non-FIPS / Available | Non-FIPS / Default | FIPS / Available | FIPS / Default |
|---|---|---|---|---|---|
| 21 | secp224r1 |  |  | Yes |  |
| 23 | secp256r1 | Yes | Yes | Yes | Yes |
| 24 | secp384r1 | Yes | Yes | Yes | **Preshare** |
| 25 | secp521r1 | Yes | Yes | Yes | Yes |
| 26 | brainpoolP256r1 |  |  |  |  |
| 27 | brainpoolP384r1 |  |  |  |  |
| 28 | brainpoolP512r1 |  |  |  |  |
| 29 | x25519 | Yes | **Preshare** |  |  |
| 30 | x448 | Yes | Yes |  |  |
| 31 | brainpoolP256r1tls13 |  |  |  |  |
| 32 | brainpoolP384r1tls13 |  |  |  |  |
| 33 | brainpoolP512r1tls13 |  |  |  |  |
| 256 | ffdhe2048 |  |  | Yes |  |
| 257 | ffdhe3072 |  |  | Yes |  |
| 258 | ffdhe4096 |  |  | Yes |  |
| 259 | ffdhe6144 |  |  | Yes |  |
| 260 | ffdhe8192 |  |  | Yes |  |
| 512 | MLKEM512 | Yes |  | Yes |  |
| 513 | MLKEM768 | Yes |  | Yes |  |
| 514 | MLKEM1024 | Yes | Yes | Yes | **First** |
| 4587 | SecP256r1MLKEM768 | Yes | Yes | Yes | Yes |
| 4588 | X25519MLKEM768 | Yes | **First** | Yes | Yes |
| 4589 | SecP384r1MLKEM1024 | Yes | Yes | Yes | Yes |

## TLS SignatureScheme

| TLS Signature Scheme / value | TLS Signature Scheme / description | Non-FIPS / Available | Non-FIPS / Default | FIPS / Available | FIPS / Default |
|---|---|---|---|---|---|
| 0x0401 | rsa_pkcs1_sha256 | Yes | Yes | Yes | Yes |
| 0x0403 | ecdsa_secp256r1_sha256 | Yes | Yes | Yes | Yes |
| 0x0501 | rsa_pkcs1_sha384 | Yes | Yes | Yes | Yes |
| 0x0503 | ecdsa_secp384r1_sha384 | Yes | Yes | Yes | Yes |
| 0x0601 | rsa_pkcs1_sha512 | Yes | Yes | Yes | Yes |
| 0x0603 | ecdsa_secp521r1_sha512 | Yes | Yes | Yes | Yes |
| 0x0804 | rsa_pss_rsae_sha256 | Yes | Yes | Yes | Yes |
| 0x0805 | rsa_pss_rsae_sha384 | Yes | Yes | Yes | Yes |
| 0x0806 | rsa_pss_rsae_sha512 | Yes | Yes | Yes | Yes |
| 0x0807 | ed25519 | Yes | Yes | Yes | Yes |
| 0x0808 | ed448 | Yes | Yes | Yes | Yes |
| 0x0809 | rsa_pss_pss_sha256 | Yes | Yes | Yes | Yes |
| 0x080A | rsa_pss_pss_sha384 | Yes | Yes | Yes | Yes |
| 0x080B | rsa_pss_pss_sha512 | Yes | Yes | Yes | Yes |
| 0x081A | ecdsa_brainpoolP256r1tls13_sha256 |  |  |  |  |
| 0x081B | ecdsa_brainpoolP384r1tls13_sha384 |  |  |  |  |
| 0x081C | ecdsa_brainpoolP512r1tls13_sha512 |  |  |  |  |
| 0x0904 | mldsa44 | Yes | Yes | Yes | Yes |
| 0x0905 | mldsa65 | Yes | Yes | Yes | Yes |
| 0x0906 | mldsa87 | Yes | Yes | Yes | Yes |

## Elliptic Curves

| Elliptic Curve / OID | Elliptic Curve / description | Non-FIPS / Available | Non-FIPS / Default | FIPS / Available | FIPS / Default |
|---|---|---|---|---|---|
| 1.2.840.10045.3.1.7 | prime256v1 (P-256, secp256r1) | Yes | Yes | Yes | Yes |
| 1.3.36.3.3.2.8.1.1.1 | brainpoolP160r1 |  |  |  |  |
| 1.3.36.3.3.2.8.1.1.2 | brainpoolP160t1 |  |  |  |  |
| 1.3.36.3.3.2.8.1.1.3 | brainpoolP192r1 |  |  |  |  |
| 1.3.36.3.3.2.8.1.1.4 | brainpoolP192t1 |  |  |  |  |
| 1.3.36.3.3.2.8.1.1.5 | brainpoolP224r1 |  |  |  |  |
| 1.3.36.3.3.2.8.1.1.6 | brainpoolP224t1 |  |  |  |  |
| 1.3.36.3.3.2.8.1.1.7 | brainpoolP256r1 |  |  |  |  |
| 1.3.36.3.3.2.8.1.1.8 | brainpoolP256t1 |  |  |  |  |
| 1.3.36.3.3.2.8.1.1.9 | brainpoolP320r1 |  |  |  |  |
| 1.3.36.3.3.2.8.1.1.10 | brainpoolP320t1 |  |  |  |  |
| 1.3.36.3.3.2.8.1.1.11 | brainpoolP384r1 |  |  |  |  |
| 1.3.36.3.3.2.8.1.1.12 | brainpoolP384t1 |  |  |  |  |
| 1.3.36.3.3.2.8.1.1.13 | brainpoolP512r1 |  |  |  |  |
| 1.3.36.3.3.2.8.1.1.14 | brainpoolP512t1 |  |  |  |  |
| 1.3.132.0.10 | secp256k1 | Yes |  |  |  |
| 1.3.132.0.34 | secp384r1 (P-384) | Yes | Yes | Yes | Yes |
| 1.3.132.0.35 | secp521r1 (P-521) | Yes | Yes | Yes | Yes |
