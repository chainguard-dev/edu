---
title: "False Positives and False Negatives with Images Scanners"
linktitle: "False Positives and Negatives"
aliases: 
- /chainguard/chainguard-images/scanners/false-results
description: "An overview of the formation of false positive and false negative vulnerability results in container image scanners"
lead: "An overview of the formation of false positive and false negative vulnerability results in container image scanners"
type: "article"
date: 2023-09-14T16:59:04+00:00
lastmod: 2023-09-14T16:59:04+00:00
contributors: ["Michelle McAveety"]
draft: false
tags: ["CVE", "Overview", "Conceptual"]
images: []
menu:
  docs:
    parent: "scanners"
weight: 030
toc: true
---

A *vulnerability scanner* is a tool that analyzes your software components and reports any [CVEs](/software-security/cves/cve-intro/) it finds. Using a vulnerability scanner to find CVEs that impact your system is a critical step in [software vulnerability remediation](/software-security/cves/cve-remediation/), but as you begin to triage scanner-reported vulnerabilities, you may find that your scanner's results are not perfectly accurate.

The goal of a vulnerability scanner is to identify the vulnerabilities that impact your container images, which can be considered *true positive vulnerabilities*. Sometimes, a scanner surfaces CVEs which are not actually impacting your images, which are called *false positive vulnerabilities*. Your scanner may even miss some vulnerabilities that are impacting you, termed *false negative vulnerabilities*.

The presence of false positive and negative vulnerabilities can add a tricky layer to the vulnerability remediation process. False positive vulnerabilities can be "noisy" and distract you from remediating the vulnerabilities that are actively impacting your containers. Additionally, false negative vulnerabilities can silently affect you, making them a hidden threat to your container image security.

This article aims to explain the formation of false positive and false negative vulnerabilities, allowing you to better understand what they mean, how they impact you, and how you can use tools to fine-tune your scanner to improve the accuracy of your scan results.

## How False Positives and False Negatives Occur

Understanding how false positives and negatives occur first requires insight into how scanners operate. 

