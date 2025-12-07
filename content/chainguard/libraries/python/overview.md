---
title: "Chainguard Libraries for Python Overview"
linktitle: "Python Overview "
description: "Learn about Chainguard Libraries for Python, providing enhanced security for PyPI packages through automated vulnerability patching and supply chain protection"
type: "article"
date: 2025-04-09:04:00+00:00
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

## Technical Details

Most organizations consume Chainguard Libraries for Python through a repository
manager such as Cloudsmith, JFrog Artifactory, or Sonatype Nexus Repository. For
full details, refer to our [Global Configuration
documentation](/chainguard/libraries/python/global-configuration/). The rest of
this article provides details of the underlying implementation of Chainguard
Libraries for Python and how to access individual libraries manually.

The Chainguard Libraries for Python indexes use the PyPI repository format and
only include release artifacts of the libraries built by Chainguard from source.

The URLs for the repositories include:

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
GPU-accelerated Python wheels. See more details in the [CUDA Enabled 
Libraries](#cuda-enabled-libraries) section.

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

## CVE Remediation

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

## CUDA Enabled Libraries
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
https://libraries.cgr.dev/cu130/simple/
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

## Runtime and Build Requirements

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

### Behavior on Windows and MacOS

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
package from PyPI, since it is not available from Chainguard. Any build on Linux,,
however, uses suitable a package from Chainguard Libraries. When using CVE remediation,
this also means that remediated packages with native binaries are only used on
Linux.


<a id="manual"></a>

## Manual Access

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

## SBOM and attestation files

Chainguard Libraries for Python include files that contain software bill of
material (SBOM) information. Additional files attest details about build
infrastructure with  the [Supply-chain Levels for Software Artifacts
(SLSA)](https://slsa.dev/) provenance information.

The related files for Chainguard Libraries for Python are located within the
Python wheel file for each package following the [PEP 770 Improving
measurability of Python packages with Software Bill-of-Materials
specification](https://peps.python.org/pep-0770/) for software composition
analytis (SCA) using the SPDX format.

Specifically a wheel file contains two directories, the main code directory that
uses the name of the library only, and the version-specific distribution info
directory `.dist.info`. For example, the wheel archive for Flask version 2.0.0
includes a directory `flask-2.0.0.dist.info`. You can also find this directory
in the `site-packages` directory of a Python project using a virtual environment.

Find the SBOM information in the file `sboms/sbom.spdx.json`. Any package from
Chainguard includes the reference to Chainguard in the creators section:

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

A [Sigstore bundle file](https://docs.sigstore.dev/about/bundle/) is available
as `bundle.json` from the integrity context at
`https://libraries.cgr.dev/python/integrity/PACKAGE/VERSION/FILE/bundle.json`
specifically for each package, version, and file. 
