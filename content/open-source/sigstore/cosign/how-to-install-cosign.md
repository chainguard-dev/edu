---
title: "How to Install Cosign"
type: "article"
lead: "Details for installing Cosign across operating systems to sign software artifacts"
description: "Details for installing Cosign across operating systems"
date: 2022-07-13T08:49:31+00:00
lastmod: 2024-12-16T15:16:50+01:00
draft: false
tags: ["Cosign", "Procedural"]
images: []
menu:
  docs:
    parent: "cosign"
weight: 002
toc: true
---

_An earlier version of this material was published in the [Cosign chapter](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/block-v1:LinuxFoundationX+LFS182x+2T2022+type@sequential+block@204b98f35bca48c194d1868e0356bef1/block-v1:LinuxFoundationX+LFS182x+2T2022+type@vertical+block@2f0ad9cb8f124a39ab555ac8bf1a114c) of the Linux Foundation [Sigstore course](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/home)._

Cosign supports software artifact signing, verification, and storage in an OCI (Open Container Initiative) registry. By signing software, you can authenticate that you are who you say you are, which can in turn enable a trust root so that developers and consumers who leverage your software can verify that you created the software artifact that you have said you’ve created. They can also ensure that that artifact was not tampered with by a third party. As someone who may use software libraries, containers, or other artifacts as part of your development lifecycle, a signed artifact can give you greater assurance that the code or container you are incorporating is from a trusted source.

There are a few different ways to install Cosign to your local machine or remote server. The approach you choose should be based on the way you set up packages, the tooling that you use, or the way that your organization recommends. We will go through several options. Please refer to the [official Cosign installation documentation](https://docs.sigstore.dev/cosign/system_config/installation/) for additional context and updates.

## Installing Cosign with Homebrew or Linuxbrew

Those who are running macOS locally may be familiar with Homebrew as a package manager. There is also a [Linuxbrew](https://docs.brew.sh/Homebrew-on-Linux) version for those running a Linux distribution. If you are using macOS and would like to leverage a package manager, you can review the [official documentation to install Homebrew](https://brew.sh/) to your machine.

To install Cosign with Homebrew, run the following command.

```sh
brew install cosign
```

To update Cosign in the future, you can run `brew upgrade cosign` to get the newest version.

## Installing Cosign with Linux Package Managers

Cosign is supported by the Arch Linux, Alpine Linux, and Nix package managers. On the [releases page](https://github.com/sigstore/cosign/releases), you’ll also find `.deb` and `.rpm` packages for manual download and installation.

To install Cosign on Arch Linux, use the `pacman` package manager.

```sh
pacman -S cosign
```

If you are using Alpine Linux or an Alpine Linux image, you can add Cosign with `apk`.

```sh
apk add cosign
```

For NixOS, you can install Cosign with the following command:

```sh
nix-env -iA nixpkgs.cosign
```

And for NixOS Linux, you can install Cosign using `nixos.cosign` with the `nix-env` package manager.

```sh
nix-env -iA nixos.cosign
```

For Ubuntu and Debian distributions, check the releases page and download the latest `.deb` package. At the time of this writing, this would be version 1.8.0. To install the `.deb` file, run:

```sh
sudo dpkg -i ~/Downloads/cosign_1.8.0_amd64.deb
```

For CentOS and Fedora, download the latest `.rpm` package from the releases page and install Cosign with:

```sh
rpm -ivh cosign-1.8.0.x86_64.rpm
```

You can check to ensure that Cosign is successfully installed using the `cosign version` command following installation. When you run the command, you should receive output that indicates the version you have installed.

## Installing Cosign with Go

You can install Cosign using the Go package manager. Installing with Go will work across different operating systems and distributions. First, check that you have Go installed on your machine, and ensure that it is Go version `1.22.7` or later.

```sh
go version
```

```
go version go1.23.4 linux/amd64
```

If you run into an error or don’t receive output like the above, you’ll need to install Go in order to install Cosign with Go. Navigate to the official Go website in order to download the appropriate version of Go for your machine.

With Go installed, you are ready to install Cosign using the following command.

```sh
go install github.com/sigstore/cosign/v2/cmd/cosign@latest
```

The resulting binary from this installation will be placed at `$GOPATH/bin/cosign`.

### Installing a Cosign release with Go

You can install Cosign with Go directly from the [Cosign GitHub releases page](https://github.com/sigstore/cosign/releases).

At the time of writing, the newest release is [v2.0.0](https://github.com/sigstore/cosign/releases/tag/v2.0.0). You can download this version with the following command.

```sh
go install github.com/sigstore/cosign/v2/cmd/cosign@v2.0.0
```

The resulting binary from this installation will be placed at `$GOPATH/bin/cosign`. Check the [release page]([Cosign GitHub releases page](https://github.com/sigstore/cosign/releases) for additional releases.

## Installing Cosign with the Cosign Binary

Installing Cosign via its binary offers you greater control over your installation, but this method also requires you to manage your installation yourself. In order to install via binary, check for the most updated version in the open source GitHub repository for Cosign under the [releases page](https://github.com/sigstore/cosign/releases).

You can use the `wget` command to install the most recent binary. In our example, the release we are installing is 2.0.0.

```sh
wget "https://github.com/sigstore/cosign/releases/download/v2.0.0/cosign-linux-amd64"
```

Next, move the Cosign binary to your bin folder.

```sh
sudo mv cosign-linux-amd64 /usr/local/bin/cosign
```

Finally, update permissions so that Cosign can execute within your filesystem.

```sh
sudo chmod +x /usr/local/bin/cosign
```

You’ll need to ensure that you keep Cosign up to date if you install via binary. You can always later opt to use a package manager to update Cosign in the future.

