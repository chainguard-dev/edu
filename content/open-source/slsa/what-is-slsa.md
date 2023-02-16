---
title: "What is SLSA?"
description: "A conceptual overview of SLSA"
lead: "A conceptual overview of SLSA"
type: "article"
date: 2023-02-14T08:49:15+00:00
lastmod: 2023-02-14T08:49:15+00:00
contributors:  
draft: false
images: []
menu:
  docs:
    parent: "slsa"
weight: 50
toc: true
---

SLSA (pronounced “salsa”), or Supply chain Levels for Software Artifacts, is a security framework consisting of standards and controls that prevent tampering, improve integrity, and secure packages and infrastructure. While cyberattacks like [SolarWinds](https://www.gao.gov/assets/gao-22-104746.pdf) and [Codecov](https://www.reuters.com/technology/codecov-hackers-breached-hundreds-restricted-customer-sites-sources-2021-04-19/) have demonstrated the importance of protecting software from tampering and malicious compromise, the complexity of the software development lifecycle can leave many feeling unable to adequately understand or respond to these specific security issues. 

[Released by Google’s Open Source Security Team](https://security.googleblog.com/2021/06/introducing-slsa-end-to-end-framework.html) in 2021, SLSA was created as a _framework_ to help software creators understand where and how they can harden their supply chain security practices, and help software consumers evaluate the integrity of a software product or component before they decide to use it. SLSA was also designed around the creation of verifiable metadata, so that software consumers can set automated policies to prevent the deployment of code that does not meet their preferred SLSA level. 

Today, SLSA is a vendor-neutral project supported by the [Open Source Security Foundation](https://openssf.org/) and is actively evolving its standards and supporting tools with industry input. In this guide, you will learn about SLSA levels and security requirements, emerging tools that can help you meet these requirements, and where you can learn more about the framework.  


## SLSA Levels 

In its current release (SLSA v0.1), SLSA offers four ascending levels of security, each containing a set of security requirements that builds on the requirements of the prior level. These levels are designed to work as a ladder so that developers and organizations can incrementally work towards achieving an ideal security posture or the security level appropriate for their risk profile. Some software projects may take more time to advance up the ladder, so this framework offers a piecemeal approach that may be more realistic (and encouraging) than trying to meet all of the requirements at once. Note that these levels and/or their requirements may shift with the release of SLSA v1.0. 

The levels are described as follows:

 
### Level 1
**The build process must be fully scripted/automated and generate provenance.** 

Designed to be easy to adopt, this level sets a foundation for working towards the subsequent SLSA levels. The build process must be fully scripted (using, for instance, ​​a Makefile or GitHub Action yaml file) to ensure that no undocumented manual additions have been added.  [_Provenance_](https://edu.chainguard.dev/software-security/glossary/#provenance), which [SLSA defines](https://slsa.dev/provenance/v0.2) as “the verifiable information about software artifacts describing where, when and how something was produced.” Provenance data should include information about the builder, the inputs to the build, and the build commands.

While Level 1 does not prevent tampering, fulfilling its requirements represents an important first step for securing your software supply chain. Labeling your software with this level can also help consumers make decisions about whether the software is safe enough to use for their contexts. For more information on getting started with reaching Level 1, visit [SLSA’s quick start guide](https://slsa.dev/get-started#reaching-slsa-level-1. 

### Level 2
**Requires using version control and a hosted build service that generates authenticated provenance.** 

Stepping up from Level 1, Level 2 requires the use of a hosted build service like GitHub Actions, Google Cloud Build, or Travis CI rather than a developer’s local environment. It also requires the use of a version control system that tracks change history and provides immutable references to all changes, such as git, Mercurial, Subversion, or Perforce. These changes do not need to be made public, but should be attested to by an external organization that a consumer can choose to trust or not. 

The stricter requirements for Level 2 help provide more protection against software tampering and enable greater levels of trust that the provenance data is accurately represented. 

### Level 3 
**The source and build platforms meet specific standards to guarantee the auditability of the source and the integrity of the provenance respectively.** 

This level aims to increase trust and harden infrastructure through a variety of requirements designed to meet specific threats. The requirements are as follows:

* **[Build as code](https://slsa.dev/spec/v0.1/requirements#build-as-code)**: You must be able to verifiably derive the build definition and configuration from text file definitions stored in a version control system.  
*  **[Ephemeral environment](https://slsa.dev/spec/v0.1/requirements#ephemeral-environment)**:  Build steps must be run in an ephemeral environment, such as a container or VM, that has been created specifically for the build. Environments must not be reused. 
*  **[Isolated](https://slsa.dev/spec/v0.1/requirements#isolated)**: The build steps must be run in an isolated environment without risk of influence from other build processes.  
*  **[Parameterless](https://slsa.dev/spec/v0.1/requirements#parameterless)**: The build process must be fully defined through the build script and not require user parameters other than the build entry point and the top-level source location.
*  **[Non-falsifiable](https://slsa.dev/spec/v0.1/requirements#non-falsifiable)**:  It must be impossible for the build service’s users to falsify provenance information. All provenance information must be generated by the build service in a trusted control plane, except for noted exceptions. 

Generating provenance compliant with Level 3 requirements can help end users verify the integrity of the software before implementing it. Recently, SLSA released the free SLSA 3 Container Generator for GitHub Actions that helps ease the process by allowing you to build automated provenance generation into your container workflows. To learn more about how it works, visit the [General availability of SLSA 3 Container Generator for GitHub Actions](https://slsa.dev/blog/2023/02/slsa-github-workflows-container-ga) announcement blog post. You can also check out SLSA's guide on [Reaching Level 3](https://slsa.dev/get-started#reaching-slsa-level-3). 

### Level 4 
**Requires two-person review of all changes and a hermetic, reproducible build process.**

This level represents the highest level of trust possible in the SLSA framework and provides the strongest possible assurance that the software has not been tampered with. It is the most difficult level to achieve, and may not be necessary (or even possible) for all software projects. 
For this level, every change in the revision’s history must be agreed to by two trusted persons prior to submission. The software must also be produced through a hermetic, reproducible build process. 

A _hermetic_ build is defined by a build where all build steps, sources, and dependencies are declared with _immutable references_, or identifiers that are guaranteed to point to an immutable artifact whose integrity is authenticated by a cryptographic hash of its contents. These build steps, sources, and dependencies must also include their transitive counterparts, or dependencies of dependencies. The build steps must also run without network access. 

A _reproducible_ build is one in which the build steps will always reproduce “bit-for-bit” identical output. If software cannot meet this requirement, a justification must be provided. Though the build service may not verify reproducibility, consumers should be able to check its reproducibility and can reject the build if they cannot reproduce the results.

## SLSA Tools and Practices

SLSA is a relatively new framework, with supporting tools and practices still actively evolving. Some of the requirements listed in the levels above can be met using popular build and version control systems. More specific requirements may require additional tooling, and SLSA hosts some supporting tools in its [GitHub repository](https://github.com/slsa-framework). As mentioned in the description of Level 3, [SLSA released a tool for automating provenance generation](https://slsa.dev/blog/2023/02/slsa-github-workflows-container-ga), one of the hardest requirements, with GitHub Actions in February 2023.  

To verify the SLSA provenance of a piece of software, you can use the [`slsa-verifier` tool](https://github.com/slsa-framework/slsa-verifier), which can verify a provenance generated by the `slsa-generator` tool or Google Cloud Build. Other tools, like Chainguard’s [Enforce](https://www.chainguard.dev/chainguard-enforce) or Sigstore’s open source [Policy Controller](https://docs.sigstore.dev/policy-controller/overview/) allow you to create policies around SLSA requirements in your Kubernetes cluster. 

Developers are also encouraged to include the corresponding SLSA level badge ([Level 1](https://slsa.dev/images/gh-badge-level1.svg), [Level 2](https://slsa.dev/images/gh-badge-level2.svg), [Level 3](https://slsa.dev/images/gh-badge-level3.svg), [Level 4](https://slsa.dev/images/gh-badge-level4.svg) in their README once their codebase meets the level’s requirements. You can access the badges below. 

## Learn more 

In this guide, you learned about how SLSA helps secure the software supply chain, the requirements for its four security levels, and some of the tools used to implement or confirm these levels. This knowledge will help you work towards achieving SLSA levels for your software projects, assess external software based on its SLSA levels, and use admissions controllers to set SLSA-based policies in your codebase. 

While SLSA provides a strong framework for verifying the authenticity and integrity of software, it is important to note that it does not protect against every type of supply chain attack. For example, SLSA requirements cannot prevent attacks enabled through vulnerable code, vulnerabile build platforms, or collusion between high level actors. Still, SLSA offers a powerful framework for defending against common supply chain threats, and will likely emerge as a standard component of modern software as tooling and community adoption evolves. 

To learn more about SLSA, you can visit the [SLSA website](https://slsa.dev/), read an [in-depth overview of SLSA requirements](https://slsa.dev/spec/v0.1/requirements), or explore the [SLSA repository on GitHub](https://github.com/slsa-framework).  
