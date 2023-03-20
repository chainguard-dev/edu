---
title: "Network Requirements"
type: "article"
description: "Ports and Protocols Required for Chainguard Enforce"
date: 2023-01-26T15:22:20
lastmod: 2023-03-18T15:22:20
draft: false
images: []
menu:
  docs:
    parent: "chainguard-enforce-kubernetes"
weight: 80
toc: true
---

> _This document relates to Chainguard Enforce. In order to follow along, you will need access to Chainguard Enforce. You can request access through selecting **Chainguard Enforce for Kubernetes** on the [inquiry form](https://www.chainguard.dev/get-demo?utm_source=docs)._

This document provides an overview of network requirements and general guidance for using Chainguard Enforce for Kubenetes. To use Enforce in environments with firewalls, VPNs, and IDS/IPS systems, you will need to add some rules to allow traffic into and out of your networks. 

## Enforce Agent Access

Whether you are working with public or private registries, ensure that outbound connections from the Enforce agent (running in the `gulfstream` namespace) are permitted. Also be sure to allow the corresponding return traffic if you are using symmetric firewall rules.

## Enforce SaaS Access

If you are using Enforce in agentless mode, you will need to ensure that your registry is publicly accessible to the agent. Refer to the [CIDR Ranges](#cidr-ranges) section of this page for a list of ranges to add to your firewall rules or access control lists.

## Image Registry Access

Enforce needs access to any registry or registries that are configured for your cluster or containers so that it can validate images and policies. Depending on your environment, you will need to configure your firewalls and access control lists to allow Enforce access.

## Chainguard Hosts

This table lists the DNS hostnames, associated ports, and protocols that will need to be allowed to communicate with your Kubernetes cluster or clusters.

{{< blurb/enforce-domains >}}

## Third-party Hosts
| Hostname |Port |Protocol |
|----------|-----|---------|
| chainguard-cd-nvt30yluzzsmvk7t.edge.tenants.us.auth0.com | 443 | HTTPS |
| googlecode.l.googleusercontent.com | 443 | HTTPS |
| raw.githubusercontent.com | 443 | HTTPS |
| storage.googleapis.com | 443 | HTTPS |

## CIDR Ranges

For cluster and workload discovery to work, and to be able to communicate effectively to and from Chainguard Enforce, you will need to ensure access to and from the following CIDR ranges.

If you are using Google GKE for your cluster, this page explains how to authorize our networks: [Add an authorized network to an existing cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks#add). 

If you are using Amazon EKS then refer to [Amazon EKS cluster endpoint access control](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html).

{{< blurb/enforce-ips >}}

## Ingress and Egress

Connections to the hosts listed on this page are generally initiated as new outbound connections. If you are using stateful firewall rules, then you will need to add symmetric rules to ensure that traffic flows correctly.

You will need egress rules that allow new traffic to the hosts listed here. You will need corresponding ingress rules that allow related and established traffic.

For the CIDR ranges listed here, ensure that you allow incoming connections from those networks. These IPs are used for workload discovery on public clouds.

## DNS Records and TTLs

Many of the hosts listed on this page use multiple DNS A records or CNAME aliases. Additionally, many A records have a short time to live of 60 seconds, and the majority are less than an hour (3600s).

If your network filters traffic based on IP addresses, ensure that any firewalls update their rules at an appropriate interval to match the TTL for each DNS record.

## JA3 Fingerprints

Client traffic for each of the *.enforce.dev domains can be identified by the following JA3 fingerprint data:

### Fullstring
```
771,49195-49199-49196-49200-52393-52392-49161-49171-49162-49172-156-157-47-53-49170-10-4865-4866-4867,0-5-10-11-13-65281-16-18-43-51,29-23-24-25,0
```

### Fingerprint
```
3fed133de60c35724739b913924b6c24
```
