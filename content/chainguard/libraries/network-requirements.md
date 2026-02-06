---
title: "Chainguard Libraries network requirements"
linktitle: "Network requirements"
description: "Learn the network requirements for accessing Chainguard Libraries, including domains needed for authentication, package downloads, and verification tools"
type: "article"
date: 2025-06-04T09:30:00+00:00
lastmod: 2025-07-23T15:09:59+00:00
draft: false
tags: ["Chainguard Libraries", "Reference"]
menu:
  docs:
    parent: "libraries"
weight: 003
toc: true
---

[Chainguard Libraries](/chainguard/libraries/overview/) require specific network access to ensure secure delivery of hardened dependencies to your development environment. This guide details the domains and ports needed for authentication, package downloads, and verification tools.

## Access for chainctl and other tools

For initial configuration with chainctl as well as for verification of
downloaded libraries with cosign and other tools, you must allow HTTPS access to
the following domains:

* `dl.enforce.dev` for download and update of chainctl
* `issuer.enforce.dev` for authentication in web console and with chainctl
* `console-api.enforce.dev` for web console and chainctl to administrate and use
  your Chainguard accounts.
* `console.chainguard.dev` for the web console to administrate and use your
  Chainguard accounts.

## Access for development tools

Whether using a repository manager or accessing libraries directly, you must have HTTPS access to:

* `libraries.cgr.dev` for library access
* `issuer.enforce.dev` for authentication

When using a repository manager, configure these domains in your repository manager. Your workstations and build infrastructure typically require no additional network access, as libraries are served through your repository manager.

If accessing Chainguard Libraries directly for testing with curl or builds, configure these domains on your workstation.

### Library storage locations

Chainguard Libraries are stored and served from Google Artifact Registry (GAR).
