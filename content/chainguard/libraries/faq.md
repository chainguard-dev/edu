---
title: "Chainguard Libraries FAQ"
linktitle: "FAQ"
description: "Frequently asked questions and answers for Chainguard Libraries users"
type: "article"
date: 2025-03-25T08:04:00+00:00
lastmod: 2025-04-07T14:47 :00+00:00
draft: false
tags: ["Chainguard Libraries", "Overview"]
menu:
  docs:
    parent: "libraries"
weight: 004
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

### Malicious GlueStack Packages

* This May 2025 attack uploaded compromised packages to PyPI and npm that enable remote shell access and uploading files to compromised machines
* Chainguard Libraries would have protected against this attack. First, the packages have invalid upstream source URLs so there was no source repository. In the case of the lone exception (a package with a valid source repository link), no code was present for Chainguard to build a valid package.
- [The Hacker News](https://thehackernews.com/2025/06/new-supply-chain-malware-operation-hits.html) blog post on the attack

### Ultralytics Python project

* Attackers compromised the GitHub Actions workflows for the Ultralytics repository, injecting malware
  into PyPI package releases.
* Attackers pushed out four malicious versions of the Ultralytics YOLO project over the course of a week (8.3.41, 8.3.42, 8.3.45, 8.3.46).
* Ultralytics YOLO is a widely-used fast object detection neural network library downloaded about five million times per month. Users affected during this period were infected with cryptomining malware.
* Chainguard Libraries would have prevented this attack by building the project from clean source. No source code was modified by attackers during this incident.
* See also [PyPI attack analysis](https://blog.pypi.org/posts/2024-12-11-ultralytics-attack-analysis/) and
  [bleepingcomputer blog post](https://www.bleepingcomputer.com/news/security/ultralytics-ai-model-hijacked-to-infect-thousands-with-cryptominer/).

### Lottie Player

* Hackers gained access to the NPM registry by compromising a developer authentication token.
* Token used to upload a compromised version of Lottie Player.
* The malicious package drained crypto wallet funds.
* Chainguard Libraries would have prevented this attack by building the project from clean source. No source code was modified by attackers during this incident.
* See also [npm package Lottie-Player compromised in supply chain attack, Nov 2024](https://www.infosecurity-magazine.com/news/npm-package-lottieplayer-supply/).

### MavenGate

* MavenGate is a proof of concept for exploiting abandoned Java library domains.
* Vulnerabilities in Maven dependency management allow unauthorized package replacements.
* All Java build tools using Maven repositories, including Maven, Gradle, and
  Ant, could be affected.
* MavenGate relied on the use of multiple repositories and any attack with the
  proposed mechanism would not publish source code. Chainguard Libraries use
  replaces other repositories and the use of Chainguard Libraries, based on
  building from the original source, would have prevented an attack using this approach
* See also [_The Hacker News_ article](https://thehackernews.com/2024/01/hackers-hijack-popular-java-and-android.html),
  [_Oversecured_ blog post](https://blog.oversecured.com/Introducing-MavenGate-a-supply-chain-attack-method-for-Java-and-Android-applications/),
  and [Sonatype's take as Maven Central
  operator](https://www.sonatype.com/sonatypes-ongoing-commitment-to-maven-central).

### XZ Utils backdoor

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

### Other examples and resources

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

## Does Chainguard Libraries for Java include CVE remediation fixes?

Short answer: 

No. Libraries are built from source code in the secured and hardened Chainguard
infrastructure. This eliminates any build and distribution stage
vulnerabilities.

More details:

Chainguard cannot patch Java libraries and create binaries with the same
identifier because the complete behavior and API surface of every library
affects the use. That use however is part of the application development of each
customer. It varies widely and any change potentially creates incompatibilities,
different behavior or even new security issues. 

Chainguard collaborates with many upstream projects and can collaborate with
customers to increase and accelerate the creation and adoption of fixes and the
work towards new releases.

Importantly, [over 95% of all known vulnerable components have a fixed version
available](https://www.sonatype.com/blog/are-unnecessary-vulnerabilities-polluting-your-software-supply-chain)
and, by adopting those newer versions in your application, you can remediate most
CVEs. Chainguard Libraries for Java includes those newest versions and adds the
build and distribution channel security.

## What are Chibbies?

Chibbies is the internal codename for the Chainguard Libraries. It evolved from
Chainguard Libraries being shortened to Chainguard Libbies, and then [finally to
Chibbies](https://www.youtube.com/watch?v=adfU9LJg3I0&t=2843s). 
