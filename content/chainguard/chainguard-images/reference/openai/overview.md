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
|  `latest`     | August 15th  | `sha256:ec2bd48a5b4c46aff26ed699281df05ba67f14884ee8f16b120ff746b3f7e2fa` |
|  `latest-dev` | August 15th  | `sha256:077eb636a99a7667de5d1c163133e9d3efde08f935d73f510d354232e4c459b9` |



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

