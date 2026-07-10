---
aliases:
- /chainguard/migration/migration-guides/migrating-dotnet/
title: "Migrating to .NET Chainguard Containers"
linktitle: ".NET"
type: "article"
description: "Learn how to migrate .NET applications from images provided by Microsoft to Chainguard's security-hardened .NET container images."
date: 2025-11-05T00:00:00+00:00
lastmod: 2026-06-22T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Migration"]
images: []
weight: 023
toc: true
---

Chainguard's [.NET container images](https://images.chainguard.dev/directory/image/dotnet-sdk/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-migration-migrating-dotnet) provide a security-hardened foundation for building and running applications with significantly fewer vulnerabilities than .NET images provided by Microsoft. Chainguard's .NET container images maintain full .NET compatibility while dramatically reducing the attack surface.

This guide demonstrates migrating a .NET application from Microsoft's official images to Chainguard's .NET container images by building one application with two different Dockerfiles and comparing the results side by side. This guide also highlights concrete examples of the security improvements resulting from migrating to Chainguard Containers.

## Prerequisites

This tutorial uses the publicly available .NET container images from Chainguard's [Free tier](/chainguard/chainguard-images/about/images-categories/#free-containers) of images. You don't need special access or permissions to use these images.

To follow along, you must have Docker installed on your local machine. If you don't have Docker installed, you can download and install it from the [official Docker website](https://docs.docker.com/get-docker/). Optionally, you can install [Grype](https://github.com/anchore/grype) to scan container images for vulnerabilities and compare the security posture of different base images.

## Retrieving the Demo Application Files

This step involves downloading the demo application code to your local machine. To prevent the application files from remaining on your system, navigate to a temporary directory like `/tmp/`:

```sh
cd /tmp/
```

Most systems automatically delete the `/tmp/` directory's contents the next time they shut down or reboot.

