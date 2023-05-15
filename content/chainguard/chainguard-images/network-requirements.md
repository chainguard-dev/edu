---
title: "Network Requirements for Chainguard Images"
lead: "Using Chainguard Images with firewalls, access control lists, and proxies"
type: "article"
description: "Using Chainguard Images with firewalls, access control lists, and proxies"
date: 2023-05-15T08:49:31+00:00
lastmod: 2023-05-15T08:49:31+00:00
draft: false
tags: ["Chainguard Images", "Product", "Reference"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 500
toc: true
---

This document provides an overview of network requirements  for using [Chainguard Images](https://www.chainguard.dev/chainguard-images?utm_source=docs). To use Chainguard Images in environments with firewalls, VPNs, and IDS/IPS systems, you will need to add some rules to allow traffic into and out of your networks.

## Chainguard Hosts

This table lists the DNS hostnames, associated ports, and protocols that will need to be allowed through firewalls and proxies to use Chainguard Images:

| Hostname |Port |Protocol | Notes |
|----------|-----|---------|-------|
| cgr.dev | 443 | HTTPS | Main image registry|
| packages.wolfi.dev | 443 | HTTPS | Package repository|

## Third-party Hosts

This table lists the third-party DNS hostnames, associated ports, and protocols that will need to be allowed through firewalls and proxies to use Chainguard Images:

| Hostname |Port |Protocol |Notes |
|----------|-----|---------|------|
| ghcr.io | 443 | HTTPS | Used for wolfi development|
| *.r2.cloudflarestorage.com | 443 | HTTPS | Blob storage for cgr.dev|

## DNS Records and TTLs

Many of the hosts listed on this page use multiple DNS A records or CNAME aliases. Additionally, many A records have a short time to live of 60 seconds, and the majority are less than an hour (3600s).

If your network filters traffic based on IP addresses, ensure that any firewalls update their rules at an appropriate interval to match the TTL for each DNS record.