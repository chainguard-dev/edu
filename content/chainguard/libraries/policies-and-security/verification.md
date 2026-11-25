---
title: "Chainguard Libraries verification"
linktitle: "Verification"
description:
  "Learn how to verify libraries and packages are from Chainguard
  Libraries using the chainctl tool for enhanced supply chain security"
type: "article"
date: 2025-07-03T12:00:00+00:00
lastmod: 2026-11-25T12:00:00+00:00
draft: false
tags: ["Chainguard Libraries"]
menu:
  docs:
    parent: "policies-and-security"
weight: 20
toc: true
aliases:
  - /chainguard/libraries/verification/
---

Chainguard's `chainctl` tool with the command [`libraries
verify`](/platform/chainctl/chainctl-docs/chainctl_libraries_verify/) verifies
which of your language ecosystem dependencies were built by Chainguard,
providing critical visibility into your software supply chain security. By
verifying binary artifacts across your projects and repositories, you can confirm which dependencies came from Chainguard's hardened build environment, identify opportunities to
improve security posture, and maintain compliance with supply chain security
policies.

For packages that aren't built by Chainguard, you can enable [upstream fallback](/chainguard/libraries/introduction/overview/#upstream-fallback-and-controls) to apply additional configurable security controls.

Command characteristics:

- Uses a signature-based binary identification and a checksum fallback.
- Supports different binary formats, including JAR, WAR, EAR, ZIP, TAR, WHL,
  APK, npm tarballs (.tgz), and NuGet packages (.nupkg), as well as container
  images.
- Allows analysis of directories and nested archive files.
- Creates output in text, json, yaml, and CSV formats.

## Supported inputs by ecosystem

The following table lists what `chainctl libraries verify` accepts for each
ecosystem:

| Ecosystem | Accepted inputs | Lockfiles |
|---|---|---|
| Java | JAR, WAR, and EAR files; archives that contain them; container images; `remote:` URLs | Not supported. Verify the JAR files. |
| JavaScript | npm tarballs (`.tgz`), npm cache, pnpm store, Yarn Classic cache, `node_modules` directories, container images | `package-lock.json`, `npm-shrinkwrap.json`, `pnpm-lock.yaml`, `yarn.lock`, `bun.lock` |
| Python | Wheel files, installed virtual environments, `remote:` wheel URLs | Not supported. Verify the installed environment or the wheel files. |
| .NET | `.nupkg` files, directories of them, the NuGet global packages folder, a published app's `*.deps.json` or its directory, container images, `remote:` and `jfrog:` URLs | `packages.lock.json` |
| Go | Not supported | Not supported |

For Go, `go mod verify` checks downloaded modules against `go.sum`. It doesn't
verify Chainguard provenance.

### Identify upstream fallback packages in a lockfile

Some lockfiles record the URL of each package, which can show whether the
package came from [upstream
fallback](/chainguard/libraries/introduction/overview/#upstream-fallback-and-controls):

- **JavaScript**: In `pnpm-lock.yaml`, a package from upstream fallback has a
  `tarball:` URL under `/javascript-upstream/`, as shown in [Verify a pnpm
  store](#verify-a-pnpm-store).
- **Python**: In `uv.lock`, each wheel's `url` and the `sdist.url` show a
  `/python-upstream/` route for a file from upstream fallback. uv records the
  route per file, so a package can list Chainguard-built wheels for some
  platforms and upstream wheels for others. The wheel you install depends on
  your platform. The `source` registry URL shows `/python/` either way.
  `poetry.lock` records only filenames and hashes, so it doesn't show where a
  file came from.

A repository manager can rewrite these URLs. A URL without
`/javascript-upstream/` or `/python-upstream/` therefore doesn't prove that
Chainguard built the package. To confirm which packages Chainguard built, run
`chainctl libraries verify` against a supported input.

## Requirements

Before using `chainctl` to verify libraries, ensure you have the following
installed and available on your path:

- [`chainctl`](/platform/chainctl-usage/how-to-install-chainctl/) —
  Chainguard-maintained tool that includes the `libraries verify` command,
  details also in the [reference
  documentation](/platform/chainctl/chainctl-docs/chainctl_libraries_verify/).

`chainctl libraries verify` checks signatures in-process. To fetch the Sigstore
trust root, the command needs network access to `tuf-repo-cdn.sigstore.dev`.
Refer to [network requirements](/chainguard/libraries/introduction/network-requirements/) for
the full list of domains.

Local .NET inputs are an exception. A run that checks only local `.nupkg`
files, NuGet packages folders, NuGet lockfiles, or .NET deps files needs no
token, no entitlement, and no network access, because the Chainguard signature
is inside each package. This holds only without `--fetch-missing` and
`--output-attestations`. For details, refer to [Analyze .NET
packages](#analyze-net-packages).

You also need:

- A Linux, macOS, or Windows system (x86_64 or arm64)
- Sufficient [network access](/chainguard/libraries/introduction/network-requirements/)
- Your organization [must include entitlement for access to Chainguard
  Libraries](/chainguard/libraries/introduction/access/#entitlement)
- One of the following for each ecosystem you verify:
    - The `pull_token_creator` role, such as
      `libraries.java.pull_token_creator`, or the `owner` role. After a regular
      `chainctl auth login`, the command creates a pull token to fetch
      provenance data, which requires one of these roles. Each run creates a
      new pull token, which appears in your organization's identity list as
      `pull-token - libraries.<ecosystem>`.
    - The `pull` role, such as `libraries.java.pull`, with a libraries-scoped
      token, as described in [Verify with a pull role](#verify-with-a-pull-role).
      The command uses the token directly and creates no pull token.

  For what each role includes, refer to [Pull token creator
  roles](/platform/administration/iam-organizations/roles-role-bindings/capabilities-reference/#pull-token-creator-roles).

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

### Verify with a pull role

If your identity holds only a `pull` role, such as `libraries.java.pull`, sign
in with the libraries registry as the audience and pass the resulting token to
the command in the `CHAINCTL_AUTH_TOKEN` environment variable:

```sh
chainctl auth login --audience=libraries.cgr.dev
export CHAINCTL_AUTH_TOKEN="$(chainctl auth token --audience=libraries.cgr.dev)"
chainctl libraries verify /path/to/artifact.jar
```

Without `CHAINCTL_AUTH_TOKEN`, a `pull` role reports 0% coverage, even after you
sign in with the libraries audience. Because this method creates no pull token,
it also keeps repeated runs, such as CI/CD jobs, from adding a pull token to
your organization each time.

## Verification results

`chainctl libraries verify` reports coverage: the share of the inspected
artifacts that Chainguard built from source. It doesn't report
vulnerabilities, policy decisions, or whether an artifact is safe to deploy. A
package that your organization received through [upstream
fallback](/chainguard/libraries/introduction/overview/#upstream-fallback-and-controls)
counts as not verified, so coverage below 100% is expected when upstream
fallback is on.

The report is informational. Keep the following in mind when you run the
command in CI/CD:

- The command exits with status 0 whatever the coverage, so the exit status
  can't gate a build. Gating a build on the coverage percentage isn't the
  intended use either.
- If the command can't obtain credentials, for example because the identity
  lacks the [required role](#requirements), it prints an error, reports 0%
  coverage, and still exits with status 0. With `-o json`, the JSON report
  doesn't include the error. Before you trust a 0% result, check the command's
  error output.
- For JavaScript lockfiles, entries that the registry couldn't answer for,
  because of an outage or rejected credentials, are reported as unchecked
  rather than unverified.

## File analysis

To save available Software Bills of Materials (SBOMs) and attestations while
verifying Java artifacts, JavaScript packages, Python wheels, or NuGet
packages, add
`--output-attestations`. Use `--output-dir` to choose the base directory, which
defaults to `attestations` in the current directory. Only packages verified as
Chainguard builds produce companion files. The verification report lists the
saved files and their trust status in text, JSON, YAML, and CSV output.

> **Note**: Running `chainctl libraries verify` requires the `pull_token_creator` role for the ecosystem you verify, the `owner` role, or a `pull` role with a libraries-scoped token. For details, refer to [Requirements](#requirements).

### Analyze a Python wheel file

`chainctl libraries verify` checks installed virtual environments and wheel
files. It doesn't support Python lockfiles, such as `requirements.txt`,
`uv.lock`, or `poetry.lock`, and reports an unsupported file type error if you
pass one.

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

[Verification results](#verification-results) explains what this report can and can't tell a pipeline.

#### Download Python SBOMs and attestations

Save the available companions for a verified wheel:

```sh
chainctl libraries verify flask-3.0.1-py3-none-any.whl --output-attestations
```

Files are saved under `--output-dir`, which defaults to `attestations`, in a
directory named for the normalized package name and version. For the preceding
command, the directory is `attestations/flask/3.0.1/`, with these files when
available:

- `flask-3.0.1-py3-none-any.whl.signature-bundle.json` — The exact Sigstore bundle
  used to verify the wheel.
- `flask-3.0.1-py3-none-any.whl.pep740-attestation.json` — PEP 740 provenance.
  Before saving it as trusted, `chainctl` independently verifies its signature,
  the Chainguard Python signer identity and issuer, and the wheel's SHA-256
  digest as an attested subject.
- `flask-3.0.1-py3-none-any.whl.sbom.spdx.json` — The SPDX SBOM extracted from the
  verified wheel's top-level `.dist-info/sboms/` directory.

The full wheel filename distinguishes companions for different platform and
Python builds of the same package version. Remediated versions with a `+cgr`
suffix also support downloads. Legacy signature bundles served from the
provenance endpoint do not produce a PEP 740 file.

Downloads require a wheel file. An installed Python environment or a source
distribution does not produce companion files. For details about the formats,
refer to [SBOM and attestation
files](/chainguard/libraries/python/overview/#sbom-and-attestation-files).

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

In this example, out of 31 `totalItems`, 23 were verified. The `artifactVerificationCoverage` percent is 74.

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

#### Download SBOMs and attestations

During verification, `chainctl` fetches the SBOM and SLSA provenance published
alongside a Chainguard-built Java artifact and discards them after the check.
Add the `--output-attestations` flag to save these files to disk instead:

```sh
chainctl libraries verify commons-lang3-3.17.0.jar --output-attestations
```

Use `--output-dir` to set the base directory, which defaults to `attestations`.
Files are written under each artifact's Maven repository path,
`group/artifact/version`, matching the layout of a local Maven repository:

```sh
chainctl libraries verify commons-lang3-3.17.0.jar \
  --output-attestations --output-dir repo
