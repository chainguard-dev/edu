---
title: "Image Overview: rqlite"
type: "article"
description: "Overview: rqlite Chainguard Image"
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

[cgr.dev/chainguard/rqlite](https://github.com/chainguard-images/images/tree/main/images/rqlite)

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` | September 4th | `sha256:56bf1749b0c2ea3c05f2a661bdc95b1086659263213c24b56c65c3a3a90fead7` |
|  `latest`     | September 4th | `sha256:ce63052a88d2bad2eaf33d5d406d598617f771ddc1c08980a9c9ae579b06abff` |



Minimal image with rqlite. **EXPERIMENTAL**

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/rqlite:latest
```

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

