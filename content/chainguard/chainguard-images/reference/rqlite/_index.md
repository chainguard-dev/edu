---
title: "Image Overview: rqlite"
linktitle: "rqlite"
type: "article"
layout: "single"
description: "Overview: rqlite Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2023-11-27 16:34:14
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/rqlite/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/rqlite/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/rqlite/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/rqlite/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image with rqlite. **EXPERIMENTAL**
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/rqlite:latest
```
<!--getting:end-->

<!--body:start-->
## Using Vault

The Chainguard Vault image contains the `rqlite` and `rqlited` server binaries.
The default entrypoint uses the `docker-entrypoint.sh` script from the `rqlite` project.


To run the `rqlite` program:

```shell
% docker run cgr.dev/chainguard/rqlite rqlite
[rqlited] 2023/03/26 21:53:22 rqlited starting, version 7, SQLite 3.39.4, commit unknown, branch unknown, compiler gc
[rqlited] 2023/03/26 21:53:22 go1.20.2, target architecture is arm64, operating system target is linux
[rqlited] 2023/03/26 21:53:22 launch command: /usr/bin/rqlited -node-id d3d5c2306506 -http-addr 0.0.0.0:4001 -http-adv-addr d3d5c2306506:4001 -raft-addr 0.0.0.0:4002 -raft-adv-addr d3d5c2306506:4002 /rqlite/file/data

            _ _ _
           | (_) |
  _ __ __ _| |_| |_ ___
 | '__/ _  | | | __/ _ \   The lightweight, distributed
 | | | (_| | | | ||  __/   relational database.
 |_|  \__, |_|_|\__\___|
         | |               www.rqlite.io
         |_|

[rqlited] 2023/03/26 21:53:22 Raft TCP mux Listener registered with byte header 1
[rqlited] 2023/03/26 21:53:22 no preexisting node state detected in /rqlite/file/data, node may be bootstrapping
[cluster] 2023/03/26 21:53:22 service listening on d3d5c2306506:4002
```
<!--body:end-->

