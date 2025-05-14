---
title: "Chainguard Libraries for Python Overview"
linktitle: "Python Overview "
description: "Python libraries for your application development"
type: "article"
date: 2025-04-09:04:00+00:00
lastmod: 2025-14-05:04:00+00:00
draft: false
tags: ["Chainguard Libraries", "Python", "Overview"]
menu:
  docs:
    parent: "python"
weight: 010
toc: true
---

## Introduction

Python is one of the most popular programming languages in the world and the open [Python Package Index (PyPI)](https://pypi.org/) contains over 600,000 libraries for application development, machine learning, data science, and many other use cases. Chainguard Libraries for Python rebuilds these powerful open source projects within the Chainguard Factory, enabling access to the Python ecosystem while dramatically reducing risk from an untrusted software supply chain.

Chainguard Libraries for Python enables access to a growing collection of Python packages rebuilt from source. New releases of common libraries or artifacts requested by customers are added to the index by an automated system. Any request for a library or library version missing in Chainguard Libraries automatically triggers a process to provision the artifacts from relevant sources if available. In combination with third-party software repository managers, you can use Chainguard Libraries for Python as a secure source of truth for your development process.

## Technical Details

Most organisations will consume Chainguard Libraries for Python through a repository manager such as
Cloudsmith, JFrog Artifactory or Sonatype Nexus Repository. For full details on how to do this,
refer to our [Global Configuration
documentation](/chainguard/libraries/python/global-configuration). The rest of this article provides
details of the underlying implementation of Chainguard Libraries for Python and how to access
individual libraries manually.

A [username and password retrieved with
chainctl](/chainguard/libraries/access/) are required to access the Chainguard
Libraries for Python repository. The URL for the repository is:

```
https://libraries.cgr.dev/python/
```

The URL does not expose a browsable directory structure. However, if you know the location of any particular artifact, you can use the login credentials and a set path URL to access a file.

This Chainguard Libraries for Python repository uses the PyPI repository format and only includes release artifacts of the libraries built by Chainguard from source. 

For example, you can locate a `tar.gz` file on PyPI:

```
https://files.pythonhosted.org/packages/source/f/flask/flask-3.1.0.tar.gz
```

Combine it with the URL for the Chainguard Libraries for Python repository to check for the presence of the same file:

```
https://libraries.cgr.dev/python/flask/flask-3.1.0.tar.gz
```

Use the search functionality on [pypi.org](https://pypi.org/) to locate packages of interest.

If you use the URL directly in a browser, you have to provide the username and
password to log in to the Chainguard repository to download the file.

Use curl and specify the [username and password retrieved with
chainctl](/chainguard/libraries/access/) for basic user authentication and the
URL of the file to download and save the file with the original name:

```
curl --user "exampleusername:examplepassword" \
  -O https://libraries.cgr.dev/python/flask/flask-3.1.0.tar.gz
```

The Chainguard Libraries for Python repository does not include all packages from PyPI. Chainguard Libraries for Python are rebuilt from source and require that source be available. Therefore, packages that do not provide a valid source URL cannot be rebuilt within the Chainguard Factory. In addition, initial package rebuild coverage for Chainguard Libraries for Python is not comprehensive. 

Since coverage within Chainguard Libraries for Python is not comprehensive, you should strongly consider setting the PyPI public package index as a fallback within your artifact repository manager. In this case, failed requests are logged by Chainguard and, where possible, the package will be prioritized for rebuild from source. Typically, access is [configured globally on a repository manager for your organization](/chainguard/libraries/python/global-configuration/).

Alternatively, you can use the token for direct access to the Chainguard Libraries for Python index as discussed in [Build configuration](/chainguard/libraries/python/build-configuration/).
