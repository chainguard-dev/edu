---
title: "Image Overview: erlang-fips"
linktitle: "erlang-fips"
type: "article"
layout: "single"
description: "Overview: erlang-fips Chainguard Image"
date: 2024-03-20 01:10:09
lastmod: 2024-03-20 01:10:09
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/erlang-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/erlang-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/erlang-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/erlang-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Container image for building Erlang applications.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/erlang:latest
```
<!--getting:end-->

<!--body:start-->
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
<!--body:end-->

