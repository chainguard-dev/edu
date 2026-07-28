---
title: "Chainguard Products Changelog"
linktitle: "Changelog"
type: "article"
description: "Weekly changelog of Chainguard product updates — product announcements, breaking changes, container images reaching end-of-life or leaving the catalog, and images newly added to it."
date: 2026-07-14T00:00:00+00:00
lastmod: 2026-07-14T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Changelog"]
images: []
weight: 070
toc: true
tocEndLevel: 2
---

This page logs Chainguard product updates week by week, newest first: product announcements, breaking changes, container images that reached end-of-life or are no longer available, and images newly added to the catalog. Each event is listed once, in the week it first appeared.

## Week of 2026-07-14

{{< changelog-label "EOL" >}}

Chainguard offers [a grace period](/chainguard/chainguard-images/features/eol-gp-overview/) for eligible end-of-life images: up to six months of continued rebuilds and security updates while you complete your upgrade.

### Images that are no longer available

The following container images reached the end of their grace period and are no longer available:

| Image | End-of-life | Grace period ended |
| --- | --- | --- |
| `envoy:1.33` | 2026-01-14 | 2026-07-14 |

### Images that have reached end-of-life

The following container images reached end-of-life and entered their grace period:

| Image | End-of-life | Grace period ends |
| --- | --- | --- |
| `pdns:5.1` | 2026-07-08 | 2027-01-08 |
| `cloud-sql-proxy:2.18` | 2026-07-11 | 2027-01-11 |
| `affinity-clickhouse:23.3` | 2026-07-14 | 2027-01-14 |
| `altinity-clickhouse:23.3` | 2026-07-14 | 2027-01-14 |

{{< changelog-label "New Images" >}}

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
<tr><td><a href="https://images.chainguard.dev/directory/image/crossplane-aws-budgets/versions"><code>crossplane-aws-budgets</code></a></td><td>application +fips</td><td>2026-07-14</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/crossplane-aws-cloud9-fips/versions"><code>crossplane-aws-cloud9-fips</code></a></td><td>fips</td><td>2026-07-14</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/crossplane-aws-codepipeline/versions"><code>crossplane-aws-codepipeline</code></a></td><td>application +fips</td><td>2026-07-14</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/crossplane-aws-configservice/versions"><code>crossplane-aws-configservice</code></a></td><td>application +fips</td><td>2026-07-14</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/crossplane-aws-dax/versions"><code>crossplane-aws-dax</code></a></td><td>application +fips</td><td>2026-07-14</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/crossplane-aws-dms/versions"><code>crossplane-aws-dms</code></a></td><td>application +fips</td><td>2026-07-14</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/crossplane-aws-imagebuilder/versions"><code>crossplane-aws-imagebuilder</code></a></td><td>application +fips</td><td>2026-07-14</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/crossplane-aws-route53recoveryreadiness-fips/versions"><code>crossplane-aws-route53recoveryreadiness-fips</code></a></td><td>fips</td><td>2026-07-14</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/crossplane-aws-servicecatalog/versions"><code>crossplane-aws-servicecatalog</code></a></td><td>application +fips</td><td>2026-07-14</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/crossplane-aws-waf/versions"><code>crossplane-aws-waf</code></a></td><td>application +fips</td><td>2026-07-14</td></tr>
</tbody>
</table>
</details>
</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/kubeflow-tensorboard-web-app/versions"><code>kubeflow-tensorboard-web-app</code></a></td><td>application +fips</td><td>2026-07-13</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/solr-fips/versions"><code>solr-fips</code></a></td><td>fips</td><td>2026-07-14</td></tr>
</tbody>
</table>

## Week of 2026-07-13

{{< changelog-label "EOL" >}}

Chainguard offers [a grace period](/chainguard/chainguard-images/features/eol-gp-overview/) for eligible end-of-life images: up to six months of continued rebuilds and security updates while you complete your upgrade.

### Images that are no longer available

The following container images reached the end of their grace period and are no longer available:

| Image | End-of-life | Grace period ended |
| --- | --- | --- |
| `coredns:1.13` | 2026-01-08 | 2026-07-08 |
| `prometheus:3.8` | 2026-01-09 | 2026-07-09 |

### Images that have reached end-of-life

The following container images reached end-of-life and entered their grace period:

| Image | End-of-life | Grace period ends |
| --- | --- | --- |
| `mariadb:10.6` | 2026-07-06 | 2027-01-06 |

{{< changelog-label "New Images" >}}

Chainguard built 1 new container image this week.

<table class="cl-images">
<thead><tr><th>Image</th><th>Tier</th><th>Added</th></tr></thead>
<tbody>
<tr><td><a href="https://images.chainguard.dev/directory/image/fluent-bit-iamguarded/versions"><code>fluent-bit-iamguarded</code></a></td><td>application</td><td>2026-07-06</td></tr>
</tbody>
</table>

## Week of 2026-07-07

{{< changelog-label "EOL" >}}

Chainguard offers [a grace period](/chainguard/chainguard-images/features/eol-gp-overview/) for eligible end-of-life images: up to six months of continued rebuilds and security updates while you complete your upgrade.

### Images that are no longer available

