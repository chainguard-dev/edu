---
title: "How to Sign an SBOM with Cosign"
type: "article"
description: "Signing software bills of materials with Cosign"
lead: "Use Cosign to sign software bills of materials"
date: 2022-13-07T15:22:20+01:00
lastmod: 2024-07-29T15:12:18+00:00
draft: false
tags: ["Cosign", "Procedural", "SBOM"]
images: []
menu:
  docs:
    parent: "cosign"
weight: 005
toc: true
---

_An earlier version of this material was published in the [Cosign chapter](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/block-v1:LinuxFoundationX+LFS182x+2T2022+type@sequential+block@204b98f35bca48c194d1868e0356bef1/block-v1:LinuxFoundationX+LFS182x+2T2022+type@vertical+block@2f0ad9cb8f124a39ab555ac8bf1a114c) of the Linux Foundation [Sigstore course](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/home)._

Cosign is a useful tool for signing software artifacts. Signatures are a form of metadata, and you can add other signed metadata to make different assertions about a software package. 

For example, a [software bill of materials](https://www.cisa.gov/sbom), or **SBOM**, is an inventory of the components that make up a given software artifact. Increasingly, SBOMs are considered part of the foundation that makes a more secure software supply chain. 

As a developer leveraging the software that others make, an SBOM can help you understand what goes into the software that you’re using. As a developer releasing software into the world, including an SBOM with what you ship can help others trust the provenance of the software. You can instill greater trust in your software products by signing your SBOMs along with other software artifacts. 

Let’s demonstrate how to create an SBOM and sign the SBOM using the `hello-container` example from the [How to Sign a Container with Cosign](/open-source/sigstore/cosign/how-to-sign-a-container-with-cosign/) tutorial. Alternatively, you can use another container that you have on hand.

## Install Syft

We can create an SBOM with the open source Syft tool from the Anchore community. First, to install Syft, you can review the guidance on installation on the project’s [README file](https://github.com/anchore/syft#installation). Please note that Syft’s current recommended installation is to use `curl` to download a script that is hosted in their GitHub repository. We recommend that you inspect the script to make sure you know what you’re executing.

You can alternatively use Homebrew for macOS or Linux as a package manager to install Syft:

```sh
brew tap anchore/syft
brew install syft
```

If you will use `curl` to install Syft, we recommend inspecting the [install.sh](https://github.com/anchore/syft/blob/main/install.sh) file prior to downloading. Before piping the command through, it is always a good idea to audit the script. Let’s first download the file.

```sh
curl -O https://raw.githubusercontent.com/anchore/syft/main/install.sh
```

You can now open the file and review it in a text editor such as `nano` or `vi`. Once you are satisfied with your audit of the file, and if you are happy to move forward, you can now run the install script. 

```sh
curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin
```

With Syft installed, you can generate an SBOM with the `syft` command. 

## Generate an SBOM

Using the Syft tool, you can begin to generate an SBOM by using the `syft` command and calling your container image. In our example, the container is your Docker username and the `hello-container` image. 

```sh
syft docker-username/hello-container:latest
```

You should receive output regarding all the components in your container. If you created the same container that we demonstrated in our tutorial, your output should be very similar to the below. 

```
 ✔ Loaded image            
 ✔ Parsed image            
 ✔ Cataloged packages      [14 packages]

NAME                    VERSION      TYPE
alpine-baselayout       3.2.0-r18    apk   
alpine-keys             2.4-r1       apk   
apk-tools               2.12.7-r3    apk   
busybox                 1.34.1-r5    apk   
ca-certificates-bundle  20211220-r0  apk   
libc-utils              0.7.2-r3     apk   
libcrypto1.1            1.1.1n-r0    apk   
libretls                3.3.4-r3     apk   
libssl1.1               1.1.1n-r0    apk   
musl                    1.2.2-r7     apk   
musl-utils              1.2.2-r7     apk   
scanelf                 1.3.3-r0     apk   
ssl_client              1.34.1-r5    apk   
zlib                    1.2.12-r0    apk   
```

We would like this SBOM to be output to a particular file format that we can sign with Cosign. We’ll use the Linux Foundation Project **[SPDX](https://spdx.dev/)** format, which stands for Software Package Data Exchange. SPDX is an open standard for communicating SBOM information. 

We’ll output this to a file called `latest.spdx` to represent the most recent container version’s SBOM. You may want to version SBOMs along with your releases, but keeping a most up-to-date “latest” version can generally be helpful. 

```sh
syft docker-username/hello-container:latest -o spdx > latest.spdx
```

You’ll get output similar to the SBOM output again (without the list of all the components).

```
 ✔ Loaded image            
 ✔ Parsed image            
 ✔ Cataloged packages      [14 packages]
```

With the file written, you can inspect it.

```sh
cat latest.spdx
```

This will be a fairly lengthy file, even for our small container image. It will provide information for each of the components that make up the software in the example `hello-container` image. 

```
SPDXVersion: SPDX-2.2
DataLicense: CC0-1.0
SPDXID: SPDXRef-DOCUMENT
DocumentName: docker-username/hello-container-latest
…
##### Package: zlib

PackageName: zlib
SPDXID: SPDXRef-Package-apk-zlib-7934e949300925b1
PackageVersion: 1.2.12-r0
PackageDownloadLocation: NOASSERTION
FilesAnalyzed: false
PackageLicenseConcluded: Zlib
PackageLicenseDeclared: Zlib
PackageCopyrightText: NOASSERTION
ExternalRef: SECURITY cpe23Type cpe:2.3:a:zlib:zlib:1.2.12-r0:*:*:*:*:*:*:*
ExternalRef: PACKAGE_MANAGER purl pkg:alpine/zlib@1.2.12-r0?arch=aarch64&upstream=zlib&distro=alpine-3.15.4
```

Next, you’ll use Cosign to work with the SBOM and the image.

## Attach the SBOM to the Image

You will now attach the SBOM via Cosign to the container that you have hosted on Docker Hub or other container registry.

```sh
cosign attach sbom --sbom latest.spdx docker-username/hello-container:latest
```

You’ll receive feedback once the SBOM is pushed to the container registry.

```
…
Uploading SBOM file for [index.docker.io/docker-username/hello-container:latest] to [index.docker.io/docker-username/hello-container:sha256-690ecfd885f008330a66d08be13dc6c115a439e1cc935c04d181d7116e198f9c.sbom] with mediaType [text/spdx].
```

Though you have pushed the SBOM with Cosign, you haven’t signed the SBOM. Depending on your organization’s approach to security, an SBOM and a signed container may be adequate. In the next section we will demonstrate how to sign the SBOM to have an additional layer of security.

## Sign the SBOM

You will sign the SBOM in a similar way to signing other software artifacts. 

Make sure you are in the correct local directory for your Cosign key pair. If you generated the key pair in the signed container example, it will be in your home user directory, so make sure you move your present working directory there with the `cd ~` command.

You’ll be signing the SBOM with the SHA that you received in the output from the previous command. This is a long string that starts with `sha256` and ends with `.sbom`. You can verify that this was pushed to the container registry by checking the web user interface of Docker Hub or alternate registry. 

We have an example SBOM SHA below, please use the SHA output you received.

```sh
cosign sign --key cosign.key docker-username/hello-container:sha256-690ecfd885f008330a66d08be13dc6c115a439e1cc935c04d181d7116e198f9c.sbom
```

Again, you’ll be prompted for the password for your Cosign private key. Once you enter the password, you’ll receive output that the signature was pushed to the registry.

```
Pushing signature to: index.docker.io/docker-username/hello-container
```

You can verify the signature on the SBOM as you can with any other signature.

```
cosign verify --key cosign.pub docker-username/hello-container:sha256-690ecfd885f008330a66d08be13dc6c115a439e1cc935c04d181d7116e198f9c.sbom
```

As before, you’ll receive output that the SBOM’s signature is verified and you’ll receive a JSON formatted digest of the information. 

You have now created and signed an SBOM for your container!
