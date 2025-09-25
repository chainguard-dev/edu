---
title: "Global Configuration"
linktitle: "Global Configuration  "
description: "Configuring Chainguard Libraries for JavaScript in your organization"
type: "article"
date: 2025-06-05T09:00:00+00:00
lastmod: 2025-06-05T09:00:00+00:00
draft: false
tags: ["Chainguard Libraries", "JavaScript"]
images: []
menu:
  docs:
    parent: "javascript"
weight: 052
toc: true
---

JavaScript and npm package consumption in a large organization is typically
managed by a repository manager. Commonly used repository manager applications
are [JFrog Artifactory](https://jfrog.com/artifactory/), [Sonatype Nexus
Repository](https://www.sonatype.com/products/sonatype-nexus-repository), and
others. The repository manager acts as a single point of access for developers
and development tools to retrieve the required libraries.

At a high level, adopting the use of Chainguard Libraries consists of the
following steps:

* Add the Chainguard Libraries for JavaScript registry as a remote repository
  for library retrieval.
* Configure the repository as the first choice for any library access. This
  ensures that any future requests of new libraries access the version supplied
  by Chainguard. Typically this is accomplished by creating a group repository
  or virtual repository that combines the repository with other external and
  internal repositories.

Additional steps depend on the desired insights and can include the following
optional measures:

* Remove all cached libraries in the proxy repository of the npm Registry. This
  step allows you to validate which libraries are not available from Chainguard
  Libraries and proceed with potential next steps with Chainguard and your own
  development efforts. 
* Remove any repositories that are no longer desired or necessary. Depending on
  your library requirements this step can result in removal of some proxy
  repositories or even removal of all proxy repositories. 

Adopting the use of a repository manager is the recommended approach, however if
your organization does not use a repository manager, you can still use
Chainguard Libraries. All access to the Chainguard Libraries repository is then
distributed across all your build platforms and therefore more complex to
configure and control. Refer to the [direct access documentation for build
tools](/chainguard/libraries/javascript/build-configuration/#direct-access) for more
information.

<a name="cloudsmith"></a>

## Cloudsmith

[Cloudsmith](https://cloudsmith.com/) supports npm registries repositories for
proxying and hosting. Refer to the [npm registry
documentation](https://help.cloudsmith.io/docs/npm-registry) and the [npm
Upstream
documentation](https://help.cloudsmith.io/docs/upstream-proxying-caching#create-a-npm-upstream)
for Cloudsmith for more information. Cloudsmith supports combining repositories
by defining multiple upstream repositories.

### Initial configuration

Use the following steps to add a repository with the npm registry and the
Chainguard Libraries for JavaScript repository as npm upstream repositories.

Configure a *javascript-all* repository:

1. Log in as a user with administrator privileges.
1. Select the **Repositories** tab near the top of the screen.
1. On the **Repositories** page, click the **+ New repository** button.
1. Enter the name *javascript-all* for your new repository. The name should
   include *javascript* to identify the ecosystem. This convention helps
   avoid confusion since repositories in Cloudsmith are multi-format.
1. Select a storage region that is appropriate for your organization and
   infrastructure.
1. Press **+ Create Repository**.

Configure an upstream proxy for the npm registry:

1. Click the name of the new *javascript-all* repository on the repositories
   page to configure it.
1. Access the **Upstreams** tab and click **+ Add Upstream Proxy**.
1. Configure an upstream proxy with the format **npm** and the following details:
1. Configure another upstream proxy with the following details
    * **Name** *javascript-public*
    * **Priority** *2*
    * **Upstream URL** *https://registry.npmjs.org/*
    * **Mode** *Cache and Proxy*
1. Press **Create Upstream Proxy**.

Configure an upstream proxy for the Chainguard Libraries for JavaScript
repository:

1. Click the name of the new *javascript-chainguard* repository on the
   repositories page to configure it.
1. Access the **Upstreams** tab and click **+ Add Upstream Proxy**.
1. Configure an upstream proxy with the format **npm** and the following details:
    * **Name** *javascript-chainguard*
    * **Priority** *1*
    * **Proxy URL** *https://libraries.cgr.dev/javascript/*
    * **Mode** *Cache and Proxy*
    * Add the **Username** and **Password** value from [Chainguard Libraries
      access](/chainguard/libraries/access/) in **Authentication Settings**
1. Press **Create Upstream Proxy**.

Use this setup for initial testing with Chainguard Libraries for JavaScript. For
production usage, add the `javascript-chainguard` upstream proxy to your production
repository.

### Build tool access

The following steps allow you to determine the URL and authentication details
for accessing the repository:

1. Select the **Packages** tab.
1. Press **Push/Pull Packages**.
1. Choose the format **NPM**.
1. Refer to the **Pull Package** tab.
1. Note the registry URL and syntax from the code snippets for npm. For example,
   the URL for the registry in the `example` organization is
   `https://npm.cloudsmith.io/example/javascript-all/`.
1. Note that authentication is using an authentication token and the syntax for
   npm in the `example` organization is
   `//npm.cloudsmith.io/example/javascript-all/:_authToken=YOUR-API-KEY`

Use the provided code snippets directly for your use with npm, or adjust as
necessary for other JavaScript build and packaging tools. Find relevant details
in the [Build
Configuration](/chainguard/libraries/javascript/build-configuration/) and
specific packaging tool documentation.

Use the following steps to retrieve the necessary API key as an authentication
token for the registry access:

1. Click on your user name at the top, right corner. 
1. Select *Personal API keys**.
1. Authenticate again in the **Confirm access** dialog.
1. Create a new token or refresh the existing one in case you lost the token
   value.

<a name="artifactory"></a>

## JFrog Artifactory

[JFrog Artifactory](https://jfrog.com/artifactory/) supports npm repositories
for proxying and hosting, and virtual repositories to combine them. Refer to the
[npm registry documentation for
Artifactory](https://jfrog.com/help/r/jfrog-artifactory-documentation/npm-registry)
for more information.

### Initial configuration

Use the following steps to add the npm Registry and the Chainguard Libraries for
JavaScript repository as remote repositories and combine them as a virtual
repository:

1. Log in as a user with administrator privileges.
1. Press **Administration** in the top navigation bar.
1. Select **Repositories** in the left hand navigation.

Configure a remote repository for the npm Registry:

1. Press **Create a Repository** and choose the **Remote** option.
1. Select **Npm** as the **Package type**.
1. Set the **Repository Key** to *javascript-public*.
1. Set the **URL** to *https://registry.npmjs.org* .
1. Press **Create Remote Repository**.

Configure a remote repository for the Chainguard Libraries for JavaScript
repository:

1. Press **Create a Repository** and choose the **Remote** option.
1. Select *Npm* as the **Package type**.
1. Set the **Repository Key** to *javascript-chainguard*.
1. Set the **URL** to *https://libraries.cgr.dev/javascript/*.
1. Set **User Name** and **Password / Access Token** to the [values as retrieved
   with chainctl](/chainguard/libraries/access/).
1. Press **Create Remote Repository**.

Combine the two repositories in a new virtual repository:

1. Press **Create a Repository** and choose the **Virtual** option.
1. Select **Npm** as the **Package type**.
1. Set the **Repository Key** to *javascript-all*.
1. Scroll down to the **Repositories** section.
1. Add the *javascript-chainguard* and *javascript-public* repositories. Ensure
   the *javascript-chainguard* repository is the first in the displayed list.
   Use the icon on the right of the repository name to drag and drop
   repositories into the desired position.
1. Press **Create Virtual Repository**.

Use this setup for initial testing with Chainguard Libraries for JavaScript. For
production usage add the `javascript-chainguard` repository to your production
virtual repository.

### Build tool access

The following steps allow you to determine the URL and authentication details
for accessing the repository:

1. Press **Administration** in the top navigation bar.
1. Select **Repositories** in the left hand navigation.
1. Select the **Virtual** tab in the repositories view.
1. Locate the *javascript-all* repository.
1. Hover over the row and click the **...** in the last column on the right.
1. Select **Set Me Up** in the dialog.
1. Press **Generate Token & Create Instructions**.
1. Copy the generated token value to use as the password for authentication.
1. Press **Generate Settings**.
1. Copy the value from a **url** field. The are all identical. For example,
   `https://exampleorg.jfrog.io/artifactory/javascript-all/` with `exampleorg`
   replaced with the name of your organization.

Use the URL of the virtual repository in the [build
configuration](/chainguard/libraries/javascript/build-configuration/) and build a
first test project. In a working setup the chainguard remote repository contains
all libraries retrieved from Chainguard.

<a name="nexus"></a>

## Sonatype Nexus Repository

[Sonatype Nexus
Repository](https://www.sonatype.com/products/sonatype-nexus-repository) allows
for merging multiple remote repositories as a repository group. The below
instructions for  are based on the [Nexus documentation for
npm](https://help.sonatype.com/en/npm-registry.html).

### Initial configuration

For initial testing and adoption it is advised to create a separate proxy
repository for the npm registry, a separate proxy repository Chainguard
Libraries for JavaScript repository, and a separate repository group:

1. Log in as a user with administrator privileges.
1. Access the **Server administration** and configuration section with the gear
   icon in the top navigation bar.

Configure a remote repository for the npm Registry:

1. Select **Repository - Repositories** in the left hand navigation.
1. Press **Create repository**.
1. Select the **npm (proxy)** recipe.
1. Provide a new name *javascript-public*.
1. In the **Proxy - Remote storage** input add the URL
   *https://registry.npmjs.org/*.
1. Press **Create repository**.

Configure a remote repository for the Chainguard Libraries for JavaScript
repository:

1. Select **Repository - Repositories** in the left hand navigation.
1. Press **Create repository**.
1. Select the **npm (proxy)** recipe.
1. Provide a new name *javascript-chainguard*.
1. In the **Proxy - Remote storage** input add the URL
   *https://libraries.cgr.dev/javascript/*.
1. In **HTTP - Authentication** with the **Authentication type** *Username*,
   provide the [username and password values as retrieved with
   chainctl](/chainguard/libraries/access/).
1. Press **Create repository**. 

Combine a new repository group and add the two repositories:

1. Select **Repository - Repositories** in the left hand navigation.
1. Press **Create repository**.
1. Select the **npm (group)** recipe.
1. Provide a new name *javascript-all*.
1. In the section **Group - Member repositories**, move the new repositories
   `javascript-public` and `javascript-chainguard` to the right and move the
   `javascript-chainguard` repository to the top of the list with the arrow
   control.

### Build tool access

The following steps allow you to determine the URL and authentication details
for accessing the repository:

1. Click **Browse** in the **Welcome** view or the browse icon (cube) in the top
   navigation bar.
1. Locate the **URL** column for the *javascript-all* repository group and press
   **copy**. For example, `https://repo.example.com/repository/javascript-all/`
   with `repo.example.com` replaced with the hostname of you repository manager.
1. Copy the URL in the dialog.
1. Use your configured username and password unless **Security** - **Anonymous
   Access** - **Access** - **Allow anonymous users to access the server** is
   activated. Details vary based on your configured authentication system.

Use the URL of the repository group, such as
*https://repo.example.com/repository/javascript-all/* in the [build
configuration](/chainguard/libraries/javascript/build-configuration/) and build a
first test project. In a working setup the `javascript-chainguard` proxy
repository contains all libraries retrieved from Chainguard.
