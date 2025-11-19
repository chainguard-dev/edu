---
title: "Chainguard FIPS TLS Connectivity Requirements"
linktitle: "FIPS TLS Connectivity Requirements"
lead: ""
type: "article"
description: "FIPS TLS requirements for clients and servers to establish connectivity"
date: 2025-11-15T08:49:31+00:00
lastmod: 2025-11-15T15:22:20+01:00
draft: false
tags: ["FIPS", "TLS", "Product"]
images: []
toc: true
weight: 010
---

This document provides an overview of FIPS TLS connectivy requirements for using Chainguard FIPS products. These FIPS products have **higher** minimum TLS requirements, which complicates connecting them to insecure EOL non-FIPS systems, as well as FIPS systems with lapsed (historical) certification.

Chainguard strives to ensure the broadest connectivity possible for its FIPS products. However, many obsolete systems are still widely used and may not be able to connect with Chainguard FIPS products.

## FIPS TLS Requirements

### TLSv1.3

[NIST Special Publication 800-52 Rev. 2](https://csrc.nist.gov/pubs/sp/800/52/r2/final) required all clients and servers to support TLSv1.3 by January 1, 2024.

While the majority of FIPS modules do have support for TLSv1.3, there are many FIPS 140-2 certified products and operating systems that do not have TLSv1.3 support. As of November 2025 there are [768 Active FIPS 140-2](https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search?SearchMode=Advanced&Standard=140-2&CertificateStatus=Active&ValidationYear=0) validated modules, many of which do not have TLSv1.3 capability.

As a rule of thumb, products launched prior to 2019 do not have TLSv1.3 support, and still require TLSv1.2. If at all possible, upgrade clients and servers to gain TLSv1.3 capability, as newer FIPS modules have started to drop support for validated TLSv1.2. This is primarily driven by adding Post-Quantum Cryptograpy (PQC) which is only supported with TLSv1.3.

### TLSv1.2 RFC 7627

A "triple handshake" man-in-the-middle attack was discovered in the original TLSv1.2 [RFC 5246](https://datatracker.ietf.org/doc/html/rfc5246) protocol specification. The TLSv1.2 [RFC 7627](https://datatracker.ietf.org/doc/html/rfc7627) (published in 2015) addresses this vulnerability with an Extended Master Secret extension.

If you connect to Chainguard's products without support for TLSv1.2 RFC 7627, your privacy and data integrity are not guaranteed.

To address this vulnerability in FIPS modules, NIST initiated a [programmatic transition](https://csrc.nist.gov/Projects/cryptographic-module-validation-program/programmatic-transitions) to require TLSv1.2 [RFC 7627](https://datatracker.ietf.org/doc/html/rfc7627) in approved mode for all new module validations from May 16, 2023.

This means that all FIPS modules submitted after that date require TLSv1.2 with RFC 7627 support in approved mode.

As a rule of thumb, there are very few products that have support for TLSv1.2 with RFC 7627 without TLSv1.3 support, most notably some versions of Windows and Android.

## Known compatible clients and servers

The following Operating Systems, and newer versions of thereof, are known to support TLSv1.2 RFC 7627 and/or TLSv1.3 and should be able to establish TLS connectivy with Chainguard FIPS products:

* Windows 10
* Windows Server 2016
* RHEL 8
* Fedora 28
* Ubuntu 18.04
* Amazon Linux 2023
* SLES 15
* OpenSUSE Leap 15
* Debian 10
* Android 6.0
* Apple macOS Siera 10.12
* iOS 10

This list is not exhaustive. To find FIPS products that suppot TLSv1.2 RFC 7627 or TLS v1.3 one can use [CAVP search](https://csrc.nist.gov/Projects/cryptographic-algorithm-validation-program/validation-search), select **Implementation**, and in the list of algorithms select "**TLS v1.2 RFC7627**" or "**TLS v1.3 KDF**".

### Amazon Linux 2 connectivity support

There is no approved mode for connecting Chainguard products with Amazon Linux 2 in its default FIPS and non-FIPS configurations.

Amazon Linux 2 ships without support for TLSv1.2 RFC 7627 or TLS v1.3. Additionally, Amazon Linux 2 FIPS certification has lapsed.

Amazon Linux 2 non-FIPS has an optional package: `openssl11`. With this installed, it is possible to gain approved connectivity with Chainguard FIPS products.

As of this writing, Amazon Linux 2 is currently scheduled to sunset on June 30, 2026. We recommend upgrading to Chainguard VMs, Amazon Linux 2023, or Bottlerocket.

## Testing Connectivity

To guarantee connectivity, clients and servers communicating with Chainguard FIPS products must, at minimum, support the following  TLS requirements:

- TLSv1.3 with the TLS_AES_256_GCM_SHA384 cipher suite
- TLSv1.2 with
  - ECDHE-ECDSA-AES256-GCM-SHA384 cipher string
  - [RFC 7627](https://datatracker.ietf.org/doc/html/rfc7627) Extended Master Secret Extenstion support
- Signatures using P-256 with SHA-256
- Signatures using RSA with 2048 bits and SHA-256

These requirements can be approximately tested with the following OpenSSL client command:

```shell
openssl s_client -cipher @SECLEVEL=2:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384 -ciphersuites TLS_AES_256_GCM_SHA384 -groups P-256 -connect HOST:PORT
```

> Note that in the case of TLSv1.2 connectivity you must check the output for `Extended master secret: yes`.
