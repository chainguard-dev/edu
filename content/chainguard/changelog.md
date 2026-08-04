---
title: "Chainguard Products Changelog"
linktitle: "Changelog"
type: "article"
description: "Weekly changelog of Chainguard product updates — product announcements, breaking changes, container images reaching end-of-life or leaving the catalog, and images newly added to it."
date: 2026-07-28T00:00:00+00:00
lastmod: 2026-07-28T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Changelog"]
images: []
weight: 070
toc: true
tocEndLevel: 2
---

This page logs Chainguard product updates week by week, newest first: product announcements, breaking changes, container images that reached end-of-life or are no longer available, and images newly added to the catalog. Each event is listed once, in the week it first appeared.

## Week of 2026-08-03

{{< changelog-label "Breaking Changes" >}}

### ingress-nginx-controller entrypoint, command, and default user changes

_Effective July 15, 2026._

Chainguard aligned the entrypoint and command behavior of all supported `ingress-nginx-controller` images with the upstream image, correcting a startup configuration defect present since the image was first published in 2024. Non-`iamguarded` variants also changed their default runtime user from `root` (UID 0) to `www-data` (UID 101).

- **Affected:** all supported `ingress-nginx-controller` images, including FIPS and `-iamguarded` variants.
- **Action:** review any configuration that overrides `command`, `args`, `entrypoint`, or `runAsUser`, or that depends on admission policies or file ownership assumptions. Deployments using the upstream Helm chart defaults need no changes.

{{< changelog-label "EOL" >}}

Chainguard offers [a grace period](/chainguard/chainguard-images/features/eol-gp-overview/) for eligible end-of-life images: up to six months of continued rebuilds and security updates while you complete your upgrade.

### Images that are no longer available

The following container images reached the end of their grace period and are no longer available:

| Image | End-of-life | Grace period ended |
| --- | --- | --- |
| `cilium:1.16` | 2026-02-03 | 2026-08-03 |
| `neo4j:2025.12` | 2026-02-03 | 2026-08-03 |

### Images that have reached end-of-life

The following container images reached end-of-life and entered their grace period:

| Image | End-of-life | Grace period ends |
| --- | --- | --- |
| `eks-distro:1.33` | 2026-07-29 | 2027-07-29 |
| `mongo:8.2` | 2026-07-31 | 2027-01-31 |
| `prometheus:3.5` | 2026-07-31 | 2027-01-31 |
| `cockroach:26.1` | 2026-08-02 | 2027-02-02 |
| `cockroach-openssl:26.1` | 2026-08-02 | 2027-02-02 |

{{< changelog-label "New Images" >}}

Chainguard built 22 new container images this week, including both standard and FIPS variants.

<table class="cl-images">
<thead><tr><th>Image</th><th>Tier</th><th>Added</th></tr></thead>
<tbody>
<tr><td><a href="https://images.chainguard.dev/directory/image/glab/versions"><code>glab</code></a></td><td>application +fips</td><td>2026-07-27</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/metabase/versions"><code>metabase</code></a></td><td>application</td><td>2026-07-27</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/atlas/versions"><code>atlas</code></a></td><td>application +fips</td><td>2026-07-29</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/azure-metrics-exporter/versions"><code>azure-metrics-exporter</code></a></td><td>application +fips</td><td>2026-07-29</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/crossplane-azure-solutions/versions"><code>crossplane-azure-solutions</code></a></td><td>application</td><td>2026-07-29</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/crossplane-azure-streamanalytics/versions"><code>crossplane-azure-streamanalytics</code></a></td><td>application</td><td>2026-07-29</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/crossplane-azure-web/versions"><code>crossplane-azure-web</code></a></td><td>application</td><td>2026-07-29</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/dns-controller-manager/versions"><code>dns-controller-manager</code></a></td><td>application +fips</td><td>2026-07-29</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/instrumentisto-haraka/versions"><code>instrumentisto-haraka</code></a></td><td>application +fips</td><td>2026-07-29</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/openstack-kolla-toolbox/versions"><code>openstack-kolla-toolbox</code></a></td><td>application +fips</td><td>2026-07-29</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/sftpgo/versions"><code>sftpgo</code></a></td><td>application</td><td>2026-07-29</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/flink-kubernetes-operator-fips/versions"><code>flink-kubernetes-operator-fips</code></a></td><td>fips</td><td>2026-07-30</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/traccar/versions"><code>traccar</code></a></td><td>application +fips</td><td>2026-07-30</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/metacontroller-fips/versions"><code>metacontroller-fips</code></a></td><td>fips</td><td>2026-07-31</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/chainguard-desktop-workstation-rpi/versions"><code>chainguard-desktop-workstation-rpi</code></a></td><td>base</td><td>2026-08-01</td></tr>
</tbody>
</table>

