---
title: "Chainguard Libraries Network Requirements"
linktitle: "Network Requirements"
description: "Network requirements for different use cases with Chainguard Libraries"
type: "article"
date: 2025-06-04T09:30:00+00:00
lastmod: 2025-06-04T09:30:00+00:00
draft: false
tags: ["Chainguard Libraries", "Reference"]
menu:
  docs:
    parent: "libraries"
weight: 003
toc: true
---

The following sections detail the required network access to use Chainguard
Libraries and the related tools such as chainctl.

### Access for chainctl and Other Tools

For initial configuration with chainctl as well as for verification of
downloaded libraries with cosign and other tools, you must have HTTPS access to
the following domains:

* `dl.enforce.dev` for download and update of chainctl
* `issuer.enforce.dev` for authentication in web console and with chainctl
* `console-api.enforce.dev` for web console and chainctl to administrate and use
  your Chainguard accounts.
* `console.chainguard.dev` for the web console to administrate and use your
  Chainguard accounts.

### Access for Libraries

Chainguard Libraries use is transparent for development efforts and typically
requires no additional network access for workstations and other infrastructure
running builds because the libraries are provided by the repository manager as
configured for [Java](/chainguard/libraries/java/global-configuration) or
[Python](/chainguard/libraries/python/global-configuration).

The repository manager application must have HTTPS access to the domain
`libraries.cgr.dev` for library access and `issuer.enforce.dev` for
authentication.

If you are accessing Chainguard Libraries directly for testing with curl or with
a build tool, the used workstation must have identical access.
