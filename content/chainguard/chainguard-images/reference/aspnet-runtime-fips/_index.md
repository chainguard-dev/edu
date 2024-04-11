---
title: "Image Overview: aspnet-runtime-fips"
linktitle: "aspnet-runtime-fips"
type: "article"
layout: "single"
description: "Overview: aspnet-runtime-fips Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu: 
  docs: 
    parent: "images-reference"
weight: 500
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/aspnet-runtime-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/aspnet-runtime-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/aspnet-runtime-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/aspnet-runtime-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Container image with the latest ASP.NET runtime.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/aspnet-runtime-fips:latest
```


<!--body:start-->
## FIPS Enablement
Our `ASPNET Runtime` images have [FIPS enabled](https://edu.chainguard.dev/chainguard/chainguard-images/images-features/fips-images/) versions. However, the underlying ASPNET core runtime does not include any mechanisms to enforce FIPS compliance according to [Microsoft's official documentation](https://learn.microsoft.com/en-us/dotnet/standard/security/fips-compliance). Accordingly, it is up you and/or your developers to ensure that your application is using FIPS compliant algorithms and that the runtime environment is also properly configured to run in FIPS mode.

## Usage

The dotnet-sdk-fips image can be used directly for simple cases, or with a multi-stage build using the dotnet-sdk-fips as the builder and aspnet-runtime-fips as the final target container.

To get started, go to your current dotnet application directory (or where you house your dotnet applications) and execute the following command. This command should be able to detect the dotnet project in your directory and create a base for the docker initialization.

```docker init```

This command should create the following files.

```
Dockerfile
compose.yaml
README.Docker.md
.dockerignore
```

After the files have been created, replace the contents within the created Dockerfile with the following

```Dockerfile
FROM cgr.dev/chainguard/dotnet-sdk-fips:latest AS build

COPY --chown=nonroot:nonroot . /source

# If your project resides in a sub directory, make sure you are pointing to that directory. ex: If your project resided in a directory called 'app', you would set the destination to /source/app
WORKDIR /source

RUN dotnet publish --use-current-runtime --self-contained false -o Release

# If you are running an .NET project, you can instead pull our .NET image cgr.dev/chainguard/dotnet-runtime-fips:latest
FROM cgr.dev/chainguard/aspnet-runtime-fips:latest AS final
WORKDIR /

# Copy everything needed to run the app from the "build" stage.
COPY --from=build source .

ENTRYPOINT ["dotnet", "Release/dotnet.dll"]
```

This will build your application using the SDK image and then copy the built application over to the Runtime image which will then start.

You can run and publish a local image with the following command
```
docker compose up -d --build
```

You can also remove the container using the following
```
docker compose down
```
<!--body:end-->

