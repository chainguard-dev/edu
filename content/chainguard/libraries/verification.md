---
title: "Chainguard Libraries verification"
linktitle: "Verification"
description:
  "Learn how to verify libraries and packages are from Chainguard
  Libraries using the chainctl tool for enhanced supply chain security"
type: "article"
date: 2025-07-03T12:00:00+00:00
lastmod: 2026-08-27T19:36:12+00:00
draft: false
tags: ["Chainguard Libraries"]
menu:
  docs:
    parent: "libraries"
weight: 004
toc: true
---

Chainguard's `chainctl` tool with the command [`libraries
verify`](/chainguard/chainctl/chainctl-docs/chainctl_libraries_verify/) verifies
which of your language ecosystem dependencies were built by Chainguard,
providing critical visibility into your software supply chain security. By
verifying binary artifacts across your projects and repositories, you can confirm which dependencies came from Chainguard's hardened build environment, identify opportunities to
improve security posture, and maintain compliance with supply chain security
policies.

For packages that aren't built by Chainguard, you can enable [upstream fallback](/chainguard/libraries/overview/#upstream-fallback-and-controls) to apply additional configurable security controls.

Command characteristics:

- Uses a signature-based binary identification and a checksum fallback.
- Supports different binary formats, including JAR, WAR, EAR, ZIP, TAR, WHL,
  APK, and npm tarballs (.tgz), as well as container images.
- Allows analysis of directories and nested archive files.
- Creates output in text, json, yaml, and CSV formats.

## Requirements

Before using `chainctl` to verify libraries, ensure you have the following
installed and available on your path:

- [`chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/) —
  Chainguard-maintained tool that includes the `libraries verify` command,
  details also in the [reference
  documentation](/chainguard/chainctl/chainctl-docs/chainctl_libraries_verify/).

`chainctl libraries verify` checks signatures in-process. To fetch the Sigstore
trust root, the command needs network access to `tuf-repo-cdn.sigstore.dev`.
Refer to [network requirements](/chainguard/libraries/network-requirements/) for
the full list of domains.

You also need:

