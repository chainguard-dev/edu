---
title: "gitlab-container-registry Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public gitlab-container-registry Chainguard Image."
date: 2024-07-10 00:36:03
lastmod: 2024-07-10 00:36:03
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gitlab-container-registry/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/gitlab-container-registry/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/gitlab-container-registry/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gitlab-container-registry/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **gitlab-container-registry** Image.

|              | latest-dev                 | latest                     |
|--------------|----------------------------|----------------------------|
| Default User | `git`                      | `git`                      |
| Entrypoint   | `/scripts/entrypoint.sh`   | `/scripts/entrypoint.sh`   |
| CMD          | `/scripts/process-wrapper` | `/scripts/process-wrapper` |
| Workdir      | not specified              | not specified              |
| Has apk?     | yes                        | no                         |
| Has a shell? | yes                        | yes                        |

Check the [tags history page](/chainguard/chainguard-images/reference/gitlab-container-registry/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                                 | latest-dev | latest |
|-------------------------------------------------|------------|--------|
| `apk-tools`                                     | X          |        |
| `bash`                                          | X          | X      |
| `busybox`                                       | X          | X      |
| `ca-certificates-bundle`                        | X          | X      |
| `chainguard-baselayout`                         | X          | X      |
| `curl`                                          | X          | X      |
| `git`                                           | X          |        |
| `gitlab-cng-ee-17.1-base`                       | X          | X      |
| `gitlab-cng-ee-17.1-container-registry-scripts` | X          | X      |
| `gitlab-container-registry`                     | X          | X      |
| `gitlab-container-registry-compat`              | X          | X      |
| `gitlab-logger`                                 | X          | X      |
| `glibc`                                         | X          | X      |
| `glibc-locale-posix`                            | X          | X      |
| `gomplate`                                      | X          | X      |
| `ld-linux`                                      | X          | X      |
| `libbrotlicommon1`                              | X          | X      |
| `libbrotlidec1`                                 | X          | X      |
| `libcrypt1`                                     | X          | X      |
| `libcrypto3`                                    | X          | X      |
| `libcurl-openssl4`                              | X          | X      |
| `libexpat1`                                     | X          |        |
| `libffi`                                        | X          | X      |
| `libgcc`                                        | X          | X      |
| `libidn2`                                       | X          | X      |
| `libnghttp2-14`                                 | X          | X      |
| `libpcre2-8-0`                                  | X          |        |
| `libproc-2-0`                                   | X          | X      |
| `libpsl`                                        | X          | X      |
| `libssl3`                                       | X          | X      |
| `libunistring`                                  | X          | X      |
| `libxcrypt`                                     | X          | X      |
| `ncurses`                                       | X          | X      |
| `ncurses-terminfo-base`                         | X          | X      |
| `procps`                                        | X          | X      |
| `readline`                                      | X          | X      |
| `ruby-3.2`                                      | X          | X      |
| `wget`                                          | X          |        |
| `wolfi-baselayout`                              | X          | X      |
| `xtail`                                         | X          | X      |
| `yaml`                                          | X          | X      |
| `zlib`                                          | X          | X      |

