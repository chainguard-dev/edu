---
title: "Image Overview: fluentd"
type: "article"
description: "Overview: fluentd Chainguard Image"
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

[cgr.dev/chainguard/fluentd](https://github.com/chainguard-images/images/tree/main/images/fluentd)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | August 3rd   | `sha256:f6b0e31348796d10de973d96c6ed63d50c46a9a05e18737541b2e9f5c31068fb` |
|  `latest`     | August 3rd   | `sha256:0e94bf73c99a1bd918f9cf83bd305a67480235b371dcbfa81190c7edc573e13b` |



Fluentd: Unified Logging Layer (project under CNCF)

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/fluentd
```

## Using fluentd

Run a Fluentd instance that will receive messages over TCP port 24224 through the Forward protocol, and send the messages to the STDOUT interface in JSON format

Run the fluentd container and mount the fluent.conf in [examples/](https://github.com/chainguard-images/images/tree/main/images/fluentd/examples)

```sh
docker run --rm -p 127.0.0.1:24224:24224 -v ${PWD}/examples/basic_docker.conf:/etc/fluent/fluent.conf cgr.dev/chainguard/fluentd
```

In another terminal try sending some logs to fluentd with another container

```sh
docker run --rm --log-driver=fluentd --log-opt tag="docker.{{.ID}}" cgr.dev/chainguard/wolfi-base echo 'Hello Fluentd!'
```

The Fluentd container should receive the message and print it to stdout:

```sh
2023-02-24 17:06:32 +0000 [info]: starting fluentd-1.15.3 pid=1 ruby="3.2.0"
2023-02-24 17:06:32 +0000 [info]: spawn command to main:  cmdline=["/usr/bin/ruby", "-Eascii-8bit:ascii-8bit", "/usr/bin/fluentd", "--under-supervisor"]
2023-02-24 17:06:32 +0000 [info]: init supervisor logger path=nil rotate_age=nil rotate_size=nil
2023-02-24 17:06:32 +0000 [info]: #0 init worker0 logger path=nil rotate_age=nil rotate_size=nil
2023-02-24 17:06:32 +0000 [info]: adding match pattern="*.*" type="stdout"
2023-02-24 17:06:32 +0000 [info]: adding source type="forward"
2023-02-24 17:06:32 +0000 [warn]: #0 define <match fluent.**> to capture fluentd logs in top level is deprecated. Use <label @FLUENT_LOG> instead
2023-02-24 17:06:32 +0000 [info]: #0 starting fluentd worker pid=11 ppid=1 worker=0
2023-02-24 17:06:32 +0000 [info]: #0 listening port port=24224 bind="0.0.0.0"
2023-02-24 17:06:32 +0000 [info]: #0 fluentd worker is now running worker=0
2023-02-24 17:06:32.824499403 +0000 fluent.info: {"pid":11,"ppid":1,"worker":0,"message":"starting fluentd worker pid=11 ppid=1 worker=0"}
2023-02-24 17:06:32.824689854 +0000 fluent.info: {"port":24224,"bind":"0.0.0.0","message":"listening port port=24224 bind=\"0.0.0.0\""}
2023-02-24 17:06:32.825323737 +0000 fluent.info: {"worker":0,"message":"fluentd worker is now running worker=0"}
2023-02-24 17:06:54.000000000 +0000 docker.eb2613ef91b4: {"container_id":"eb2613ef91b4fa0989b7af9f3b1310bc4de6c13aae5ee42901d553e81b575045","container_name":"/focused_fermat","source":"stdout","log":"Hello Fluentd!"}
```

## Using the -dev variant

The `-dev` variant contains a shell and tools like `apk` to allow users to easily debug and modify the image. The `-dev` variant uses the same entrypoint as the regular image so if you want to get a shell make sure to override the entrypoint like so.

```sh
docker run --rm --entrypoint 'sh' cgr.dev/chainguard/fluentd
```

