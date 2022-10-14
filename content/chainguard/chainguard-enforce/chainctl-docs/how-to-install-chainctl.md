---
title: "How to Install chainctl for Chainguard Enforce"
type: "article"
description: "Install the chainctl command line tool to work with Chainguard Enforce"
date: 2022-22-09T15:56:52-07:00
lastmod: 2022-14-10T15:56:52-07:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-enforce-kubernetes"
toc: true
---

> _This documentation is related to Chainguard Enforce. You can request access to the product selecting **Chainguard Enforce for Kubernetes** on the [inquiry form](https://www.chainguard.dev/get-demo?utm_source=docs)._

The Chainguard Enforce command line interface (CLI) tool, `chainctl`, will help you interact with the account model that Chainguard Enforce provides, and enable you to make queries into the state of your clusters and policies registered with the platform. 

The tool uses the familiar `<context> <noun> <verb>` style of CLI interactions. For example, to list groups within the context of Chainguard Identity and Access Management (IAM), you can run `chainctl iam groups list` to receive relevant output.

Before we begin, let’s move into a temporary directory that we can work in. Be sure you have curl installed, which you can achieve through visiting the [curl download docs](https://curl.se/download.html) for your relevant operating system.

```sh
mkdir ~/tmp && cd $_
```

To install `chainctl`, we’ll use the `curl` command to pull the application down.

```sh
curl -o chainctl "https://dl.enforce.dev/chainctl_$(uname -s)_$(uname -m)"
```

Move `chainctl` into your `/usr/local/bin` directory and elevate its permissions so that it can execute as needed.

```sh
sudo install -o $UID -g $GID 0755 chainctl /usr/local/bin/chainctl
```

Finally, alias its path so that you can use `chainctl` on the command line.

```sh
alias chainctl=/usr/local/bin/chainctl
```

You can verify that everything was set up correctly by checking the `chainctl` version.

```sh
chainctl version
```

You should receive output similar to the following.

```
   ____   _   _      _      ___   _   _    ____   _____   _
  / ___| | | | |    / \    |_ _| | \ | |  / ___| |_   _| | |
 | |     | |_| |   / _ \    | |  |  \| | | |       | |   | |
 | |___  |  _  |  / ___ \   | |  | |\  | | |___    | |   | |___
  \____| |_| |_| /_/   \_\ |___| |_| \_|  \____|   |_|   |_____|
chainctl: Chainguard Control

GitVersion:    bf36b2b
GitCommit:     bf36b2be08c0dca8e4d2174ee21c31b9679c4ece
GitTreeState:  clean
BuildDate:     2022-10-13T21:13:11Z
GoVersion:     go1.18.7
Compiler:      gc
Platform:      darwin/arm64
```

If you received different output, check your bash profile to make sure that your system is using the expected PATH. If your version of `chainctl` is a few weeks or months old, you may consider updating it as follows.

```sh
sudo chainctl update
```

Keeping `chainctl` up to date will ensure that you are using the most up to date version.
