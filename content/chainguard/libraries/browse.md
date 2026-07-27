---
title: "Browsing Chainguard Libraries"
linktitle: "Browsing"
description: "Searching, browsing, and inspecting Chainguard Libraries in the console"
type: "article"
date: 2025-07-03T14:00:00+00:00
lastmod: 2026-07-24T15:09:10+00:00
draft: false
tags: ["Chainguard Libraries"]
menu:
  docs:
    parent: "libraries"
weight: 007
toc: true
---

Chainguard Libraries includes thousands of libraries and many more individual
library versions and artifacts. In the Chainguard Console, you can
browse all available libraries and their versions, and inspect their
characteristics before using them in your application development.

## Access libraries in the Chainguard Console

Log in to the Chainguard Console at
[https://console.chainguard.dev/](https://console.chainguard.dev/).

In the left-hand navigation under **Libraries**, expand **Ecosystems** to find
links for browsing Chainguard's [**Java**](/chainguard/libraries/java/overview/), [**JavaScript**](/chainguard/libraries/javascript/overview/), and [**Python**](/chainguard/libraries/python/overview/) libraries.

<a id="initial-display"></a>

### Browse the libraries list

When you open a specific ecosystem, you'll see a search input box and a list of
libraries. Click any row to open the [library detail page](#library-page).

The list includes the following columns:

* **Name**: The full library name, excluding any version identifiers.
    * Python library names are simple strings, such as `setuptools` or
  `Flask-Admin`.
    * Java library names are the concatenation of the Maven
  coordinate values `groupId` and `artifactId`, separated by `:`. Examples are
  `org.springframework:spring-core` or `org.eclipse.jetty:jetty-http`.
* **Latest version**: The latest released and available version of the library
  and the total number of available versions.
* **Updated**: The most recent date when any version of this library was built
and published by Chainguard, or cached from the upstream fallback (when upstream fallback is enabled).

At the bottom of the page, see a total count of available libraries.

#### Upstream fallback details

At the top of the JavaScript ecosystem page, see whether [upstream fallback](/chainguard/libraries/overview/#upstream-fallback-and-controls) is enabled. For JavaScript, you can enable and disable upstream fallback in the Console or via `chainctl` commands.

Upstream fallback and policy controls can be enabled for the Python and Java ecosystems via `chainctl` commands, but cannot currently be enabled via the Chainguard Console. Learn more in the [Libraries Overview documentation](/chainguard/libraries/overview/#upstream-fallback-and-controls). are available for Chainguard Libraries and can be enabled via `chainctl` commands. For JavaScript, in addition to the ability to enable upstream fallback via `chainctl`, you can also enable it in the Chainguard Console.

When fallback is configured for your organization, you will see all JavaScript packages -- including those built by Chainguard and those that are mirrored from upstream npm -- in the Console. For a given package, you can see whether it is being served from Chainguard's rebuilt artifacts or proxied from upstream npm. For Java and Python, you cannot currently view upstream vs. Chainguard-built packages via the Chainguard Console.

<a id="search"></a>

### Search the libraries list

Use the **Search** text input at the top of the libraries list to
narrow down the list and to locate a specific library.

Click into a row to view a [specific library page](#library-page).

<a id="library-page"></a>

### View remediated libraries

[CVE remediation](/chainguard/libraries/cve-remediation/) is available for a
subset of Chainguard Libraries for Python and Java. You can view remediated libraries in
the Chainguard Console.

In the Python and Java libraries directories, click the **Remediated** tab to view a list
of remediated libraries. Click into a library to see which versions have
remediated CVEs.

While viewing the list of remediated versions for a library, click into a
version to view more details: which CVEs were remediated, the date that the
version was patched, and links to additional resources.

Learn more about browsing remediations in [CVE remediation for Chainguard
Libraries](/chainguard/libraries/cve-remediation/#about-cve-remediation).

### View malware information

For the JavaScript and Python ecosystems, click the **Malware** tab to learn how many packages have been blocked by Chainguard due to malware or greyware detection.

The list at the bottom of the page displays all blocked packages, including the package name, blocked version, the date it was blocked on, its MAL ID if available, and signals detected.

## Library page

To access a library page, click on the row for a specific library in the search
results or the [initial library list](#initial-display).

On a library's page, use the search bar at the top to search for specific
versions.

The list of library versions includes the following columns:

* **Version** - the version of the library. Library versions are strings.
  Depending on the ecosystem and library they can follow naming patterns and
  other restrictions that allow ordering by version.
* **Size** - the size of the library.
    * The displayed size reflects the primary file(s) only: `.jar`/`.pom` for
      Java, and `.whl`/`.tar.gz` for Python. It is not an aggregation of all
      files under a given version.
* **Built** - The date when this version was built and published by Chainguard.

Click on the column titles to change the **sort** order of the list.

## View repository configuration in the Chainguard Console

The Chainguard Console provides visibility into your repository configuration and the packages being served. When the upstream fallback is configured for your organization, you will see all packages including those built by Chainguard and those that are mirrored from upstream npm.

## Other resources

* [Chainguard Console](/platform/console/): Learn about using the Chainguard Console to browse container images.
* [Libraries Overview](/chainguard/libraries/overview/): Learn about criteria for building a library, upstream fallback and policy controls, and more.
