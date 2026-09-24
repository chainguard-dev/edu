---
title: "Migrating a .NET project to Chainguard Libraries"
type: "article"
linktitle: "Migrate to Chainguard"
description: "How to migrate an existing .NET project to pull dependencies from Chainguard Libraries"
date: 2026-09-23T00:00:00+00:00
lastmod: 2026-09-23T00:00:00+00:00
tags: ["Chainguard Libraries", ".NET"]
menu:
  docs:
    parent: dotnet
    identifier: .NET Migration
weight: 056
toc: true
---

Chainguard Libraries for .NET provides a registry of NuGet packages that have been scanned for malware and are subject to configurable policies. Switching an existing project requires only a registry configuration change – no changes to your application code or dependency versions.

This guide walks through migrating an existing .NET project to Chainguard Libraries, covering the two most common setups:

- **Direct access**: Your build tool connects directly to libraries.cgr.dev. This option is faster for initial evaluation and smaller-scale setups.
- **Repository manager**: Your build tool connects to a repository manager, which proxies requests to Chainguard Libraries. This option is recommended for teams and organizations.

## Prerequisites

Before getting started, you need:

- A .NET project with a .csproj file
- The .NET SDK
    - If you are using macOS, install the .NET SDK with Homebrew: `brew install --cask dotnet-sdk`
- `chainctl` installed and authenticated
- An [entitlement to Chainguard Libraries for .NET](#create-an-entitlement)
- A [pull token for Chainguard Libraries for .NET](#create-a-pull-token)

### Create an entitlement

To create an entitlement to Chainguard Libraries for .NET and enable upstream fallback, including a default 7-day cooldown, run:

```bash
chainctl libraries entitlements create --ecosystems=DOTNET --policy=CHAINGUARD_AND_UPSTREAM
```

You can also configure the cooldown policy after you create the entitlement. For example, to create and enforce a policy for a 14-day cooldown:

```bash
chainctl libraries policy create --name=dotnet-cooldown-14d --cooldown-days=14
chainctl libraries policy enable dotnet-cooldown-14d --ecosystem=DOTNET --mode=ENFORCE
```

It can take up to 30 minutes for the fallback and cooldown policies to take effect. Learn more about cooldown and other policies in the [Libraries policies documentation](/chainguard/chainguard-repository/library-policies/).

### Create a pull token

Create a pull token for the .NET repository:

```bash
chainctl auth pull-token --repository=dotnet --ttl=8670h
```

The command returns a username and password. Use these values to authenticate NuGet to Chainguard Libraries.

> **Note**: Do not commit the credentials to source control. Keep `nuget.config` out of the repository when it contains literal credentials, or generate it at build time from secrets stored in your CI/CD system. For shared environments, use a dedicated machine identity or service account instead of a personal token when available.

## Step 1: Configure authentication and registry

From the project directory, create a NuGet configuration file:

```bash
dotnet new nugetconfig
```

Replace its contents with the following configuration, making sure to replace the value of the username and key with the values of your pull token:

```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <packageSources>
    <clear />
    <add key="chainguard" value="https://libraries.cgr.dev/dotnet/v3/index.json" />
  </packageSources>
  <packageSourceCredentials>
    <chainguard>
      <add key="Username" value="&lt;REPLACE WITH USERNAME FROM pull-token&gt;" />
      <add key="ClearTextPassword" value="&lt;REPLACE WITH PASSWORD FROM pull-token&gt;" />
    </chainguard>
  </packageSourceCredentials>
</configuration>
```

The `<clear />` element removes previously configured package sources, including `nuget.org`. This prevents NuGet from silently falling back to `nuget.org`.

Confirm the active sources:

```bash
dotnet nuget list source
```

The expected output shows Chainguard as enabled:

```output
Registered Sources:
  1.  chainguard [Enabled]
      https://libraries.cgr.dev/dotnet/v3/index.json
```

## Step 2: Clear caches, restore, and build

Because packages have previously been served from upstream, you must clear the NuGet HTTP cache and restore:

```bash
dotnet nuget locals http-cache --clear
dotnet restore --force --no-cache --verbosity normal
```

The output should include requests to the Chainguard endpoint. If the URL or credentials are incorrect, `restore` fails instead of using a cached package. Common errors include `NU1301`, `NU1101`, and `HTTP 401` responses.

After restoring, build your project:

```bash
dotnet build
```

## Step 3: Verify your libraries

Inspect the project assets file to confirm that your project is using Chainguard Libraries:

```bash
grep -A1 '"sources"' obj/project.assets.json
```

The expected output includes the Chainguard endpoint:

```output
      "sources": {
        "https://libraries.cgr.dev/dotnet/v3/index.json": {}
```
