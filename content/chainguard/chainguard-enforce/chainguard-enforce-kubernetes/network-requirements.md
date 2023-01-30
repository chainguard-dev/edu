---
title: "Network Requirements for Chainguard Enforce"
type: "article"
description: "Ports and Protocols Required for Chainguard Enforce"
date: 2023-01-26T15:22:20
lastmod: 2022-11-29T15:22:20
draft: false
images: []
menu:
  docs:
    parent: "chainguard-enforce-kubernetes"
weight: 100
toc: true
---

> _This document relates to Chainguard Enforce. In order to follow along, you will need access to Chainguard Enforce. You can request access through selecting **Chainguard Enforce for Kubernetes** on the [inquiry form](https://www.chainguard.dev/get-demo?utm_source=docs)._

To use Chainguard Enforce for Kubernetes in environments with firewalls, VPNs, and IDS/IPS systems, you will need to add some rules to allow traffic into and out of your networks. The following table lists the DNS hostnames, associated ports, and protocols that will need to be allowed to communicate with your Kubernetes cluster or clusters.


## Chainguard Hosts

| Hostname |Port |Protocol |
|----------|-----|---------|
| auth.chainguard.dev | 443 | HTTPS |
| canary.enforce.dev | 443 | HTTPS |
| console-api.enforce.dev | 443 | HTTPS |
| console.enforce.dev | 443 | HTTPS |
|cosigned-continuous-verification.enforce.dev | 443 | HTTPS |
| dl.enforce.dev | 443 | HTTPS |
| eots-omni.enforce.dev | 443 | HTTPS |
| issuer.enforce.dev | 443 | HTTPS |
| policy-compiler.enforce.dev | 443 | HTTPS |
| policy-conversion.enforce.dev | 443 | HTTPS |
|policy-distribution.enforce.dev | 443 | HTTPS |
| policy-defaulting.enforce.dev | 443 | HTTPS |
| policy-validation.enforce.dev | 443 | HTTPS |
| tsa.enforce.dev | 443 | HTTPS |

## Third-party Hosts
| Hostname |Port |Protocol |
|----------|-----|---------|
| chainguard-cd-nvt30yluzzsmvk7t.edge.tenants.us.auth0.com | 443 | HTTPS |
| googlecode.l.googleusercontent.com | 443 | HTTPS |
| raw.githubusercontent.com | 443 | HTTPS |
| storage.googleapis.com | 443 | HTTPS |

## Additional Notes

### Ingress and Egress 

Connections to the hosts listed here  are initiated as new outbound connections. If you are using stateful firewall rules, then you will need to add symmetric rules to ensure that traffic flows correctly.

You will need egress rules that allow new traffic to the hosts listed here. You will need corresponding ingress rules that allow related and established traffic.

### DNS Records and TTLs

Many of the hosts listed on this page use multiple DNS A records or CNAME aliases. Additionally, many A records have a short time to live of 60 seconds, and the majority are less than an hour (3600s).

If your network filters traffic based on IP addresses, ensure that any firewalls update their rules at an appropriate interval to match the TTL for each DNS record.