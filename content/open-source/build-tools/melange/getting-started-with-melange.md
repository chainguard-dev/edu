---
title: "Getting Started with melange"
aliases:
- /open-source/melange/getting-started-with-melange
- /open-source/melange/tutorials/getting-started-with-melange
lead: "An apk builder tool"
type: "article"
description: "melange is a declarative apk builder"
date: 2022-07-21T15:21:01+02:00
lastmod: 2024-08-01T15:21:01+02:00
draft: false
tags: ["melange", "Procedural"]
images: []
menu:
  docs:
    parent: "melange-tutorials"
weight: 100
toc: true
---

[melange](https://github.com/chainguard-dev/melange) is an [apk](https://wiki.alpinelinux.org/wiki/Package_management) builder tool that uses declarative pipelines to create apk packages. From a single YAML file, users are able to generate multi-architecture apks that can be injected directly into [apko](https://github.com/chainguard-dev/apko) builds.

Understanding melange can help you better understand the [Wolfi](/open-source/wolfi) operating system and how [Chainguard Containers](/chainguard/chainguard-images) are made to be minimal and secure, but it is not necessary to have a background in melange in order to use Chainguard Containers.

In this guide, you'll learn how to build a software package with melange. To demonstrate the versatile combination of melange and apko builds, we'll package a small command-line PHP script and build a minimalist container image based on Wolfi with the generated apk. All files used in this demo are open source and available at the [melange-php-demos](https://github.com/chainguard-dev/melange-php-demos/tree/main/hello-minicli) repository.

## Requirements

Our guide is compatible with operating systems that support Docker and shared volumes. Please follow the [appropriate Docker installation instructions](https://docs.docker.com/get-docker/) for your operating system.

You won't need PHP or Composer installed on your system, since we'll be using Docker to build the demo app.

### Note for Linux Users

In order to be able to build apks for multiple architectures using Docker, you may need to register additional QEMU headers within your kernel. This is done automatically for Docker Desktop users, so if you are on macOS you don't need to run this additional step.

Run the following command to register the necessary handlers within your kernel, using the [multiarch/qemu-user-static](https://github.com/multiarch/qemu-user-static) image.

```shell
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
```

You should now be able to build apks for all architectures supported by melange.

## 1 — Downloading the melange Image

The fastest way to get melange up and running on your system is by using the [official melange image](https://images.chainguard.dev/directory/image/melange/versions?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-open-source-build-tools-melange-getting-started-with-melange) with Docker. Start by pulling the melange image into your local system:

```shell
docker pull cgr.dev/chainguard/melange:latest
```

This will download the latest version of the melange image, which is rebuilt every night for extra freshness.

Check that you're able to run melange with `docker run`.

```shell
docker run --rm cgr.dev/chainguard/melange version
```

You should get output similar to the following:

```
  __  __   _____   _          _      _   _    ____   _____
 |  \/  | | ____| | |        / \    | \ | |  / ___| | ____|
 | |\/| | |  _|   | |       / _ \   |  \| | | |  _  |  _|
 | |  | | | |___  | |___   / ___ \  | |\  | | |_| | | |___
 |_|  |_| |_____| |_____| /_/   \_\ |_| \_|  \____| |_____|
melange

GitVersion:    v0.11.1
GitCommit:     a52edcc075ebf1dc89aea87893e3821944171ee3
GitTreeState:  clean
BuildDate:     '2024-07-19T16:04:17Z'
GoVersion:     go1.22.5
Compiler:      gc
Platform:      linux/amd64

```

With melange installed, you’re ready to proceed.

## 2 — Cloning the Demo Repository

To demonstrate melange's features with a minimalist application that has real-world functionality, our demo consists of a PHP command line app that queries the [Slip advice](https://api.adviceslip.com/) API and outputs a random piece of advice. The app is a single-file script built with [Minicli](https://github.com/minicli).

Start by cloning the demo repository to your local machine and navigating to the `melange-php-demos/hello-minicli` directory:

```shell
git clone git@github.com:chainguard-dev/melange-php-demos.git
cd melange-php-demos/hello-minicli
```

Run the following command, which will use the official Composer image to generate a composer.json file and download minicli/minicli:

```shell
docker run --rm -it -v "${PWD}":/app composer require minicli/minicli
```

Once you receive confirmation that the download was completed, you'll need a second dependency to query the Advice Slip API. Run the following command to include `minicli/curly`, a `curl` wrapper for Minicli:
```shell
docker run --rm -it -v "${PWD}":/app composer require minicli/curly
```

Now you can run the application to make sure it's functional. You can do that using Docker and Chainguard's PHP image:

```shell
docker run --rm -it -v "${PWD}":/app cgr.dev/chainguard/php /app/minicli advice
```

You should get a random piece of advice such as:

```
Gratitude is said to be the secret to happiness.
```

With the application ready, you can start building your package.

## 3 — The melange YAML File
The `melange.yaml` file is where you declare the details and specifications of your apk package. For code that generates self-contained binaries, this is typically where you'll build your application artifacts with compiler tools. In the case of interpreted languages, you'll likely build your application by downloading vendor dependencies, setting up relevant paths, and setting the environment up for production.

The melange specification file contains three main sections:

- **package**: defines package specs, such as name, license, and runtime dependencies. Runtime dependencies will be brought into the system automatically as dependencies when the apk is installed.
- **environment**: defines how the environment should be prepared for the build, including required packages and their source repositories. Anything that is only required at build time goes here, and shouldn't be part of the runtime dependencies.
- **pipeline**: defines the build pipeline for this package.

One of the best advantages of using melange is to be able to control all steps of your build pipeline, and include only what's necessary. This way, you'll be able to build smaller and more secure container images by removing unnecessary dependencies.

This is what the `melange.yaml` included in our demo looks like, for your reference:

```yaml
package:
  name: hello-minicli
  version: 0.1.0
  description: Minicli melange demo
  target-architecture:
    - all
  copyright:
    - license: MIT
  dependencies:
    runtime:
      - php
      - php-curl

environment:
  contents:
    keyring:
      - https://packages.wolfi.dev/os/wolfi-signing.rsa.pub
      - ./melange.rsa.pub
    repositories:
      - https://packages.wolfi.dev/os
    packages:
      - ca-certificates-bundle
      - busybox
      - curl
      - git
      - php
      - php-phar
      - php-iconv
      - php-openssl
      - php-curl
      - composer

pipeline:
  - name: Build Minicli application
    runs: |
      MINICLI_HOME="${{targets.destdir}}/usr/share/minicli"
      EXEC_DIR="${{targets.destdir}}/usr/bin"
      mkdir -p "${MINICLI_HOME}" "${EXEC_DIR}"
      cp ./composer.json "${MINICLI_HOME}"
      /usr/bin/composer install -d "${MINICLI_HOME}" --no-dev
      cp ./minicli "${EXEC_DIR}"
      chmod +x "${EXEC_DIR}/minicli"

```

Our build pipeline will set up two distinct directories, separating the application dependencies from its executable entry point. The executable `minicli` script will be copied into `/usr/bin`, while the vendor files will be located at `/usr/share/minicli`.

## 4 — Building the minicli apk with melange

Before building the package, you'll need to create a temporary keypair to sign it. You can use the following command for that:

```shell
docker run --rm -v "${PWD}":/work cgr.dev/chainguard/melange keygen
```
This will generate a `melange.rsa` and `melange.rsa.pub` files in the current directory.

```
2024/08/01 16:55:31 INFO generating keypair with a 4096 bit prime, please wait...
2024/08/01 16:55:33 INFO wrote private key to melange.rsa
2024/08/01 16:55:33 INFO wrote public key to melange.rsa.pub
```

Next, build the apk defined in the `melange.yaml` file with the following command:

```shell
docker run --privileged --rm -v "${PWD}":/work \
  cgr.dev/chainguard/melange build melange.yaml \
  --arch amd64,aarch64 \
  --signing-key melange.rsa
```
This will set up a volume sharing your current folder with the location `/work` inside the container. We'll build packages for `amd64` and `aarch64` platforms and sign them using the `melange.rsa` key created in the previous command.

When the build is finished, you should be able to find a `packages` folder containing the generated apks (and associated apk index files):

```
packages
├── aarch64
│   ├── APKINDEX.json
│   ├── APKINDEX.tar.gz
│   └── hello-minicli-0.1.0-r0.apk
└── x86_64
    ├── APKINDEX.json
    ├── APKINDEX.tar.gz
    └── hello-minicli-0.1.0-r0.apk

3 directories, 6 files
```

You have successfully built a multi-architecture software package with melange!

## 5 — Building a Container Image with apko

With the apk packages and apk index in place, you can now build a container image and have your apk(s) installed within it.

The following `apko.yaml` file will create a container image tailored to the application we built in the previous steps. Because we defined the PHP dependencies as runtime dependencies within the apk, you don't need to require these packages again here. The container entrypoint command will be set to `/usr/bin/minicli`, where the application executable is located.

One important thing to note is how we reference the `hello-minicli` apk as a local package within the `repositories` section of the YAML file. The `@local` notation tells apko to search for apks in the specified directory, in this case `/work/packages`.

This is what the `apko.yaml` file included in our demo looks like, for your reference:

```yaml
contents:
  keyring:
    - https://packages.wolfi.dev/os/wolfi-signing.rsa.pub
    - ./melange.rsa.pub
  repositories:
    - https://packages.wolfi.dev/os
    - '@local /work/packages'
  packages:
    - wolfi-base
    - ca-certificates-bundle
    - hello-minicli@local
accounts:
  groups:
    - groupname: nonroot
      gid: 65532
  users:
    - username: nonroot
      uid: 65532
  run-as: 65532
entrypoint:
  command: /usr/bin/minicli advice
```

The following command will set up a volume sharing your current folder with the location `/work` in the apko container, running the `apko build` command to generate an image based on your `apko.yaml` definition file.

```shell
docker run --rm --workdir /work -v ${PWD}:/work cgr.dev/chainguard/apko \
  build apko.yaml hello-minicli:test hello-minicli.tar --arch host
```
This will build an OCI image based on your host system's architecture (specified by the `--arch host` flag). If you receive warnings at this point, those are likely related to the types of SBOMs being uploaded and can be safely ignored.

The command will generate a few new files in the app's directory:

- `hello-minicli.tar` — the packaged OCI image that can be imported with a `docker load` command
- `sbom-%host-architecture%.spdx.json` — an SBOM file for your host architecture in `spdx-json` format

Next, load your image within Docker:

```shell
docker load < hello-minicli.tar
```
```
7cbaefdf1c30: Loading layer   13.7MB/13.7MB
Loaded image: hello-minicli:test-%host-architecture%
```

Note that the `%host-architecture%` will vary, and there may be multiple images loaded into your Docker daemon. Be sure to edit the variable in the following `docker run` command to match your target architecture.

Now you can run your Minicli program with:

```shell
docker run --rm hello-minicli:test-%host-architecture%
```
The demo should output an advice slip such as:

```
Only those who attempt the impossible can achieve the absurd.
```

You have successfully built a minimalist container image with your apk package installed on it. This image is fully [OCI](https://opencontainers.org/) compatible and can be signed with [Cosign](/open-source/sigstore/cosign/how-to-sign-a-container-with-cosign/) for provenance attestation.

## Conclusion

In this guide, we packaged a PHP command-line app with melange. We also built a container image to install and run our custom apk, using the apko tool. For more information about apko, check our [Getting Started with apko](/open-source/apko/getting-started-with-apko/) guide.

The demo files are available at the [melange-php-demos](https://github.com/chainguard-dev/melange-php-demos) repository, in the `hello-minicli` subfolder. For additional information on how to debug your builds and other features, check the [melange](https://github.com/chainguard-dev/melange) and [apko](https://github.com/chainguard-dev/apko) repositories on GitHub.
