---
title: "Build Configuration"
linktitle: "Build Configuration"
description: "Configuring Chainguard Libraries for Java on your workstation"
type: "article"
date: 2025-03-25T08:04:00+00:00
lastmod: 2025-04-21T13:22:00+00:00
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
  configuration](/chainguard/libraries/java/global-configuration/) are
  implemented.

These changes must be performed on all workstations of individual developers and
other engineers running relevant application builds. They must also be performed
on any build server such as Jenkins, TeamCity, GitHub or other infrastructure
that builds the applications or otherwise downloads and uses relevant libraries.

## Cloudsmith

Build configuration to retrieve artifacts from Cloudsmith requires you to
authenticate. Use your username and password for Cloudsmith in your build tool
configuration.

Follow the steps from the [global
configuration](/chainguard/libraries/java/global-configuration/#cloudsmith) to
determine URL and authentication details.

## JFrog Artifactory

Build configuration to retrieve artifacts from Artifactory typically requires
you to authenticate and use the identity token in the configuration of your
build tool.

Follow the steps from the [global
configuration](/chainguard/libraries/java/global-configuration/#jfrog-artifactory)
to determine URL and authentication details.

## Sonatype Nexus Repository

Build configuration to retrieve artifacts from Nexus may require authentication.
Use your username and password for Nexus in your build tool configuration.

Follow the steps from the [global
configuration](/chainguard/libraries/java/global-configuration/#sonatype-nexus-repository)
to determine URL and authentication details.

## Apache Maven

[Apache Maven](https://maven.apache.org/) is the most widely used build tool in
the Java ecosystem. 

### Remove Maven caches

Apache Maven uses a local cache of libraries. When adopting Chainguard Libraries
for Java you must delete that local cache so that libraries are downloaded
again. By default the cache, also known as the local repository, is located in a
hidden `.m2/repository` directory in your user's home directory. Use the
following command to delete it:

```shell
rm -rf ~/.m2/repository
```

### Change Maven configuration

Before running a new build you must configure access to Chainguard Libraries
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
      <!-- Set the identifier for the server credentials for repository manager access -->
      <id>repo-example</id>
      <!--Send all requests to the repository manager -->
      <mirrorOf>*</mirrorOf>
      <url>https://repo.example.com/repository/group</url>
      <!-- Cloudsmith example -->
      <!-- <url>https://dl.cloudsmith.io/basic/exampleorg/java-all/maven/</url> -->
      <!-- JFrog Artifactory example -->
      <!-- <url>https://example.jfrog.io/artifactory/java-all/</url> -->
      <!-- Sonatype Nexus example -->
      <!-- <url>https://repo.example.com:8443/repository/java-all/</url> -->
    </mirror>
  </mirrors>

  <!-- Activate repo manager and override central repo from Maven itself with invalid URLs -->
  <activeProfiles>
    <activeProfile>repo-manager</activeProfile>
  </activeProfiles>
  <profiles>
    <profile>
      <id>repo-manager</id>
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
for the server. The `id` value in the server element must match the `id` value
in the mirror configuration - `repo-example` in the example. The username
and password values vary depending on the repository manager and the configured
authentication, contact the administrator and refer to the [global configuration
documentation](/chainguard/libraries/java/global-configuration/).

```xml
<settings>
...
  <servers>
    <server>
      <id>repo-example</id>
      <username>YOUR_USERNAME_FOR_REPOSITORY_MANAGER</username>
      <password>YOUR_PASSWORD</password>
    </server>
  </servers>
</settings>
```

Note that you can use a secret manager application to populate the credentials
for each user on their workstation as well as for service applications in your
CI/CD pipelines into environment variables, for example `CHAINGUARD_JAVA_IDENTITY_ID`
and `CHAINGUARD_JAVA_TOKEN`. You can then use an identical server configuration, and
therefore settings file, for all users:

```xml
<settings>
...
  <servers>
    <server>
      <id>repo-example</id>
      <username>${env.CHAINGUARD_JAVA_IDENTITY_ID}</username>
      <password>${env.CHAINGUARD_JAVA_TOKEN}</password>
    </server>
  </servers>
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

If you organization does not use a repository manager you can configure the
Chainguard Libraries for Java repository. Ensure that the Chainguard
repository is located above the necessary override for the built-in `central`
repository and any other repositories.

The following listing shows a complete `~/.m2/settings.xml` file with the
desired configuration and placeholder values `CG_PULLTOKEN_USERNAME` and
`CG_PULLTOKEN_PASSWORD` or [environment
variables](/chainguard/libraries/access/#env) for the pull token detailed in
[Chainguard Libraries access](/chainguard/libraries/access/)

```xml
<settings>
 <activeProfiles>
    <activeProfile>no-repo-manager</activeProfile>
  </activeProfiles>
  <profiles>
    <profile>
      <id>no-repo-manager</id>
      <repositories>
        <repository>
          <id>chainguard</id>
          <url>https://libraries.cgr.dev/java/</url>
          <releases>
            <enabled>true</enabled>
          </releases>
          <snapshots>
            <enabled>false</enabled>
          </snapshots>
        </repository>
        <repository>
          <id>central</id>
          <url>https://repo1.maven.org/maven2/</url>
          <releases>
            <enabled>true</enabled>
          </releases>
          <snapshots>
            <enabled>false</enabled>
          </snapshots>
        </repository>
      </repositories>
      <pluginRepositories>
        <pluginRepository>
          <id>chainguard</id>
          <url>https://libraries.cgr.dev/java/</url>
          <releases>
            <enabled>true</enabled>
          </releases>
          <snapshots>
            <enabled>false</enabled>
          </snapshots>
        </pluginRepository>
        <pluginRepository>
          <id>central</id>
          <url>https://repo1.maven.org/maven2/</url>
          <releases>
            <enabled>true</enabled>
          </releases>
          <snapshots>
            <enabled>false</enabled>
          </snapshots>
        </pluginRepository>
      </pluginRepositories>
    </profile>
  </profiles>
  <servers>
    <server>
      <id>chainguard</id>
      <!-- pick up values from environment variables -->
      <username>${env.CHAINGUARD_JAVA_IDENTITY_ID}</username>
      <password>${env.CHAINGUARD_JAVA_TOKEN}</password>
      <!-- or use literal values -->
      <!-- <username>CG_PULLTOKEN_USERNAME</username> -->
      <!-- <password>CG_PULLTOKEN_PASSWORD</password> -->
    </server>
  </servers>
</settings>
```

The preceding settings affects all projects built on the machine where the file
is configured. Alternatively you can add the `repositories` and
`pluginRepositories` to individual project `pom.xml` files. Authentication
details must remain within the settings file.

## Gradle

[Gradle](https://gradle.org/) is a commonly used build tool in the Java
ecosystem.

### Remove Gradle caches

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

```groovy
repositories {
   ...
    mavenLocal()    
}
```

If this configuration is used, ensure to [delete the local Maven repository as
well](#remove-maven-caches). 

### Change Gradle configuration

Before running a new build you must configure access to the Chainguard Libraries
for Java. If the administrator for your organization’s repository manager
created a new repository or virtual repository or group repository, you must
update your Gradle configuration. Artifact download is Gradle can be configured
in an [init
script](https://docs.gradle.org/current/userguide/init_scripts.html#sec:using_an_init_script)
using the repositories definition. Each project can also [declare
repositories](https://docs.gradle.org/current/userguide/declaring_repositories_basics.html)
separately.

A typical setup removes the direct reference to Maven Central `mavenCentral()`
and any other repositories, and adds a replacement definition with the URL of the
repository group or virtual repository from your repository manager
`https://repo.example.com/group/` and any applicable authentication details.

```groovy
repositories {
    maven {
        url = uri("https://repo.example.com/group/")
        credentials {
            username = "YOUR_USERNAME_FOR_REPOSITORY_MANAGER"
            password = "YOUR_PASSWORD"
        }
    }
}
```

Example URLs for repository managers:

* Cloudsmith: `https://dl.cloudsmith.io/basic/exampleorg/java-all/maven/`
* JFrog Artifactory: `https://example.jfrog.io/artifactory/java-all/`
* Sonatype Nexus: `https://repo.example.com:8443/repository/java-all/`

If your organization does not use a repository manager you can configure the
Chainguard Libraries for Java repository with the credentials from [Chainguard
Libraries access](/chainguard/libraries/access/) replacing the placeholders
`CHAINGUARD_JAVA_IDENTITY_ID` and `CHAINGUARD_JAVA_TOKEN`. Ensure that the
Chainguard repository is located above the `mavenCentral` repository and any
other repositories:

```groovy
repositories {
    maven {
        url = uri("https://libraries.cgr.dev/java/")
        credentials {
            username = "CHAINGUARD_JAVA_IDENTITY_ID"
            password = "CHAINGUARD_JAVA_TOKEN"
        }
    }
    mavenCentral()
}
```

Alternatively configure [environment
variables](/chainguard/libraries/access/#env) and access the values:

```groovy
repositories {
    maven {
        url = uri("https://libraries.cgr.dev/java/")
        credentials {
            username = "$System.env.CHAINGUARD_JAVA_IDENTITY_ID"
            password = "$System.env.CHAINGUARD_JAVA_TOKEN"
        }
    }
    mavenCentral()
}
```

The following listing shows a valid `init.gradle` file. It wraps the
`repositories` element with `allprojects` so that the scope of the file affects
all projects built locally with Gradle. It also allows for downloads for plugins
and build scripts from the remote URL using `buildscript`. Lastly the example
shows use of an internal repository manager that only serves artifacts without
authentication using HTTP only. Since this is not advisable unless other
networking setups allow a secure use with HTTP, the override with the property
`allowInsecureProtocol` is required:

```groovy
allprojects {
  buildscript {
    repositories {
      maven {
        url = "http://repo.example.com:8081/repository/java-all/"
        allowInsecureProtocol = true
      }
    }
  }
  repositories {
    maven {
        url = "http://repo.example.com:8081/repository/java-all/"
        allowInsecureProtocol = true
    }
  }
}
```

<a id="bazel"></a>

## Bazel

[Bazel](https://bazel.build/) is a fast, scalable, and extensible build tool
commonly used in large-scale projects.

### Remove Bazel caches

Bazel uses a cache to store downloaded artifacts. When adopting Chainguard
Libraries for Java, you must delete this cache to ensure that libraries are
downloaded again. By default, the cache is located in the `.cache/bazel` on
Linux or `/private/var/tmp/_bazel_$USER` on MacOS directory in your user's home
directory. Use the following command to delete it:

```shell
bazel clean --expunge
```

The [Bazel documentation on output
directories](https://bazel.build/remote/output-directories) contains further
details.

### Change Bazel configuration

Before running a new build, you must configure access to Chainguard Libraries
for Java. If the administrator for your organization’s repository manager
created a new repository or virtual repository, you must update your Bazel
configuration to use the repository manager.

Bazel uses `MODULE.bazel` files to define external dependencies as `artifacts`.
You can configure a Maven repository for artifact retrieval using `repositories`
from the
[rules_jvm_external](https://github.com/bazel-contrib/rules_jvm_external) rule: 

Following is an example configuration for a repository manager:

```MODULE.bazel
bazel_dep(name = "rules_jvm_external", version = "6.3")
maven = use_extension("@rules_jvm_external//:extensions.bzl", "maven")

maven.install(
    name = "maven",
    # Example dependencies to retrieve
    artifacts = [
        "com.google.guava:guava:32.0.1-jre",
        "org.slf4j:slf4j-api:2.0.5", 
        "ch.qos.logback:logback-classic:1.4.7",
    ],
    repositories = [
        # To use Chainguard Libraries for Java via a repository manager:
        "https://repo.example.com/repository/java-all/",
    ],
    # Uncomment and configure authentication if needed:
    # auth = {
    #     "https://repo.example.com/repository/java-all/": {
    #         "type": "basic",
    #         "username": "YOUR_USERNAME_FOR_REPOSITORY_MANAGER", 
    #         "password": "YOUR_PASSWORD",
    #     },
    # },
)

use_repo(maven, "maven")
```

Example URLs for repository managers:

* Cloudsmith: https://dl.cloudsmith.io/basic/exampleorg/java-all/maven/
* JFrog Artifactory: https://example.jfrog.io/artifactory/java-all/
* Sonatype Nexus: https://repo.example.com:8443/repository/java-all/

If your organization does not use a repository manager, you can configure the
Chainguard Libraries for Java repository directly, and include the Maven Central
repository as fallback. Replace the placeholders `CHAINGUARD_JAVA_IDENTITY_ID`
and `CHAINGUARD_JAVA_TOKEN` with the credentials provided by Chainguard:

```MODULE.bazel
maven.install(
    name = "maven",
    # Example dependencies to retrieve
    artifacts = [
        "com.google.guava:guava:32.0.1-jre",
        "org.slf4j:slf4j-api:2.0.5", 
        "ch.qos.logback:logback-classic:1.4.7",
    ],
    
    repositories = [
        # To use Chainguard Libraries directly (requires credentials):
        "https://libraries.cgr.dev/java/",
        
        # Use Maven Central as fallback
        "https://repo1.maven.org/maven2/",
    ],
    auth = {
         "https://libraries.cgr.dev/java/": {
             "type": "basic",
             "username": "CHAINGUARD_JAVA_IDENTITY_ID", 
             "password": "CHAINGUARD_JAVA_TOKEN",
         },
    },
)
```

Ensure that the Chainguard repository is listed before any other repositories to
prioritize it for artifact retrieval. 

For more complex Bazel setups, you can use [.netrc for
authentication](/chainguard/libraries/access/#netrc).

Refer to the [official Bazel documentation for
rules_jvm_external](https://github.com/bazel-contrib/rules_jvm_external) for
more detailed configuration options.

## Other build tools

Other build tools such as [Apache Ant](https://ant.apache.org/) with the [Maven
Artifact Resolver Ant Tasks](https://maven.apache.org/resolver-ant-tasks/),
[sbt](https://www.scala-sbt.org/), [Leiningen](https://leiningen.org/) and
others use Maven or Gradle caches or similar approaches. Refer to the
documentation of your specific tool and the preceding sections to determine how
to remove any used caches.

These tools also include their own mechanisms to configure repositories for
binary artifact retrieval. Consult the specific documentation and adjust your
configuration to use your repository manager and newly created repository group
or virtual repository.

Example URLs for repository managers:

* Cloudsmith: `https://dl.cloudsmith.io/basic/exampleorg/java-all/maven/`
* JFrog Artifactory: `https://example.jfrog.io/artifactory/java-all/`
* Sonatype Nexus: `https://repo.example.com:8443/repository/java-all/`