A vulnerability scanner starts by ingesting various *vulnerability databases*. A vulnerability database (such as the [National Vulnerability Database](https://nvd.nist.gov/)) is home to information regarding causes, impacts, and security advisories for software vulnerabilities. A container image scanner will often use multiple vulnerability databases as references for what software components may be vulnerable. Different databases may focus on documenting vulnerabilities for certain software vendors or products. As a result, collecting vulnerability data from numerous sources allows a scanner to identify a more exhaustive selection of vulnerabilities across software components.

When you conduct a vulnerability scan on your container images, the scanner attempts to detect what packages comprise the image. It does so by sifting through the images' source code and files introduced by package managers in search of open source software components. If successful, the scanner collects key metadata (such as package names and versions) that can be referred to later. It will then compare this metadata with the various databases it references in an attempt to determine if any packages in the software are affected by vulnerabilities.

Due to the complexity of cross-referencing image components against databases, scanners are not infallible. Sometimes vulnerabilities are misidentified — or even missed entirely. There are multiple ways in which this can occur throughout the scanning process from start to finish.

### Scanner-level Issues

Vulnerability scanners may be unable to consistently detect container components, causing the results of scans to be incomplete or inaccurate. Scanners often rely on package managers and package metadata to catalog the parts of a container. If a scanner cannot collect complete information about package metadata the results of the scan may not reflect the true contents of the image. For example, if a package in a container is not tracked by a package manager, it may go undetected, so vulnerabilities contained within are not reported.

For an in-depth discussion of how scanners fail to collect certain information, we encourage you to check out our [blog post on "Software Dark Matter"](https://www.chainguard.dev/unchained/software-dark-matter-is-the-enemy-of-software-transparency?utm_source=docs). 

### Program Scope

Some reported vulnerabilities may be falsely positive because they are detected outside of the scope of your container images. For example, a container may have packages in it which have vulnerabilities, though the [specific vulnerable functions](https://www.chainguard.dev/unchained/stemming-the-tide-of-false-positive-vulnerabilities?utm_source=docs) may not be called or reachable by your images. As a result, these vulnerabilities may pop up in your scans despite your program not interacting with their vulnerable sources. 

It is worth noting that these false positive vulnerabilities could impact you if other vulnerabilities are leveraged to access them, so they are not negligible. However, such a situation arises infrequently as a result of the exploitation of other vulnerabilities, which are first in a line of defense.

### Missing or Mismatched Information

Inconsistencies in package versioning conventions may cause scanners to fail in detecting the correct versions of your software components. Software vendors choose different version naming schemes for their products, so scanners may not easily detect what package versions are in use. Alternatively, missing or inconsistent data on vulnerable package versions in vulnerability databases can have a similar effect. In both cases, your scanner may struggle in correlating the package version in your container to package versions in vulnerability records, producing false positives and negatives where components are mismatched.

### SCA vs SAST Tools

[Software Composition Analysis (SCA)](https://snyk.io/series/open-source-security/software-composition-analysis-sca/) tools focus on the detection and assessment of open source software components, making them ideal for container image scans. SCA tools cross-reference package metadata with vulnerability databases to determine if vulnerabilities are present. However, in situations where SCA tools cannot match a package to its entries in a vulnerability database, false negatives can occur.

[Static Application Security Testing (SAST)](https://owasp.org/www-community/Source_Code_Analysis_Tools) tools scan your proprietary software to search for vulnerabilities. They provide guidance on how to modify code to resolve a given vulnerability. However, SAST tools lack context surrounding the software's behavior at runtime, giving an incomplete analysis of how the software may function. Without a comprehensive view of the software's anatomy and use, many false positive vulnerabilities [occur in SAST scans](https://blog.checkpoint.com/security/avoiding-false-positive-the-silent-sast-killer/).

To learn how to choose the right scanner method for your application, check out [this comparison of SCA and SAST scanning tools](https://github.blog/2022-09-09-sca-vs-sast-what-are-they-and-which-one-is-right-for-you/
).

## Impacts of False Positives and False Negatives

False positive vulnerabilities are [red herrings](https://en.wikipedia.org/wiki/Red_herring): They look important, but take you away from the vulnerabilities which truly matter. Identifying what vulnerabilities are true and false positives can be difficult, as your false positive results are mixed in with other true positive finds. When dealing with hundreds of vulnerabilities, the [costs of extensive triage and remediation [PDF]](https://media.bitpipe.com/io_15x/io_152272/item_2184126/ponemon-state-of-vulnerability-response-.pdf) can add up fast.

False negative vulnerabilities can have major impacts on a system if they are not discovered. They are a goldmine for attackers if they find them before you do. The successful exploitation of a false negative vulnerability can result in a *zero-day attack*. A [zero-day attack](https://usa.kaspersky.com/resource-center/definitions/zero-day-exploit) occurs when an adversary exploits a vulnerability in software which the maintainer is unaware of. This can cause the attack to go unnoticed or unresolved until the vulnerability is discovered. Many [infamous CVEs](/software-security/cves/infamous-cves/), such as Log4Shell, are examples of incredibly impactful zero-day vulnerabilities.

The presence of false positive and negative vulnerabilities in your scans add another unnecessary layer of complexity to the remediation process. Having an unreliable scanner can increase the amount of time you spend filtering out false positive results, giving you less time to focus on the true positives affecting you. Additionally, an inconsistent scanner reduces your confidence in the completeness and accuracy of your scans, making it difficult to determine if false negatives are lurking among your containers.

## Reducing False Results

Unfortunately, there is no single way to stop false positives and false negatives from occurring in your vulnerability scans. Triaging reported vulnerabilities will always be necessary to determine what vulnerabilities need to be addressed based on their severity. However, steps can be taken to reduce the overall number of false positive and negative results that surface. 

### SBOMs, Purls, and VEX

An SBOM, or [Software Bill of Materials](/open-source/sbom/what-is-an-sbom/), is a helpful document that catalogs the packages and components of your software in a machine-readable format. Using an SBOM can improve your vulnerability scans as package information is stored in one place, so scanners don't have to hunt down and risk missing component information throughout your software. There are [different ways to generate an SBOM](/open-source/sbom/what-makes-a-good-sbom/) in order to improve their comprehensiveness and utility.

To address the inconsistencies caused by software vendors using proprietary version naming schemes, adopting the [purl specification](https://github.com/package-url/purl-spec) can help. A purl, or package URL, aims to standardize versioning by outlining a convention that incorporates pertinent package information in every identifier. Using purls can [reduce the number of false positives which surface](https://www.chainguard.dev/unchained/a-purl-of-wisdom-on-sboms-and-vulnerabilities?utm_source=docs) by making it easier for scanners to align version information between data sources.

[Vulnerability Exploitability eXchange (VEX) [PDF]](https://www.cisa.gov/sites/default/files/2023-01/VEX_Use_Cases_Aprill2022.pdf) documents can provide helpful insight about the status of software vulnerabilities in a product. VEX documents allow developers to report the exploitability status of a vulnerability in a product through the use of identifiers. Using VEX can streamline the triage and remediation process by making it simpler to determine when action is needed for a given vulnerability.

One way to leverage VEX documents is through [OpenVEX](https://github.com/openvex), an open source implementation of the VEX specification. OpenVEX offers a set of tools to make ingesting and manipulating VEX documents easier. To learn more, check out our article on [getting started with OpenVEX](/open-source/sbom/getting-started-openvex-vexctl/).

### Hardened Base Images

A primary cause of large vulnerability counts reported in scanners is the dead weight caused by unnecessary dependencies. Many popular container images contain hundreds of packages, each with their own potential to introduce vulnerabilities, both true and false positives. Having so much noise to sift through draws out the vulnerability management process.

[Chainguard Images](https://www.chainguard.dev/chainguard-images?utm_source=docs), built on the [Wolfi un-distro](/open-source/wolfi/), can help you reduce your CVE count dramatically by keeping things minimal. By bundling only what is necessary to run the image, Chainguard Images are hardened and lightweight in comparison to their counterparts. To learn more about how Chainguard Images can help you achieve low (or zero!) CVEs in your containers, check out our [Images documentation](/chainguard/chainguard-images/reference/).

### Updating and Rebuilding Images

Updating your container images to utilize recent stable package releases can help reduce the number of vulnerabilities found in your images. Research from [Chainguard Labs](https://www.chainguard.dev/labs?utm_source=docs) has shown that [popular container images accumulate about one CVE per day](https://www.chainguard.dev/unchained/enforce-against-vulnerability-sprawl-with-up-to-date-images?utm_source=docs) when not updated. In many cases, updating packages and rebuilding your images to incorporate them can readily resolve numerous vulnerabilities with released fixes. This may resolve false positive vulnerabilities outside of your program scope, allowing you to focus on the true positives which still remain.

## Learn More

With false results mixed into your scans, triaging and addressing true positive vulnerabilities can quickly become a time-consuming task. Taking steps to adjust your scanner can help reduce the deluge of false positives and negatives clouding your scans, bringing you closer to securing your software.

In this article, you learned how false results from your vulnerability scanners can occur, and how they can impact your development workflow. Additionally, you explored various ways you can improve the accuracy of your scanner through the application of tools like VEX, rebuilding your images, and choosing a base image suitable for your applications.

To learn more about reducing false positives and negatives in your images, you can check out our [collection of articles on SBOMs and VEX](/open-source/sbom/), read about [selecting a base image](/software-security/selecting-a-base-image/) for your applications, or discover how Chainguard Images can help you [reach zero CVEs in your containers](https://www.chainguard.dev/chainguard-images?utm_source=docs).