```

For the preceding command, the files land under
`repo/org/apache/commons/commons-lang3/3.17.0/`:

- `commons-lang3-3.17.0.spdx.json` — SPDX SBOM, saved as a trusted Chainguard
  attestation
- `commons-lang3-3.17.0.slsa-attestation.json` — SLSA provenance, also saved
  as trusted
- `commons-lang3-3.17.0-cyclonedx.json` and `commons-lang3-3.17.0-cyclonedx.xml`
  — CycloneDX SBOMs, saved when present but marked unverified, since
  Chainguard does not vouch for their contents

Only an artifact that verifies as a Chainguard build saves anything. Upstream or
tampered bytes save nothing. Inside a fat JAR, each embedded library is verified
and saved individually, so only the verified libraries contribute files. The
saved files are listed in the text, JSON, YAML, and CSV output, with unverified
files clearly marked.

For a description of these files and the alternative of downloading them
directly, refer to [SBOM and attestation
files](/chainguard/libraries/java/overview/#sbom-and-attestation-files).

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

#### Verify JavaScript lockfiles without installing dependencies

> **Note**: This command requires `chainctl` v0.2.354 or later.

Verify a JavaScript lockfile directly, without running an install and without requiring `node_modules` or a persistent package manager cache:

```sh
chainctl libraries verify package-lock.json
```

Supported lockfiles include `package-lock.json`, `npm-shrinkwrap.json`, `pnpm-lock.yaml`, `yarn.lock`, and `bun.lock`.

This command verifies what the lockfile claims will be installed. It does not verify the package bytes present on disk.

An entry counts as verified only when the lockfile binds it to the tarball that Chainguard attested. A single integrity hash binds the entry, because the package manager rejects any tarball that doesn't match it. An entry that lists several integrity hashes is reported as attested but not bound, because a tarball matching any one of them would install. The exception is an entry whose resolved URL is on the Chainguard built route, `https://libraries.cgr.dev/javascript/`, which fixes the source.

