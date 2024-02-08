---
title: "gitlab-exporter Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public gitlab-exporter Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-02-08 00:18:32
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gitlab-exporter/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/gitlab-exporter/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/gitlab-exporter/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gitlab-exporter/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **gitlab-exporter** Image.

## Variants Compared
The **gitlab-exporter** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                                        | latest                                            |
|--------------|---------------------------------------------------|---------------------------------------------------|
| Default User | `nonroot`                                         | `nonroot`                                         |
| Entrypoint   | `/scripts/entrypoint.sh /scripts/process-wrapper` | `/scripts/entrypoint.sh /scripts/process-wrapper` |
| CMD          | not specified                                     | not specified                                     |
| Workdir      | not specified                                     | not specified                                     |
| Has apk?     | yes                                               | no                                                |
| Has a shell? | yes                                               | yes                                               |

Check the [tags history page](/chainguard/chainguard-images/reference/gitlab-exporter/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                               | latest-dev | latest |
|-------------------------------|------------|--------|
| `apk-tools`                   | X          |        |
| `bash`                        | X          | X      |
| `busybox`                     | X          | X      |
| `ca-certificates-bundle`      | X          | X      |
| `curl`                        | X          | X      |
| `git`                         | X          |        |
| `gitlab-cng-base`             | X          | X      |
| `gitlab-cng-exporter-scripts` | X          | X      |
| `gitlab-exporter`             | X          | X      |
| `gitlab-logger`               | X          | X      |
| `glibc`                       | X          | X      |
| `glibc-locale-posix`          | X          | X      |
| `gomplate`                    | X          | X      |
| `jemalloc`                    | X          | X      |
| `ld-linux`                    | X          | X      |
| `libbrotlicommon1`            | X          | X      |
| `libbrotlidec1`               | X          | X      |
| `libcrypt1`                   | X          | X      |
| `libcrypto3`                  | X          | X      |
| `libcurl-openssl4`            | X          | X      |
| `libexpat1`                   | X          |        |
| `libffi`                      | X          | X      |
| `libgcc`                      | X          | X      |
| `libidn2`                     | X          | X      |
| `libnghttp2-14`               | X          | X      |
| `libpcre2-8-0`                | X          |        |
| `libpq-15`                    | X          | X      |
| `libproc-2-0`                 | X          | X      |
| `libpsl`                      | X          | X      |
| `libssl3`                     | X          | X      |
| `libstdc++`                   | X          | X      |
| `libunistring`                | X          | X      |
| `ncurses`                     | X          | X      |
| `ncurses-terminfo-base`       | X          | X      |
| `openssl-config`              | X          | X      |
| `procps`                      | X          | X      |
| `readline`                    | X          | X      |
| `ruby-3.2`                    | X          | X      |
| `ruby3.2-bundler`             | X          | X      |
| `ruby3.2-concurrent-ruby`     | X          | X      |
| `ruby3.2-connection_pool`     | X          | X      |
| `ruby3.2-deep_merge`          | X          | X      |
| `ruby3.2-excon`               | X          | X      |
| `ruby3.2-faraday`             | X          | X      |
| `ruby3.2-faraday-excon`       | X          | X      |
| `ruby3.2-faraday-net_http`    | X          | X      |
| `ruby3.2-mustermann`          | X          | X      |
| `ruby3.2-nio4r`               | X          | X      |
| `ruby3.2-pg`                  | X          | X      |
| `ruby3.2-puma`                | X          | X      |
| `ruby3.2-quantile`            | X          | X      |
| `ruby3.2-rack-2.2`            | X          | X      |
| `ruby3.2-rack-protection`     | X          | X      |
| `ruby3.2-redis`               | X          | X      |
| `ruby3.2-redis-client`        | X          | X      |
| `ruby3.2-redis-namespace`     | X          | X      |
| `ruby3.2-ruby2_keywords`      | X          | X      |
| `ruby3.2-sidekiq`             | X          | X      |
| `ruby3.2-sinatra`             | X          | X      |
| `ruby3.2-tilt`                | X          | X      |
| `ruby3.2-webrick`             | X          | X      |
| `wget`                        | X          |        |
| `wolfi-baselayout`            | X          | X      |
| `xtail`                       | X          | X      |
| `yaml`                        | X          | X      |
| `zlib`                        | X          | X      |

