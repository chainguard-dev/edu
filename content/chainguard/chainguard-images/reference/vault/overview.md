---
title: "Image Overview: vault"
type: "article"
description: "Overview: vault Chainguard Images"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "images-reference"
weight: 500
toc: true
---

`experimental` [cgr.dev/chainguard/vault](https://github.com/chainguard-images/images/tree/main/images/vault)
| Tags         | Aliases                                            |
|--------------|----------------------------------------------------|
| `latest`     | `1`, `1.13`, `1.13.2`, `1.13.2-r2`                 |
| `latest-dev` | `1-dev`, `1.13-dev`, `1.13.2-dev`, `1.13.2-r2-dev` |



Minimal image with Vault. **EXPERIMENTAL**

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/vault:latest
```

## Using Vault

The Chainguard Vault image contains the `vault` server binary.
The default entrypoint uses the `serve -dev` flag, which stands up a single-node instance for testing and development.

DO NOT use this in production!

```shell
$ docker run cgr.dev/chainguard/vault
==> Vault server configuration:

             Api Address: http://127.0.0.1:8200
                     Cgo: disabled
         Cluster Address: https://127.0.0.1:8201
   Environment Variables: GODEBUG, HOME, HOSTNAME, PATH, SSL_CERT_FILE
              Go Version: go1.20.1
              Listener 1: tcp (addr: "127.0.0.1:8200", cluster address: "127.0.0.1:8201", max_request_duration: "1m30s", max_request_size: "33554432", tls: "disabled")
               Log Level: info
                   Mlock: supported: true, enabled: false
           Recovery Mode: false
                 Storage: inmem
                 Version: Vault v1.12.3, built 1970-01-01T00:00:00Z
             Version Sha: 209b3dd99fe8ca320340d08c70cff5f620261f9b

==> Vault server started! Log data will stream in below:
```

Instead, supply a vault configuration file and override this using the container command, for example:

```shell
$ docker run cgr.dev/chainguard/vault serve -config /etc/vault.hcl
```

Note that some configurations (including the default included in this image at that location) will require extra capabilities, specifically `CAP_IPC_LOCK`.

To use this with Docker:

```shell
$ docker run --cap-add CAP_IPC_LOCK cgr.dev/chainguard/vault server -config /etc/vault.hcl
==> Vault server configuration:

             Api Address: http://127.0.0.1:8200
                     Cgo: disabled
         Cluster Address: https://127.0.0.1:8201
   Environment Variables: GODEBUG, HOME, HOSTNAME, PATH, SSL_CERT_FILE
              Go Version: go1.20.1
              Listener 1: tcp (addr: "127.0.0.1:8200", cluster address: "127.0.0.1:8201", max_request_duration: "1m30s", max_request_size: "33554432", tls: "disabled")
               Log Level: info
                   Mlock: supported: true, enabled: true
           Recovery Mode: false
                 Storage: file
                 Version: Vault v1.12.3, built 1970-01-01T00:00:00Z
             Version Sha: 209b3dd99fe8ca320340d08c70cff5f620261f9b

2023-03-18T16:13:52.564Z [INFO]  proxy environment: http_proxy="" https_proxy="" no_proxy=""
2023-03-18T16:13:52.639Z [INFO]  core: Initializing version history cache for core
==> Vault server started! Log data will stream in below:
```

