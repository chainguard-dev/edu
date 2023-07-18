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
|               | July 12th    | `sha256:cb21a7ec1088c6141e502a2db6bc0d599c321932c5296ea9d3fbbd912811321a` |
|               | July 11th    | `sha256:2fb7345617b05583e77744cf46b204279c7271ab82272fc5799f4c1efd082d57` |
|               | July 8th     | `sha256:5a89ccf60d766a54ddaf554890fceba742adc8f64b32ab2c274118153ec2f68c` |
|               | July 8th     | `sha256:bfb698f3f9cbeafcfc5f25ff407665494140adab4b8d33f92f517301db901c1f` |
|               | June 29th    | `sha256:9c14b4fca957e95860585a99edb7cc211cba8b059b0aecdd763c9cc6a2c5117d` |
|               | June 29th    | `sha256:b48b683b0c6faa004c27d88768a2028a552b8282b9bb0e82efee343e70fc139b` |
|               | June 26th    | `sha256:4971a7fc51b23a6732a1c82a854c875f1cc06927daae8752be8db18d18bce7b8` |
|               | June 26th    | `sha256:894c6bfd7d0eee09b54c003dd19782c8c6e87012e32bd685b7bcabc512529354` |
|               | June 22nd    | `sha256:8b4517c1db9d591bf951510b08dac39fb2d6abebd529524f6f31879a4c94d076` |
|               | June 22nd    | `sha256:ea2211b0a206b46e2c6794396b6f5e7996dbe80383bb781501ec2453aa606d4f` |



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

