---
title: "Dockerfile Converter"
linktitle: "Dockerfile Converter"
type: "article"
description: "User Guide for Chainguard's Dockerfile Converter (dfc)"
date: 2025-03-18T15:22:20+01:00
lastmod: 2025-04-30T15:22:20+01:00
draft: false
tags: ["Chainguard Containers", "Open Source"]
images: []
menu:
  docs:
    parent: "migration"
weight: 030
toc: true
---

Chainguard's [Dockerfile Converter (dfc)](https://github.com/chainguard-dev/dfc) was designed to facilitate the process of porting existing Dockerfiles to use Chainguard Containers. The following platforms are currently supported:

* Alpine (`apk`)
* Debian / Ubuntu (`apt`, `apt-get`)
* Fedora / RedHat / UBI (`yum`, `dnf`, `microdnf`)

## Installation

If you use Homebrew, you can install dfc with:

```shell
brew install chainguard-dev/tap/dfc
```

If you prefer to use the Go toolchain, you can install dfc directly from source. The following command will download the latest version of dfc and install it in your `$GOPATH/bin` directory:

```shell
go install github.com/chainguard-dev/dfc@latest
```

To verify that the installation was successful, run:

```shell
dfc -v
```

You will receive output indicating which version of dfc you have installed, such as:

```
dfc version v0.9.3
```

## Getting Started

DFC supports inline conversion of entire Dockerfiles and single `FROM` and `RUN` instructions. It can also read Dockerfiles from files or standard input (stdin). The converted Dockerfile will use Chainguard Containers as the base image, which are available at `cgr.dev/<org>`.

### Inline Usage

With inline usage, you can convert single instructions or entire Dockerfiles. For example, to convert a single `FROM` line, you can run:

```shell
echo "FROM node" | dfc -
```

This will give you the following result:

```
FROM cgr.dev/ORG/node:latest
```

The `ORG` here is a placeholder that you should replace with your unique organization's namespace at Chainguard, or use `chainguard` for the free tier of images. In the [customizing section](#customizing-the-conversion) you'll learn how to use the `--org` flag to set this up automatically.

You can also convert single `RUN` directives such as the following:

```shell
echo "RUN apt-get update && apt-get install -y nano" | dfc -
```

Which will give you the following output:

```
RUN apk add --no-cache nano
```

It is also possible to convert a whole Dockerfile using inline mode. Here we use a heredoc input stream to create the Dockerfile content and pipe it to `dfc`:

```shell
cat <<DOCKERFILE | dfc -
FROM node
RUN apt-get update && apt-get install -y nano
DOCKERFILE
```

This will convert to:

```
FROM cgr.dev/ORG/node:latest-dev
USER root
RUN apk add --no-cache nano
```

Notice the `USER root` directive that has been included here to allow for package installations. You'll find details of why that happens in the [How it Works](#package-installations) section of this guide.

### Usage with Regular Dockerfiles
Unless specified, dfc will not make any direct changes to your Dockerfile, writing the results to the default output stream. To convert a Dockerfile and save the output to a new file called `Dockerfile.converted`, run the following command:

```shell
dfc ./Dockerfile > ./Dockerfile.converted
```

You can also pipe the Dockerfile’s contents from stdin:

```shell
cat ./Dockerfile | dfc -
```


## How it Works
DFC was designed to work offline by default, which means it doesn't validate image names or check for the existence of images in a live registry. Instead, it relies on a set of rules and mappings to convert Dockerfiles to use Chainguard Containers. This includes not only the change of base image used in a Dockerfile, but also the conversion of package managers and commands used in `RUN` instructions.

### FROM Conversion

DFC will convert the `FROM` instruction in a Dockerfile using two main mechanisms:

- **Registry Path Rewriting:** `dfc` programmatically rewrites the registry path in all `FROM` instructions to align with the Chainguard registry format. By default, it inserts a placeholder for the organization name, which can be explicitly set using the `--org` flag. This mechanism ensures that resulting images are sourced from the appropriate organization namespace within the Chainguard container registry.
- **Image Name Translation:** `dfc` also performs automated translation of image names based on an internal mapping file. This mapping correlates common base images and their versions to their Chainguard Container equivalents. Custom mappings can be defined to accommodate project-specific requirements, as detailed in a subsequent section. When a mapping does not exist for a specific image, `dfc` will default to use the same image name as the original Dockerfile.

