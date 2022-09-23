---
title: "How to Install chainctl for Chainguard Enforce"
type: "article"
description: "Install the chainctl command line tool to work with Chainguard Enforce"
date: 2022-09-02T15:56:52-07:00
lastmod: 2022-09-02T15:56:52-07:00
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

To install `chainctl`, create variables that simplify the commands and export them to be used by child processes.

```sh
export BUCKET="us.artifacts.prod-enforce-fabc.appspot.com"
export BASE_URL="https://storage.googleapis.com/${BUCKET}"
```

Here, we are using the bucket our Chainguard Enforce tool is hosted in, and calling that bucket within the base URL of our application hosted by Google.

We’ll use the `curl` command to pull the application down.

```sh
curl -o chainctl "$BASE_URL/chainctl_$(uname -s)_$(uname -m)"
```

Move `chainctl` into your `/usr/local/bin` directory.

```sh
sudo mv ./chainctl /usr/local/bin/chainctl
```

Next, elevate the permissions of `chainctl` so that it can execute as needed.

```sh
chmod +x /usr/local/bin/chainctl
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

GitVersion:    e01c38b
GitCommit:     e01c38b452ee34e44cf5f8663d7730a2cf69f0c3
GitTreeState:  clean
BuildDate:     2022-09-21T00:10:26Z
GoVersion:     go1.18.6
Compiler:      gc
Platform:      darwin/arm64
```

If you received different output, check your bash profile to make sure that your system is using the expected PATH. If your version of `chainctl` is a few weeks or months old, you may consider updating it by following the steps above so that you can use the most up to date version.