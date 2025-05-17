---
title: "Management and Maintenance"
linktitle: "Management"
description: "Working with your Chainguard Libraries for Java use"
type: "article"
date: 2025-03-25T08:04:00+00:00
lastmod: 2025-04-03T09:09:00+00:00
draft: false
tags: ["Chainguard Libraries", "Java"]
images: []
menu:
  docs:
    parent: "java"
weight: 053
toc: true
---

After the initial [global
configuration](/chainguard/libraries/java/global-configuration/) and [build
configuration](/chainguard/libraries/java/build-configuration/) the use of
Chainguard Libraries for Java is transparently in progress. Newly use artifacts
from new projects or new artifact versions are automatically retrieved from the
Chainguard repository as they are available and the Maven Central Repository and
other configure repositories serve as backstop to provide any additionally
needed artifacts.

The following sections detail optional management, maintenance, and auditing
steps on the repository manager and the build tool.

<a id="java-verification">

## Source verification

You can verify what artifacts are retrieved from the Chainguard Libraries
repository on a global level:

* Browse the `chainguard` proxy repository on your Artifactory or Nexus server.
* Access the **Packages** tab of the repository on your Cloudsmith instance.
  Filter the package list with the tag value with the name for your upstream
  proxy for Chainguard, for example `tag:chainguard`. The tag uses the name of
  the upstream proxy, with spaces replaced with dashes.

Use the browsing access to locate specific artifacts and identify their name,
file size, checksum values, timestamp and other identifiers. With these details
you can verify your libraries use in the following locations:

* Local cache repositories on developer workstation
* Cache repositories in your CI pipeline
* Libraries in your application bundles
* Installed applications on your hosts or in your container images

A uniquely identifying characteristic of library artifacts are their checksums.
Contrary to filenames and timestamps, checksums do not change in the use of
libraries during an application build or the assembly of a deployment artifact
like a tarball or container. This allows you to identify a library artifact by
determining the checksum and then locating it in your repository manager.

Calculate the different commonly used sums for a file `example.jar` with the
following commands and output examples:

```shell
$ sha1sum example.jar
aea83e64ebec6a37e0be100f968a55fb381143c2  example.jar

$ sha256sum example.jar
87a25c44e0fdb0c71e898c57f67b236d2205bfa76a25dbbb9779ebe2f93e787e  example.jar

$ md5sum example.jar
fefd660ddc795900d48bdf49c17b3135  example.jar
```

Use the search features in your repository manager, such as Sonatype Nexus, to
locate the library. For the specific example, you find that the checksums
correspond to the file `junit-4.13.2.jar` found in `junit/junit/4.13.2/` and
that the artifact is found in the `chainguard` proxy repository. You can
therefore conclude that the `example.jar` file originates from Chainguard, was
built in the Chainguard Factory from source, and is available at
`https://libraries.cgr.dev/java/junit/junit/4.13.2/junit-4.13.2.jar`. You can
[manually download the file to
compare](/chainguard/libraries/java/overview/#java-repo-test), if desired.

## Increase Chainguard Library use

The number of available artifacts in Chainguard Libraries for Java increases
over time. If an artifact was already retrieved from the Maven Central
Repository and is available in your repository manager or local repository it is
not automatically replaced with the equivalent Chainguard Library version. 

You can force a download of new libraries by erasing them from your local
repositories on your workstations and the Maven Central proxy repository in your
repository manager. Both these repositories are caches only and it is therefore
safe to delete them.

After the deletion any new build retrieves the artifact again and attempts to
download from the Chainguard repository. As a result, newly available artifacts
replace old artifacts that originated from Maven Central and your use of
Chainguard Libraries increased.

For a more fine-grained approach you can also delete subsections of local
repositories and the proxy repositories.
