---
title: "dask-gateway-dask-gateway-server Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public dask-gateway-dask-gateway-server Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/dask-gateway-dask-gateway-server/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/dask-gateway-dask-gateway-server/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/dask-gateway-dask-gateway-server/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/dask-gateway-dask-gateway-server/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **dask-gateway-dask-gateway-server** Image.

## Variants Compared
The **dask-gateway-dask-gateway-server** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                                                                           |
|--------------|----------------------------------------------------------------------------------|
| Default User | `nonroot`                                                                        |
| Entrypoint   | `/sbin/tini -g --`                                                               |
| CMD          | `/usr/bin/dask-gateway-server --config /etc/dask-gateway/dask_gateway_config.py` |
| Workdir      | not specified                                                                    |
| Has apk?     | no                                                                               |
| Has a shell? | no                                                                               |

Check the [tags history page](/chainguard/chainguard-images/reference/dask-gateway-dask-gateway-server/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `dask-gateway-server`    | X      |
| `gdbm`                   | X      |
| `glibc`                  | X      |
| `glibc-locale-posix`     | X      |
| `ld-linux`               | X      |
| `libbz2-1`               | X      |
| `libcrypt1`              | X      |
| `libcrypto3`             | X      |
| `libexpat1`              | X      |
| `libffi`                 | X      |
| `libgcc`                 | X      |
| `libssl3`                | X      |
| `libstdc++`              | X      |
| `mpdecimal`              | X      |
| `ncurses`                | X      |
| `ncurses-terminfo-base`  | X      |
| `openssl-config`         | X      |
| `py3-aiohttp`            | X      |
| `py3-aiosignal`          | X      |
| `py3-async-timeout`      | X      |
| `py3-asynctest`          | X      |
| `py3-attrs`              | X      |
| `py3-certifi`            | X      |
| `py3-cffi`               | X      |
| `py3-charset-normalizer` | X      |
| `py3-colorama`           | X      |
| `py3-colorlog`           | X      |
| `py3-cryptography`       | X      |
| `py3-dateutil`           | X      |
| `py3-frozenlist`         | X      |
| `py3-idna`               | X      |
| `py3-idna-ssl`           | X      |
| `py3-importlib-metadata` | X      |
| `py3-kubernetes-asyncio` | X      |
| `py3-multidict`          | X      |
| `py3-pycparser`          | X      |
| `py3-pyyaml`             | X      |
| `py3-six`                | X      |
| `py3-sqlalchemy`         | X      |
| `py3-traitlets`          | X      |
| `py3-typing-extensions`  | X      |
| `py3-urllib3`            | X      |
| `py3-yarl`               | X      |
| `py3-zipp`               | X      |
| `py3.11-setuptools`      | X      |
| `python-3.11`            | X      |
| `readline`               | X      |
| `sqlite-libs`            | X      |
| `tini`                   | X      |
| `wolfi-baselayout`       | X      |
| `xz`                     | X      |
| `zlib`                   | X      |

