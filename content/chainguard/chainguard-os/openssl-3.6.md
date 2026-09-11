---
title : "OpenSSL 3.6 Configuration"
lead: ""
description: "OpenSSL 3.6 Configuration"
type: "article"
date: 2026-09-10T00:48:23+00:00
lastmod: 2026-09-11T00:00:00+00:00
draft: false
weight: 040
menu:
  docs:
    parent: "chainguard-os"
    identifier: "Chainguard OpenSSL 3.6"
toc: true
table_layout: auto
---

This is a summary of available algorithms in Chainguard OpenSSL 3.6
(non-fips) and Chainguard FIPS Provider for OpenSSL 3.4.

The majority of the available algorithms are not enabled default and are
only available with manual overrides, configuration, and reduction of
default security level of 2, to a lower value. Those that are
available in FIPS also require manual overrides and configuration.

The Non-FIPS and FIPS columns read as follows:

- **Default**: negotiated by default under the shipped Chainguard OS
  crypto policy. For key exchange groups, **First** marks the most
  preferred group and **Preshare** the group whose key share is sent
  in the first ClientHello.
- **Available**: works, but only with manual configuration.
- **Non-TLS only**: the elliptic curve works for keys, signatures and
  certificates, but has no TLS supported group and so cannot be used
  in TLS.
- **Verify only**: the FIPS provider verifies signatures on the curve
  but does not generate keys or sign with it.
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