- A Linux, macOS, or Windows system (x86_64 or arm64)
- Sufficient [network access](/chainguard/libraries/network-requirements/)
- Your organization [must include entitlement for access to Chainguard
  Libraries](/chainguard/libraries/access/#entitlement)
- You must have one of the `libraries.java.pull`, `libraries.javascript.pull`, or `libraries.python.pull` permissions, or the Owner role.

Confirm that `chainctl` is installed and available on the `PATH`:

```sh
chainctl version
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

> **Note**: Running `chainctl libraries verify` requires one of the `libraries.java.pull`, `libraries.javascript.pull`, or `libraries.python.pull` permissions, or the Owner role.

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

If you use Poetry and the virtual environment is not in the project directory, verify the environment returned by Poetry:

```bash
chainctl libraries verify --detailed "$(poetry env info --path)"
```

For CI/CD, use JSON output to save a machine-readable report:

```bash
chainctl libraries verify --detailed -o json .venv/ > provenance-report.json
```

### Analyze a Java JAR file

Analyze a Java `.jar` file:

```sh
chainctl libraries verify commons-lang3-3.17.0.jar
```

Verifying a JAR file is performed by looking up checksums and provenance
information from the Chainguard repositories. This requires network access and
can take longer if you analyze multiple files or archives that contain multiple
libraries. Typically, you find the JAR files in the local Maven repository cache
in `~/.m2/repository`. For best results, verify individual JAR files from this cache before packaging your application. Refer to [Java fat JAR limitations](#java-fat-jar-limitations) for more details.

Analyze a deployment archive for your custom application that contains other
libraries:

```sh
chainctl libraries verify example-application.tar.gz
```

Note that if your deployment archive is a fat JAR, uber JAR, or shaded JAR,
verification returns 0% coverage. This is expected behavior; refer to [Java fat JAR limitations](#java-fat-jar-limitations) for the recommended verification
approach.

For other archive types such as tarballs that contain individual unmodified JAR
files, scanning can take a significant amount of time if numerous libraries are
included. Consider detailed output with the `--detailed` flag
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

#### Recommended build-time workflow for Maven

For Maven-based applications, a recommended workflow is to copy only runtime dependencies into a dedicated directory then verify those files, allowing you to avoid noise from unrelated artifacts in `~/.m2/repository`. For example:

```bash
mvn -U -q -s settings.xml dependency:copy-dependencies \
  -DincludeScope=runtime \
  -DoutputDirectory=target/chainguard-verify

chainctl libraries verify -o json --detailed target/chainguard-verify/*.jar \
  > provenance-report.json
```

> Note: If you belong to multiple Chainguard organizations, include the `--parent=<org>` flag in the command.

It can take up to 5 minutes for this command to return results. It returns output similar to the following:

```bash
{
  "artifactVerificationCoverage": 74.19354838709677,
  "verifiedItems": 23,
  "totalItems": 31,
  "artifactsSummary": {
    "totalArtifacts": 31,
    "fullyVerified": 23,
    "partiallyVerified": 0,
    "notVerified": 8,
    "verifiedPercent": 74.19354838709677
  },
  "results": [
    {
      "artifact": "target/chainguard-verify/jakarta.validation-api-3.0.2.jar",
      "artifactVerificationCoverage": 100,
      "details": "Fully verified by Chainguard (signature verified)\nMaven artifact: jakarta.validation:jakarta.validation-api:3.0.2"
    },
...
```

In this example, out of 31 `totalItems`, 23 were verified. The `arfifactVerificationCoverage` percent is 74.

#### Java fat JAR limitations

The fat JAR packaging approach merges the class files from all dependency
JARs into one combined archive, which means the original JAR boundaries are
lost.

Because `chainctl libraries verify` identifies libraries by checking checksums
and provenance information against individual JAR files, it cannot trace merged
class files back to their source JARs. As a result, running `chainctl libraries
verify` against a fat JAR returns 0% coverage, even if the
dependencies inside it were sourced from Chainguard Libraries.

#### Recommended verification approach for fat JARs

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

### Analyze JavaScript packages

`chainctl libraries verify` can scan local package manager caches and stores
to confirm that your installed JavaScript packages were built by Chainguard. It supports the following JavaScript package managers:

- pnpm store: auto-detected by `v10/index/` or `v11/index/` structure (pnpm v10 and v11 supported)
- npm cache: auto-detected by `_cacache/index-v5/` structure
- Yarn Classic: v1.x, requires `yarn:` prefix

#### Analyze an npm tarball

Verify an npm package tarball to confirm it was built by Chainguard:

```sh
chainctl libraries verify PACKAGE-VERSION.tgz
```

Replace `PACKAGE`
and `VERSION` with the package name and version (for example, `@eslint-js`
and `9.0.0`)

Verification uses SLSA provenance attestations. `chainctl` computes a SHA-512 digest of the tarball locally, fetches the signed attestation bundle, and verifies in-process that the signature is valid, the certificate chains to the Sigstore root, the signer identity matches the Chainguard JavaScript builder, and the digest matches what was attested at build time.

#### Verify an npm cache

Verify your npm cache:

```sh
chainctl libraries verify "$(npm config get cache)"
```

#### Verify a pnpm store

Verify your pnpm store. Use `--store-dir` to install to an explicit path and verify that location:

```sh
pnpm install --store-dir /tmp/my-pnpm-store
chainctl libraries verify /tmp/my-pnpm-store
```

pnpm v9 and earlier are not supported. Verification works by comparing
the tarball hash recorded in your local store against the hash in Chainguard's
signed SLSA attestation. pnpm v10 records this hash in the index file path;
pnpm v9 does not.

Note that in `pnpm-lock.yaml`, packages resolved from Chainguard have only a
`resolution:` entry with an integrity hash:

```yaml
supports-color@7.2.0:
  resolution: {integrity: sha512-LPhWJX...}
```

Packages that are pulled from the upstream fallback include an explicit `tarball:` URL pointing to `javascript-upstream`. For example:

```yaml
tar-fs@2.1.4:
  resolution: {integrity: sha512-mDAjwm..., tarball: https://libraries.cgr.dev/javascript-upstream/tar-fs/-/tar-fs-2.1.4.tgz}
```

#### Verify a Yarn Classic cache

Verify a Yarn Classic (v1) cache:

```sh
chainctl libraries verify yarn:
```

To specify a non-default cache location:

```sh
chainctl libraries verify yarn:~/Library/Caches/Yarn/v6
```

Unlike npm and pnpm, Yarn Classic requires the `yarn:` prefix because its
cache directory layout cannot be reliably auto-detected.

#### Verify a `node_modules` directory

Verify npm packages installed in a `node_modules` directory:

```sh
chainctl libraries verify ./node_modules
```

If `.package-lock.json` is not present, the directory is not recognized as an npm tree and verification will not run.

#### Verify a container image

Verify JavaScript packages inside a container image:

```sh
chainctl libraries verify IMAGE:TAG
```

Coverage is reported as the percentage of JavaScript packages in the image that are confirmed Chainguard-rebuilt libraries.

Images built with npm versions earlier than v7, or where `.package-lock.json` was removed during the build, cannot be verified this way.

### Other bundled artifact formats

The same limitation applies to other ecosystems where dependencies are bundled
into a single output artifact, such as JavaScript bundles and Python
applications packaged with tools that inline dependencies. Dependencies may also
be minified, partially copied, or otherwise transformed during the build
process. In all of these cases, verification should also be performed against
the original package files before bundling rather than against the final output
artifact.

## Verify artifacts in a repository manager

You can verify what artifacts are retrieved from the Chainguard Libraries
repository on a global level:

- **Artifactory and Nexus**: Browse the `chainguard` proxy repository on your repository manager server.
- **Cloudsmith**: Access the **Packages** tab of the repository on your Cloudsmith instance.
  Filter the package list with the tag value with the name for your upstream
  proxy for Chainguard, for example `tag:chainguard`. The tag uses the name of
  the upstream proxy, with spaces replaced with dashes.

Use the browsing access to locate specific artifacts and identify their name,
file size, checksum values, timestamp and other identifiers. With these details
you can verify your libraries use in the following locations:

- Local cache repositories on developer workstation
- Cache repositories in your CI pipeline
- Libraries in your application bundles
- Installed applications on your hosts or in your container images

A uniquely identifying characteristic of library artifacts are their checksums.
Contrary to filenames and timestamps, checksums do not change in the use of
libraries during an application build or the assembly of a deployment artifact
like a tarball or container. This allows you to identify a library artifact by
determining the checksum and then locating it in your repository manager.

Calculate the different commonly used sums for a file `example.jar` with the
following commands and output examples:

```
$ sha1sum example.jar
aea83e64ebec6a37e0be100f968a55fb381143c2  example.jar

$ sha256sum example.jar
87a25c44e0fdb0c71e898c57f67b236d2205bfa76a25dbbb9779ebe2f93e787e  example.jar

$ md5sum example.jar
fefd660ddc795900d48bdf49c17b3135  example.jar
```

Use the search features in your repository manager to
locate the library. For the specific example, you find that the checksums
correspond to the file `junit-4.13.2.jar` found in `junit/junit/4.13.2/` and
that the artifact is found in the `chainguard` proxy repository. You can
therefore conclude that the `example.jar` file originates from Chainguard, was
built in the Chainguard Factory from source, and is available at
`https://libraries.cgr.dev/java/junit/junit/4.13.2/junit-4.13.2.jar`. You can
[manually download the file to
compare](/chainguard/libraries/java/overview/#manual-access/), if desired.

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

## Troubleshooting

### Why might I see 0% coverage when verifying Java artifacts?

A 0% coverage result is expected when verifying a fat JAR, uber JAR, or shaded JAR. Those packaging formats merge dependency contents into a single archive, so `chainctl libraries verify` cannot trace merged classes back to the original JARs.

## Resources

- [Chainguard Libraries overview](/chainguard/libraries/overview/)
- [Chainguard Libraries authentication](/chainguard/libraries/access/)
- [`chainctl libraries verify` reference documentation](/chainguard/chainctl/chainctl-docs/chainctl_libraries_verify/)
- [{{<icon "play-circle-fill">}} Learning Lab: Chainguard Libraries for Java](/software-security/learning-labs/ll202505/)
- [{{<icon "play-circle-fill">}} Learning Lab: Chainguard Libraries for Python](/software-security/learning-labs/ll202506/)
