---
title: "Image Overview: hugo"
type: "article"
description: "Overview: hugo Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "images-reference"
weight: 500
toc: true
---

[cgr.dev/chainguard/hugo](https://github.com/chainguard-images/images/tree/main/images/hugo)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 18th    | `sha256:f1ec08fa96d10f6b909af5a73ecb9dfd42aa6d0bd3c6c2598f2fc42c7f2963b8` |
|  `latest`     | July 14th    | `sha256:c8e60c8f0258d196f0a00d24159b8941d4dce86a7069ea6ff8876e0ba22216a3` |



This is a minimal [Hugo](https://gohugo.io/) image. The image only contains
`hugo` and supporting libraries.  The hugo process start in `/hugo` by default
so this directory may be initialized with the Hugo site to serve.


Here is an example using the Hugo image to run the
["quickstart"](https://gohugo.io/getting-started/quick-start/#commands) locally:

```shell
# Start a shell in the Hugo "dev" container:
docker run -ti --rm -v -p 8080:8080 --entrypoint=/bin/sh \
       cgr.dev/chainguard/hugo:latest-dev

# Pass the quickstart commands (changing the bind address and port)
hugo new site quickstart
cd quickstart
git init
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke themes/ananke
echo "theme = 'ananke'" >> config.toml
hugo server --bind 0.0.0.0 --port 8080
```

Now open your browser to [localhost:8080](http://localhost:8080)!