| Value | Cipher Suite | Non-FIPS | FIPS | PQC |
|---|---|---|---|---|
| TLSv1.3 | | | | |
| 0x13,0x01 | TLS_AES_128_GCM_SHA256 | Default | Default | Yes |
| 0x13,0x02 | TLS_AES_256_GCM_SHA384 | **First** | **First** | Yes |
| 0x13,0x03 | TLS_CHACHA20_POLY1305_SHA256 | Default |  | Yes |
| TLSv1.2 | | | | |
| 0x00,0x2F | TLS_RSA_WITH_AES_128_CBC_SHA | Available |  |  |
| 0x00,0x32 | TLS_DHE_DSS_WITH_AES_128_CBC_SHA | Available |  |  |
| 0x00,0x33 | TLS_DHE_RSA_WITH_AES_128_CBC_SHA | Available | Available |  |
| 0x00,0x34 | TLS_DH_anon_WITH_AES_128_CBC_SHA | Available | Available |  |
| 0x00,0x35 | TLS_RSA_WITH_AES_256_CBC_SHA | Available |  |  |
| 0x00,0x38 | TLS_DHE_DSS_WITH_AES_256_CBC_SHA | Available |  |  |
| 0x00,0x39 | TLS_DHE_RSA_WITH_AES_256_CBC_SHA | Available | Available |  |
| 0x00,0x3A | TLS_DH_anon_WITH_AES_256_CBC_SHA | Available | Available |  |
| 0x00,0x3C | TLS_RSA_WITH_AES_128_CBC_SHA256 | Available |  |  |
| 0x00,0x3D | TLS_RSA_WITH_AES_256_CBC_SHA256 | Available |  |  |
| 0x00,0x40 | TLS_DHE_DSS_WITH_AES_128_CBC_SHA256 | Available |  |  |
| 0x00,0x41 | TLS_RSA_WITH_CAMELLIA_128_CBC_SHA | Available |  |  |
| 0x00,0x44 | TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA | Available |  |  |
| 0x00,0x45 | TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA | Available |  |  |
| 0x00,0x46 | TLS_DH_anon_WITH_CAMELLIA_128_CBC_SHA | Available |  |  |
| 0x00,0x67 | TLS_DHE_RSA_WITH_AES_128_CBC_SHA256 | Available | Available |  |
| 0x00,0x6A | TLS_DHE_DSS_WITH_AES_256_CBC_SHA256 | Available |  |  |
| 0x00,0x6B | TLS_DHE_RSA_WITH_AES_256_CBC_SHA256 | Available | Available |  |
| 0x00,0x6C | TLS_DH_anon_WITH_AES_128_CBC_SHA256 | Available | Available |  |
| 0x00,0x6D | TLS_DH_anon_WITH_AES_256_CBC_SHA256 | Available | Available |  |
| 0x00,0x84 | TLS_RSA_WITH_CAMELLIA_256_CBC_SHA | Available |  |  |
| 0x00,0x87 | TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA | Available |  |  |
| 0x00,0x88 | TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA | Available |  |  |
| 0x00,0x89 | TLS_DH_anon_WITH_CAMELLIA_256_CBC_SHA | Available |  |  |
| 0x00,0x8C | TLS_PSK_WITH_AES_128_CBC_SHA | Available | Available |  |
| 0x00,0x8D | TLS_PSK_WITH_AES_256_CBC_SHA | Available | Available |  |
| 0x00,0x90 | TLS_DHE_PSK_WITH_AES_128_CBC_SHA | Available | Available |  |
| 0x00,0x91 | TLS_DHE_PSK_WITH_AES_256_CBC_SHA | Available | Available |  |
| 0x00,0x94 | TLS_RSA_PSK_WITH_AES_128_CBC_SHA | Available |  |  |
| 0x00,0x95 | TLS_RSA_PSK_WITH_AES_256_CBC_SHA | Available |  |  |
| 0x00,0x9C | TLS_RSA_WITH_AES_128_GCM_SHA256 | Available |  |  |
| 0x00,0x9D | TLS_RSA_WITH_AES_256_GCM_SHA384 | Available |  |  |
| 0x00,0x9E | TLS_DHE_RSA_WITH_AES_128_GCM_SHA256 | Available | Available |  |
| 0x00,0x9F | TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 | Available | Available |  |
| 0x00,0xA2 | TLS_DHE_DSS_WITH_AES_128_GCM_SHA256 | Available |  |  |
| 0x00,0xA3 | TLS_DHE_DSS_WITH_AES_256_GCM_SHA384 | Available |  |  |
| 0x00,0xA6 | TLS_DH_anon_WITH_AES_128_GCM_SHA256 | Available | Available |  |
| 0x00,0xA7 | TLS_DH_anon_WITH_AES_256_GCM_SHA384 | Available | Available |  |
| 0x00,0xA8 | TLS_PSK_WITH_AES_128_GCM_SHA256 | Available | Available |  |
| 0x00,0xA9 | TLS_PSK_WITH_AES_256_GCM_SHA384 | Available | Available |  |
| 0x00,0xAA | TLS_DHE_PSK_WITH_AES_128_GCM_SHA256 | Available | Available |  |
| 0x00,0xAB | TLS_DHE_PSK_WITH_AES_256_GCM_SHA384 | Available | Available |  |
| 0x00,0xAC | TLS_RSA_PSK_WITH_AES_128_GCM_SHA256 | Available |  |  |
| 0x00,0xAD | TLS_RSA_PSK_WITH_AES_256_GCM_SHA384 | Available |  |  |
| 0x00,0xAE | TLS_PSK_WITH_AES_128_CBC_SHA256 | Available | Available |  |
| 0x00,0xAF | TLS_PSK_WITH_AES_256_CBC_SHA384 | Available | Available |  |
| 0x00,0xB2 | TLS_DHE_PSK_WITH_AES_128_CBC_SHA256 | Available | Available |  |
| 0x00,0xB3 | TLS_DHE_PSK_WITH_AES_256_CBC_SHA384 | Available | Available |  |
| 0x00,0xB6 | TLS_RSA_PSK_WITH_AES_128_CBC_SHA256 | Available |  |  |
| 0x00,0xB7 | TLS_RSA_PSK_WITH_AES_256_CBC_SHA384 | Available |  |  |
| 0x00,0xBA | TLS_RSA_WITH_CAMELLIA_128_CBC_SHA256 | Available |  |  |
| 0x00,0xBD | TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA256 | Available |  |  |
| 0x00,0xBE | TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA256 | Available |  |  |
| 0x00,0xBF | TLS_DH_anon_WITH_CAMELLIA_128_CBC_SHA256 | Available |  |  |
| 0x00,0xC0 | TLS_RSA_WITH_CAMELLIA_256_CBC_SHA256 | Available |  |  |
| 0x00,0xC3 | TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA256 | Available |  |  |
| 0x00,0xC4 | TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA256 | Available |  |  |
| 0x00,0xC5 | TLS_DH_anon_WITH_CAMELLIA_256_CBC_SHA256 | Available |  |  |
| 0xC0,0x09 | TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA | Available | Available |  |
| 0xC0,0x0A | TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA | Available | Available |  |
| 0xC0,0x13 | TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA | Available | Available |  |
| 0xC0,0x14 | TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA | Available | Available |  |
| 0xC0,0x18 | TLS_ECDH_anon_WITH_AES_128_CBC_SHA | Available | Available |  |
| 0xC0,0x19 | TLS_ECDH_anon_WITH_AES_256_CBC_SHA | Available | Available |  |
| 0xC0,0x1D | TLS_SRP_SHA_WITH_AES_128_CBC_SHA | Available | Available |  |
| 0xC0,0x1E | TLS_SRP_SHA_RSA_WITH_AES_128_CBC_SHA | Available | Available |  |
| 0xC0,0x1F | TLS_SRP_SHA_DSS_WITH_AES_128_CBC_SHA | Available |  |  |
| 0xC0,0x20 | TLS_SRP_SHA_WITH_AES_256_CBC_SHA | Available | Available |  |
| 0xC0,0x21 | TLS_SRP_SHA_RSA_WITH_AES_256_CBC_SHA | Available | Available |  |
| 0xC0,0x22 | TLS_SRP_SHA_DSS_WITH_AES_256_CBC_SHA | Available |  |  |
| 0xC0,0x23 | TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256 | Available | Available |  |
| 0xC0,0x24 | TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384 | Available | Available |  |
| 0xC0,0x27 | TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 | Available | Available |  |
| 0xC0,0x28 | TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 | Available | Available |  |
| 0xC0,0x2B | TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 | Default | Default |  |
| 0xC0,0x2C | TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 | **First** | **First** |  |
| 0xC0,0x2F | TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 | Default | Default |  |
| 0xC0,0x30 | TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 | **First** | **First** |  |
| 0xC0,0x35 | TLS_ECDHE_PSK_WITH_AES_128_CBC_SHA | Available | Available |  |
| 0xC0,0x36 | TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA | Available | Available |  |
| 0xC0,0x37 | TLS_ECDHE_PSK_WITH_AES_128_CBC_SHA256 | Available | Available |  |
| 0xC0,0x38 | TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384 | Available | Available |  |
| 0xC0,0x50 | TLS_RSA_WITH_ARIA_128_GCM_SHA256 | Available |  |  |
| 0xC0,0x51 | TLS_RSA_WITH_ARIA_256_GCM_SHA384 | Available |  |  |
| 0xC0,0x52 | TLS_DHE_RSA_WITH_ARIA_128_GCM_SHA256 | Available |  |  |
| 0xC0,0x53 | TLS_DHE_RSA_WITH_ARIA_256_GCM_SHA384 | Available |  |  |
| 0xC0,0x56 | TLS_DHE_DSS_WITH_ARIA_128_GCM_SHA256 | Available |  |  |
| 0xC0,0x57 | TLS_DHE_DSS_WITH_ARIA_256_GCM_SHA384 | Available |  |  |
| 0xC0,0x5C | TLS_ECDHE_ECDSA_WITH_ARIA_128_GCM_SHA256 | Available |  |  |
| 0xC0,0x5D | TLS_ECDHE_ECDSA_WITH_ARIA_256_GCM_SHA384 | Available |  |  |
| 0xC0,0x60 | TLS_ECDHE_RSA_WITH_ARIA_128_GCM_SHA256 | Available |  |  |
| 0xC0,0x61 | TLS_ECDHE_RSA_WITH_ARIA_256_GCM_SHA384 | Available |  |  |
| 0xC0,0x6A | TLS_PSK_WITH_ARIA_128_GCM_SHA256 | Available |  |  |
| 0xC0,0x6B | TLS_PSK_WITH_ARIA_256_GCM_SHA384 | Available |  |  |
| 0xC0,0x6C | TLS_DHE_PSK_WITH_ARIA_128_GCM_SHA256 | Available |  |  |
| 0xC0,0x6D | TLS_DHE_PSK_WITH_ARIA_256_GCM_SHA384 | Available |  |  |
| 0xC0,0x6E | TLS_RSA_PSK_WITH_ARIA_128_GCM_SHA256 | Available |  |  |
| 0xC0,0x6F | TLS_RSA_PSK_WITH_ARIA_256_GCM_SHA384 | Available |  |  |
| 0xC0,0x72 | TLS_ECDHE_ECDSA_WITH_CAMELLIA_128_CBC_SHA256 | Available |  |  |
| 0xC0,0x73 | TLS_ECDHE_ECDSA_WITH_CAMELLIA_256_CBC_SHA384 | Available |  |  |
| 0xC0,0x76 | TLS_ECDHE_RSA_WITH_CAMELLIA_128_CBC_SHA256 | Available |  |  |
| 0xC0,0x77 | TLS_ECDHE_RSA_WITH_CAMELLIA_256_CBC_SHA384 | Available |  |  |
| 0xC0,0x94 | TLS_PSK_WITH_CAMELLIA_128_CBC_SHA256 | Available |  |  |
| 0xC0,0x95 | TLS_PSK_WITH_CAMELLIA_256_CBC_SHA384 | Available |  |  |
| 0xC0,0x96 | TLS_DHE_PSK_WITH_CAMELLIA_128_CBC_SHA256 | Available |  |  |
| 0xC0,0x97 | TLS_DHE_PSK_WITH_CAMELLIA_256_CBC_SHA384 | Available |  |  |
| 0xC0,0x98 | TLS_RSA_PSK_WITH_CAMELLIA_128_CBC_SHA256 | Available |  |  |
| 0xC0,0x99 | TLS_RSA_PSK_WITH_CAMELLIA_256_CBC_SHA384 | Available |  |  |
| 0xC0,0x9A | TLS_ECDHE_PSK_WITH_CAMELLIA_128_CBC_SHA256 | Available |  |  |
| 0xC0,0x9B | TLS_ECDHE_PSK_WITH_CAMELLIA_256_CBC_SHA384 | Available |  |  |
| 0xC0,0x9C | TLS_RSA_WITH_AES_128_CCM | Available |  |  |
| 0xC0,0x9D | TLS_RSA_WITH_AES_256_CCM | Available |  |  |
| 0xC0,0x9E | TLS_DHE_RSA_WITH_AES_128_CCM | Available | Available |  |
| 0xC0,0x9F | TLS_DHE_RSA_WITH_AES_256_CCM | Available | Available |  |
| 0xC0,0xA0 | TLS_RSA_WITH_AES_128_CCM_8 | Available |  |  |
| 0xC0,0xA1 | TLS_RSA_WITH_AES_256_CCM_8 | Available |  |  |
| 0xC0,0xA2 | TLS_DHE_RSA_WITH_AES_128_CCM_8 | Available | Available |  |
| 0xC0,0xA3 | TLS_DHE_RSA_WITH_AES_256_CCM_8 | Available | Available |  |
| 0xC0,0xA4 | TLS_PSK_WITH_AES_128_CCM | Available | Available |  |
| 0xC0,0xA5 | TLS_PSK_WITH_AES_256_CCM | Available | Available |  |
| 0xC0,0xA6 | TLS_DHE_PSK_WITH_AES_128_CCM | Available | Available |  |
| 0xC0,0xA7 | TLS_DHE_PSK_WITH_AES_256_CCM | Available | Available |  |
| 0xC0,0xA8 | TLS_PSK_WITH_AES_128_CCM_8 | Available | Available |  |
| 0xC0,0xA9 | TLS_PSK_WITH_AES_256_CCM_8 | Available | Available |  |
| 0xC0,0xAA | TLS_PSK_DHE_WITH_AES_128_CCM_8 | Available | Available |  |
| 0xC0,0xAB | TLS_PSK_DHE_WITH_AES_256_CCM_8 | Available | Available |  |
| 0xC0,0xAC | TLS_ECDHE_ECDSA_WITH_AES_128_CCM | Available | Available |  |
| 0xC0,0xAD | TLS_ECDHE_ECDSA_WITH_AES_256_CCM | Available | Available |  |
| 0xC0,0xAE | TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8 | Available | Available |  |
| 0xC0,0xAF | TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8 | Available | Available |  |
| 0xCC,0xA8 | TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 | Default |  |  |
| 0xCC,0xA9 | TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256 | Default |  |  |
| 0xCC,0xAA | TLS_DHE_RSA_WITH_CHACHA20_POLY1305_SHA256 | Available |  |  |
| 0xCC,0xAB | TLS_PSK_WITH_CHACHA20_POLY1305_SHA256 | Available |  |  |
| 0xCC,0xAC | TLS_ECDHE_PSK_WITH_CHACHA20_POLY1305_SHA256 | Available |  |  |
| 0xCC,0xAD | TLS_DHE_PSK_WITH_CHACHA20_POLY1305_SHA256 | Available |  |  |
| 0xCC,0xAE | TLS_RSA_PSK_WITH_CHACHA20_POLY1305_SHA256 | Available |  |  |

