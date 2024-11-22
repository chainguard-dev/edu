---
title: "What is OpenVex?"
description: "A conceptual overview of OpenVex"
lead: "A conceptual overview of OpenVex"
type: "article"
date: 2023-01-31T15:21:01+02:00
lastmod: 2024-11-21T15:21:01+02:00
contributors:  
draft: false
tags: ["SBOM", "VEX", "CONCEPTUAL"]
images: []
menu:
  docs:
    parent: "sbom"
weight: 15
toc: true
---


[OpenVEX](https://github.com/openvex) is an open source specification, library, and suite of tools designed to enable software users to eliminate vulnerability noise and focus their security efforts on vulnerabilities that pose an immediate risk. [Released by Chainguard in January 2023](https://www.chainguard.dev/unchained/accelerate-vex-adoption-through-openvex), it’s the first set of open source tools to support the VEX specification championed by the [United States National Telecommunications and Information Administration (NTIA)](https://ntia.gov/) and the [Cybersecurity and Infrastructure Security Agency (CISA)](https://www.cisa.gov/). 

With OpenVEX, stakeholders from across the software supply chain can collaborate on identifying and remediating exploitable vulnerabilities and use automation to enable more precise and efficient methods of security management. In this guide, you will learn more about the emerging supply chain security standards that OpenVEX supports, as well as how OpenVEX tooling can help you leverage them in your security management processes. 


## SBOMs and VEX

One of the most important ways you can protect your codebase from cyberattacks is to have timely and precise information about whether it contains known vulnerabilities. Unfortunately, many cyberattacks are able to broaden the scope of their damage *after* a vulnerability is publicly identified because individual software operators and end users are unaware that their codebase contains a known vulnerability and requires a patch. Many codebases are too complex and contain too many dependencies for their maintainers to have a comprehensive awareness of their contents. 

Incorporating [software bills of materials (SBOMs)](/open-source/sbom/what-is-an-sbom/) is a powerful way of improving visibility into your codebase so that vulnerabilities can be identified in a timely manner. When vulnerabilities are made known through security advisories, code owners and other users can refer to the tool's SBOM to see if they have dependencies associated with the specified vulnerability. 

In this way, SBOMs represent a significant step forward in security management by enabling software users to quickly identify vulnerabilities, which can otherwise require a significant amount of labor. For example, [one federal agency reportedly spent 33,000 hours responding to the Log4j vulnerability](https://federalnewsnetwork.com/commentary/2023/01/application-security-a-pillar-of-zero-trust/) at the expense of other priorities. 

Though the SBOM's improvement of visibility can greatly improve an organization's security posture, it can also be accompanied by an overproduction of false positives. In this context, [false positives](/chainguard/chainguard-images/recommended-practices/false-results/) are vulnerabilities that are associated with an organization's codebase but have been determined to not be exploitable in specific circumstances. 

This increase in false positives can hinder an SBOM's security utility as organizations are tasked with investigating the broadened list of vulnerabilities to see which ones pose genuine threats to their codebase. In cases like this, organizations may once again struggle to efficiently identify and respond to vulnerabilities before it is too late.  

Though the SBOM's improvement of visibility can greatly improve an organization's security posture, it can also be accompanied by an overproduction of false positives. In this context, [false positives](/chainguard/chainguard-images/recommended-practices/false-results/) are vulnerabilities that are associated with an organization's codebase but have been determined to not be exploitable in specific circumstances. 
When publishing a VEX document for a known software vulnerability, the author assigns the product a status drawn from the following list: 

* NOT AFFECTED — No remediation is required regarding this vulnerability. 
* AFFECTED — Actions are recommended to remediate or address this vulnerability. 
* FIXED — These product versions contain a fix for the vulnerability. 
* UNDER INVESTIGATION — It is not yet known whether these product versions are affected by the vulnerability. An update will be provided in a later release. 

Once published, downstream software users (such as operators or developers) can use these VEX documents to determine whether they are impacted by a vulnerability and what steps they might need to take to address it.

Though VEX documents do not need to be used with an SBOM, together they offer a powerful and efficient way to comprehensively scan your codebase for vulnerabilities that matter. An SBOM helps you know whether you have dependencies associated with a vulnerability, while a VEX document tells you which of those vulnerabilities you can ignore. A further benefit of VEX documents is that they are machine readable, enabling users to integrate them into automated workflows and broader tooling to support efficient security management. 

VEX has value for stakeholders across the supply chain, enabling collaboration across suppliers, operators, and end users that can save the community significant amounts of time investigating and mitigating vulnerabilities. Software suppliers can use VEX to let their users know when they’ve already investigated a vulnerability and whether that vulnerability affects the product or if further action needs to be taken by the user. And in the case that end users investigate potential vulnerabilities without a security advisory, they can encode their findings in a VEX document to share with the supplier or track for future or ongoing investigations.


## How to Leverage VEX and SBOMs with OpenVEX  

To help software suppliers and users leverage VEX, Chainguard developed OpenVEX, an open source specification, library, and suite of tools based on the VEX standard. Developed in collaboration with CISA’s VEX Working Group, OpenVEX is the first format to meet the VEX Minimum Requirements and is designed to be lightweight in order to help support community adoption. 

### A specification

OpenVEX documents are JSON-LD files that capture the minimal requirements for VEX as defined by the VEX working group organized by CISA. You can think of the VEX minimal requirements as the “specification of specifications”, and the OpenVEX format as a lightweight, embeddable, integration-friendly spec that complies with the VEX specification. 

VEX documents are composed of metadata (such as the author and timestamp) and a series of statements that link together a software product (with an identifier that can be traced to an SBOM, such as a Package URL), a vulnerability (using a vuln identifier such as CVE or OSV) , and one of the four impact statuses defined by VEX (“not affected”, “affected”, “fixed”, and “under investigation”).  

For example, an OpenVEX document with one statement could be written like this:

```json
{
  "@context": "https://openvex.dev/ns",
  "@id": "https://openvex.dev/docs/example/vex-9fb3463de1b57",
  "author": "Wolfi J Inkinson",
  "role": "Document Creator",
  "timestamp": "2023-01-08T18:02:03.647787998-06:00",
  "version": "1",
  "statements": [
    {
      "vulnerability": "CVE-2023-12345",
      "products": [
        "pkg:apk/wolfi/git@2.39.0-r1?arch=armv7",
        "pkg:apk/wolfi/git@2.39.0-r1?arch=x86_64"
      ],
      "status": "fixed"
    }
  ]
}
```

The OpenVEX specification details additional information you can include in an OpenVEX document. For example, certain statuses require additional statement information. A statement with a `not_affected` status must include a status justification or an `impact_statement` describing why the product is not affected. A statement with a `not_affected` status might be written like this: 

```json
  {
      "vulnerability": "CVE-2023-12345",
      "products": [
        "pkg:apk/wolfi/product@1.23.0-r1?arch=armv7",
      ],
      "status": "not_affected",
      "justification": "component_not_present",
      "impact_statement": "The vulnerable code was removed with a custom patch"
    }
```

These additional fields allow users to include valuable context and justification for VEX statements that can help users prioritize vulnerabilities and know what further action they need to take. 

You can learn more about the OpenVEX Specification in the [OpenVEX repo](https://github.com/openvex/spec/blob/main/OPENVEX-SPEC.md). 

### A Go library

The project has a Go library (openvex/go-vex) that lets projects generate, transform and consume OpenVEX files. It enables the ingestion of VEX metadata expressed in other VEX implementations.

You can learn more about `go-vex` in the [OpenVEX repo](https://github.com/openvex/go-vex). 

### A set of tools

OpenVEX is also committed to building out tools that will allow software authors and consumers to work with VEX metadata. The first project in this initiative is `vexctl`, a CLI to create, merge and attest VEX documents. This tool can also be used to apply VEX documents to scanner results in order to filter out false positives. 

For example, you can create a VEX document using a `vexctl create` command like the following:

```shell
vexctl create --product="pkg:apk/wolfi/git@2.38.1-r0?arch=x86_64" \
               --vuln="CVE-2014-123456" \
               --status="not_affected" \
               --justification="inline_mitigations_already_exist"
```

This code snippet will create the following OpenVEX document:

```Output
{
  "@context": "https://openvex.dev/ns/v0.2.0",
  "@id": "https://openvex.dev/docs/public/vex-783356508926ad84f48fa51480d2ed85476160dd3d4169eb0024c346edd1f10b",
  "author": "Unknown Author",
  "timestamp": "2024-11-21T15:52:42.58376093-08:00",
  "version": 1,
  "statements": [
	{
  	"vulnerability": {
    	"name": "CVE-2014-123456"
  	},
  	"timestamp": "2024-11-21T15:52:42.583761761-08:00",
  	"products": [
    	{
      	"@id": "pkg:apk/wolfi/git@2.38.1-r0?arch=x86_64"
    	}
  	],
  	"status": "not_affected",
  	"justification": "inline_mitigations_already_exist"
	}
  ]
}
```

Or, to filter out vulnerabilities from security scanner results that are fixed or not exploitable, you can use the `vexctl filter` command.  In this example, `scan_results.sarif.json` is the file with the scanner results and `vex_data.csaf` contains the VEX information:

```shell
vexctl filter scan_results.sarif.json vex_data.csaf
```
This command will return output showing vulnerabilities from the scanner that are not resolved by the VEX document. 

To learn about other commands and capabilities of the `vexctl` tool, visit the [OpenVEX repo](https://github.com/openvex/vexctl).  

## Learn More

OpenVEX is actively evolving to support VEX adoption across the community, and will continue building out tooling and adjusting its specification to meet community needs.

To learn more about VEX, check out related resources on Chainguard’s blog:

* [Reflections on Trusting VEX (or when humans can improve SBOMs)](https://www.chainguard.dev/unchained/reflections-on-trusting-vex-or-when-humans-can-improve-sboms)
* [Putting VEX to work](https://www.chainguard.dev/unchained/putting-vex-to-work)
* [Understanding the Promise of VEX](https://www.chainguard.dev/unchained/understanding-the-promise-of-vex)
* [What is VEX and Why Should I Care?](https://www.endorlabs.com/blog/what-is-vex-and-why-should-i-care)

You can also read more about VEX use cases in [this report published by the Cybersecurity and Infrastructure Security Agency](https://www.cisa.gov/sites/default/files/publications/VEX_Use_Cases_Aprill2022.pdf).