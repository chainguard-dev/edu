---
title: "Image Overview: erlang"
linktitle: "erlang"
type: "article"
layout: "single"
description: "Overview: erlang Chainguard Image"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/erlang/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/erlang/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/erlang/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/erlang/provenance_info/" >}}
{{</ tabs >}}



Container image for building Erlang applications.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/erlang:latest
```

## Usage

The image can be used to run the `erl` tool, or to compile and run Erlang scripts.

For example, a simple Hello World script in Erlang, `hello.erl`:

```
-module(hello).
-export([hello_world/0]).

hello_world() -> io:fwrite("hello, world\n").
```

can be compiled in Docker with:

```
FROM cgr.dev/chainguard/erlang
COPY . .
RUN erlc hello-world.erl
ENTRYPOINT [ "erl" ]
CMD [ "-noshell", "-eval", "hello:hello_world().", "-s", "init", "stop" ]
```

Running this image should output `hello, world`.

