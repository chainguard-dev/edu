---
title: "Image Overview: openai"
type: "article"
description: "Overview: openai Chainguard Image"
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

[cgr.dev/chainguard/openai](https://github.com/chainguard-images/images/tree/main/images/openai)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | August 4th   | `sha256:67dacc748a8f6cc54ddf98a156458375e75eaa49a3ee6168190317e1dec96f6a` |
|  `latest`     | August 4th   | `sha256:717cc49b91c3846153745dd6ea3d3b055464a21bb92ff2d675ac3cd8d2361355` |



Minimal image with the OpenAI CLI.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/openai:latest
```

This image requires the `OPENAI_API_KEY` environment variable to be set to work correctly.
You can obtain this directly from openai.com, and set it with the `-e` flag to `docker run`, or the `--env-file` flag to specify it as a file.

```shell
$ docker run -e OPENAI_API_KEY=$OPENAI_API_KEY cgr.dev/chainguard/openai api
usage: openai api [-h]
                  {engines.list,engines.get,engines.update,engines.generate,chat_completions.create,completions.create,deployments.list,deployments.get,deployments.delete,deployments.create,models.list,models.get,models.delete,files.create,files.get,files.delete,files.list,fine_tunes.list,fine_tunes.create,fine_tunes.get,fine_tunes.results,fine_tunes.events,fine_tunes.follow,fine_tunes.cancel,fine_tunes.delete,image.create,image.create_edit,image.create_variation,audio.transcribe,audio.translate}
                  ...

positional arguments:
  {engines.list,engines.get,engines.update,engines.generate,chat_completions.create,completions.create,deployments.list,deployments.get,deployments.delete,deployments.create,models.list,models.get,models.delete,files.create,files.get,files.delete,files.list,fine_tunes.list,fine_tunes.create,fine_tunes.get,fine_tunes.results,fine_tunes.events,fine_tunes.follow,fine_tunes.cancel,fine_tunes.delete,image.create,image.create_edit,image.create_variation,audio.transcribe,audio.translate}
                        All API subcommands

options:
  -h, --help            show this help message and exit
```

