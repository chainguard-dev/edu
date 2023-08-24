---
title: "Image Overview: git"
type: "article"
description: "Overview: git Chainguard Image"
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

[cgr.dev/chainguard/git](https://github.com/chainguard-images/images/tree/main/images/git)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | August 23rd  | `sha256:2529db9b1f7a2f0817a3715a53a0bce125f4ac241a67e5745072cd1912523f7b` |
|  `latest-dev` | August 23rd  | `sha256:061d9311949cf2398faf870541e2a5e6c11c89a88c273a90bc7844f7c19dd6b7` |



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
docker run -it -v ~/workspace:/home/git --rm cgr.dev/chainguard/git clone https://github.com/chainguard-images/.github.git
```

You should get output like this:

```
Cloning into '.github'...
remote: Enumerating objects: 217, done.
remote: Counting objects: 100% (104/104), done.
remote: Compressing objects: 100% (74/74), done.
remote: Total 217 (delta 39), reused 78 (delta 27), pack-reused 113
Receiving objects: 100% (217/217), 207.47 KiB | 1.46 MiB/s, done.
Resolving deltas: 100% (70/70), done.
```

You can now check the contents of your `workspace` directory, where you should find the cloned repo.

