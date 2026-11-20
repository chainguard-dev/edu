---
title: "JFrog Curation and Chainguard Libraries"
linktitle: "JFrog Curation"
description: "How JFrog Curation and Catalog recognize Chainguard Libraries, ecosystem coverage, and answers to common Curation questions."
type: "article"
date: 2026-11-10T12:00:00+00:00
lastmod: 2026-11-10T12:00:00+00:00
draft: false
tags: ["Chainguard Libraries", "JFrog", "Curation"]
menu:
  docs:
    parent: "policies-and-security"
weight: 45
toc: true
---

[JFrog Curation](https://jfrog.com/xray/curation/) is a request-time policy
engine that gates which open-source packages can enter JFrog Artifactory. It
evaluates each incoming package against your organization's rules using
metadata from [JFrog Catalog](https://jfrog.com/catalog/), rather than
scanning artifacts itself. [JFrog Xray](https://jfrog.com/xray/) handles
scanning of artifacts already in Artifactory.

When you add Chainguard Libraries as a remote to a JFrog deployment that
already runs Curation, those policies evaluate Chainguard packages alongside
everything else. This page covers how Curation and Catalog recognize Chainguard
Libraries today, which ecosystems are covered, and how to resolve the
conflicts that come up when remediated versions meet existing policies.

For the steps to add Chainguard Libraries as a remote in JFrog Artifactory,
see the JFrog Artifactory sections of the [Java](/chainguard/libraries/java/global-configuration/#jfrog-artifactory),
[JavaScript](/chainguard/libraries/javascript/global-configuration/#jfrog-artifactory),
and [Python](/chainguard/libraries/python/global-configuration/#jfrog-artifactory)
global configuration guides.

## How the integration works

Catalog pre-scans and registers packages so that Curation can evaluate them
against policy before Artifactory serves them. Curation recognizes a remote
repository pointed at a Chainguard endpoint, for example
`https://libraries.cgr.dev/java/`, as a Maven/ChainGuard source and evaluates
it against Chainguard's data. The following minimum versions are required:

- JFrog Artifactory **7.63.5** or later
- JFrog Curation/Xray **3.145.x** or later

When Catalog has already analyzed a package, Curation evaluates it immediately
on the first request. When Catalog has not analyzed it yet, the first pull
may be delayed or fail while JFrog runs an on-demand scan.

## Ecosystem coverage

Curation coverage for Chainguard Libraries differs by ecosystem. The following
reflects the current state as of 2026-11; some rows are still being validated
with JFrog and are expected to evolve.

| Ecosystem        | Chainguard Libraries | Remediated libraries |
| ---------------- | -------------------- | -------------------- |
| Java (Maven)     | Supported            | Supported            |
| JavaScript (npm) | Partial              | Not supported        |
| Python (PyPI)    | Not supported        | Not supported        |

- **Java (Maven):** Catalog pre-registers Chainguard Java packages, so
  Curation evaluates them before the first download. Remediated `-0.cgr.N`
  builds are recognized.
- **JavaScript (npm):** Catalog coverage is incomplete. Catalog pre-registers
  some Chainguard npm packages; the rest fall through to an on-demand scan on
  first pull, which may delay or fail the build. Catalog does not recognize
  remediated `-cgr.N` builds today. Both gaps are on JFrog's roadmap.
- **Python (PyPI):** No Chainguard-specific Catalog or Curation path exists
  today. Standard PyPI workflows through Artifactory may still work, without
  the same integration guarantees.

For the version-suffix conventions, see [CVE remediation for Chainguard
Libraries](/chainguard/libraries/policies-and-security/cve-remediation/#remediated-version-naming).

## Related JFrog products

- **JFrog Artifactory** serves Chainguard Libraries like any other Maven, npm,
  or PyPI remote. See the per-language global configuration guides linked
  earlier.
- **JFrog Xray** scans artifacts stored in Artifactory and recognizes
  Chainguard Libraries for Java through component name and version matching.
  Xray does not yet recognize remediated `-0.cgr.N` builds as containing CVE
  fixes, and it consumes VEX only through CycloneDX VEX workflows generated
  inside the platform, not external feeds such as the Chainguard [public VEX
  feed](/chainguard/libraries/policies-and-security/cve-remediation/#vex). To
  suppress findings on remediated versions, pair Xray with a scanner that
  consumes the Chainguard VEX feed. See [Vulnerability scanners and Chainguard
  Libraries](/chainguard/libraries/policies-and-security/scanners/) for setup
  details.
- **JFrog Zero-Touch Remediation** (part of the JFrog Unified Security bundle)
  routes an application to a Chainguard-remediated version when it identifies
  a vulnerable dependency. It does not require Curation.

## Frequently asked questions

### Should Curation checks be skipped for the Chainguard remote repository?

No. Keep Curation enabled and confirm that Catalog recognizes the Chainguard
remote. Neither JFrog nor Chainguard recommends skipping Curation on the
Chainguard remote.

For Java through a recognized Maven remote, Curation evaluates Chainguard
packages against Chainguard's data and does not re-flag base-version CVEs that
remediated builds fix. For JavaScript and Python, where Catalog coverage is
partial or unavailable, you may need a scoped policy exemption to avoid false
blocks when a build requests a remediated version. Scope exemptions to the
ecosystem rather than skipping the remote wholesale.

### How can I tell whether a `.cgr` version has CVEs before it enters Artifactory?

Each remediated version ships with signed OpenVEX advisories that list the
CVEs it fixes. You can inspect these before ingestion through any of the
following:

- The **Chainguard Console**, under the Remediated tab for the package. See
  [Browsing Chainguard Libraries](/chainguard/libraries/introduction/browse/)
  for navigation.
- The **public VEX feed**: the aggregated file at
  [`https://libraries.cgr.dev/openvex/v1/all.json`](https://libraries.cgr.dev/openvex/v1/all.json),
  or a per-package file (the Python example in the docs is
  `https://libraries.cgr.dev/openvex/v1/pypi/urllib3.openvex.json`).
- [`chainctl libraries packages versions`](/platform/chainctl/chainctl-docs/chainctl_libraries_packages_versions/)
  to list the remediated revisions Chainguard has published for a package.

Scanners that consume the Chainguard VEX feed, including Grype 0.100.0 and
later, Trivy 0.54 and later, and Wiz, flag remediated versions correctly.
See [Vulnerability scanners and Chainguard
Libraries](/chainguard/libraries/policies-and-security/scanners/) for setup
details.

### How can I block an outdated revision such as `.cgr.1` when `.cgr.2` exists?

No documented JFrog mechanism today automatically rejects an older `.cgr`
revision before it reaches an Artifactory cache.

Pin the approved revision in your build configuration instead. In Gradle, a
dynamic version such as `6.2.19-0.cgr.+` tracks the latest revision as new
ones are published. In Maven, use `dependencyManagement` to lock the revision
explicitly. See [Selecting remediated library
versions](/chainguard/libraries/java/build-configuration/#selecting-remediated-library-versions)
for the build-side configuration.

For Curation-side enforcement of specific revisions, confirm with JFrog how
Catalog handles new remediated versions, retractions, and signed VEX evidence
for your deployment.

### How can a developer using a Maven Central version find whether Chainguard has a remediated version, and what the highest `.cgr` revision is?

Use any of these:

- The **Remediated** tab in the Chainguard Console; see [Browsing Chainguard
  Libraries](/chainguard/libraries/introduction/browse/) for navigation.
- [`chainctl libraries packages versions`](/platform/chainctl/chainctl-docs/chainctl_libraries_packages_versions/)
  to list the available revisions for a package.
- The [public VEX feed](#how-can-i-tell-whether-a-cgr-version-has-cves-before-it-enters-artifactory),
  either the aggregated `all.json` or the per-package file.

No public API exists today for querying the latest `.cgr` revision or searching
remediated libraries by CVE. A CVE search API is on the near-term roadmap.

Java remediation is opt-in: builds resolve the upstream version unless the
`java-remediated` repository is configured and the suffixed version is
requested. See [Add remediated
libraries](/chainguard/libraries/java/global-configuration/#add-remediated-libraries)
for the Artifactory setup, and [CVE
remediation](/chainguard/libraries/java/overview/#cve-remediation) in the Java
overview for the version-suffix behavior.

Coverage is a subset of libraries. Java remediation is currently in beta for
Spring Boot; reach out to your account team to request remediation for
additional libraries.

## Related reading

- [CVE remediation for Chainguard Libraries](/chainguard/libraries/policies-and-security/cve-remediation/)
- [Vulnerability scanners and Chainguard Libraries](/chainguard/libraries/policies-and-security/scanners/)
- [Global configuration for Chainguard Libraries for Java: JFrog Artifactory](/chainguard/libraries/java/global-configuration/#jfrog-artifactory)
- [Add remediated libraries (Artifactory)](/chainguard/libraries/java/global-configuration/#add-remediated-libraries)
- [Artifactory pull-through guides for Chainguard Containers](/chainguard/containers/registry/pull-through-guides/artifactory-containers-pull-through/) and [Chainguard APK packages](/chainguard/containers/registry/pull-through-guides/artifactory-packages-pull-through/)
