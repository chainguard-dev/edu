---
title: "Getting Started with Apko"
type: "article"
description: "One-pager quickstart to get Apko up and running"
lead: "Getting started with Apko and building your first images"
date: 2021-07-06T08:49:31+00:00
lastmod: 2021-07-06T08:49:31+00:00
draft: false
images: []
menu:
  docs:
    parent: "apko"
weight: 630
toc: true
---

[Apko](http://github.com/chainguard-dev/apko) is an APK-based [OCI builder](https://opencontainers.org/) that uses a declarative language based on YAML files to define and build OCI-compatible base images. apko is compatible with Linux and Mac OS systems.

Using a declarative language to build such images has many advantages when compared to traditional Dockerfiles. Generally speaking, YAML definitions are easier to parse through and understand. This methodology facilitates automation and removes noise from image definitions, allowing users to "do more" with fewer lines of configuration.

Additionally, apko builds are fully reproducible and automatically generate [SBOM](https://en.wikipedia.org/wiki/Software_supply_chain) files for every image built, which adds a new layer of security to your images.

In this tutorial, you'll learn how to build images from YAML files, and how to run the generated tar images with Docker.

## Requirements

To follow this guide, you'll need Docker and Apko installed on your local system.

## Building a Basic Image from an YAML file

To test that you're able to build images, you can use one of the example `yaml` definition files that are included in the project. For this example, we'll use the `alpine-base.yaml` file that is defined as follows:

```yaml
contents:
  repositories:
    - https://dl-cdn.alpinelinux.org/alpine/edge/main
  packages:
    - alpine-base

cmd: /bin/sh -l

# optional environment configuration
environment:
  PATH: /usr/sbin:/sbin:/usr/bin:/bin

```

To build this image, run the following command from the apko prompt:

```shell
[apko] ❯ apko build examples/alpine-base.yaml apko-alpine:test apko-alpine.tar
```

```shell
2022/06/23 14:50:22 loading config file: examples/alpine-base.yaml
2022/06/23 14:50:22 apko (x86_64): building image 'apko-alpine:test'
2022/06/23 14:50:22 apko (x86_64): build context:
2022/06/23 14:50:22 apko (x86_64):   working directory: /tmp/apko-210217652
2022/06/23 14:50:22 apko (x86_64):   tarball path:
…
2022/06/23 14:50:23 apko (x86_64): running: /usr/sbin/chroot /tmp/apko-210217652 /bin/busybox --install -s
2022/06/23 14:50:23 apko (x86_64): generating supervision tree
2022/06/23 14:50:23 apko (x86_64): finished building filesystem in /tmp/apko-210217652
2022/06/23 14:50:23 apko (x86_64): built image layer tarball as /tmp/apko-4011354626.tar.gz
2022/06/23 14:50:23 apko (x86_64): generating SBOM
2022/06/23 14:50:23 apko (x86_64): generating SBOM
2022/06/23 14:50:23 building OCI image from layer '/tmp/apko-4011354626.tar.gz'
2022/06/23 14:50:23 OCI layer digest: sha256:0f7e5fe41003a3566f470bfdee659bf89905773914347b41e21d373fbfd75a19
2022/06/23 14:50:23 OCI layer diffID: sha256:94aabf0f74abb9da05ddb7a3ed52546d5c0399c19104dbe436888878f7f438f5
2022/06/23 14:50:23 output OCI image file to apko-alpine.tar
[apko] ❯

```

Now you can load the generated tar file into a Docker image and execute it. First, open another terminal window or exit the Apko shell with:

```shell
[apko] ❯ exit
```

To load the tar file into a Docker image, run:

```shell
docker load <  apko-alpine.tar
```

Now you can run the image with:

```shell
docker run -it apko-alpine:test
```

This will get you into a container running the apko-built image `apko-alpine:test`.

## Conclusion

In this guide, you installed and built your first images with apko. In the next part of this series, we'll have a more detailed look at the YAML files that create image definitions, what each directive means, and how to start creating custom OCI images with apko.

