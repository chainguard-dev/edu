---
title: "Chainguard Libraries Verification"
linktitle: "Verification"
description:
  "Learn how to verify Java and Python dependencies are from Chainguard
  Libraries using the chainver tool for enhanced supply chain security"
type: "article"
date: 2025-07-03T12:00:00+00:00
lastmod: 2025-07-23T15:09:59+00:00
draft: false
tags: ["Chainguard Libraries"]
menu:
  docs:
    parent: "libraries"
weight: 004
toc: true
---

## Overview

Chainguard's `chainver` tool verifies that your Java and Python dependencies
come from Chainguard Libraries, providing critical visibility into your software
supply chain security. By verifying binary artifacts across your projects and
repositories, you can ensure dependencies are sourced from Chainguard's hardened
build environment rather than potentially compromised public repositories,
identify opportunities to improve security posture, and maintain compliance with
supply chain security policies.

The `chainver` tool:

- Uses a signature-based binary identification and a checksum fallback.
- Supports different binary formats, including JAR, WAR, EAR, ZIP, TAR, WHL, and
  APK files as well as container images.
- Allows analysis of directories and nested archive files.
- Creates output in text, json, yaml, and CSV formats.

## Prerequisites

Before installing chainver, ensure you have the following installed and
available on your path:

- [`chainctl`](https://edu.chainguard.dev/chainguard/chainctl-usage/how-to-install-chainctl/)
  — A Chainguard-maintained tool used for authentication
- [`cosign`](https://docs.sigstore.dev/cosign/system_config/installation/) — A
  Sigstore-maintained tool used to verify signatures

You also need:

- A Linux, macOS, or Windows system (x86_64 or arm64)
- Sufficient [network access](/chainguard/libraries/network-requirements/)

You can confirm that `chainctl` and `cosign` are installed with the following
commands:

```sh
chainctl version
```

```sh
cosign version
```

## Installation

[Download the latest release - version 0.4.1](https://dl.enforce.dev/chainver/0.4.1/chainver-v0.4.1.zip)

### Binary (macOS and Linux)

The below command will download the latest version of `chainver` as an archive, extract it, verify the download, and move the binary to `/usr/local/bin`.

First,, set the `ARCH` variable to match your system using one of
the following options:

- `Linux_x86_64` - Linux with x86_64 processor
- `Linux_arm64` - Linux with ARM processor
- `Darwin_arm64` - macOS with Apple Silicon (M1/M2/M3)
- `Darwin_x86_64` - macOS with Intel processor

```sh
ARCH=Linux_x86_64 && \
LATEST=$(curl -s "https://storage.googleapis.com/us.artifacts.prod-enforce-fabc.appspot.com/?prefix=chainver/" | \
  grep -oE 'chainver/[0-9]+\.[0-9]+\.[0-9]+/' | \
  sed 's|chainver/||g' | sed 's|/$||g' | \
  sort -V | tail -1) && \
curl -LO "https://dl.enforce.dev/chainver/${LATEST}/chainver-v${LATEST}.zip" && \
unzip -q chainver-*.zip && \
cd chainver-package && \
EXT=$([ "$ARCH" = "Windows_x86_64" ] && echo "zip" || echo "tar.gz") && \
./verify-signatures.sh archives/chainver_${LATEST}_${ARCH}.${EXT} && \
if [ "$ARCH" = "Windows_x86_64" ]; then \
  unzip -q archives/chainver_${LATEST}_${ARCH}.zip; \
else \
  tar xzf archives/chainver_${LATEST}_${ARCH}.tar.gz; \
fi && \
sudo mv chainver /usr/local/bin/ && \
cd .. && rm -rf chainver-*.zip chainver-package && \
chainver version
```

### Go

If you have the [Go runtime installed](https://go.dev/doc/install), you can
install `chainver` with the following:

```sh
go install github.com/chainguard-dev/chainver@latest
```

### Container Image

Run chainver using the Chainguard container image:

```sh
docker run -v /path/to/artifacts:/data \
  cgr.dev/chainguard/chainver:latest /data/your-artifact.jar
```

Analyze remote artifacts:

```sh
docker run cgr.dev/chainguard/chainver:latest \
  remote:repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.12.0/commons-lang3-3.12.0.jar
```

### Version-Agnostic Download

Download the latest release using `curl`. (Note that [`jq`](https://jqlang.org/download/) must be on the path.)

```sh
LATEST_URL=$(curl -s https://dl.enforce.dev/chainver/latest/latest-metadata.json | jq -r '.download_url') && \
 curl -LO "${LATEST_URL}"
```

## Authentication Setup

### Using chainctl

You can authenticate with your Chainguard organization using chainctl. First,
initiate the login flow:

```sh
chainctl auth login
```

Then log in using one of the provided options.

Next, find your organization name:

```sh
chainctl iam organizations list
```

When using `chainver` commands, provide the name of your organization using the
`--parent` flag as follows, replacing `<your-organization>` with the name of
your organization:

```sh
chainver --parent <your-organization> /path/to/artifact.jar
```

### Using Tokens

For CI/CD pipelines or environments without chainctl, you can use a token.
First, [create a pull token for Chainguard Libraries](https://edu.chainguard.dev/chainguard/libraries/access/#pull-token-for-libraries).

Once you have your token, you can authenticate by passing it to `chainver` using
the `--token` flag:

```sh
chainver --token <your-chainguard-token> /path/to/artifact.jar
```

Alternatively, set the token as an environment variable:

```sh
export CHAINGUARD_TOKEN=your-chainguard-token
chainver /path/to/artifact.jar
```

The following environment variables are supported:

- `CHAINCTL_TOKEN` or `CHAINGUARD_TOKEN` - Authentication token
- `JFROG_API_KEY` - JFrog Artifactory access
- `CLOUDSMITH_API_KEY` - Cloudsmith access

## Usage

Analyze a local `.jar` or `.whl` file:

```sh
chainver --parent <your-organization> commons-lang3-3.12.0.jar
```

Analyze a container image on a registry:

```sh
chainver --parent <your-organization> cgr.dev/chainguard/nginx:latest
```

Analyze a local container:

```sh
chainver redis:latest
chainver nginx:alpine
chainver ubuntu:20.04
```

Analyze a local image with localhost prefix:

```sh
chainver --parent <your-organization> localhost/myapp:latest
```

Analyze with detailed output:

```sh
chainver --detailed /path/to/archive.zip
```

Analyze multiple artifacts with detailed output:

```sh
chainver --detailed artifact1.jar artifact2.zip
```

JSON output for CI/CD integration:

```sh
chainver -o json /path/to/artifact.jar
```

Run via Docker:

```sh
docker run -v /path/to/artifacts:/data cgr.dev/chainguard/chainver:latest /data/your-artifact
```

Generate inventory from repository:

```sh
chainver inventory --ecosystem java remote:repo1.maven.org/maven2/org/apache
```

Analyze a remote artifact on Maven Central:

```sh
chainver --parent <your-organization> remote:repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.12.0/commons-lang3-3.12.0.jar
```

Analyze a remote artifact on PyPI:

```sh
chainver --parent <your-organization> remote:files.pythonhosted.org/packages/70/8e/0e2d847013cb52cd35b38c009bb167a1a26b2ce6cd6965bf26b47bc0bf44/requests-2.31.0-py3-none-any.whl
```

## Resources

- [Chainguard Libraries Overview](/chainguard/libraries/overview)
- [Chainguard Libraries Authentication](/chainguard/libraries/access/)
- [Learning Lab: Chainguard Libraries for Java](/software-security/learning-labs/ll202505/)
