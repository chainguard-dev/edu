---
title: "Chainguard Libraries verification"
linktitle: "Verification"
description:
  "Learn how to verify libraries and packages are from Chainguard
  Libraries using the chainctl tool for enhanced supply chain security"
type: "article"
date: 2025-07-03T12:00:00+00:00
lastmod: 2026-01-06T15:09:59+00:00
draft: false
tags: ["Chainguard Libraries"]
menu:
  docs:
    parent: "libraries"
weight: 004
toc: true
---

## Overview

Chainguard's `chainctl` tool with the command [`libraries
verify`](/chainguard/chainctl/chainctl-docs/chainctl_libraries_verify/) verifies
that your language ecosystem dependencies come from Chainguard Libraries,
providing critical visibility into your software supply chain security. By
verifying binary artifacts across your projects and repositories, you can ensure
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
  Chainguard-maintained tool that includes the `libraries verify` command,
  details also in the [reference
  documentation](/chainguard/chainctl/chainctl-docs/chainctl_libraries_verify/).
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

### Analyze a Python wheel file

Analyze a Python wheel file in the current directory:

```sh
chainctl libraries verify flask-3.0.1-py3-none-any.whl
```

The analysis of wheel files is fast because the provenance information is
available within the archive. Python development tools often unpack the wheel
file and you can also scan these extracted packages. For example, if you create
a virtual environment in your Python project, you can subsequently analyze the
package in the virtual environment:

```sh
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
chainctl libraries verify --detailed ./venv/
```

### Analyze a local Java JAR file

Analyze a local Java `.jar` file:

```sh
chainctl libraries verify commons-lang3-3.17.0.jar
```

Verifying a JAR file is performed by looking up checksums and provenance
information from the Chainguard repositories. This requires network access and
can take longer if you analyze multiple files or archives that contain multiple
libraries. Typically, you find the JAR files in the local Maven repository cache
in `~/.m2/repository`. For best results, verify individual JAR files from this cache before packaging your application. See [Java fat JAR limitations](#java-fat-jar-limitations) for more details.

Analyze a deployment archive for your custom application that contains other
libraries:

```sh
chainctl libraries verify example-application.tar.gz
```

Note that if your deployment archive is a fat JAR, uber JAR, or shaded JAR,
verification will return 0% coverage. This is expected behavior; see [Java fat JAR limitations](#java-fat-jar-limitations) for the recommended verification
approach. 

For other archive types such as tarballs that contain individual
unmodified JAR files, scanning larger archives that contain numerous libraries can take a
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

## Java fat JAR limitations

The fat JAR packaging approach merges the class files from all dependency
JARs into one combined archive, which means the original JAR boundaries are
lost.

Because `chainctl libraries verify` identifies libraries by checking checksums
and provenance information against individual JAR files, it cannot trace merged
class files back to their source JARs. As a result, running `chainctl libraries
verify` against a fat JAR returns 0% coverage, even if the
dependencies inside it were sourced from Chainguard Libraries.

### Recommended verification approach for fat JARs

To verify that your Java dependencies come from Chainguard Libraries, run
`chainctl libraries verify` during your build process against the individual JAR
files in your local Maven repository cache, **before** fat JAR assembly.

After resolving dependencies with Maven, the individual JAR files are available
in `~/.m2/repository`. The following example uses `net.logstash.logback:logstash-logback-encoder:8.1`
as the library, but you can replace the path with the specific JAR you want to verify:

```sh
chainctl libraries verify ~/.m2/repository/net/logstash/logback/logstash-logback-encoder/8.1/logstash-logback-encoder-8.1.jar
```

To integrate this into your build pipeline, add the verification step after
dependency resolution and before the packaging phase. 

### Other bundled artifact formats

The same limitation applies to other ecosystems where dependencies are bundled
into a single output artifact, such as JavaScript bundles and Python
applications packaged with tools that inline dependencies. In these cases,
verification should also be performed against the original package files before
bundling rather than against the final output artifact.

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
artifacts from Chainguard and elsewhere. Note that authentication to the
repository is not supported and you must download artifacts to a local directory
as an alternative method to verify them.

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
- [`chainctl libraries verify` reference documentation](/chainguard/chainctl/chainctl-docs/chainctl_libraries_verify/)
- [Learning Lab: Chainguard Libraries for Java](/software-security/learning-labs/ll202505/)
- [Learning Lab: Chainguard Libraries for Python](/software-security/learning-labs/ll202506/)
