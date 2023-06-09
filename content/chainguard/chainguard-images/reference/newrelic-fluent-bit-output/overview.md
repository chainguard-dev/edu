---
title: "Image Overview: newrelic-fluent-bit-output"
type: "article"
description: "Overview: newrelic-fluent-bit-output Chainguard Images"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "images-reference"
weight: 500
toc: true
---

`stable` [cgr.dev/chainguard/newrelic-fluent-bit-output](https://github.com/chainguard-images/images/tree/main/images/newrelic-fluent-bit-output)
| Tags         | Aliases                                            |
|--------------|----------------------------------------------------|
| `latest`     | `1`, `1.16`, `1.16.0`, `1.16.0-r3`                 |
| `latest-dev` | `1-dev`, `1.16-dev`, `1.16.0-dev`, `1.16.0-r3-dev` |



The newrelic-fluent-bit-output plugin forwards output to New Relic. Minimal [newrelic-fluent-bit-output](https://github.com/newrelic/newrelic-fluent-bit-output) container image.

## Get It

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/newrelic-fluent-bit-output
```

## Usage

Fluent Bit needs to know the location of the New Relic output plugin. We already added the plugin to the image, so you just need to tell Fluent Bit where to find it which is "/fluent-bit/bin/out_newrelic.so" in the image.

Add the following to your Fluent Bit configuration file and save it as `fluent-bit.conf`:

```ini
[INPUT]
    Name tail
    Path /path/to/your/log/file

[OUTPUT]
    Name newrelic
    Match *
    licenseKey <NEW_RELIC_LICENSE_KEY>

[FILTER]
    Name modify
    Match *
    Add hostname <HOSTNAME>
    Add service_name <SERVICE_NAME>
```

Then run Fluent Bit with the following command:

```shell
docker run -v /path/to/your/config/file:/fluent-bit/etc/fluent-bit.conf:ro -v /path/to/your/log/file:/path/to/your/log/file:ro cgr.dev/chainguard/newrelic-fluent-bit-output -c /fluent-bit/etc/fluent-bit.conf -e /fluent-bit/bin/out_newrelic.so
```

