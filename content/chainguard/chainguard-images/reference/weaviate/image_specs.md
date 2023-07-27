---
title: "Weaviate Image Variants"
type: "article"
description: "Detailed information about the Weaviate Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Weaviate"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Weaviate** Image.

## Variants Compared
The **weaviate** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                                     | latest-dev                                 |
|--------------|--------------------------------------------|--------------------------------------------|
| Default User | `weaviate`                                 | `weaviate`                                 |
| Entrypoint   | `/bin/weaviate`                            | `/bin/weaviate`                            |
| CMD          | `--host 0.0.0.0 --port 8080 --scheme http` | `--host 0.0.0.0 --port 8080 --scheme http` |
| Workdir      | not specified                              | not specified                              |
| Has apk?     | no                                         | yes                                        |
| Has a shell? | no                                         | yes                                        |

Check the [tags history page](/chainguard/chainguard-images/reference/weaviate/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|            | latest | latest-dev |
|------------|--------|------------|
| `weaviate` | X      | X          |
| `openssl`  | X      | X          |
