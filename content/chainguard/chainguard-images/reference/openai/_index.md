---
title: "Image Overview: openai"
linktitle: "openai"
type: "article"
layout: "single"
description: "Overview: openai Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/openai/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/openai/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/openai/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/openai/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image with the OpenAI CLI.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/openai:latest
```


<!--body:start-->
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
<!--body:end-->

