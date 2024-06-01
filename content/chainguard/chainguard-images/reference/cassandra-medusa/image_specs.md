---
title: "cassandra-medusa Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public cassandra-medusa Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-06-01 00:50:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cassandra-medusa/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/cassandra-medusa/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/cassandra-medusa/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cassandra-medusa/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **cassandra-medusa** Image.

|              | latest-dev                             | latest                                 |
|--------------|----------------------------------------|----------------------------------------|
| Default User | `cassandra`                            | `cassandra`                            |
| Entrypoint   | `/home/cassandra/docker-entrypoint.sh` | `/home/cassandra/docker-entrypoint.sh` |
| CMD          | not specified                          | not specified                          |
| Workdir      | `/home/cassandra/`                     | `/home/cassandra/`                     |
| Has apk?     | yes                                    | no                                     |
| Has a shell? | yes                                    | yes                                    |

Check the [tags history page](/chainguard/chainguard-images/reference/cassandra-medusa/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                 | latest-dev | latest |
|---------------------------------|------------|--------|
| `apk-tools`                     | X          |        |
| `bash`                          | X          | X      |
| `busybox`                       | X          | X      |
| `ca-certificates-bundle`        | X          | X      |
| `chainguard-baselayout`         | X          | X      |
| `gdbm`                          | X          | X      |
| `git`                           | X          |        |
| `glibc`                         | X          | X      |
| `glibc-locale-posix`            | X          | X      |
| `ld-linux`                      | X          | X      |
| `libbrotlicommon1`              | X          |        |
| `libbrotlidec1`                 | X          |        |
| `libbz2-1`                      | X          | X      |
| `libcrypt1`                     | X          | X      |
| `libcrypto3`                    | X          | X      |
| `libcurl-openssl4`              | X          |        |
| `libexpat1`                     | X          | X      |
| `libffi`                        | X          | X      |
| `libgcc`                        | X          | X      |
| `libidn2`                       | X          |        |
| `libnghttp2-14`                 | X          |        |
| `libpcre2-8-0`                  | X          |        |
| `libpsl`                        | X          |        |
| `libssl3`                       | X          | X      |
| `libstdc++`                     | X          | X      |
| `libunistring`                  | X          |        |
| `libxcrypt`                     | X          | X      |
| `mpdecimal`                     | X          | X      |
| `ncurses`                       | X          | X      |
| `ncurses-terminfo-base`         | X          | X      |
| `py3-attrs`                     | X          | X      |
| `py3-build`                     | X          | X      |
| `py3-cachecontrol`              | X          | X      |
| `py3-cassandra-medusa`          | X          | X      |
| `py3-cassandra-medusa-compat`   | X          | X      |
| `py3-certifi`                   | X          | X      |
| `py3-cffi`                      | X          | X      |
| `py3-charset-normalizer`        | X          | X      |
| `py3-cleo`                      | X          | X      |
| `py3-crashtest`                 | X          | X      |
| `py3-cryptography`              | X          | X      |
| `py3-distlib`                   | X          | X      |
| `py3-dulwich`                   | X          | X      |
| `py3-filelock`                  | X          | X      |
| `py3-idna`                      | X          | X      |
| `py3-importlib-metadata`        | X          | X      |
| `py3-importlib-resources`       | X          | X      |
| `py3-jaraco.classes`            | X          | X      |
| `py3-jeepney`                   | X          | X      |
| `py3-jsonschema`                | X          | X      |
| `py3-jsonschema-specifications` | X          | X      |
| `py3-keyring`                   | X          | X      |
| `py3-more-itertools`            | X          | X      |
| `py3-msgpack`                   | X          | X      |
| `py3-packaging`                 | X          | X      |
| `py3-parsing`                   | X          | X      |
| `py3-pexpect`                   | X          | X      |
| `py3-pkginfo`                   | X          | X      |
| `py3-platformdirs`              | X          | X      |
| `py3-poetry`                    | X          | X      |
| `py3-poetry-core`               | X          | X      |
| `py3-ptyprocess`                | X          | X      |
| `py3-pycparser`                 | X          | X      |
| `py3-pyproject-hooks`           | X          | X      |
| `py3-pywin32-ctypes`            | X          | X      |
| `py3-rapidfuzz`                 | X          | X      |
| `py3-referencing`               | X          | X      |
| `py3-requests`                  | X          | X      |
| `py3-requests-toolbelt`         | X          | X      |
| `py3-rpds-py`                   | X          | X      |
| `py3-secretstorage`             | X          | X      |
| `py3-shellingham`               | X          | X      |
| `py3-tomli`                     | X          | X      |
| `py3-tomlkit`                   | X          | X      |
| `py3-trove-classifiers`         | X          | X      |
| `py3-typing-extensions`         | X          | X      |
| `py3-urllib3`                   | X          | X      |
| `py3-virtualenv`                | X          | X      |
| `py3-xattr`                     | X          | X      |
| `py3-zipp`                      | X          | X      |
| `py3.12-installer`              | X          | X      |
| `python-3.11-base`              | X          | X      |
| `python-3.12`                   | X          | X      |
| `python-3.12-base`              | X          | X      |
| `readline`                      | X          | X      |
| `sqlite-libs`                   | X          | X      |
| `wget`                          | X          |        |
| `wolfi-baselayout`              | X          | X      |
| `xz`                            | X          | X      |
| `zlib`                          | X          | X      |

