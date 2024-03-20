---
title: "Image Overview: gradle"
linktitle: "gradle"
type: "article"
layout: "single"
description: "Overview: gradle Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-03-14 00:37:02
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu: 
  docs: 
    parent: "images-reference"
weight: 500
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/gradle/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gradle/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/gradle/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gradle/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image with [Gradle](https://gradle.org/) build system.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/gradle:latest
```
<!--getting:end-->

<!--body:start-->
## Using gradle

Chainguard gradle images come with different versions of OpenJDK, ensure you choose the correct image tag for your application needs.  In these examples we will use a Chainguard gradle image based on OpenJDK 11.

__NOTE__: if you are running Docker on Mac M1 you may experience intermittent container high CPU and container / JVM crashes.  There have been [reports](https://github.com/metanorma/metanorma-docker/issues/126) of this behaviour and also affects non Chainguard images.  It is expected that using `arm` based images will address the problem which is in development for Chainguard images.  When running the examples below you might experince gradle builds hanging.  If you do, you can `docker ps` and `docker kill $PID` and retry.  This is not an ideal experience and will be improved.

Check the gradle version
```
 % docker run gradle --version

Welcome to Gradle 8.0.1-20230224000000+0000!

Here are the highlights of this release:
 - Improvements to the Kotlin DSL
 - Fine-grained parallelism from the first build with configuration cache
 - Configurable Gradle user home cache cleanup


------------------------------------------------------------
Gradle 8.0.1-20230224000000+0000
------------------------------------------------------------

Build time:   2023-02-24 00:00:00 UTC
Revision:     68959bf76cef4d28c678f2e2085ee84e8647b77a

Kotlin:       1.8.10
Groovy:       3.0.13
Ant:          Apache Ant(TM) version 1.10.11 compiled on July 10 2021
JVM:          11.0.18-internal (wolfi 11.0.18-internal+0-wolfi-r1)
OS:           Linux 5.15.49-linuxkit aarch64
```
<!--body:end-->

