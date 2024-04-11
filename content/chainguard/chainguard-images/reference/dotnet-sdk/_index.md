---
title: "Image Overview: dotnet-sdk"
linktitle: "dotnet-sdk"
type: "article"
layout: "single"
description: "Overview: dotnet-sdk Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/dotnet-sdk/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/dotnet-sdk/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/dotnet-sdk/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/dotnet-sdk/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image for .NET and the .NET Tools.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/dotnet-sdk:latest
```


<!--compatibility:start-->
## Compatibility Notes

The Chainguard .NET images are available on `cgr.dev` as two variants: `dotnet-sdk` and `dotnet-runtime`. The SDK variant contains additional tooling to facilitate development and building, while the runtime variant contains only the runtime to execute .NET applications. Both the `sdk` and `runtime` images also have `latest-dev` version that contain a shell and various other tools for development.

### SDK
```
docker pull cgr.dev/chainguard/dotnet-sdk:latest
```

### Runtime
```
docker pull cgr.dev/chainguard/dotnet-runtime:latest
```

<!--compatibility:end-->

<!--body:start-->
## Usage

The dotnet-sdk image can be used directly for simple cases, or with a multi-stage build using the dotnet-sdk as the builder and dotnet-runtime as the final target container.

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
FROM cgr.dev/chainguard/dotnet-sdk:latest AS build

COPY --chown=nonroot:nonroot . /source

# If your project resides in a sub directory, make sure you are pointing to that directory. ex: If your project resided in a directory called 'app', you would set the destination to /source/app
WORKDIR /source

RUN dotnet publish --use-current-runtime --self-contained false -o Release

# If you are running an ASPNET project, you can instead pull our ASPNET image cgr.dev/chainguard/aspnet-runtime:latest
FROM cgr.dev/chainguard/dotnet-runtime:latest AS final
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

