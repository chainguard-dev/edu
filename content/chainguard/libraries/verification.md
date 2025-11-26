---
title: "Chainguard Libraries Verification"
linktitle: "Verification"
description:
  "Learn how to verify libraries and packages are from Chainguard
  Libraries using the chainctl tool for enhanced supply chain security"
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

Chainguard's `chainctl` tool with the command `libraries verify` verifies that
your language ecosystem dependencies come from Chainguard Libraries, providing
critical visibility into your software supply chain security. By verifying
binary artifacts across your projects and repositories, you can ensure
dependencies are sourced from Chainguard's hardened build environment rather
than potentially compromised public repositories, identify opportunities to
improve security posture, and maintain compliance with supply chain security
policies.

Command characteristics:

- Uses a signature-based binary identification and a checksum fallback.
- Supports different binary formats, including JAR, WAR, EAR, ZIP, TAR, WHL, and
  APK files as well as container images.
- Allows analysis of directories and nested archive files.
- Creates output in text, json, yaml, and CSV formats.

## Requirements

Before using chainctl to verify libraries, ensure you have the following
installed and available on your path:

- [`chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/)
  — Chainguard-maintained tool that includes the libraries verify command.
- [`cosign`](https://docs.sigstore.dev/cosign/system_config/installation/) — A
  Sigstore-maintained tool used to verify signatures.

You also need:

- A Linux, macOS, or Windows system (x86_64 or arm64)
- Sufficient [network access](/chainguard/libraries/network-requirements/)
- Your organization [must include entitlement for access to Chainguard
  Libraries](/chainguard/libraries/access/#entitlement)

Confirm that `chainctl` and `cosign` are installed and available on the `PATH`
with the following commands:

```sh
chainctl version
```

```sh
cosign version
```

## Authentication and configuration

You can authenticate with your Chainguard organization using `chainctl`. First,
initiate the login flow:

```sh
chainctl auth login
```

TBD CONFIRM 
If you are member of one organization only, you can proceed to use `libraries
verify` and other commands.

If you are member of multiple organizations you must provide the name of your
organization using the `--parent` flag as follows, replacing
`<your-organization>` with the name of your organization, with every command:

```sh
chainctl libaries verify --parent <your-organization> /path/to/artifact.jar
```

To avoid the need for the additional parameter, you can configure a default
organization with the following steps:

Find your organization name with the entitlement:

```sh
chainctl iam organizations list
```

Set the configuration for the default group: TBD - this does NOT yet work, also maybe default.org-name instead??

```sh
chainctl config set default.group <your-organization>
```

Verify the configuration:

```sh
chainctl config view
```

Ensure to use this configuration or add the `--parent` parameter in all
following examples as necessary.

## Usage

Analyze a local `.jar` or `.whl` file:

```sh
chainctl libraries verify commons-lang3-3.12.0.jar
```

Analyze a container image on a registry:

```sh
chainctl  libraries verify cgr.dev/chainguard/nginx:latest
```

Analyze a local container:

```sh
chainctl libraries verify redis:latest
chainctl libraries verify nginx:alpine
chainctl libraries verify ubuntu:20.04
```

Analyze a local image with localhost prefix:

```sh
chainctl libraries verify --parent <your-organization> localhost/myapp:latest
```

Analyze with detailed output:

```sh
chainctl libraries verify --detailed /path/to/archive.zip
```

Analyze multiple artifacts with detailed output:

```sh
chainctl libraries verify --detailed artifact1.jar artifact2.zip
```

Receive JSON output:

```sh
chainver libraries verify -o json /path/to/artifact.jar
```

Generate inventory from repository. Note that passing a URL from the public
Maven Central repository returns a negative result, because packages were not
built by Chainguard.

```sh
chainctl libraries verify inventory --ecosystem java remote:repo1.maven.org/maven2/org/apache
```

Analyze a remote artifact on Maven Central:

```sh
chainctl libraries verify remote:repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.12.0/commons-lang3-3.12.0.jar
```

Analyze a remote artifact on PyPI:

```sh
chainver libraries verify remote:files.pythonhosted.org/packages/70/8e/0e2d847013cb52cd35b38c009bb167a1a26b2ce6cd6965bf26b47bc0bf44/requests-2.31.0-py3-none-any.whl
```

## Resources

- [Chainguard Libraries Overview](/chainguard/libraries/overview/)
- [Chainguard Libraries Authentication](/chainguard/libraries/access/)
- [Learning Lab: Chainguard Libraries for Java](/software-security/learning-labs/ll202505/)
- [Learning Lab: Chainguard Libraries for Python](/software-security/learning-labs/ll202506/)
