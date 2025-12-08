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

- [`chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/) —
  Chainguard-maintained tool that includes the `libraries verify` command.
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

If you are a member of one organization only, you can proceed to use `libraries
verify` and other commands.

If you are a member of multiple organizations, you must provide the name of your
organization using the `--parent` flag as follows, replacing
`<your-organization>` with the name of your organization, with every command:

```sh
chainctl libraries verify --parent <your-organization> /path/to/artifact.jar
```

To avoid the need for the additional parameter, you can configure a default
organization with the following steps.

Find your organization name with the entitlement:

```sh
chainctl iam organizations list
```

Set the configuration for the default group:

```sh
chainctl config set default.group <your-organization>
```

Verify the configuration:

```sh
chainctl config view
```

Ensure that you use this configuration or add the `--parent` parameter in all
the following examples as necessary.

## File analysis

Analyze a Python wheel file in the current directory:

```sh
chainctl libraries verify flask-3.0.1-py3-none-any.whl
```

The analysis of wheel files is fast because the provenance information is
available within the archive.

Analyze a local Java `.jar` file:

```sh
chainctl libraries verify commons-lang3-3.17.0.jar
```

Verifying a JAR file is performed by looking up checksums and provenance
information from the Chainguard repositories. This requires network access and
can take longer if you analyze multiple files or archives that contain multiple
libraries.

Analyze a deployment archive for your custom application that contains other
libraries:

```sh
chainctl libraries verify example-application.tar.gz
```

Note that scanning larger archives that contain numerous libraries can take a
significant amount of time. Consider detailed output with the `--detailed` flag
for more information about the performed verification steps, and potentially
pipe the output into a file.

```sh
chainctl libraries verify --detailed commons-lang3-3.17.0.jar > run.log 
```

Use the `--verbose` flag for even more details.

Analyze multiple artifacts output:

```sh
chainctl libraries verify artifact1.jar artifact2.zip
```

Analyze a file and create JSON output:

```sh
chainctl libraries verify -o json commons-lang3-3.17.0.jar
```

## Container analysis

You can also analyze container images to verify the libraries contained within
the container. Note that this requires more time to verify depending on the
container size, and the number and type of included libraries.

Analyze a container image:

```sh
chainctl libraries verify cgr.dev/chainguard/maven:latest
```

Note that the analysis separately downloads the container tarball and analyzes
it, rather than any container available in your local container setup.

Analyze a local image with localhost prefix:

```sh
chainctl libraries verify localhost/myapp:latest
```

## Other examples

The following examples use Maven Central and PyPI URLs and returns a negative
result, because packages were not built by Chainguard. A practical use of this
functionality points to an internal repository manager with a mixture of
artifacts from Chainguard and elsewhere.

Analyze a remote artifact on Maven Central:

```sh
chainctl libraries verify remote:repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.17.0/commons-lang3-3.17.0.jar
```

Analyze a remote artifact on PyPI:

```sh
chainctl libraries verify remote:files.pythonhosted.org/packages/...../requests-2.31.0-py3-none-any.whl
```

## Built-in help

Use the `help` command for more command options and details for the `verify` command:

```sh
chainctl help libraries verify
```

## Resources

- [Chainguard Libraries Overview](/chainguard/libraries/overview/)
- [Chainguard Libraries Authentication](/chainguard/libraries/access/)
- [Learning Lab: Chainguard Libraries for Java](/software-security/learning-labs/ll202505/)
- [Learning Lab: Chainguard Libraries for Python](/software-security/learning-labs/ll202506/)
