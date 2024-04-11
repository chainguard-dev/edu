---
title: "Image Overview: shadowsocks-rust-sslocal"
linktitle: "shadowsocks-rust-sslocal"
type: "article"
layout: "single"
description: "Overview: shadowsocks-rust-sslocal Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu: 
  docs: 
    parent: "images-reference"
weight: 500
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/shadowsocks-rust-sslocal/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/shadowsocks-rust-sslocal/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/shadowsocks-rust-sslocal/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/shadowsocks-rust-sslocal/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Shadowsocks-rust is a Rust implementation of the Shadowsocks protocol, aimed at ensuring secure and private internet access by encrypting connections and circumventing internet restrictions.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/shadowsocks-rust-sslocal:latest
```


<!--body:start-->
## Usage

Create a configuration file `config.json`:

```bash
cat <<EOF > config.json
{
    "server": "127.0.0.1",
    "server_port": 8388,
    "local_port": 1080,
    "local_address": "127.0.0.1",
    "password": "password",
    "timeout": 300,
    "method": "aes-256-gcm"
}
EOF
```

* Start the `sslocal`:

```bash
docker run \
  --name sslocal-rust \
  --restart always \
  -p 1080:1080/tcp \
  -v /path/to/config.json:/etc/shadowsocks-rust/config.json \
  -dit cgr.dev/chainguard/shadowsocks-rust-ssserver:latest
```

* Start the `ssserver`:

```bash
docker run \
  --name ssserver-rust \
  --restart always \
  -p 8388:8388/tcp \
  -p 8388:8388/udp \
  -v /path/to/config.json:/etc/shadowsocks-rust/config.json \
  -dit cgr.dev/chainguard/shadowsocks-rust-sslocal:latest
```

Jump to the official [Getting Started](https://github.com/shadowsocks/shadowsocks-rust?tab=readme-ov-file#getting-started) guide for more detailed usage.
<!--body:end-->

