---
title: "Image Overview: request-1303"
linktitle: "request-1303"
type: "article"
layout: "single"
description: "Overview: request-1303 Chainguard Image"
date: 2024-03-06 00:47:02
lastmod: 2024-03-06 00:47:02
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/request-1303/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/request-1303/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/request-1303/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/request-1303/provenance_info/" >}}
{{</ tabs >}}

# Bundled Cassandra Image

A custom image request for `c3.ai`, provides a `bundled` container image,
containing `cassandra` and multiple supporting applications.

## Image contents

This bundled image contains the following packages:

- cass-config-builder
- cass-operator-fips
- k8ssandra-system-logger-fips
- k8ssandra-operator-fips
- management-api-for-apache-cassandra
- cassandra-medusa
- cassandra-reaper-fips

> [!NOTE]
> You may notice that some of the packages do not have a `-fips` suffix. These are Java images which can not be made FIPS compliant, but are still packaged using a bcfips JDK image, as requested.

## Important Changes

* `cass-config-builder` uses `openjdk-11` instead of `openjdk-8`
* `k8ssandra-operator-fips` binary located at `/usr/bin/k8ssandra-operator-fips-manager` and `/manager` path no longer exists
* `cass-operator-fips` binary located at `/usr/bin/cass-operator-fips-manager` and `/manager` path no longer exists
* `management-api-for-apache-cassandra` uses `nonroot` as a `user` and `group` instead of `cassandra`, and the `uid` and `gid` are set to `65532` instead of `999`
* `cassandra-medusa` uses `nonroot` as a `user` and `group` instead of `cassandra`, and the `uid` and `gid` are set to `65532` instead of `999`

## Running the packages

### `cass-config-builder`

Refer to the [cass-config-builder](https://github.com/chainguard-images/images/blob/main/images/cass-config-builder/README.md)
image documentation for more information.

Entrypoint:

```shell
/usr/local/bin/entrypoint
```

Example using Docker:

```shell
docker run --entrypoint /usr/local/bin/entrypoint cgr.dev/c3.ai/bundled-cassandra-jre-bcfips:latest
```

### `cass-operator-fips`

Refer to the [cass-operator](https://github.com/chainguard-images/images/blob/main/images/cass-operator/README.md)
image documentation for more information.

Entrypoint:

```shell
/usr/bin/cass-operator-fips-manager
```

Example using Docker:

```shell
docker run --entrypoint /usr/bin/cass-operator-fips-manager cgr.dev/c3.ai/bundled-cassandra-jre-bcfips:latest
```

### `k8ssandra-system-logger-fips`

Entrypoint:

```shell
/usr/bin/vector
```

Example using Docker:

```shell
docker run --entrypoint /usr/bin/vector cgr.dev/c3.ai/bundled-cassandra-jre-bcfips:latest
```

### `k8ssandra-operator-fips`

Refer to the [k8ssandra-operator](https://github.com/chainguard-images/images/blob/main/images/k8ssandra-operator/README.md)
image documentation for more information.

Entrypoint:

```shell
/usr/bin/k8ssandra-operator-fips-manager
```

Example using Docker:

```shell
docker run --entrypoint /usr/bin/k8ssandra-operator-fips-manager cgr.dev/c3.ai/bundled-cassandra-jre-bcfips:latest
```

### `management-api-for-apache-cassandra`

Refer to the [management-api-for-apache-cassandra](https://github.com/chainguard-images/images/blob/main/images/management-api-for-apache-cassandra/README.md)
image documentation for more information.

Entrypoint:

```shell
/docker-entrypoint.sh
```

Example using Docker:

```shell
docker run --entrypoint /docker-entrypoint.sh cgr.dev/c3.ai/bundled-cassandra-jre-bcfips:latest
```

### `cassandra-medusa`

Refer to the [cassandra-medusa](https://github.com/chainguard-images/images/blob/main/images/cassandra-medusa/README.md)
image documentation for more information.

Entrypoint:

```shell
MEDUSA_MODE=GRPC /home/cassandra/docker-entrypoint.sh
```

The error `No such file or directory: '/etc/medusa/medusa.ini'` is expected since it need be created by Kustomization plugin or manually.

Example using Docker:

```shell
docker run -e MEDUSA_MODE='GRPC' --entrypoint /home/cassandra/docker-entrypoint.sh cgr.dev/c3.ai/bundled-cassandra-jre-bcfips:latest
```

### `cassandra-reaper`

Refer to the [cassandra-reaper](https://github.com/chainguard-images/images/blob/main/images/cassandra-reaper/README.md)
image documentation for more information.

Entrypoint:

```shell
/usr/local/bin/entrypoint.sh
```

Example using Docker:

```shell
docker run --entrypoint /usr/local/bin/entrypoint.sh cgr.dev/c3.ai/bundled-cassandra-jre-bcfips:latest cassandra-reaper
```

## Architecture

This image is built only for the `linux/amd64` architecture. It's because of some of the packages are not available for other architectures. (i.e., `cassandra-reaper`)

## Entrypoint

No `entrypoint` is configured for this image. The executable path will need to be passed when running the image, to launch the approperiate application.

## Working Directory

The working directory for the image is `/`

## Default user

This image is configured to run as the `nonroot` user.

## Image versioning

This image produces a 'latest' tagged image, as well as a tagged image using the Cassandra package version.
