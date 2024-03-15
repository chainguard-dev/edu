---
title: "docker-selenium Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public docker-selenium Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-03-15 00:51:40
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/docker-selenium/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/docker-selenium/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/docker-selenium/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/docker-selenium/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **docker-selenium** Image.

|              | latest-dev                | latest                    |
|--------------|---------------------------|---------------------------|
| Default User | `root`                    | `root`                    |
| Entrypoint   | `/opt/bin/entry_point.sh` | `/opt/bin/entry_point.sh` |
| CMD          | not specified             | not specified             |
| Workdir      | not specified             | not specified             |
| Has apk?     | yes                       | no                        |
| Has a shell? | yes                       | yes                       |

Check the [tags history page](/chainguard/chainguard-images/reference/docker-selenium/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                     | latest-dev | latest |
|-------------------------------------|------------|--------|
| `Xvfb`                              | X          | X      |
| `alsa-lib`                          | X          | X      |
| `apk-tools`                         | X          |        |
| `at-spi2-core`                      | X          | X      |
| `avahi`                             | X          | X      |
| `bash`                              | X          | X      |
| `busybox`                           | X          | X      |
| `ca-certificates`                   | X          | X      |
| `ca-certificates-bundle`            | X          | X      |
| `cairo`                             | X          | X      |
| `chainguard-baselayout`             | X          | X      |
| `chromium`                          | X          | X      |
| `chromium-docker-selenium-compat`   | X          | X      |
| `coreutils`                         | X          | X      |
| `cups-libs`                         | X          | X      |
| `dbus-libs`                         | X          | X      |
| `docker-selenium`                   | X          | X      |
| `docker-selenium-supervisor-config` | X          | X      |
| `fftw-single-libs`                  | X          | X      |
| `fluxbox`                           | X          | X      |
| `font-ipa`                          | X          | X      |
| `font-liberation`                   | X          | X      |
| `font-misc-cyrillic`                | X          | X      |
| `font-noto-emoji`                   | X          | X      |
| `font-opensans`                     | X          | X      |
| `font-ubuntu`                       | X          | X      |
| `font-wqy-zenhei`                   | X          | X      |
| `fontconfig`                        | X          | X      |
| `fontconfig-config`                 | X          | X      |
| `freetype`                          | X          | X      |
| `fribidi`                           | X          | X      |
| `gdbm`                              | X          | X      |
| `giflib`                            | X          | X      |
| `git`                               | X          |        |
| `glib`                              | X          | X      |
| `glibc`                             | X          | X      |
| `glibc-locale-en`                   | X          | X      |
| `glibc-locale-posix`                | X          | X      |
| `graphite2`                         | X          | X      |
| `gst-plugins-base`                  | X          | X      |
| `gstreamer`                         | X          | X      |
| `harfbuzz`                          | X          | X      |
| `imlib2`                            | X          | X      |
| `java-cacerts`                      | X          | X      |
| `java-common`                       | X          | X      |
| `lcms2`                             | X          | X      |
| `ld-linux`                          | X          | X      |
| `libacl1`                           | X          | X      |
| `libasyncns`                        | X          | X      |
| `libatk-1.0`                        | X          | X      |
| `libatk-bridge-2.0`                 | X          | X      |
| `libattr1`                          | X          | X      |
| `libblkid`                          | X          | X      |
| `libbrotlicommon1`                  | X          | X      |
| `libbrotlidec1`                     | X          | X      |
| `libbz2-1`                          | X          | X      |
| `libcap`                            | X          | X      |
| `libcrypt1`                         | X          | X      |
| `libcrypto3`                        | X          | X      |
| `libcurl-openssl4`                  | X          |        |
| `libdaemon`                         | X          | X      |
| `libdrm`                            | X          | X      |
| `libelf`                            | X          | X      |
| `libevent`                          | X          | X      |
| `libexpat1`                         | X          | X      |
| `libfdisk`                          | X          | X      |
| `libffi`                            | X          | X      |
| `libflac`                           | X          | X      |
| `libfontconfig1`                    | X          | X      |
| `libfontenc`                        | X          | X      |
| `libgcc`                            | X          | X      |
| `libgcrypt`                         | X          | X      |
| `libgfortran`                       | X          | X      |
| `libgomp`                           | X          | X      |
| `libgpg-error`                      | X          | X      |
| `libice`                            | X          | X      |
| `libid3tag`                         | X          | X      |
| `libidn2`                           | X          |        |
| `libjpeg-turbo`                     | X          | X      |
| `libltdl`                           | X          | X      |
| `libmount`                          | X          | X      |
| `libnghttp2-14`                     | X          |        |
| `libnspr`                           | X          | X      |
| `libnss`                            | X          | X      |
| `libnss-tools`                      | X          | X      |
| `libogg`                            | X          | X      |
| `libpciaccess`                      | X          | X      |
| `libpcre2-8-0`                      | X          | X      |
| `libpng`                            | X          | X      |
| `libpsl`                            | X          |        |
| `libpulse`                          | X          | X      |
| `libsm`                             | X          | X      |
| `libsndfile`                        | X          | X      |
| `libssl3`                           | X          | X      |
| `libssp`                            | X          | X      |
| `libstdc++`                         | X          | X      |
| `libsystemd`                        | X          | X      |
| `libtasn1`                          | X          | X      |
| `libtheora`                         | X          | X      |
| `libunistring`                      | X          |        |
| `libuuid`                           | X          | X      |
| `libvncserver`                      | X          | X      |
| `libvorbis`                         | X          | X      |
| `libwebp`                           | X          | X      |
| `libx11`                            | X          | X      |
| `libxau`                            | X          | X      |
| `libxaw`                            | X          | X      |
| `libxcb`                            | X          | X      |
| `libxcomposite`                     | X          | X      |
| `libxdamage`                        | X          | X      |
| `libxdmcp`                          | X          | X      |
| `libxext`                           | X          | X      |
| `libxfixes`                         | X          | X      |
| `libxfont`                          | X          | X      |
| `libxft`                            | X          | X      |
| `libxi`                             | X          | X      |
| `libxinerama`                       | X          | X      |
| `libxkb`                            | X          | X      |
| `libxkbcommon`                      | X          | X      |
| `libxml2`                           | X          | X      |
| `libxmu`                            | X          | X      |
| `libxpm`                            | X          | X      |
| `libxrandr`                         | X          | X      |
| `libxrender`                        | X          | X      |
| `libxshmfence`                      | X          | X      |
| `libxt`                             | X          | X      |
| `libxtst`                           | X          | X      |
| `libxv`                             | X          | X      |
| `libxxf86vm`                        | X          | X      |
| `libzstd1`                          | X          | X      |
| `linux-pam`                         | X          | X      |
| `mcookie`                           | X          | X      |
| `mesa`                              | X          | X      |
| `mesa-gbm`                          | X          | X      |
| `mesa-gl`                           | X          | X      |
| `mesa-glapi`                        | X          | X      |
| `mpdecimal`                         | X          | X      |
| `ncurses`                           | X          | X      |
| `ncurses-terminfo-base`             | X          | X      |
| `net-tools`                         | X          | X      |
| `novnc`                             | X          | X      |
| `numpy`                             | X          | X      |
| `openblas`                          | X          | X      |
| `openjdk-11`                        | X          | X      |
| `openjdk-11-default-jvm`            | X          | X      |
| `openjdk-11-jre`                    | X          | X      |
| `openjdk-11-jre-base`               | X          | X      |
| `openssl-config`                    | X          | X      |
| `opus`                              | X          | X      |
| `orc`                               | X          | X      |
| `p11-kit`                           | X          | X      |
| `p11-kit-trust`                     | X          | X      |
| `pango`                             | X          | X      |
| `pixman`                            | X          | X      |
| `pulseaudio`                        | X          | X      |
| `py3-certifi`                       | X          | X      |
| `py3-charset-normalizer`            | X          | X      |
| `py3-idna`                          | X          | X      |
| `py3-jwcrypto`                      | X          | X      |
| `py3-requests`                      | X          | X      |
| `py3-simplejson`                    | X          | X      |
| `py3-urllib3`                       | X          | X      |
| `py3.12-setuptools`                 | X          | X      |
| `python-3.12`                       | X          | X      |
| `python-3.12-base`                  | X          | X      |
| `readline`                          | X          | X      |
| `selenium-server`                   | X          | X      |
| `selenium-server-compat`            | X          | X      |
| `soxr`                              | X          | X      |
| `speexdsp`                          | X          | X      |
| `sqlite-libs`                       | X          | X      |
| `sudo-rs`                           | X          | X      |
| `supervisor`                        | X          | X      |
| `systemd`                           | X          | X      |
| `tdb`                               | X          | X      |
| `tiff`                              | X          | X      |
| `ttf-dejavu`                        | X          | X      |
| `tzdata`                            | X          | X      |
| `wayland-libs-client`               | X          | X      |
| `wayland-libs-server`               | X          | X      |
| `websockify`                        | X          | X      |
| `wget`                              | X          |        |
| `wolfi-baselayout`                  | X          | X      |
| `x11vnc`                            | X          | X      |
| `xauth`                             | X          | X      |
| `xkbcomp`                           | X          | X      |
| `xkeyboard-config`                  | X          | X      |
| `xmessage`                          | X          | X      |
| `xvfb-run`                          | X          | X      |
| `xz`                                | X          | X      |
| `zlib`                              | X          | X      |

