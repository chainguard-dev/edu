---
title: "Image Overview: rabbitmq"
linktitle: "rabbitmq"
type: "article"
layout: "single"
description: "Overview: rabbitmq Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-03-01 12:14:22
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/rabbitmq/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/rabbitmq/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/rabbitmq/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/rabbitmq/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[RabbitMQ](https://github.com/rabbitmq/rabbitmq-server) RabbitMQ is a message broker.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/rabbitmq:latest
```
<!--getting:end-->

<!--body:start-->
## Using RabbitMQ

The default RabbitMQ port is 5672.
To run with Docker using default configuration:

```sh
docker run -p 5672:5672 --rm cgr.dev/chainguard/rabbitmq
2023-01-02 00:11:37.199274+00:00 [notice] <0.44.0> Application syslog exited with reason: stopped
2023-01-02 00:11:37.206489+00:00 [notice] <0.229.0> Logging: switching to configured handler(s); following messages may not be visible in this log output

  ##  ##      RabbitMQ 3.11.5
  ##  ##
  ##########  Copyright (c) 2007-2022 VMware, Inc. or its affiliates.
  ######  ##
  ##########  Licensed under the MPL 2.0. Website: https://rabbitmq.com

  Erlang:      25.2 [jit]
  TLS Library: OpenSSL - OpenSSL 3.0.7 1 Nov 2022
  Release series support status: supported

  Doc guides:  https://rabbitmq.com/documentation.html
  Support:     https://rabbitmq.com/contact.html
  Tutorials:   https://rabbitmq.com/getstarted.html
  Monitoring:  https://rabbitmq.com/monitoring.html

  Logs: /var/log/rabbitmq/rabbit@02bee2143fb7.log
        /var/log/rabbitmq/rabbit@02bee2143fb7_upgrade.log
        <stdout>

  Config file(s): (none)

  Starting broker... completed with 0 plugins.
```

## Configuration

RabbitMQ takes three configuration files: the rabbitmq configuration file, the advanced configuration file,
and the environment file.

These can be placed into the image at the following locations, or overridden with the corresponding
environment variables:

```shell
RABBITMQ_CONFIG_FILE=/etc/rabbitmq/rabbitmq.conf
RABBITMQ_ADVANCED_CONFIG_FILE=/etc/rabbitmq/advanced.config
RABBITMQ_CONF_ENV_FILE=/etc/rabbitmq/rabbitmq-env.conf
```

## Users and Directories

By default this image runs as a non-root user named `rabbitmq` with a uid of 65532.

Logs go to `/var/log/rabbitmq/` by default.
<!--body:end-->

