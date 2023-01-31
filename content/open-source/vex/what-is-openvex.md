---
title: "What is OpenVex?"
description: "A conceptual overview of OpenVex"
lead: "A conceptual overview of OpenVex"
type: "article"
date: 2023-01-31T15:21:01+02:00
lastmod: 2023-01-31T15:21:01+02:00
contributors:  
draft: false
images: []
menu:
  docs:
    parent: "vex"
weight: 5
toc: true
---


[OpenVex](https://github.com/openvex) is an open source specification, library, and suite of tools designed to enable software users to eliminate vulnerability noise and focus their security efforts on vulnerabilities that pose an immediate risk. [Released by Chainguard in January 2023](https://www.chainguard.dev/unchained/accelerate-vex-adoption-through-openvex), it’s the first set of open source tools to support the VEX specification championed by the [United States National Telecommunications and Information Administration (NTIA)](https://ntia.gov/) and the [Cybersecurity and Infrastructure Security Agency (CISA)](https://www.cisa.gov/). 

With OpenVex, stakeholders from across the software supply chain can collaborate on identifying and remediating exploitable vulnerabilities and use automation to enable more precise and efficient methods of security management. In this guide you will learn more about the emerging supply chain security standards that OpenVex supports, and how OpenVex tooling can help you leverage them in your security management. 


## SBOMs and VEX

One of the most important ways you can protect your codebase from cyberattacks is to have timely and precise information about whether it contains known vulnerabilities. Unfortunately, many cyberattacks are able to broaden the scope of their damage *after* a vulnerability is publicly identified because individual software operators and end users are unaware that their codebase contains a known vulnerability and requires a patch. Many codebases are too complex and contain too many dependencies for software users to have an intuitive and comprehensive awareness of its contents. 

Incorporating a [software bill of materials (SBOM)](https://edu.chainguard.dev/open-source/sbom/what-is-an-sbom/) is a powerful way of enabling visibility into your codebase so that vulnerabilities are easily identified in a timely manner. When vulnerabilities are made known through security advisories, software users can refer to their SBOM to see if they have dependencies associated with the specified vulnerability. In this way, SBOMs represent a significant step forward in security management, enabling software users to quickly identify vulnerabilities, which can otherwise can involve a significant amout of labor. For example, [one federal agency reportedly spent 33,000 hours responding to the Log4j vulnerability](https://federalnewsnetwork.com/commentary/2023/01/application-security-a-pillar-of-zero-trust/) at the expense of other priorities. However, though the SBOM's affordance of heightened visibility greatly improves an organization's security posture, it can also be accompanied by an overproduction of false positives or vulnerabilities that are associated with an organization's codebase but have been determined to not be exploitable in specific circumstances. This increase in false positives can impede upon an SBOM's security utility as organizations are tasked with investigating the broadened list of vulnerabilities to see which ones pose genuine threats to their codebase. In this case, organizations may once again struggle to efficiently identify and respond to vulnerabilities before it is too late.  

To address this problem, SBOM working groups came up with the idea of the Vulnerability Exploitability eXchange (VEX), a system designed to help users eliminate vulnerability “noise” and focus on vulnerabilities that present a genuine risk to their organization. VEX is a mechanism that enables software suppliers and third party stakeholders (such as security researchers) to publish machine-readable security advisories on the status of Common Vulnerabilities and Exposures. When publishing a VEX document for a known vulnerability of a software product, the author assigns the product a status drawn from the following list: 

* NOT AFFECTED – No remediation is required regarding this vulnerability. 
* AFFECTED – Actions are recommended to remediate or address this vulnerability. 
* FIXED – These product versions contain a fix for the vulnerability. 
* UNDER INVESTIGATION – It is not yet known whether these product versions are affected by the vulnerability. An update will be provided in a later release. 

Once published, users of the software product (such as operators or developers) can use these VEX documents to determine whether they are impacted by a vulnerability and what steps they might need to take to address it. Though VEX documents do not need to be used with an SBOM, together they offer a powerful and efficient way to comprehensively scan your codebase for vulnerabilities that matter. An SBOM helps you know whether you have dependencies associated with a vulnerability, while a VEX document tells you which of those vulnerabilities you can ignore. A further benefit of VEX documents is that they are machine readable, enabling users to integrate them into automated workflows and broader tooling to support efficient security management. 

VEX has value for stakeholders across the supply chain, enabling collaboration across suppliers, operators, and end users that can save the community significant amounts of time investigating and mitigating vulnerabilities. Software suppliers can use VEX to let their users know when they’ve already investigated a vulnerability and whether that vulnerability affects the product or if further action needs to be taken by the user. And in the case that  end users investigate potential vulnerabilities without a security advisory, they can encode their learnings in a VEX document to share with the supplier or track for future or ongoing investigations.

## How to leverage VEX and SBOMs with OpenVex  

To help software suppliers and users leverage VEX, Chainguard developed OpenVEX, an open source specification, library, and suite of tools based on the VEX standard. Developed in collaboration with CISA’s VEX Working Group, OpenVex is the first format to meet the VEX Minimum Requirements and is designed to be lightweight to help support community adoption. 

### A Specification
OpenVEX documents are JSON-LD files that capture the minimal requirements for VEX as defined by the VEX working group organized by CISA. You can think of the VEX minimal requirements as the “spec of specs”, and the OpenVex format as a lightweight, embeddable, integration-friendly spec that complies with the VEX specification. 

VEX documents are composed of metadata (such as the author and timestamp) and a series of statements that link together a software product (with an identifier that can be traced to an SBOM, such as a Package URL), a vulnerability (using a vuln identifier such as CVE or OSV) , and one of the four impact statuses VEX enables (“not affected”, “affected”, “fixed”, and “under investigation”).  

For example, an OpenVex document with one statement could be written like this:

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

The OpenVex spec details additional information you can include in an OpenVex document. For example, certain statuses require additional statement information. A statement with a `not_affected` status must include a status justification or an `impact_statement` describing why the product is not affected. A statement with a `not_affected` status might be written like this: 

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

These additional fields enable users to include valuable context and justification for VEX statements that can help users prioritize vulnerabilities and know what further action they need to take. 

You can learn more about the OpenVex Specification in the [OpenVex repo](https://github.com/openvex/spec/blob/main/OPENVEX-SPEC.md). 

### A Go Library
The project has a go library (openvex/go-vex) that lets projects generate, transform and consume OpenVEX files. It enables the ingestion of VEX metadata expressed in other VEX implementations.

You can learn more about `go-vex` in the [OpenVex repo](https://github.com/openvex/go-vex). 

### A Set of Tools
OpenVex is also committed to building out tools that will enable software authors and consumers to work with VEX metadata. The first project in this initiative is `vexctl`, a CLI to create, merge and attest VEX documents. This tool can also be used to apply VEX documents to scanner results in order to filter out false positives. 

For example, you can create a VEX document using the following `vexctl create` command:

```
vexctl create --product="pkg:apk/wolfi/git@2.38.1-r0?arch=x86_64" \
               --vuln="CVE-2014-123456" \
               --status="not_affected" \
               --justification="inline_mitigations_already_exist"
```

This code snippet will create the following OpenVex document:

```
{
  "@context": "https://openvex.dev/ns",
  "@id": "https://openvex.dev/docs/public/vex-cfaef18d38537412a0307ec266bed56aa88fa58b7c1f2c6b8c9ef997028ba4bd",
  "author": "Unknown Author",
  "role": "Document Creator",
  "timestamp": "2023-01-10T20:24:50.498233798-06:00",
  "version": "1",
  "statements": [
    {
      "vulnerability": "CVE-2014-123456",
      "products": [
        "pkg:apk/wolfi/trivy@0.36.1-r0?arch=x86_64"
      ],
      "status": "not_affected",
      "justification": "component_not_present"
    }
  ]
}
```

Or, to filter out “Vex’ed out” vulnerabilities from security scanner results, you can use the `filter` command.  In this example, `scan_results.sarif.json` is the file with the scanner results and `vex_data.csaf` contains the VEX information.   

```
# From a VEX file:
vexctl filter scan_results.sarif.json vex_data.csaf
```

To learn about other commands and capabilities of the `vexctl` tool, visit the [OpenVex repo](https://github.com/openvex/vexctl).  

## Learn More
OpenVEX is actively evolving to support VEX adoption across the community, and will continue building out tooling and adjusting its specification to meet community needs.

To learn more about Chainguard’s view of VEX, check out related resources on Chainguard’s blog:

* [Reflections on Trusting VEX (or when humans can improve SBOMs)](https://www.chainguard.dev/unchained/reflections-on-trusting-vex-or-when-humans-can-improve-sboms_
* [Putting VEX to work](https://www.chainguard.dev/unchained/putting-vex-to-work
https://www.chainguard.dev/unchained/understanding-the-promise-of-vex) 
* [Understanding the Promise of VEX](https://www.chainguard.dev/unchained/understanding-the-promise-of-vex)
* [What is VEX and Why Should I Care?] https://www.endorlabs.com/blog/what-is-vex-and-why-should-i-care

You can also read more about VEX use cases in a report published by the [Cybersecurity and Infrastructure Security Agency](https://www.cisa.gov/sites/default/files/publications/VEX_Use_Cases_Aprill2022.pdf). 