46 of the TLSv1.2 suites (those whose minimum protocol version is TLS 1.0) also negotiate on TLS 1.0 and TLS 1.1 in the non-FIPS build when the shipped policy, which sets the minimum protocol version to TLS 1.2, is bypassed. TLS 1.0 and TLS 1.1 never work with the FIPS provider.

## TLS Supported Groups

| Value | Supported Group | Non-FIPS | FIPS | PQC |
|---|---|---|---|---|
| PQC TLSv1.3 | | | | |
| 512 | MLKEM512 | Available |  | Yes |
| 513 | MLKEM768 | Available |  | Yes |
| 514 | MLKEM1024 | Default |  | Yes |
| 4587 | SecP256r1MLKEM768 | Default |  | Yes |
| 4588 | X25519MLKEM768 | **First** |  | Yes |
| 4589 | SecP384r1MLKEM1024 | Default |  | Yes |
| TLSv1.2 & TLSv1.3 | | | | |
| 15 | secp160k1 | Available |  |  |
| 16 | secp160r1 | Available |  |  |
| 17 | secp160r2 | Available |  |  |
| 18 | secp192k1 | Available |  |  |
| 19 | secp192r1 | Available |  |  |
| 20 | secp224k1 | Available |  |  |
| 21 | secp224r1 | Available | Available |  |
| 22 | secp256k1 | Available |  |  |
| 23 | secp256r1 | Default | Default |  |
| 24 | secp384r1 | Default | **First** & Preshare |  |
| 25 | secp521r1 | Default | Available |  |
| 26, 31 | brainpoolP256r1 | Available |  |  |
| 27, 32 | brainpoolP384r1 | Available |  |  |
| 28, 33 | brainpoolP512r1 | Available |  |  |
| 29 | x25519 | Preshare |  |  |
| 30 | x448 | Default |  |  |
| 256 | ffdhe2048 | Available | Available |  |
| 257 | ffdhe3072 | Available | Available |  |
| 258 | ffdhe4096 | Available | Available |  |
| 259 | ffdhe6144 | Available | Available |  |
| 260 | ffdhe8192 | Available | Available |  |

