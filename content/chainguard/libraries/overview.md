---
title: "Chainguard Libraries overview"
linktitle: "Libraries overview"
description: "Learn about Chainguard Libraries, providing enhanced security for 
    Java, JavaScript, and Python dependencies through automated patching and 
    comprehensive supply chain protection."
type: "article"
date: 2025-03-25T08:04:00+00:00
lastmod: 2025-07-23T15:09:59+00:00
draft: false
tags: ["Chainguard Libraries", "Overview"]
menu:
  docs:
    parent: "libraries"
weight: 001
toc: true
---

[Chainguard Libraries](https://www.chainguard.dev/libraries) provide enhanced
security for open source dependencies in the Java, JavaScript, and Python
ecosystems, addressing critical supply chain vulnerabilities through automated
patching and continuous monitoring. Modern applications rely heavily on
libraries from public repositories like [Maven
Central](https://central.sonatype.com/), [npm Registry](https://www.npmjs.com/),
and [PyPI](https://pypi.org/), but using these repositories introduces supply
chain risks that could expose your applications and system to compromise.

## Background

Open source libraries distributed through public repositories face several
security challenges: maintainers may not promptly address vulnerabilities,
binary artifacts can be compromised, and the sheer volume of transitive
dependencies makes manual security management impractical. While these
repositories enable rapid development, they also introduce supply chain risks
that traditional security approaches struggle to address.

While convenient, these services remove the direct link from your application to
the source code of a specific project, and create a potential risk for quality
issues with the artifacts, man-in-the-middle attacks, removal or override of
libraries with vulnerable or malicious versions, and other issues. The
[Supply-chain Levels for Software Artifacts (SLSA)](https://slsa.dev/)
specification describes these risks and how to protect your software against
them.

Although this is a common way of accessing open source binaries, it requires you
to put tremendous trust into the following aspects for the dozen or even
hundreds of open source libraries you typically use for each application:

* Maintainers and especially release managers of the projects
* Local workstation or CI setup used for the release build
* Release process mechanisms to create the binaries
* Transport of the binaries from the build system to the public repositories
* Management of access to the repositories
* Monitoring of repositories for attacks as well as harmful or malicious
  binaries
* Traffic to public repositories and attacks on the transport to your
  infrastructure

There are no real guarantees as to the actual provenance of the software code.
Repositories also vary greatly in quality and there is no guarantee that the
upstream source of a project is available in a repository. In addition, these
repositories also hold non-open source binaries of libraries.

All these factors create uncertainty. Using these public repositories can feel
as opaque as picking up a USB drive off of the sidewalk and plugging it into
your laptop.

## Introduction

Chainguard Libraries builds all available libraries from source code in the
Chainguard Factory and makes them available for you. The Chainguard Factory
is Chainguard's internal tooling that enables a more secure, dedicated,
private, and SLSA-certified build infrastructure for building software from
source and publishing the binaries to customers.

Chainguard Libraries and the use of the Chainguard Factory remove many software
supply chain problems for libraries:

* All binary libraries and library versions are built within the trusted
  Chainguard infrastructure directly from the source code of the official
  project.
* Binaries are handled and managed only by Chainguard and made exclusively
  available for your consumption.
* Any supply chain attacks at build and distribution are eliminated, since all
  steps from the source to your use are handled by Chainguard.
* If there is no open source code available, no binaries are made available by
  Chainguard. This eliminates any license-related risks from commercial
  libraries. The policy and process to have no binaries without source also
  removes the danger from malicious artifacts, since these artifacts do not
  provide source code in public code repositories.

Chainguard Libraries is available for the following library ecosystems:

* Java and the larger Java Virtual Machine (JVM) ecosystem with
  [Chainguard Libraries for Java](/chainguard/libraries/java/overview/)
* JavaScript and the larger ecosystem around JavaScript, TypeScript, npm, React,
  and others with 
  [Chainguard Libraries for JavaScript](/chainguard/libraries/javascript/overview/)
* Python and the larger ecosystem with
  [Chainguard Libraries for Python](/chainguard/libraries/python/overview/)

## Chainguard criteria for building a library

Chainguard Libraries includes thousands of Java, JavaScript, and Python libraries, and coverage is continuously growing as we add more packages and versions over time. Chainguard aims to build libraries that are relevant to our customers and that support broader software supply chain security goals. However, it is not always feasible or safe to rebuild and redistribute every package from public registries such as Maven Central, npm, or PyPI.

### Licensing and source availability

Chainguard Libraries are rebuilt from upstream source code, not mirrored binaries from public registries. For a library to be in scope:

* Source code must be available and verifiable
    * The project’s source must be available in a source code manager (such as GitHub or GitLab). Packages that do not provide a valid or verifiable source URL cannot be rebuilt in the Chainguard Factory and are out of scope.
* Licensing must allow rebuild and redistribution
    * The project must be licensed in a way that allows Chainguard to rebuild and redistribute it to customers.

### Library version support

Chainguard builds libraries using supported language toolchains in our hardened build environment. We do not aim to replicate all historical runtime environments exactly, but we do attempt to preserve runtime compatibility where it is safe to do so. For older or EOL projects, our ability to build and remediate issues is constrained by runtime compatibility and by upstream maintenance practices.

Our current minimum supported toolchains are:

* **Python**: Python 3.10 and higher.
* **Java**: Java 8 and higher.
* **JavaScript**: Any supported, non-EOL version of Node.js. 

We will attempt to rebuild any libraries that meet the [licensing and source availability criteria](#licensing-and-source-availability) using the supported toolchains.

### EOL version support

When a library version reaches end of life (EOL) upstream, Chainguard Libraries continues to build packages and provide security fixes for that version for six months beyond the upstream EOL date.

After that six-month window closes, Chainguard Libraries will:
- No longer build new packages that require the EOL version
- No longer provide security fixes for packages built against the EOL version
- Continue to serve previously built packages

## Upstream fallback and controls

Chainguard Libraries support an optional protected upstream fallback, managed through the [Chainguard
Repository](/chainguard/chainguard-repository/overview/).

By default, the Chainguard library endpoints serve
only Chainguard-built packages. When the upstream fallback is enabled, upstream packages are
subject to additional security controls before being served.

> Note: When using `chainctl` to configure upstream fallback or cooldown duration, it can take up to 30 minutes for the repository changes to take effect.

### Enable the upstream repository

To enable or change upstream fallback configuration, use the [`chainctl
libraries entitlements`
command](/chainguard/chainctl/chainctl-docs/chainctl_libraries_entitlements_create/). 

For example, the following command creates or updates an entitlement to Chainguard Libraries
for JavaScript, and adds the npm upstream fallback policy. Enabling upstream fallback includes a 7-day cooldown by default, which can also be configured:

```bash
chainctl libraries entitlements create --ecosystems=JAVASCRIPT --policy=CHAINGUARD_AND_UPSTREAM 
```

For JavaScript, you can also enable upstream fallback in the Chainguard Console. For Java and Python, you cannot currently enable fallback or view upstream vs. Chainguard-built packages via the Chainguard Console.

### Fallback options

The following options are available:
* **No upstream fallback (default)**: Only Chainguard-built packages are served.
* **Upstream fallback enabled with default 7-day cooldown**: Upstream packages are available after passing a configurable cooldown period and malware scan. The same cooldown period is enforced across Chainguard-built packages and upstream packages, so that dependency trees resolve consistently across both sources.

### Malware and greyware detection

Chainguard's [source code and maintainer behavior
scanning](https://www.chainguard.dev/unchained/the-expanding-threat-landscape-chainguard-now-scans-source-code-for-traditional-malware-and-greyware/)
identifies and blocks malicious and greyware packages in Chainguard Libraries
via the Chainguard Repository. This includes packages that are publicly reported
as malicious (including packages associated with OSV malware IDs) and packages
that Chainguard determines are unsafe through its own malware source code
scanning, even when no public malware advisory exists yet. 

Malware detection is continuous. If a version that was previously cached is
later identified as malicious, it is added to the block list and will be blocked
on subsequent requests.

Chainguard's scanning evaluates multiple signal types, including:

- **Maintainer behavior**: Flags anomalies in publisher accounts, release
  history, and package metadata, checking to see if a maintainer account was
  recently transferred, if a version was quietly yanked and republished, or if a
  publish timestamp falls outside any normal window. It also monitors for
  changes in publishing policy, process, or toolchain as these updates can be an
  indicator of ownership takeover. 
- **Package contents**: Downloads and scans the actual package that was
  published for obfuscated code, embedded C2 domains, modified binaries, and
  other indicators that something fishy was inserted into the package before it
  hit the registry. It also triggers on newly added dependencies and significant
  changes in code or binary size.
- **Publishing signals**: Compares the published package against its source
  code, providing extra protection for all of the packages served via
  Chainguard’s upstream fallback. It also monitors for items such as a release
  not being tagged or being signed with an unknown key. Other publish signals
  include force pushing a tag or a commit hash not being in the event log.
- **Dynamic execution**: Runs install scripts in a sandboxed, network-blocked
  environment to see if there are attempts to call out to an external server,
  read system files, or execute hidden payloads.

Use Chainguard's [malware API endpoint](/chainguard/api/spec-api-v1/#tag/malware) to query malware scanning details.

### Cooldown period

When fallback is enabled, upstream packages are subject to a cooldown period from their publication date before the Chainguard Repository will serve them. The cooldown is an additional layer of security that provides a window for the security community to identify and report malicious packages before your builds can pull them. 

The cooldown applies globally across Chainguard-built packages and upstream packages served through the fallback. This prevents installs from failing when a Chainguard-built package depends on an upstream dependency that is still under the cooldown window.

If a requested package version falls within the cooldown period, the package manager will output a 404 error. The package becomes available once it has passed the cooldown period and cleared malware scanning.

Learn how to create, enforce, disable, and list policies in the [Libraries Access](/chainguard/libraries/access/#policy) page.

### How package resolution works

When you request a package from the Chainguard Repository, the following logic applies:

* **Chainguard-built package available**: The package is served directly from Chainguard's rebuilt artifact store, complete with SBOM, provenance, and signatures, subject to the configured cooldown.
* **Package not yet built by Chainguard**: If upstream fallback is enabled, the repository checks whether the package has passed the cooldown period and malware scan.
    * **Within the cooldown period**: The request returns an error. This prevents newly published packages — which carry higher malware risk — from being served immediately.
    * **After the cooldown period**: If upstream fallback is enabled and the version is outside the cooldown window and passes malware scanning, the repository pulls the version through from the upstream registry, serves it to the client, and caches it in the upstream mirror for future requests.
* **Malware or greyware detected**: Any package version that is detected for malware or greyware is blocked, whether it originates from Chainguard's builds or the upstream fallback.
    * Malware scanning checks all packages against the Open Source Vulnerabilities (OSV) database, which includes the OpenSSF Malicious Packages feed among other sources. Any package version flagged with a malware identifier is blocked. This covers reported malicious packages across the npm ecosystem.

> **Note**: Chainguard Repository is not a full mirror of upstream repositories. Packages are screened for malware before being made available. Some packages may be delayed by the cooldown period or permanently blocked if flagged as malicious.

## Other resources

* [Chainguard Libraries product page](https://www.chainguard.dev/libraries)
* [{{< icon "play-circle-fill" >}} Learning Lab for October 2025 on Chainguard Libraries for JavaScript and CVE remediation for Python libraries](/software-security/learning-labs/ll202510/)
* [{{< icon "play-circle-fill" >}} Learning Lab for June 2025 on Chainguard Libraries for Python](/software-security/learning-labs/ll202506/)
* [{{< icon "play-circle-fill" >}} Learning Lab for May 2025 about Chainguard Libraries for Java](/software-security/learning-labs/ll202505/)

Blog posts

* [Mitigating Malware in the npm Ecosystem with Chainguard Libraries](https://www.chainguard.dev/unchained/mitigating-malware-in-the-npm-ecosystem-with-chainguard-libraries
)
* [Announcing Chainguard Libraries for JavaScript: Malware-Resistant Dependencies Built Securely from Source](https://www.chainguard.dev/unchained/announcing-chainguard-libraries-for-javascript-malware-resistant-dependencies-built-securely-from-source)
* [Registries and the npm Breach: Securing the Weakest Link in the Software Supply Chain](https://www.chainguard.dev/unchained/registries-and-the-npm-breach-securing-the-weakest-link-in-the-software-supply-chain)
* [Malware-Resistant Python without the Guesswork](https://www.chainguard.dev/unchained/malware-resistant-python-without-the-guesswork)
* [This Shit is Hard: Java Archeology at a Massive Scale](https://www.chainguard.dev/unchained/this-shit-is-hard-java-archeology-at-a-massive-scale)
* [Mitigating Malware in the Python Ecosystem with Chainguard Libraries](https://www.chainguard.dev/unchained/mitigating-malware-in-the-python-ecosystem-with-chainguard-libraries)
* [Announcing Chainguard Libraries for Python: Malware-Resistant Dependencies Built Securely from Source](https://www.chainguard.dev/unchained/announcing-chainguard-libraries-for-python-malware-resistant-dependencies-built-securely-from-source)
* [Announcing Chainguard Libraries: Guarded Java Language Dependencies Built from Source](https://www.chainguard.dev/unchained/announcing-chainguard-libraries-guarded-java-language-dependencies-built-from-source)