For example, the following command will convert an inline `FROM` instruction using `node` as the base image:

```shell
echo "FROM node" | dfc -
```
You will receive the following output:

```shell
FROM cgr.dev/ORG/node:latest
```

### Tag Mappings

The tag conversion process follows a set of rules:

1) For `chainguard-base`, always use the `latest` tag.
   - This means that if the base image is `debian`, it will be converted to `cgr.dev/ORG/chainguard-base:latest`.
2) When no tag is specified, or when a tag is not semantic, use `latest`.
   - For example, `FROM node` will be converted to `FROM cgr.dev/ORG/node:latest`.
3) When a tag is specified, truncate semantic to major.minor (e.g.: 1.2.3 to 1.2).
   - For example, `FROM node:14.17.3` will be converted to `FROM cgr.dev/ORG/node:14.17`.
   - If the tag is not semantic (e.g., `latest`, `stable`, etc.), it will be converted to `latest`.
4) For any version except `chainguard-base`, add `-dev` suffix when there are `RUN` commands.
   - For example, `FROM node:14` will be converted to `FROM cgr.dev/ORG/node:14-dev` if the Dockerfile has `RUN` instructions.
   - If there are no `RUN` commands, it will not have the `-dev` suffix, e.g., `FROM node:14` will be converted to `FROM cgr.dev/ORG/node:14`.

More Examples:

- `FROM node:14` → `FROM cgr.dev/ORG/node:14-dev` (if stage has RUN commands)
- `FROM node:14.17.3` → `FROM cgr.dev/ORG/node:14.17-dev` (if stage has RUN commands)
- `FROM debian:bullseye` → `FROM cgr.dev/ORG/chainguard-base:latest` (always)
- `FROM golang:1.19-alpine` → `FROM cgr.dev/ORG/go:1.19-dev` (if stage has RUN commands)
- `FROM node:${VERSION}` → `FROM cgr.dev/ORG/node:${VERSION}-dev` (if stage has RUN commands)

### Package Installations

When a Dockerfile uses package managers such as `apt`, `dnf`, or `yum` to install software, `dfc` automatically translates these commands to their `apk` equivalents. This conversion leverages an internal mapping file to resolve package name differences between distributions, ensuring accurate and compatible package installation within the Chainguard Containers environment.

In addition to that, DFC automatically includes a `USER root` directive when it detects package installation commands in the Dockerfile. This is necessary because Chainguard Containers are built with a non-root user by default, and package installation commands typically require root privileges.

For example, consider the following Dockerfile based on Fedora:

```Dockerfile
FROM fedora

RUN dnf -y update && dnf clean all && dnf -y install python-pip && dnf clean all

ADD . /src

RUN cd /src; pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "/src/index.py"]
```

The following command will convert this Dockerfile and print the results to stdout:

```shell
dfc Dockerfile
```

You will receive the following output:

```Dockerfile
FROM cgr.dev/ORG/chainguard-base:latest
USER root

RUN apk add --no-cache python-pip

ADD . /src

RUN cd /src; pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "/src/index.py"]
```

### Busybox Changes for User and Group Management
DFC will automatically change any `useradd` and `groupadd` instructions in your Dockerfile to `adduser` and `addgroup` to match Busybox’s syntax. This ensures that user and group creation commands execute correctly within the Chainguard Containers environment, maintaining consistent behavior and preventing build failures.

For example, consider the following Dockerfile that adds a `nonroot` user to the image:

```Dockerfile
FROM php:8.3-cli

RUN apt-get update && apt-get install -y \
    git \
    curl \
    libxml2-dev \
    zip \
    unzip

# Install Composer and set up application
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

WORKDIR /app
COPY . /app

# set up nonroot system user
RUN useradd -r -s /bin/bash nonroot && \
    chown -R nonroot /app && \
    cd /app && composer install

USER nonroot
ENTRYPOINT [ "php", "minicli", "mycommand" ]
```

