---
title: "Chainguard Libraries for .NET overview"
linktitle: ".NET overview"
description: "Learn about Chainguard Libraries for .NET, providing enhanced security for NuGet dependencies"
type: "article"
date: 2026-09-23T00:00:00+00:00
lastmod: 2026-09-23T00:00:00+00:00
draft: false
tags: ["Chainguard Libraries", ".NET", "NuGet"]
menu:
  docs:
    parent: "dotnet"
weight: 051
toc: true
---

Chainguard Libraries for .NET provides a secure source for your open source NuGet dependencies. NuGet is the primary public registry for .NET packages, but packages from public registries can expose applications and build pipelines to malicious or compromised code. Chainguard addresses these supply chain risks through the [Chainguard Repository](/chainguard/chainguard-repository/overview/) by applying malware and greyware scanning, organization-defined policies, and additional security controls before packages are made available. The Chainguard Repository provides a single endpoint for package retrieval.

In combination with third-party software repository managers, you can use Chainguard Libraries for .NET as a secure source of truth for your .NET development and build processes.

{{< beta feature="Chainguard Libraries for .NET" enroll="true" >}}

## Runtime requirements

The runtime requirements for .NET artifacts available from Chainguard Libraries for .NET are identical to the requirements of the original upstream project.

## Technical details

You must use the username and password [retrieved with chainctl](/chainguard/libraries/introduction/access/) to access the Chainguard Libraries for .NET repository.

The URL for the repository is: `https://libraries.cgr.dev/dotnet/`.

## View packages blocked due to malware

Chainguard’s source code and maintainer behavior scanning identifies and blocks malicious and greyware packages in Chainguard Libraries via the [Chainguard Repository](/chainguard/chainguard-repository/overview/). You can get a list of blocked packages via `chainctl` or the API. Refer to the [Libraries Overview page](/chainguard/libraries/introduction/overview/#malware-and-greyware-detection) for more information.
