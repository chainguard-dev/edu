---
title: "Image Overview: nginx"
type: "article"
description: "Overview: nginx Chainguard Images"
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

`stable` [cgr.dev/chainguard/nginx](https://github.com/chainguard-images/images/tree/main/images/nginx)
| Tags         | Aliases                                            |
|--------------|----------------------------------------------------|
| `latest`     | `1`, `1.24`, `1.24.0`, `1.24.0-r1`                 |
| `latest-dev` | `1-dev`, `1.24-dev`, `1.24.0-dev`, `1.24.0-r1-dev` |
| `next`       |                                                    |



A minimal nginx base image rebuilt every night from source.

## Upcoming Breaking Changes

On May 3 2023 the Chainguard nginx image will be rebuilt with several improvements, including
breaking changes. You may need to take action to update your application to prevent disruption. 

Specifically, the config file is being changed to bring the default configuration closer to that of
official nginx image. If you override the config with a custom configuration, you should not be affected.

The changes include:

 - Moving the default port from 80 to 8080. This is required to run on Kubernetes as a non-privileged user.
 - Setting nginx to automatically determine the number of worker processes
 - Moving the HTML directory to `/usr/share/nginx/html`

You can test the new image out now by pulling the `cgr.dev/chainguard/nginx:next` image. This is a
temporary tag that will be removed shortly after May 3, 2023, when the changes will merged into the
`latest` image.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/nginx:latest
```

## Usage

To try out the image, run:

```
docker run -p 8080:80 cgr.dev/chainguard/nginx
```

If you navigate to `localhost:8080`, you should see the nginx welcome page.

To run an example Hello World app, navigate to the root of this repo and run:

```
docker run -v $(pwd)/examples/hello-world/site-content:/var/lib/nginx/html -p 8080:80 cgr.dev/chainguard/nginx
```

If you navigate to `localhost:8080`, you should see `Hello World from Nginx!`.

To use a custom `nginx.conf` you can mount the file into the container

```
docker run -v $(pwd)/$CUSTOM_NGINX_CONF_DIRECTORY/nginx.conf:/etc/nginx/nginx.conf -p 8080:80 cgr.dev/chainguard/nginx
```