## Week of 2026-07-28

{{< changelog-label "Product Announcements" >}}

### SUSE NeuVector now natively supports Chainguard Containers

_Launched July 24, 2026._

SUSE's NeuVector vulnerability scanner now natively supports Chainguard Containers and ingests Chainguard's OSV advisory feed, which includes recent data-quality improvements. Scans of Chainguard images suppress false positives and report more accurate results.

### Group-based role mapping is now generally available

_Launched July 22, 2026._

Administrators can map identity provider groups — Okta or Microsoft Entra ID, for example — directly to Chainguard roles, instead of assigning roles one user at a time. Anyone who authenticates with a mapped group in their token receives that role for the session.

For more information, including setup steps, refer to [Grant Chainguard Roles from Identity Provider Groups](/platform/administration/custom-idps/grant-roles-from-groups/).

{{< changelog-label "EOL" >}}

Chainguard offers [a grace period](/chainguard/chainguard-images/features/eol-gp-overview/) for eligible end-of-life images: up to six months of continued rebuilds and security updates while you complete your upgrade.

### Images that are no longer available

The following container images reached the end of their grace period and are no longer available:

| Image | End-of-life | Grace period ended |
| --- | --- | --- |
| `knative-eventing:1.19` | 2026-01-28 | 2026-07-28 |
| `knative-serving:1.19` | 2026-01-28 | 2026-07-28 |
| `net-kourier:1.19` | 2026-01-28 | 2026-07-28 |

### Images that have reached end-of-life

The following container images reached end-of-life and entered their grace period:

| Image | End-of-life | Grace period ends |
| --- | --- | --- |
| `dnsdist:1.9` | 2026-07-21 | 2027-01-21 |
| `longhorn-backing-image-manager:1.8` | 2026-07-22 | 2027-01-22 |
| `longhorn-instance-manager:1.8` | 2026-07-22 | 2027-01-22 |
| `envoy:1.35` | 2026-07-23 | 2027-01-23 |

{{< changelog-label "New Images" >}}

Chainguard built 16 new container images this week, including both standard and FIPS variants.

<table class="cl-images">
<thead><tr><th>Image</th><th>Tier</th><th>Added</th></tr></thead>
<tbody>
<tr><td><a href="https://images.chainguard.dev/directory/image/coder/versions"><code>coder</code></a></td><td>application +fips</td><td>2026-07-22</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/flink-kubernetes-operator/versions"><code>flink-kubernetes-operator</code></a></td><td>application</td><td>2026-07-22</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/pghero/versions"><code>pghero</code></a></td><td>application +fips</td><td>2026-07-22</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/kargo/versions"><code>kargo</code></a></td><td>application</td><td>2026-07-23</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/nuclio-controller/versions"><code>nuclio-controller</code></a></td><td>application +fips</td><td>2026-07-23</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/phpmyadmin/versions"><code>phpmyadmin</code></a></td><td>application +fips</td><td>2026-07-23</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/apache-exporter-iamguarded/versions"><code>apache-exporter-iamguarded</code></a></td><td>application</td><td>2026-07-24</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/rpi-server-bootc/versions"><code>rpi-server-bootc</code></a></td><td>base</td><td>2026-07-25</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/glab/versions"><code>glab</code></a></td><td>application +fips</td><td>2026-07-27</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/metabase/versions"><code>metabase</code></a></td><td>application</td><td>2026-07-27</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/crossplane-azure-relay/versions"><code>crossplane-azure-relay</code></a></td><td>application</td><td>2026-07-28</td></tr>
</tbody>
</table>
