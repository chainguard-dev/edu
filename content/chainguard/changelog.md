---
title: "Chainguard Products Changelog"
linktitle: "Changelog"
type: "article"
description: "Weekly changelog of Chainguard product updates — product announcements, breaking changes, container images reaching end-of-life or leaving the catalog, and images newly added to it."
date: 2026-07-28T00:00:00+00:00
lastmod: 2026-08-10T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Changelog"]
images: []
weight: 070
toc: true
tocEndLevel: 2
---

This page logs Chainguard product updates week by week, newest first: product announcements, breaking changes, container images that reached end-of-life or are no longer available, and images newly added to the catalog. Each event is listed once, in the week it first appeared.

## Week of 2026-08-10

{{< changelog-label "Product Announcements" >}}

### Chainguard Libraries available through AWS Security Hub Extended

_Launched August 4, 2026._

AWS added a Supply Chain category to Security Hub Extended and named Chainguard one of its inaugural partners. You can now subscribe to Chainguard Libraries from the Security Hub console and pay through your existing AWS account. Libraries findings arrive normalized to the Open Cybersecurity Schema Framework (OCSF), so they appear alongside your AWS and other partner findings, and AWS Enterprise Support customers receive Level 1 support from AWS.

For more information about the catalog, refer to the [Chainguard Libraries overview](/chainguard/libraries/overview/).

### Malware avoidance in the Console (beta)

_Launched August 4, 2026._

The Console now shows which malicious and suspicious packages Chainguard Libraries blocked before they reached your environment. A weekly chart tracks the malware and greyware stopped across the Python and JavaScript ecosystems, and a search tool reports why any given package was flagged unsafe. Find it under the **Malware** tab in the Libraries section of the Console sidebar; it is enabled by default for every organization entitled to Libraries.

For more information, refer to [View malware information](/chainguard/libraries/browse/#view-malware-information).

### PKCE support for custom identity providers

_Launched August 3, 2026._

Chainguard now supports Proof Key for Code Exchange (PKCE) on the OAuth token exchange with custom OIDC identity providers, in line with OAuth 2.1. Administrators can enable it with `chainctl` or the Chainguard API, either alongside an existing client secret or as a secret-free public client.

For more information, including setup steps, refer to [Enable PKCE for OAuth Token Exchange](/platform/administration/custom-idps/enabling-pkce/).

{{< changelog-label "EOL" >}}

Chainguard offers [a grace period](/chainguard/chainguard-images/features/eol-gp-overview/) for eligible end-of-life images: up to six months of continued rebuilds and security updates while you complete your upgrade.

### Images that have reached end-of-life

The following container images reached end-of-life and entered their grace period:

| Image | End-of-life | Grace period ends |
| --- | --- | --- |
| `net-kourier:1.21` | 2026-08-04 | 2027-02-04 |
| `tekton-pipelines:1.3` | 2026-08-04 | 2027-02-04 |
| `ruby3.2-rails:7.2` | 2026-08-09 | 2027-02-09 |
| `ruby3.3-rails:7.2` | 2026-08-09 | 2027-02-09 |
| `ruby3.4-rails:7.2` | 2026-08-09 | 2027-02-09 |
| `ruby4.0-rails:7.2` | 2026-08-09 | 2027-02-09 |

{{< changelog-label "New Images" >}}

Chainguard built 25 new container images this week, including both standard and FIPS variants.

<table class="cl-images">
<thead><tr><th>Image</th><th>Tier</th><th>Added</th></tr></thead>
<tbody>
<tr><td><a href="https://images.chainguard.dev/directory/image/prometheus-stackdriver-exporter/versions"><code>prometheus-stackdriver-exporter</code></a></td><td>application +fips</td><td>2026-08-03</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/crossplane-azure-keyvault/versions"><code>crossplane-azure-keyvault</code></a></td><td>application</td><td>2026-08-04</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/crossplane-azure-kusto/versions"><code>crossplane-azure-kusto</code></a></td><td>application</td><td>2026-08-04</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/influxdb-fips/versions"><code>influxdb-fips</code></a></td><td>fips</td><td>2026-08-04</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/moodle-iamguarded/versions"><code>moodle-iamguarded</code></a></td><td>application</td><td>2026-08-04</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/pypiserver-fips/versions"><code>pypiserver-fips</code></a></td><td>fips</td><td>2026-08-04</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/kubevirt-cdi-cloner/versions"><code>kubevirt-cdi-cloner</code></a></td><td>application +fips</td><td>2026-08-05</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/yopass/versions"><code>yopass</code></a></td><td>application</td><td>2026-08-05</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/acm-controller/versions"><code>acm-controller</code></a></td><td>application +fips</td><td>2026-08-06</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/gremlin-server/versions"><code>gremlin-server</code></a></td><td>application</td><td>2026-08-06</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/rollouts-plugin-trafficrouter-gatewayapi/versions"><code>rollouts-plugin-trafficrouter-gatewayapi</code></a></td><td>application +fips</td><td>2026-08-06</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/chainguard-desktop-workstation-qemu/versions"><code>chainguard-desktop-workstation-qemu</code></a></td><td>base</td><td>2026-08-07</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/claude/versions"><code>claude</code></a></td><td>application</td><td>2026-08-07</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/codex/versions"><code>codex</code></a></td><td>application</td><td>2026-08-07</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/cruise-control/versions"><code>cruise-control</code></a></td><td>application +fips</td><td>2026-08-07</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/dotstatsuite-supercore/versions"><code>dotstatsuite-supercore</code></a></td><td>application</td><td>2026-08-07</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/chainguard-server-workstation-gcp/versions"><code>chainguard-server-workstation-gcp</code></a></td><td>base</td><td>2026-08-08</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/opencode/versions"><code>opencode</code></a></td><td>application</td><td>2026-08-08</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/zalando-pgbouncer/versions"><code>zalando-pgbouncer</code></a></td><td>application +fips</td><td>2026-08-10</td></tr>
</tbody>
</table>

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

Chainguard built 18 new container images this week, including both standard and FIPS variants.

<table class="cl-images">
<thead><tr><th>Image</th><th>Tier</th><th>Added</th></tr></thead>
<tbody>
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

Chainguard built 15 new container images this week, including both standard and FIPS variants.

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
<tr><td><a href="https://images.chainguard.dev/directory/image/glab/versions"><code>glab</code></a></td><td>application +fips</td><td>2026-07-27</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/metabase/versions"><code>metabase</code></a></td><td>application</td><td>2026-07-27</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/crossplane-azure-relay/versions"><code>crossplane-azure-relay</code></a></td><td>application</td><td>2026-07-28</td></tr>
</tbody>
</table>
