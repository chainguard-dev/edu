---
title: "What is software supply chain security"
description: "Software supply chain security - an explanation"
lead: "A beginner's guide to software supply chain security"
type: "article"
date: 2022-08-04T15:21:01+02:00
lastmod: 2022-08-04T15:21:01+02:00
contributors: ["John Speed Meyers"]
draft: false
images: []
menu:
  docs:
    parent: "software-security"
weight: 10
toc: true
---

_An earlier version of this material was published in the [first chapter](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/block-v1:LinuxFoundationX+LFS182x+2T2022+type@sequential+block@1623557b9fc849d5a1e38177502b1499/block-v1:LinuxFoundationX+LFS182x+2T2022+type@vertical+block@825d4b442d1346ba8e9d7c3b4f765e76) of the Linux Foundation [Sigstore course](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/home)._

Software producers have a supply chain just like manufacturing businesses have a supply chain. And just like manufacturers require physical inputs and then perform a manufacturing process to build a finished product, so do software producers, whether the producer is a company or individual. In other words, a software producer uses components, developed by third parties and themselves, and technologies to write, build, and distribute software. A compromise introduced anywhere in this chain is an example of a software supply chain security issue.

Some observers might think that all software security issues are software supply chain issues. How else would vulnerabilities end up in the finished software if not through the software supply chain?  A generic example can help illustrate the difference. Imagine ACME company unintentionally creates a SQL injection vulnerability in a piece of software that ACME company distributes. This is not a software supply chain security issue. Code from ACME’s own developers is responsible for this security issue. But should ACME company use an open source software component that has been maliciously tampered with to send sensitive secrets to an attacker when the code was built, then ACME would be the victim of a software supply chain attack. In that case, the supply chain of ACME’s developers is the origin of the security issue.

Software supply chain compromises can involve both malicious and unintentional vulnerabilities. The insertion of malicious code anywhere along the supply chain poses a severe risk to downstream users, but unintentional vulnerabilities in the software supply chain can also lead to risks should some party choose to exploit these vulnerabilities. For instance, the [log4j (PDF)](https://www.cisa.gov/sites/default/files/publications/CSRB-Report-on-Log4-July-11-2022_508.pdf) open source software vulnerability in late 2021 exemplifies the danger of vulnerabilities in the supply chain, including the open source software supply chain. In this case, log4j, a popular open source Java logging library, had a severe and relatively easily exploitable security bug. Many of the companies and individuals using software built with log4j found themselves vulnerable because of this bug.

Malicious attacks, or what often amounts to code tampering, deserve special recognition though. In these attacks, an attacker controls the functionality inserted into the software supply chain and can often target attacks on specific victims. These attacks often prey on the lack of integrity in the software supply chain, taking advantage of the trust that software developers place in the components and tools they use to build software. Notable attack vectors include compromises of source code systems, such as GitHub or GitLab; build systems, like Jenkins; and publishing infrastructure attacks on either corporate software publishing servers, update servers, or on community package infrastructure. Another important attack vector is when an attacker steals the credentials of an individual open source software developer and adds malicious code to a source code management system or published package.

Fortunately, a number of promising counters to software supply chain attacks have emerged. For instance, projects like Sigstore offer a chance to restore integrity to the software supply chain and initiatives like the Open Source Security Foundation provide a forum for concerted action. Further information on software supply chain security compromises and counters can be found in [this reading list](https://github.com/chainguard-dev/ssc-reading-list).

One further term merits a definition and explanation. Cloud-native software software supply chain security refers to software supply chain security efforts that are related to container technology. The process of selecting, building, and operating containers has a number of important implications for software supply chain security. For instance, signing containers with a digital signature (via a tool like [Cosign](https://github.com/sigstore/cosign)) is one way to ensure that an attacker that tampers with a container is detected. Container technology both epitomizes the potential software supply chain security perils that modern organizations must confront while also enabling approaches that can make a software supply chain secure by default.
