---
title: "Dockerfile Converter"
linktitle: "Dockerfile Converter"
type: "article"
description: "User Guide for Chainguard's Dockerfile Converter (dfc)"
date: 2025-03-18T15:22:20+01:00
lastmod: 2025-04-30T15:22:20+01:00
draft: false
tags: ["CHAINGUARD IMAGES", "PRODUCT", "OPEN SOURCE"]
images: []
menu:
  docs:
    parent: "migration"
weight: 030
toc: true
---

Chainguard's [Dockerfile Converter (dfc)](https://github.com/chainguard-dev/dfc) was designed to facilitate the process of porting existing Dockerfiles to use Chainguard Images. The following platforms are currently supported:

* Alpine (`apk`)
* Debian / Ubuntu (`apt`, `apt-get`)
* Fedora / RedHat / UBI (`yum`, `dnf`, `microdnf`)

For each `FROM` line in the Dockerfile, `dfc` attempts to replace the base image with an equivalent Chainguard Image. For each `RUN` line in the Dockerfile, `dfc` attempts to detect the use of a known package manager (e.g. `apt` / `yum` / `apk`) and extracts the names of any packages being installed. It then attempts to map these packages to Chainguard equivalent APKs. Additionally, dfc will add a `USER root` instruction to allow package installations since most Chainguard Images run as a regular, non-root user.

You can find more details about dfc's mapping process on their GitHub repository, in the [How it Works](https://github.com/chainguard-dev/dfc?tab=readme-ov-file#how-it-works) section of their README.

{{< note >}}
dfc is an open source tool that is still under active development and subject to changes. While we try to cover a variety of use case scenarios, some inconsistencies may occur due to the diverse nature of Dockerfiles and package manager instructions. There may be errors or gaps in functionality as you use the feature in the early access phase. Please let us know if you come across any issues or have any questions.You can [file an issue](https://github.com/chainguard-dev/dfc/issues/new/choose) on GitHub to get in touch.
{{< /note >}}

## Installation

You’ll need a Go environment to install and run dfc. To install it on your local system, run:

```shell
go install github.com/chainguard-dev/dfc@latest
```

To verify that the installation was successful, run:

```shell
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

```shell
dfc ./Dockerfile > ./Dockerfile.converted
```

You can also pipe the Dockerfile’s contents from stdin:

```shell
cat ./Dockerfile | dfc -
```

The following CLI flags are available:

* `--org=<org>` \- the registry namespace, i.e. `cgr.dev/<org>` (default placeholder: `ORGANIZATION`)
* `--json` \- serialize Dockerfile as JSON
* `--in-place / -i` \- modify the Dockerfile in place vs. printing to stdout, saving original in a .bak file

## Examples

This section has a few practical examples you can use as reference.

### Setting the ORG

By default, `dfc` uses `ORG` as a placeholder for the image registry address. You can provide the `--org` parameter to specify the organization that you’re a member of. To use free tier images, use `chainguard` as the organization.

Consider the following Dockerfile for a CLI PHP application:

```Dockerfile
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

The following command will convert this Dockerfile to use Chainguard Images, using the `chainguard` organization for the free tier images. The output will be redirected to a new file called `Dockerfile.new`:

```shell
dfc Dockerfile > Dockerfile.new --org chainguard
```

The modified file will now use `cgr.dev/chainguard/php:latest-dev` as base image:

```Dockerfile.new
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

```shell
echo "FROM node" | dfc --org chainguard.edu -
```

This will give you the following result:

```
FROM cgr.dev/chainguard.edu/node:latest-dev
```

You can also convert single `RUN` directives such as the following:

```shell
echo "RUN apt-get update && apt-get install -y nano" | dfc -
```

Which will give you the following output:

```
RUN apk add -U nano
```

It is also possible to convert a whole Dockerfile using inline mode. Here we use a heredoc input stream to create the Dockerfile contents:

```shell
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

## Using dfc as a Go Library
You can import the package `github.com/chainguard-dev/dfc/pkg/dfc` and use it directly from Go code to parse and convert Dockerfiles on your own, without the dfc CLI. This way, you can integrate dfc into your own Go applications or scripts, which can be especially useful if you have a large number of Dockerfiles to convert or if you want to further customize the output produced by dfc.

Check the [Using from Go](https://github.com/chainguard-dev/dfc?tab=readme-ov-file#using-from-go) section on the dfc repository for examples on how to use it as a Go library.

## Learn More

If you'd like to learn more about our Dockerfile Converter, including how to get involved with the project, you can check out the [dfc repository on GitHub](https://github.com/chainguard-dev/dfc). We welcome contributions and feedback from the community.
