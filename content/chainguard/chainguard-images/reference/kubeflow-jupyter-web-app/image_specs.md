---
title: "kubeflow-jupyter-web-app Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public kubeflow-jupyter-web-app Chainguard Image variants"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubeflow-jupyter-web-app/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/kubeflow-jupyter-web-app/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubeflow-jupyter-web-app/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubeflow-jupyter-web-app/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **kubeflow-jupyter-web-app** Image.

## Variants Compared
The **kubeflow-jupyter-web-app** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                                                                                                                       | latest                                                                                                                           |
|--------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Default User | `nonroot`                                                                                                                        | `nonroot`                                                                                                                        |
| Entrypoint   | `/bin/bash -c "gunicorn -w 3 --bind 0.0.0.0:5000 --chdir /usr/share/kubeflow-jupyter-web-app --access-logfile - entrypoint:app"` | `/bin/bash -c "gunicorn -w 3 --bind 0.0.0.0:5000 --chdir /usr/share/kubeflow-jupyter-web-app --access-logfile - entrypoint:app"` |
| CMD          | not specified                                                                                                                    | not specified                                                                                                                    |
| Workdir      | not specified                                                                                                                    | not specified                                                                                                                    |
| Has apk?     | yes                                                                                                                              | no                                                                                                                               |
| Has a shell? | yes                                                                                                                              | yes                                                                                                                              |

Check the [tags history page](/chainguard/chainguard-images/reference/kubeflow-jupyter-web-app/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                            | latest-dev | latest |
|----------------------------|------------|--------|
| `apk-tools`                | X          |        |
| `bash`                     | X          | X      |
| `busybox`                  | X          |        |
| `ca-certificates-bundle`   | X          | X      |
| `gdbm`                     | X          | X      |
| `git`                      | X          |        |
| `glibc`                    | X          | X      |
| `glibc-locale-posix`       | X          | X      |
| `kubeflow-jupyter-web-app` | X          | X      |
| `ld-linux`                 | X          | X      |
| `libbrotlicommon1`         | X          |        |
| `libbrotlidec1`            | X          |        |
| `libbz2-1`                 | X          | X      |
| `libcrypt1`                | X          | X      |
| `libcrypto3`               | X          | X      |
| `libcurl-openssl4`         | X          |        |
| `libexpat1`                | X          | X      |
| `libffi`                   | X          | X      |
| `libgcc`                   | X          | X      |
| `libnghttp2-14`            | X          |        |
| `libpcre2-8-0`             | X          |        |
| `libssl3`                  | X          | X      |
| `libstdc++`                | X          | X      |
| `mpdecimal`                | X          | X      |
| `ncurses`                  | X          | X      |
| `ncurses-terminfo-base`    | X          | X      |
| `openssl-config`           | X          | X      |
| `py3-gunicorn`             | X          | X      |
| `py3-importlib-metadata`   | X          | X      |
| `py3-packaging`            | X          | X      |
| `py3-parsing`              | X          | X      |
| `py3-typing-extensions`    | X          | X      |
| `py3-zipp`                 | X          | X      |
| `py3.12-setuptools`        | X          | X      |
| `python-3.12`              | X          | X      |
| `readline`                 | X          | X      |
| `sqlite-libs`              | X          | X      |
| `wolfi-baselayout`         | X          | X      |
| `xz`                       | X          | X      |
| `zlib`                     | X          | X      |

