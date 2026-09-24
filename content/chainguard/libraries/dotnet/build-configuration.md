---
title: "Configure .NET build tools"
linktitle: "Configure build tools"
description: "Configuring Chainguard Libraries for .NET on your workstation"
type: "article"
date: 2026-09-23T00:00:00+00:00
lastmod: 2026-09-24T15:12:33+00:00
draft: false
tags: ["Chainguard Libraries", ".NET"]
menu:
  docs:
    parent: "dotnet"
    identifier: ".NET Build Configuration"
weight: 053
toc: true
---

Chainguard Libraries for .NET works with the standard NuGet client through a package-source configuration change. This page is a reference for configuration, authentication, and cache clearing. Apply these changes on every workstation and build server that builds and restores .NET dependencies, including CI/CD infrastructure.

The `https://libraries.cgr.dev/dotnet` endpoint is also the [Chainguard Repository](/chainguard/chainguard-repository/overview/) endpoint for .NET. It serves requested versions from upstream [under Chainguard security controls](/chainguard/libraries/introduction/overview/#upstream-fallback-and-controls).

This guide outlines build tool configuration. If you are looking for something else, refer to the following guides depending on your goals:

| If you want to... | Use this page |
| --- | --- |
| Understand what Chainguard Libraries for .NET is and how it works | [.NET overview](/chainguard/libraries/dotnet/overview/) |
| Set up organization-wide access through a repository manager | [Global configuration](/chainguard/libraries/dotnet/global-configuration/) |
| Look up how to configure .NET for use with Chainguard Libraries | This page |
| Migrate an existing project step by step | [.NET migration guide](/chainguard/libraries/dotnet/migration/) |

If a package or version is blocked by a policy or malware scan, your build tool returns an error. Refer to the [Error messages documentation](/chainguard/libraries/troubleshooting/errors/) for more details.

## Library access approaches

### Direct access

For direct access, add your current session’s Chainguard credentials to your NuGet configuration file:

```bash
chainctl auth configure nuget
```

To configure NuGet with a long-lived pull token instead:

```bash
chainctl auth configure nuget --pull-token
```

#### Manually configure direct access

For direct access, add your Chainguard credentials to your NuGet configuration file. If you do not have a configuration yet, create a project-level NuGet configuration file:

```bash
dotnet new nugetconfig
```

Add the following configuration, making sure to substitute the username and password returned by `chainctl auth pull-token`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <packageSources>
    <clear />
    <add key="chainguard" value="https://libraries.cgr.dev/dotnet/v3/index.json" />
  </packageSources>
  <packageSourceCredentials>
    <chainguard>
      <add key="Username" value="REPLACE WITH USERNAME" />
      <add key="ClearTextPassword" value="REPLACE WITH PASSWORD" />
    </chainguard>
  </packageSourceCredentials>
</configuration>
```

### Repository manager

If your organization uses a repository manager, configure it to proxy the Chainguard .NET endpoint. Then configure NuGet to use the repository manager URL, for example:

```xml
<configuration>
  <packageSources>
    <clear />
    <add key="organization" value="https://repo.example.com/nuget/dotnet" />
  </packageSources>
</configuration>
```

Use the repository manager’s credentials in the NuGet configuration. Do not use the Chainguard pull token to authenticate directly to a third-party repository manager.

## Applying configuration

### Clear caches

If you suspect stale or corrupted package data, clear the NuGet HTTP cache:

```bash
dotnet nuget locals http-cache --clear
```

To force a network fetch and bypass both the global packages cache and the HTTP cache, run:

```bash
dotnet restore --force --no-cache --verbosity normal
```

When Chainguard is configured correctly, the restore output should include requests to `https://libraries.cgr.dev/...`.

### Restore and build

Restore dependencies and build the project:

```bash
dotnet restore
dotnet build
dotnet run
```

An existing project does not require changes to `Program.cs`, dependency declarations, or application code. The package-source configuration controls where NuGet retrieves the existing dependencies.

Verify that Chainguard was used:

```bash
grep -A1 '"sources"' obj/project.assets.json
```

The output should return a Chainguard source.

## Minimal example project

To test the configuration with a small application, create a console project and add a package:

```bash
dotnet new console -o MyConsoleApp
cd MyConsoleApp
dotnet add package Newtonsoft.Json
```

For this sample project only, update `Program.cs` so the application uses the package:

```Program.cs
using System;
using Newtonsoft.Json;

namespace MyConsoleApp
{
    class Program
    {
        static void Main(string[] args)
        {
            var account = new { Name = "Alice", Joined = DateTime.Now };
            string json = JsonConvert.SerializeObject(account, Formatting.Indented);
            Console.WriteLine(json);
        }
    }
}
```

Restore and run the sample:

```bash
dotnet restore
dotnet run
```

### Verify the package source

Inspect the project assets file to confirm that the restore used Chainguard Libraries:

```bash
grep -A1 '"sources"' obj/project.assets.json
```

The output should include the Chainguard endpoint:

```output
      "sources": {
        "https://libraries.cgr.dev/dotnet/v3/index.json": {}
```

If the project uses a repository manager, the assets file should instead show the repository manager URL.