By default, `chainctl libraries update-hashes` adds the Chainguard hash alongside the original registry hash, which produces multi-hash entries. Those entries verify only while they resolve from the Chainguard built route, so behind a repository manager or a custom `--registry-url` they're reported as not bound. To record a single Chainguard hash per entry, run `chainctl libraries update-hashes --replace`. Entries bound this way verify regardless of where they resolve from.

Entries with no usable digest, such as linked dependencies, git dependencies, and Yarn Berry checksums, are reported at zero coverage.

#### Download JavaScript SBOMs and attestations

Save the available companions for a verified npm tarball:

```sh
chainctl libraries verify lodash-4.17.21.tgz --output-attestations
```

Files are saved under `--output-dir`, which defaults to `attestations`, in a
directory named `name/version/`, or `@scope/name/version/` for scoped packages.
For the preceding command, the directory is `attestations/lodash/4.17.21/`,
with these files when available:

- `lodash-provenance-4.17.21.sigstore` — The exact signed SLSA provenance bundle
  verified against the package's integrity digest and Chainguard signer identity.
- `lodash-sbom-4.17.21.spdx.json` — The SPDX SBOM retrieved from the authenticated
  Chainguard SBOM endpoint. `chainctl` reports it as trusted based on that
  endpoint. The npm provenance does not cryptographically bind the SBOM's bytes.

