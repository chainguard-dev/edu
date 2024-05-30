---
title: "renovate Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public renovate Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-05-30 00:47:59
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/renovate/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/renovate/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/renovate/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/renovate/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **renovate** Image.

|              | latest-dev    | latest        |
|--------------|---------------|---------------|
| Default User | `nonroot`     | `nonroot`     |
| Entrypoint   | `renovate`    | `renovate`    |
| CMD          | `--help`      | `--help`      |
| Workdir      | not specified | not specified |
| Has apk?     | yes           | yes           |
| Has a shell? | yes           | yes           |

Check the [tags history page](/chainguard/chainguard-images/reference/renovate/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                 | latest-dev | latest |
|---------------------------------|------------|--------|
| `apk-tools`                     | X          | X      |
| `bash`                          | X          | X      |
| `binutils`                      | X          | X      |
| `binutils-gold`                 | X          | X      |
| `build-base`                    | X          | X      |
| `busybox`                       | X          | X      |
| `c-ares`                        | X          | X      |
| `ca-certificates`               | X          | X      |
| `ca-certificates-bundle`        | X          | X      |
| `chainguard-baselayout`         | X          | X      |
| `composer`                      | X          | X      |
| `coreutils`                     | X          | X      |
| `dotnet-7`                      | X          | X      |
| `dotnet-7-runtime`              | X          | X      |
| `elixir-1.16`                   | X          | X      |
| `erlang-27`                     | X          | X      |
| `fontconfig-config`             | X          | X      |
| `freetype`                      | X          | X      |
| `gcc`                           | X          | X      |
| `gdbm`                          | X          | X      |
| `git`                           | X          | X      |
| `glibc`                         | X          | X      |
| `glibc-dev`                     | X          | X      |
| `glibc-locale-posix`            | X          | X      |
| `gmp`                           | X          | X      |
| `go-1.22`                       | X          | X      |
| `gradle-8`                      | X          | X      |
| `helm`                          | X          | X      |
| `icu`                           | X          | X      |
| `isl`                           | X          | X      |
| `java-cacerts`                  | X          | X      |
| `java-common`                   | X          | X      |
| `jsonnet-bundler`               | X          | X      |
| `ld-linux`                      | X          | X      |
| `lerna`                         | X          | X      |
| `libLLVM-18.1`                  | X          | X      |
| `libacl1`                       | X          | X      |
| `libatomic`                     | X          | X      |
| `libattr1`                      | X          | X      |
| `libbrotlicommon1`              | X          | X      |
| `libbrotlidec1`                 | X          | X      |
| `libbrotlienc1`                 | X          | X      |
| `libbz2-1`                      | X          | X      |
| `libcrypt1`                     | X          | X      |
| `libcrypto3`                    | X          | X      |
| `libcurl-openssl4`              | X          | X      |
| `libexpat1`                     | X          | X      |
| `libffi`                        | X          | X      |
| `libfontconfig1`                | X          | X      |
| `libgcc`                        | X          | X      |
| `libgo`                         | X          | X      |
| `libgomp`                       | X          | X      |
| `libidn2`                       | X          | X      |
| `libnghttp2-14`                 | X          | X      |
| `libpcre2-8-0`                  | X          | X      |
| `libpng`                        | X          | X      |
| `libpsl`                        | X          | X      |
| `libssl3`                       | X          | X      |
| `libstdc++`                     | X          | X      |
| `libstdc++-dev`                 | X          | X      |
| `libtasn1`                      | X          | X      |
| `libunistring`                  | X          | X      |
| `libunwind`                     | X          | X      |
| `libuv`                         | X          | X      |
| `libxcrypt`                     | X          | X      |
| `libxcrypt-dev`                 | X          | X      |
| `libxml2`                       | X          | X      |
| `linux-headers`                 | X          | X      |
| `llvm18.1`                      | X          | X      |
| `lttng-ust`                     | X          | X      |
| `make`                          | X          | X      |
| `mpc`                           | X          | X      |
| `mpdecimal`                     | X          | X      |
| `mpfr`                          | X          | X      |
| `ncurses`                       | X          | X      |
| `ncurses-terminfo-base`         | X          | X      |
| `nodejs-22`                     | X          | X      |
| `npm`                           | X          | X      |
| `nss-db`                        | X          | X      |
| `nss-hesiod`                    | X          | X      |
| `openjdk-17-default-jvm`        | X          | X      |
| `openjdk-17-jre`                | X          | X      |
| `openjdk-17-jre-base`           | X          | X      |
| `p11-kit`                       | X          | X      |
| `p11-kit-trust`                 | X          | X      |
| `php-8.2`                       | X          | X      |
| `php-8.2-config`                | X          | X      |
| `pkgconf`                       | X          | X      |
| `pnpm`                          | X          | X      |
| `posix-cc-wrappers`             | X          | X      |
| `py3-attrs`                     | X          | X      |
| `py3-build`                     | X          | X      |
| `py3-cachecontrol`              | X          | X      |
| `py3-certifi`                   | X          | X      |
| `py3-cffi`                      | X          | X      |
| `py3-charset-normalizer`        | X          | X      |
| `py3-cleo`                      | X          | X      |
| `py3-crashtest`                 | X          | X      |
| `py3-cryptography`              | X          | X      |
| `py3-distlib`                   | X          | X      |
| `py3-dulwich`                   | X          | X      |
| `py3-filelock`                  | X          | X      |
| `py3-hashin`                    | X          | X      |
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
| `py3-pipenv`                    | X          | X      |
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
| `py3.12-pip`                    | X          | X      |
| `py3.12-setuptools`             | X          | X      |
| `python-3.12`                   | X          | X      |
| `python-3.12-base`              | X          | X      |
| `readline`                      | X          | X      |
| `renovate`                      | X          | X      |
| `ruby-3.2`                      | X          | X      |
| `ruby3.2-bundler`               | X          | X      |
| `rust-1.78`                     | X          | X      |
| `sqlite-libs`                   | X          | X      |
| `wget`                          | X          |        |
| `wolfi-base`                    | X          | X      |
| `wolfi-baselayout`              | X          | X      |
| `wolfi-keys`                    | X          | X      |
| `xz`                            | X          | X      |
| `yaml`                          | X          | X      |
| `yarn`                          | X          | X      |
| `zlib`                          | X          | X      |

