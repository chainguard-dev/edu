---
title: "Overview"
type: "article"
description: "Getting started with Wolfi, the Linux undistro for secure container images"
lead: "Introducing Wolfi, the Linux undistro for secure container images"
date: 2022-09-01T08:49:31+00:00
lastmod: 2022-09-01T08:49:31+00:00
contributors: ["Erika Heidi"]
draft: false
images: []
menu:
  docs:
    parent: "wolfi"
weight: 100
toc: true
---
The popularization of cloud-native solutions and automated workflows based on containers brought in new opportunities and also new challenges to the software industry. In addition to being hyper vigilant about your software dependencies and supply chain, you have to account for the system that builds and releases your software. That's why using safer container images is an important step you can take to improve the security of your build environments.

Wolfi is a Linux _undistro_ and build toolchain designed from the ground up to produce [Chainguard Images](/chainguard/chainguard-images), our distroless-style container images that meet the requirements of a secure software supply chain.

## Why Undistro
We call it an undistro because unlike a typical Linux distribution, Wolfi doesn't have a kernel of its own and contains only the bare minimum to build other container images, which results in a much smaller footprint. The reduced surface of attack results in less CVEs detected by security scanners, as demonstrated in the following graph comparing our curated Nginx image versus the official Alpine-based Nginx image available at Docker Hub:

[INCLUDE GRAPH COMPARING NGINX IMAGES]

These types of base images are also known as _distroless_.

## What is Included

Wolfi is a minimalist base image that doesn't include a package manager, or even manual pages. There are two versions of Wolfi available, each for a different use case:

- wolfi-glibc, for building and running applications with the standard [GNU C library](https://www.gnu.org/software/libc/) (glibc) build kit, as in Debian-based systems.
- wolfi-musl, for building and running applications with the [musl libc](https://musl.libc.org/) build kit, as in Alpine systems.

### Wolfi glibc

[fill in some list of what is included]

### Wolfi musl

[fill in some list of what is included]
