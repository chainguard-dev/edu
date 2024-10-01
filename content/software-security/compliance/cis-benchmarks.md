---
title: "Overview of CIS Benchmarks"
linktitle: "CIS Benchmarks"
description: "A brief overview of CIS Benchmarks and how they can be used."
type: "article"
date: 2024-09-18T14:05:09+00:00
lastmod: 2024-09-18T14:05:09+00:00
contributors: []
draft: false
tags: ["COMPLIANCE", "STANDARDS"]
images: []
menu:
  docs:
    parent: "compliance"
weight: 025
toc: true
---

The [Center for Internet Security](https://www.cisecurity.org/) (CIS) is a nonprofit organization dedicated to enhancing the cybersecurity posture of organizations worldwide. Founded in 2000, CIS aims to develop best practices and guidelines that help organizations protect themselves against cyber threats.

CIS's mission is to foster collaboration among security professionals, policymakers, and industry leaders to safeguard both public and private organizations against cyber threats. One of the ways it does this is by publishing CIS Benchmarks: a set of recommendations that, when applied to a given tool, can help to harden it against threats.

This conceptual article serves as a high-level overview of CIS Benchmarks.


## What are CIS Benchmarks?

As mentioned in the introduction, CIS Benchmarks are a set of best practices and configuration guidelines designed to improve the security of various systems, applications, and networks. These benchmarks are widely recognized as authoritative standards for securing IT systems, and are developed through a consensus-driven process involving industry experts.

CIS benchmarks cover a wide range of platforms, including operating systems, cloud providers, web browsers, network devices, and application software. Each benchmark provides detailed recommendations and prescriptive guidance on how to configure systems securely. They focus on areas such as user access controls, password policies, and network security settings.

By following CIS benchmarks, organizations can significantly reduce their vulnerability to cyber threats. Additionally, many regulatory frameworks and standards recognize CIS benchmarks, making them useful for achieving compliance.

You can find the full list of available CIS Benchmarks on [the CIS website](https://www.cisecurity.org/cis-benchmarks). 

### Structure of CIS Benchmarks

CIS Benchmarks are distributed as PDF documents from the CIS website at no cost. After completing the [CIS Benchmarks PDF download form](https://learn.cisecurity.org/benchmarks), you can access all the Benchmark documents.

> **Note**: By signing up for a CIS SecureSuite Membership you can download Benchmarks in a variety of other formats, including Word or Excel documents.

CIS Benchmarks start with a brief overview of what they covers and lay out any typographical conventions or definitions specific to the Benchmark. They also define configuration profiles which can help users understand what recommendations they actually need to implement.

For example, the CIS Google Chrome Benchmark has two profiles: Level 1 is for general use in Corporate/Enterprise environments and Level 2 is for High Security or Sensitive Data environments that only need limited functionality. In this case, Level 2 is an extension of Level 1; any recommendations for organizations that fit the Level 1 profile should also be implemented for Level 2 organizations, but not vice versa.

The Benchmark will then go into individual recommendations relating to the tool it covers. These recommendations typically have the following fields:

* **Profile Applicability**: the configuration profile (mentioned above) which the recommendation applies to
* **Description**: a brief description of the recommendation
* **Rationale**: the reasoning for the recommendation, with details on how it can improve security
* **Impact**: the effect that implementing the recommendation would have on the tool's default behavior
* **Audit**: details on how you can check whether the recommendation has been implemented
* **Remediation**: details on how to establish the recommended configuration
* **Default Value**: the tool's default value, before the recommendation has been implemented
* **References**: a list of resources which informed CIS's recommendation
* **CIS Controls**: the relevant CIS Controls for the recommendation

Regarding this last bullet, [CIS Controls](https://www.cisecurity.org/controls) are more high-level recommendations than Benchmarks. CIS Benchmarks are best practices for specific tools, while CIS Controls are more simplified general recommendations that can be applied to a variety of technologies.


## Learn more

By implementing CIS benchmarks, organizations not only improve their security against evolving cyber threats but also align with regulatory standards, ensuring compliance and minimizing risks. To explore the full range of benchmarks and start implementing these best practices, visit the [CIS website](https://www.cisecurity.org/cis-benchmarks) today.

Additionally, you may find our resources on other [compliance frameworks](/software-security/compliance/) to be of interest.
