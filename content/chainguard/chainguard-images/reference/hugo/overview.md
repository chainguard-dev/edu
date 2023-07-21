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
|  `latest`     | July 20th    | `sha256:e7d7ee2875b70af0a5226a9ee9f853774e8dc64d16b2cef68f20bd39ae6f5859` |
|  `latest-dev` | July 20th    | `sha256:015eb856164c8a358775978b3c240f60f9d725a6e813b50ea31f11e53480269e` |



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

