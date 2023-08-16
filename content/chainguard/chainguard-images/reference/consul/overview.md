---
title: "Image Overview: consul"
type: "article"
description: "Overview: consul Chainguard Image"
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

[cgr.dev/chainguard/consul](https://github.com/chainguard-images/images/tree/main/images/consul)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | August 15th  | `sha256:155a1bc310943d2031e10bf0622583557025dd3d1b32e3446b1bb1625e1de20c` |
|  `latest-dev` | August 15th  | `sha256:adcb9dc3d5c020c043228d9e7f74c7e9eda3bd9c8a31405351e5a99674eafd77` |



Minimal image with Consul. **EXPERIMENTAL**

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/consul:latest
```

## Using Consul

The Chainguard Consul image contains the `consul` binary and a `docker-entrypoint.sh` script.

This script expects to be run as `root` and uses `su-exec` to drop permissions to a `consul` user itself.
The default entrypoint uses the entrypoint script.


```shell
$ docker run cgr.dev/chainguard/consul
==> Starting Consul agent...
              Version: '1.15.2'
           Build Date: '2023-03-30 17:51:19 +0000 UTC'
              Node ID: '82ed4fdf-4602-c15b-6547-6a85588a0de4'
            Node name: 'd1503dbb6c54'
           Datacenter: 'dc1' (Segment: '<all>')
               Server: true (Bootstrap: false)
          Client Addr: [0.0.0.0] (HTTP: 8500, HTTPS: -1, gRPC: 8502, gRPC-TLS: 8503, DNS: 8600)
         Cluster Addr: 127.0.0.1 (LAN: 8301, WAN: 8302)
    Gossip Encryption: false
     Auto-Encrypt-TLS: false
            HTTPS TLS: Verify Incoming: false, Verify Outgoing: false, Min Version: TLSv1_2
             gRPC TLS: Verify Incoming: false, Min Version: TLSv1_2
     Internal RPC TLS: Verify Incoming: false, Verify Outgoing: false (Verify Hostname: false), Min Version: TLSv1_2

==> Log data will now stream in as it occurs:
```

