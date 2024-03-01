---
title: "Image Overview: cassandra-reaper"
linktitle: "cassandra-reaper"
type: "article"
layout: "single"
description: "Overview: cassandra-reaper Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/cassandra-reaper/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cassandra-reaper/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/cassandra-reaper/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cassandra-reaper/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Automated Repair Awesomeness for Apache Cassandra
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/cassandra-reaper:latest
```
<!--getting:end-->

<!--body:start-->

## Overview

Cassandra Reaper is a tool for managing Apache Cassandra clusters. It helps operators to easily repair and run consistent backups of their clusters. It also provides a simple yet powerful web UI and a REST API for cluster monitoring and management.

## Usage

There is a Helm chart available for Cassandra Reaper [here](https://docs.k8ssandra.io/install/local/single-cluster-helm/). You just need to edit the `K8ssandraCluster` resource and add the following under the `.spec` section:

```
...
  reaper:
    containerImage:
      registry: cgr.dev
      repository: chainguard # you should provide only the repository name without the image name, it will be appended automatically
      tag: latest
    initContainerImage:
      registry: cgr.dev
      repository: chainguard
      tag: latest
    httpManagement:
      enabled: true
...
```

It is also possible to run Cassandra Reaper as a standalone Docker container:

```
docker container run -p 8080:8080 --platform linux/amd64 --pull always --rm cgr.dev/chainguard/cassandra-reaper:latest
```

You will see the Web UI at http://localhost:8080/webui.

<!--body:end-->

