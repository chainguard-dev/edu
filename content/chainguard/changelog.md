---
title: "Chainguard products changelog"
linktitle: "Changelog"
type: "article"
description: "Weekly changelog of Chainguard product updates — product announcements, breaking changes, container images reaching end-of-life or leaving the catalog, and images newly added to it."
date: 2026-07-28T00:00:00+00:00
lastmod: 2026-08-31T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Changelog"]
images: []
weight: 070
toc: true
tocEndLevel: 2
---

This page logs Chainguard product updates week by week, newest first: product announcements, breaking changes, container images that reached end-of-life or are no longer available, and images newly added to the catalog. Each event is listed once, in the week it first appeared.

Breaking changes and product announcements cover the entire Chainguard portfolio, while end-of-life, availability, and new-image entries relate specifically to Chainguard Containers. This page summarizes the changes most likely to affect your work rather than every change Chainguard ships. Routine updates, such as new tags for existing images, are not listed individually. For the current tags and versions of any container image, refer to its entry in the [Chainguard Directory](https://images.chainguard.dev/directory).

## Week of 2026-08-31

{{< changelog-label "Product Announcements" >}}

### chainctl fixes for standard Windows accounts

_Launched August 26, 2026._

Several `chainctl` workflows now work for standard, non-administrator Windows users:

- Configuring Docker credentials no longer requires symlinks or Developer Mode.
- Self-update replaces the running executable correctly and checks release attestations before installing.
- Library verification checks signatures in-process and cleans up its temporary directories reliably.
- Authentication failures report an error instead of a misleading 0.00% coverage result.

These are targeted fixes. Chainguard's official Windows support tier is unchanged.

### Custom container policies (open beta)

_Launched August 25, 2026._

Organizations enabled for the beta can now write their own container pull policies instead of relying only on Chainguard's system policies. Custom policies are [Rego](https://www.openpolicyagent.org/docs/policy-language) expressions submitted as YAML manifests and managed with `chainctl`, so you can keep them in git and validate them in CI.

- Policies can declare parameters, with values set per binding.
- `chainctl policies custom validate` reports the exact line and column of an error before the policy is stored.
- Evaluation runs in a sandbox with no network or filesystem access.
- A custom policy in `ENFORCE` mode blocks pulls, but cannot loosen a system policy.

For more information, refer to [Writing custom policies](/chainguard/chainguard-repository/container-policies/#writing-custom-policies).

### Build pinning for Chainguard Libraries

_Launched August 24, 2026._

Build pinning is now enabled for all organizations using Chainguard Libraries with upstream fallback, across JavaScript, Python, and Java. The first time your organization pulls a package version, Chainguard records which copy you received — the upstream mirror or the Chainguard rebuild — and keeps resolving that version to the same copy until you choose to move forward. This keeps your lockfiles and checksums valid as Chainguard's library coverage grows.

Organizations that do not use upstream fallback see no change. To review what your organization holds, or to opt out, refer to [`chainctl libraries cache`](/platform/chainctl/chainctl-docs/chainctl_libraries_cache/).

{{< changelog-label "EOL" >}}

Chainguard offers [a grace period](/chainguard/containers/features/eol-gp-overview/) for eligible end-of-life images: up to six months of continued rebuilds and security updates while you complete your upgrade.

### Images that are no longer available

The following container images reached the end of their grace period and are no longer available:

| Image | End-of-life | Grace period ended |
| --- | --- | --- |
| `kube-conformance:1.32` | 2026-02-28 | 2026-08-28 |
| `kubernetes:1.32` | 2026-02-28 | 2026-08-28 |
| `nextcloud-server:31` | 2026-02-28 | 2026-08-28 |
| `rke2-runtime:1.32` | 2026-02-28 | 2026-08-28 |
| `teleport:17` | 2026-02-28 | 2026-08-28 |

### Images that have reached end-of-life

The following container images reached end-of-life and entered their grace period:

| Image | End-of-life | Grace period ends |
| --- | --- | --- |
| `istio:1.29` | 2026-08-31 | 2027-02-28 |
| `istio-cni:1.29` | 2026-08-31 | 2027-02-28 |
| `istio-envoy:1.29` | 2026-08-31 | 2027-02-28 |
| `istio-operator:1.29` | 2026-08-31 | 2027-02-28 |
| `istio-pilot-agent:1.29` | 2026-08-31 | 2027-02-28 |
| `istio-pilot-discovery:1.29` | 2026-08-31 | 2027-02-28 |
| `teleport:18` | 2026-08-31 | 2027-02-28 |
| `ztunnel:1.29` | 2026-08-31 | 2027-02-28 |

{{< changelog-label "New Images" >}}

Chainguard built 21 new container images this week, including both standard and FIPS variants.

<table class="cl-images">
<thead><tr><th>Image</th><th>Tier</th><th>Added</th></tr></thead>
<tbody>
<tr><td><a href="https://images.chainguard.dev/directory/image/dynatrace-operator/versions"><code>dynatrace-operator</code></a></td><td>application +fips</td><td>2026-08-24</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/netshoot/versions"><code>netshoot</code></a></td><td>application +fips</td><td>2026-08-24</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/strimzi-drain-cleaner/versions"><code>strimzi-drain-cleaner</code></a></td><td>application +fips</td><td>2026-08-24</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/kube-logging-operator-fluentd-drain-watch/versions"><code>kube-logging-operator-fluentd-drain-watch</code></a></td><td>application +fips</td><td>2026-08-25</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/mlrun-api-fips/versions"><code>mlrun-api-fips</code></a></td><td>fips</td><td>2026-08-25</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/mlrun-fips/versions"><code>mlrun-fips</code></a></td><td>fips</td><td>2026-08-25</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/redpanda-console/versions"><code>redpanda-console</code></a></td><td>application</td><td>2026-08-26</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/apache-polaris/versions"><code>apache-polaris</code></a></td><td>application +fips</td><td>2026-08-28</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/kserve-pmmlserver/versions"><code>kserve-pmmlserver</code></a></td><td>ai +fips</td><td>2026-08-28</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/kserve-xgbserver/versions"><code>kserve-xgbserver</code></a></td><td>ai +fips</td><td>2026-08-28</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/nomad/versions"><code>nomad</code></a></td><td>application +fips</td><td>2026-08-28</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/victorialogs-vlagent/versions"><code>victorialogs-vlagent</code></a></td><td>application +fips</td><td>2026-08-28</td></tr>
</tbody>
</table>

## Week of 2026-08-24

{{< changelog-label "Product Announcements" >}}

### SCIM user provisioning (Early Access)

_Launched August 20, 2026._

Chainguard now supports SCIM user provisioning for Okta and Microsoft Entra ID in Early Access. Assigning a user to the provisioning application creates and updates their Chainguard provisioning record through the SCIM `/Users` resource; deactivating or unassigning them blocks the next login or token refresh once the current token expires, within about an hour. Roles stay under Chainguard's control through default roles, manual bindings, and group-based role mapping. SCIM group provisioning is not available, so leave your identity provider's SCIM group push turned off.

For more information, refer to [SCIM user provisioning](/platform/administration/custom-idps/scim-provisioning/).

### Chainguard API v2 is generally available

_Launched August 19, 2026._

Chainguard API v2 is now generally available at `/v2/`, replacing the `v2beta1` designation with a stable contract covering organization and access management, registry metadata, vulnerability and security advisories, event subscriptions, and library artifacts. It standardizes cursor-based pagination, server-side ordering, resource naming, dedicated resource lookups, partial updates, and typed error details, and ships an OpenAPI specification and v2 Go SDK clients. Existing `v2beta1` integrations keep their request and response shapes and need only update the path prefix. API v1 remains supported during the transition.

For more information, refer to [Migrating from API v1 to API v2](/platform/api/api-v2-migration/).

### Self-serve Helm chart provisioning

_Launched August 18, 2026._

Catalog customers can now provision Chainguard Helm charts from the Chainguard Console instead of filing a request ticket. When you select a chart, the Console identifies the required images your organization is missing, adds them in a single request, and starts provisioning the chart asynchronously; the chart appears in your registry once synchronization completes, without EOL tags. Dependency resolution does not detect renamed images.

For more information, refer to [Self-serve Helm charts](/get-started/self-serve/helm-charts/).

{{< changelog-label "EOL" >}}

Chainguard offers [a grace period](/chainguard/containers/features/eol-gp-overview/) for eligible end-of-life images: up to six months of continued rebuilds and security updates while you complete your upgrade.

### Images that are no longer available

The following container images reached the end of their grace period and are no longer available:

| Image | End-of-life | Grace period ended |
| --- | --- | --- |
| `flux:2.5` | 2026-02-24 | 2026-08-24 |

### Images that have reached end-of-life

The following container images reached end-of-life and entered their grace period:

| Image | End-of-life | Grace period ends |
| --- | --- | --- |
| `grafana:12.3` | 2026-08-19 | 2027-02-19 |
| `py3-numpy:2.1` | 2026-08-19 | 2027-02-19 |

{{< changelog-label "New Images" >}}

Chainguard built 27 new container images this week, including both standard and FIPS variants.

<table class="cl-images">
<thead><tr><th>Image</th><th>Tier</th><th>Added</th></tr></thead>
<tbody>
<tr><td colspan="3">
<details>
<summary><strong><code>airbyte-*</code></strong> — 5 images (with FIPS variants)</summary>
<table>
<thead><tr><th>Image</th><th>Tier</th><th>Added</th></tr></thead>
<tbody>
<tr><td><a href="https://images.chainguard.dev/directory/image/airbyte-bootloader/versions"><code>airbyte-bootloader</code></a></td><td>application +fips</td><td>2026-08-21</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/airbyte-cron/versions"><code>airbyte-cron</code></a></td><td>application +fips</td><td>2026-08-21</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/airbyte-worker/versions"><code>airbyte-worker</code></a></td><td>application +fips</td><td>2026-08-21</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/airbyte-workload-api-server/versions"><code>airbyte-workload-api-server</code></a></td><td>application +fips</td><td>2026-08-21</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/airbyte-workload-launcher/versions"><code>airbyte-workload-launcher</code></a></td><td>application +fips</td><td>2026-08-21</td></tr>
</tbody>
</table>
</details>
</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/percona-server-mongodb-fips/versions"><code>percona-server-mongodb-fips</code></a></td><td>fips</td><td>2026-08-17</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/application-gateway-kubernetes-ingress/versions"><code>application-gateway-kubernetes-ingress</code></a></td><td>application +fips</td><td>2026-08-18</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/falcosidekick-ui/versions"><code>falcosidekick-ui</code></a></td><td>application +fips</td><td>2026-08-18</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/kubernetes-csi-external-health-monitor-fips/versions"><code>kubernetes-csi-external-health-monitor-fips</code></a></td><td>fips</td><td>2026-08-18</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/mlrun/versions"><code>mlrun</code></a></td><td>application</td><td>2026-08-18</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/mlrun-api/versions"><code>mlrun-api</code></a></td><td>application</td><td>2026-08-18</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/spiffe-csi-driver/versions"><code>spiffe-csi-driver</code></a></td><td>application +fips</td><td>2026-08-18</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/apache-activemq-artemis-fips/versions"><code>apache-activemq-artemis-fips</code></a></td><td>fips</td><td>2026-08-19</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/aws-iam-controller/versions"><code>aws-iam-controller</code></a></td><td>application +fips</td><td>2026-08-21</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/commercial-nginx-plus-fips/versions"><code>commercial-nginx-plus-fips</code></a></td><td>commercial</td><td>2026-08-21</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/kserve-lgbserver/versions"><code>kserve-lgbserver</code></a></td><td>ai +fips</td><td>2026-08-21</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/ranger/versions"><code>ranger</code></a></td><td>application</td><td>2026-08-21</td></tr>
</tbody>
</table>

## Week of 2026-08-17

{{< changelog-label "Product Announcements" >}}

### Clearer npm errors for blocked packages

_Launched August 13, 2026._

When Chainguard Libraries withholds an npm package or version — because of detected malware or greyware, a pending malware scan, or a policy block such as a cooldown — npm now returns a `403` naming the specific reason, for example `MALWARE_DETECTED`, instead of the unexplained `404` it returned before. The other supported package managers (pnpm, yarn, uv, poetry, Maven, and Gradle) still report a blocked version as a generic not-found error, and a `409` when an entire package is blocked for malware.

For more information, refer to [Error messages](/chainguard/libraries/troubleshooting/errors/#package-manager-behavior).

### Guardener GitHub App (beta)

_Launched August 12, 2026._

Chainguard Guardener, the automated migration tool, now covers GitHub Actions as well as container images. The GitHub App inventories the Actions in use across your organization's repositories, maps them to hardened Chainguard equivalents, and opens pull requests to swap them in, pinned to a specific SHA rather than a mutable tag. It runs in two modes: an upfront pass that surfaces existing Actions usage and opens migration pull requests, and ongoing standardization that watches workflow files and suggests Chainguard equivalents as new upstream Actions appear.

For more information, refer to [Getting started with Chainguard Guardener](/chainguard/guardener/github/getting-started/).

{{< changelog-label "Breaking Changes" >}}

### Chainguard Libraries build pinning

_Effective August 24, 2026._

Chainguard Repository can serve two copies of the same package version: the upstream copy mirrored from the public registry, and Chainguard's copy rebuilt from source. The two have different checksums, and each request resolves independently, so when Chainguard publishes a rebuild of a version your organization already pulled, the next resolution moves you to the rebuild and its checksum no longer matches your lockfile — surfacing client-side as errors such as `EINTEGRITY` in npm. As of August 24, 2026, build pinning records which copy your organization received the first time it downloads a package version and keeps resolving that version to the same copy until you choose to move forward. Malware and policy blocks apply independently: a version that is later blocked stops being served rather than being replaced with a different copy.

- **Affected:** organizations using Chainguard Libraries with upstream fallback, across JavaScript, Python, and Java. Organizations without upstream fallback see no change.
- **Action:** none required. To keep the current behavior, run `chainctl libraries cache opt-out`. Both `opt-out` and `chainctl libraries cache opt-in` accept `--ecosystem`, and pinning state is tracked per organization and ecosystem. To see which copy each held version came from, run `chainctl libraries cache list`.

For more information, refer to [`chainctl libraries cache`](/platform/chainctl/chainctl-docs/chainctl_libraries_cache/).

{{< changelog-label "EOL" >}}

Chainguard offers [a grace period](/chainguard/containers/features/eol-gp-overview/) for eligible end-of-life images: up to six months of continued rebuilds and security updates while you complete your upgrade.

### Images that are no longer available

The following container images reached the end of their grace period and are no longer available:

| Image | End-of-life | Grace period ended |
| --- | --- | --- |
| `prometheus:3.9` | 2026-02-17 | 2026-08-17 |

### Images that have reached end-of-life

The following container images reached end-of-life and entered their grace period:

| Image | End-of-life | Grace period ends |
| --- | --- | --- |
| `mattermost:10.11` | 2026-08-15 | 2027-02-15 |

{{< changelog-label "New Images" >}}

Chainguard built 17 new container images this week, including both standard and FIPS variants.

<table class="cl-images">
<thead><tr><th>Image</th><th>Tier</th><th>Added</th></tr></thead>
<tbody>
<tr><td><a href="https://images.chainguard.dev/directory/image/azurite/versions"><code>azurite</code></a></td><td>application</td><td>2026-08-10</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/k0s-cni-node/versions"><code>k0s-cni-node</code></a></td><td>application +fips</td><td>2026-08-10</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/peerdb-ui/versions"><code>peerdb-ui</code></a></td><td>application +fips</td><td>2026-08-10</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/scc/versions"><code>scc</code></a></td><td>application +fips</td><td>2026-08-10</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/zitadel-login/versions"><code>zitadel-login</code></a></td><td>application</td><td>2026-08-11</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/aws-lambda-nodejs/versions"><code>aws-lambda-nodejs</code></a></td><td>application +fips</td><td>2026-08-12</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/localstack/versions"><code>localstack</code></a></td><td>application</td><td>2026-08-12</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/kserve-router-fips/versions"><code>kserve-router-fips</code></a></td><td>fips</td><td>2026-08-13</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/jdk-openssl-fips/versions"><code>jdk-openssl-fips</code></a></td><td>fips</td><td>2026-08-14</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/jre-openssl-fips/versions"><code>jre-openssl-fips</code></a></td><td>fips</td><td>2026-08-14</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/kube-router/versions"><code>kube-router</code></a></td><td>application +fips</td><td>2026-08-14</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/commercial-nginx-ingress-plus/versions"><code>commercial-nginx-ingress-plus</code></a></td><td>commercial</td><td>2026-08-17</td></tr>
</tbody>
</table>

## Week of 2026-08-10

{{< changelog-label "Product Announcements" >}}

### Chainguard Libraries available through AWS Security Hub Extended

_Launched August 4, 2026._

AWS added a Supply Chain category to Security Hub Extended and named Chainguard one of its inaugural partners. You can now subscribe to Chainguard Libraries from the Security Hub console and pay through your existing AWS account. Libraries findings arrive normalized to the Open Cybersecurity Schema Framework (OCSF), so they appear alongside your AWS and other partner findings, and AWS Enterprise Support customers receive Level 1 support from AWS.

For more information about the catalog, refer to the [Chainguard Libraries overview](/chainguard/libraries/introduction/overview/).

### Malware avoidance in the Console (beta)

_Launched August 4, 2026._

The Console now shows which malicious and suspicious packages Chainguard Libraries blocked before they reached your environment. A weekly chart tracks the malware and greyware stopped across the Python and JavaScript ecosystems, and a search tool reports why any given package was flagged unsafe. Find it under the **Malware** tab in the Libraries section of the Console sidebar; it is enabled by default for every organization entitled to Libraries.

For more information, refer to [View malware information](/chainguard/libraries/introduction/browse/#view-malware-information).

### PKCE support for custom identity providers

_Launched August 3, 2026._

Chainguard now supports Proof Key for Code Exchange (PKCE) on the OAuth token exchange with custom OIDC identity providers, in line with OAuth 2.1. Administrators can enable it with `chainctl` or the Chainguard API, either alongside an existing client secret or as a secret-free public client.

For more information, including setup steps, refer to [Enable PKCE for OAuth Token Exchange](/platform/administration/custom-idps/enabling-pkce/).

{{< changelog-label "EOL" >}}

Chainguard offers [a grace period](/chainguard/containers/features/eol-gp-overview/) for eligible end-of-life images: up to six months of continued rebuilds and security updates while you complete your upgrade.

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

Chainguard built 23 new container images this week, including both standard and FIPS variants.

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
<tr><td><a href="https://images.chainguard.dev/directory/image/claude/versions"><code>claude</code></a></td><td>application</td><td>2026-08-07</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/codex/versions"><code>codex</code></a></td><td>application</td><td>2026-08-07</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/cruise-control/versions"><code>cruise-control</code></a></td><td>application +fips</td><td>2026-08-07</td></tr>
<tr><td><a href="https://images.chainguard.dev/directory/image/dotstatsuite-supercore/versions"><code>dotstatsuite-supercore</code></a></td><td>application</td><td>2026-08-07</td></tr>
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

Chainguard offers [a grace period](/chainguard/containers/features/eol-gp-overview/) for eligible end-of-life images: up to six months of continued rebuilds and security updates while you complete your upgrade.

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

For more information, including setup steps, refer to [Grant Chainguard roles from identity provider groups](/platform/administration/custom-idps/grant-roles-from-groups/).

{{< changelog-label "EOL" >}}

Chainguard offers [a grace period](/chainguard/containers/features/eol-gp-overview/) for eligible end-of-life images: up to six months of continued rebuilds and security updates while you complete your upgrade.

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
