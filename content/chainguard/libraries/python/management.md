---
title: "Management and Maintenance "
linktitle: "Management "
description: "Working with your Chainguard Libraries for Python use"
type: "article"
date: 2025-03-25T08:04:00+00:00
lastmod: 2025-04-03T09:09:00+00:00
draft: false
tags: ["Chainguard Libraries", "Python"]
images: []
menu:
  docs:
    parent: "Python"
weight: 053
toc: true
---

After the initial [global
configuration](/chainguard/libraries/java/global-configuration/) and [build
configuration](/chainguard/libraries/java/build-configuration/) the use of
Chainguard Libraries for Python is transparently in progress. Newly use artifacts
from new projects or new artifact versions are automatically retrieved from the
Chainguard repository as they are available and the PyPI repository and
other configured repositories serve as backstop to provide any additionally
needed artifacts.

The following sections detail optional management, maintenance, and auditing
steps on the repository manager and the build tool.

## Source Verification

You can verify what artifacts are retrieved from the Chainguard Libraries
repository on a global level:

* Browse the `chainguard` proxy repository on your Artifactory or Nexus server.
* Access the **Packages** tab of the the repository on your Cloudsmith instance.
  Filter the package list with the tag value with the name for your upstream
  proxy for Chainguard, for example `tag:chainguard`. The tag uses the name of
  the upstream proxy, with spaces replaced with dashes.

Use the browsing access to locate specific artifacts and identify their name,
filesize, checksum values, timestamp and other identifiers. With these details
you can verify your libraries use in the following locations:

* Local cache repositories on developer workstation
* Cache repositories in your CI pipeline
* Libraries in your application bundles
* Installed applications on your hosts or in your container images

## Increase Chainguard Library Use

The number of available artifacts in Chainguard Libraries for Python increases
over time. If an artifact was already retrieved from the PyPI
Repository and is available in your repository manager or local repository it is
not automatically replaced with the equivalent Chainguard Library version. 

You can force a download of new libraries by erasing them from your local
repositories on your workstations and the PyPI proxy repository in your
repository manager. Both these repositories are caches only and it is therefore
safe to delete them.

After the deletion any new build retrieves the artifact again and attempts to
download from the Chainguard repository. As a result, newly available artifacts
replace old artifacts that originated from PyPI and your use of
Chainguard Libraries increased.

For a more fine-grained approach you can also delete subsections of local
repositories and the proxy repositories.
