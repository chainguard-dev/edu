---
title: "Network Requirements"
linktitle: "Network Requirements"
lead: "Using Chainguard Containers with firewalls, access control lists, and proxies"
type: "article"
description: "Using Chainguard Containers with firewalls, access control lists, and proxies"
date: 2023-09-08T08:49:31+00:00
lastmod: 2024-11-20T15:22:20+01:00
draft: false
tags: ["CHAINGUARD IMAGES", "PRODUCT", "REFERENCE"]
images: []
toc: true
weight: 001
---

This document provides an overview of network requirements for using [Chainguard Containers](https://www.chainguard.dev/chainguard-images?utm_source=docs). To use Chainguard tools and Containers in environments with firewalls, VPNs, and IDS/IPS systems, you will need to add some rules to allow traffic into and out of your networks.

Chainguard Containers do not call Chainguard services while running, so no network changes would be required to the runtime environment. Review the **Notes** column for more info on each Hostname.

## Chainguard Containers Hosts

This table lists the DNS hostnames, associated ports, and protocols that will need to be allowed through firewalls and proxies to use Chainguard Containers:

| Hostname                | Port | Protocol | Notes                                           |
| ----------------------- | ---- | -------- | ----------------------------------------------- |
| cgr.dev                 | 443  | HTTPS    | Main container image registry                   |
| console.chainguard.dev  | 443  | HTTPS    | Chainguard dashboard                            |
| data.chainguard.dev     | 443  | HTTPS    | Console API endpoint                            |
| console-api.enforce.dev | 443  | HTTPS    | Registry API endpoint                           |
| enforce.dev             | 443  | HTTPS    | Registry authentication                         |
| dl.enforce.dev          | 443  | HTTPS    | `chainctl` downloads                            |
| issuer.enforce.dev      | 443  | HTTPS    | Registry STS (Security Token Service)           |
| apk.cgr.dev             | 443  | HTTPS    | Package repository                              |
| packages.cgr.dev        | 443  | HTTPS    | Package repository (Extra packages)             |
| packages.wolfi.dev      | 443  | HTTPS    | Package repository (Starter containers)           |



> If you experience networking issues while trying to use Chainguard Containers, please ensure that your firewall allows traffic to and from these hosts, and that it doesn't have any rules to block `.dev` domains.

## Chainguard Containers Third-party Hosts

This table lists the third-party DNS hostnames, associated ports, and protocols that will need to be allowed through firewalls and proxies to use Chainguard Containers:

| Hostname                                                  | Port | Protocol | Notes                        |
| --------------------------------------------------------- | ---- | -------- | ---------------------------- |
| 9236a389bd48b984df91adc1bc924620.r2.cloudflarestorage.com | 443  | HTTPS    | Blob storage for cgr.dev     |
| chainguardhelp.zendesk.com                                | 443  | HTTPS    | Support access for customers |

## Ingress and Egress

Connections to the hosts listed on this page are generally initiated as new outbound connections. If you are using stateful firewall rules, then you will need to add symmetric rules to ensure that traffic flows correctly.

You will need egress rules that allow new traffic to the hosts listed here. You will need corresponding ingress rules that allow related and established traffic.

## DNS Records and TTLs

Many of the hosts listed on this page use multiple DNS A records or CNAME aliases. Additionally, many A records have a short time to live of 60 seconds, and the majority are less than an hour (3600s).

If your network filters traffic based on IP addresses, ensure that any firewalls update their rules at an appropriate interval to match the TTL for each DNS record.