The brainpool rows combine two codepoints each: the first one (`brainpoolP256r1`, `brainpoolP384r1`, `brainpoolP512r1`) is what TLS 1.2 negotiates, the second one (`brainpoolP256r1tls13`, `brainpoolP384r1tls13`, `brainpoolP512r1tls13`) is the TLS 1.3 name of the same curve.

## TLS SignatureScheme

| Value | Signature Scheme | Non-FIPS | FIPS | PQC |
|---|---|---|---|---|
| PQC TLSv1.3 | | | | |
| 0x0904 | mldsa44 | Default |  | Yes |
| 0x0905 | mldsa65 | Default |  | Yes |
| 0x0906 | mldsa87 | Default |  | Yes |
| TLSv1.2 & TLSv1.3 | | | | |
| 0x0201 | rsa_pkcs1_sha1 | Available |  |  |
| 0x0202 | Reserved for backward compatibility (dsa_sha1) | Available |  |  |
| 0x0203 | ecdsa_sha1 | Available |  |  |
| 0x0301 | Reserved for backward compatibility (rsa_pkcs1_sha224) | Available | Available |  |
| 0x0302 | Reserved for backward compatibility (dsa_sha224) | Available |  |  |
| 0x0303 | Reserved for backward compatibility (ecdsa_sha224) | Available | Available |  |
| 0x0401 | rsa_pkcs1_sha256 | Default | Default |  |
| 0x0402 | Reserved for backward compatibility (dsa_sha256) | Available |  |  |
| 0x0403 | ecdsa_secp256r1_sha256 | Default | Default |  |
| 0x0501 | rsa_pkcs1_sha384 | Default | Default |  |
| 0x0502 | Reserved for backward compatibility (dsa_sha384) | Available |  |  |
| 0x0503 | ecdsa_secp384r1_sha384 | Default | Default |  |
| 0x0601 | rsa_pkcs1_sha512 | Default | Default |  |
| 0x0602 | Reserved for backward compatibility (dsa_sha512) | Available |  |  |
| 0x0603 | ecdsa_secp521r1_sha512 | Default | Default |  |
| 0x0804 | rsa_pss_rsae_sha256 | Default | Default |  |
| 0x0805 | rsa_pss_rsae_sha384 | Default | Default |  |
| 0x0806 | rsa_pss_rsae_sha512 | Default | Default |  |
| 0x0807 | ed25519 | Default | Default |  |
| 0x0808 | ed448 | Default | Default |  |
| 0x0809 | rsa_pss_pss_sha256 | Default | Default |  |
| 0x080A | rsa_pss_pss_sha384 | Default | Default |  |
| 0x080B | rsa_pss_pss_sha512 | Default | Default |  |
| 0x081A | ecdsa_brainpoolP256r1tls13_sha256 | Available |  |  |
| 0x081B | ecdsa_brainpoolP384r1tls13_sha384 | Available |  |  |
| 0x081C | ecdsa_brainpoolP512r1tls13_sha512 | Available |  |  |

