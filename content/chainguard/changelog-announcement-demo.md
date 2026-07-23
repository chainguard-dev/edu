---
title: "Chainguard Changelog — Announcement Demo"
linktitle: "Changelog - Announcement Demo"
type: "article"
description: "Demo of the changelog with manually entered sections, showing how a breaking change and a product announcement appear at the top of a week."
date: 2026-07-14T00:00:00+00:00
lastmod: 2026-07-14T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Changelog"]
images: []
weight: 080
toc: true
tocEndLevel: 2
---

{{< note >}}
This is a demo page — a copy of the changelog with a sample breaking change and product announcement added to the top of the most recent week, to show how these manually entered sections render. It is not the live changelog; see the [Changelog](/chainguard/changelog/).
{{< /note >}}

This page logs notable Chainguard Containers lifecycle events week by week, newest first: images that entered their end-of-life grace period, images no longer available after their grace period ended, and images newly added to the catalog. Each event is listed once, in the week it first appeared.

## Week of 2026-07-14

{{< changelog-label "Breaking Change" >}}

### `nginx` images now run as a non-root user by default

The `nginx` images below now start as UID `65532` instead of `root`. Containers
that bind to port 80, or write to root-owned paths, will fail to start until
reconfigured.

- **Affected:** `nginx:1.27`, `nginx:1.28` (and their `-fips` variants).
- **Action:** listen on port 8080 (or another port above 1024) and make any
  mounted paths writable by UID `65532`.

{{< changelog-label "EOL" >}}

Chainguard offers [a grace period](/chainguard/chainguard-images/features/eol-gp-overview/) for eligible end-of-life images: up to six months of continued rebuilds and security updates while you complete your upgrade.

The following images reached the end of their grace period and are no longer available:

| Image | End-of-life | Grace period ended |
| --- | --- | --- |
| `envoy:1.33` | 2026-01-14 | 2026-07-14 |

The following images reached end-of-life and entered their grace period:

| Image | End-of-life | Grace period ends |
| --- | --- | --- |
| `pdns:5.1` | 2026-07-08 | 2027-01-08 |
| `cloud-sql-proxy:2.18` | 2026-07-11 | 2027-01-11 |
| `affinity-clickhouse:23.3` | 2026-07-14 | 2027-01-14 |
| `altinity-clickhouse:23.3` | 2026-07-14 | 2027-01-14 |

{{< changelog-label "New Image" >}}

Chainguard built 21 new container images this week, including both standard and FIPS variants.

<table class="cl-images">
<thead><tr><th>Image</th><th>Tier</th><th>Added</th></tr></thead>
<tbody>
<tr><td colspan="3">
<details>
<summary><strong><code>crossplane-aws-*</code></strong> — 10 images (with FIPS variants)</summary>
<table>
<thead><tr><th>Image</th><th>Tier</th><th>Added</th></tr></thead>
<tbody>
<tr><td><code>crossplane-aws-budgets</code></td><td>application +fips</td><td>2026-07-14</td></tr>
<tr><td><code>crossplane-aws-cloud9-fips</code></td><td>fips</td><td>2026-07-14</td></tr>
<tr><td><code>crossplane-aws-codepipeline</code></td><td>application +fips</td><td>2026-07-14</td></tr>
<tr><td><code>crossplane-aws-configservice</code></td><td>application +fips</td><td>2026-07-14</td></tr>
<tr><td><code>crossplane-aws-dax</code></td><td>application +fips</td><td>2026-07-14</td></tr>
<tr><td><code>crossplane-aws-dms</code></td><td>application +fips</td><td>2026-07-14</td></tr>
<tr><td><code>crossplane-aws-imagebuilder</code></td><td>application +fips</td><td>2026-07-14</td></tr>
<tr><td><code>crossplane-aws-route53recoveryreadiness-fips</code></td><td>fips</td><td>2026-07-14</td></tr>
<tr><td><code>crossplane-aws-servicecatalog</code></td><td>application +fips</td><td>2026-07-14</td></tr>
<tr><td><code>crossplane-aws-waf</code></td><td>application +fips</td><td>2026-07-14</td></tr>
</tbody>
</table>
</details>
</td></tr>
<tr><td><code>kubeflow-tensorboard-web-app</code></td><td>application +fips</td><td>2026-07-13</td></tr>
<tr><td><code>solr-fips</code></td><td>fips</td><td>2026-07-14</td></tr>
</tbody>
</table>

{{< changelog-label "Product Announcement" >}}

### Container Policies now in open beta

_Launched July 10, 2026._

Container Policies gives DevOps and security teams org-wide, policy-based control
over which container images can be pulled. Three policies are available:

- **`no-eol`** — blocks pulls of end-of-life images.
- **`support-window`** — restricts pulls to long-term-support versions.
- **`cooldown`** — delays new builds for a configurable bake period (7 days by
  default).

Each policy runs in `DRY_RUN` (warn only) or `ENFORCE` (blocking) mode and is
managed at the org level through `chainctl` or the API. Container Policies
replaces custom scripts and third-party registry tooling with built-in
guardrails, so teams no longer have to choose between taking every upstream
update (and risking breaking changes) or freezing versions (and missing security
fixes).

## Week of 2026-07-13

{{< changelog-label "EOL" >}}

Chainguard offers [a grace period](/chainguard/chainguard-images/features/eol-gp-overview/) for eligible end-of-life images: up to six months of continued rebuilds and security updates while you complete your upgrade.

The following images reached the end of their grace period and are no longer available:

| Image | End-of-life | Grace period ended |
| --- | --- | --- |
| `coredns:1.13` | 2026-01-08 | 2026-07-08 |
| `prometheus:3.8` | 2026-01-09 | 2026-07-09 |

