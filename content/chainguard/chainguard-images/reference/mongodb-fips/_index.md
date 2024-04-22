---
title: "Image Overview: mongodb-fips"
linktitle: "mongodb-fips"
type: "article"
layout: "single"
description: "Overview: mongodb-fips Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-04-22 00:45:38
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/mongodb-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/mongodb-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/mongodb-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/mongodb-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
The MongoDB Database image
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/mongodb-fips:latest
```


<!--body:start-->
## Using MongoDB
```shell
$ docker run cgr.dev/chainguard/mongodb
```

Connect to the MongoDB Deployment with mongosh and confirm your MongoDB instance is running by inserting a new document

```shell
$ mongosh --port 27017
$test> db.products.insert( { item: "card", qty: 15 } )
{
  acknowledged: true,
  insertedIds: { '0': ObjectId('662141e9a1519b8bd2ac3fc4') }
}
$test> show collections
products

```
<!--body:end-->

