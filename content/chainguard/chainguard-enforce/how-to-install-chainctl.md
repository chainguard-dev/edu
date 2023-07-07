---
title: "How to Install chainctl"
linktitle: "Install chainctl"
type: "article"
description: "Install the chainctl command line tool to work with Chainguard Enforce and Images"
date: 2022-09-22T15:56:52-07:00
lastmod: 2023-03-22T15:56:52-07:00
draft: false
tags: ["Enforce", "chainctl", "Product"]
images: []
menu:
  docs:
    parent: "chainguard-enforce"
toc: true
weight: 998
---

> _This documentation is related to Chainguard Enforce. You can request access to the product by selecting **Chainguard Enforce** on the [inquiry form](https://www.chainguard.dev/contact?utm_source=docs)._

The Chainguard Enforce command line interface (CLI) tool, `chainctl`, will help you interact with the account model that Chainguard Enforce provides, and enable you to make queries into the state of your clusters and policies registered with the platform.

The tool uses the familiar `<context> <noun> <verb>` style of CLI interactions. For example, to list groups within the context of Chainguard Identity and Access Management (IAM), you can run `chainctl iam groups list` to receive relevant output.

Before we begin, let’s move into a temporary directory that we can work in. Be sure you have curl installed, which you can achieve through visiting the [curl download docs](https://curl.se/download.html) for your relevant operating system.

```sh
mkdir ~/tmp && cd $_
```

There are currently two ways to install `chainctl`, depending on your operating system and preferences.

## Install `chainctl` with Homebrew

You can install `chainctl` for macOS and Linux with the package manager [Homebrew](https://brew.sh/).

Note that you will need to have the Xcode Command Line Tools installed prior to installing `chainctl` with Homebrew on macOS. Without these installed, you won't be able to use Homebrew to install `chainctl` on your macOS device.

If you haven't already done so, you can install the Xcode Command Line Tools with the following command.

```sh
xcode-select --install
```

Before installing `chainctl` with Homebrew, use `brew tap` to bring in Chainguard's repositories.

```sh
brew tap chainguard-dev/tap
```

Next, install `chainctl` with Homebrew.

```sh
brew install chainctl
```

You are now ready to use the `chainctl` command. You can verify that it works correctly in the final section of this guide.

## Install with `curl`

A platform agnostic approach to installing `chainctl` is through using `curl`, which you can achieve with the following command.

```bash
curl -o chainctl "https://dl.enforce.dev/chainctl/latest/chainctl_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m)"
```

Move `chainctl` into your `/usr/local/bin` directory and elevate its permissions so that it can execute as needed.

```sh
sudo install -o $UID -g $GID -m 0755 chainctl /usr/local/bin/chainctl
```

At this point, you'll be able to use the `chainctl` command.

## Verify installation

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

GitVersion:    <semver version>
GitCommit:     <commit hash>
GitTreeState:  clean
BuildDate:     <date here>
GoVersion:     <compiler version>
Compiler:      gc
Platform:      <your platform>
```

If you received output that you did not expect, check your bash profile to make sure that your system is using the expected PATH. 

## Verifying the `chainctl` binary with Cosign

You can verify the integrity of your `chainctl` binary using Cosign. Ensure that you have the latest version of Cosign installed by following our [How to Install Cosign guide](/open-source/sigstore/cosign/how-to-install-cosign/). Verify your `chainctl` binary with the following command:

```sh
cosign verify-blob \
   --signature "https://dl.enforce.dev/chainctl/$(chainctl version 2>&1 |awk '/GitVersion/ {print $2}')/chainctl_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m).sig" \
   --certificate "https://dl.enforce.dev/chainctl/$(chainctl version 2>&1 |awk '/GitVersion/ {print $2}')/chainctl_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m).cert.pem" \
   --certificate-identity "https://github.com/chainguard-dev/mono/.github/workflows/.release-drop.yaml@refs/tags/v$(chainctl version 2>&1 |awk '/GitVersion/ {print $2}')" \
   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
   $(which chainctl)
```

You should receive the following output:

```
Verified OK
```

If you do not see the line `Verified OK` then there is a problem with your `chainctl` binary and you should reinstall it using the instructions at the beginning of this page.

## Updating `chainctl`

When your version of `chainctl` is a few weeks old or older, you may consider updating it to make sure that your version is the most up to date. You can update `chainctl` by running the `update` command.

```sh
sudo chainctl update
```

Keeping `chainctl` up to date will ensure that you are using the most up to date version.
