---
title: "Migrating to .NET Chainguard Containers"
linktitle: ".NET"
type: "article"
description: "Learn how to migrate .NET applications from images provided by Microsoft to Chainguard's security-hardened .NET container images."
date: 2025-11-05T00:00:00+00:00
lastmod: 2025-11-05T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Migration"]
images: []
weight: 023
toc: true
---

Chainguard's [.NET container images](https://images.chainguard.dev/directory/image/dotnet-sdk/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-migration-migrating-dotnet) provide a security-hardened foundation for building and running applications with significantly fewer vulnerabilities than .NET images provided by Microsoft. Chainguard's .NET container images maintain full .NET compatibility while dramatically reducing the attack surface.

This guide demonstrates migrating a .NET application from Microsoft's official images to Chainguard's .NET container images by comparing two nearly identical versions of an application side-by-side. This guide also highlights concrete examples of the security improvements resulting from migrating to Chainguard Containers.


## Prerequisites

This tutorial uses the publicly available .NET container images from Chainguard's free [Starter tier](/chainguard/chainguard-images/about/images-categories/#starter-containers) of images. You don't need special access or permissions to use these images. 

To follow along, you must have Docker installed on your local machine. If you don't have Docker installed, you can download and install it from the [official Docker website](https://docs.docker.com/get-docker/). Optionally, you can install [Grype](https://github.com/anchore/grype) to scan container images for vulnerabilities and compare the security posture of different base images.


## Retrieving the Demo Application Files

This step involves downloading the demo application code to your local machine. To prevent the application files from remaining on your system, navigate to a temporary directory like `/tmp/`:

```sh
cd /tmp/
```

Most systems will automatically delete the `/tmp/` directory's contents the next time it shuts down or reboots.

