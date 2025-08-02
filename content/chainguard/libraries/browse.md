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
library versions and artifacts. The Chainguard console includes features to
browse all available libraries and their versions, and  inspect some of their
characteristics, before using them in your application development.

## Access

Use your authentication details to access the console at
[https://console.chainguard.dev/](https://console.chainguard.dev/).

The left-hand navigation includes a **Libraries** section. Nested within the
**Ecosystems** drop-down you find links to browse the libraries from Chainguard
Libraries for **Java** and Chainguard Libraries for **Python**.

<a id="initial-display"></a>

## Initial Display

The initial display when accessing a specific ecosystem shows a search input box
and a list of libraries with the following columns.

* **Name** - the full name of the library excluding any version identifiers.
  Python library names are a simple string, such as `setuptools` or
  `Flask-Admin`. Java library names are the concatenation of the Maven
  coordinate values `groupId` and `artifactId`, separated by `:`. Examples are
  `org.springframework:spring-core` or `org.eclipse.jetty:jetty-http`.
* **Latest version** - the latest released and available version of the library
  and the total number of available versions.
* **Created** - TBD .. not sure what specific date that is, arguably it should
  be removed because it is not clear what library version these values are for,
  or header tile should change to Latest version release date or something
  (upstream release date ...), when Chainguard built a library could be a
  separate field but that might be less useful,
* **Updated** - TBD .. not sure .... I think we should remove this, libraries
  should not change so there should be no updated date

Below the list is a pagination control with **Previous** and **Next** buttons
and a total count of available libraries.

Clicking on a row brings you to the [specific library page](#library-page).

<a id="search"></a>

## Search

Use the **Search** text input on the [initial display](#initial-display) to
narrow down the list of displayed libraries and locate a specific library.

TBD Say more about what search patterns are supported and such, this is currently changing
Currently works partial match on name (art)

TBD - feature-wise Needs some sort of progress display since its sometimes slow

Search results display identically to the [initial display](#initial-display)
but with a limited number of libraries.

Clicking on a row brings you to the [specific library page](#library-page).

<a id="library-page"></a>

## Library Page

Access the library page by clicking on the row for a specific library in the
search results or the initial display page.

The title of the library page shows the name of the library and includes a text
input to filter the displayed library versions.

The list of library versions uses the following columns:

* **Version** - the version of the library. Library versions are strings.
  Depending on the ecosystem and library they can follow naming patterns and
  other restrictions that allow ordering by version.
* **Size** - TBD .. size of what? the jar , the pom, the war, probably should be
  removed and used on the library version page that lists the files
* **Created** - TBD .. not sure what specific date that is, we should probably
  change that to be the release date of the upstream release, when Chainguard
  build a library could be a separate field but that might be less useful
* **Updated** - TBD .. not sure .... I think we should remove this, libraries
  should not change so there should be no updated date

Click on the column titles to change the **sort** order of the list.

Clicking on a row brings you to the [specific library version
page](#library-version-page).

<a id="library-version-page"></a>

## Library Version Page

TBD - does not exist yet Shows details about the library including list of
available files and ideally also some of the metadata like source URL or Python
specifics like supported glibc versions, operating systems

potentially add download feature for files

## Java-specific Details ?? 

TBD ?

jar file typically, also pom and others, probably also all the provenance and
signature files and such

## Python-specific Details ??

TBD? 

wheel and sdist files, also for different operating systems and so on
