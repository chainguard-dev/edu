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

Chainguard Libraries for Python provides enhanced security for the vast Python ecosystem by rebuilding PyPI packages with comprehensive supply chain protection and automated patching. With over 600,000 packages on the [Python Package Index (PyPI)](https://pypi.org/) serving application development, machine learning, and data science needs, Chainguard addresses the critical security challenges of depending on packages from untrusted sources by rebuilding them within the controlled Chainguard Factory environment. In addition, Chainguard eliminates security risk by remediating High and Critical vulnerabilities across older package versions where upstream maintainers are not able to prioritize fixes.

Chainguard Libraries for Python enables access to a growing collection of Python
packages rebuilt from source. New releases of common libraries or artifacts
requested by customers are added to the index by an automated system. Any
request for a library or library version missing in Chainguard Libraries
automatically triggers a process to provision the artifacts from relevant
sources if available. In combination with third-party software repository
managers, you can use Chainguard Libraries for Python as a secure source of
truth for your development process.

## Runtime requirements

The runtime requirements for Python artifacts available from Chainguard
Libraries for Python are identical to the requirements of the original upstream
project. For example, if a Python wheel retrieved from PyPI requires Python 3.10
or higher, the same Python 3.10 runtime requirement applies to the binary
artifact from Chainguard Libraries for Python.

Some Python libraries include Python extensions that depend on native
binaries supplied by the operating system or included in the
distribution archive. For these libraries the following requirements
apply:

* All Linux distributions must use glibc 2.28 or higher, such as RHEL 8, Ubuntu
  20.04, or Amazon Linux 2023.
* On Windows and MacOS you must use a suitable Linux distribution with a
  container solution, such as WSL2, apple/container or Docker Desktop. 
* Processor architecture of the runtime environment must be `x86_64` or
  `aarch64`.

## CVE Remediation

Chaingard Libraries for Python includes includes [CVE Remediation](/chainguard/libraries/cve-remediation.md). This provides access to remediated library versions with High and Critical CVE fixes, particularly when upstream maintainers are not able to backport fixes to older versions. Python libraries with CVE remediation include a local version identifier of `+cgr.N`. For example, the `flask` library has CVE-2023-30861 remediated in versions `1.1.2+cgr.1` and `2.0.0+cgr.1`.

In some cases, multiple CVEs may be remediated in the same library version across separate local version bumps. For example, `aiohttp` has both CVE-2024-23334 and CVE-2024-30251 remediated in the version `3.9.1+cgr.2`. Python package management tools interpret the `+cgr.N` suffix as a local version, which takes precedence over versions without the version suffix during dependency resolution.

## Technical details

Most organizations consume Chainguard Libraries for Python through a repository
manager such as Cloudsmith, JFrog Artifactory or Sonatype Nexus Repository. For
full details, refer to our [Global Configuration
documentation](/chainguard/libraries/python/global-configuration/). The rest of
this article provides details of the underlying implementation of Chainguard
Libraries for Python and how to access individual libraries manually.

The Chainguard Libraries for Python indexes use the PyPI repository format and 
only include release artifacts of the libraries built by Chainguard from source.

The URLs for the repositories are:

```
https://libraries.cgr.dev/python/
https://libraries.cgr.dev/python-remediated/
```

The first index provides all Python libraries that we build from source, without remediated versions. The second index provides remediated libraries with High and Critical CVE fixes applied to older versions.

Use the URLs with your [username and password retrieved with
chainctl](/chainguard/libraries/access/) to access the Chainguard Libraries for
Python repository manually with a browser.

After successful login, you are redirected to the `simple` sub-context at
`https://libraries.cgr.dev/python/simple/` or `https://libraries.cgr.dev/python-remediated/simple/` 
that allows you to inspect the available packages. The top level contains 
an alphabetical list of packages:

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

The Chainguard Libraries for Python repository does not include all packages
from PyPI. Chainguard Libraries for Python are rebuilt from source and require
that source be available. Therefore, packages that do not provide a valid source
URL cannot be rebuilt within the Chainguard Factory.

Since the Chainguard Libraries for Python index is not complete, you should
strongly consider setting the PyPI public package index as a fallback within
your repository manager. In this case, failed requests are logged by Chainguard
and, where possible, the package is prioritized for new build from source.
Typically, access is [configured globally on a repository manager for your
organization](/chainguard/libraries/python/global-configuration/).

Alternatively, you can use the token for direct access to the Chainguard
Libraries for Python index as discussed in [Build
configuration](/chainguard/libraries/python/build-configuration/).
