---
title: "Global configuration"
linktitle: "Global configuration"
description: "Configuring Chainguard Libraries for .NET in your organization"
type: "article"
date: 2026-09-23T00:00:00+00:00
lastmod: 2026-09-23T00:00:00+00:00
draft: false
tags: ["Chainguard Libraries", ".NET"]
images: []
menu:
  docs:
    parent: "dotnet"
    identifier: ".NET Global Configuration"
weight: 052
toc: true
---

.NET package consumption in a large organization is typically managed by a repository manager. The repository manager acts as a single point of access for developers and development tools to retrieve NuGet packages.

This page describes how to configure JFrog Artifactory to proxy Chainguard Libraries for .NET. The instructions use Chainguard Repository's built-in upstream fallback, which is the recommended configuration.

With upstream fallback enabled, configure Artifactory with a single remote repository that points to the Chainguard NuGet v3 service index: `https://libraries.cgr.dev/dotnet/v3/index.json`.

Chainguard Repository handles upstream fallback and policy enforcement. Artifactory handles local caching, access control, and the endpoint used by your NuGet clients. Do not add a direct `nuget.org` remote to the virtual repository used by your builds unless you intentionally want to manage fallback yourself.

## Prerequisites

Before you begin, you need:

- An [entitlement to Chainguard Libraries for .NET](/chainguard/libraries/dotnet/migration/#create-an-entitlement)
- Administrator access to your repository manager instance
- A [pull token for Chainguard Libraries for .NET](/chainguard/libraries/dotnet/migration/#create-a-pull-token)

## JFrog Artifactory
