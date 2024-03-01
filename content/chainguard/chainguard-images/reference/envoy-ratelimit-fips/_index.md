---
title: "Image Overview: envoy-ratelimit-fips"
linktitle: "envoy-ratelimit-fips"
type: "article"
layout: "single"
description: "Overview: envoy-ratelimit-fips Chainguard Image"
date: 2024-02-29 16:25:55
lastmod: 2024-02-29 16:25:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/envoy-ratelimit-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/envoy-ratelimit-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/envoy-ratelimit-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/envoy-ratelimit-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
 Go/gRPC service designed to enable generic rate limit scenarios from different types of applications.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/envoy-ratelimit:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

This image should be a drop-in replacement for the upstream `envoyproxy/ratelimit` image.
See the [full documentation](https://gateway.envoyproxy.io/latest/user/rate-limit.html) for installation and usage.

See for the [examples](https://github.com/envoyproxy/ratelimit#examples).

This image includes `ratelimit`.
<!--body:end-->

