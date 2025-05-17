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

## Technical details

Most organizations consume Chainguard Libraries for Python through a repository
manager such as Cloudsmith, JFrog Artifactory or Sonatype Nexus Repository. For
full details, refer to our [Global Configuration
documentation](/chainguard/libraries/python/global-configuration). The rest of
this article provides details of the underlying implementation of Chainguard
Libraries for Python and how to access individual libraries manually.

The Chainguard Libraries for Python index uses the PyPI repository format and only includes release artifacts of the libraries built by Chainguard from source. 

A [username and password retrieved with
chainctl](/chainguard/libraries/access/) are required to access the Chainguard
Libraries for Python repository. The URL for the repository is:

```
https://libraries.cgr.dev/python/
```

Following PyPI URL conventions, a browsable directory structure can be viewed at:

```
https://libraries.cgr.dev/python/simple/
```

Specific packages can be accessed by package name and version:

```
https://libraries.cgr.dev/files/flask/flask-1.1.3.tar.gz
```

Use the search functionality on [pypi.org](https://pypi.org/) to locate packages of interest.

If you use the URL directly in a browser, you are prompted to provide the username and password created using `chainctl` via basic auth.

You can also use `curl` and specify the [username and password retrieved using chainctl](/chainguard/libraries/access/) for basic user authentication:

```
curl --user "exampleusername:examplepassword" \
  -O https://libraries.cgr.dev/files/flask/flask-1.1.3.tar.gz
```

The Chainguard Libraries for Python repository does not include all packages from PyPI. Chainguard Libraries for Python are rebuilt from source and require that source be available. Therefore, packages that do not provide a valid source URL cannot be rebuilt within the Chainguard Factory. In addition, initial package rebuild coverage for Chainguard Libraries for Python is not comprehensive. 

Since the Chainguard Libraries for Python index is not comprehensive, you should strongly consider setting the PyPI public package index as a fallback within your repository manager. In this case, failed requests are logged by Chainguard and, where possible, the package is prioritized for new build from source. Typically, access is [configured globally on a repository manager for your organization](/chainguard/libraries/python/global-configuration/).

Alternatively, you can use the token for direct access to the Chainguard Libraries for Python index as discussed in [Build configuration](/chainguard/libraries/python/build-configuration/).
