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

## Introduction

Many Java builds pull dependencies from public sources like Maven Central, but those sources make no guarantees of provenance, CVE remediation, or build integrity. Chainguard Libraries for Java provides enhanced security for the Java ecosystem by rebuilding popular Maven dependencies with the latest patches and comprehensive supply chain protection. As the first supported ecosystem in [Chainguard Libraries](/chainguard/libraries/overview/), this service addresses critical vulnerabilities in the vast Java/JVM ecosystem that spans hundreds of projects from organizations like the Apache Software Foundation, Eclipse Foundation, and numerous independent maintainers. 

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

## Requirements and limitations

### Runtime requirements

The runtime requirements for Java artifacts available from Chainguard Libraries
for Java are identical to the requirements of the original upstream project. For
example, if a JAR retrieved from Maven Central requires Java 17 or higher, the
same Java 17 runtime requirement applies to the binary artifact from Chainguard
Libraries for Java.

### Limitations

Chainguard Libraries for Java focuses on secure, source-available artifacts. As a result, some content commonly found in Maven Central is intentionally excluded, including:

* Closed-source binary libraries, such as proprietary JDBC drivers (for example, Oracle Database drivers)
* Artifacts without accessible or complete source code, or where the source code cannot be used to reliably reproduce the binary
* Artifact variants that are not produced by the upstream source build, which commonly include:
  * Source JARs (*-sources.jar)
  * Javadoc JARs (*-javadoc.jar)
  * Fat or shaded JARs (JARs with dependencies included)
  * Distribution archives (such as .tar.gz)
  * Non-JAR formats (for example RPMs, shared libraries, Android AARs)

If your build depends on an artifact that is not available, you may need to request provisioning or configure a fallback repository.

### Repository order and fallback behavior

To ensure your builds use available Chainguard-built artifacts, configure Chainguard Libraries as the first repository in your build tool configuration.

When a dependency cannot be resolved from Chainguard Libraries, your build tool will automatically fall back to the next configured repository (such as Maven Central). This allows you to continue using required dependencies while preferring Chainguard-built artifacts when possible.

Requests for missing artifacts are visible to Chainguard and may be used to trigger backfill or provisioning processes where supported.

#### Repository configuration example
The following example shows Chainguard Libraries configured as the primary repository, with Maven Central as a fallback:

```xml
<repositories>
  <repository>
    <id>chainguard-libraries</id>
    <url>https://libraries.cgr.dev/java/</url>
  </repository>

  <repository>
    <id>maven-central</id>
    <url>https://repo.maven.apache.org/maven2</url>
  </repository>
</repositories>
```
In this configuration, Maven attempts to resolve dependencies from Chainguard Libraries first. If an artifact is not available, Maven falls back to Maven Central.

## Technical details

### Authentication 
Access to the Chainguard Libraries for Java repository is authenticated. 

You must obtain a [username and password using `chainctl`](/chainguard/libraries/access/) and configure those credentials in your build tooling or repository manager. 
The [username and password retrieved with
chainctl](/chainguard/libraries/access/) are required to access the Chainguard
Libraries for Java repository. 

The repository endpoint is:

```
https://libraries.cgr.dev/java/
```

### Repository behavior
This Chainguard Libraries for Java repository uses the Maven repository format
and only includes release artifacts of the libraries built by Chainguard from
source. 

Note the following:
* Only released versions of artifacts are available; snapshot (-SNAPSHOT) versions are not supported
* The repository does not expose a browsable directory listing when accessed via a web browser
* Artifacts can still be retrieved directly if you know the full Maven path (group ID, artifact ID, version, and filename) and provide valid credentials
  * Learn more below under [Manual access](#manual).

This design supports reproducible builds and secure artifact distribution.Snapshot versions are not available.

### Recommended setup
Access is typically [configured globally on a repository manager for your
organization](/chainguard/libraries/java/global-configuration/). This approach
is strongly recommended. 

Alternatively, you can configure credentials directly in your build tool (e.g., Maven or Gradle) to access the repository without a repository manager. This approach is typically used for smaller environments or local development. For more informatioin, see [Build
configuration](/chainguard/libraries/java/build-configuration/).

<a id="manual">

## Manual access

To manually access artifacts in the Chainguard Libraries for Java repository, use the URL [`https://libraries.cgr.dev/java/`](https://libraries.cgr.dev/java/)
with your [username and password retrieved with
chainctl](/chainguard/libraries/access/).

The repository follows the standard [Maven repository
format](https://maven.apache.org/repository/layout.html), where artifacts are organized by `groupId`, `artifactId`, and version. If you know the exact Maven coordinates of an artifact, you can use the full path to retrieve files directly.

This site provides a listing capability similar to
the [Maven Central repository](https://repo1.maven.org/maven2/) (but unlike Maven Central, the repository does not provide an openly browsable directory index). The
structure follows the [Maven repository
format](https://maven.apache.org/repository/layout.html). The `groupId` and
`artifactId` of a library is used to create a nested directory structure,
similar to the package structure within Java projects.

For example, the Maven coordinates for [Apache Commons
Lang](https://commons.apache.org/proper/commons-lang/) 3.18.0 are the following:

```xml
<groupId>org.apache.commons</groupId>
<artifactId>commons-lang3</artifactId>
<version>3.18.0</version>
```

All available versions can be found in
[https://libraries.cgr.dev/java/org/apache/commons/commons-lang3](https://libraries.cgr.dev/java/org/apache/commons/commons-lang3)
since the `groupId` is used to create separate, nested directories `org`
`apache`, and `commons`, and the `artifactId` results in the `commons-lang3`
directory.

The final leaf directory is created from the `version`, in the example `3.18.0`.
All leaf directories are allocated for a specific version of a specific library
and contain all relevant files.

For example, the directory at
`https://libraries.cgr.dev/java/org/apache/commons/commons-lang3` contains all
files for the `org.apache.commons:commons-lang3:3.18.0` library. Specifically,
this includes the file `commons-lang3-3.18.0.pom` for the main Maven metadata
from the project and main JAR file `commons-lang3-3.18.0.jar`. The directory
also includes numerous other files, and related checksum files. Specific files
vary between the different libraries.

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
