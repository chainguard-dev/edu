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

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest-dev` | July 12th    | `sha256:cb21a7ec1088c6141e502a2db6bc0d599c321932c5296ea9d3fbbd912811321a` |
| `latest`     | July 11th    | `sha256:2fb7345617b05583e77744cf46b204279c7271ab82272fc5799f4c1efd082d57` |



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