The code that comprises this demo application is hosted in a [public GitHub repository managed by Chainguard](https://github.com/chainguard-dev/edu-images-demos). Pull down the example application files from GitHub with the following command:

```sh
git clone --sparse https://github.com/chainguard-dev/edu-images-demos.git
```

Because this guide's demo application code is stored in a repository with other examples, we don't need to pull down every file from this repository. For this reason, this command includes the `--sparse` option. This initializes a [sparse-checkout](https://git-scm.com/docs/git-sparse-checkout) file, causing the working directory to contain only the files in the root of the repository until you modify the sparse-checkout configuration.

Navigate into this new directory:

```sh
cd edu-images-demos/
```

To retrieve the files you need for this tutorial's sample application, run the following `git` command:

```sh
git sparse-checkout set dotnet
```

This modifies the sparse-checkout configuration initialized in the previous `git clone` command so that the checkout only consists of the repo's `dotnet` directory.

Navigate into the `dotnet` directory:

```sh
cd dotnet/
```

This directory holds a single .NET application along with two Dockerfiles that build it:

- `notlinky.Dockerfile`: Builds the application on Microsoft's official .NET images
- `linky.Dockerfile`: Builds the same application on Chainguard Containers

Both Dockerfiles compile the same `Program.cs` and `dotnetapp.csproj`, so the only difference between the two images comes from the base images each Dockerfile uses.

## Understanding the Demo Application

The demo application is a .NET console program that displays runtime and system information, including:

- Operating system architecture and description
- .NET framework version
- Current user and hostname
- Hardware information (processor count and memory)
- Container cgroup memory limits and usage

When it runs, the application prints an ASCII art banner reading `dotnet` followed by these runtime details. It also writes the same output to a file named `output.txt` in its working directory, so the runtime image must allow the application's user to write to that directory. This detail matters when you build with Chainguard Containers, as explained later in this guide.

This sample application is based on Microsoft's [dotnet-runtimeinfo sample](https://github.com/dotnet/dotnet-docker/blob/main/samples/) and demonstrates a typical .NET console application that could be containerized for various use cases.

In the following sections, we'll build and compare both versions of the application.

## Building with Microsoft's .NET Images

Start by building and running the application with the .NET container images provided by Microsoft to establish a baseline for comparison.

Inspect `notlinky.Dockerfile` to see how it's structured:

```sh
cat notlinky.Dockerfile
```

```output
FROM mcr.microsoft.com/dotnet/sdk AS build

WORKDIR /source

COPY dotnetapp.csproj .
RUN dotnet restore

COPY . .
RUN dotnet publish --no-restore -o /app

FROM mcr.microsoft.com/dotnet/runtime

COPY --from=build --chown=app:app /app /app

WORKDIR /app

USER app

ENTRYPOINT ["./dotnetapp"]
```

This Dockerfile uses a multi-stage build pattern:

1. **Build stage**: Uses `mcr.microsoft.com/dotnet/sdk` to restore dependencies and publish the application
2. **Runtime stage**: Uses `mcr.microsoft.com/dotnet/runtime` for the final image
3. **User configuration**: Copies the published files with `--chown=app:app` and then switches to the non-root `app` user with `USER app`

Build the container image using this Dockerfile:

```sh
docker build -t dotnet-example:notlinky -f notlinky.Dockerfile .
```

Using `notlinky.Dockerfile`, this `docker build` command builds an image tagged `dotnet-example:notlinky`.

Use this image to run the application:

```sh
docker run --rm dotnet-example:notlinky
```

```output
         42
         42              ,d                             ,d
         42              42                             42
 ,adPPYb,42  ,adPPYba, MM42MMM 8b,dPPYba,   ,adPPYba, MM42MMM
a8"    `Y42 a8"     "8a  42    42P'   `"8a a8P_____42   42
8b       42 8b       d8  42    42       42 8PP!!!!!!!   42
"8a,   ,d42 "8a,   ,a8"  42,   42       42 "8b,   ,aa   42,
 `"8bbdP"Y8  `"YbbdP"'   "Y428 42       42  `"Ybbd8"'   "Y428

OSArchitecture: X64
OSDescription: Ubuntu 24.04.4 LTS
FrameworkDescription: .NET 10.0.9

UserName: app
HostName : ca426367d7a5

ProcessorCount: 16
TotalAvailableMemoryBytes: 16472748032 (15.34 GiB)
```

Running the container returns system information, including a stylized ASCII art banner followed by runtime details.

## Building with Chainguard's .NET Container Images

Next, build the application with Chainguard's .NET container images. Inspect `linky.Dockerfile` to understand the differences:

```sh
cat linky.Dockerfile
```

```output
FROM cgr.dev/chainguard/dotnet-sdk AS build

WORKDIR /source

COPY dotnetapp.csproj .
USER root
RUN dotnet restore

COPY . .
RUN dotnet publish --no-restore -o /app

FROM cgr.dev/chainguard/dotnet-runtime

COPY --from=build --chown=65532:65532 /app /app

WORKDIR /app

ENTRYPOINT ["./dotnetapp"]
```

Like `notlinky.Dockerfile`, this Dockerfile uses a multi-stage build. To find the differences between the two, run the following `diff` command:

```sh
git diff --no-index -U1000 notlinky.Dockerfile linky.Dockerfile
```

```diff
diff --git a/notlinky.Dockerfile b/linky.Dockerfile
index 3b7a6e2..8cd6f2e 100644
--- a/notlinky.Dockerfile
+++ b/linky.Dockerfile
@@ -1,19 +1,18 @@
-FROM mcr.microsoft.com/dotnet/sdk AS build
+FROM cgr.dev/chainguard/dotnet-sdk AS build

 WORKDIR /source

 COPY dotnetapp.csproj .
+USER root
 RUN dotnet restore

 COPY . .
 RUN dotnet publish --no-restore -o /app

-FROM mcr.microsoft.com/dotnet/runtime
+FROM cgr.dev/chainguard/dotnet-runtime

-COPY --from=build --chown=app:app /app /app
+COPY --from=build --chown=65532:65532 /app /app

 WORKDIR /app

-USER app
-
 ENTRYPOINT ["./dotnetapp"]
```

This `diff` output highlights the following differences:

1. **Registry and images**: The Chainguard Dockerfile uses `cgr.dev/chainguard/dotnet-sdk` and `cgr.dev/chainguard/dotnet-runtime` instead of the `mcr.microsoft.com` equivalents.
2. **User switching during restore**: The Chainguard Dockerfile switches to `USER root` before `dotnet restore`. Chainguard's .NET images run as a non-root user by default, and restoring packages requires root.
3. **File ownership**: Both Dockerfiles use `--chown` so the runtime user owns the copied files and can write the application's `output.txt`. The Microsoft image names its user `app`, while Chainguard's default non-root user is UID `65532`. The default username varies across Chainguard's container images (for example, `nonroot` or `app`), so referencing the UID is less ambiguous.
4. **No explicit runtime user**: The Microsoft Dockerfile ends with `USER app` to drop root privileges. The Chainguard runtime already runs as non-root, so the Chainguard Dockerfile omits this line.

Build a container image with this Dockerfile:

```sh
docker build -t dotnet-example:linky -f linky.Dockerfile .
```

Here, the `docker build` command tags the image `dotnet-example:linky`.

Run the application:

```sh
docker run --rm dotnet-example:linky
```

```output
         42
         42              ,d                             ,d
         42              42                             42
 ,adPPYb,42  ,adPPYba, MM42MMM 8b,dPPYba,   ,adPPYba, MM42MMM
a8"    `Y42 a8"     "8a  42    42P'   `"8a a8P_____42   42
8b       42 8b       d8  42    42       42 8PP!!!!!!!   42
"8a,   ,d42 "8a,   ,a8"  42,   42       42 "8b,   ,aa   42,
 `"8bbdP"Y8  `"YbbdP"'   "Y428 42       42  `"Ybbd8"'   "Y428

OSArchitecture: X64
OSDescription: Wolfi
FrameworkDescription: .NET 10.0.9

UserName: nonroot
HostName : 7e5255990efe

ProcessorCount: 16
TotalAvailableMemoryBytes: 16472748032 (15.34 GiB)
```

This output is nearly identical to what the `dotnet-example:notlinky` image returned. The differences reflect the underlying base image: the operating system is `Wolfi` rather than Ubuntu, and the application runs as `nonroot` rather than `app`. Otherwise, the two applications function identically.

## Comparing the Results

If you have Grype installed, you can scan both of the container images you've built for vulnerabilities. Start by scanning the `dotnet-example:notlinky` image:

```sh
grype dotnet-example:notlinky
```

```output
. . .

[0014]  INFO found 19 vulnerability matches across 270 packages
[0014] DEBUG   ├── fixed: 0
[0014] DEBUG   ├── ignored: 0 (due to user-provided rule)
[0014] DEBUG   ├── dropped: 0 (due to hard-coded correction)
[0014] DEBUG   └── matched: 19
[0014] DEBUG       ├── unknown severity: 0
[0014] DEBUG       ├── negligible: 0
[0014] DEBUG       ├── low: 12
[0014] DEBUG       ├── medium: 7
[0014] DEBUG       ├── high: 0
[0014] DEBUG       └── critical: 0
NAME                INSTALLED                FIXED-IN  TYPE  VULNERABILITY   SEVERITY
coreutils           9.4-3ubuntu6.2                     deb   CVE-2025-5278   Low
dpkg                1.22.6ubuntu6.6                    deb   CVE-2026-2219   Medium
gpgv                2.4.4-2ubuntu17.4                  deb   CVE-2025-68972  Medium
. . .
```

This portion of the `grype` output shows that the `dotnet-example:notlinky` container image has 19 vulnerabilities, including 12 low-severity and 7 medium-severity vulnerabilities.

Next, scan the Chainguard-based image:

```sh
grype dotnet-example:linky
```

```output
. . .

[0002]  INFO found 0 vulnerability matches across 195 packages
[0002] DEBUG   ├── fixed: 0
[0002] DEBUG   ├── ignored: 0 (due to user-provided rule)
[0002] DEBUG   ├── dropped: 0 (due to hard-coded correction)
[0002] DEBUG   └── matched: 0
[0002] DEBUG       ├── unknown severity: 0
[0002] DEBUG       ├── negligible: 0
[0002] DEBUG       ├── low: 0
[0002] DEBUG       ├── medium: 0
[0002] DEBUG       ├── high: 0
[0002] DEBUG       └── critical: 0
No vulnerabilities found
```

As this output shows, `grype` didn't find any vulnerabilities in the `dotnet-example:linky` image.

You can compare the sizes of the two container images with `docker`:

```sh
docker images dotnet-example
```

```output
REPOSITORY       TAG        IMAGE ID       CREATED         SIZE
dotnet-example   linky      defe30f42942   5 minutes ago   151MB
dotnet-example   notlinky   70e03529cea6   7 minutes ago   210MB
```

This output shows that the `dotnet-example:linky` container image is significantly smaller than the `dotnet-example:notlinky` image.

> **Note**: The command outputs shown in these examples were validated at the time of this writing. Over time, the number of vulnerabilities in either image is likely to change, though you can always expect the Chainguard-based image to contain fewer vulnerabilities.

## .NET Migration Considerations and Best Practices

When migrating a .NET application to use Chainguard Containers, keep the following considerations in mind:

- **Registry change**: Update image references from `mcr.microsoft.com` to `cgr.dev/chainguard` (or to your organization's private repository within the Chainguard registry, as in `cgr.dev/example.com`)
- **Multi-stage builds**: Both approaches use [multi-stage builds](/chainguard/chainguard-images/about/getting-started-distroless/#multi-stage-builds) to separate build-time and runtime dependencies
- **`restore` operations**: Chainguard's security model requires switching to root for `dotnet restore` or `apk` operations:

```dockerfile
USER root
RUN dotnet restore
```

- **File ownership**: Chainguard runtime images run as a non-root user by default. If your application writes to its working directory, copy the published files with `--chown` so the runtime user owns them. Referencing the default non-root UID, `65532`, avoids ambiguity, since the username varies across Chainguard Containers:

```dockerfile
COPY --from=build --chown=65532:65532 /app /app
```

Because the Chainguard runtime image already runs as non-root, you don't need to add a `USER` directive to drop privileges in the runtime stage.

Choose the runtime image based on the type of application:

- `cgr.dev/chainguard/dotnet-runtime:latest` for .NET Core applications (these are often console applications, like the one in this guide)
- `cgr.dev/chainguard/aspnet-runtime:latest` for ASP.NET applications (these are typically web applications)

If a build stage needs a shell or package manager, use a [development variant](/chainguard/chainguard-images/about/differences-development-production/) of the relevant Chainguard container image.

## Learn More

Migrating .NET applications from Microsoft's official images to Chainguard's container images provides significant security benefits with minimal code changes. The multi-stage build pattern remains the same, with the primary differences being:

1. Updated image registry and tags
2. Switching to root during package operations in the build stage
3. Automatic non-root execution in the runtime stage

These small changes result in containerized applications with few-to-zero vulnerabilities and smaller image sizes.

For detailed information about Chainguard's .NET container images and additional configuration options, refer to the following resources:

- The [.NET SDK](https://images.chainguard.dev/directory/image/dotnet-sdk/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-migration-migrating-dotnet) and [.NET Runtime](https://images.chainguard.dev/directory/image/dotnet-runtime/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-migration-migrating-dotnet) documentation pages contain full details on Chainguard's .NET images, including usage documentation, provenance, and security advisories.
- Our [General Migration Guidance](/chainguard/migration/migrating-to-chainguard-images/) is helpful for understanding migration best practices.
- [The Guardener](/chainguard/migration/the-guardener/) is an AI-powered agent that iteratively converts, builds, and validates your Dockerfiles for use with Chainguard Containers.
