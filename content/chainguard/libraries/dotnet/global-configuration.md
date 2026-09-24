---
title: "Global configuration"
linktitle: "Global configuration"
description: "Configuring Chainguard Libraries for .NET in your organization"
type: "article"
date: 2026-09-23T00:00:00+00:00
lastmod: 2026-09-24T15:12:33+00:00
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

JFrog Artifactory supports NuGet repositories for proxying packages and virtual repositories for combining repositories behind a single endpoint.

The following configuration uses the recommended upstream-fallback approach. A remote repository that points directly to nuget.org can bypass Chainguard Repository protections. Because Artifactory resolves packages through a virtual repository, a misplaced or incorrectly ordered remote can result in an unprotected package being served without an obvious build error.

### Initial configuration

Use the following steps to add Chainguard Libraries for .NET as an Artifactory remote repository:

1. Sign in to Artifactory as a user with administrator privileges.
1. Click **Administration** in the top navigation bar.
1. In the left navigation, click **Repositories**.
1. Click **Create a Repository**, then choose **Remote**.
1. Configure the remote repository with the following values:
    - **Package type**: NuGet
    - **Repository key**: `dotnet-chainguard`
    - **URL**: `https://libraries.cgr.dev/dotnet/v3/index.json`
    - **Username**: the username returned by `chainctl`
    - **Password**: the password returned by `chainctl`
1. Open the **Advanced configuration** tab and configure the following:
    - In the **Network** section, confirm that **Lenient Host Authentication** is unchecked. This prevents Artifactory from forwarding credentials across a redirect.
    - Optionally select **Enable Cookie Management**. JFrog recommends this for remote repositories that use redirects.
    - In the **Others** section, select **Bypass HEAD Requests** so that Artifactory retrieves package files with GET requests instead of probing with HEAD requests first.
    - In the **Others** section, uncheck **Block Mismatching Mime Types**.
    - Select **Disable URL Normalization** so that Artifactory does not rewrite a pre-signed redirect URL.
1. Click **Create Remote Repository**.

These settings are required because Chainguard Libraries stores artifacts behind redirects to pre-signed URLs. Without them, Artifactory may rewrite the redirect, forward credentials to the redirected host, or cache the redirect response instead of the NuGet package.

### Create a virtual repository

Create a virtual repository to give NuGet clients a single access point:

1. Click **Create a Repository**, then choose **Virtual**.
1. Configure the virtual repository with the following values:
    - **Package type**: NuGet
    - **Repository Key**: `dotnet-all`
    - **Repositories**: add `dotnet-chainguard`
1. Click **Create Virtual Repository**.

For the recommended configuration, `dotnet-chainguard` should be the only external upstream in `dotnet-all`. You can also add approved internal NuGet repositories to the virtual repository according to your organization's access-control requirements.

### Validate the remote repository

Validate the Artifactory remote before configuring developer workstations or CI/CD systems. The Artifactory **Test** button is not a reliable indicator of a working Chainguard configuration; a remote can pass the test but still be misconfigured for package retrieval.

- Confirm that the remote repository URL is `https://libraries.cgr.dev/dotnet/v3/index.json`.
- Confirm that the remote uses the current .NET pull-token username and password. Confirm that the token is not expired and was copied correctly.
- Confirm that the [Advanced configuration settings](#initial-configuration) are applied.
- Clear any previously cached test content from `dotnet-chainguard` if the repository was configured with different settings.
- Create or use a test .NET project that references a package available from Chainguard Libraries.
- Configure the test project to use the Artifactory virtual repository, then clear the NuGet HTTP cache:

```bash
 dotnet nuget locals all --clear
 ```

- Force a network restore:

 ```bash
 dotnet restore --force --no-cache --verbosity normal
```

- Inspect `obj/project.assets.json`. The `sources` entry must contain the Artifactory `dotnet-all` URL, and must not contain `nuget.org`.
- In Artifactory, confirm that the package is present in the `dotnet-chainguard` remote cache and that the request is available through the `dotnet-all` virtual repository.

### Configure build tools

After validation, configure each workstation and build server that restores .NET dependencies, including CI/CD infrastructure, to use the Artifactory virtual repository.

In Artifactory, select the dotnet-all virtual repository and use Set Me Up or Generate Settings to obtain the URL and authentication instructions for your Artifactory version. The URL commonly has the following form: `https://<artifactory-host>/artifactory/api/nuget/dotnet-all`
