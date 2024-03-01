---
title: "Image Overview: management-api-for-apache-cassandra"
linktitle: "management-api-for-apache-cassandra"
type: "article"
layout: "single"
description: "Overview: management-api-for-apache-cassandra Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/management-api-for-apache-cassandra/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/management-api-for-apache-cassandra/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/management-api-for-apache-cassandra/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/management-api-for-apache-cassandra/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
RESTful / Secure Management Sidecar for Apache Cassandra
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/management-api-for-apache-cassandra:latest
```
<!--getting:end-->

<!--body:start-->

# Usage

You can run the Management API as a standalone Docker container:

 > docker run -p 8080:8080 -it --rm cgr.dev/chainguard/management-api-for-apache-cassandra:latest

 > curl http://localhost:8080/api/v0/probes/liveness
 OK

 # Check service and C* are running
 > curl http://localhost:8080/api/v0/probes/readiness
 OK

<!--body:end-->

