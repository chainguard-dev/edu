---
title: "What Makes a Good SBOM?"
description: "An explanation of what makes a good SBOM"
lead: "A guide to SBOM quality"
type: "article"
date: 2022-08-04T15:21:01+02:00
lastmod: 2022-08-04T15:21:01+02:00
contributors: ["John Speed Meyers"]
draft: false
tags: ["SBOM", "Conceptual"]
images: []
menu:
  docs:
    parent: "software-security"
weight: 10
toc: true
---

A [software bill of materials](/software-security/glossary/#sbom), or an SBOM (pronounced s-bomb), is a formal record of the components contained in a piece of software. It is analogous to an ingredients list for a recipe. And it has become recognized as one of the key building blocks of software supply chain security. Proponents rightfully point out that organizations can't secure their software if they don't know what's inside their software.

As awareness and adoption of SBOM has grown, there has been a gradual acknowledgement that [not all SBOMs are created equal](https://www.chainguard.dev/unchained/not-all-sboms-are-created-equal), some are more or less useful, depending on the goals of the SBOM user and the contents of the SBOM. This guide exists to provide some guidance on evaluating the quality of an SBOM, suggesting common use cases and the data fields that support these use cases and open source SBOM quality tools.

## Basic SBOM Use Cases and Required SBOM Data

**Identifying Vulnerable Components**: SBOMs can help organizations and individuals know the unfixed vulnerabilities in their software. By providing an inventory of components, this allows a software maintainer to check whether the versions of their component are associated with any known vulnerabilities. The software maintainer can then update or patch any components with known vulnerabilities.

To enable this use case, SBOMs must contain information, at a minimum, about the component name and version. Because there are many different open source software package ecosystems, it is also advantageous to include information about the package ecosystem from which a component originates. This reduces the chances of a false positive when identifying potential vulnerabilities. A [package URL](https://github.com/package-url/purl-spec) (or purl) provides this ecosystem information. Additionally, SBOMs ought to include all transitive dependencies, dependencies of dependencies.

**Identifying Licenses**: SBOMs can also help organizations and individuals use open source software consistent with the licensing terms of all components. By identifying all components and associated licenses, software teams can understand the legal implications of any decision related to incorporating a particular component. Some organization also wish to track, often for legal or procurement purposes, the "supplier" of a particular component.

To enable license analysis, an SBOM must contain information about the license or licenses associated with all components. Additionally, there is a supplier data field that can help organizations understand component suppliers.

**Ensuring Software Integrity**: SBOMs can also help organizations and individuals ensure software integrity, discovering instances of tampering where a party has introduced malicious functionality.

Providing checksums for packages or files within the SBOM enables machine-verification of software integrity.

Note: There are [other SBOM use cases](https://www.atlanticcouncil.org/in-depth-research-reports/issue-brief/the-cases-for-using-sboms/), such as mapping broader ecosystem risks, but this guide currently focuses on the arguably three relatively well-established SBOM use cases.

## Measuring SBOM Quality

The tools for measuring SBOM quality — like the overall concept of SBOM quality itself — are nascent. There are currently two tools that are worth watching to evaluate SBOMs.

[SBOM Scorecard](https://github.com/eBay/sbom-scorecard) analyzes both major SBOM formats and returns a composite quality score indicating the extent to which an SBOM possesses key fields, including whether the components in the SBOM contain a purl and whether there are licenses associated with each component.

[NTIA Conformance Checker](https://github.com/spdx/ntia-conformance-checker) analyzes whether [SPDX](https://spdx.dev/) SBOM documents possess the data fields associated with the so-called "NTIA minimum elements." [The U.S. National Telecommunications and Information Administration "minimum elements"](https://www.ntia.doc.gov/files/ntia/publications/sbom_minimum_elements_report.pdf) include the data fields deemed essential for basic SBOM use cases, including the identification of vulnerable components and the identification of component licenses.

## Learn More

Check out Chainguard's blog post on ["Are SBOMs Any Good?"](https://www.chainguard.dev/unchained/are-sboms-any-good-preliminary-measurement-of-the-quality-of-open-source-project-sboms) to see an application of these SBOM quality tools to a dataset of open source project SBOMs. You can also learn about the complications for SBOM quality created by ["software dark matter."](https://www.chainguard.dev/unchained/software-dark-matter-is-the-enemy-of-software-transparency).