---
title: "Image Overview: cassandra"
linktitle: "cassandra"
type: "article"
layout: "single"
description: "Overview: cassandra Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-05-23 00:45:07
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/cassandra/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cassandra/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/cassandra/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cassandra/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[Cassandra](https://cassandra.apache.org) is a free and open-source, distributed, wide-column store, NoSQL database.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/cassandra:latest
```


<!--body:start-->

## Deploying
Deploy a new instance of Cassandra using this image:

```bash
docker run -d \
  --name cassandra \
  -e CASSANDRA_START_RPC=true \
  -p 9042:9042 cgr.dev/chainguard/cassandra:latest
```

You can use `nodetool status` command to check if Cassandra is running properly.
Note, it'll take a couple of minutes for Cassandra to become fully operational:

```bash
docker exec -it cassandra nodetool status

Datacenter: datacenter1
=======================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address    Load        Tokens  Owns (effective)  Host ID                               Rack
UN  127.0.0.1  104.38 KiB  16      100.0%            0e75f72d-d273-4fac-807e-2b230583458c  rack1
```

`cqlsh` is available on the image:

```bash
docker exec -i cassandra cqlsh -e "
CREATE KEYSPACE testkeyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
USE testkeyspace;
CREATE TABLE users (user_id UUID PRIMARY KEY, name text);
INSERT INTO users (user_id, name) VALUES (uuid(), 'Chainguard');
SELECT * FROM users;
"

 user_id                              | name
--------------------------------------+------------
 3f13c6b4-4a22-4de7-a1f6-a3ac6e887ddb | Chainguard
 67e3be15-07f9-4dd6-b9b9-c00037d705ac | Chainguard

(2 rows)
```

For more information, refer to the [Cassandra documentation](https://cassandra.apache.org/_/quickstart.html).

<!--body:end-->

