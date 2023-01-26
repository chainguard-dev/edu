---
title: "What is an SBOM (software bill of materials)?"
description: "A conceptual overview of SBOMs"
lead: "A conceptual overview of SBOMs"
type: "article"
date: 2022-08-04T15:21:01+02:00
lastmod: 2022-08-04T15:21:01+02:00
contributors:  
draft: false
images: []
menu:
  docs:
    parent: "sbom"
weight: 5
toc: true
---

Today, software products often contain hundreds to thousands of different open source and third-party software components, many of which are unknown to the software operator or end user. Without an organized way of overseeing these components, it is difficult — or even impossible — to identify and respond to security risks associated with these individual components. Even when software distributors identify vulnerabilities and provide patches, software operators may not have a way to identify vulnerable components quickly enough. Or, in the worst case, operators remain entirely unaware of these vulnerabilities, enabling malicious actors to exploit them without their knowledge.  

A software bill of materials, or an SBOM (pronounced s-bomb), is a key resource for enabling visibility into the different software components of a codebase. Often described as a list of software “ingredients,” an SBOM is a formally structured list of libraries, modules, licensing, and version information that make up any given piece of software. An SBOM’s purpose is to enable software operators (or any type of software user) to have a comprehensive view of their codebase so that they can quickly identify software components that have known vulnerabilities, or investigate other tracked features like patch status, supplier, license, or version. 

## SBOM use cases

