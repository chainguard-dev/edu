---
title: "Image Overview: ruby"
linktitle: "ruby"
type: "article"
layout: "single"
description: "Overview: ruby Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-02-29 16:25:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/ruby/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/ruby/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/ruby/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/ruby/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal Ruby base image.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/ruby:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

Ruby applications typically require the installation of third-party dependencies through [Rubygems](https://rubygems.org/). This means that using a fully distroless image for building your application would not work, as these do not include a package manager. In cases like this, you’ll need to implement a multi-stage Docker build that uses one of Chainguard's `-dev` Image variants to set up the application.

We encourage you to check out our guide on [getting started with Ruby](https://edu.chainguard.dev/chainguard/chainguard-images/getting-started/getting-started-ruby/) which demonstrates how you can use Chainguard's Ruby Image in both single- and multi-stage builds.
<!--body:end-->

