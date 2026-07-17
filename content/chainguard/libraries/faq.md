---
title: "Chainguard Libraries FAQ"
linktitle: "FAQ"
description: "Frequently asked questions about Chainguard Libraries, including security benefits, supported ecosystems, and how automated patching protects against supply chain attacks"
type: "article"
date: 2025-03-25T08:04:00+00:00
lastmod: 2026-07-16T15:09:59+00:00
draft: false
tags: ["Chainguard Libraries", "Overview"]
menu:
  docs:
    parent: "libraries"
    identifier: "Libraries FAQ"
weight: 010
toc: true
---

## What security issues can Chainguard Libraries prevent?

As detailed on the [background](/chainguard/libraries/overview/#background) and
[introduction](/chainguard/libraries/overview/#introduction) pages, Chainguard
Libraries are built directly from source in the Chainguard Factory and the
resulting binaries are directly provided to you by Chainguard. Chainguard
operates the whole supply chain for the package lifecycle as one reliable,
secure partner. You can therefore avoid issues from the following software
supply chain attack surface points:

* Build pipeline
* Build system
* Dependency injection
* Bypass of CI/CD systems
* Library distribution
* Library consumption

More information about these stages in the software supply chain is available on the [Supply chain
Levels for Software Artifacts (SLSA) website](https://slsa.dev/).

The following examples are issues, attacks, and compromises that affect stages
of the software supply chain for libraries across different language ecosystems:

{{< details "Malicious GlueStack packages" >}}

* This May 2025 attack uploaded compromised packages to PyPI and npm that enable remote shell access and uploading files to compromised machines
* Chainguard Libraries would have protected against this attack. First, the packages have invalid upstream source URLs so there was no source repository. In the case of the lone exception (a package with a valid source repository link), no code was present for Chainguard to build a valid package.
* [The Hacker News](https://thehackernews.com/2025/06/new-supply-chain-malware-operation-hits.html) blog post on the attack

{{< /details >}}

{{< details "Ultralytics Python project" >}}

* Attackers compromised the GitHub Actions workflows for the Ultralytics repository, injecting malware
  into PyPI package releases.
* Attackers pushed out four malicious versions of the Ultralytics YOLO project over the course of a week (8.3.41, 8.3.42, 8.3.45, 8.3.46).
* Ultralytics YOLO is a widely-used fast object detection neural network library downloaded about five million times per month. Users affected during this period were infected with cryptomining malware.
* Chainguard Libraries would have prevented this attack by building the project from clean source. No source code was modified by attackers during this incident.
* See also [PyPI attack analysis](https://blog.pypi.org/posts/2024-12-11-ultralytics-attack-analysis/) and
  [bleepingcomputer blog post](https://www.bleepingcomputer.com/news/security/ultralytics-ai-model-hijacked-to-infect-thousands-with-cryptominer/).

{{< /details >}}

{{< details "Lottie Player" >}}

* Hackers gained access to the NPM registry by compromising a developer authentication token.
* Token used to upload a compromised version of Lottie Player.
* The malicious package drained crypto wallet funds.
* Chainguard Libraries would have prevented this attack by building the project from clean source. No source code was modified by attackers during this incident.
* See also [npm package Lottie-Player compromised in supply chain attack, Nov 2024](https://www.infosecurity-magazine.com/news/npm-package-lottieplayer-supply/).

{{< /details >}}

{{< details "MavenGate" >}}

* MavenGate is a proof of concept for exploiting abandoned Java library domains.
* Vulnerabilities in Maven dependency management allow unauthorized package replacements.
* All Java build tools using Maven repositories, including Maven, Gradle, and
  Ant, could be affected.
* MavenGate relied on the use of multiple repositories and any attack with the
  proposed mechanism would not publish source code. Chainguard Libraries replace other repositories and the use of Chainguard Libraries, based on
  building from the original source, would have prevented an attack using this approach
* See also [_The Hacker News_ article](https://thehackernews.com/2024/01/hackers-hijack-popular-java-and-android.html),
  [_Oversecured_ blog post](https://blog.oversecured.com/Introducing-MavenGate-a-supply-chain-attack-method-for-Java-and-Android-applications/),
  and [Sonatype's take as Maven Central
  operator](https://www.sonatype.com/sonatypes-ongoing-commitment-to-maven-central).

{{< /details >}}

{{< details "XZ Utils backdoor" >}}

* Example of a supply chain attack leveraging social engineering by a patient actor
* Sophisticated backdoor that had remote code execution capability and the potential to affect many systems
* Vulnerability was patched within hours of disclosure by reverting to a
  previous version known to be safe.
* Malicious source tarball and binaries were distributed successfully, but
  source code repository was not compromised.
* Since no source code was compromised, a similar attack on a protected library ecosystem
  would be prevented by Chainguard Libraries
* XZ Utils is written in C and therefore not available as an ecosystem protected by Chainguard Libraries. However, Chainguard Containers include XZ Utils packages. These are also built
  from source and are not affected.
* See also [Wikipedia article](https://en.wikipedia.org/wiki/XZ_Utils_backdoor)
  and [official page from the XZ data compression](https://tukaani.org/xz-backdoor/).

{{< /details >}}

{{< details "Other examples and resources" >}}

The following links provide details for other software supply chain attacks.
Depending on the exact details some of these attacks and approaches are
prevented by use of Chainguard Libraries.

* [Successful supply chain attack on Solana JS library](https://socket.dev/blog/supply-chain-attack-solana-web3-js-library)
* [PyPI packages without source](https://thehackernews.com/2024/12/researchers-uncover-pypi-packages.html)
* [Compromised PyTorch nightly](https://pytorch.org/blog/compromised-nightly-dependency/)
* [Commercial artifacts with RCE vulnerability and without source on PyPI, Aug 2024](https://giraffesecurity.dev/posts/amazon-hat-trick/)
* [Thwarted attempts to flood npm registry](https://www.sonatype.com/blog/crypto-enthusiasts-flood-npm-with-281000-bogus-packages-overnight)
* [PyPI Python library "aiocpa" found exfiltrating crypto keys via Telegram bot, Nov 2024](https://thehackernews.com/2024/11/pypi-python-library-aiocpa-found.html)
* [Supply chain attack detected in Solana's web3.js library. Dec 2024](https://socket.dev/blog/supply-chain-attack-solana-web3-js-library)
* [PyTorch namespace (dependency) confusion attack](https://www.sonatype.com/blog/pytorch-namespace-dependency-confusion-attack)
* [Typo squatting attempt to gain credentials](https://socket.dev/blog/malicious-maven-package-exfiltrates-oauth-credentials)
* [Typo squatting attempts on Maven Central](https://www.sonatype.com/blog/malware-removed-from-maven-central)
* [tj-actions GitHub action issue as example of build infrastructure supply chain compromise](https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-tj-actionschanged-files-cve-2025-30066-and-reviewdogaction)

Find pointers to further resources in the [Software supply chain reading
list](https://github.com/chainguard-dev/ssc-reading-list).

{{< /details >}}

## Why do the Chainguard library checksums differ from those published by upstream repositories?

Chainguard rebuilds libraries from source in a controlled environment to improve supply-chain security. As a result, while functionality remains the same, build metadata and generated content, such as SBOMs, differs from upstream distributions. Whether Chainguard library checksums match upstream depends on the ecosystem and build process.

During initial migration to Chainguard Libraries, some common causes of checksum errors include:

* Artifacts were previously cached from upstream repositories
    * Example: Maven's `.m2` or Gradle's cache.
* Dependencies are pinned to upstream checksums or hashes
    * Example: JavaScript's `package-lock.json` or `yarn.lock`.
* Repository managers or build tools enforce strict verification
    * Example: Artifactory validating against Maven Central.

## What’s the difference between malware‑hardened libraries and CVE remediation?

Malware‑hardened libraries are the baseline Chainguard Libraries experience:
Chainguard rebuilds open source Java, JavaScript, and Python dependencies from
upstream source in the [Chainguard Factory](/platform/factory/), a controlled,
SLSA‑aligned build environment, and publishes them to hardened registries for
customers to consume. This closes off most supply chain malware vectors compared
to pulling directly from public registries like Maven Central, npm, and PyPI.

[CVE remediation](/chainguard/libraries/cve-remediation/) is an additional
feature where Chainguard backports High and Critical vulnerability fixes from
newer upstream releases to older versions that customers are still using,
particularly when upstream maintainers no longer ship patches for those older
versions. Remediated versions are:

* Published in a separate repository:
  `https://libraries.cgr.dev/python-remediated/simple/` for Python and
  `https://libraries.cgr.dev/java-remediated/` for Java.
* Given a local version suffix -- like `+cgr.N` for Python (for example,
  2.0.0+cgr.1) and `-0.cgr.N` for Java -- so dependency resolvers can
  distinguish them from non‑remediated upstream versions while still preferring
  the remediated build during resolution.

## Why might I still see 404s with fallback enabled through Chainguard Repository?

Chainguard offers upstream fallback through the [Chainguard
Repository](/chainguard/chainguard-repository/) as a unified, managed endpoint for each ecosystem. This single endpoint:

* Serves Chainguard‑built packages first, rebuilt from source.
* Optionally falls back to upstream for packages or versions that are not
  yet available from Chainguard.
* Applies security controls on the upstream fallback, including malware and greyware scanning that blocks packages flagged as suspicious, and configurable policies such as cooldown periods.

Because of those controls, you can still see 404s or failed fetches even when
fallback is enabled, for example when:

* A package or version is blocked by malware detection and therefore
  intentionally not served from upstream.
* A recently published version is still in the cooldown period, so the
  repository will not yet proxy it from npm.
* The requested package/version truly does not exist in either Chainguard’s
  catalog or upstream.

Fallback respects security policies first, then mirrors safe content from upstream.
For customers, this can surface as a 404 from the Chainguard endpoint even
though a version appears in the public registry.

## What are Chibbies?

Chibbies is the internal codename for the Chainguard Libraries. It evolved from
Chainguard Libraries being shortened to Chainguard Libbies, and then [finally to
Chibbies](https://www.youtube.com/watch?v=adfU9LJg3I0&t=2843s).

## JFrog Artifactory troubleshooting

The following questions apply to repo manager configurations for Chainguard Libraries, using JFrog Artifactory. Learn more about using a repo manager in the global configuration pages for each ecosystem: [Java](/chainguard/libraries/java/global-configuration/), [JavaScript](/chainguard/libraries/javascript/global-configuration/), [Python](/chainguard/libraries/python/global-configuration/).

### What are the most common setup mistakes when using Artifactory with Chainguard Libraries?

Follow these steps for general troubleshooting:

* Verify the token and repository settings.
  * Confirm that the token is scoped correctly, not expired, and copied correctly. Also confirm that the repository URL is the correct language-specific endpoint and that the expected remote repository settings are in place.
* Validate pulling packages with direct access.
  * Attempt to pull a package directly from the Chainguard endpoint from a controlled environment. This helps you confirm that the token works and that the package is available independently of Artifactory.
  * Attempt to pull the same package through the Artifactory remote or virtual repository and compare the result. 
  * If direct access works but the Artifactory path fails, check the network path between Artifactory and the Chainguard endpoint. This is where firewall restrictions, proxy behavior, TLS inspection, or object-storage allowlisting issues may have an impact. 
* Test with a real package fetch.
  * The **Test** button in Artifactory is not a reliable way to confirm that your integration is working as expected. Instead, use a real package fetch, install, or checksum comparison.
* If results aren't as expected, [clear one cache layer at a time and rerun the same test](#why-might-i-experience-inconsistent-fallback-behavior-outdated-package-metadata-or-inconsistent-experience-between-users). 

### Why might I see TLS or SSL handshake errors and authentication failures after configuring Artifactory with Chainguard Libraries?

In some cases, authentication failures or malformed token behavior are caused by traffic inspection or proxy-layer handling. When troubleshooting, check the following:

* Whether a proxy, TLS inspection layer, or MITM device is in path
* Whether the full certificate chain is installed correctly
* Whether the environment uses an internal CA
* Whether the runtime, package manager, and repository manager trust the same CA bundle
* Whether the proxy is modifying or normalizing headers, tokens, or request format

### Why might I experience timeouts or "connection refused" errors after configuring Artifactory with Chainguard Libraries?

Firewall rules can prevent dependency resolution or break integration behavior. This is often observed when the repository manager can reach one destination but not another required upstream host or storage host. When troubleshooting, check the following:

* Allowed outbound destinations
* DNS resolution
* Port restrictions
* Whether the repository manager can reach all required upstream hosts
* Whether object-storage or redirect targets also need to be allowlisted

### Why might I experience authentication loops, 4xx or 5xx responses, incorrect endpoint routing, stale artifacts, or behavior that differs between direct and proxied paths after configuring Artifactory with Chainguard Libraries?

Proxy layers can change headers, certificate handling, path routing, protocol support, and cache behavior. When troubleshooting, check the following:

* Whether a forward proxy, reverse proxy, or both are present
* Header rewriting
* Path rewriting
* Auth forwarding
* TLS termination point
* HTTP/2 support where required
* Cache behavior at each layer

### Why might I experience inconsistent fallback behavior, outdated package metadata, or inconsistent experience between users after configuring Artifactory with Chainguard Libraries?

Caching is a common cause of unexpected behavior during onboarding and testing.
Builds can continue using previously cached public-registry artifacts or stale
metadata even after you switch a repository over to Chainguard. When
troubleshooting, check the following:

* Local package manager cache
* Artifact repository cache
* Proxy cache
* CI/CD runner cache

Clear one cache layer at a time and rerun the same test after each change. Avoid
clearing multiple cache layers simultaneously unless the steps are documented.
If you are switching an existing Artifactory repository to Chainguard,
invalidate or zap the remote cache before concluding that the configuration is
broken.