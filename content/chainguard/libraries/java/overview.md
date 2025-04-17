---
title: "Chainguard Libraries for Java Overview"
linktitle: "Java Overview"
description: "Java libraries for your application development"
type: "article"
date: 2025-03-25T08:04:00+00:00
lastmod: 2025-03-31T15:31:00+00:00
draft: false
tags: ["Chainguard Libraries", "Java", "Overview"]
menu:
  docs:
    parent: "java"
weight: 051
toc: true
---

## Introduction

**Chainguard Libraries for Java** represents the first ecosystem support with
[Chainguard Libraries](/chainguard/libraries/overview/). The Java and larger JVM
ecosystem consists of hundreds of open source projects from large foundations
such as the Apache Software Foundation, the Eclipse Foundation, and many smaller
foundations and projects. 

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

## Technical Details

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

* Source JAR artifacts
* Javadocs JAR artifacts
* Distributable versions of artifacts such JARs with dependencies or tar.gz archives
* Other package formats sometimes found such as RPMs, SO files, Android AARs,
  and similar rarely used artifacts

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

<a id="java-repo-test">

### Manual Testing

You can manually download specific artifacts from the repository if you know the
URL as determined by the identifying GAV coordinates for an artifact.

For example, you can locate a Maven POM file on the Maven Central Repository:

```
https://repo1.maven.org/maven2/commons-io/commons-io/2.17.0/commons-io-2.17.0.pom
```

And then use the path composed from the Maven coordinates

```
commons-io/commons-io/2.17.0/commons-io-2.17.0.pom
```

And combine it with the URL for the Chainguard Libraries for Java repository to
check for the presence of the same file:

```
https://libraries.cgr.dev/java/commons-io/commons-io/2.17.0/commons-io-2.17.0.pom
```

Use the [Maven Central Repository search](https://central.sonatype.com/) or
[browse functionality](https://repo1.maven.org/maven2/) to locate artifacts of
interest.

If you use the URL directly in a browser, you have to provide the username and
password to log in to the Chainguard repository to download the file.

Use curl and specify the [username and password retrieved with
chainctl](/chainguard/libraries/access/) for basic user authentication and the
URL of the file to download and save the file with the original name:

```
curl --user "exampleusername:examplepassword" \
  -O https://libraries.cgr.dev/java/commons-io/commons-io/2.17.0/commons-io-2.17.0.pom
```

[Use checksums of any file to
verify](/chainguard/libraries/java/management/#java-verification) if it
originates from the Chainguard repository.