The flags also work for npm caches, pnpm stores, Yarn Classic caches, installed
`node_modules` directories, and supported JavaScript lockfiles. For example,
save companions while verifying the dependencies recorded in a lockfile:

```sh
chainctl libraries verify package-lock.json --output-attestations
```

For lockfiles, downloads require verified provenance that identifies the package
the lockfile will install. Ambiguous entries with multiple candidate integrity
hashes do not produce companion files unless the resolved URL identifies the
Chainguard build.

Missing SBOMs are skipped. If the verified provenance bundle cannot be read,
`chainctl` warns and skips downloads for that package. If saving a later
companion fails, the report still lists successfully saved files with a warning.

For manual retrieval, refer to [Provenance and
attestations](/chainguard/libraries/javascript/overview/#provenance-and-attestations).

#### Verify a container image

Verify JavaScript packages inside a container image:

```sh
chainctl libraries verify IMAGE:TAG
```

Coverage is reported as the percentage of JavaScript packages in the image that are confirmed Chainguard-rebuilt libraries.

Images built with npm versions earlier than v7, or where `.package-lock.json` was removed during the build, cannot be verified this way.

### Analyze .NET packages

> **Note**: .NET package verification requires `chainctl` v0.2.397 or later.
> Lockfile, published app, and container image verification require v0.2.409
> or later. The provenance check and the downloads in [Download .NET SBOMs and
> attestations](#download-net-sboms-and-attestations) require v0.2.408 or
> later.

`chainctl libraries verify` checks a NuGet package (`.nupkg`) by the Chainguard
package signature inside it. Each .NET package that Chainguard builds carries an
author signature, made with the Chainguard code-signing certificate and
timestamped. `chainctl` checks this signature against the certificate that it
pins. The check reads only the package, so it needs no token, no network
access, and no Sigstore trust root.

#### Verify a NuGet package

Verify a `.nupkg` file:

```sh
chainctl libraries verify Newtonsoft.Json.13.0.3.nupkg
```

For a package to verify, all of the following conditions must be true:

- The package carries an author signature under the Chainguard code-signing
  certificate that `chainctl` pins.
- The signature was made for this package. A Chainguard signature copied from
  another package does not verify.
- The signature carries an RFC 3161 timestamp that chains to a timestamp root
  that `chainctl` pins. Because of the timestamp, a signature stays valid after
  the signing certificate expires.

A verified package reports 100% coverage. Its details are `Fully verified by
Chainguard (package signature verified)`. With `-o json --detailed`, the
verification method names the signer, the SHA-256 fingerprint of its
certificate, and the time of the timestamp. A package that fails a condition,
such as a package from nuget.org that Chainguard did not build, reports 0%
coverage.

Chainguard can sign a package with a new certificate that your `chainctl`
release does not pin yet. The result is then indeterminate, and the details tell
you to upgrade `chainctl`. Upgrade, then run the command again.

`chainctl` also verifies a NuGet package in a remote repository. It downloads
the package and checks it the same way. The download never uses your Chainguard
token. If the repository needs an API key, `chainctl` uses that key. For a JFrog
repository, `chainctl` reads the key from `ARTIFACT_API_KEY`. If
`ARTIFACT_API_KEY` is not set, it reads `JFROG_API_KEY`:

```sh
chainctl libraries verify jfrog:example.jfrog.io/artifactory/nuget-remote/polysharp.1.15.0.nupkg
```

#### Verify the global packages folder

When NuGet restores a project, it keeps each package in the global packages
folder, `~/.nuget/packages` by default. Verify all of the packages in the
folder:

```sh
chainctl libraries verify ~/.nuget/packages
```

For each package, `chainctl` verifies the signature of the `.nupkg` that NuGet
keeps. It then makes sure that the package id and version match the directory.
Last, it compares the files that NuGet extracted beside the package with the
contents of the signed package. Your build reads the extracted files, not the
`.nupkg`. So a file that is missing, changed, or not in the package makes the
package not verified. A verified package reports `Fully verified by Chainguard
(package signature verified, and the extracted files match the package)`.

`chainctl` does not compare NuGet's own files, `.nupkg.metadata` and the
`.sha512` hash. A nuspec or IntelliSense XML file that the restore left out does
not count as missing. A package with no `.nupkg` kept, such as a package
restored from a fallback folder, is reported as unchecked.

The global packages folder holds every package that the machine restored, from
every source and for every project. To verify only what one project uses,
restore the project into an empty folder and verify that folder. The
`NUGET_PACKAGES` environment variable sets the global packages folder for one
restore:

```sh
NUGET_PACKAGES="$PWD/chainguard-verify" dotnet restore
chainctl libraries verify --detailed ./chainguard-verify
```

A folder that also holds files outside its package directories is checked as a
plain directory, so that every artifact in it is checked.

#### Verify a NuGet lockfile

If your project uses a NuGet lockfile, restore the project, then verify the
lockfile:

```sh
dotnet restore
chainctl libraries verify packages.lock.json
```

`chainctl` also accepts a per-project lockfile name, such as
`packages.MyApp.lock.json`. It reads every target framework and runtime section
of the lockfile and skips project references. The report counts the package
entries that the lockfile declares, and gives the number of entries that are
Chainguard packages.

`chainctl` reads the package of each entry from the global packages folder. It
uses the folder that `--packages-dir` names. If you do not set
`--packages-dir`, it uses `NUGET_PACKAGES`, or `~/.nuget/packages` if that
variable is not set. `chainctl` does not read a `globalPackagesFolder` from
`nuget.config`. If your configuration sets one, pass that folder with
`--packages-dir`.

An entry verifies in two steps. First, its package must verify as in a global
packages folder. Second, the package must match the entry's `contentHash`. The
`contentHash` is the SHA-512 digest of the package without its signature.
NuGet refuses to restore a package that does not match it, so the match ties
the entry to the package whose signature verified. A verified entry reports
`Fully verified by Chainguard (package signature verified, the lockfile's
contentHash matches, and the extracted files match the package)`.

An entry whose package is not in the folder is reported as unchecked, not as
not verified. To check those entries too, add `--fetch-missing`. `chainctl` then
fetches each missing package from the Chainguard feed and checks its signature,
its id and version, and the entry's `contentHash`. A fetched package has no
extracted files to compare, and its details say that it was fetched. With
`--fetch-missing`, you can verify a lockfile with no restore:

```sh
chainctl libraries verify --fetch-missing --parent <your-organization> packages.lock.json
```

An entry for a package that the feed does not serve reports `Not verified: the
Chainguard feed does not serve the package`. If the feed cannot answer for an
entry, the entry is reported as unchecked.

Like a `.nupkg`, a lockfile needs no token and no network access. The exception
is a run with `--fetch-missing` or `--output-attestations`. Both flags need a
token for an organization entitled to Chainguard Libraries for .NET. If the
registry rejects the credentials, `chainctl` fetches nothing more. It reports the
entries that it did not fetch as unchecked, and it prints the rejection after
the results.

#### Regenerate `packages.lock.json` after you move to Chainguard

If your project uses a NuGet lockfile, regenerate `packages.lock.json` when
the project starts to restore from Chainguard Libraries. A Chainguard build of a
package has a different content hash than the nuget.org package of the same
version. NuGet checks every package against the hash in the lockfile, with or
without `--locked-mode`. So a lockfile written against nuget.org makes the
restore stop with `NU1403` ("Package content hash validation failed").

To regenerate the lockfile, restore once against the Chainguard source with
`--force-evaluate`, or delete `packages.lock.json` and restore:

```sh
dotnet restore --force-evaluate
```

Then commit the new `packages.lock.json`. A lockfile written against nuget.org
also does not match the packages restored from Chainguard, so `chainctl
libraries verify` reports its entries as not verified.

#### Verify a published app or a container image

A published .NET app holds DLL files, not `.nupkg` files. Its deps file is
`<app>.deps.json`. For each NuGet package that the app uses, the deps file
names the version, the SHA-512 digest, and the files from the package that the
app holds. Verify the deps file, or the publish directory that holds it:

```sh
dotnet publish -o out
chainctl libraries verify out/MyApp.deps.json
```

The deps file alone is a claim, so `chainctl` compares the app's files with the
package. For a package to verify, all of the following conditions must be true:

- Its `.nupkg` carries a Chainguard package signature.
- The `.nupkg` matches the SHA-512 digest in the deps file.
- Every file that the deps file lists for the package is in the app, byte for
  byte as the package has it.

When the global packages folder holds that exact package, `chainctl` reads
the `.nupkg` from it. It finds the folder as for a lockfile. A package that is
not there is unchecked. To fetch it from the Chainguard feed, add
`--fetch-missing`.
Without `--fetch-missing`, a deps file needs no token.

The report gives the number of packages that are Chainguard packages. It counts
packages, not files. It lists the app's own assemblies, the .NET runtime, and
packages with no file in the app, but does not count them. A file that differs
from the package leaves the package not verified, with the details `Modified at
publish (ReadyToRun or trimming)`. A ReadyToRun or trimmed publish changes the
files, so verify an app that you publish without these options. A file that is
missing from the app leaves the package unchecked. Single-file apps, whose deps
file is inside the executable, are not supported.

To verify the .NET packages of an app in a container image, pass the image:

```sh
chainctl libraries verify --parent <your-organization> registry.example.com/my-app:latest
```

An image has no packages folder, so `chainctl` always fetches the packages from
the Chainguard feed, and the check needs a token. In an image, `chainctl` reads
each file from the top layer that holds it. A file that a later layer deletes
counts as missing. `chainctl` does not check the deps files of the .NET
installation itself, because they describe Microsoft's tools and frameworks,
not your app.

#### Download .NET SBOMs and attestations

Add `--output-attestations` to also check the SLSA provenance that the
Chainguard feed serves for each package, and to save the provenance and the SPDX
SBOM:

```sh
chainctl libraries verify Semver.3.0.0.nupkg --output-attestations
```

The provenance is a Sigstore bundle with a signed SLSA statement. `chainctl`
verifies the bundle and makes sure that the Chainguard .NET signing identity
signed it. It also makes sure that the statement names the SHA-256 digest of
the `.nupkg`. Either the package signature or the provenance verifies a package,
and the report records both.

The provenance check is not offline. It needs a token for an organization
entitled to Chainguard Libraries for .NET. It also needs network access to
`libraries.cgr.dev` and `tuf-repo-cdn.sigstore.dev`. For the roles, refer to
[Requirements](#requirements).

Files are saved under `--output-dir`, which defaults to `attestations`, in a
directory named `<id>/<version>/`, both in lowercase, as the feed names them.
For the preceding command, the directory is `attestations/semver/3.0.0/`. When
they are available, it holds these files:

- `semver.3.0.0.nupkg.provenance.sigstore.json`: The exact Sigstore bundle that
  `chainctl` verified, saved as trusted.
- `semver.3.0.0.nupkg.sbom.spdx.json`: The SPDX SBOM. The verified
  provenance names the SBOM with its SHA-256 digest. When the digest of the
  SBOM is equal to that digest, `chainctl` saves the SBOM as trusted. If the
  digests are different, `chainctl` does not save the SBOM and prints a note on
  stderr.

The JSON output lists each saved file in `downloadedAttestations`, with its
`kind`, `path`, `url`, and `trusted` fields.

Downloads also work for the packages of a global packages folder, a lockfile,
and a published app. `chainctl` saves files only for a package that is fully
verified. In a global packages folder, that includes its extracted files.

The provenance step can fail for a package whose signature verified. The
package then stays verified, but `chainctl` saves no files for it:

- If the feed serves no provenance for the package, `chainctl` prints a warning
  on stderr. A package that came from nuget.org through upstream fallback has no
  provenance.
- If the registry rejects your credentials, `chainctl` prints the report and
  then the rejection on stderr. The exit status does not change.

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
compare](/chainguard/libraries/java/overview/#manual-access), if desired.

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

- [Chainguard Libraries overview](/chainguard/libraries/introduction/overview/)
- [Chainguard Libraries authentication](/chainguard/libraries/introduction/access/)
- [`chainctl libraries verify` reference documentation](/platform/chainctl/chainctl-docs/chainctl_libraries_verify/)
- [{{<icon "play-circle-fill">}} Learning Lab: Chainguard Libraries for Java](/software-security/learning-labs/ll202505/)
- [{{<icon "play-circle-fill">}} Learning Lab: Chainguard Libraries for Python](/software-security/learning-labs/ll202506/)