The following container images reached the end of their grace period and are no longer available:

| Image | End-of-life | Grace period ended |
| --- | --- | --- |
| `superset:4.1` | 2026-01-04 | 2026-07-04 |
| `keycloak:26.4` | 2026-01-06 | 2026-07-06 |
| `datadog-agent:7.73` | 2026-01-07 | 2026-07-07 |

### Images that have reached end-of-life

The following container images reached end-of-life and entered their grace period:

| Image | End-of-life | Grace period ends |
| --- | --- | --- |
| `superset:5.0` | 2026-07-01 | 2027-01-01 |
| `perl:5.38` | 2026-07-02 | 2027-01-02 |

{{< changelog-label "New Images" >}}

Chainguard built 6 new container images this week, including both standard and FIPS variants.

<table class="cl-images">
<thead><tr><th>Image</th><th>Tier</th><th>Added</th></tr></thead>
<tbody>
<tr><td><a href="https://images.chainguard.dev/directory/image/kubeflow-pipelines-driver/versions"><code>kubeflow-pipelines-driver</code></a></td><td>application</td><td>2026-07-01</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/ansible/versions"><code>ansible</code></a></td><td>application</td><td>2026-07-02</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/opentelemetry-collector-k8s/versions"><code>opentelemetry-collector-k8s</code></a></td><td>application +fips</td><td>2026-07-02</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/gitlab-runner-operator/versions"><code>gitlab-runner-operator</code></a></td><td>application +fips</td><td>2026-07-03</td></tr>
</tbody>
</table>

## Week of 2026-07-01

{{< changelog-label "EOL" >}}

Chainguard offers [a grace period](/chainguard/chainguard-images/features/eol-gp-overview/) for eligible end-of-life images: up to six months of continued rebuilds and security updates while you complete your upgrade.

### Images that are no longer available

The following container images reached the end of their grace period and are no longer available:

| Image | End-of-life | Grace period ended |
| --- | --- | --- |
| `haproxy:3.1` | 2026-01-01 | 2026-07-01 |

### Images that have reached end-of-life

The following container images reached end-of-life and entered their grace period:

| Image | End-of-life | Grace period ends |
| --- | --- | --- |
| `grafana:11.6` | 2026-06-25 | 2026-12-25 |
| `kube-conformance:1.33` | 2026-06-28 | 2026-12-28 |
| `kubernetes:1.33` | 2026-06-28 | 2026-12-28 |
| `rke2-runtime:1.33` | 2026-06-28 | 2026-12-28 |

{{< changelog-label "New Images" >}}

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
<tr><td><a href="https://images.chainguard.dev/directory/image/peerdb-flow-api/versions"><code>peerdb-flow-api</code></a></td><td>application</td><td>2026-06-24</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/peerdb-flow-maintenance/versions"><code>peerdb-flow-maintenance</code></a></td><td>application</td><td>2026-06-24</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/peerdb-flow-snapshot-worker/versions"><code>peerdb-flow-snapshot-worker</code></a></td><td>application</td><td>2026-06-24</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/peerdb-flow-worker/versions"><code>peerdb-flow-worker</code></a></td><td>application</td><td>2026-06-24</td></tr>
</tbody>
</table>
</details>
</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/dependency-track-v4-migrator/versions"><code>dependency-track-v4-migrator</code></a></td><td>application</td><td>2026-06-24</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/postgres-operator-logical-backup/versions"><code>postgres-operator-logical-backup</code></a></td><td>application +fips</td><td>2026-06-24</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/swagger-ui/versions"><code>swagger-ui</code></a></td><td>application +fips</td><td>2026-06-24</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/cosmo-router/versions"><code>cosmo-router</code></a></td><td>application +fips</td><td>2026-06-25</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/crossplane-provider-family-gcp/versions"><code>crossplane-provider-family-gcp</code></a></td><td>application</td><td>2026-06-25</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/kserve-models-web-app/versions"><code>kserve-models-web-app</code></a></td><td>ai</td><td>2026-06-25</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/kubeflow-katib-tfevent-metrics-collector/versions"><code>kubeflow-katib-tfevent-metrics-collector</code></a></td><td>application</td><td>2026-06-25</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/starrocks-operator/versions"><code>starrocks-operator</code></a></td><td>application +fips</td><td>2026-06-25</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/grafana-otel-lgtm/versions"><code>grafana-otel-lgtm</code></a></td><td>application +fips</td><td>2026-06-26</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/harvester/versions"><code>harvester</code></a></td><td>application +fips</td><td>2026-06-26</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/tbot-distroless/versions"><code>tbot-distroless</code></a></td><td>application</td><td>2026-06-26</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/versitygw/versions"><code>versitygw</code></a></td><td>application +fips</td><td>2026-06-26</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/ksops-fips/versions"><code>ksops-fips</code></a></td><td>fips</td><td>2026-06-28</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/apache-tomee/versions"><code>apache-tomee</code></a></td><td>application</td><td>2026-06-29</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/tomcat-iamguarded/versions"><code>tomcat-iamguarded</code></a></td><td>application +fips</td><td>2026-06-29</td></tr>
</tbody>
</table>
