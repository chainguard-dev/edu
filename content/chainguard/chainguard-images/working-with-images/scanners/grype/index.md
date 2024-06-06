---
title: "Using the grype Container Scanner"
type: "article"
linktitle: "grype"
aliases: 
- /chainguard/chainguard-images/working-with-images/scanners/grype
description: "Learn to use grype to detect CVEs in images"
date: 2024-06-06:08:00+02:00
lastmod: 2024-06-06:08:00+00:00
tags: ["Conceptual", "CVE"]
draft: false
images: []
menu:
  docs:
    parent: "scanners"
weight: 100
toc: true
---

[grype](https://github.com/anchore/grype) is a vulnerability scanner for container images and filesystems developed and maintained by [Anchore](https://anchore.com/) and written in the Go programming language. grype can scan from Docker, OCI, Singularity, podman, image archives, and local directory. grype supports a variety of SBOM formats for faster scanning, and grype's [vulnerability database](https://github.com/anchore/grype-db) draws from a wide variety of sources, including [Wolfi SecDB]( https://pkg.go.dev/github.com/wolfi-dev/wolfictl/pkg/advisory/secdb),

grype is appropriate for one-off detection for manual CVE mitigation and in automated use in CI pipelines. Chainguard maintains a [low-to-no CVE Chainguard Image for grype](https://edu.chainguard.dev/chainguard/chainguard-images/reference/grype/) based on our lightweight Wolfi distribution.

## Installation

### Container Images

grype is readily available as a container image. To pull the low-to-no-CVE Chainguard Image for grype and perform a scan on the official Docker nginx image, run the following:

```bash
docker run -it cgr.dev/chainguard/grype nginx
```

Alternatively, you can scan using the official grype Docker image:

```
docker run -it anchore/grype:latest nginx
```

### Binary Installation

To install grype as a binary, find and download the appropriate package file or binary from the [official releases page](https://github.com/anchore/grype/releases). Place the binary on your system path or install the package using the conventions for your OS and distribution.

grype can also be [built from source](https://github.com/anchore/grype/blob/main/DEVELOPING.md#native-development).

### Install via Package Manager

grype can be installed using the following commands specific to your OS and distribution: 

#### Homebrew

```
brew tap anchore/grype
brew install grype
```

#### Chocolatey

```
choco install grype -y
```

## Basic Usage

Throughout this tutorial, we'll use the `grype` command to run grype. If you're running grype as an image, replace this command with the appropriate `docker run` command, such as `docker run -it cgr.dev/chainguard/grype`.

To run grype on an image in a Docker or OCI registry, pass the image name as an argument:

```bash
grype nginx
```

```bash
grype cgr.dev/chainguard/nginx
```

To scan an image stored to `.tar`, pas the path to the archive file as an argument:

```bash
docker pull cgr.dev/chainguard/nginx
docker save cgr.dev/chainguard/nginx > nginx_chainguard_image.tar.gz
grype nginx_chainguard_image.tar.gz
```

grype can scan local directories, such as Python virtual environment (venv) or `node_modules` folders.


```bash
python -m venv venv
./venv/bin/pip install WTForms==2.3.3 Werkzeug==2.0.1
grype venv
```

```bash
mkdir node_project && cd node_project
npm init -y
npm install qs@6.5.2
grype .
```

### Comprehending Grype Output




### Scanning from SBOMs



## grype API
