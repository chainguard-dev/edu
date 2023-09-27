---
title: "fluentd Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public fluentd Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/fluentd/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/fluentd/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/fluentd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/fluentd/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **fluentd** Image.

## Variants Compared
The **fluentd** Chainguard Image currently has 4 public variants: 

- `latest-dev`
- `latest-splunk-dev`
- `latest-splunk`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev     | latest-splunk-dev | latest-splunk  | latest         |
|--------------|----------------|-------------------|----------------|----------------|
| Default User | `fluent`       | `fluent`          | `fluent`       | `fluent`       |
| Entrypoint   | Service Bundle | Service Bundle    | Service Bundle | Service Bundle |
| CMD          | not specified  | not specified     | not specified  | not specified  |
| Workdir      | not specified  | not specified     | not specified  | not specified  |
| Has apk?     | yes            | yes               | no             | no             |
| Has a shell? | yes            | yes               | no             | no             |

Check the [tags history page](/chainguard/chainguard-images/reference/fluentd/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                     | latest-dev | latest-splunk-dev | latest-splunk | latest |
|-------------------------------------|------------|-------------------|---------------|--------|
| `apk-tools`                         | X          | X                 |               |        |
| `bash`                              | X          | X                 |               |        |
| `binutils`                          | X          | X                 |               |        |
| `build-base`                        | X          | X                 |               |        |
| `busybox`                           | X          | X                 |               |        |
| `ca-certificates-bundle`            | X          | X                 | X             | X      |
| `execline`                          | X          | X                 | X             | X      |
| `gcc`                               | X          | X                 |               |        |
| `git`                               | X          | X                 |               |        |
| `glibc`                             | X          | X                 | X             | X      |
| `glibc-dev`                         | X          | X                 |               |        |
| `glibc-locale-posix`                | X          | X                 | X             | X      |
| `gmp`                               | X          | X                 |               |        |
| `isl`                               | X          | X                 |               |        |
| `ld-linux`                          | X          | X                 | X             | X      |
| `libatomic`                         | X          | X                 |               |        |
| `libbrotlicommon1`                  | X          | X                 |               |        |
| `libbrotlidec1`                     | X          | X                 |               |        |
| `libcrypt1`                         | X          | X                 | X             | X      |
| `libcrypto3`                        | X          | X                 | X             | X      |
| `libcurl-openssl4`                  | X          | X                 |               |        |
| `libexpat1`                         | X          | X                 |               |        |
| `libffi`                            | X          | X                 | X             | X      |
| `libgcc`                            | X          | X                 | X             | X      |
| `libgo`                             | X          | X                 |               |        |
| `libgomp`                           | X          | X                 |               |        |
| `libnghttp2-14`                     | X          | X                 |               |        |
| `libpcre2-8-0`                      | X          | X                 |               |        |
| `libpq-11`                          | X          | X                 | X             | X      |
| `libssl3`                           | X          | X                 | X             | X      |
| `libstdc++`                         | X          | X                 |               |        |
| `libstdc++-dev`                     | X          | X                 |               |        |
| `linux-headers`                     | X          | X                 |               |        |
| `make`                              | X          | X                 |               |        |
| `mpc`                               | X          | X                 |               |        |
| `mpfr`                              | X          | X                 |               |        |
| `ncurses`                           | X          | X                 | X             | X      |
| `ncurses-terminfo-base`             | X          | X                 | X             | X      |
| `nss-db`                            | X          | X                 |               |        |
| `nss-hesiod`                        | X          | X                 |               |        |
| `openssl-config`                    | X          | X                 | X             | X      |
| `pkgconf`                           | X          | X                 |               |        |
| `posix-cc-wrappers`                 | X          | X                 |               |        |
| `readline`                          | X          | X                 | X             | X      |
| `ruby-3.2`                          | X          | X                 | X             | X      |
| `ruby-3.2-dev`                      | X          | X                 |               |        |
| `ruby3.2-bundler`                   | X          | X                 | X             | X      |
| `ruby3.2-concurrent-ruby`           | X          | X                 | X             | X      |
| `ruby3.2-cool.io`                   | X          | X                 | X             | X      |
| `ruby3.2-fluentd`                   | X          | X                 | X             | X      |
| `ruby3.2-http_parser.rb`            | X          | X                 | X             | X      |
| `ruby3.2-msgpack`                   | X          | X                 | X             | X      |
| `ruby3.2-serverengine`              | X          | X                 | X             | X      |
| `ruby3.2-sigdump`                   | X          | X                 | X             | X      |
| `ruby3.2-strptime`                  | X          | X                 | X             | X      |
| `ruby3.2-tzinfo`                    | X          | X                 | X             | X      |
| `ruby3.2-tzinfo-data`               | X          | X                 | X             | X      |
| `ruby3.2-webrick`                   | X          | X                 | X             | X      |
| `ruby3.2-yajl-ruby`                 | X          | X                 | X             | X      |
| `s6`                                | X          | X                 | X             | X      |
| `skalibs`                           | X          | X                 | X             | X      |
| `wolfi-baselayout`                  | X          | X                 | X             | X      |
| `yaml`                              | X          | X                 | X             | X      |
| `zlib`                              | X          | X                 | X             | X      |
| `fluent-plugin-prometheus`          |            | X                 | X             |        |
| `fluent-plugin-rewrite-tag-filter`  |            | X                 | X             |        |
| `fluent-plugin-splunk-hec`          |            | X                 | X             |        |
| `net-tools`                         |            | X                 | X             |        |
| `ruby3.2-activemodel`               |            | X                 | X             |        |
| `ruby3.2-activesupport`             |            | X                 | X             |        |
| `ruby3.2-aes_key_wrap`              |            | X                 | X             |        |
| `ruby3.2-attr_required`             |            | X                 | X             |        |
| `ruby3.2-bindata`                   |            | X                 | X             |        |
| `ruby3.2-connection_pool`           |            | X                 | X             |        |
| `ruby3.2-date`                      |            | X                 | X             |        |
| `ruby3.2-faraday`                   |            | X                 | X             |        |
| `ruby3.2-faraday-follow_redirects`  |            | X                 | X             |        |
| `ruby3.2-faraday-net_http`          |            | X                 | X             |        |
| `ruby3.2-fluent-config-regexp-type` |            | X                 | X             |        |
| `ruby3.2-i18n`                      |            | X                 | X             |        |
| `ruby3.2-json-jwt`                  |            | X                 | X             |        |
| `ruby3.2-mail`                      |            | X                 | X             |        |
| `ruby3.2-mini_mime`                 |            | X                 | X             |        |
| `ruby3.2-multi_json`                |            | X                 | X             |        |
| `ruby3.2-net-http-persistent`       |            | X                 | X             |        |
| `ruby3.2-net-imap`                  |            | X                 | X             |        |
| `ruby3.2-net-protocol`              |            | X                 | X             |        |
| `ruby3.2-openid_connect-1.1.8`      |            | X                 | X             |        |
| `ruby3.2-prometheus-client`         |            | X                 | X             |        |
| `ruby3.2-public_suffix`             |            | X                 | X             |        |
| `ruby3.2-rack`                      |            | X                 | X             |        |
| `ruby3.2-rack-oauth2`               |            | X                 | X             |        |
| `ruby3.2-ruby2_keywords`            |            | X                 | X             |        |
| `ruby3.2-swd`                       |            | X                 | X             |        |
| `ruby3.2-timeout`                   |            | X                 | X             |        |
| `ruby3.2-validate_email`            |            | X                 | X             |        |
| `ruby3.2-validate_url`              |            | X                 | X             |        |
| `ruby3.2-webfinger`                 |            | X                 | X             |        |

