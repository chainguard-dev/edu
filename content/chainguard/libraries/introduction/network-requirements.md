---
title: "Chainguard Libraries network requirements"
linktitle: "Network requirements"
description: "Learn the network requirements for accessing Chainguard Libraries, including domains needed for authentication, package downloads, and verification tools"
type: "article"
date: 2025-06-04T09:30:00+00:00
lastmod: 2026-08-25T13:24:30+00:00
draft: false
tags: ["Chainguard Libraries", "Reference"]
menu:
  docs:
    parent: "introduction"
weight: 014
toc: true
aliases:
  - /chainguard/libraries/network-requirements/
---

[Chainguard Libraries](/chainguard/libraries/introduction/overview/) require specific network access to ensure secure delivery of hardened dependencies to your development environment. This guide details the domains and ports needed for authentication, package downloads, and verification tools.

## Access for chainctl and other tools

For initial configuration with chainctl and for in-process verification of
downloaded libraries, you must allow HTTPS access to the following domains:

* `dl.enforce.dev` for download and update of chainctl
* `issuer.enforce.dev` for authentication with the Chainguard Console and with chainctl
* `console-api.enforce.dev` for Chainguard Console and chainctl to administrate and use
  your Chainguard accounts.
* `console.chainguard.dev` for the Chainguard Console to administrate and use your
  Chainguard accounts.
* `tuf-repo-cdn.sigstore.dev` for the Sigstore trust root that `chainctl libraries verify`
  uses to verify library signatures.

## Access for repository managers

When using a repository manager, ensure your network allows outbound HTTPS access
to the following domains from your repository manager. Your workstations and build
infrastructure typically require no additional network access, as libraries are
served through your repository manager.

* `libraries.cgr.dev` and `9236a389bd48b984df91adc1bc924620.r2.cloudflarestorage.com` for library access

## Access for development tools

If accessing Chainguard Libraries directly — for example, testing with curl or running builds without a repository manager — ensure your network allows outbound HTTPS access to the following domains from your workstation:

* `libraries.cgr.dev` and `9236a389bd48b984df91adc1bc924620.r2.cloudflarestorage.com` for library access

If you're also using `chainctl` to verify downloaded libraries in this workflow, see [Access for chainctl and other tools](#access-for-chainctl-and-other-tools) for the additional domains required.

> Note that the `9236a389bd48b984df91adc1bc924620.r2.cloudflarestorage.com` host is used to serve files via `libraries.cgr.dev`. The same host is also used to serve Chainguard Container images.
