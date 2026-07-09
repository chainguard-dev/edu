---
title: "Global configuration"
linktitle: "Global configuration"
description: "Configuring Chainguard Libraries for Java in your organization"
type: "article"
date: 2025-03-25T08:04:00+00:00
lastmod: 2026-06-24T14:42:00+00:00
draft: false
tags: ["Chainguard Libraries", "Java"]
images: []
menu:
  docs:
    parent: "java"
    identifier: "Java Global Configuration"
weight: 052
toc: true
---

Java and JVM library consumption in a large organization is typically managed by
a repository manager. Commonly used repository manager applications are
[Cloudsmith](https://cloudsmith.com/), [Google Artifact Registry](https://cloud.google.com/artifact-registry/docs), [JFrog
Artifactory](https://jfrog.com/artifactory/), and [Sonatype Nexus
Repository](https://www.sonatype.com/products/sonatype-nexus-repository). The
repository manager acts as a single point of access for developers and
development tools to retrieve the required libraries.

The recommended approach is to use the [upstream
fallback](/chainguard/libraries/overview/#upstream-fallback-and-controls)
feature of Chainguard Repository, which allows you to configure your repository
manager with a single upstream pointed at `https://libraries.cgr.dev/java/`. The
Chainguard Repository handles fallback and policy enforcement; your repository
manager handles local caching and access control. Chainguard also retrieves
packages from the public Maven Central repository on your behalf when upstream
fallback is enabled. This includes protections such as malware scanning and a
cooldown period for newly published packages.

At a high level, adopting the use of Chainguard Libraries consists of the following steps:

* Configure your environment to use `https://libraries.cgr.dev/java/`
  as the single upstream source for Java package retrieval. This can be done
  either:
    * As a remote repository in your repository manager, or
    * Directly in your Java build configuration (for example, Maven or Gradle).
* Additional steps depend on your specific environment and preferences, and can include the following
optional measures:
    * Remove all cached artifacts for Maven Central. This step ensures that any libraries you pull are from Chainguard Libraries, and not existing cached artifacts from upstream. 
    * Remove any repositories that are no longer desired or necessary, depending on your organization's preferences. 

This page explains how to use Chainguard Libraries for Java with a repository
manager. If your organization does not use a repository manager, you can pull
directly from Chainguard. Refer to the [direct access documentation for build
tools](/chainguard/libraries/java/build-configuration/#direct-access) for more
information.

### Manually managing fallback
Chainguard recommends using the Chainguard Repository's built-in [upstream
fallback](/chainguard/libraries/overview/#upstream-fallback-and-controls) rather
than configuring a public registry fallback in your repo manager. Configuring
your own fallback bypasses the protection that the Chainguard Repository
provides.

However, if you intentionally want to manage fallback ordering yourself, you can
configure `https://libraries.cgr.dev/java/` as a remote repository alongside
your Maven upstream, and combine them in a virtual or group repository with
Chainguard as the first priority. The per-tool instructions on this page follow
this pattern. If you configure a fallback to Maven Central, packages sourced
from that registry are not covered by Chainguard's malware-resistance
guarantees. 

<a name="cloudsmith"></a>

## Cloudsmith

[Cloudsmith](https://cloudsmith.com/) supports Maven repositories for proxying
and hosting. Refer to the [Maven Repository
documentation](https://help.cloudsmith.io/docs/maven-repository) and the [Maven
Upstream
documentation](https://help.cloudsmith.io/docs/upstream-proxying-caching#create-a-maven-upstream)
for Cloudsmith for more information. Cloudsmith supports combining repositories
by defining multiple upstream repositories.

### Initial configuration

Use the following steps to set up a repository in Cloudsmith to access Chainguard Java Libraries via the Chainguard Repository. 

Configure a `java-all` repository:

1. Log in as a user with administrator privileges.
1. Select the **Repositories** tab near the top of the screen.
1. On the **Repositories** page, click the **+ New repository** button.
1. Enter the name `java-all` for your new repository. The name should
   include `java` to identify the ecosystem. This convention helps
   avoid confusion since repositories in Cloudsmith are multi-format. 
1. Select a storage region that is appropriate for your organization and
   infrastructure.
1. Click **+Create Repository**. 

Configure an upstream proxy for the Chainguard Libraries for Java repository:

1. Click the name of the new `java-chainguard` repository on the repositories
   page to configure it.
1. Click the **Upstreams** tab, then click **+Add Upstream Proxy**.
1. Configure an upstream proxy with the format **Maven** and the following details:
    * **Name**: `java-chainguard`
    * **Priority**: `1`
    * **Proxy URL**: `https://libraries.cgr.dev/java/`
    * **Mode**: Cache and Proxy
    * **Authentication Settings**: Enter the **Username** and **Password** value from [Chainguard Libraries
      access](/chainguard/libraries/access/).
1. Click **Create Upstream Proxy**.
1. If you are using the separate repository with remediated Java libraries, repeat the preceding steps to create remote repository named `java-chainguard-remediated` with a URL set to `https://libraries.cgr.dev/java-remediated/`. Use the same authentication details.

If you are manually configuring fallback, you can add an additional upstream proxy for the public Maven Central repository with a lower priority than `java-chainguard`.

Use this setup for initial testing with Chainguard Libraries for Java. For
production usage, add the `java-chainguard` upstream proxy to your production
repository.

### Build tool access

The following steps allow you to determine the URL and authentication details
for accessing the repository:

1. Select the **Packages** tab.
1. Click **Push/Pull Packages**.
1. Choose the format **Maven**.
1. Copy the value in the `<url>` tag from the XML snippet with the
   `<repositories>` entry. For example,
   `https://dl.cloudsmith.io/basic/exampleorg/java-all/maven/` with `exampleorg`
   replaced with the name of your organization. Note that the name of the
   repository `java-all` as well as `maven` as identifier for the format are
   part of the URL.
1. Copy the username and password values block from the second code snippet for
   authentication after choosing the desired authentication of **Default** or
   **API Key**.

Choose a different format and the equivalent sections if you are using another
build tools such as Gradle.

Use the URL of the repository, the username, and the password for the server
authentication block in the [build
configuration](/chainguard/libraries/java/build-configuration/) and build a
first test project. In a working setup, all libraries retrieved from Chainguard
are tagged with the name of the upstream proxy.

<a name="gar"></a>

## Google Artifact Registry

[Google Artifact Registry (GAR)](https://cloud.google.com/artifact-registry) supports
the Maven format for hosting artifacts in **Standard** repositories and proxying
artifacts from public repositories in **Remote** repositories. Use **Virtual**
repositories to combine them for consumption with Maven and other build tools.
Use the [Java package documentation for Google Artifact
Registry](https://cloud.google.com/artifact-registry/docs/java) as the starting
point for more details.

### Initial configuration

Use the following steps to set up a repository in GAR to access Chainguard Java Libraries via the Chainguard Repository. 

1. Log in to the Google Cloud console as a user with administrator privileges.
1. Navigate to your project and find the **Artifact Registry** with the search.
1. Activate Artifact Registry if necessary.
1. Navigate to your project and find the **Secret Manager** with the search.
1. Activate **Secret Manager** if necessary.

Before configuring the repositories, you must create a secret with the [password
value as retrieved with chainctl](/chainguard/libraries/access/):

1. Navigate to the **Secret Manager**
1. Click **Create secret**. 
1. Set the **Name** to `chainguard-libraries-java`.
1. Set the **Secret** value to the password from your `chainctl` output.
1. Click **Create secret**.

Navigate to Artifact Registry. In the left hand navigation under Artifact Registry, select **Repositories**. Configure a remote
repository for Chainguard Libraries for Java:

1. Click **Create a Repository** (or the **+** button).
1. Configure the repository:
    * **Name**: `java-chainguard`
    * **Format**: `Maven`
    * **Mode**: Remote
    * **Remote repository source**: Custom
    * **Custom repository URL**: `https://libraries.cgr.dev/java/`
    * **Remote repository authentication mode**: Authenticated
    * **Username for the upstream repository**: Set this to the [value as retrieved
   with chainctl](/chainguard/libraries/access/).
    * **Secret**: Select the `chainguard-libraries-java` secret in the list.
    * **Location type > Region**: Select the same region configured for your `java-public` repository.
1. Click **Create**.
1. If you are using the separate repository with remediated Java libraries, repeat the preceding steps to create remote repository named `java-chainguard-remediated` with a URL set to `https://libraries.cgr.dev/java-remediated/`. Use the same authentication details.

If you are manually managing fallback, you can configure an additional remote repository for the public Maven Central with lower priority.

Combine the repositories in a new virtual repository:

1. Click the **+** button to add another repository.
1. Configure the repository:
    * **Name**: `java-all`
    * **Format**: Maven
    * **Mode**: Virtual
1. Under **Virtual upstream repositories**, click **Add upstream repository**.
1. Use the **Browse** button to locate and select the `java-chainguard`
   repository as **Repository 1** and set the **Policy name 1** to
   `java-chainguard`. 
1. If you are using the remediated repository or manually configuring fallback to the public Maven repository, use the **Browse** button to locate and select each repository. 
1. Under **Virtual upstream repositories**, click **Add upstream repository**.
1. Set the **Priority** values for the repositories. The priority order should be: `java-chainguard-remediated`, `java-chainguard`, then if you are manually configuring fallback to public Maven, `java-public` last. 
1. Under **Location type**, choose the same suitable **Region** for your development as configured for the `java-public` repository.
1. Click **Create**.

### Build tool access

The following steps allow you to configure your build tool for accessing the
repository:

1. Navigate to Artifact Registry and select **Repositories** in the left hand
   navigation under the **Artifact Registry** label.
1. Click the `java-all` repository name in the list of repositories.
1. Click **Setup instructions** and follow the documentation. Note
   that you must add the extension
   `com.google.cloud.artifactregistry:artifactregistry-maven-wagon` to each
   project.

In a working setup, the `chainguard` remote repository contains all artifacts
retrieved from Chainguard.

<a name="artifactory"></a>

## JFrog Artifactory

[JFrog Artifactory](https://jfrog.com/artifactory/) supports Maven repositories
for proxying and hosting, and virtual repositories to combine them. Refer to the
[Maven Repository documentation for
Artifactory](https://docs.jfrog.com/artifactory/docs/maven-repositories)
for more information.

### Initial configuration

Use the following steps to set up a repository in Artifactory to access Chainguard Java Libraries via the Chainguard Repository. 

1. Log in as a user with administrator privileges.
1. Click **Administration** in the top navigation bar.
1. Select **Repositories** in the left hand navigation.

Configure a remote repository for the Chainguard Libraries for Java repository:

1. Click **Create a Repository** and choose the **Remote** option.
1. Configure the repository:
    * **Package type**: Maven
    * **Repository Key**: `java-chainguard`
    * **URL**: `https://libraries.cgr.dev/java/`
    * **User Name** and **Password / Access Token**: Set to the [values as retrieved with chainctl](/chainguard/libraries/access/).
    * Deactivate **Maven Settings - Handle Snapshots**.
1. Optionally click **Test** to verify connection and authentication.
1. Click the **Advanced** configuration tab. In the **Others** section, check the box next to **Disable URL Normalization** and uncheck the box next to **Block Mismatching Mime Types**.
1. Click **Create Remote Repository**.
1. If you are using the separate repository with remediated Java libraries, repeat the preceding steps to create remote repository named `java-chainguard-remediated` with a URL set to `https://libraries.cgr.dev/java-remediated/`. Use the same authentication details.

If you are manually managing fallback, you can configure an additional remote repository for Maven Central with lower priority. Make sure to deactivate **Maven Settings - Handle Snapshots** in the remote repository.

Combine the repositories in a new virtual repository:

1. Click **Create a Repository** and choose the **Virtual** option.
1. Configure the repository:
    * **Package type**: Maven
    * **Repository Key**: `java-all`
1. Scroll down to the **Repositories** section.
1. Add the `java-chainguard` and `java-public` repositories. Drag and drop repositories into the
   desired position.
    * If you are using the remediated repository, add the `java-chainguard-remediated` repository and ensure it is the first in the displayed list. If not, ensure the `java-chainguard` repository is first. 
1. Click **Create Virtual Repository**.

Use this setup for initial testing with Chainguard Libraries for Java. For
production usage add the `java-chainguard` repository to your production virtual
repository.

### Validate the remote repository

After creating the `java-chainguard` remote repository, validate that Artifactory is successfully proxying through to Chainguard before proceeding. Because Artifactory falls back to Maven Central when a connection to a remote repository fails, a misconfigured repository may silently resolve packages from Mavel Central rather than Chainguard — and the build will succeed without any visible error.

Common sources of misconfiguration include invalid or expired credentials, or an incorrect or incomplete repository URL. The Artifactory **Test** button on the repository configuration screen is not a reliable indicator; it may fail for a correctly configured repository, and may pass for an incorrectly configured one. Instead, use the following steps to verify that fetching an artifact through Artifactory produces the same checksum as fetching it directly from `libraries.cgr.dev`.

1. Fetch the artifact directly from Chainguard and compute its checksum. This example uses `junit-4.13.2.jar`. You can substitute any artifact you know to be available.

```bash
curl -sSf -L \
  -u "${CHAINGUARD_JAVA_IDENTITY_ID}:${CHAINGUARD_JAVA_TOKEN}" \
  https://libraries.cgr.dev/java/junit/junit/4.13.2/junit-4.13.2.jar \
  | sha256sum
```

2. Fetch the same artifact through the Artifactory remote repository and compute its checksum:

```bash
curl -sSf -L \
  -u "${ARTIFACTORY_USER}:${ARTIFACTORY_TOKEN}" \
  https://<artifactory-host>/artifactory/java-chainguard/junit/junit/4.13.2/junit-4.13.2.jar \
  | sha256sum
```
Replace `artifactory-host` with your Artifactory instance hostname.

The checksums returned by the commands must match. 

If the checksum from the Artifactory remote repository differs from the direct fetch, or if the Artifactory fetch fails entirely, review the following before proceeding:

* URL: The remote repository URL must be set to `https://libraries.cgr.dev/java/`. 
* Credentials: You may need to regenerate your pull token with `chainctl auth pull-token --repository=java` and update the Artifactory repository credentials. Expired tokens fail silently.
* Advanced configuration: Ensure all recommended Advanced settings from the [remote repository configuration steps](#initial-configuration-2) have been applied.

Do not proceed to virtual repository setup or build configuration until the checksums match.

### Build tool access

The following steps allow you to determine the URL and authentication details
for accessing the repository:

1. Click **Administration** in the top navigation bar.
1. Select **Repositories** in the left hand navigation.
1. Select the **Virtual** tab in the repositories view.
1. Locate the `chainguard-maven` repository.
1. Hover over the row and click the **...** in the last column on the right.
1. Select **Set Me Up** in the dialog.
1. Click **Generate Token & Create Instructions**.
1. Copy the generated token value to use as the password for authentication.
1. Click **Generate Settings**.
1. Copy the value from a **url** field. They are all identical. For example,
   `https://exampleorg.jfrog.io/artifactory/java-all/` with `exampleorg`
   replaced with the name of your organization.

Use the URL of the virtual repository in the [build
configuration](/chainguard/libraries/java/build-configuration/) and build a 
first test project. In a working setup the chainguard remote repository contains 
all libraries retrieved from Chainguard.

<a name="nexus"></a>

## Sonatype Nexus Repository

[Sonatype Nexus
Repository](https://www.sonatype.com/products/sonatype-nexus-repository)
includes a `maven-public` repository group out of the box. It groups access to
the Maven Central Repository from the `maven-central` repository with the
internal `maven-releases` and `maven-snapshot` repositories. Refer to the [Maven
Repositories documentation for
Nexus](https://help.sonatype.com/en/maven-repositories.html) for more
information.

If you are using this group, you can add a proxy repository for Chainguard
Libraries for Java repository for production use.

### Initial configuration

Use the following steps to set up a repository in Sonatype Nexus to access Chainguard Java Libraries via the Chainguard Repository. 

If you are configuring your own fallback in your repo manager, for initial testing it is advised to create a separate proxy
repository for the Maven Central Repository, a separate proxy repository
Chainguard Libraries for Java repository, and a separate repository group.

1. Log in as a user with administrator privileges.
1. Click the gear icon in the top navigation bar to access **Server administration**.

Configure a remote repository for the Chainguard Libraries for Java repository:

1. Select **Repository - Repositories** in the left hand navigation.
1. Click **Create repository**, then select the `maven2 (proxy)` recipe.
1. Configure the repository:
    * **Name**: `java-chainguard`
    * **Maven 2 - Version policy**: `Release`.
    * **Proxy - Remote storage**: Add the URL `https://libraries.cgr.dev/java/`
    * **HTTP - Authentication** Select the `username` **Authentication type**, and
   provide the [username and password values as retrieved with
   chainctl](/chainguard/libraries/access/).
1. Click **Create repository**. 
1. If you are using the separate repository with remediated Java libraries, repeat the preceding steps to create remote repository named `java-chainguard-remediated` with a URL set to `https://libraries.cgr.dev/java-remediated/`. Use the same authentication details.

If you are manually managing fallback, you can configure an additional `java-public` remote repository for Maven Central with lower priority.

Combine a new repository group and add the repositories:

1. Select **Repository - Repositories** in the left hand navigation.
1. Click **Create repository**, then select the `maven2 (group)` recipe.
1. Configure the repository:
    * **Name**: `java-all`
    * Under **Group - Member repositories**, move the new repositories
   `java-public` and `java-chainguard` to the right. Move the
   `java-chainguard` repository to the top of the list with the arrow control. If you are using the remediated repository, move the `java-chainguard-remediated` repository to the top.

### Build tool access

The following steps allow you to determine the URL and authentication details
for accessing the repository:

1. Click **Browse** in the **Welcome** view or the browse icon (cube) in the top
   navigation bar.
1. Locate the **URL** column for the `java-all` repository group and click
   **Copy**. 
     * For example, `https://repo.example.com/repository/java-all/` (with
   `repo.example.com` replaced with the hostname of your repository manager).
1. Use your configured username and password, unless **Security > Anonymous
   Access > Access > Allow anonymous users to access the server** is
   activated. Details vary based on your configured authentication system.

Use the URL of the repository group, such as
`https://repo.example.com/repository/java-all/` or
`https://repo.example.com/repository/maven-public/` in the [build
configuration](/chainguard/libraries/java/build-configuration/) and build a 
first test project. In a working setup the `java-chainguard` proxy repository contains
all libraries retrieved from Chainguard.

