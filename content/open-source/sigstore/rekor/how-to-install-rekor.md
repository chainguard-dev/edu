---
title: "How to Install the Rekor CLI"
type: "article"
description: "An overview of how to instal rekor-cli to query the Sigstore transparency log"
date: 2022-08-20T08:49:31+00:00
lastmod: 2022-08-20T08:49:31+00:00
draft: false
tags: ["Rekor", "Procedural"]
images: []
menu:
  docs:
    parent: "rekor"
weight: 002
toc: true
---

_An earlier version of this material was published in the [Rekor chapter](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/block-v1:LinuxFoundationX+LFS182x+2T2022+type@sequential+block@e785fae1be184e2c929db62dbe7444fa/block-v1:LinuxFoundationX+LFS182x+2T2022+type@vertical+block@a48c33126e2c4ee6ad3bfa6b7bc9c957) of the Linux Foundation [Sigstore course](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/home)._

Follow this tutorial for an overview of how to install `rekor-cli`.

To install the Rekor command line interface (rekor-cli) with Go, you will need Go version 1.16 or greater. For Go installation instructions, see the [official Go documentation](https://go.dev/doc/install). If you have Go installed already, you can check your Go version via this command.

```sh
go version
```

If Go is installed, you'll receive output similar to the following.

```
go version go1.13.8 linux/amd64
```

You will also need to set your `$GOPATH`, the location of your Go workspace.

```sh
export GOPATH=$(go env GOPATH)
```

You can then install `rekor-cli`:

```sh
go install -v github.com/sigstore/rekor/cmd/rekor-cli@latest
```

Check that the installation of `rekor-cli` was successful using the following command:

```sh
rekor-cli version
```

You should receive output similar to that of below:

```
GitVersion:    v0.4.0-59-g2025bf8
GitCommit:     2025bf8aa50b368fc3972bb276dfeae8b604d435
GitTreeState:  clean
BuildDate:     '2022-01-26T00:20:33Z'
GoVersion:     go1.17.6
Compiler:      gc
Platform:      darwin/arm64
```

Now that you have the Rekor CLI tool successfully installed, you can start working with it.
