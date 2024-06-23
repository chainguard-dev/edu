---
title: "kubeflow-pipelines-metadata-writer Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public kubeflow-pipelines-metadata-writer Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-06-23 00:43:06
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubeflow-pipelines-metadata-writer/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/kubeflow-pipelines-metadata-writer/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubeflow-pipelines-metadata-writer/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubeflow-pipelines-metadata-writer/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **kubeflow-pipelines-metadata-writer** Image.

|              | latest-dev                                           | latest                                               |
|--------------|------------------------------------------------------|------------------------------------------------------|
| Default User | `nonroot`                                            | `nonroot`                                            |
| Entrypoint   | `python3 -u /kfp/metadata_writer/metadata_writer.py` | `python3 -u /kfp/metadata_writer/metadata_writer.py` |
| CMD          | not specified                                        | not specified                                        |
| Workdir      | not specified                                        | not specified                                        |
| Has apk?     | yes                                                  | no                                                   |
| Has a shell? | yes                                                  | no                                                   |

Check the [tags history page](/chainguard/chainguard-images/reference/kubeflow-pipelines-metadata-writer/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                                | latest-dev | latest |
|------------------------------------------------|------------|--------|
| `abseil-cpp`                                   | X          | X      |
| `abseil-cpp-base`                              | X          | X      |
| `abseil-cpp-city`                              | X          | X      |
| `abseil-cpp-cord`                              | X          | X      |
| `abseil-cpp-cord-internal`                     | X          | X      |
| `abseil-cpp-cordz-functions`                   | X          | X      |
| `abseil-cpp-cordz-handle`                      | X          | X      |
| `abseil-cpp-cordz-info`                        | X          | X      |
| `abseil-cpp-crc-cord-state`                    | X          | X      |
| `abseil-cpp-crc-internal`                      | X          | X      |
| `abseil-cpp-crc32c`                            | X          | X      |
| `abseil-cpp-debugging-internal`                | X          | X      |
| `abseil-cpp-demangle-internal`                 | X          | X      |
| `abseil-cpp-examine-stack`                     | X          | X      |
| `abseil-cpp-exponential-biased`                | X          | X      |
| `abseil-cpp-flags-commandlineflag`             | X          | X      |
| `abseil-cpp-flags-commandlineflag-internal`    | X          | X      |
| `abseil-cpp-flags-config`                      | X          | X      |
| `abseil-cpp-flags-internal`                    | X          | X      |
| `abseil-cpp-flags-marshalling`                 | X          | X      |
| `abseil-cpp-flags-private-handle-accessor`     | X          | X      |
| `abseil-cpp-flags-program-name`                | X          | X      |
| `abseil-cpp-flags-reflection`                  | X          | X      |
| `abseil-cpp-hash`                              | X          | X      |
| `abseil-cpp-int128`                            | X          | X      |
| `abseil-cpp-kernel-timeout-internal`           | X          | X      |
| `abseil-cpp-log-globals`                       | X          | X      |
| `abseil-cpp-log-internal-format`               | X          | X      |
| `abseil-cpp-log-internal-globals`              | X          | X      |
| `abseil-cpp-log-internal-log-sink-set`         | X          | X      |
| `abseil-cpp-log-internal-message`              | X          | X      |
| `abseil-cpp-log-internal-nullguard`            | X          | X      |
| `abseil-cpp-log-internal-proto`                | X          | X      |
| `abseil-cpp-log-sink`                          | X          | X      |
| `abseil-cpp-low-level-hash`                    | X          | X      |
| `abseil-cpp-malloc-internal`                   | X          | X      |
| `abseil-cpp-random-internal-platform`          | X          | X      |
| `abseil-cpp-random-internal-pool-urbg`         | X          | X      |
| `abseil-cpp-random-internal-randen`            | X          | X      |
| `abseil-cpp-random-internal-randen-hwaes`      | X          | X      |
| `abseil-cpp-random-internal-randen-hwaes-impl` | X          | X      |
| `abseil-cpp-random-internal-randen-slow`       | X          | X      |
| `abseil-cpp-random-internal-seed-material`     | X          | X      |
| `abseil-cpp-random-seed-gen-exception`         | X          | X      |
| `abseil-cpp-raw-hash-set`                      | X          | X      |
| `abseil-cpp-raw-logging-internal`              | X          | X      |
| `abseil-cpp-spinlock-wait`                     | X          | X      |
| `abseil-cpp-stacktrace`                        | X          | X      |
| `abseil-cpp-status`                            | X          | X      |
| `abseil-cpp-statusor`                          | X          | X      |
| `abseil-cpp-str-format-internal`               | X          | X      |
| `abseil-cpp-strerror`                          | X          | X      |
| `abseil-cpp-strings`                           | X          | X      |
| `abseil-cpp-strings-internal`                  | X          | X      |
| `abseil-cpp-symbolize`                         | X          | X      |
| `abseil-cpp-synchronization`                   | X          | X      |
| `abseil-cpp-throw-delegate`                    | X          | X      |
| `abseil-cpp-time`                              | X          | X      |
| `abseil-cpp-time-zone`                         | X          | X      |
| `apk-tools`                                    | X          |        |
| `bash`                                         | X          |        |
| `busybox`                                      | X          |        |
| `c-ares`                                       | X          | X      |
| `ca-certificates-bundle`                       | X          | X      |
| `chainguard-baselayout`                        | X          | X      |
| `gdbm`                                         | X          | X      |
| `git`                                          | X          |        |
| `glibc`                                        | X          | X      |
| `glibc-locale-posix`                           | X          | X      |
| `icu`                                          | X          | X      |
| `kubeflow-pipelines-metadata-writer`           | X          | X      |
| `kubeflow-pipelines-metadata-writer-compat`    | X          | X      |
| `ld-linux`                                     | X          | X      |
| `libbrotlicommon1`                             | X          |        |
| `libbrotlidec1`                                | X          |        |
| `libbz2-1`                                     | X          | X      |
| `libcrypt1`                                    | X          | X      |
| `libcrypto3`                                   | X          | X      |
| `libcurl-openssl4`                             | X          |        |
| `libexpat1`                                    | X          | X      |
| `libffi`                                       | X          | X      |
| `libgcc`                                       | X          | X      |
| `libidn2`                                      | X          |        |
| `libnghttp2-14`                                | X          |        |
| `libpcre2-8-0`                                 | X          |        |
| `libpsl`                                       | X          |        |
| `libssl3`                                      | X          | X      |
| `libstdc++`                                    | X          | X      |
| `libunistring`                                 | X          |        |
| `libxcrypt`                                    | X          | X      |
| `mpdecimal`                                    | X          | X      |
| `ncurses`                                      | X          | X      |
| `ncurses-terminfo-base`                        | X          | X      |
| `py3-absl-py`                                  | X          | X      |
| `py3-asn1`                                     | X          | X      |
| `py3-asn1-modules`                             | X          | X      |
| `py3-attrs`                                    | X          | X      |
| `py3-cachetools`                               | X          | X      |
| `py3-certifi`                                  | X          | X      |
| `py3-charset-normalizer`                       | X          | X      |
| `py3-google-auth`                              | X          | X      |
| `py3-grpcio`                                   | X          | X      |
| `py3-idna`                                     | X          | X      |
| `py3-importlib-metadata`                       | X          | X      |
| `py3-ipaddress`                                | X          | X      |
| `py3-kubernetes`                               | X          | X      |
| `py3-lru-dict`                                 | X          | X      |
| `py3-ml-metadata`                              | X          | X      |
| `py3-oauthlib`                                 | X          | X      |
| `py3-protobuf`                                 | X          | X      |
| `py3-python-dateutil`                          | X          | X      |
| `py3-requests`                                 | X          | X      |
| `py3-requests-oauthlib`                        | X          | X      |
| `py3-rsa`                                      | X          | X      |
| `py3-typing-extensions`                        | X          | X      |
| `py3-urllib3`                                  | X          | X      |
| `py3-websocket-client`                         | X          | X      |
| `py3-zipp`                                     | X          | X      |
| `py3.12-pyyaml`                                | X          | X      |
| `py3.12-six`                                   | X          | X      |
| `python-3.12`                                  | X          | X      |
| `python-3.12-base`                             | X          | X      |
| `re2`                                          | X          | X      |
| `readline`                                     | X          | X      |
| `sqlite-libs`                                  | X          | X      |
| `wget`                                         | X          |        |
| `wolfi-baselayout`                             | X          | X      |
| `xz`                                           | X          | X      |
| `yaml`                                         | X          | X      |
| `zlib`                                         | X          | X      |

