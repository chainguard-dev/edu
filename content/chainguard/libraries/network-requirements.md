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
* `issuer.enforce.dev` for authentication with the Chainguard Console and with chainctl
* `console-api.enforce.dev` for Chainguard Console and chainctl to administrate and use
  your Chainguard accounts.
* `console.chainguard.dev` for the Chainguard Console to administrate and use your
  Chainguard accounts.

## Access for development tools

When using a repository manager, ensure your network allows outbound HTTPS access 
to the following domains from your repository manager. Your workstations and build 
infrastructure typically require no additional network access, as libraries are 
served through your repository manager. If accessing Chainguard Libraries directly 
for testing with curl or builds, ensure your network allows outbound HTTPS access 
to these domains from your workstation:

* `libraries.cgr.dev` and `9236a389bd48b984df91adc1bc924620.r2.cloudflarestorage.com` for library access
* `issuer.enforce.dev` for authentication

> Note that the `9236a389bd48b984df91adc1bc924620.r2.cloudflarestorage.com` host is used to serve Libraries via `libraries.cgr.dev`. The same host is also used to serve Chainguard Container images.