When converting this Dockerfile with `dfc`, the `useradd` command will be replaced with `adduser`, and the resulting Dockerfile will look like this:

```Dockerfile
FROM cgr.dev/ORG/php:8.3-dev
USER root

RUN apk add --no-cache curl git libxml2-dev unzip zip

# Install Composer and set up application
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

WORKDIR /app
COPY . /app

# set up nonroot system user
RUN adduser --system --shell /bin/bash nonroot && \
    chown -R nonroot /app && \
    cd /app && \
    composer install

USER nonroot
ENTRYPOINT [ "php", "minicli", "mycommand" ]
```

### Multi-stage Dockerfiles
Multi-stage builds are crucial for creating smaller, more secure, and efficient container images. By separating the build environment from the final runtime environment, they significantly reduce the final image size by discarding unnecessary build-time dependencies. This also enhances security by minimizing the attack surface.

DFC is designed to recognize and process multi-stage Dockerfiles the same way it handles regular single-stage Dockerfiles, converting them to leverage the advantages of Chainguard Containers.

Consider this multi-stage Python Dockerfile, which includes a few build-time dependencies and a leaner runtime:

```Dockerfile
FROM python:3.9 as builder
WORKDIR /app

RUN apt update && apt install -y curl git

ENV PATH="/venv/bin:$PATH"
RUN python -m venv /app/venv

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.9-slim
WORKDIR /app

ENV PATH="/venv/bin:$PATH"

COPY main.py /app
COPY --from=builder /app/venv /venv

CMD ["python", "/app/main.py"]
```

Running DFC on this Dockerfile with default options will give you the following result:

```shell
FROM cgr.dev/ORG/python:3.9-dev AS builder
USER root
WORKDIR /app

RUN apk add --no-cache curl git

ENV PATH="/venv/bin:$PATH"
RUN python -m venv /app/venv

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

FROM cgr.dev/ORG/python:3.9
WORKDIR /app

ENV PATH="/venv/bin:$PATH"

COPY main.py /app
COPY --from=builder /app/venv /venv

CMD ["python", "/app/main.py"]
```

As you will notice, DFC used a _distroless_ Python Chainguard Container for the final runtime stage: `cgr.dev/ORG/python:3.9`. That is possible because DFC didn't detect any `RUN` instruction in the final stage. If we had system-level dependencies installed via `apk` or other `RUN` instructions in the runtime stage, DFC would instead default to the regular, fully-featured Python image from Chainguard Containers, which in this case would be `cgr.dev/ORG/python:3.9-dev`.

