---
title: "Image Overview: confluent-kafka"
linktitle: "confluent-kafka"
type: "article"
layout: "single"
description: "Overview: confluent-kafka Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/confluent-kafka/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/confluent-kafka/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/confluent-kafka/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/confluent-kafka/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
A Wolfi-based container image for the Community Edition of Confluent Kafka (cp-kafka), which extends Apache Kafka with additional features.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/confluent-kafka:latest
```


<!--body:start-->
Here's a basic example of how to launch a local instance of confluent-kafka in
KRaft mode:

```bash
docker run -it --rm \
  --name "${CONTAINER_NAME}" \
  -h kafka-kraft \
  -p "${KAFKA_PORT}":9092 \
  -e KAFKA_NODE_ID=1 \
  -e KAFKA_LISTENER_SECURITY_PROTOCOL_MAP='CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT' \
  -e KAFKA_ADVERTISED_LISTENERS='PLAINTEXT://kafka-kraft:29092,PLAINTEXT_HOST://localhost:9092' \
  -e KAFKA_JMX_PORT=9101 \
  -e KAFKA_JMX_HOSTNAME=localhost \
  -e KAFKA_PROCESS_ROLES='broker,controller' \
  -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 \
  -e KAFKA_CONTROLLER_QUORUM_VOTERS='1@kafka-kraft:29093' \
  -e KAFKA_LISTENERS='PLAINTEXT://kafka-kraft:29092,CONTROLLER://kafka-kraft:29093,PLAINTEXT_HOST://0.0.0.0:9092' \
  -e KAFKA_INTER_BROKER_LISTENER_NAME='PLAINTEXT' \
  -e KAFKA_CONTROLLER_LISTENER_NAMES='CONTROLLER' \
  -e CLUSTER_ID='MkU3OEVBNTcwNTJENDM2Qk' \
  cgr.dev/chainguard/confluent-kafka:latest
```

Please refer to the [upstream documentation](https://docs.confluent.io/platform/current/installation/docker/installation.html), for guidiance on how to run and configure.
<!--body:end-->

