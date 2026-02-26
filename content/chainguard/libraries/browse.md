---
title: "Browsing Chainguard Libraries"
linktitle: "Browsing"
description: "Searching, browsing, and inspecting Chainguard Libraries in the console"
type: "article"
date: 2025-07-03T14:00:00+00:00
lastmod: 2025-07-03T14:00:00+00:00
draft: false
tags: ["Chainguard Libraries"]
menu:
  docs:
    parent: "libraries"
weight: 007
toc: true
---

Chainguard Libraries includes thousands of libraries and many more individual
library versions and artifacts. Through the Chainguard Console, you can
browse all available libraries and their versions, and inspect their
characteristics before using them in your application development.

## Access libraries in the Chainguard Console

Log in to the Chainguard Console at
[https://console.chainguard.dev/](https://console.chainguard.dev/).

In the left-hand navigation under **Libraries**, expand **Ecosystems** to find links for browsing Chainguard's [**Java**](/chainguard/libraries/java/overview/) and [**Python**](/chainguard/libraries/python/overview/) libraries. 

<a id="initial-display"></a>

### Browse the libraries list

When you open a specific ecosystem, you'll see a search input box
and a list of libraries. Click any row to open the [library detail page](#library-page).

The list includes the following columns:

* **Name** - the full library name, excluding any version identifiers.
    * Python library names are simple strings, such as `setuptools` or
  `Flask-Admin`. 
    * Java library names are the concatenation of the Maven
  coordinate values `groupId` and `artifactId`, separated by `:`. Examples are
  `org.springframework:spring-core` or `org.eclipse.jetty:jetty-http`.
* **Latest version** - the latest released and available version of the library
  and the total number of available versions.
* **Updated** - The most recent date when any version of this library was built and published by Chainguard.

At the bottom of the page, see a total count of available libraries.

<a id="search"></a>

### Search the libraries list

Use the **Search** text input at the top of the libraries list to
narrow down the list and to locate a specific library.

Click into a row to view a [specific library page](#library-page).

<a id="library-page"></a>

## Library Page

To access a library page, click on the row for a specific library in the
search results or the initial library list.

On a library's page, use the search bar at the top to search for specific versions.

The title of the library page shows the name of the library and includes a text
input to filter the displayed library versions.

The list of library versions uses the following columns:

* **Version** - the version of the library. Library versions are strings.
  Depending on the ecosystem and library they can follow naming patterns and
  other restrictions that allow ordering by version.
* **Size** - the size of the library.
* **Built** - The date when this version was built and published by Chainguard.

Click on the column titles to change the **sort** order of the list.