The code that comprises this demo application is hosted in a [public GitHub repository managed by Chainguard](https://github.com/chainguard-dev/edu-images-demos). Pull down the example application files from GitHub with the following command:

```sh
git clone --sparse https://github.com/chainguard-dev/edu-images-demos.git
```

Because this guide's demo application code is stored in a repository with other examples, we don't need to pull down every file from this repository. For this reason, this command includes the `--sparse` option. This initializes a [sparse-checkout](https://git-scm.com/docs/git-sparse-checkout) file, causing the working directory to contain only the files in the root of the repository until the sparse-checkout configuration is modified.

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

Here you'll find two subdirectories:
- `not-linky/`: Contains an application that uses Microsoft's official .NET images
- `linky/`: Contains a nearly identical application, but with a Dockerfile that uses Chainguard Containers


## Understanding the Demo Application

The demo application in both directories is a .NET console program that displays runtime and system information, including:

- Operating system architecture and description
- .NET framework version
- Current user and hostname
- Hardware information (processor count and memory)
- Container cgroup memory limits and usage

The only significant difference between the two is that the application in the `not-linky` directory prints an ASCII art banner reading `dotnet`, while the `linky` directory's application prints ASCII art of Linky, Chainguard's octopus mascot. Otherwise, both directories' `Program.cs` and `dotnetapp.csproj` files are identical.

This sample application is based on Microsoft's [dotnet-runtimeinfo sample](https://github.com/dotnet/dotnet-docker/blob/main/samples/) and demonstrates a typical .NET console application that could be containerized for various use cases.

In the following sections, we'll build and compare both versions of the application.


## Building with Microsoft's .NET Images

Let's start by building and running the application using the .NET container images provided by Microsoft to establish a baseline for comparison.

Navigate to the `not-linky` directory:

```sh
cd not-linky
```

You can inspect the Dockerfile to see how it's structured:

```sh
cat Dockerfile
```
```Output
# Learn about building .NET container images:
# https://github.com/dotnet/dotnet-docker/blob/main/samples/README.md
ARG IMAGE_REGISTRY="mcr.microsoft.com"
FROM --platform=$BUILDPLATFORM ${IMAGE_REGISTRY}/dotnet/sdk:9.0 AS build
ARG TARGETARCH
WORKDIR /source

# Copy project file and restore as distinct layers
COPY --link *.csproj .
RUN dotnet restore -a $TARGETARCH

# Copy source code and publish app
COPY --link . .
RUN dotnet publish -a $TARGETARCH --no-restore -o /app

# Runtime stage
FROM ${IMAGE_REGISTRY}/dotnet/runtime:9.0
WORKDIR /app
COPY --link --from=build /app .
USER $APP_UID
ENTRYPOINT ["./dotnetapp"]
```

This Dockerfile uses a multi-stage build pattern:

1. **Build stage**: Uses `mcr.microsoft.com/dotnet/sdk:9.0` to compile the application
2. **Runtime stage**: Uses `mcr.microsoft.com/dotnet/runtime:9.0` for the final image
3. **User configuration**: Explicitly switches to a non-root user with `USER $APP_UID`

Build the container image:

```sh
docker build -t dotnet-notlinky .
```

This `docker build` command builds a container image named `dotnet-notlinky`.

Run the application:

```sh
docker run --rm dotnet-notlinky
```
```Output
         42                                                    
         42              ,d                             ,d     
         42              42                             42     
 ,adPPYb,42  ,adPPYba, MM42MMM 8b,dPPYba,   ,adPPYba, MM42MMM  
a8"    `Y42 a8"     "8a  42    42P'   `"8a a8P_____42   42     
8b       42 8b       d8  42    42       42 8PP!!!!!!!   42     
"8a,   ,d42 "8a,   ,a8"  42,   42       42 "8b,   ,aa   42,    
 `"8bbdP"Y8  `"YbbdP"'   "Y428 42       42  `"Ybbd8"'   "Y428  

OSArchitecture: X64
OSDescription: Debian GNU/Linux 12 (bookworm)
FrameworkDescription: .NET 9.0.10

UserName: app
HostName : 33b915776b75

ProcessorCount: 16
TotalAvailableMemoryBytes: 16472768512 (15.34 GiB)
```

Running the container returns system information, including a stylized ASCII art banner followed by runtime details.


## Building with Chainguard's .NET Container Images

Now let's build the application with Chainguard's .NET container images. Navigate to the `linky` directory:

```sh
cd ../linky
```

The main difference between the two application directories is their respective Dockerfiles. Inspect the `linky` directory's Dockerfile to understand the differences:

```sh
cat Dockerfile
```
```Output
# Learn about building .NET container images:
# https://github.com/dotnet/dotnet-docker/blob/main/samples/README.md
ARG IMAGE_REGISTRY="cgr.dev/chainguard"
FROM --platform=$BUILDPLATFORM ${IMAGE_REGISTRY}/dotnet-sdk:latest-dev AS build
ARG TARGETARCH
WORKDIR /source

# Copy project file and restore as distinct layers
COPY --link *.csproj .
# switch to root user in order to do restore
USER 0
RUN dotnet restore -a $TARGETARCH

# Copy source code and publish app
COPY --link . .
RUN dotnet publish -a $TARGETARCH --no-restore -o /app

# Runtime stage
FROM ${IMAGE_REGISTRY}/aspnet-runtime:latest
WORKDIR /app
COPY --link --from=build /app .
ENTRYPOINT ["./dotnetapp"]
```

Like the Dockerfile in the `not-linky` directory, this Dockerfile uses a multi-stage build. However, there are a few key differences between the two Dockerfiles. To find these differences, run the following `diff` command:

```shell
git diff --no-index -U10000 ../not-linky/Dockerfile Dockerfile
```
```diff
diff --git a/../not-linky/Dockerfile b/Dockerfile
index ce4d06d..cdd6a64 100644
--- a/../not-linky/Dockerfile
+++ b/Dockerfile
@@ -1,21 +1,22 @@
 # Learn about building .NET container images:
 # https://github.com/dotnet/dotnet-docker/blob/main/samples/README.md
-ARG IMAGE_REGISTRY="mcr.microsoft.com"
-FROM --platform=$BUILDPLATFORM ${IMAGE_REGISTRY}/dotnet/sdk:9.0 AS build
+ARG IMAGE_REGISTRY="cgr.dev/chainguard"
+FROM --platform=$BUILDPLATFORM ${IMAGE_REGISTRY}/dotnet-sdk:latest-dev AS build
 ARG TARGETARCH
 WORKDIR /source
 
 # Copy project file and restore as distinct layers
 COPY --link *.csproj .
+# switch to root user in order to do restore
+USER 0
 RUN dotnet restore -a $TARGETARCH
 
 # Copy source code and publish app
 COPY --link . .
 RUN dotnet publish -a $TARGETARCH --no-restore -o /app
 
 # Runtime stage
-FROM ${IMAGE_REGISTRY}/dotnet/runtime:9.0
+FROM ${IMAGE_REGISTRY}/aspnet-runtime:latest
 WORKDIR /app
 COPY --link --from=build /app .
-USER $APP_UID
 ENTRYPOINT ["./dotnetapp"]
```

This `diff` output highlights the following differences:

1. **Build stage**: The `linky` directory's Dockerfile uses `cgr.dev/chainguard/dotnet-sdk:latest-dev` with the `-dev` variant for build tools instead of `mcr.microsoft.com/dotnet/sdk:9.0`
2. **User switching**: This Dockerfile switches to `USER 0` (root) during the restore phase, as this is required for package operations in Chainguard's security model
3. **Runtime stage**: The `linky` Dockerfile uses `cgr.dev/chainguard/aspnet-runtime:latest` which runs as non-root by default, meaning it doesn't require explicit `USER` directives

Build a container image with this Dockerfile:

```sh
docker build -t dotnet-linky .
```

Here, the `docker build` command names the image `dotnet-linky`.

Run the application:

```sh
docker run --rm dotnet-linky
```
```Output
******************************************************************************++++++++++++++++++++++
*************************************************************************+++++++++++++++++++++++++++
*************************************************************************+++++++++++++++++++++++++++
************************************************++++******************++++++++++++++++++++++++++++++
******************************************+-:..........:-+**********++++++++++++++++++++++++++++++++
***************************************+:.....:-=++=-:.....:=****+++++++++++++++++++++++++++++++++++
*************************************-....=**************=....-+*+++++++++++++++++++++++++++++++++++
***********************************=...:***+.....:*********+:...=+++++++++++++++++++++++++++++++++++
**********************************:..:****-......-************:..:++++++++++++++++++++++++++++++++++
********************************+...=**-:*+....-***************=...=++++++++++++++++++++++++++++++++
*******************************+...+*=...+**********************+...=+++++++++++++++++++++++++++++++
******************************+...***+:-*************************+...=++++++++++++++++++++++++++++++
*****************************+...*********************************+...++++++++++++++++++++++++++++++
*****************************:..+**********************************=..:+++++++++++++++++++++++++++++
****************************=..-***********************************+:..=++++++++++++++++++++++++++++
***************************+...**********-....:+**********-....:+**++...++++++++++++++++++++++++++++
***************************=..:********=..=+*+..:*******+..=+++:.:+++:..=+++++++++++++++++++++++++++
***************************=..-********..****:...+*****+..+**+-...=++-..=+++++++++++++++++++++++++++
***************************=..-********..+*****:.+*****+..+**+*+:.=++-..-+++++++++++++++++++++++++++
***************************=..:********=..-++=..-*******+..-===..-+++:..=+++++++++++++++++++++++++++
***************************+...+*********=:..:-+*********+=:..:-+++++...++++++++++++++++++++++++++++
****************************+...*************************+++++++++++...=++++++++++++++++++++++++++++
************************+=-:....:**********************++++++++++++:....:-=+++++++++++++++++++++++++
*******************+=:.......:-+********************+++++++++++++++++-:.... ..:-=+++++++++++++++++++
****************+:.....:=+************************++++++++++++++++++++++++=-:.....:=++++++++++++++++
***************-...=****************************++++++++++++++++++++++++++++++++-...-+++++++++++++++
**************+..:*****************************+++++++++++++++++++++++++++++++++++...+++++++++++++++
***************-..:**************************+++++++++++++++++++++++++++++++++++=:..:+++++++++++++++
****************-.. ....::::-*************++++++++++++++=++++++++++++++::::........-++++++++++++++++
******************+=:......=**************=-++++++++++++-=++++++++++++++-......:-+++++++++++++++++++
***********************=..-*************+-.-++++++++++++:.-++++++++++++++-..-+++++++++++++++++++++++
******************+++++=..-***********+=....++++++++++++....-++++++++++++:..=+++++++++++++++++++++++
*****************+++++*+:...-++**++=-.......-++++++++++-.......:=+++++=-...:++++++++++++++++++++++++
***************++*++++++++:...........:=++:..-++++++++-..:++=:...........:=+++++++++++++++++++++++++
*************++++++++++++++++======++++++++:...=++++=...:+++++++===--==+++++++++++++++++++++++++++++
**********++*+++++++++++++++++++++++++++++++=..........=++++++++++++++++++++++++++++++++++++++++++++
**********+++++++++++++++++++++++++++++++++++++-::::=+++++++++++++++++++++++++++++++++++++++++++++++
********++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
*****+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

OSArchitecture: X64
OSDescription: Wolfi
FrameworkDescription: .NET 9.0.10

UserName: nonroot
HostName : 1914681fe4cb

ProcessorCount: 16
TotalAvailableMemoryBytes: 16472768512 (15.34 GiB)
```

This output is similar to what was returned by running the `dotnet-notlinky` image, albeit with different ASCII art. Otherwise, the two applications function identically.


## Comparing the Results

If you have Grype installed, you can scan both the container images you've built for vulnerabilities. Start by scanning the `dotnet-notlinky` image:

```sh
grype dotnet-notlinky
```
```output
. . .

[0014]  INFO found 72 vulnerability matches across 262 packages
[0014] DEBUG   ├── fixed: 0
[0014] DEBUG   ├── ignored: 0 (due to user-provided rule)
[0014] DEBUG   ├── dropped: 0 (due to hard-coded correction)
[0014] DEBUG   └── matched: 72
[0014] DEBUG       ├── unknown severity: 0
[0014] DEBUG       ├── negligible: 48
[0014] DEBUG       ├── low: 6
[0014] DEBUG       ├── medium: 12
[0014] DEBUG       ├── high: 5
[0014] DEBUG       └── critical: 1
NAME                INSTALLED               FIXED-IN     TYPE  VULNERABILITY     SEVERITY   
apt                 2.6.1                                deb   CVE-2011-3374     Negligible  
bsdutils            1:2.38.1-5+deb12u3                   deb   CVE-2022-0563     Negligible  
. . .
```

This portion of the `grype` output shows that the `dotnet-notlinky` container image has 72 vulnerabilities, including five high-severity vulnerabilities and one critical vulnerability.

Next, scan the Chainguard-based image:

```sh
grype dotnet-linky
```
```output
. . .

[0002]  INFO found 0 vulnerability matches across 333 packages
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

As this output shows, `grype` didn't find any vulnerabilities in the `dotnet-linky` image.

You can compare the sizes of the two container images with `docker`:

```sh
docker image list | grep dotnet-
```
```output
dotnet-linky                                       latest       046ae0be8f9b   5 minutes ago   171MB
dotnet-notlinky                                    latest       ab2b43e44aca   7 minutes ago   199MB
```

This output shows that the `dotnet-linky` container image is significantly smaller than the `dotnet-notlinky` image.

> **Note**: The command outputs shown in these examples were validated at the time of this writing. Over time, the number of vulnerabilities in either image is likely to change, though you can always expect the Chainguard-based image to contain fewer vulnerabilities.


## .NET Migration Considerations and Best Practices

When migrating a .NET application to use Chainguard Containers, keep the following considerations in mind:

- **Registry change**: Update image references from `mcr.microsoft.com` to `cgr.dev/chainguard` (or to your organization's private repository within the Chainguard registry, as in `cgr.dev/example.com`)
- **Multi-stage builds**: Both approaches use [multi-stage builds](/chainguard/chainguard-images/about/getting-started-distroless/#multi-stage-builds) to separate build-time and runtime dependencies
- **Development variants**: Use [development variants](/chainguard/chainguard-images/about/differences-development-production/) of Chainguard Containers for build stages that need package management tools
- **`restore` operations**: Chainguard's security model requires explicit root user switching for `dotnet restore` or `apk` operations:

```dockerfile
USER 0
RUN dotnet restore -a $TARGETARCH
```

The runtime stage automatically runs as non-root, so you don't need to add `USER` directives.

When migrating your .NET applications to Chainguard Containers, remember to use the `dotnet-sdk:latest-dev` container image for the build stage, and to choose the appropriate runtime based on the type of application:

- `cgr.dev/chainguard/aspnet-runtime:latest` for ASP.NET applications
- `cgr.dev/chainguard/dotnet-runtime:latest` for console applications


## Learn More

Migrating .NET applications from Microsoft's official images to Chainguard's container images provides significant security benefits with minimal code changes. The multi-stage build pattern remains the same, with the primary differences being:

1. Updated image registry and tags
2. Explicit user switching during package operations in build stages
3. Automatic non-root execution in runtime stages

These small changes result in containerized applications with few-to-zero vulnerabilities and smaller image sizes.

For detailed information about Chainguard's .NET container images and additional configuration options, refer to the following resources:

- The [.NET SDK](https://images.chainguard.dev/directory/image/dotnet-sdk/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-migration-migrating-dotnet) and [ASP.NET Runtime](https://images.chainguard.dev/directory/image/aspnet-runtime/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-migration-migrating-dotnet) documentation pages contain full details on Chainguard's .NET images, including usage documentation, provenance and security advisories.
- Our [General Migration Guidance](/chainguard/migration/migrating-to-chainguard-images/) is helpful for understanding migration best practices.
- Chainguard's [Dockerfile Converter (dfc)](/chainguard/migration/dockerfile-conversion/) is a helpful tool for porting existing Dockerfiles to use Chainguard Containers.
