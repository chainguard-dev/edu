---
title: "Global Configuration"
linktitle: "Global Configuration"
type: "article"
description: "Configuring Chainguard Libraries for Java in your organization"
lead: "lead tbd"
draft: false
tags: ["Chainguard Libraries", "Java"]
images: []
menu:
  docs:
    parent: "java"
weight: 052
toc: true
---

Java and JVM library consumption in a large organization is typically managed by
a repository manager. Commonly used repository manager applications are
[Cloudsmith](https://cloudsmith.com/), [JFrog
Artifactory](https://jfrog.com/artifactory/), and [Sonatype Nexus
Repository](https://www.sonatype.com/products/sonatype-nexus-repository). The
repository manager acts as a single point of access for developers and
development tools to retrieve the required libraries.

At a high level, adopting the use of Chainguard Libraries consists of the the
following steps:

* Add Chainguard Libraries as a remote repository for library retrieval.
* Configure the Chainguard Libraries repository as the first choice for any
  library access. This ensures that any future requests of new libraries access
  the version supplied by Chainguard. Typically this is accomplished by creating a
  group repository or virtual repository that combines the repository with other
  external and internal repositories.

Additional steps depend on the desired insights and can include the following
optional measures:

* Remove all cached artifacts in the proxy repository of Maven Central and other
  repositories. This step allows you to validate which libraries are not
  available from Chainguard Libraries and proceed with potential next steps with
  Chainguard and your own development efforts. 
* Remove any repositories that are no longer desired or necessary. Depending on
  your library requirements this step can result in removal of some proxy
  repositories or even removal of all proxy repositories. 

Adopting the use of a repository manager is the recommended approach, however if
your organization does not use a repository manager, you can still use
Chainguard Libraries. All access to the Chainguard libraries repository is then
distributed across all your build platforms and therefore more complex to
configure and control. 

## Cloudsmith

[Cloudsmith](https://cloudsmith.com/) supports Maven repositories for proxying
and hosting. Refer to the [Maven Repository
documentation](https://help.cloudsmith.io/docs/maven-repository) and the [Maven
Upstream
documentation](https://help.cloudsmith.io/docs/upstream-proxying-caching#create-a-maven-upstream)
for Cloudsmith for more information. Cloudsmith supports combining repositories
by defining multiple upstream repositories.

Use the following steps to add a repository with the Maven Central Repository
and the Chainguard Libraries for Java repository as Maven upstream repositories. 

1. Log in as a user with administrator privileges.
1. Select the **Repositories** tab near the top of the screen.
1. On the **Repositories** page, click the **+ New Repository** button.
1. Enter the name *maven* for your new repository. The name should include
   *maven* to identify the repository format. This convention helps avoiding
   confusion since repositories in Cloudsmith are multi-format.
1. Press **+ Create Repository**. 
1. Click the name of the new repository on the repositories page to configure
   it.
1. Access the **Upstreams** tab and click **+ Add Upstream Proxy** and proceed
   to configure two upstream proxies.
1. Configure an upstream proxy with the following details:
    * **Name** *chainguard* 
    * **Priority** *1*
    * **Upstream URL** *https://libraries.cgr.dev/maven/*
    * **Mode** *Cache and Proxy*
    * Add the **Username** and **Password** value from [Chainguard Libraries
      access](/chainguard/libraries/access/) in **Authentication**
1. Press **Create Maven Upstream**.
1. Configure another upstream proxy with the following details
    * **Name** *central* 
    * **Priority** *2*
    * **Upstream URL** *https://repo1.maven.org/maven2/*
    * **Mode** *Cache and Proxy*
1. Press **Create Maven Upstream**.

Use this setup for initial testing with Chainguard Libraries for Java. For
production usage add the `chainguard` upstream proxy to your production
repository.

Use the URL of the repository in the [build
configuration](/chainguard/libraries/java/build-configuration) and build a
first test project. In a working setup all libraries retrieved from Chainguard
are tagged with the name of the upstream proxy.

## JFrog Artifactory

[JFrog Artifactory](https://jfrog.com/artifactory/) supports Maven repositories
for proxying and hosting, and virtual repositories to combine them. Refer to the
[Maven Repository documentation for
Artifactory](https://jfrog.com/help/r/jfrog-artifactory-documentation/maven-repository)
for more information.

Use the following steps to add the Maven Central Repository and the Chainguard
Libraries for Java repository as remote repositories and combine them as a
virtual repository:

1. Log in as a user with administrator privileges.
1. Press **Administration** in the top navigation bar.
1. Select **Repositories** in the left hand navigation.

Configure a remote repository for the Maven Central Repository:

1. Press **Create a Repository** and choose the **Remote** option.
1. Select *Maven* as the Package type.
1. Set the **Repository Key** to *maven-central*.
1. Set the **URL** to *https://repo1.maven.org/maven2/* .
1. Press Create Remote Repository.

Configure a remote repository for the Chainguard Libraries for Java repository:

1. Press **Create a Repository** and choose the **Remote** option.
1. Select *Maven* as the **Package type**.
1. Set the **Repository Key** to *chainguard*.
1. Set the **URL** to *https://libraries.cgr.dev/maven/*.
1. Set **User Name** and Password / Access Token to the [values as retrieved
   with chainctl](/chainguard/libraries/access/).
1. Check the **Enable Token Authentication** checkbox.
1. Press Test to validate the connection.
1. Press Create Remote Repository.

Combine the two repositories in a new virtual repository:

1. Press **Create a Repository** and choose the **Virtual** option.
1. Set the **Repository Key** to *chainguard-group*.
1. Scroll down to the **Repositories** section
1. Add the *chainguard* and *maven-central* repositories. Ensure the *chainguard* repository is the
   first in the displayed list.
1. Press **Create Virtual Repository**.

Use this setup for initial testing with Chainguard Libraries for Java. For
production usage add the `chainguard` repository to your production virtual
repository.

Use the URL of the virtual repository in the [build
configuration](/chainguard/libraries/java/build-configuration) and build a first
test project. In a working setup the chainguard remote repository contains all
libraries retrieved from Chainguard.

## Sonatype Nexus Repository

[Sonatype Nexus
Repository](https://www.sonatype.com/products/sonatype-nexus-repository)
includes a *maven-public* repository group out of the box. It groups access to
the Maven Central Repository from the *maven-central* repository with the
internal *maven-releases* and *maven-snapshot* repositories. Refer to the [Maven
Repositories documentation for
Nexus](https://help.sonatype.com/en/maven-repositories.html) for more
information.

If you are using this group, you can add a proxy repository for Chainguard
Libraries for Java repository for production use.

For initial testing and adoption it is advised to create a separate proxy
repository for the Maven Central Repository, a separate proxy repository
Chainguard Libraries for Java repository, and a separate repository group:

1. Log in as a user with administrator privileges.
1. Access the **Server administration** and configuration section with the gear
   icon in the top navigation bar.

Configure a remote repository for the Maven Central Repository:

1. Select **Repository - Repositories** in the left hand navigation.
1. Press **Create repository**.
1. Select the **maven2 (proxy)** recipe.
1. Provide a new name *central*.
1. In the **Proxy - Remote storage** input add the URL *https://repo1.maven.org/maven2/*.
1. Press **Create repository**.

Configure a remote repository for the Chainguard Libraries for Java repository:

1. Select **Repository - Repositories** in the left hand navigation.
1. Press **Create repository**.
1. Select the **maven2 (proxy)** recipe.
1. Provide a new name *chainguard*.
1. In the **Proxy - Remote storage** input add the URL *https://libraries.cgr.dev/maven*.
1. In **HTTP - Authentication** with the **Authentication type** *username*,
   provide the [username and password values as retrieved with
   chainctl](/chainguard/libraries/access/).
1. Press **Create repository**. 

Combine a new repository group and add the two repositories:

1. Select **Repository - Repositories** in the left hand navigation.
1. Press **Create repository**.
1. Select the **maven2 (group)** recipe.
1. Provide a new name *chainguard-group*.
1. In the section **Group - Member repositories**, move the new repositories
   `central` and `chainguard` to the right and move the `chainguard` repository
   to the top of the list with the arrow control.

Use the URL of the repository group, such as
*https://repo.example.com/repository/chainguard-group/* or
*https://repo.example.com/repository/maven-public/* in the [build
configuration](/chainguard/libraries/java/build-configuration) and build a first
test project. In a working setup the `chainguard` proxy repository contains all
libraries retrieved from Chainguard.
