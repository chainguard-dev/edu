---
title: "Image Overview: gptscript"
linktitle: "gptscript"
type: "article"
layout: "single"
description: "Overview: gptscript Chainguard Image"
date: 2024-03-08 00:56:03
lastmod: 2024-03-08 00:56:03
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/gptscript/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gptscript/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/gptscript/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gptscript/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal [gptscript](https://github.com/gptscript-ai/gptscript) container image.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/gptscript:latest
```
<!--getting:end-->

<!--body:start-->

## Usage

Before using our gptscript image, you'll need an [OpenAI API key](https://platform.openai.com/api-keys).

After retrieving your key, run the container with the following command:

```bash
docker run -e "OPENAI_API_KEY=<YOUR OPENAI API KEY>" cgr.dev/chainguard/gptscript:latest
```

Azure OpenAI may also be used:

```bash
docker run \
  -e "OPENAI_API_KEY=<YOUR API KEY>" \
  -e "OPENAI_BASE_URL=<YOUR ENDPOINT>" \
  -e "OPENAI_API_TYPE=AZURE" \
  -e "OPENAI_AZURE_DEPLOYMENT=<YOUR DEPLOYMENT NAME>" \
  cgr.dev/chainguard/gptscript:latest
```

To run a basic hello world test, run the following:

```bash
docker run -e "OPENAI_API_KEY=<YOUR OPENAI API KEY>" cgr.dev/chainguard/gptscript:latest  https://get.gptscript.ai/echo.gpt --input 'Hello, World!'
```

<!--body:end-->

