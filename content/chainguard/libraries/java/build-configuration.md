---
title: "Build Configuration"
linktitle: "Build Configuration"
type: "article"
description: "Configuring Chainguard Libraries for Java on your workstation"
draft: false
tags: ["Chainguard Libraries", "Java"]
menu:
  docs:
    parent: "java"
weight: 053
toc: true
---

The configuration for the use of Chainguard Libraries depends on your build
tools, continuous integration, and continuous deployment setups

At a high level adopting the use of Chainguard Libraries consists of the
following steps:

* Remove local caches on workstations and CI/CD pipelines. This step ensures that
  any libraries that were already sourced from other repositories are requested
  again and the version from Chainguard Libraries is used instead of other
  binaries.
* Change configuration to access Chainguard Libraries via your repository
  manager after the changes from the [global
  configuration](/chainguard/libraries/java/global-configuration) are
  implemented.

These changes must be performed on all workstations of individual developers and
other engineers running relevant application builds. They must also be performed
on any build server such as Jenkins, TeamCity, GitHub or other infrastructure
that builds the applications or otherwise downloads and uses relevant libraries.

## Cloudsmith

Build configuration to retrieve artifacts from Cloudsmith requires you to
authenticate. Use your username and password for Cloudsmith in your build tool
configuration.

## JFrog Artifactory

Build configuration to retrieve artifacts from Artifactory typically requires
you to authenticate and use the identity token in the configuration of your
build tool:

1. Log in as user with access to the configured virtual repository.
1. Select **Edit Profile** from the drop down in the top right corner from your
   user name.
1. Press **Generate Identity Token**.
1. Provide a description such as *Chainguard Libraries* for the token as a
   reminder for the use of the token.
1. Copy the token value and use it as your password in your build tool
   configuration.

## Sonatype Nexus Repository

Build configuration to retrieve artifacts from Nexus requires you to
authenticate. Use your username and password for Nexus in your build tool
configuration.

## Apache Maven

[Apache Maven](https://maven.apache.org/) is the most widely used build tool in
the Java ecosystem. 

### Remove Maven Caches

Apache Maven uses a local cache of libraries. When adopting Chainguard Libraries
for Java you must delete that local cache so that libraries are downloaded
again. By default the cache, also known as the local repository, is located in a
hidden `.m2/repository` directory in your user's home directory. Use the
following command to delete it:

```shell
rm -rf ~/.m2/repository
```

### Change Maven Configuration

Before running a new build you must configure access to the Chainguard Libraries
for Java. If the administrator for your organization’s repository manager
created a new repository or virtual repository or group repository, you must
update your settings defined in `~/.m2/settings.xml`.

A typical setup defines a global mirror (id `ecosystems`) for all artifacts and
configures the URL of the repository group or virtual repository from your
repository manager `https://repo.example.com/group/`. Since the group or virtual
repository combines release and snapshot artifacts you must override the
built-in `central` repository and its configuration in an automatically
activated profile.


```xml
<settings>

  <mirrors>
    <mirror>
      <!--Send all requests to the repository manager -->
      <id>ecosystems</id>
      <mirrorOf>*</mirrorOf>
      <url>https://repo.example.com/group/</url>
    </mirror>
  </mirrors>

  <activeProfiles>
    <activeProfile>ecosystems</activeProfile>
  </activeProfiles>

  <profiles>
    <profile>
      <id>ecosystems</id>
      <repositories>
        <repository>
          <id>central</id>
          <url>http://central</url>
          <releases>
            <enabled>true</enabled>
          </releases>
          <snapshots>
            <enabled>true</enabled>
          </snapshots>
        </repository>
      </repositories>
      <pluginRepositories>
        <pluginRepository>
          <id>central</id>
          <url>http://central</url>
          <releases>
            <enabled>true</enabled>
          </releases>
          <snapshots>
            <enabled>true</enabled>
          </snapshots>
        </pluginRepository>
      </pluginRepositories>
    </profile>
  </profiles>

</settings>
```

If your repository manager requires authentication, you must specify credentials
for the server. The id value in the server element must match the id value in
the mirror configuration. The username and password values vary depending on the
repository manager and the configured authentication.

```xml
<settings>
...

  <servers>
    <server>
      <id>ecosystems</id>
      <username>YOUR_USERNAME_FOR_REPOSITORY_MANAGER</username>
      <password>YOUR_PASSWORD</password>
    </server>
  </servers>

....
</settings>

```

Refer to the [official documentation for the Maven settings
file](https://maven.apache.org/settings.html) for more details.

If the administrator only re-configured the existing repository group or virtual
repository, you can trigger a build to initiate use of Chainguard Libraries for
Java.

If you are not using a repository manager at your organization, you can
configure access to the Chainguard Libraries for Java repository directly in
your settings or pom files. Note that the order of the repositories in these
files is significant and you must configure the chainguard repository to be
located on the top of the list.

## Gradle

[Gradle](https://gradle.org/) is a commonly used build tool in the Java
ecosystem.

### Remove Gradle Caches

Gradle uses a local cache of libraries. When adopting Chainguard Libraries for
Java you must delete that local cache so that libraries are downloaded again. By
default the cache is located in a hidden `.gradle/.cache` directory in your
users home directory. Use the following command to delete it:

```shell
rm -rf ~/.gradle/caches/
```

Gradle can also be configured to use a local Maven repository with a repository
configuration in the global `init.gradle` or a project specific `build.gradle`
file:

```
repositories {
   ...
    mavenLocal()    
}
```

If this configuration is used, ensure to [delete the local Maven repository as
well](#remove-maven-caches). 

### Change Gradle Configuration

Global configuration for artifact download is Gradle can be performed in an
[init
script](https://docs.gradle.org/current/userguide/init_scripts.html#sec:using_an_init_script)
using the repositories definition. Each project can also [declare
repositories](https://docs.gradle.org/current/userguide/declaring_repositories_basics.html)
separately.

Configure the Chainguard Libraries for Java repository with the credentials from
[Chainguard Libraries access](/chainguard/libraries/access/). Ensure that the
chainguard repository is located above the mavenCentral repository.

```
repositories {
    maven {
        url = uri("https://libraries.cgr.dev/maven/")
        credentials {
            username = "longhash"
            password = "longerhash"
        }
    }
    mavenCentral()
}
```

## Other Build Tools

Other build tools such as [Apache Ant](https://ant.apache.org/) with the [Maven
Artifact Resolver Ant Tasks](https://maven.apache.org/resolver-ant-tasks/),
[sbt](https://www.scala-sbt.org/), [Bazel](https://bazel.build/),
[Leiningen](https://leiningen.org/) and others use Maven or Gradle caches or
similar approaches. Refer to the documentation of your specific tool and the
preceding sections to determine how to remove any used caches.

These tools also include their own mechanisms to configure repositories for
binary artifact retrieval. Consult the specific documentation and adjust your
configuration to use your repository manager and newly created repository group
or virtual repository.
