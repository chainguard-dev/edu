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

Python library consumption in a large organization is typically managed by a repository manager. Commonly used repository manager applications are [Cloudsmith](https://cloudsmith.com/), [JFrog Artifactory](https://jfrog.com/artifactory/), and [Sonatype Nexus Repository](https://www.sonatype.com/products/sonatype-nexus-repository). The repository manager acts as a single point of access for developers and development tools to retrieve the required libraries.

At a high level, adopting the use of Chainguard Libraries consists of the following steps:

* Add Chainguard Libraries as a remote repository for library retrieval.
* Add the public [PyPI](https://pypi.org/) repository as a remote repository.
* Create a group, virtual, or polyglot repository combining these repository sources with any desired internal repositories. Configure the Chainguard Libraries repository as the first choice for any library access after any desired internal repositories.

You should also:

* Remove all prior cached artifacts in the virtual server or proxy public repository. This step reduces confusion about the origin of libraries and assists technical evaluation and adoption of Chainguard Libraries.
* Remove any repositories that are no longer desired or necessary. Depending on your library requirements, this step can result in removal of some proxy repositories or even removal of all proxy repositories. 

If your organization does not use a repository manager, you can still use Chainguard Libraries. However, this approach requires configuration of multiple build and development platforms and utilities to use Chainguard Libraries. For this reason, adopting the use of a repository manager is the recommended approach. 

<a id="cloudsmith"></a>

## Cloudsmith

[Cloudsmith](https://cloudsmith.com/) supports Python repositories for proxying and hosting and polyglot repositories that combine multiple repositories sources with compatible formats. Refer to the [Cloudsmith Python Repository documentation](https://help.cloudsmith.io/docs/python-repository) and the [Cloudsmith documentation for creating a repository](https://help.cloudsmith.io/docs/create-a-repository) for more information. 

### Initial configuration

Use the following steps to add a repository with both Chainguard Libraries for
Python and PyPI as upstream sources.

First, create a repository:

1. Log in to your Cloudsmith instance as user with administrator privileges.
1. Select the **Repositories** tab near the top of the screen.
1. Navigate to the **Repositories Overview**, then select **+ New repository**.
1. At the new repository form, enter the name *python-all* for your new
   repository. The name should include *python* to identify the repository
   format. This convention helps avoid confusion, since repositories in
   Cloudsmith are multi-format. 
1. Select a storage region that is appropriate for your organization and infrastructure.
1. Select **+ Create Repository**. 

Next, configure the upstream proxies:

1. Select the name of the new *python-all* repository on the repositories page
   to configure it.
1. Access the **Upstreams** tab and click **+ Add Upstream Proxy**.
1. Configure an upstream proxy with the format **python** and the following details: 
    * **Name**: `python-chainguard`
    * **Priority**: `1`
    * **Upstream URL**: `https://libraries.cgr.dev/python/`
    * **Mode**: `Cache and Proxy`
1. Select **Create Upstream Proxy**.
1. Configure another upstream proxy with the following details
    * **Name**: `python-public`
    * **Priority**: `2`
    * **Upstream URL**: `https://pypi.org/`
    * **Mode**: `Cache and Proxy`
1. Select **Create Upstream Proxy**.

### Build tool access

See the page on [build tool configuration for Chainguard Libraries for
Python](/chainguard/libraries/python/build-configuration/#cloudsmith) for information on
accessing credentials and setting up build tools.

<a id="artifactory"></a>

## JFrog Artifactory

[JFrog Artifactory](https://jfrog.com/artifactory/) supports PyPI repositories for proxying and virtual repositories to combine multiple sources into a single repository. The following instructions are based on on the [PyPI Repository documentation for Artifactory](https://jfrog.com/help/r/jfrog-artifactory-documentation/set-up-pypi-repositories-on-artifactory).

### Initial configuration

Use the following steps to add the Chainguard Libraries for Python index and the
PyPI public index as remote repositories and combine them as a virtual
repository:

1. Log in as a user with administrator privileges.
1. Press **Administration** in the top navigation bar.
1. Select **Repositories** in the left hand navigation.

Configure a remote repository for the Chainguard Libraries for Python index:

1. Select **Create a Repository** and choose the **Remote** option.
1. Select *PyPI* as the **Package type**.
1. Set the **Repository Key** to `python-chainguard`.
1. Set the **URL** to `https://libraries.cgr.dev/python/`.
1. Set **User Name** and **Password / Access Token** to the [values as retrieved
   with chainctl](/chainguard/libraries/access/).
1. Check the **Enable Token Authentication** checkbox.
1. Set the **Pypi Settings - Registry URL** to `https://libraries.cgr.dev/python/`.
1. Press **Create Remote Repository**.

Configure a remote repository for the PyPI public index:

1. Select **Create a Repository** and choose the **Remote** option.
1. Select *PyPI* as the Package type.
1. Set the **Repository Key** to `python-public`.
1. Set the **URL** to `https://files.pythonhosted.org`.
1. Set the **Pypi Settings - Registry URL** to `https://pypi.org/`.
1. Select **Create Remote Repository**.

Combine the two repositories in a new virtual repository:

1. Press **Create a Repository** and choose the **Virtual** option.
1. Set the **Repository Key** to `python-all`.
1. In the **Repositories** section, find the `python-chainguard` and
   `python-public` repositories. Ensure the `python-chainguard` repository is
   the first in the displayed list. Use the icon on the right of the repository
   name to drag and drop repositories into the desired position.
1. Select **Create Virtual Repository**.

### Build tool access

See the page on [build tool configuration for Chainguard Libraries for
Python](/chainguard/libraries/python/build-configuration/#artifactory) for
information on accessing credentials and setting up build tools.

<a id="nexus"></a>

## Sonatype Nexus Repository

[Sonatype Nexus Repository](https://www.sonatype.com/products/sonatype-nexus-repository) allows for merging multiple remote repositories as a repository group. The below instructions for  are based on the [Nexus documentation for PyPI](https://help.sonatype.com/en/pypi-repositories.html) 

### Initial configuration

The following steps create remote repositories for Chainguard Libraries for
Python, a remote repository for the public PyPI index, and a repository group
combining these sources.

First, log in to Sonatype Nexus as a user with administrator privileges and access the **Server administration** and configuration section within the gear icon in the top navigation bar.

Next, configure a remote repository for the public PyPI index:

1. Select **Repository - Repositories** in the left hand navigation.
1. Select **Create repository**.
1. Select the **PyPI (proxy)** recipe.
1. Provide a new name, such as `python-public`.
1. In the **Proxy - Remote storage** field, add the following URL: `https://pypi.org/`.
1. Select **Create repository**.

Configure a remote repository for the Chainguard Libraries for Python repository:

1. Select **Repository - Repositories** in the left hand navigation.
1. Select **Create repository**.
1. Select the **PyPI (proxy)** recipe.
1. Provide a new name, such as `python-chainguard`.
1. In the **Proxy - Remote storage**field, add the following URL: `https://libraries.cgr.dev/python/`.
1. In **HTTP - Authentication**, set the **Authentication type** to *username* and enter the the [username and password values as retrieved with chainctl](/chainguard/libraries/access/).
1. Select **Create repository**. 

Finally, create a new repository group and add the two repositories:

1. Select **Repository - Repositories** in the left hand navigation.
1. Select **Create repository**.
1. Select the **PyPI (group)** recipe.
1. Provide a new name, such as `python-all`.
1. In the section **Group - Member repositories**, move the new repositories
   `python-public` and `python-chainguard` to the right and move the
   `python-chainguard` repository to the top of the list with the arrow control.

### Build tool access

See the page on [build tool configuration for Chainguard Libraries for
Python](/chainguard/libraries/python/build-configuration/#nexus) for information on
accessing credentials and setting up build tools.
