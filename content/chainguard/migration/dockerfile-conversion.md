---
title: "Dockerfile Conversion Tool"
linktitle: "Dockerfile Conversion Tool"
type: "article"
description: "Early Access User Guide for Chainguard's Dockerfile Conversion Tool (dfc)"
date: 2025-03-18T15:22:20+01:00
lastmod: 2025-03-18T15:22:20+01:00
draft: false
tags: ["CHAINGUARD IMAGES", "PRODUCT", "OPENSOURCE"]
images: []
menu:
  docs:
    parent: "migration"
weight: 030
toc: true
---

Our [Dockerfile Conversion (dfc) tool](https://github.com/chainguard-dev/dfc) was designed to facilitate the process of porting existing Dockerfiles to use Chainguard Images. The following platforms are currently supported:

* Alpine (`apk`)
* Debian / Ubuntu (`apt`, `apt-get`)
* Fedora / RedHat / UBI (`yum`, `dnf`, `microdnf`)


For each `FROM` line in the Dockerfile, `dfc` attempts to replace the base image with an equivalent Chainguard Image. For each `RUN` line in the Dockerfile, `dfc` attempts to detect the use of a known package manager (e.g. `apt` / `yum` / `apk`) and extracts the names of any packages being installed. It then attempts to map these packages to Chainguard equivalent APKs, defaulting to the existing names. All existing package manager commands are then removed and replaced with a single `apk add -U <packages>`. Additionally, dfc will add a `USER root` instruction to allow package installations since most Chainguard Images run as a regular, non-root user.

{{< note >}}
dfc is an open source tool that is still under active development and subject to changes. While we try to cover a variety of use case scenarios, some inconsistencies may occur due to the diverse nature of Dockerfiles and package manager instructions. There may be errors or gaps in functionality as you use the feature in the early access phase. Please let us know if you come across any issues or have any questions.You can [file an issue](https://github.com/chainguard-dev/dfc/issues/new/choose) on GitHub to get in touch.
{{< /note >}}

## Installation

You’ll need a Go environment to install and run Chainguard’s dfc tool. To install it on your local system, run:

```
go install github.com/chainguard-dev/dfc@latest
```

To verify that the installation was successful, run:

```
dfc --help
```

You will receive output with basic usage instructions.

```
Usage:
  dfc [flags]

Examples:
dfc <path_to_dockerfile>

Flags:
  -h, --help         help for dfc
  -i, --in-place     modified the Dockerfile in place (vs. stdout), saving original in a .bak file
      --json         print dockerfile as json (pre-conversion)
      --org string   the root repo namespace at cgr.dev/<org> (default "ORGANIZATION")
```

## Basic Usage

Unless specified, dfc will not make any direct changes to your Dockerfile, writing the results to the default output stream. Run the following to convert a Dockerfile and save the output to a new file:

```
dfc ./Dockerfile > ./Dockerfile.converted
```

You can also pipe the Dockerfile’s contents from stdin:

```
cat ./Dockerfile | dfc -
```

The following CLI flags are available:

* `--org=<org>` \- the registry namespace, i.e. `cgr.dev/<org>` (default placeholder: `ORGANIZATION`)
* `--json` \- serialize Dockerfile as JSON
* `--in-place / -i` \- modify the Dockerfile in place vs. printing to stdout, saving original in a .bak file

## Examples

This section has a few practical examples you can use as reference.

### Setting the ORG

By default, `dfc` uses `ORGANIZATION` as a placeholder for the image registry address. You can provide the `--org` parameter to specify the organization that you’re a member of. To use free tier images, use `chainguard` as the organization.

Consider the following Dockerfile for a CLI PHP application:

```
FROM php:8.2-cli

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

ENTRYPOINT [ "php", "/application/minicli" ]
```

The following command will convert this Dockerfile to use Chainguard Images, using the `chainguard` org for the free tier images. The output will be redirected to a new file called `Dockerfile.new`:

```
dfc Dockerfile > Dockerfile.new --org chainguard
```

The modified file will now use `cgr.dev/chainguard/php:latest-dev` as base image:

```
FROM cgr.dev/chainguard/php:latest-dev
USER root

RUN apk add -U curl git libxml2-dev unzip zip

# Install Composer and set up application
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer
RUN mkdir /application
COPY . /application/
RUN cd /application && composer install

ENTRYPOINT [ "php", "/application/minicli" ]
```

### Inline Usage

With inline usage, you can convert single instructions or entire Dockerfiles. For example, to convert a single `FROM` line, you can run:

```
echo "FROM node" | dfc --org chainguard.edu -
```

This will give you the following result:

```
FROM cgr.dev/chainguard.edu/node:latest-dev
USER root
```

You can also convert single `RUN` directives such as the following:

```
echo "RUN apt-get update && apt-get install -y nano" | dfc -
```

Which will give you the following output:

```
RUN apk add -U nano
```

It is also possible to convert a whole Dockerfile using inline mode. Here we use a heredoc input stream to create the Dockerfile contents:

```
cat <<DOCKERFILE | dfc --org chainguard.edu -
FROM node
RUN apt-get update && apt-get install -y nano
DOCKERFILE
```

This will convert to:

```
FROM cgr.dev/chainguard.edu/node:latest-dev
USER root
RUN apk add -U nano
```

### Making In Place Changes

By default, dfc will print the converted Dockerfile to stdout, and won’t make any changes to your original Dockerfile. You can use the `--in-place` flag to make dfc overwrite the original file. A `.bak` file is created to back up the original file contents.

```
dfc Dockerfile --in-place
```

```
2025/03/14 14:54:21 saving dockerfile backup to Dockerfile.bak
2025/03/14 14:54:21 overwriting Dockerfile
```

This method does not work with inline input.

### Working with JSON Output

If you plan on using `dfc` programmatically, the JSON output can come in handy. For example, the following will convert an inline Dockerfile and output the results in JSON format, parsed by `jq` for readability:

```
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