SBOMs are leveraged for a variety of purposes, which will likely continue to evolve. Some of the most prominent uses of SBOMs today are:  
* *Supply chain security*: One of the most common uses of SBOMs is enabling users to check for security vulnerabilities in their codebase’s dependencies or base images. If you learn of a vulnerability in one of the libraries your codebase depends on, you can inspect your SBOM to investigate whether your projects are affected. This security utility is further strengthened when used with [VEX](https://www.chainguard.dev/unchained/understanding-the-promise-of-vex), the Vulnerability Exploitability eXchange, which enables you to efficiently filter out security alerts that pose no threat to your codebase.  
* *Identify software suppliers*: SBOMs can be used to identify the _suppliers_ of software components, such as a software author or the individual or entity repackaging the software for redistribution. Supplier identity is often investigated for legal or procurement reasons and there is an evolving debate about which types of distributors should be held legally accountable as suppliers.    
* *Licensing*: Software projects often pull from tens or hundreds of dependencies, whose different licenses have different restrictions on the use of the code. Being able to track the licenses of your dependencies allows you to stay informed about legal restrictions and licensing compatibility issues, and help you decide which dependencies to use. 
* *Automate alerts*: The machine readable format of SBOMs enables you to create automated alerts to inform you of important events in your codebase, such as security vulnerabilities, missing components, or incompatible dependency licensing. 

## The evolution and growing importance of SBOMs

For more than a decade, a variety of communities have worked on standards for generating and sharing SBOMs or SBOM-relevant resources, with institutional support from organizations and government agencies like the Department of Commerce. Discussion of SBOMs grew significantly after the White House signed a cybersecurity executive order in May 2021 recommending the requirement of SBOMs for all software used by the federal government. This recommendation was based on the logic that SBOMs, had they been in use, would have helped minimize damage of recent large scale software supply chain security incidents such as SolarWinds and Log4j.  More recently, the Department of Homeland Security demonstrated the U.S. government’s sustained interest in SBOMs by supporting and funding the SBOM community’s research and development.  

Even without requirements, [SBOMs are becoming increasingly popular in industry](https://www.linuxfoundation.org/press/press-release/the-linux-foundation-releases-the-state-of-software-bill-of-materials-sbom-and-cybersecurity-readiness-research) given their utility for managing security risks and licensing, and providing greater visibility into an organization’s codebase. SBOM tools and practices, however, are still maturing and have yet to realize their full potential as an industry practice. While there has been an uptick in the creation and use of SBOMs, many of these SBOMs fail to meet the minimum requirements set forth by the [Department of Commerce](https://ntia.gov/sites/default/files/publications/sbom_minimum_elements_report_0.pdf). For example, [in an analysis of 3,000 SBOMs](https://www.chainguard.dev/unchained/are-sboms-good-enough-for-government-work) taken from a list of popular Docker containers, Chainguard Labs found that only one percent of SBOMs conformed with the minimum required elements. Nonetheless, proponents of SBOMs (such as Chainguard) remain optimistic about their potential. As industry strengthens SBOM tooling and practices, SBOMs continue to hold great promise for helping secure software supply chains.  

## Open source SBOM tools

### SBOM creation tools

Currently, most SBOMs are generated after the build process using a variety of tools that can scan the software for packages, licensing info, and other information relevant to an SBOM. [syft](https://github.com/anchore/syft) and [Trivy](https://github.com/aquasecurity/trivy) are two popular open source tools for generating SBOMs for containers after the build process, along with [bom](https://github.com/kubernetes-sigs/bom), an open source tool for creating, viewing, and transforming SBOMs for Kubernetes projects. 

One downside of generating SBOMs after the build process is that [scanners typically do not recognize components that are not registered with a package management system](https://www.chainguard.dev/unchained/not-all-sboms-are-created-equal). Thus, locally built software components can be missed by the scanner and result in the generation of an SBOM that is missing critical information about the software’s inventory. 

Ideally, SBOMs should be generated during the build process, which enables a higher level of accuracy given that the SBOM can be generated directly from the software inventory rather than from database records. Though build systems do not typically provide support for this approach, more build tools are beginning to provide SBOM support, such as [apko](https://github.com/chainguard-dev/apko), a tool for building and publishing OCI container images.  

### SBOM Formats

When selecting an SBOM generation tool, it’s important to make sure it supports the format you wish to use. Though there are a variety of available SBOM formats, most SBOMs follow either CycloneDX or SPDX, both of which are approved by the National Telecommunications and Information Administration for fulfilling the executive order’s SBOM requirement. 

### Quality measurement tools: 

An SBOM’s utility is dependent on the quality and comprehensiveness of the information it contains. As noted above, many SBOMs available today fail to meet the NITA’s minimum requirements. The following tools are helpful for assessing the quality of SBOMs you use or create:  
* The open source *[SBOM Scorecard](https://github.com/eBay/sbom-scorecard)*, created by eBay, analyzes SPDX and CycloneDX formats according to evolving key fields such as spec compliance, licensing information, and package data. 
* The open source *[NTIA Conformance Checker](https://github.com/spdx/ntia-conformance-checker) analyzes whether an SPDX SBOM meets the NTIA’s minimum elements, such as supplier’s name, dependency relationship, and timestamp.  

### Signing SBOMs
[Signing your SBOM](https://edu.chainguard.dev/open-source/sigstore/cosign/an-introduction-to-cosign/) is an important way of ensuring end users that it has not been tampered with by a third party and that it comes from a trusted source (you). You can use [Cosign](https://github.com/sigstore/cosign), an open-source tool for signing containers and other software artifacts, [to sign your SBOM](https://edu.chainguard.dev/open-source/sigstore/cosign/how-to-sign-an-sbom-with-cosign/). 

## Learn more:
In this guide, you have learned about the purpose of SBOMs and why proponents see them as a rising star of software supply chain security. You have also learned about key tools and formats used in SBOM production and consumption, and how to measure the quality of the SBOMs you generate or consume. 

SBOM practices and tooling are actively evolving. To learn more about SBOMs, check out related research by Chainguard Labs, such as [What Makes a Good SBOM?](https://edu.chainguard.dev/open-source/sbom/what-makes-a-good-sbom/), [Are SBOMs Any Good? Preliminary Measurement of the Quality of Open Source Project SBOMs](https://www.chainguard.dev/unchained/are-sboms-any-good-preliminary-measurement-of-the-quality-of-open-source-project-sboms), and [Are SBOMs Good Enough for Government Work?](https://www.chainguard.dev/unchained/are-sboms-good-enough-for-government-work). 
