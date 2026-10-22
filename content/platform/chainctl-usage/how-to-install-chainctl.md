---
title: "How to install chainctl"
linktitle: "Install chainctl"
aliases:
- /chainguard/chainctl-usage/how-to-install-chainctl/
- /chainguard/chainguard-enforce/how-to-install-chainctl
- /chainguard/administration/how-to-install-chainctl
type: "article"
description: "Learn how to install chainctl, Chainguard's command-line interface for managing container images, IAM resources, and security configurations across platforms"
date: 2022-09-22T15:56:52-07:00
lastmod: 2026-10-22T13:47:36+00:00
draft: false
tags: ["chainctl"]
images: []
menu:
  docs:
    parent: "administration"
toc: true
weight: 10
---

Chainguard's `chainctl` command-line interface provides essential tools for managing your container security infrastructure, including image management, identity and access control, and resource monitoring. This CLI enables automation of Chainguard operations and integration with CI/CD pipelines.

The tool uses the familiar `<context> <noun> <verb>` style of CLI interactions. For example, to retrieve a list of all the private Chainguard Containers available to your organization, you can run `chainctl images list`.

## Install `chainctl`

To install `chainctl` with [Homebrew](https://brew.sh/) on macOS or Linux, run the following command:

```sh
brew install chainguard-dev/tap/chainctl
```

To install `chainctl` with [curl](https://curl.se/download.html) on macOS or Linux, download the latest release for your platform and move it into `/usr/local/bin`:

```sh
curl -fL -o chainctl "https://dl.enforce.dev/chainctl/latest/chainctl_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m | sed 's/aarch64/arm64/')"
sudo install -o $UID -g $(id -g) -m 0755 chainctl /usr/local/bin/
```

On Windows, install with [`curl` in PowerShell](#installing-with-curl-in-windows-powershell) or with [Scoop](#install-with-scoop-in-windows).

To check the binary's signature before you run it, [install a pinned version with `curl`](#install-a-pinned-version-with-curl) and then [verify it with Cosign](#verifying-the-chainctl-binary-with-cosign). When you're done, [confirm the installation](#verifying-installation).

### Install `chainctl` with Homebrew

The `brew install chainguard-dev/tap/chainctl` command adds Chainguard's tap, trusts the `chainctl` formula in it, and installs `chainctl`. You don't need to run `brew tap` or `brew trust` first.

On macOS, Homebrew needs the Xcode Command Line Tools to install `chainctl`. The Homebrew installer sets them up, so most Macs already have them. If `brew` reports `No developer tools installed`, install the tools and then run the `brew install` command again:

```sh
xcode-select --install
```

### Troubleshoot a Homebrew installation

If `brew` reports that `trust` is an unknown command, your Homebrew is earlier than version 5.1.15, which added `brew trust`. Older instructions for `chainctl` ran `brew tap` and `brew trust --tap` as separate steps. Skip them and run `brew install chainguard-dev/tap/chainctl`, which needs no separate trust step on any version. To update Homebrew itself, run `brew update`.

If `brew` fails to clone the tap with `Permission denied (publickey)`, your Git configuration probably rewrites GitHub HTTPS URLs to SSH. The tap repository is public and needs no credentials over HTTPS, but the rewrite sends the clone over SSH, which fails unless GitHub accepts one of your SSH keys. To check for a rewrite, run the following command:

```sh
git config --get-regexp '^url\..*\.insteadof$'
```

Output such as `url.git@github.com:.insteadof https://github.com/` shows a rewrite. To fix the clone, add an SSH key to your GitHub account or remove the rewrite. Otherwise, [install with `curl`](#install-chainctl) instead.

### Install with `curl`

The `curl` command in [Install `chainctl`](#install-chainctl) builds the download URL from `uname`, so it fetches the binary for your operating system and architecture. The `sudo install` command copies the binary into `/usr/local/bin`, sets you as its owner, and makes it executable.

### Install a pinned version with `curl`

To verify the binary with Cosign, download it from an explicit version path instead of `/latest/`. Pinning the version keeps the binary and its signature bundle in the same release. This method needs [jq](https://jqlang.org/download/) to read the release version.

Move into a temporary working directory:

```sh
mkdir -p ~/tmp && cd $_
```

Resolve the platform and the latest release version, and then download and install that version:

```sh
PLATFORM="$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m | sed 's/aarch64/arm64/')"
VERSION=$(curl -sS "https://dl.enforce.dev/chainctl/latest/metadata.json" | jq -r .version)
curl -fL -o chainctl "https://dl.enforce.dev/chainctl/${VERSION}/chainctl_${PLATFORM}"
sudo install -o $UID -g $(id -g) -m 0755 chainctl /usr/local/bin/
```

Keep this terminal session open for [the Cosign verification](#verifying-the-chainctl-binary-with-cosign), so that it reuses the `PLATFORM` and `VERSION` values.

### Installing with `curl` in Windows PowerShell

As stated previously, you can also use `curl` install `chainctl` on Windows systems. Running the following command in PowerShell will download the appropriate `.exe` file.

```PowerShell
$VERSION = (curl -UseBasicParsing https://dl.enforce.dev/chainctl/latest/metadata.json | ConvertFrom-Json).version
curl -o chainctl.exe https://dl.enforce.dev/chainctl/$VERSION/chainctl_windows_x86_64.exe
```

It may take several minutes for this operation to complete.

Following that you can use `chainctl`. Be aware that Windows PowerShell does not load commands from the working directory by default so you will need to include `.\` before any `chainctl` commands you run, as in this example.

```PowerShell
.\chainctl auth login
```

Also, please note that while [`chainctl` commands](/platform/chainctl/) will generally work, some are not as thoroughly tested on Windows and may not behave as expected.

### Install with Scoop in Windows

Scoop is a command-line installer for Windows that has a community-contributed and -maintained way of [installing `chainctl`](https://scoop.sh/#/apps?q=chainctl).

If you have Scoop installed, then installing `chainctl` only requires two commands.

First, add the bucket.

```shell
scoop bucket add main
```

And then install `chainctl` from there.

```shell
scoop install main/chainctl
```

## Verifying the `chainctl` binary with Cosign

Before running `chainctl` for the first time, you should verify the integrity of the downloaded binary using Cosign. This ensures the binary has not been tampered with. Ensure that you have the latest version of Cosign installed by following our [How to install Cosign guide](/open-source/sigstore/cosign/how-to-install-cosign/). This step also needs [jq](https://jqlang.org/download/).

The following commands download the release's Sigstore bundle, which holds the binary's signature and certificate, and use it to verify the binary. The first two lines set `PLATFORM` and `VERSION`. If you're in the same terminal session as the [pinned installation](#install-a-pinned-version-with-curl), skip them so that the bundle comes from the version you installed:

```sh
PLATFORM="$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m | sed 's/aarch64/arm64/')"
VERSION=$(curl -sS "https://dl.enforce.dev/chainctl/latest/metadata.json" | jq -r .version)
curl -sS -o chainctl.sigstore.json "https://dl.enforce.dev/chainctl/${VERSION}/chainctl_${PLATFORM}.sigstore.json"
cosign verify-blob \
   --bundle chainctl.sigstore.json \
   --certificate-identity "https://github.com/chainguard-dev/mono/.github/workflows/.release-drop.yaml@refs/tags/v${VERSION}" \
   --certificate-oidc-issuer https://token.actions.githubusercontent.com \
   $(which chainctl)
```

{{< note >}}
Always pin the binary and bundle downloads to the same explicit `${VERSION}` rather than fetching each from `/latest/` independently. If a new release is published between the individual downloads, you can end up with a binary and a bundle from different releases, and verification will fail with an error such as `invalid signature when validating ASN.1 encoded signature`.
{{< /note >}}

You should receive the following output:

```output
Verified OK
```

If you do not see the line `Verified OK` then there is a problem with your `chainctl` binary and you should reinstall it using the instructions at the beginning of this page.

## Verifying installation

Once verified, you can confirm that everything was set up correctly by checking the `chainctl` version.

```sh
chainctl version
```

You should receive output similar to the following.

```output
   ____   _   _      _      ___   _   _    ____   _____   _
  / ___| | | | |    / \    |_ _| | \ | |  / ___| |_   _| | |
 | |     | |_| |   / _ \    | |  |  \| | | |       | |   | |
 | |___  |  _  |  / ___ \   | |  | |\  | | |___    | |   | |___
  \____| |_| |_| /_/   \_\ |___| |_| \_|  \____|   |_|   |_____|
chainctl: Chainguard Control

GitVersion: <semver version>
GitCommit:  <commit hash>
GitTreeState:  clean
BuildDate:  <date here>
GoVersion:  <compiler version>
Compiler:   gc
Platform:   <your platform>
```

If you received output that you did not expect, check your bash profile to make sure that your system is using the expected PATH.

## Authenticating

With chainctl installed, you can authenticate into Chainguard with the following command:

```sh
chainctl auth login
```

This will open your browser window and take you through a workflow to login with your OIDC provider.

{{< blurb/chainctl-auth >}}

### Authentication tokens

If you ever need to retrieve your local Chainguard token, you can do so with the following command:

```shell
chainctl auth token
```

Following the [XDG standard](https://specifications.freedesktop.org/basedir/latest/), chainctl stores tokens in the local OS's cache directory:

* **On Linux systems**, this is typically `~/.cache/`
* **On MacOS**, this is `~/Library/Caches/`
* **On Windows**, this is `%LocalAppData%` (typically `C:\Users\<username>\AppData\Local`)

The token's path is the local cache directory appended with `/chainguard/<audience>/<oidc-token|refresh-token>`. The `oidc-token` is a short-lived access token used for authentication, while the `refresh-token` is a longer-lived credential that allows chainctl to obtain new access tokens without requiring you to log in again.

For example, on Linux you can find the `oidc-token` for the `https://console-api.enforce.dev` audience in the following location:

```
/home/$USER/.cache/chainguard/https:--console-api.enforce.dev/
```

Note that for this audience, chainctl replaces `/` with `-` in order to ensure a valid file path.

On Windows, the same `oidc-token` is stored at:

```
C:\Users\<username>\AppData\Local\chainguard\https---console-api.enforce.dev\oidc-token
```

Windows doesn't allow `:` in file paths either, so on Windows chainctl replaces both `/` and `:` with `-`. The `https://console-api.enforce.dev` audience becomes `https---console-api.enforce.dev` (three hyphens), rather than the `https:--console-api.enforce.dev` form used on Linux and macOS.

## Configure a Docker credential helper

You can configure a Docker credential helper with chainctl by running:

```sh
chainctl auth configure-docker
```

This will:

* Create a link for `docker-credential-cgr` in the same directory as `chainctl`.
* Update your Docker config file to call `docker-credential-cgr` when an auth token is needed. A browser window will open when the token needs to be refreshed.

{{< note >}}
If you installed `chainctl` to a directory that needs root permissions and run as root (eg with `sudo`) when creating the `docker-credential-cgr` symlink, and then complete login in that same session, the Docker credentials will be written to `root`'s `.docker/config.json` instead of your user's Docker config. In that case, run `configure-docker` again as the correct user.
{{< /note >}}

### Docker credential helper on Windows

On Windows, Docker expects a `docker-credential-cgr.exe` helper to be available on your `PATH`. `chainctl auth configure-docker` creates this helper for you by copying `chainctl.exe` to `docker-credential-cgr.exe` in the same directory. Because it copies the binary rather than creating a symbolic link, a standard, non-administrator account can run it without enabling Developer Mode or running PowerShell as an administrator. To make Docker pulls work, perform the following steps:

#### 1. Add `chainctl.exe` to the `PATH` (replace `C:\Tools` with the actual directory you used):

```PowerShell
$env:Path += ";C:\Tools"
```

For a persistent setup, add that directory to your user or system `PATH` via the Windows Environment Variables settings.

#### 2. Authenticate and configure Docker credentials:

```PowerShell
chainctl auth configure-docker
```

`chainctl auth configure-docker` creates `docker-credential-cgr.exe` next to `chainctl.exe` and updates your Docker configuration to use it. You don't need to run `chainctl auth login` first; `configure-docker` authenticates you when no valid token is available. Following this, you can verify Docker pulls from Chainguard by pulling a private image.

## Updating `chainctl`

When your version of `chainctl` is a few weeks old or older, you may consider updating it to make sure that your version is the most up to date. You can update `chainctl` by running the `update` command.

```sh
sudo chainctl update
```

The command shows your current version and the latest version, then asks `Do you want to continue? [Y,n]`. Enter `Y` to update. To skip the prompt, run `sudo chainctl update --yes` instead.

The update command verifies the signature of the downloaded binary in-process before replacing your existing installation, so you don't need a separate `cosign` binary on your `PATH`. Verification needs network access to the download host (`dl.enforce.dev`) and, at least on first use, to the Sigstore trust root at `tuf-repo-cdn.sigstore.dev`. If verification fails or those hosts are unreachable, the update stops, the unverified binary is removed, and your current installation is left in place.

When the update finishes, `chainctl` keeps a backup of your previous binary and prints a command to delete it, such as `rm -f "/root/.cache/chainctl/chainctl.bak"`. Once the new version works, you can run that command to remove the backup.

Keeping `chainctl` up to date will ensure that you are using the most up to date version.
