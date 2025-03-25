---
title: "Chainguard Libraries FAQ"
linktitle: "FAQ"
type: "article"
description: "Frequently asked questions and answers for Chainguard Libraries users"
draft: false
tags: ["Chainguard Libraries", "Overview"]
menu:
  docs:
    parent: "libraries"
weight: 003
toc: true
---

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

Importantly [over 95% of all known vulnerable components have a fixed version
available](https://www.sonatype.com/blog/are-unnecessary-vulnerabilities-polluting-your-software-supply-chain)
and by adopting those newer versions in your application you can remediate most
CVEs. Chainguard Libraries for Java includes those newest versions and adds the
build and distribution channel security.