## Elliptic Curves

| OID | Elliptic Curve | Non-FIPS | FIPS |
|---|---|---|---|
| 1.2.840.10045.3.1.1 | prime192v1 (P-192, secp192r1) | Available | Verify only |
| 1.2.840.10045.3.1.2 | prime192v2 | Non-TLS only |  |
| 1.2.840.10045.3.1.3 | prime192v3 | Non-TLS only |  |
| 1.2.840.10045.3.1.4 | prime239v1 | Non-TLS only |  |
| 1.2.840.10045.3.1.5 | prime239v2 | Non-TLS only |  |
| 1.2.840.10045.3.1.6 | prime239v3 | Non-TLS only |  |
| 1.2.840.10045.3.1.7 | prime256v1 (P-256, secp256r1) | Default | Default |
| 1.3.36.3.3.2.8.1.1.1 | brainpoolP160r1 | Non-TLS only |  |
| 1.3.36.3.3.2.8.1.1.2 | brainpoolP160t1 | Non-TLS only |  |
| 1.3.36.3.3.2.8.1.1.3 | brainpoolP192r1 | Non-TLS only |  |
| 1.3.36.3.3.2.8.1.1.4 | brainpoolP192t1 | Non-TLS only |  |
| 1.3.36.3.3.2.8.1.1.5 | brainpoolP224r1 | Non-TLS only |  |
| 1.3.36.3.3.2.8.1.1.6 | brainpoolP224t1 | Non-TLS only |  |
| 1.3.36.3.3.2.8.1.1.7 | brainpoolP256r1 | Available |  |
| 1.3.36.3.3.2.8.1.1.8 | brainpoolP256t1 | Non-TLS only |  |
| 1.3.36.3.3.2.8.1.1.9 | brainpoolP320r1 | Non-TLS only |  |
| 1.3.36.3.3.2.8.1.1.10 | brainpoolP320t1 | Non-TLS only |  |
| 1.3.36.3.3.2.8.1.1.11 | brainpoolP384r1 | Available |  |
| 1.3.36.3.3.2.8.1.1.12 | brainpoolP384t1 | Non-TLS only |  |
| 1.3.36.3.3.2.8.1.1.13 | brainpoolP512r1 | Available |  |
| 1.3.36.3.3.2.8.1.1.14 | brainpoolP512t1 | Non-TLS only |  |
| 1.3.132.0.6 | secp112r1 | Non-TLS only |  |
| 1.3.132.0.7 | secp112r2 | Non-TLS only |  |
| 1.3.132.0.8 | secp160r1 | Available |  |
| 1.3.132.0.9 | secp160k1 | Available |  |
| 1.3.132.0.10 | secp256k1 | Available |  |
| 1.3.132.0.28 | secp128r1 | Non-TLS only |  |
| 1.3.132.0.29 | secp128r2 | Non-TLS only |  |
| 1.3.132.0.30 | secp160r2 | Available |  |
| 1.3.132.0.31 | secp192k1 | Available |  |
| 1.3.132.0.32 | secp224k1 | Available |  |
| 1.3.132.0.33 | secp224r1 (P-224) | Available | Available |
| 1.3.132.0.34 | secp384r1 (P-384) | Default | Default |
| 1.3.132.0.35 | secp521r1 (P-521) | Default | Default, TLS 1.3 only |
| 2.23.43.1.4.6 | wap-wsg-idm-ecid-wtls6 | Non-TLS only |  |
| 2.23.43.1.4.7 | wap-wsg-idm-ecid-wtls7 | Non-TLS only |  |
| 2.23.43.1.4.8 | wap-wsg-idm-ecid-wtls8 | Non-TLS only |  |
| 2.23.43.1.4.9 | wap-wsg-idm-ecid-wtls9 | Non-TLS only |  |
| 2.23.43.1.4.12 | wap-wsg-idm-ecid-wtls12 | Non-TLS only |  |
