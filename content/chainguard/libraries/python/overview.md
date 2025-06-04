---
title: "Chainguard Libraries for Python Overview"
linktitle: "Python Overview "
description: "Python libraries for your application development"
type: "article"
date: 2025-04-09:04:00+00:00
lastmod: 2025-05-14:16:00+00:00
draft: false
tags: ["Chainguard Libraries", "Python", "Overview"]
menu:
  docs:
    parent: "python"
weight: 010
toc: true
---

## Introduction

Python is one of the most popular programming languages in the world. The
open [Python Package Index (PyPI)](https://pypi.org/) contains over 600,000
libraries for application development, machine learning, data science, and many
other use cases. Chainguard Libraries for Python rebuilds these powerful open
source projects within the Chainguard Factory, enabling access to the Python
ecosystem while dramatically reducing risk from an untrusted software supply
chain.

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

Some Python libraries depend on native binaries supplied by the operating system
or included in the distribution archive. For these libraries the following
requirements apply:

* Only Linux operating system supported, no Windows or MacOS versions.
* Linux distributions based on glibc 2.39 or higher, including Chainguard
  Containers based on Chainguard OS/Wolfi.
* Processor architectures `x86_64` and `aarch64` only.

## Technical details

Most organizations consume Chainguard Libraries for Python through a repository
manager such as Cloudsmith, JFrog Artifactory or Sonatype Nexus Repository. For
full details, refer to our [Global Configuration
documentation](/chainguard/libraries/python/global-configuration). The rest of
this article provides details of the underlying implementation of Chainguard
Libraries for Python and how to access individual libraries manually.

The Chainguard Libraries for Python index uses the PyPI repository format and
only includes release artifacts of the libraries built by Chainguard from
source.

The URL for the repository is:

```
https://libraries.cgr.dev/python/
```

Use the URL with your [username and password retrieved with
chainctl](/chainguard/libraries/access/) to access the Chainguard Libraries for
Python repository manually with a browser.

After successful login, you are redirected to the `simple` sub-context at
`https://libraries.cgr.dev/python/simple/` that allows you to inspect the
available packages. The top level contains an alphabetical list of packages:

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

Each package name is a link with to the specific binary. The link includes long
unique identifiers and cannot be determined without browsing. The list uses
ascending order for the full name including the version.

Use the search functionality on [pypi.org](https://pypi.org/) to locate packages
of interest and then browse in the simple index to determine available versions
in Chainguard Libraries for Python.

You can also use `curl` and specify the [username and password retrieved using
chainctl](/chainguard/libraries/access/) for basic user authentication after
browsing for the correct URL.

```
curl --user "exampleusername:examplepassword" \
  -O https://libraries.cgr.dev/files/...
```

Curl also supports using [.netrc for
authentication](/chainguard/libraries/access#netrc).

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
