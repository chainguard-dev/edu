---
title: "Chainguard Libraries for Java overview"
linktitle: "Java overview"
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

Chainguard Libraries for Java provides enhanced security for the Java ecosystem by rebuilding dependencies from Maven Central and other common repositories with the latest patches and comprehensive supply chain protection. This service addresses critical vulnerabilities in the vast Java/JVM ecosystem that spans hundreds of projects from organizations like the Apache Software Foundation, Eclipse Foundation, and numerous independent maintainers. 

Chainguard Libraries for Java provides access to all open source libraries
commonly used. New releases of common libraries or artifacts requested by
customers are added to the growing index by an automated system. The number of
included libraries continues to grow. These artifacts are accessible through the
[Chainguard Repository](https://edu.chainguard.dev/chainguard/libraries/chainguard-repository/),
a single endpoint for package retrieval that supports configurable security
policies for both Chainguard-built and upstream packages.

The main public repository for binary artifacts is the [Maven Central
Repository](https://central.sonatype.com/). In operation for over
20 years, it hosts artifacts for most open source projects in the
Java community. It is the default repository in all commonly used build tools
from the Java community including [Apache Maven](https://maven.apache.org/),
[Gradle](https://gradle.org/), and others, and uses the Maven repository format.
Chainguard Libraries for Java covers a broad and growing set of artifacts from
Maven Central.

While Maven Central is the primary reference repository, Chainguard Libraries
for Java also builds binaries for open source projects available in other
repositories like the Google or Confluent repositories. This covers libraries
not found on Maven Central, sourced from
[Google](https://maven.google.com/web/index.html),
[Oracle](https://www.oracle.com/webfolder/application/maven/index.html),
[JetBrains](https://www.jetbrains.com/intellij-repository/releases),
CERN,
[Confluent](https://packages.confluent.io/maven/), [Gradle](https://plugins.gradle.org/m2/), and other public artifact repositories.
Note that coverage is not exhaustive for any single repository; the index
continues to grow, and any request for a missing library or version
automatically triggers a process to provision the artifacts from relevant
sources if available. 

## Runtime requirements

The runtime requirements for Java artifacts available from Chainguard Libraries
for Java are identical to the requirements of the original upstream project. For
example, if a JAR retrieved from Maven Central requires Java 17 or higher, the
same Java 17 runtime requirement applies to the binary artifact from Chainguard
Libraries for Java.

## Technical details

You must use the [username and password retrieved with
chainctl](/chainguard/libraries/access/) to access the Chainguard
Libraries for Java repository. 

The URL for the repository is:

```
https://libraries.cgr.dev/java/
```

The repository root at `https://libraries.cgr.dev/java/` is not browsable, but you can access artifacts directly by their [Maven repository format](https://maven.apache.org/repository/layout.html) path: list the available versions of a library through its `maven-metadata.xml` file, view the files for a specific version in that version's directory, and download individual files by their full path. Learn more under [Manual access](#manual).
The repository root at `https://libraries.cgr.dev/java/` is not browsable, but you can access artifacts directly by their [Maven repository format](https://maven.apache.org/repository/layout.html) path: list the available versions of a library through its `maven-metadata.xml` file, view the files for a specific version in that version's directory, and download individual files by their full path. Learn more under [Manual access](#manual).

This Chainguard Libraries for Java repository uses the Maven repository format
and only includes release artifacts of the libraries built by Chainguard from
source. It does not include all artifacts from Maven Central or other repositories. Snapshot versions are not available.

The following components can be required by your application
builds, but are not included:

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

As a result, **you must configure the repository as the first point of contact and
request for any retrieval of a library**. This ensures that any library that is
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

## CVE remediation

Chainguard Libraries for Java includes the [CVE
Remediation](/chainguard/libraries/cve-remediation/) feature, available in beta for Spring Boot. Remediated
libraries include an appended local version identifier of `-0.cgr.N`. 

For example, if `org.apache.commons:commons-lang3:3.18.0` has a remediated build, that build is published as `org.apache.commons:commons-lang3:3.18.0-0.cgr.1`. If Chainguard publishes another remediated iteration for the same base version, the trailing number increases, such as `-0.cgr.2` or `-0.cgr.3`.

Maven and Gradle treat the `-0` as part of the version ordering. In practice, `3.18.0-0.cgr.1` sorts higher than `3.18.0`. This means version ranges or dependency management rules can resolve to the remediated build when the overlay repository is available.

Learn how to opt in to remediated versions in the [Java build configuration docs](/chainguard/libraries/java/build-configuration/#selecting-remediated-library-versions).

### Troubleshooting resolution issues

Enabling the remediated repository does not typically require clearing caches. However, clearing the cache may help when troubleshooting resolution issues.

Maven:

```bash
rm -rf ~/.m2/repository
```

Gradle:

```bash
rm -rf ~/.gradle/caches/
```

Bazel:

```bash
bazel clean --expunge
```

<a id="manual"></a>

## Manual access

To manually access artifacts in the Chainguard Libraries for Java repository, use the URL [`https://libraries.cgr.dev/java/`](https://libraries.cgr.dev/java/)
with your [username and password retrieved with
chainctl](/chainguard/libraries/access/).

The repository follows the [Maven repository
format](https://maven.apache.org/repository/layout.html), where the `groupId` and
`artifactId` of a library form a nested directory structure, similar to the
package structure within Java projects. The repository root at
[`https://libraries.cgr.dev/java/`](https://libraries.cgr.dev/java/) is not
browsable, but you can discover and retrieve artifacts directly as described
below.
The repository follows the [Maven repository
format](https://maven.apache.org/repository/layout.html), where the `groupId` and
`artifactId` of a library form a nested directory structure, similar to the
package structure within Java projects. The repository root at
[`https://libraries.cgr.dev/java/`](https://libraries.cgr.dev/java/) is not
browsable, but you can discover and retrieve artifacts directly as described
below.

For example, the Maven coordinates for [Apache Commons
Lang](https://commons.apache.org/proper/commons-lang/) are the following:
Lang](https://commons.apache.org/proper/commons-lang/) are the following:

```xml
<groupId>org.apache.commons</groupId>
<artifactId>commons-lang3</artifactId>
<version>3.13.0</version>
<version>3.13.0</version>
```

**Find available versions**

List the versions that Chainguard has built for a library by requesting its
`maven-metadata.xml` file at the `groupId`/`artifactId` path. The `groupId`
`org.apache.commons` becomes the nested directories `org/apache/commons`, and the
`artifactId` adds the `commons-lang3` directory:

```
https://libraries.cgr.dev/java/org/apache/commons/commons-lang3/maven-metadata.xml
```

The repository only includes release artifacts that Chainguard builds from source,
so the versions listed may differ from those available on Maven Central.

**List the files for a version**

Each version has its own leaf directory, formed by appending the `version` to the
`groupId`/`artifactId` path. This version directory is browsable and lists all
files for that specific library version:

```
https://libraries.cgr.dev/java/org/apache/commons/commons-lang3/3.13.0/
```

For the `org.apache.commons:commons-lang3:3.13.0` library, this directory includes
the main Maven metadata file `commons-lang3-3.13.0.pom`, the main JAR file
`commons-lang3-3.13.0.jar`, related checksum files, and the SBOM and attestation
files described below. Specific files vary between libraries.
**Find available versions**

List the versions that Chainguard has built for a library by requesting its
`maven-metadata.xml` file at the `groupId`/`artifactId` path. The `groupId`
`org.apache.commons` becomes the nested directories `org/apache/commons`, and the
`artifactId` adds the `commons-lang3` directory:

```
https://libraries.cgr.dev/java/org/apache/commons/commons-lang3/maven-metadata.xml
```

The repository only includes release artifacts that Chainguard builds from source,
so the versions listed may differ from those available on Maven Central.

**List the files for a version**

Each version has its own leaf directory, formed by appending the `version` to the
`groupId`/`artifactId` path. This version directory is browsable and lists all
files for that specific library version:

```
https://libraries.cgr.dev/java/org/apache/commons/commons-lang3/3.13.0/
```

For the `org.apache.commons:commons-lang3:3.13.0` library, this directory includes
the main Maven metadata file `commons-lang3-3.13.0.pom`, the main JAR file
`commons-lang3-3.13.0.jar`, related checksum files, and the SBOM and attestation
files described below. Specific files vary between libraries.

All filenames can be used to download individual files.

Use `curl`, specify the username and password retrieved with [chainctl for basic
user authentication](/chainguard/libraries/access/) and use the URL of the file to
download and save the file with the original name.

With [.netrc authentication](/chainguard/libraries/access/#netrc):

```shell
curl -n -L \
  -O https://libraries.cgr.dev/java/commons-io/commons-io/2.13.0/commons-io-2.13.0.pom
  -O https://libraries.cgr.dev/java/commons-io/commons-io/2.13.0/commons-io-2.13.0.pom
```

With [environment variables](/chainguard/libraries/access/#env):

```shell
curl -L --user "$CHAINGUARD_JAVA_IDENTITY_ID:$CHAINGUARD_JAVA_TOKEN" \
  -O https://libraries.cgr.dev/java/commons-io/commons-io/2.13.0/commons-io-2.13.0.pom
  -O https://libraries.cgr.dev/java/commons-io/commons-io/2.13.0/commons-io-2.13.0.pom
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
* `.spdx.json` for the SBOM information
* `.spdx.json` for the SBOM information

For example, the files for artifactId `commons-compress` and version
`1.23.0` are located in the version directory
[https://libraries.cgr.dev/java/org/apache/commons/commons-compress/1.23.0/](https://libraries.cgr.dev/java/org/apache/commons/commons-compress/1.28.0/).
It includes the following files:

* `commons-compress-1.23.0.pom`
* `commons-compress-1.23.0.jar`
* `commons-compress-1.23.0.slsa-attestation.json`
* `commons-compress-1.23.0.spdx.json`

## Upstream fallback policy and controls

Chainguard Libraries for Java supports an optional built-in fallback to
the upstream Maven Central repository, managed through the [Chainguard
Repository](/chainguard/chainguard-repository/overview/). By default, the endpoint serves
only Chainguard-built packages. When the upstream fallback is enabled, upstream packages are
subject to additional security controls before being served, including source code and maintainer behavior scanning and a configurable cooldown period.

For Java, Chainguard's scanning inspects compiled `.class` files, package metadata, and extracted `.jar`, `.war`, and `.ear` archive contents for suspicious patterns and malicious signals.

Learn more in the [Chainguard Libraries Overview](/chainguard/libraries/overview/).
