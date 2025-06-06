---
title: "Global Configuration"
linktitle: "Global Configuration  "
description: "Configuring Chainguard Libraries for Javascript in your organization"
type: "article"
date: 2025-06-05T09:00:00+00:00
lastmod: 2025-06-05T09:00:00+00:00
draft: false
tags: ["Chainguard Libraries", "Javascript"]
images: []
menu:
  docs:
    parent: "javascript"
weight: 052
toc: true
---

tbd

<a name="cloudsmith"></a>

## Cloudsmith

tbd

### Initial configuration

tbd

### Build tool access

tbd

<a name="gar"></a>

## Google Artifact Registry

tbd

### Initial configuration

tbd

### Build tool access

tbd

<a name="artifactory"></a>

## JFrog Artifactory

[JFrog Artifactory](https://jfrog.com/artifactory/) supports npm repositories
for proxying and hosting, and virtual repositories to combine them. Refer to the
[npm registry documentation for
Artifactory](https://jfrog.com/help/r/jfrog-artifactory-documentation/npm-registry)
for more information.

### Initial configuration

Use the following steps to add the Maven Central Repository and the Chainguard
Libraries for Java repository as remote repositories and combine them as a
virtual repository:

1. Log in as a user with administrator privileges.
1. Press **Administration** in the top navigation bar.
1. Select **Repositories** in the left hand navigation.

Configure a remote repository for the Maven Central Repository:

1. Press **Create a Repository** and choose the **Remote** option.
1. Select *Npm* as the Package type.
1. Set the **Repository Key** to *javascript-public*.
1. Set the **URL** to *https://registry.npmjs.org* .
1. Press **Create Remote Repository**.

Configure a remote repository for the Chainguard Libraries for Java repository:

1. Press **Create a Repository** and choose the **Remote** option.
1. Select *Npm* as the **Package type**.
1. Set the **Repository Key** to *javascript-chainguard*.
1. Set the **URL** to *https://libraries.cgr.dev/javascript/*.
1. Set **User Name** and **Password / Access Token** to the [values as retrieved
   with chainctl](/chainguard/libraries/access/).
1. Check the **Enable Token Authentication** checkbox.
1. Press **Test** to validate the connection.
1. Press **Create Remote Repository**.

Combine the two repositories in a new virtual repository:

1. Press **Create a Repository** and choose the **Virtual** option.
1. Select *Npm* as the **Package type**.
1. Set the **Repository Key** to *javascript-all*.
1. Scroll down to the **Repositories** section
1. Add the *javascript-chainguard* and *javascript-public* repositories. Ensure
   the *javascript-chainguard* repository is the first in the displayed list.
   Use the icon on the right of the repository name to drag and drop
   repositories into the desired position.
1. Press **Create Virtual Repository**.

Use this setup for initial testing with Chainguard Libraries for Java. For
production usage add the `javascript-chainguard` repository to your production virtual
repository.

### Build tool access

The following steps allow you to determine the URL and authentication details
for accessing the repository:

1. Press **Administration** in the top navigation bar.
1. Select **Repositories** in the left hand navigation.
1. Select the **Virtual** tab in the repositories view.
1. Locate the *javascript-all** repository.
1. Hover over the row and click the **...** in the last column on the right.
1. Select **Set Me Up** in the dialog.
1. Press **Generate Token & Create Instructions**
1. Copy the generated token value to use as the password for authentication.
1. Press **Generate Settings**.
1. Copy the value from a *url* field. The are all identical. For example,
   `https://exampleorg.jfrog.io/artifactory/javascript-all/` with `exampleorg`
   replaced with the name of your organization.

Use the URL of the virtual repository in the [build
configuration](/chainguard/libraries/java/build-configuration) and build a first
test project. In a working setup the chainguard remote repository contains all
libraries retrieved from Chainguard.

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
Libraries for Javascript repository, and a separate repository group:

1. Log in as a user with administrator privileges.
1. Access the **Server administration** and configuration section with the gear
   icon in the top navigation bar.

Configure a remote repository for the Maven Central Repository:

1. Select **Repository - Repositories** in the left hand navigation.
1. Press **Create repository**.
1. Select the **npm (proxy)** recipe.
1. Provide a new name *javascript-public*.
1. In the **Proxy - Remote storage** input add the URL *https://registry.npmjs.org/*.
1. Press **Create repository**.

Configure a remote repository for the Chainguard Libraries for Javascript repository:

1. Select **Repository - Repositories** in the left hand navigation.
1. Press **Create repository**.
1. Select the **npm (proxy)** recipe.
1. Provide a new name *javascript-chainguard*.
1. In the **Proxy - Remote storage** input add the URL *https://libraries.cgr.dev/javascript/*.
1. In **HTTP - Authentication** with the **Authentication type** *username*,
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
configuration](/chainguard/libraries/javascript/build-configuration) and build a
first test project. In a working setup the `javascript-chainguard` proxy
repository contains all libraries retrieved from Chainguard.
