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
|               | July 18th    | `sha256:7521793b51979c8b4bc706c330d28b91c9b11462dd28549f4fafcbb8ec2b8891` |
|               | July 18th    | `sha256:ed6e5cf04ea370598ac36792a4278cb963c40f4bc855b10b3b97355d2dadb0b8` |
|  `latest`     | July 18th    | `sha256:523a38daa32e21ed22c131e0268a9a88c7776853d05a2bc037fe04bc562fb398` |
|  `latest-dev` | July 18th    | `sha256:7f3470a1bb02c0319236e4708dfb22879f5c10fd0c6ded54c42a1043eb00af14` |
|               | July 18th    | `sha256:e2d4cf377c7d08a1d7d9555b7202a1a5db6dd00a7664288688f8dba06167880f` |
|               | July 18th    | `sha256:ebf230730e7d13c92e25289f4e0977ba6613f10fe4432c0e5ea9db9f608b63b8` |
|               | July 18th    | `sha256:52e10d35ce9df94452fbda262340bd04351811df10677352a38d0efcdd757edf` |
|               | July 18th    | `sha256:f510cecc9babe2c38b33dc9ba0828f94a5550a87d3c084a06fbe33cc012cfc38` |
|               | July 14th    | `sha256:f84e212076ec63cf9171f7569d2e97f705ef12c9218f726f38637bae4f3855a1` |
|               | July 14th    | `sha256:c7bd030a434fd60da3368e4f1c4e92377f3b4d4af937d3771c640f293f93ad50` |
|               | July 3rd     | `sha256:74f408188469af5d87a4052ead3eedc5b2b501dcd30262dbdf75db4ee868691e` |
|               | July 3rd     | `sha256:404ae3e315d07abaf90e726114e2305c6dfc5e227e7bb3cc86715bb1804a69c9` |
|               | June 28th    | `sha256:861308137ee974fc4f52202f1d15f2c3e80f44227a6eb09418900c9ee20fbce1` |
|               | June 28th    | `sha256:fc4cbc32a421fd45c5121e40a23aae7f55f60653f56a32d41c71bb20651ae91f` |



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

