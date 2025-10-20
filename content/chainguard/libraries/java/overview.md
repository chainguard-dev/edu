---
title: "Chainguard Libraries for Java Overview"
linktitle: "Java Overview"
description: "Learn about Chainguard Libraries for Java, providing enhanced security for Maven dependencies through automated vulnerability patching and supply chain protection"
type: "article"
date: 2025-03-25T08:04:00+00:00
lastmod: 2025-07-23T15:09:59+00:00
draft: false
tags: ["Chainguard Libraries", "Java", "Overview"]
menu:
  docs:
    parent: "java"
weight: 051
toc: true
---

## Introduction

Chainguard Libraries for Java provides enhanced security for the Java ecosystem by rebuilding popular Maven dependencies with the latest patches and comprehensive supply chain protection. As the first supported ecosystem in [Chainguard Libraries](/chainguard/libraries/overview/), this service addresses critical vulnerabilities in the vast Java/JVM ecosystem that spans hundreds of projects from organizations like the Apache Software Foundation, Eclipse Foundation, and numerous independent maintainers. 

Chainguard Libraries for Java provides access to all open source libraries
commonly used. New releases of common libraries or artifacts requested by
customers are added to the growing index by an automated system. The number of
included libraries continues to grow.

The main public repository for binary artifacts is the [Maven Central
Repository](https://central.sonatype.com/). It has been in operation for  nearly
20 years and hosts artifacts of all releases of most open source projects in the
Java community.  It is the default repository in all commonly used build tools
from the Java community including [Apache Maven](https://maven.apache.org/),
[Gradle](https://gradle.org/), and others and uses the Maven repository format.
Chainguard Libraries for Java covers all open source artifacts from Maven
Central.

Chainguard Libraries for Java also builds binaries for many other open source
projects available in other repositories or on code hosting platforms like
GitHub. Examples include Google, Oracle, JetBrains, CERN, Apache, and many
others. Any request for a library or library version missing in Chainguard
Libraries automatically triggers a process to provision the artifacts from
relevant sources if available. 

You can use Chainguard Libraries for Java alongside third-party software
repositories to create a single source of truth with your repository manager
application. 

## Runtime requirements

The runtime requirements for Java artifacts available from Chainguard Libraries
for Java are identical to the requirements of the original upstream project. For
example, if a JAR retrieved from Maven Central requires Java 17 or higher, the
same Java 17 runtime requirement applies to the binary artifact from Chainguard
Libraries for Java.

## Technical details

The [username and password retrieved with
chainctl](/chainguard/libraries/access/) are required to access the Chainguard
Libraries for Java repository. The URL for the repository is:

```
https://libraries.cgr.dev/java/
```

This Chainguard Libraries for Java repository uses the Maven repository format
and only includes release artifacts of the libraries built by Chainguard from
source. Snapshot versions are not available.

The URL does not expose a browsable directory structure. However, if you know the
location of any particular artifact you can use the login credentials and a set
path URL to access a file.

The Chainguard Libraries for Java repository does not include all artifacts from
the Maven Central Repository and other repositories.

Specifically, the following components can be required by your application
builds, yet are not included:

* Binary versions of closed-source libraries. The Maven Central Repository and
  other repositories often include such libraries. They enable interoperability
  with open source applications and development of internal applications as a
  combination of these libraries and other open source libraries. Examples include
  JDBC drivers for proprietary databases such as Oracle
* Other artifacts that are found in the Maven Central Repository with incomplete
  information about the location of the source code or a pointer to a location
  with access restrictions or an incomplete source, that prevents creation of a
  binary by Chainguard.

Some types of artifacts are included if the source build produces them, but are
often not available:

* JAR artifacts containing the source code
* JAR artifacts containing JavaDoc HTML files
* Distributable versions of artifacts such JARs with dependencies or tar.gz archives
* Other package formats sometimes found such as RPMs, SO files, Android AARs,
  and similar, rarely used artifacts

As a result, you must configure the repository as the first point of contact and
request for any retrieval of a library. This ensures that any library that is
available from Chainguard is also used. In addition, any failed requests are
flagged at Chainguard and backfill processes are run where possible.

At the same time, you must continue to use the Maven Central Repository, and any
other repository that fills the needs for libraries that are not available from
the Chainguard Libraries repository.

Typically the access is [configured globally on a repository manager for your
organization](/chainguard/libraries/java/global-configuration/). This approach
is strongly recommended. 

Alternatively, you can use the token for direct access from a build tool as
discussed in [Build
configuration](/chainguard/libraries/java/build-configuration/).

<a id="manual">

## Manual access

Use the URL [`https://libraries.cgr.dev/java/`](https://libraries.cgr.dev/java/)
with your [username and password retrieved with
chainctl](/chainguard/libraries/access/) to access the Chainguard Libraries for
Java repository and manually browse the repository contents.

This site provides a directory browsing and file listing capability similar to
the Maven Central repository at
[`https://repo1.maven.org/maven2/`](https://repo1.maven.org/maven2/). The
structure follows the [Maven repository
format](https://maven.apache.org/repository/layout.html).

All leaf directories are allocated for a specific version of a specific library
and contain all relevant files. 

For example, the directory at
`https://libraries.cgr.dev/java/commons-io/commons-io/2.17.0/` contains all
files for the `commons-io:commons-io:2.17.0` library. Specifically, this
includes the file `commons-io-2.17.0.pom` for the main Maven metadata from the
project and main JAR file `commons-io-2.17.0.jar`. The directory also includes
numerous other files, and related checksum files. Specific files vary between
the different libraries.

All filenames can be used to download individual files.

Use `curl`, specify the username and password retrieved with [chainctl for basic
user authentication](/chainguard/libraries/access/) and use the URL of the file to
download and save the file with the original name.

With [.netrc authentication](/chainguard/libraries/access/#netrc):

```shell
curl -n -L \
  -O https://libraries.cgr.dev/java/commons-io/commons-io/2.17.0/commons-io-2.17.0.pom
```

With [environment variables](/chainguard/libraries/access/#env):

```shell
curl -L --user "$CHAINGUARD_JAVA_IDENTITY_ID:$CHAINGUARD_JAVA_TOKEN" \
  -O https://libraries.cgr.dev/java/commons-io/commons-io/2.17.0/commons-io-2.17.0.pom
```

The option `-L` is required to follow redirects for the actual file locations.

[Use checksums of any file to
verify](/chainguard/libraries/java/management/#java-verification) if it
originates from the Chainguard repository.

## SBOM and attestation files

Chainguard Libraries for Java include files that contain software bill of
material (SBOM) information. Additional files attest details about build
infrastructure with  the [Supply-chain Levels for Software Artifacts
(SLSA)](https://slsa.dev/) provenance information.

The related files for Chainguard Libraries for Java are located in the same
location as the `.pom`, `.jar`, and other artifacts for a specific library
version and uses the same `artifactId-version` naming convention with the
following extensions:

* `.slsa-attestation.json` for the SLSA provenance attestation
* `.spdx.json for the SBOM information

For example, the file location for artifactId `commons-compress` and version
`1.28.0` is
[https://libraries.cgr.dev/java/org/apache/commons/commons-compress/1.28.0/](https://libraries.cgr.dev/java/org/apache/commons/commons-compress/1.28.0/).
It includes the following files:

* `commons-compress-1.28.0.pom`
* `commons-compress-1.28.0.jar`
* `commons-compress-1.28.0.slsa-attestation.json`
* `commons-compress-1.28.0.spdx.json`
