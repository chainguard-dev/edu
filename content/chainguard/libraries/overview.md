---
title: "Chainguard Libraries Overview"
linktitle: "Libraries Overview"
description: "Learn about Chainguard Libraries, providing enhanced security for Java and Python dependencies through automated patching and comprehensive supply chain protection"
type: "article"
date: 2025-03-25T08:04:00+00:00
lastmod: 2025-07-23T15:09:59+00:00
draft: false
tags: ["Chainguard Libraries", "Overview"]
menu:
  docs:
    parent: "libraries"
weight: 001
toc: true
---

Chainguard Libraries provide enhanced security for open source dependencies in Java and Python ecosystems, addressing critical supply chain vulnerabilities through automated patching and continuous monitoring. Modern applications rely heavily on libraries from public repositories like [Maven Central](https://central.sonatype.com/), [npm](https://www.npmjs.com/), and [PyPI](https://pypi.org/), but these dependencies often contain vulnerabilities that put applications at risk.

## Background

Open source libraries distributed through public repositories face several security challenges: maintainers may not promptly address vulnerabilities, binary artifacts can be compromised, and the sheer volume of transitive dependencies makes manual security management impractical. While these repositories enable rapid development, they also introduce supply chain risks that traditional security approaches struggle to address.

While convenient, these services remove the direct link from your application to
the source code of a specific project, and create a potential risk for quality
issues with the artifacts, man-in-the-middle attacks, removal or override of
libraries with vulnerable or malicious versions, and other issues. The
[Supply-chain Levels for Software Artifacts SLSA](https://slsa.dev/)
specification describes these risks and how to protect your software against
them.

In this common use of open source via binary artifacts you put tremendous trust
into the following aspects for the dozen or even hundreds of open source
libraries you typically use for each application:

* Maintainers and specifically release managers of the projects
* Local workstation or CI setup used for the release build
* Release process mechanisms to create the binaries
* Transport of the binaries from the build system to the public repositories
* Management of access to the repositories
* Monitoring of repositories for attacks as well as harmful or malicious binaries
* Traffic to public repositories and attacks on the transport to your infrastructure

There are no real guarantees as to the actual provenance of the software code.
Repositories also vary greatly in quality and there is no guarantee that the
upstream source of a project is available in a repository. In addition, these
repositories also hold non-open source binaries of libraries.

All these factors create uncertainty. Using these public repositories can feel
as opaque as picking up a USB drive off of the sidewalk and plugging its
contents into our production environment.

## Introduction 

Chainguard Libraries builds all available libraries from source code in the
Chainguard Factory and makes them available for you. The Chainguard Factory
represents Chainguard's internal tooling that enables a more secure, dedicated,
private, and SLSA-certified build infrastructure for building software from
source and publishing the binaries to customers.

Chainguard Libraries and the use of the Chainguard Factory remove all software
supply chain problems for libraries:

* Build stage protection - All binary libraries and library versions are built
  within the trusted Chainguard infrastructure directly from the source code of
  the official project. 
* Distribution stage protection - Binaries are handled and managed only by
  Chainguard and made exclusively available for your consumption.
* Any supply chain attacks at build and distribution are eliminated, since all
  steps from the source to your use are handled by Chainguard 
* If there is no open source code available, no binaries are made available by
  Chainguard. This eliminates any license-related risks from commercial
  libraries. The policy and process to have no binaries without source also
  removes the danger from malicious artifacts, since these artifacts do not
  provide source code in public code repositories.

Chainguard Libraries is available for the following library ecosystems:

* Java and the larger Java Virtual Machine (JVM) ecosystem with [Chainguard 
Libraries for Java](/chainguard/libraries/java/overview/)
