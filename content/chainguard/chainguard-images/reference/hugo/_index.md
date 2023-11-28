---
title: "Image Overview: hugo"
linktitle: "hugo"
type: "article"
layout: "single"
description: "Overview: hugo Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2023-11-28 00:31:13
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/hugo/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/hugo/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/hugo/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/hugo/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
This is a minimal [Hugo](https://gohugo.io/) image.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/hugo:latest
```
<!--getting:end-->

<!--compatibility:start-->
## Compatibility NotesThis image only contains `hugo` and supporting libraries.  The Hugo process starts in `/hugo` by default so this directory may be initialized with the Hugo site to serve.<!--compatibility:end-->

<!--body:start-->
## Application Setup for End Users

The following is an example of using the Hugo image locally. It's based on the official [Hugo "quickstart"](https://gohugo.io/getting-started/quick-start/#commands) example.

To begin, start a shell in the Hugo developer (dev) container.

```shell
docker run -v $PWD/data:/home/data --entrypoint=/bin/sh -p 8080:8080 -it \
cgr.dev/chainguard/hugo:latest-dev
```

Create a new Hugo site using the quickstart commands.

```shell
hugo new site quickstart
```

Navigate into the new site's root directory.

```shell
cd quickstart
```

Initiate an empty Git repository 

```shell
git init
```

Clone a Hugo theme into the `themes` directory. 

```shell
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke themes/ananke
```

Add a line to the site's configuration file to let Hugo know to use the new theme.

```shell
echo "theme = 'ananke'" >> hugo.toml
```

Start the Hugo development server to serve the site. Be sure to change the default bind address and port to make the site accessible outside of the container.

```shell
hugo serve --bind 0.0.0.0 --port 8080
```

Now open your browser to [localhost:8080](http://localhost:8080) to visit the sample site.

When finished, you can press `CTRL + C` to stop the Hugo server from running, and then `CTRL + D` to exit the container shell.

If you're interested in enterprise support, SLAs, and access to older tags, [get in touch](https://www.chainguard.dev/contact?utm_source=docs).
<!--body:end-->

