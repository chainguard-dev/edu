---
title: "Chainguard Criteria for Determining Whether to Build a Container Image"
linktitle: "Build Criteria"
type: "article"
description: "An overview of what Chainguard will build"
date: 2025-01-13T11:07:52+02:00
lastmod: 2025-03-21T11:07:52+02:00
draft: false
tags: ["Chainguard Containers", "Product"]
images: []
menu:
  docs:
    parent: "about"
weight: 004
toc: true
---

There are currently over [1,000 Chainguard Containers](https://images.chainguard.dev/?utm_source=docs) and that number is always growing as we add more to our expanding catalog.

If you would like to purchase a Chainguard Container that is not yet available, or inquire about whether we would build a given container image for purchase, Chainguard will endeavor to perform an analysis on the request. Chainguard aims to build new container images that are relevant to our customers and to support broader software security goals. However, it is not always feasible to package and build software. Please note that we have the following general criteria when considering requests.  

* The source code is freely available in a Source Code Manager (SCM) system such as GitHub or GitLab.
* The project is licensed under a FOSS license. Non-FOSS licenses are reviewed on a case-by-case basis.
* The project is actively maintained with supported versions. That is:
    * There are recent commits and releases. 
    * The project has not reached its end of life (EOL).
    * The project has maintained active versions. 
    * The project does not rely on outdated or unmaintained dependencies; for example, unsupported versions of Python, OpenSSL etc.
    * There is usually a lead or owner. 
* There are no technical blockers preventing us from building the container image as we’ve determined as part of an initial analysis process. 

If the software project or container image you have in mind to purchase meets the above criteria, please [contact us](https://www.chainguard.dev/contact?utm_source=docs) for more information. 


