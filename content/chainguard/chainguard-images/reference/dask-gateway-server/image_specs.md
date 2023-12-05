---
title: "dask-gateway-server Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public dask-gateway-server Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/dask-gateway-server/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/dask-gateway-server/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/dask-gateway-server/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/dask-gateway-server/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **dask-gateway-server** Image.

## Variants Compared
The **dask-gateway-server** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                                                                       | latest                                                                           |
|--------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| Default User | `nonroot`                                                                        | `nonroot`                                                                        |
| Entrypoint   | `/sbin/tini -g --`                                                               | `/sbin/tini -g --`                                                               |
| CMD          | `/usr/bin/dask-gateway-server --config /etc/dask-gateway/dask_gateway_config.py` | `/usr/bin/dask-gateway-server --config /etc/dask-gateway/dask_gateway_config.py` |
| Workdir      | not specified                                                                    | not specified                                                                    |
| Has apk?     | yes                                                                              | no                                                                               |
| Has a shell? | yes                                                                              | no                                                                               |

Check the [tags history page](/chainguard/chainguard-images/reference/dask-gateway-server/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `busybox`                | X          |        |
| `ca-certificates-bundle` | X          | X      |
| `dask-gateway-server`    | X          | X      |
| `gdbm`                   | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libbz2-1`               | X          | X      |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          | X      |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          | X      |
| `libffi`                 | X          | X      |
| `libgcc`                 | X          | X      |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libssl3`                | X          | X      |
| `libstdc++`              | X          | X      |
| `llhttp`                 | X          | X      |
| `mpdecimal`              | X          | X      |
| `ncurses`                | X          | X      |
| `ncurses-terminfo-base`  | X          | X      |
| `openssl-config`         | X          | X      |
| `py3-aiohttp`            | X          | X      |
| `py3-aiosignal`          | X          | X      |
| `py3-async-timeout`      | X          | X      |
| `py3-asynctest`          | X          | X      |
| `py3-attrs`              | X          | X      |
| `py3-certifi`            | X          | X      |
| `py3-cffi`               | X          | X      |
| `py3-charset-normalizer` | X          | X      |
| `py3-colorama`           | X          | X      |
| `py3-colorlog`           | X          | X      |
| `py3-cryptography`       | X          | X      |
| `py3-frozenlist`         | X          | X      |
| `py3-idna`               | X          | X      |
| `py3-idna-ssl`           | X          | X      |
| `py3-importlib-metadata` | X          | X      |
| `py3-kubernetes-asyncio` | X          | X      |
| `py3-multidict`          | X          | X      |
| `py3-pycparser`          | X          | X      |
| `py3-python-dateutil`    | X          | X      |
| `py3-pyyaml`             | X          | X      |
| `py3-six`                | X          | X      |
| `py3-sqlalchemy`         | X          | X      |
| `py3-traitlets`          | X          | X      |
| `py3-typing-extensions`  | X          | X      |
| `py3-urllib3`            | X          | X      |
| `py3-yarl`               | X          | X      |
| `py3-zipp`               | X          | X      |
| `py3.12-setuptools`      | X          | X      |
| `python-3.12`            | X          | X      |
| `readline`               | X          | X      |
| `sqlite-libs`            | X          | X      |
| `tini`                   | X          | X      |
| `wolfi-baselayout`       | X          | X      |
| `xz`                     | X          | X      |
| `zlib`                   | X          | X      |

