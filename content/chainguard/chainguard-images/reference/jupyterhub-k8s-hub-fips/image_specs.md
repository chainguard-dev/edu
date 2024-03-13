---
title: "jupyterhub-k8s-hub-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public jupyterhub-k8s-hub-fips Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-03-13 00:52:18
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jupyterhub-k8s-hub-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/jupyterhub-k8s-hub-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/jupyterhub-k8s-hub-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jupyterhub-k8s-hub-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **jupyterhub-k8s-hub-fips** Image.

|              | latest-dev                                                           | latest                                                               |
|--------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| Default User | `nonroot`                                                            | `nonroot`                                                            |
| Entrypoint   | `/sbin/tini --`                                                      | `/sbin/tini --`                                                      |
| CMD          | `jupyterhub --config /usr/local/etc/jupyterhub/jupyterhub_config.py` | `jupyterhub --config /usr/local/etc/jupyterhub/jupyterhub_config.py` |
| Workdir      | not specified                                                        | not specified                                                        |
| Has apk?     | yes                                                                  | no                                                                   |
| Has a shell? | yes                                                                  | no                                                                   |

Check the [tags history page](/chainguard/chainguard-images/reference/jupyterhub-k8s-hub-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                        | latest-dev | latest |
|----------------------------------------|------------|--------|
| `apk-tools`                            | X          |        |
| `bash`                                 | X          |        |
| `busybox`                              | X          |        |
| `c-ares`                               | X          | X      |
| `ca-certificates-bundle`               | X          | X      |
| `chainguard-baselayout`                | X          | X      |
| `configurable-http-proxy`              | X          | X      |
| `gdbm`                                 | X          | X      |
| `git`                                  | X          |        |
| `glibc`                                | X          | X      |
| `glibc-locale-posix`                   | X          | X      |
| `icu`                                  | X          | X      |
| `iptables`                             | X          | X      |
| `jupyterhub-k8s-hub`                   | X          | X      |
| `jupyterhub-k8s-hub-compat`            | X          | X      |
| `ld-linux`                             | X          | X      |
| `libbrotlicommon1`                     | X          | X      |
| `libbrotlidec1`                        | X          | X      |
| `libbrotlienc1`                        | X          | X      |
| `libbz2-1`                             | X          | X      |
| `libcrypt1`                            | X          | X      |
| `libcrypto3`                           | X          | X      |
| `libcurl-openssl4`                     | X          | X      |
| `libexpat1`                            | X          | X      |
| `libffi`                               | X          | X      |
| `libgcc`                               | X          | X      |
| `libidn2`                              | X          | X      |
| `libmnl`                               | X          | X      |
| `libnftnl`                             | X          | X      |
| `libnghttp2-14`                        | X          | X      |
| `libpcre2-8-0`                         | X          |        |
| `libpq-16`                             | X          | X      |
| `libpsl`                               | X          | X      |
| `libssl3`                              | X          | X      |
| `libstdc++`                            | X          | X      |
| `libunistring`                         | X          | X      |
| `libuv`                                | X          | X      |
| `linux-headers`                        | X          | X      |
| `llhttp`                               | X          | X      |
| `mpdecimal`                            | X          | X      |
| `ncurses`                              | X          | X      |
| `ncurses-terminfo-base`                | X          | X      |
| `nodejs-18`                            | X          | X      |
| `npm`                                  | X          | X      |
| `openssl-config-fipshardened`          | X          | X      |
| `openssl-provider-fips`                | X          | X      |
| `py3-aiohttp`                          | X          | X      |
| `py3-aiosignal`                        | X          | X      |
| `py3-alembic`                          | X          | X      |
| `py3-async-generator`                  | X          | X      |
| `py3-async-timeout`                    | X          | X      |
| `py3-asynctest`                        | X          | X      |
| `py3-attrs`                            | X          | X      |
| `py3-bcrypt`                           | X          | X      |
| `py3-certifi`                          | X          | X      |
| `py3-certipy`                          | X          | X      |
| `py3-cffi`                             | X          | X      |
| `py3-charset-normalizer`               | X          | X      |
| `py3-cryptography`                     | X          | X      |
| `py3-escapism`                         | X          | X      |
| `py3-frozenlist`                       | X          | X      |
| `py3-idna`                             | X          | X      |
| `py3-idna-ssl`                         | X          | X      |
| `py3-importlib-metadata`               | X          | X      |
| `py3-jinja2`                           | X          | X      |
| `py3-jsonschema`                       | X          | X      |
| `py3-jsonschema-specifications`        | X          | X      |
| `py3-jupyter-telemetry`                | X          | X      |
| `py3-jupyterhub`                       | X          | X      |
| `py3-jupyterhub-firstuseauthenticator` | X          | X      |
| `py3-jupyterhub-hmacauthenticator`     | X          | X      |
| `py3-jupyterhub-idle-culler`           | X          | X      |
| `py3-jupyterhub-kubespawner`           | X          | X      |
| `py3-jupyterhub-ldapauthenticator`     | X          | X      |
| `py3-jupyterhub-ltiauthenticator`      | X          | X      |
| `py3-jupyterhub-nativeauthenticator`   | X          | X      |
| `py3-jupyterhub-tmpauthenticator`      | X          | X      |
| `py3-kubernetes-asyncio`               | X          | X      |
| `py3-ldap3`                            | X          | X      |
| `py3-mako`                             | X          | X      |
| `py3-markupsafe`                       | X          | X      |
| `py3-multidict`                        | X          | X      |
| `py3-mwoauth`                          | X          | X      |
| `py3-nullauthenticator`                | X          | X      |
| `py3-oauthenticator`                   | X          | X      |
| `py3-oauthlib`                         | X          | X      |
| `py3-onetimepass`                      | X          | X      |
| `py3-packaging`                        | X          | X      |
| `py3-pamela`                           | X          | X      |
| `py3-parsing`                          | X          | X      |
| `py3-prometheus-client`                | X          | X      |
| `py3-psutil`                           | X          | X      |
| `py3-psycopg2`                         | X          | X      |
| `py3-pyasn1`                           | X          | X      |
| `py3-pycparser`                        | X          | X      |
| `py3-pycurl`                           | X          | X      |
| `py3-pyjwt`                            | X          | X      |
| `py3-pymysql`                          | X          | X      |
| `py3-pyopenssl`                        | X          | X      |
| `py3-python-dateutil`                  | X          | X      |
| `py3-python-editor`                    | X          | X      |
| `py3-python-json-logger`               | X          | X      |
| `py3-python-slugify`                   | X          | X      |
| `py3-pyyaml`                           | X          | X      |
| `py3-referencing`                      | X          | X      |
| `py3-requests`                         | X          | X      |
| `py3-requests-oauthlib`                | X          | X      |
| `py3-rpds-py`                          | X          | X      |
| `py3-ruamel-yaml`                      | X          | X      |
| `py3-six`                              | X          | X      |
| `py3-sqlalchemy`                       | X          | X      |
| `py3-sqlalchemy-cockroachdb`           | X          | X      |
| `py3-statsd`                           | X          | X      |
| `py3-text-unidecode`                   | X          | X      |
| `py3-tornado`                          | X          | X      |
| `py3-traitlets`                        | X          | X      |
| `py3-typing-extensions`                | X          | X      |
| `py3-urllib3`                          | X          | X      |
| `py3-yarl`                             | X          | X      |
| `py3-zipp`                             | X          | X      |
| `py3.12-setuptools`                    | X          | X      |
| `python-3.12`                          | X          | X      |
| `python-3.12-default`                  | X          | X      |
| `python-3.12-dev`                      | X          | X      |
| `python-3.12-dev-default`              | X          | X      |
| `readline`                             | X          | X      |
| `sqlite-libs`                          | X          | X      |
| `tini`                                 | X          | X      |
| `wget`                                 | X          |        |
| `wolfi-baselayout`                     | X          | X      |
| `xz`                                   | X          | X      |
| `zlib`                                 | X          | X      |

