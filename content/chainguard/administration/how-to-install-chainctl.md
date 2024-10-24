---
title: "How to Install chainctl"
linktitle: "Install chainctl"
aliases:
- /chainguard/chainguard-enforce/how-to-install-chainctl
type: "article"
description: "Install the chainctl command line tool to work with Chainguard"
date: 2022-09-22T15:56:52-07:00
lastmod: 2024-06-24T15:22:20+01:00
draft: false
tags: ["chainctl", "Product"]
images: []
menu:
  docs:
    parent: "administration"
toc: true
weight: 005
---

The Chainguard command line interface (CLI) tool, `chainctl`, will help you interact with the account model that Chainguard provides, and enable you to make queries into the state of your Chainguard resources.

The tool uses the familiar `<context> <noun> <verb>` style of CLI interactions. For example, to retrieve a list of all the private Chainguard Images available to your organization, you can run `chainctl images list`.

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

A platform-agnostic approach to installing `chainctl` is through using `curl`. We have [specific instructions for Windows users](/chainguard/administration/how-to-install-chainctl/#installing-with-curl-in-windows-powershell) on installing `chainctl` with `curl`, but all others can run the following command:

```bash
curl -o chainctl "https://dl.enforce.dev/chainctl/latest/chainctl_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m | sed 's/aarch64/arm64/')"
```

Move `chainctl` into your `/usr/local/bin` directory and elevate its permissions so that it can execute as needed.

```sh
sudo install -o $UID -g $(id -g) -m 0755 chainctl /usr/local/bin/
```

At this point, you'll be able to use the `chainctl` command.

### Installing with `curl` in Windows Powershell

As stated previously, you can also use `curl` install `chainctl` on Windows systems. Running the following command in PowerShell will download the appropriate `.exe` file.

```PowerShell
curl -o chainctl.exe https://dl.enforce.dev/chainctl/latest/chainctl_windows_x86_64.exe
```

It may take several minutes for this operation to complete.

Following that you can use `chainctl`. Be aware that Windows PowerShell does not load commands from the working directory by default so you will need to include `.\` before any `chainctl` commands you run, as in this example.

```PowerShell
.\chainctl auth login
```

Also, please note that while [`chainctl` commands](/chainguard/chainctl/) will generally work, some are not as thoroughly tested on Windows and may not behave as expected. In particular, the [`chainctl auth configure-docker`](/chainguard/chainctl/chainctl-docs/chainctl_auth_configure-docker/) command is known to cause errors on Windows as of this writing.


## Verify installation

You can verify that everything was set up correctly by checking the `chainctl` version.

```sh
chainctl version
```

You should receive output similar to the following.

```
   ____   _   _  	_  	___   _   _	____   _____   _
  / ___| | | | |	/ \	|_ _| | \ | |  / ___| |_   _| | |
 | | 	| |_| |   / _ \	| |  |  \| | | |   	| |   | |
 | |___  |  _  |  / ___ \   | |  | |\  | | |___	| |   | |___
  \____| |_| |_| /_/   \_\ |___| |_| \_|  \____|   |_|   |_____|
chainctl: Chainguard Control

GitVersion:	<semver version>
GitCommit: 	<commit hash>
GitTreeState:  clean
BuildDate: 	<date here>
GoVersion: 	<compiler version>
Compiler:  	gc
Platform:  	<your platform>
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

## Authenticating

With chainctl installed, you can authenticate into Chainguard with the following command:

```sh
chainctl auth login
```

This will open your browser window and take you through a workflow to login with your OIDC provider.

## Configure a Docker credential helper

You can configure a Docker credential helper with chainctl by running:

```sh
chainctl auth configure-docker
```

This will update your Docker config file to call chainctl when an auth token is needed. A browser window will open when the token needs to be refreshed.

For guidance on pull tokens, please review [authenticating with a pull token](/chainguard/chainguard-registry/authenticating/#authenticating-with-a-pull-token).

## Updating `chainctl`

When your version of `chainctl` is a few weeks old or older, you may consider updating it to make sure that your version is the most up to date. You can update `chainctl` by running the `update` command.

```sh
sudo chainctl update
```

Keeping `chainctl` up to date will ensure that you are using the most up to date version.
