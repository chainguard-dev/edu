---
title: "Global Configuration"
linktitle: "Global Configuration "
description: "Configuring Chainguard Libraries for Python in your organization"
type: "article"
date: 2025-03-25T08:04:00+00:00
lastmod: 2025-04-07T14:42:00+00:00
draft: false
tags: ["Chainguard Libraries", "Python"]
images: []
menu:
  docs:
    parent: "python"
weight: 052
toc: true
---

Python library consumption in a large organization is typically managed by
a repository manager. Commonly used repository manager applications are
[Cloudsmith](https://cloudsmith.com/), [JFrog
Artifactory](https://jfrog.com/artifactory/), and [Sonatype Nexus
Repository](https://www.sonatype.com/products/sonatype-nexus-repository). The
repository manager acts as a single point of access for developers and
development tools to retrieve the required libraries.

At a high level, adopting the use of Chainguard Libraries consists of the
following steps:

* Add Chainguard Libraries as a remote repository for library retrieval.
* Add any internal repositories set up by your organization.
* Add a public repository, likely PyPPI,, as a remove repository.
* Set up a virtual server or other proxy configuration such that the Chainguard Libraries repository is the first choice for any request to the virtual server (after any internal repositories). 

As part of this process, you may also wish to:

* Remove all prior cached artifacts in the virtual server or proxy public repository. This step will reduce confusion about the origin of libraries and will assist technical evaluation and adoption of Chainguard Libraries.
* Remove any repositories that are no longer desired or necessary. Depending on your library requirements, this step can result in removal of some proxy repositories or even removal of all proxy repositories. 

If your organization does not use a repository manager, you can still use Chainguard Libraries. However, this approach may require configuration of multiple build and development platforms and utilities to use Chainguard Libraries. For this reason, adopting the use of a repository manager is the recommended approach. 

<a name="cloudsmith"></a>

## Cloudsmith

[Cloudsmith](https://cloudsmith.com/) supports Python repositories for proxying and hosting and polyglot repositories that combine multiple repositories sources with compatible formats. Refer to the [Clouthsmith Python Repository documentation](https://help.cloudsmith.io/docs/python-repository) and the [Cloudsmith documentation for creating a repository](https://help.cloudsmith.io/docs/create-a-repository) for more information. 

### Initial configuration

Use the following steps to add a polyglot repository with both Chainguard Libraries and PyPI as upstream sources.

First, let's create a repository:

1. Log in as a user with administrator privileges.
1. Select the **Repositories** tab near the top of the screen.
1. Navigate to the **Repositories Overview**, then select **+ New repository**.
1. At the new repository form, enter the name *chainguard-python* for your new repository. The name should include *python* to identify the repository format. This convention helps avoid confusion, since repositories in Cloudsmith are multi-format. 
1. Select a storage region that is appropriate for your organization and infrastructure.
1. Select **+ Create Repository**. 

Next, configure an upstream proxy for the PyPI Repository:

1. Select the name of the new *chainguard-python* repository on the repositories page to configure it.
1. Access the **Upstreams** tab and click **+ Add Upstream Proxy**.
1. Configure an upstream proxy with the format **python** and the following details: 
    * **Name**: chainguard-libraries
    * **Priority**: 1
    * **Upstream URL**: https://libraries.cgr.dev/python/
    * **Mode**: Cache and Proxy
1. Configure another upstream proxy with the following details
    * **Name**: pypi
    * **Priority**: 2
    * **Upstream URL**:*https://pypi.org/
    * **Mode**: Cache and Proxy
1. Select **Create Upstream Proxy**.

### Build tool access

The following steps allow you to determine the URL and authentication details for accessing the repository:

1. Select the **Packages** tab.
1. Press **Push/Pull Packages**.
1. Choose the format **PyPI**.
1. Copy the value in the `<url>` tag from the XML snippet with the
   `<repositories>` entry. For example,
   `https://dl.cloudsmith.io/basic/exampleorg/chainguard-python/maven/` with
   `exampleorg` replaced with the name of your organization. Note that the name
   of the repository `chainguard-python` as well as `maven` as identifier for the
   format are part of the URL.
1. Copy the username and password values block from the second code snippet for
   authentication after choosing the desired authentication of *Default* or
   *API Key*.

Choose a different format and the equivalent sections if you are using another
build tools such as Gradle.

Use the URL of the repository, the username, and the password for the server
authentication block in the [build
configuration](/chainguard/libraries/python/build-configuration). and build a firs
test project. In a working setup all libraries retrieved from Chainguard are
tagged with the name of the upstream proxy.

<a name="artifactory"></a>

## JFrog Artifactory

[JFrog Artifactory](https://jfrog.com/artifactory/) supports PyPI repositories
for proxying and hosting, and virtual repositories to combine them. Refer to the
[PyPI Repository documentation for
Artifactory](https://jfrog.com/help/r/jfrog-artifactory-documentation/maven-repository)
for more information.

### Initial configuration

Use the following steps to add the PyPI Repository and the Chainguard
Libraries for Python repository as remote repositories and combine them as a
virtual repository:

1. Log in as a user with administrator privileges.
1. Press **Administration** in the top navigation bar.
1. Select **Repositories** in the left hand navigation.

Configure a remote repository for the PyPI Repository:

1. Press **Create a Repository** and choose the **Remote** option.
1. Select *PyPI* as the Package type.
1. Set the **Repository Key** to *central*.
1. Set the **URL** to *https://repo1.maven.org/maven2/* .
1. Deactivate **PyPI Settings - Handle Snapshots**.
1. Press **Create Remote Repository**.

Configure a remote repository for the Chainguard Libraries for Python repository:

1. Press **Create a Repository** and choose the **Remote** option.
1. Select *PyPI* as the **Package type**.
1. Set the **Repository Key** to *chainguard*.
1. Set the **URL** to *https://libraries.cgr.dev/maven/*.
1. Set **User Name** and **Password / Access Token** to the [values as retrieved
   with chainctl](/chainguard/libraries/access/).
1. Check the **Enable Token Authentication** checkbox.
1. Press **Test** to validate the connection.
1. Deactivate **PyPI Settings - Handle Snapshots**.
1. Press **Create Remote Repository**.

Combine the two repositories in a new virtual repository:

1. Press **Create a Repository** and choose the **Virtual** option.
1. Set the **Repository Key** to *chainguard-python*.
1. Scroll down to the **Repositories** section
1. Add the *chainguard* and *maven-central* repositories. Ensure the
   *chainguard* repository is the first in the displayed list. Use the icon on
   the right of the repository name to drag and drop repositories into the
   desired position.
1. Press **Create Virtual Repository**.

Use this setup for initial testing with Chainguard Libraries for Python. For
production usage add the `chainguard` repository to your production virtual
repository.

### Build tool access

The following steps allow you to determine the URL and authentication details
for accessing the repository:

1. Press **Administration** in the top navigation bar.
1. Select **Repositories** in the left hand navigation.
1. Select the **Virtual** tab in the repositories view.
1. Locate the *chainguard-python** repository.
1. Hover over the row and click the **...** in the last column on the right.
1. Select **Set Me Up** in the dialog.
1. Press **Generate Token & Create Instructions**
1. Copy the generated token value to use as the password for authentication.
1. Press **Generate Settings**.
1. Copy the value from a *url* field. The are all identical. For example,
   `https://exampleorg.jfrog.io/artifactory/chainguard-python` with `exampleorg`
   replaced with the name of your organization.

Use the URL of the virtual repository in the [build
configuration](/chainguard/libraries/python/build-configuration) and build a first
test project. In a working setup the chainguard remote repository contains all
libraries retrieved from Chainguard.

<a name="nexus"></a>

## Sonatype Nexus Repository

[Sonatype Nexus
Repository](https://www.sonatype.com/products/sonatype-nexus-repository)
includes a *maven-public* repository group out of the box. It groups access to
the PyPI Repository from the *maven-central* repository with the
internal *maven-releases* and *maven-snapshot* repositories. Refer to the [PyPI
Repositories documentation for
Nexus](https://help.sonatype.com/en/maven-repositories.html) for more
information.

If you are using this group, you can add a proxy repository for Chainguard
Libraries for Python repository for production use.

### Initial configuration

For initial testing and adoption it is advised to create a separate proxy
repository for the PyPI Repository, a separate proxy repository
Chainguard Libraries for Python repository, and a separate repository group:

1. Log in as a user with administrator privileges.
1. Access the **Server administration** and configuration section with the gear
   icon in the top navigation bar.

Configure a remote repository for the PyPI Repository:

1. Select **Repository - Repositories** in the left hand navigation.
1. Press **Create repository**.
1. Select the **maven2 (proxy)** recipe.
1. Provide a new name *central*.
1. Ensure **PyPI 2 - Version policy** is set to *Release*.
1. In the **Proxy - Remote storage** input add the URL *https://repo1.maven.org/maven2/*.
1. Press **Create repository**.

Configure a remote repository for the Chainguard Libraries for Python repository:

1. Select **Repository - Repositories** in the left hand navigation.
1. Press **Create repository**.
1. Select the **maven2 (proxy)** recipe.
1. Provide a new name *chainguard*.
1. Ensure **PyPI 2 - Version policy** is set to *Release*.
1. In the **Proxy - Remote storage** input add the URL *https://libraries.cgr.dev/maven/*.
1. In **HTTP - Authentication** with the **Authentication type** *username*,
   provide the [username and password values as retrieved with
   chainctl](/chainguard/libraries/access/).
1. Press **Create repository**. 

Combine a new repository group and add the two repositories:

1. Select **Repository - Repositories** in the left hand navigation.
1. Press **Create repository**.
1. Select the **maven2 (group)** recipe.
1. Provide a new name *chainguard-python*.
1. In the section **Group - Member repositories**, move the new repositories
   `central` and `chainguard` to the right and move the `chainguard` repository
   to the top of the list with the arrow control.

### Build tool access

The following steps allow you to determine the URL and authentication details
for accessing the repository:

1. Click **Browse** in the **Welcome** view or the browse icon (cube) in the top
   navigation bar.
1. Locate the **URL** column for the *chainguard-python* repository group and
   press **copy**. For example,
   `https://repo.example.com/repository/chainguard-python/`  with
   `repo.example.com` replaced with the hostname of you repository manager.
1. Copy the URL in the dialog.
1. Use your configured username and password unless **Security** - **Anonymous
   Access** - **Access** - **Allow anonymous users to access the server** is
   activated. Details vary based on your configured authentication system.

Use the URL of the repository group, such as
*https://repo.example.com/repository/chainguard-python/* or
*https://repo.example.com/repository/maven-public/* in the [build
configuration](/chainguard/libraries/python/build-configuration) and build a first
test project. In a working setup the `chainguard` proxy repository contains all
libraries retrieved frohttps://github.com/chainguard-dev/edu/pull/2148avoidm Chainguard.
