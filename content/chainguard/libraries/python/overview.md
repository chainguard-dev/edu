---
title: "Chainguard Libraries for Python overview"
linktitle: "Python overview"
description: "Learn about Chainguard Libraries for Python, providing enhanced security for PyPI packages through automated vulnerability patching and supply chain protection"
type: "article"
date: 2025-04-09T04:00:00+00:00
lastmod: 2025-07-23T15:09:59+00:00
draft: false
tags: ["Chainguard Libraries", "Python", "Overview"]
menu:
  docs:
    parent: "python"
weight: 010
toc: true
---

## Introduction

Chainguard Libraries for Python provides enhanced security for the vast Python
ecosystem by rebuilding PyPI packages with comprehensive supply chain protection
and automated patching. With over 600,000 packages on the [Python Package Index
(PyPI)](https://pypi.org/) serving application development, machine learning,
and data science needs, Chainguard addresses the critical security challenges of
depending on packages from untrusted sources by rebuilding them within the
controlled Chainguard Factory environment. In addition, Chainguard eliminates
security risk by remediating High and Critical vulnerabilities across older
package versions where upstream maintainers are not able to prioritize fixes.

Chainguard Libraries for Python enables access to a growing collection of Python
packages rebuilt from source. New releases of common libraries or artifacts
requested by customers are added to the index by an automated system. Any
request for a library or library version missing in Chainguard Libraries
automatically triggers a process to provision the artifacts from relevant
sources if available. In combination with third-party software repository
managers, you can use Chainguard Libraries for Python as a secure source of
truth for your development process. 

## Technical details

Most organizations consume Chainguard Libraries for Python through a repository
manager such as Cloudsmith, JFrog Artifactory, or Sonatype Nexus Repository. For
full details, refer to our [Global Configuration
documentation](/chainguard/libraries/python/global-configuration/). The rest of
this article provides details of the underlying implementation of Chainguard
Libraries for Python and how to access individual libraries manually.

The Chainguard Libraries for Python indexes use the PyPI repository format and
only include release artifacts of the libraries built by Chainguard from source.

URLs for the repositories:

```
https://libraries.cgr.dev/python/
https://libraries.cgr.dev/python-remediated/
https://libraries.cgr.dev/cu[**version**]/simple/
```

The first index provides all Python libraries that Chainguard builds from
source, without remediated versions. The second index provides remediated
libraries with high and critical CVE fixes applied to older versions. The
separate indexes provide you the option to make remediated versions available
for your development or to opt out of using these versions completely and
continue to use non-remediated versions only. The third index refers to 
CUDA version-specific indexes which include libraries with 
GPU-accelerated Python wheels. You can find more details in the [CUDA 
Enabled Libraries](#cuda-enabled-libraries) section.

The Chainguard Libraries for Python repository does not include all packages
from PyPI. Chainguard Libraries for Python are rebuilt from source and require
that source be available. Therefore, packages that do not provide a valid source
URL cannot be rebuilt within the Chainguard Factory.

Since the Chainguard Libraries for Python index is not complete, you should
strongly consider setting the PyPI public package index as a fallback within
your repository manager. In this case, failed requests are logged by Chainguard
and, where possible, the package is prioritized for a new build from source.
Typically, access is [configured globally on a repository manager for your
organization](/chainguard/libraries/python/global-configuration/).

Alternatively, you can use the token for direct access to the Chainguard
Libraries for Python index as discussed in [Build
configuration](/chainguard/libraries/python/build-configuration/).

Follow the steps detailed in [Manual Access](#manual) to browse the Python index
and find available packages, package versions, source distribution (sdist), and
Python wheel files for standard and remediated package version.

<a id="cve-remediation"></a>

## CVE remediation

Chainguard Libraries for Python includes the [CVE
Remediation](/chainguard/libraries/cve-remediation/) feature. Remediated
libraries include an appended local version identifier of `+cgr.N`. Python
package management tools interpret the `+cgr.N` suffix as a local version that
takes precedence over versions without the version suffix during dependency
resolution.

For example, the `flask` library has a fix for CVE-2023-30861 available in the
upstream codebase. Upon customer request for a specific version, the fix is
backported to the flask versions `1.1.2` and `2.0.0` and made available in new
versions `1.1.2+cgr.1` and `2.0.0+cgr.1`. Python package management tools
consider these local versions, such as `1.1.2+cgr.1` and `2.0.0+cgr.1`, as
newer, compatible replacements automatically.

In some cases, multiple CVEs may be remediated in a specific library version.
For example, `aiohttp` has fixes for both CVE-2024-23334 and CVE-2024-30251 in
the version `3.9.1+cgr.2`.

## CUDA-enabled libraries

Chainguard Libraries for Python includes libraries optimized for specific CUDA 
versions. These libraries are GPU‑accelerated Python wheels that are built 
and tested against specific NVIDIA CUDA versions. An example is `torch` built 
for CUDA 12.8, available via the `https://libraries.cgr.dev/cu128/simple/` index. 
These libraries are published to CUDA‑specific indexes to ensure your Python build 
tools resolve the correct wheel versions, mirroring how other CUDA-optimized 
ecosystems are commonly distributed.

Chainguard Libraries for Python includes the following repositories for 
GPU‑accelerated libraries, built for specific CUDA versions:

```
https://libraries.cgr.dev/cu126/simple/
https://libraries.cgr.dev/cu128/simple/
https://libraries.cgr.dev/cu129/simple/
```

Many Python package managers and repository managers support configuring 
multiple package indexes. You can generally treat Chainguard’s CUDA indexes 
the same way you use other CUDA-specific indexes (for example, the PyTorch 
CUDA wheels at https://download.pytorch.org/whl/cu128).

If you use a repository manager as described in the [Global Configuration
documentation](/chainguard/libraries/python/global-configuration/), configure 
a remote repository that points at the appropriate Chainguard CUDA index, and 
use it in place of any CUDA-specific index you previously proxied.

If you choose to pull directly without an artifact manager, you can similarly 
replace the CUDA index you previously used with the corresponding 
Chainguard CUDA index, with your existing package management tools like 
`pip`, `uv`, or `poetry`. 

Note that the CUDA-enabled libraries in these repositories are not dependency 
complete, since they do not include packages from the NVIDIA CUDA toolkit. You 
must configure your package manager to pull NVIDIA components from an 
upstream source such as NVIDIA's index at https://pypi.nvidia.com, or from PyPI 
where NVIDIA publishes them directly.

## Python version support

When a Python version reaches [end of life (EOL) upstream](https://devguide.python.org/versions/), Chainguard Libraries continues to build packages and provide security fixes for that version for six months beyond the upstream EOL date.

After that six-month window closes, Chainguard Libraries will:
- No longer build new packages that require the EOL Python version
- No longer provide security fixes for packages built against the EOL Python version
- Continue to serve previously built packages, but these will not receive updates

### Python 3.9 EOL

Python 3.9 reached upstream EOL on October 31, 2025. Chainguard Libraries' extended support window for Python 3.9 ends on May 15, 2026. After this date, no new Python 3.9 packages will be built, and existing Python 3.9 packages will no longer receive security updates.

To continue receiving up-to-date, secure packages from Chainguard Libraries, we strongly recommend migrating to a supported Python version. Currently supported versions are Python 3.10 and later.


## Runtime and build requirements

The runtime requirements for Python artifacts available from Chainguard
Libraries for Python are identical to the requirements of the original upstream
project. For example, if a Python wheel retrieved from PyPI requires Python 3.10
or higher, the same Python 3.10 runtime requirement applies to the binary
artifact from Chainguard Libraries for Python.

Chainguard distributes all packages as Python wheels, following the [Python
binary distribution
format](https://packaging.python.org/en/latest/specifications/binary-distribution-format/)
and are typically accompanied by a source distribution tarball. For example, for
the package `flask` version `3.1.2` the files are the
`flask-3.1.2-py3-none-any.whl` wheel and the `flask-3.1.2.tar.gz` source
distribution tarball. Note that the wheel filename includes the indication
`none-any` that signals the platform independence of the wheel.

Some Python libraries include Python extensions that depend on native binaries
supplied by the operating system or included in the distribution archive. The
following list displays all available files for the `pyyaml` package version
`6.0.3`. This list includes numerous wheel files for different environments and
the source distribution tarball:

```
pyyaml-6.0.3-cp310-cp310-manylinux_2_28_aarch64.whl
pyyaml-6.0.3-cp310-cp310-manylinux_2_28_x86_64.whl
pyyaml-6.0.3-cp310-cp310-manylinux_2_39_aarch64.whl
pyyaml-6.0.3-cp310-cp310-manylinux_2_39_x86_64.whl
pyyaml-6.0.3-cp311-cp311-manylinux_2_28_aarch64.whl
pyyaml-6.0.3-cp311-cp311-manylinux_2_28_x86_64.whl
pyyaml-6.0.3-cp311-cp311-manylinux_2_39_aarch64.whl
pyyaml-6.0.3-cp311-cp311-manylinux_2_39_x86_64.whl
pyyaml-6.0.3-cp312-cp312-manylinux_2_28_aarch64.whl
pyyaml-6.0.3-cp312-cp312-manylinux_2_28_x86_64.whl
pyyaml-6.0.3-cp312-cp312-manylinux_2_39_aarch64.whl
pyyaml-6.0.3-cp312-cp312-manylinux_2_39_x86_64.whl
pyyaml-6.0.3-cp313-cp313-manylinux_2_28_aarch64.whl
pyyaml-6.0.3-cp313-cp313-manylinux_2_28_x86_64.whl
pyyaml-6.0.3-cp313-cp313-manylinux_2_39_aarch64.whl
pyyaml-6.0.3-cp313-cp313-manylinux_2_39_x86_64.whl
pyyaml-6.0.3-cp39-cp39-manylinux_2_28_aarch64.whl
pyyaml-6.0.3-cp39-cp39-manylinux_2_28_x86_64.whl
pyyaml-6.0.3-cp39-cp39-manylinux_2_39_aarch64.whl
pyyaml-6.0.3-cp39-cp39-manylinux_2_39_x86_64.whl
pyyaml-6.0.3.tar.gz
```

The different file names use the following qualifiers to allow the build and
packaging tool to download the correct wheel file:

* The values `cp*` indicate CPython compatibility.
* The first value `cp*` value such as `cp39`, `cp310`, and others, indicates the
  compatibility with Python version `3.9`, `3.10`, and others.
* The second value `cp*` value such as `cp39`, `cp310`, and others, indicates
  the compatibility with the Python Application Binary Interface (ABI) version
  `3.9`, `3.10`, and others.
* The `manylinux` value indicates that the wheel is suitable for any modern
  Linux distribution, since no distribution specific requirements are in place.
* The `2_28` and `2_39` values indicate suitability for environments using
  `glibc 2.28` and higher or `glibc 2.39` and higher.
* The `aarch64` and `x86_64` values indicated the processor architecture
  requirement for ARM or x86.

As a result of the provided files for these libraries, the following
requirements apply:

* All Linux distributions must use `glibc 2.28` or higher, such as RHEL 8, Ubuntu
  20.04, or Amazon Linux 2023.
* On Windows and MacOS you must use a suitable Linux distribution with a
  container solution, such as
  [WSL2](https://learn.microsoft.com/en-us/windows/wsl/),
  [apple/container](https://apple.github.io/container/documentation/) or [Docker
  Desktop](https://docs.docker.com/desktop/).
* The runtime environment's processor architecture must be `x86_64` or
  `aarch64`.

### Behavior on Windows and macOS

As a result of the requirements detailed in the preceding section, the developer
experience on Windows and MacOS platforms is impacted. Chainguard only provides
packages including native binaries for Linux platforms. These are not suitable
for use on Windows or MacOS.

When using Chainguard Libraries for Python on these platforms, retrieval for
these libraries, and therefore application builds, fail. The suggested
deployment, detailed in [Technical Details](#technical-details) and [Global
Configuration](/chainguard/libraries/python/global-configuration/), involves a
repository manager that uses PyPI as a fall back for such packages. With this
configuration, any build on Windows or MacOS continues to work and pulls the
package from PyPI, since it is not available from Chainguard. Any build on Linux,
however, uses a suitable package from Chainguard Libraries. When using CVE remediation,
this also means that remediated packages with native binaries are only used on
Linux.


<a id="manual"></a>

## Manual access

Use the URLs with your [username and password retrieved with
chainctl](/chainguard/libraries/access/) to access the Chainguard Libraries for
Python repository manually with a browser.

After successful login, you are redirected to the `simple` sub-context at
`https://libraries.cgr.dev/python/simple/` or
`https://libraries.cgr.dev/python-remediated/simple/` that allow you to inspect
the available packages. The top level contains an alphabetical list of packages:

```
2captcha-python
3d-converter
absql
ahrs
amqpstorm
annogesic
apiflask
apscheduler
...
```

A list of all wheels and tarballs for the versions of a specific package is
available in the context of the package. For example, the `apiflask` context at
`https://libraries.cgr.dev/python/simple/apiflask/` shows the following list:

```
Links for apiflask
apiflask-0.1.0-py3-none-any.whl
apiflask-0.1.0.tar.gz
apiflask-0.10.0-py3-none-any.whl
apiflask-0.10.0.tar.gz
apiflask-0.10.1-py3-none-any.whl
apiflask-0.10.1.tar.gz
apiflask-0.11.0-py3-none-any.whl
apiflask-0.11.0.tar.gz
apiflask-0.12.0-py3-none-any.whl
apiflask-0.12.0.tar.gz
...
```

Each package name is a link to the specific binary. The link includes long
unique identifiers and cannot be determined without browsing. The list uses
ascending order for the full name including the version.

Use the search functionality on [pypi.org](https://pypi.org/) to locate packages
of interest and then browse in the simple index to determine available versions
in Chainguard Libraries for Python.

Use `curl`, specifying the username and password retrieved with
[chainctl](/chainguard/libraries/access/), and use the URL of the file
to download and save the file with the original name:

With [.netrc authentication](/chainguard/libraries/access/#netrc):

```shell
curl -n -L -O https://libraries.cgr.dev/files/...
```

With [environment variables](/chainguard/libraries/access/#env):

```shell
curl -L --user "$CHAINGUARD_PYTHON_IDENTITY_ID:$CHAINGUARD_PYTHON_TOKEN" \
  -O https://libraries.cgr.dev/files/...
```

The option `-L` is required to follow redirects for the actual file locations.

## Hash verification when migrating to Chainguard Libraries

Because Chainguard rebuilds Python packages from source rather than mirroring upstream PyPI artifacts, it is expected that checksums for Chainguard-built packages differ from their PyPI counterparts, even for identical package versions. This affects any tool that pins or verifies hashes:

- Tools such as `pip` verify that downloaded files match the hashes specified in requirements.txt when using `--require-hashes` or when hashes are pinned
- Tools such as `pip`, `Poetry`, and `uv` generate lock files that include SHA-256 hashes
- Repository managers such as JFrog Artifactory or Sonatype Nexus may have cached upstream PyPI wheels and continue serving them instead of Chainguard versions, even after you have reconfigured to use Chainguard Libraries

Resolving these issues requires two steps: [clearing cached artifacts](#clearing-caches-before-migration) at every layer of your build pipeline, and [updating lock files or requirements files](#updating-lockfile-hashes) so they reflect Chainguard's checksums.

### Clearing caches before migration

Most build systems treat language libraries as immutable artifacts. If a dependency already exists in a cache, the build will reuse the cached copy instead of fetching it again, even after you have reconfigured to use Chainguard. Before migrating, it is critical to start with a clean dependency cache at every layer of your build pipeline. Failing to do so can result in builds silently continuing to use PyPI-sourced artifacts after migration.

Cached packages can exist at multiple layers:

**Local developer machines**

Common cache locations for Python tools include `~/.cache/pip/`, `~/.cache/uv/`, and `~/.cache/pypoetry/`. 

Clear the cache for your tool:

```bash
pip cache purge
uv cache clean
poetry cache clear --all pypi
```

**CI/CD pipeline caches**

Build pipelines frequently cache downloaded packages between runs. These caches must be invalidated after switching to Chainguard. Common locations to check:

* GitHub Actions: Packages cached under `/home/runner/.cache/pip` or restored via `actions/cache`. Update the cache key in your `actions/cache` step to force a cache miss after switching to Chainguard.
* GitLab CI: Check for .`cache/pip` defined in the job's cache section and update the cache key or clear the directory.
* Jenkins: Agents may reuse workspaces or home directories such as `/var/lib/jenkins/.cache/pip`. Ensure cache directories are cleared as part of your build setup step.

**Containerized builds**

Cached Docker image layers may reuse upstream dependencies even after reconfiguration. If a Dockerfile contains a layer such as `RUN pip install -r requirements.txt`, Docker will reuse the cached layer unless the base image, the requirements file, or the command itself has changed. To force a fresh install from Chainguard, rebuild without the layer cache:

```bash
docker build --no-cache
```

### Updating lockfile hashes

> Note: `chainctl libraries update-hashes` does not currently support authentication through a repository manager. You will need to [configure direct access](/chainguard/libraries/python/build-configuration/#direct-access) credentials before running the command, or [update the lockfiles manually](#update-lockfiles-manually).

The `chainctl libraries update-hashes` command automates lockfile hash updates for all supported Python lockfile formats. Rather than manually regenerating lock files with each tool, you can run the command directly against your existing lockfile to update hashes to Chainguard checksums while preserving your locked dependency versions, without re-resolving your dependency graph.

Supported formats include `requirements.txt` (pip-tools `--hash` style), `poetry.lock`, `uv.lock`, `pdm.lock`, `Pipfile.lock`, and `pylock.toml`.

Run the command in your project directory to auto-detect the lockfile:

```bash
chainctl libraries update-hashes
```

Or specify a lockfile path directly:

```bash
chainctl libraries update-hashes path/to/requirements.txt
```

By default, Chainguard hashes are appended alongside existing upstream hashes. After updating the lockfiles, to switch your environment to use Chainguard packages, configure your tool to use the Chainguard index and reinstall. The `chainctl libraries update-hashes` command will output
a "Next steps" section that includes the tool-specific command for reinstalling. 

#### Update lockfiles manually

If you are using a repository manager, and do not want to use direct access temporarily while updating lockfiles, you can use the following instructions to update your lockfiles: 

{{< details "Manually updating lockfiles" >}}

Before regenerating lock files, ensure your tool is configured to use Chainguard as the package index by following the [global configuration](/chainguard/libraries/python/global-configuration/) or [direct access](/chainguard/libraries/python/build-configuration/#direct-access) documentation.

To update your lock files and requirements with Chainguard's checksums:

**pip with `--require-hashes`:** 

If your `requirements.txt` was generated using PyPI hashes, installation will
fail with a hash mismatch after switching to Chainguard. Once pip is configured
to use Chainguard as the index, regenerate your requirements file to update the
hashes:
```bash
  pip-compile --generate-hashes requirements.in -o requirements.txt
```

Note that `pip-compile` embeds your Chainguard index URL, including credentials, as an `--index-url` line in the generated file. Avoid committing this file to source control, or strip the `--index-url` line before doing so.

**uv:**

When the configured index changes, `uv sync` automatically re-resolves dependencies and updates `uv.lock` with hashes from the new index. No explicit `uv lock` step is required; running `uv sync` after configuring Chainguard as your index is sufficient. However, running `uv lock` explicitly after switching indexes is recommended to ensure your lock file accurately reflects what is being installed before you run `uv sync`.

Note that `uv sync --frozen` bypasses index configuration entirely and downloads packages using the URLs embedded directly in `uv.lock`. If your lock file was generated against PyPI, `uv sync --frozen` will continue to download from PyPI regardless of your configured index. Run `uv lock` first to update the lock file before using `--frozen`.

The credentials from your Chainguard pull token must be embedded in the index URL with the `/` in the username percent-encoded as `%2F`. For example, in `uv.toml`:

```
[[index]]
url = "https://<PULLTOKEN_USERNAME_PART1>%2F<PULLTOKEN_USERNAME_PART2>:<PULLTOKEN_PASSWORD>@libraries.cgr.dev/python/simple/"
authenticate = "always"
```
  
**Poetry:**

When the configured source changes, Poetry detects that `pyproject.toml` has changed significantly and refuses to install until the lock file is regenerated. Regenerate your lock file to update the hashes:

Poetry 1.x:

```bash
  poetry lock --no-update
```

Poetry 2.x: 

```bash
  poetry lock
```

**Repository managers:** 

Repository managers such as JFrog Artifactory or Sonatype Nexus may continue serving cached PyPI artifacts even after the upstream index is changed. Clear the cache or invalidate the artifact to ensure the Chainguard-built package is fetched. 

Before regenerating lock files, ensure your tool is configured to use Chainguard as the package index by following the [global configuration](/chainguard/libraries/python/global-configuration/) or [direct access](/chainguard/libraries/python/build-configuration/#direct-access) documentation.

{{< /details >}}

>**Note:** While hash mismatches are expected for some tooling and
configurations while migrating to Chainguard, you can verify the authenticity and provenance of Chainguard
packages using SBOM and SLSA attestation files as described in the next section.

## SBOM and attestation files

Chainguard Libraries for Python include files that contain software bill of
material (SBOM) information. Additional files attest details about build
infrastructure with  the [Supply-chain Levels for Software Artifacts
(SLSA)](https://slsa.dev/) provenance information.

### Embedded SBOMs

The related files for Chainguard Libraries for Python are located within the
Python wheel file for each package following the [PEP 770 Improving
measurability of Python packages with Software Bill-of-Materials
specification](https://peps.python.org/pep-0770/) for software composition
analytis (SCA) using the SPDX format.

A wheel file contains two directories:
- The main code directory that uses the name of the library only, and 
- The version-specific distribution info directory `.dist.info`.

For example, the wheel archive for Flask version 2.0.0
includes a directory `flask-2.0.0.dist.info`. You can also find this directory
in the `site-packages` directory of a Python project using a virtual environment.

The SBOM information is in the file `*.dist-info/sboms/sbom.spdx.json`. Any package from
Chainguard includes a reference to Chainguard in the `creators` section:

```json
{
  "spdxVersion": "SPDX-2.3",
  "dataLicense": "CC0-1.0",
  "SPDXID": "SPDXRef-DOCUMENT",
  "name": "flask",
  "documentNamespace": "https://anchore.com/syft/dir/flask-17f2a052-031c...",
  "creationInfo": {
    "licenseListVersion": "3.27",
    "creators": [
      "Tool: Syft",
      "Tool: ecosystems-wheels-rebuilder",
      "Organization: Chainguard, Inc"
    ],
  ...
  }
}
```

### SLSA provenance

SLSA provenance is available from the Chainguard Python index following the [PEP
740 – Index support for digital attestations
specification](https://peps.python.org/pep-0740/) within the integrity context
at `https://libraries.cgr.dev/python/integrity/PACKAGE/VERSION/FILE/provenance`
with `PACKAGE` as the Python package name, `VERSION` the package version, and
`FILE` the filename of the package archive with configured [basic authentication
using a pull token](/chainguard/libraries/access/).

For example, for version `2.0.0` of the package `flask` available as a platform
independent wheel archive file `flask-2.0.0-py3-none-any.whl` you can retrieve
the provenance information from
`https://libraries.cgr.dev/python/integrity/flask/2.0.0/flask-2.0.0-py3-none-any.whl/provenance`.

Packages from Chainguard are identified by the `publisher`:`environment` set as
`chainguard`:

```json
{
  "attestation_bundles": [
    {
      "attestations": [
        ...
      ]
      "publisher": {
        "environment": "chainguard",
        "kind": "URL",
        "issuer": "https://issuer.enforce.dev",
        "identity": "https://issuer.enforce.dev/3fab4fe4edb624d...",
        "repository": "chainguard-dev/ecosystems-wheel-rebuilder",
        "workflow": "python-build-versions.yaml"
      }
    }
  ],
  "version": 1
}
```

### Sigstore bundle

A [Sigstore bundle](https://docs.sigstore.dev/about/bundle/) is a self‑contained JSON file that packages everything needed
to verify the authenticity and integrity of a signed artifact.

A Sigstore bundle file is available
as `bundle.json` from the integrity context at
`https://libraries.cgr.dev/python/integrity/PACKAGE/VERSION/FILE/bundle.json`
specifically for each package, version, and file. 


