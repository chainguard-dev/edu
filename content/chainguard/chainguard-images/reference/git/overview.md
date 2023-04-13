---
title: "Image Overview: git"
type: "article"
description: "Overview: git Chainguard Images"
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

`stable` [cgr.dev/chainguard/git](https://github.com/chainguard-images/images/tree/main/images/git)
| Tags                | Aliases                                                                        |
|---------------------|--------------------------------------------------------------------------------|
| `latest`            | `2`, `2.40`, `2.40.0`, `2.40.0-r1`                                             |
| `latest-dev`        | `2-dev`, `2.40-dev`, `2.40.0-dev`, `2.40.0-r1-dev`                             |
| `latest-glibc`      | `glibc-2`, `glibc-2.40`, `glibc-2.40.0`, `glibc-2.40.0-r0`                     |
| `latest-glibc-dev`  | `glibc-2-dev`, `glibc-2.40-dev`, `glibc-2.40.0-dev`, `glibc-2.40.0-r0-dev`     |
| `latest-root`       | `root-2`, `root-2.40`, `root-2.40.0`, `root-2.40.0-r1`                         |
| `latest-glibc-root` | `glibc-root-2`, `glibc-root-2.40`, `glibc-root-2.40.0`, `glibc-root-2.40.0-r0` |



This is a minimal Git image based. The image contains `git`, `git-lfs`, and supporting libraries such as `openssh` (for `ssh`-based auth), and `ca-certs` (for `https`-based cloning). Both Wolfi (glibc) and Alpine (musl) versions are available.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/git:latest
```

Or for the glibc version:

```
docker pull cgr.dev/chainguard/git:latest-glibc
```

## Usage

The Git image allows you to run ordinary Git commands in CI/CD pipelines and also locally via Docker.

### Docker Setup

To make sure you have the latest image version available, start by running a `docker pull` command:

```shell
docker pull cgr.dev/chainguard/git
```

Then, run the image with the `--version` flag to make sure it is functional:

```shell
docker run -it --rm cgr.dev/chainguard/git --version
```
You should get output similar to this:

```
git version 2.37.1
```

### Cloning a Repository Locally

Because your local system user's ID (uid) might differ from that of the container image, if you want to clone repositories locally using this image you'll need to set up special permissions for the target dir. Then, you'll be able to set up a volume and have the contents of the cloned repo replicated on your host machine.

First, create a target directory somewhere in your home folder and set the required permissions:

```shell
mkdir ~/workspace
chmod go+wrx ~/workspace
```

Now you can use `docker run` to execute the clone command, using the directory you just set up as a volume share between your local machine and the container image on `/home/git`.

```shell
docker run -it -v ~/workspace:/home/git --rm cgr.dev/chainguard/git clone https://github.com/chainguard-images/git.git
```

You should get output like this:

```
Cloning into 'git'...
remote: Enumerating objects: 57, done.
remote: Counting objects: 100% (57/57), done.
remote: Compressing objects: 100% (47/47), done.
remote: Total 57 (delta 19), reused 35 (delta 10), pack-reused 0
Receiving objects: 100% (57/57), 15.23 KiB | 866.00 KiB/s, done.
Resolving deltas: 100% (19/19), done.
```

You can now check the contents of your `workspace` directory, where you should find the cloned repo.