For more details on distroless and how to work with multi-stage builds, check our guide on [Getting Started with Distroless](https://deploy-preview-2401--ornate-narwhal-088216.netlify.app/chainguard/chainguard-images/about/getting-started-distroless/).

## Customizing the Conversion
There are several ways to customize the conversion process of Dockerfiles using `dfc`.

### Setting the ORG

By default, `dfc` uses `ORG` as a placeholder for the image registry address. You can provide the `--org` parameter to specify the organization that you’re a member of. To use free tier images, use `chainguard` as the organization.

For example, the following command will convert a Dockerfile and set the organization to `chainguard`:

```shell
echo "FROM node" | dfc --org chainguard -
```
You will receive output similar to this:

```
FROM cgr.dev/chainguard/node:latest
```
### Using a Custom Registry

You can also specify a custom registry to use for the conversion. This is useful if you have your own registry. To do this, use the `--registry` flag followed by the desired registry URL. For example, if you want to use `myregistry.example.com` as the registry, you can run:

```shell
echo "FROM node" | dfc --registry myregistry.example.com -
```

You'll get output like this:

```
FROM myregistry.example.com/node:latest
```

One thing to note is that the `--registry` flag will override the `--org` flag, so if you specify both, the `--registry` will take precedence.

### Using Custom Mappings
You can also provide a custom mapping file to `dfc` using the `--mapping` flag. This allows you to define your own rules for converting Dockerfiles, such as specific image names or package names that should be translated differently.

For example, consider the following Dockerfile based on the `php:fpm` image:

```Dockerfile
FROM php:fpm

RUN apt-get update && apt-get install -y \
    git \
    curl \
    libxml2-dev \
    zip \
    unzip

# Install Composer and set up application
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer
RUN mkdir /application
COPY . /application/
RUN cd /application && composer install
```

By default, DFC will convert the `php:fpm` base image to Chainguard's main PHP image, `php:latest-dev`. However, we'd like this to be converted to `php:latest-fpm-dev`, since that is the FPM variant of the PHP image in the Chainguard registry. To handle that case, we can create a custom mapping file called `mappings.yaml` with the following content:

```yaml
images:
  php:fpm: php:latest-fpm-dev
```

Then, when running `dfc`, we can specify this mapping file using the `--mapping` flag:

```shell
dfc Dockerfile --mappings mappings.yaml
```
And this will produce the following output:

```Dockerfile
FROM cgr.dev/ORG/php:latest-fpm-dev
USER root

RUN apk add --no-cache curl git libxml2-dev unzip zip

# Install Composer and set up application
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer
RUN mkdir /application
COPY . /application/
RUN cd /application && composer install
```

## Advanced Topics
### Making In Place Changes

By default, dfc will print the converted Dockerfile to stdout, and won’t make any changes to your original Dockerfile. You can use the `--in-place` flag to make dfc overwrite the original file. This will also create a `.bak` file to back up the original file contents.

```shell
dfc Dockerfile --in-place
```

```
2025/03/14 14:54:21 saving dockerfile backup to Dockerfile.bak
2025/03/14 14:54:21 overwriting Dockerfile
```

This method does not work with inline input.

### Working with JSON Output

If you plan on using `dfc` programmatically, the JSON output can come in handy. For example, the following will convert an inline Dockerfile and output the results in JSON format, parsed by `jq` for readability:

```shell
cat <<DOCKERFILE | dfc --org chainguard.edu --json - | jq
FROM node
RUN apt-get update && apt-get install -y nano
DOCKERFILE
```

```
{
  "lines": [
    {
      "raw": "FROM node",
      "converted": "FROM cgr.dev/chainguard.edu/node:latest-dev\nUSER root",
      "stage": 1,
      "from": {
        "base": "node"
      }
    },
    {
      "raw": "RUN apt-get update && apt-get install -y nano",
      "converted": "RUN apk add -U nano",
      "stage": 1,
      "run": {
        "distro": "debian",
        "manager": "apt-get",
        "packages": [
          "nano"
        ]
      }
    },
    {
      "raw": ""
    }
  ]
}

```

Check also the [Useful jq formulas](https://github.com/chainguard-dev/dfc?tab=readme-ov-file#useful-jq-formulas) section from the dfc repository as reference on how to use jq to filter the JSON output.

### Using dfc as a Go Library
You can import the package `github.com/chainguard-dev/dfc/pkg/dfc` and use it directly from Go code to parse and convert Dockerfiles on your own, without the dfc CLI. This way, you can integrate dfc into your own Go applications or scripts, which can be especially useful if you have a large number of Dockerfiles to convert or if you want to further customize the output produced by dfc.

Check the [Using from Go](https://github.com/chainguard-dev/dfc?tab=readme-ov-file#using-from-go) section on the dfc repository for examples on how to use it as a Go library.

### Usage via AI Agent (MCP Server)
While dfc operates completely offline and does not in itself use AI to perform conversion of Dockerfiles, it can be leveraged as an MCP (Model Context Protocol) Server to integrate with an AI-based prompt engineering workflow.

This experimental capability allows AI agents to utilize DFC’s powerful conversion logic within a broader AI-driven engineering ecosystem. It's particularly useful for scenarios where automation handles 90% of the conversion and AI manages edge cases and custom logic.

For more information on how to use DFC with AI agents, check the [Project's README on GitHub](https://github.com/chainguard-dev/dfc#usage-via-ai-agent-mcp-server).


## Learn More

If you'd like to learn more about our Dockerfile Converter, including how to get involved with the project, you can check out the [dfc repository on GitHub](https://github.com/chainguard-dev/dfc). We welcome contributions and feedback from the community.
