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

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 18th    | `sha256:367d3fe5273e91fad58a68d0a991667aa354552bc1465c312f7c4f066eb3d2f5` |
|  `latest`     | July 14th    | `sha256:dace90619be53774a9f1c9844e5e442f5d8607bfadfb5a1e0c8e52dbd0d2c370` |
|               | July 12th    | `sha256:911565f82de2d87c47d7c1b2e17f7d3bf4fed9f41037187de1a3ed7d3083eb14` |
|               | July 8th     | `sha256:6a3e8c048b6449885f7d9790015a5fa3ece3bc22d298a190712eb0e7841250b8` |
|               | July 8th     | `sha256:021f10a8ea302aa15227f290adfb25a8b7175fdee9d5de6e420c6e15ca9c1b79` |
|               | July 8th     | `sha256:794e6a3a1c73955624e312de6fe81f1f16fa3a6c794dc5c44c669877dca909ae` |
|               | July 8th     | `sha256:d3447c8c2e0a3928aaae067f1eeda104986fc039a3d1690350fa1f6dc08fdfaf` |
|               | June 27th    | `sha256:4fc5b5d96f5f8e7a0903935d053ed1ac936d5b1ccdc1df25914805e625f9a598` |
|               | June 27th    | `sha256:e7b20af974ca407441bb1cbdf1e4074c76ba2b309f4a681a067a930d58549bfd` |
|               | June 26th    | `sha256:ace8da0bbf202dd3dd84b00a11d3d34e860cfdc7c1926d0c4c74de1002070223` |
|               | June 26th    | `sha256:ff16c53cb4d88289117d6d10f22fcf9b9184e78891248be23c628534398d5d47` |



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