The following images reached end-of-life and entered their grace period:

| Image | End-of-life | Grace period ends |
| --- | --- | --- |
| `mariadb:10.6` | 2026-07-06 | 2027-01-06 |

{{< changelog-label "New Image" >}}

Chainguard built 1 new container image this week.

<table class="cl-images">
<thead><tr><th>Image</th><th>Tier</th><th>Added</th></tr></thead>
<tbody>
<tr><td><code>fluent-bit-iamguarded</code></td><td>application</td><td>2026-07-06</td></tr>
</tbody>
</table>

## Week of 2026-07-07

{{< changelog-label "EOL" >}}

Chainguard offers [a grace period](/chainguard/chainguard-images/features/eol-gp-overview/) for eligible end-of-life images: up to six months of continued rebuilds and security updates while you complete your upgrade.

The following images reached the end of their grace period and are no longer available:

| Image | End-of-life | Grace period ended |
| --- | --- | --- |
| `superset:4.1` | 2026-01-04 | 2026-07-04 |
| `keycloak:26.4` | 2026-01-06 | 2026-07-06 |
| `datadog-agent:7.73` | 2026-01-07 | 2026-07-07 |

The following images reached end-of-life and entered their grace period:

| Image | End-of-life | Grace period ends |
| --- | --- | --- |
| `superset:5.0` | 2026-07-01 | 2027-01-01 |
| `perl:5.38` | 2026-07-02 | 2027-01-02 |

{{< changelog-label "New Image" >}}

Chainguard built 6 new container images this week, including both standard and FIPS variants.

<table class="cl-images">
<thead><tr><th>Image</th><th>Tier</th><th>Added</th></tr></thead>
<tbody>
<tr><td><code>kubeflow-pipelines-driver</code></td><td>application</td><td>2026-07-01</td></tr>
<tr><td><code>ansible</code></td><td>application</td><td>2026-07-02</td></tr>
<tr><td><code>opentelemetry-collector-k8s</code></td><td>application +fips</td><td>2026-07-02</td></tr>
<tr><td><code>gitlab-runner-operator</code></td><td>application +fips</td><td>2026-07-03</td></tr>
</tbody>
</table>

## Week of 2026-07-01

{{< changelog-label "EOL" >}}

Chainguard offers [a grace period](/chainguard/chainguard-images/features/eol-gp-overview/) for eligible end-of-life images: up to six months of continued rebuilds and security updates while you complete your upgrade.

The following images reached the end of their grace period and are no longer available:

| Image | End-of-life | Grace period ended |
| --- | --- | --- |
| `haproxy:3.1` | 2026-01-01 | 2026-07-01 |

The following images reached end-of-life and entered their grace period:

| Image | End-of-life | Grace period ends |
| --- | --- | --- |
| `grafana:11.6` | 2026-06-25 | 2026-12-25 |
| `kube-conformance:1.33` | 2026-06-28 | 2026-12-28 |
| `kubernetes:1.33` | 2026-06-28 | 2026-12-28 |
| `rke2-runtime:1.33` | 2026-06-28 | 2026-12-28 |

{{< changelog-label "New Image" >}}

Chainguard built 27 new container images this week, including both standard and FIPS variants.

<table class="cl-images">
<thead><tr><th>Image</th><th>Tier</th><th>Added</th></tr></thead>
<tbody>
<tr><td colspan="3">
<details>
<summary><strong><code>peerdb-flow-*</code></strong> — 4 images</summary>
<table>
<thead><tr><th>Image</th><th>Tier</th><th>Added</th></tr></thead>
<tbody>
<tr><td><code>peerdb-flow-api</code></td><td>application</td><td>2026-06-24</td></tr>
<tr><td><code>peerdb-flow-maintenance</code></td><td>application</td><td>2026-06-24</td></tr>
<tr><td><code>peerdb-flow-snapshot-worker</code></td><td>application</td><td>2026-06-24</td></tr>
<tr><td><code>peerdb-flow-worker</code></td><td>application</td><td>2026-06-24</td></tr>
</tbody>
</table>
</details>
</td></tr>
<tr><td><code>dependency-track-v4-migrator</code></td><td>application</td><td>2026-06-24</td></tr>
<tr><td><code>postgres-operator-logical-backup</code></td><td>application +fips</td><td>2026-06-24</td></tr>
<tr><td><code>swagger-ui</code></td><td>application +fips</td><td>2026-06-24</td></tr>
<tr><td><code>cosmo-router</code></td><td>application +fips</td><td>2026-06-25</td></tr>
<tr><td><code>crossplane-provider-family-gcp</code></td><td>application</td><td>2026-06-25</td></tr>
<tr><td><code>kserve-models-web-app</code></td><td>ai</td><td>2026-06-25</td></tr>
<tr><td><code>kubeflow-katib-tfevent-metrics-collector</code></td><td>application</td><td>2026-06-25</td></tr>
<tr><td><code>starrocks-operator</code></td><td>application +fips</td><td>2026-06-25</td></tr>
<tr><td><code>grafana-otel-lgtm</code></td><td>application +fips</td><td>2026-06-26</td></tr>
<tr><td><code>harvester</code></td><td>application +fips</td><td>2026-06-26</td></tr>
<tr><td><code>tbot-distroless</code></td><td>application</td><td>2026-06-26</td></tr>
<tr><td><code>versitygw</code></td><td>application +fips</td><td>2026-06-26</td></tr>
<tr><td><code>ksops-fips</code></td><td>fips</td><td>2026-06-28</td></tr>
<tr><td><code>apache-tomee</code></td><td>application</td><td>2026-06-29</td></tr>
<tr><td><code>tomcat-iamguarded</code></td><td>application +fips</td><td>2026-06-29</td></tr>
</tbody>
</table>
