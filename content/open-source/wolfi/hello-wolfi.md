---
title: "Hello Wolfi Workshop Kit"
type: "article"
description: "Community workshop kit about Wolfi for beginners"
date: 2022-12-19T08:49:31+00:00
lastmod: 2022-12-19T08:49:31+00:00
draft: false
tags: ["Wolfi", "Workshop Kit"]
images: []
menu:
  docs:
    parent: "wolfi"
weight: 500
toc: true
---


This workshop kit provides resources for individuals who would like to present a talk or workshop about Wolfi and the tools that comprise its ecosystem.

The following materials are included:

- [Presentation Slides](https://docs.google.com/presentation/d/e/2PACX-1vRBWi-C8w1h8UC2Kd6eYd1kyT4Qsdky9Z8X6frLoPJNeKMGZ_v7Ev4Lkfqq1I_pQIWVpHrRXKPBvcuH/pub?start=false&loop=false&delayms=3000);
- A [YouTube Video](https://www.youtube.com/watch?v=2pqhLXA6NaI) with the original talk presented at the [Wolfi 101 Webinar](https://www.crowdcast.io/c/wolfi-101);
- A [GitHub repository](https://github.com/chainguard-dev/hello-wolfi-demo) containing all files necessary to build and execute a demo showcasing Wolfi, melange, and apko;
- This guide, which includes instructions on how to execute the demo.

{{< youtube 2pqhLXA6NaI >}}

## Introduction

Software supply chain threats have been growing exponentially in the last few years, according to [industry leaders and security researchers (PDF)](https://www.usenix.org/system/files/login/articles/login_winter20_17_geer.pdf).
With the popularization of automated workflows and cloud native deployments, it is more important than ever to provide users with the ability to attest the provenance of all relevant software artifacts that compose the container images being used as build and production runtimes.

In this workshop, you'll learn more about Wolfi, a community Linux _undistro_ designed for the container and cloud-native era. You'll also learn about melange and apko, Chainguard's open source toolkit created to build more secure container images.

## Running the Demo

The demo files are available on the [chainguard.dev/hello-wolfi-demo](https://github.com/chainguard-dev/hello-wolfi-demo) repository. The demo application is a command-line script built with PHP. It connects to the [cat facts](https://catfact.ninja/) API and outputs a quote about cats.

### Preparation
Before getting started, make sure you have [Docker](https://docs.docker.com/get-docker/) installed on your machine. These steps were executed on an Ubuntu 22.04 host Linux machine, but they should work seamlessly across platforms that support Docker and [multi-platform builds](https://docs.docker.com/build/building/multi-platform/).

Clone the demo repository with:

```shell
cd ~
git clone https://github.com/chainguard-dev/hello-wolfi-demo.git
cd hello-wolfi-demo
```

### Steps Overview

The demo consists of the following steps:

1. Download the `cgr.dev/chainguard/melange` and `cgr.dev/chainguard/apko` images with `docker pull`
2. Generate melange signing keys
3. Build the `melange-php.yaml` package
4. Build the `composer-php.yaml` package
5. Build the `melange-app.yaml` package
6. Build the `apko.yaml` container image
7. Load the image with `docker load`
8. Run the image with `docker run --rm <image-name>`

### 1. Download melange and apko images
Start by downloading the latest version of the melange and apko images.

```shell
docker pull cgr.dev/chainguard/melange
docker pull cgr.dev/chainguard/apko
```

### 2. Generate melange signing keys
To make sure the generated packages work with apko, you'll need to sign them. The following command will generate a keypair that you can use when building your packages:

```shell
docker run --rm -v "${PWD}":/work cgr.dev/chainguard/melange keygen
```

### 3. Build the PHP package
Next, build the PHP package with melange. On a Linux machine, follow the next command:

```shell
docker run --privileged --rm -v "${PWD}":/work -- \
  cgr.dev/chainguard/melange build melange-php.yaml \
  --arch x86_64 \
  --signing-key melange.rsa --keyring-append melange.rsa.pub
```
On a macOS machine, use the following command.

```shell
docker run --privileged --rm -v "${PWD}":/work -- \
  cgr.dev/chainguard/melange build melange-php.yaml \
  --arch aarch64 \
  --signing-key melange.rsa --keyring-append melange.rsa.pub
```

_If you run into issues while running melange commands, check the [melange troubleshooting guide](/open-source/melange/troubleshooting/)._


### 4. Build the Composer package
You can now build the Composer package with the following command on Linux operating systems:

```shell
docker run --privileged --rm -v "${PWD}":/work -- \
  cgr.dev/chainguard/melange build melange-composer.yaml \
  --arch x86_64 \
  --signing-key melange.rsa --keyring-append melange.rsa.pub
```
On macOS, you can build the Composer package with the following command:

```shell
docker run --privileged --rm -v "${PWD}":/work -- \
  cgr.dev/chainguard/melange build melange-composer.yaml \
  --arch aarch64 \
  --signing-key melange.rsa --keyring-append melange.rsa.pub
```

### 5. Build the app package
With both the PHP and Composer dependencies in place, you can now build the application package.

On Linux systems, use the following command:

```shell
docker run --privileged --rm -v "${PWD}":/work -- \
  cgr.dev/chainguard/melange build melange-app.yaml \
  --arch x86_64 \
  --signing-key melange.rsa --keyring-append melange.rsa.pub
```
On macOS, you can build the application with:

```shell
docker run --privileged --rm -v "${PWD}":/work -- \
 cgr.dev/chainguard/melange build melange-app.yaml \
 --arch aarch64 \
 --signing-key melange.rsa --keyring-append melange.rsa.pub
 ```

### 6. Build the container image
Now that all dependencies are ready, you can now run `apko build` to build the image that runs the demo app.

```shell
docker run --rm -v ${PWD}:/work cgr.dev/chainguard/apko build --debug apko.yaml hello-wolfi:latest hello-wolfi.tar -k melange.rsa.pub
```

_If you run into issues while running apko commands, check the [apko troubleshooting guide](/open-source/apko/troubleshooting/)._

### 7. Load the container image
You can now load the generated image into Docker with the following command:

```shell
docker load < hello-wolfi.tar
```

### 8. Run the image
You can now run the image with:

```shell
docker run --rm hello-wolfi
```
You should see output similar to this, showing a quote about cats:

```
A happy cat holds her tail high and steady.
```
