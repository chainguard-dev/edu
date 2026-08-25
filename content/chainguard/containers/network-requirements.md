---
title: "Chainguard Containers network requirements"
linktitle: "Network requirements"
aliases:
- /chainguard/network-requirements
- /chainguard/administration/network-requirements/
- /chainguard/chainguard-images/network-requirements/
- /chainguard/containers/network-requirements/
lead: "Using Chainguard Containers with firewalls, access control lists, and proxies."
type: "article"
description: "Using Chainguard Containers with firewalls, access control lists, and proxies."
date: 2023-09-08T08:49:31+00:00
lastmod: 2026-08-25T13:24:30+00:00
draft: false
tags: ["Chainguard Containers", "Reference"]
images: []
toc: true
weight: 010
---

This document provides an overview of network requirements for using [Chainguard Containers](https://www.chainguard.dev/chainguard-images?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement). To use Chainguard tools and Containers in environments with firewalls, VPNs, and IDS/IPS systems, you will need to add some rules to allow traffic into and out of your networks.

Chainguard Containers do not call Chainguard services while running, so no network changes would be required to the runtime environment. Review the **Notes** column for more info on each Hostname.

## Chainguard Containers hosts

This table lists the DNS hostnames, associated ports, and protocols that will need to be allowed through firewalls and proxies to use Chainguard Containers:

| Hostname                | Port | Protocol | IP      | Notes                                 |
|-------------------------|------|----------|---------|---------------------------------------|
| cgr.dev                 | 443  | HTTPS    | v4      | Main container image registry         |
| console.chainguard.dev  | 443  | HTTPS    | v4      | Chainguard dashboard                  |
| data.chainguard.dev     | 443  | HTTPS    | v4      | Console API endpoint                  |
| console-api.enforce.dev | 443  | HTTPS    | v4      | Registry API endpoint                 |
| enforce.dev             | 443  | HTTPS    | v4      | Registry authentication               |
| dl.enforce.dev          | 443  | HTTPS    | v4      | `chainctl` downloads                  |
| issuer.enforce.dev      | 443  | HTTPS    | v4      | Registry STS (Security Token Service) |
| apk.cgr.dev             | 443  | HTTPS    | v4      | Package repository                    |
| virtualapk.cgr.dev      | 443  | HTTPS    | v4      | Package repository                    |
| packages.cgr.dev        | 443  | HTTPS    | v4      | Package repository (Extra packages)   |
| packages.wolfi.dev      | 443  | HTTPS    | v4 & v6 | Package repository (Free containers)  |

> If you experience networking issues while trying to use Chainguard Containers, please ensure that your firewall allows traffic to and from these hosts, and that it doesn't have any rules to block `.dev` domains.

## Chainguard Containers third-party hosts

This table lists the third-party DNS hostnames, associated ports, and protocols that will need to be allowed through firewalls and proxies to use Chainguard Containers:

| Hostname                                                  | Port | Protocol | IP      | Notes                                                    |
|-----------------------------------------------------------|------|----------|---------|----------------------------------------------------------|
| 9236a389bd48b984df91adc1bc924620.r2.cloudflarestorage.com | 443  | HTTPS    | v4 & v6 | Blob storage for *.cgr.dev                               |
| support.chainguard.dev                                    | 443  | HTTPS    | v4      | Support access for customers                             |
| tuf-repo-cdn.sigstore.dev                                 | 443  | HTTPS    | v4      | Sigstore trust root for `chainctl` signature verification |

> Note that the `9236a389bd48b984df91adc1bc924620.r2.cloudflarestorage.com` host is used to serve both image data and packages via `*.cgr.dev`.

## Ingress and egress

Connections to the hosts listed on this page are generally initiated as new outbound connections. If you are using stateless firewall rules, then you will need to add symmetric rules to ensure that traffic flows correctly.

You will need egress rules that allow new traffic to the hosts listed here. You will need corresponding ingress rules that allow related and established traffic.

## DNS records and TTLs

Many of the hosts listed on this page use multiple DNS A records or CNAME aliases. Additionally, many A records have a short time to live of 60 seconds, and the majority are less than an hour (3600s).

If your network filters traffic based on IP addresses, ensure that any firewalls update their rules at an appropriate interval to match the TTL for each DNS record.

## Minimum TLS parameters requirements

For guaranteed connectivity, the following TLS requirements must be at
minimum supported by clients and servers communicating with Chainguard
Containers and endpoints:

Protocol Versions:

- TLSv1.3
- TLSv1.2

TLS Cipher Suites:

- TLS_AES_256_GCM_SHA384
- TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
- TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384

TLS Supported Groups:

- X25519MLKEM768
- secp384r1

TLS Signature Schemes:

- ecdsa_secp256r1_sha256
- rsa_pss_pss_sha256

Protocol support:

- Support for encrypted HTTP/2 is required, including by any proxies in use

The requirements can be approximately tested with the following OpenSSL client command:

```shell
openssl s_client -cipher @SECLEVEL=2:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 -ciphersuites TLS_AES_256_GCM_SHA384 -groups X25519MLKEM768:secp384r1 -alpn h2 -connect cgr.dev:443 < /dev/null
```

> Note that in the case of TLSv1.2 connectivity you must check the output for `Extended master secret: yes`.

You can replace `cgr.dev:443` with your own deployments.

Many of the endpoints for Chainguard products require support for the encrypted [HTTP/2 protocol](https://http2.github.io/). Some decrypting proxies might not support HTTP/2.

{{< blurb/noproxy >}}
