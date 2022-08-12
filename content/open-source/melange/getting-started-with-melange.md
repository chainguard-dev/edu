---
title: "Getting Started with melange"
lead: "The declarative apk builder"
type: "article"
description: "The declarative apk builder"
date: 2022-07-21T15:21:01+02:00
lastmod: 2022-07-21T15:21:01+02:00
contributors: ["Erika Heidi"]
draft: false
images: []
menu:
  docs:
    parent: "melange"
weight: 100
toc: true
---

[melange](https://github.com/chainguard-dev/melange) is an [apk](https://wiki.alpinelinux.org/wiki/Package_management) builder tool that uses declarative pipelines to create apk packages. From a single YAML file, users are able to generate multi-architecture apks that can be injected directly into [apko](https://github.com/chainguard-dev/apko) builds, which renders apko and melange a [powerful combination for any container image factory](https://blog.chainguard.dev/secure-your-software-factory-with-melange-and-apko/).


## Why melange

Software supply chain threats have been growing exponentially in the last few years, according to [industry leaders and security researchers (PDF)](https://www.usenix.org/system/files/login/articles/login_winter20_17_geer.pdf). With the popularization of automated workflows and cloud native deployments, it is more important than ever to provide users with the ability to attest the provenance of all relevant software artifacts.

Instead of building your application together with your components and system dependencies, you can build your application once and compose it into different architectures and distributions using melange, as if they were any other component of an image.

In this guide, you'll learn how to build a software package with melange. To demonstrate the versatile combination of melange and apko builds, we'll package a small command-line PHP script and build a minimalist container image with the generated apk. All files used in this demo are open source and available at the [melange-php-demos](https://github.com/chainguard-dev/melange-php-demos/tree/main/hello-minicli) repository.

## Requirements

Our guide is compatible with operating systems that support Docker and shared volumes. Please follow the [appropriate Docker installation instructions](https://docs.docker.com/get-docker/) for your operating system.

You won't need PHP or Composer installed on your system, since we'll be using Docker to build the demo app.

### Note for Linux Users

In order to be able to build apks for multiple architectures using Docker, you'll need to register additional QEMU headers within your kernel. This is done automatically for Docker Desktop users, so if you are on macOS you don't need to run this additional step.

Run the following command to register the necessary handlers within your kernel, using the [multiarch/qemu-user-static](https://github.com/multiarch/qemu-user-static) image.

```shell
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
```

You should now be able to build apks for all architectures that melange supports.

## Step 1 — Downloading the melange Image

The fastest way to get melange up and running on your system is by using the [official melange image](https://github.com/distroless/melange) with Docker. Start by pulling the official melange image into your local system:

```shell
docker pull distroless.dev/melange:latest
```

This will download the latest version of the distroless melange image, which is rebuilt every night for extra freshness.

Check that you're able to run melange with `docker run`.

```shell
docker run --rm distroless.dev/melange version
```

You should get output similar to the following:

```
  __  __   _____   _          _      _   _    ____   _____
 |  \/  | | ____| | |        / \    | \ | |  / ___| | ____|
 | |\/| | |  _|   | |       / _ \   |  \| | | |  _  |  _|
 | |  | | | |___  | |___   / ___ \  | |\  | | |_| | | |___
 |_|  |_| |_____| |_____| /_/   \_\ |_| \_|  \____| |_____|
melange

GitVersion:    v0.1.0-67-g108fd6a
GitCommit:     108fd6a5e400bd100ef6db813380de44516de6e6
GitTreeState:  clean
BuildDate:     2022-08-01T13:36:41
GoVersion:     go1.18.5
Compiler:      gc
Platform:      linux/amd64
```

With melange installed, you’re ready to proceed.

## Step 2 — Preparing the Demo App

To demonstrate melange's features with a minimalist application that has real-world functionality, we'll create a PHP command line app that queries the [Slip advice](https://api.adviceslip.com/) API and outputs a random piece of advice. The app is a single-file script built with [Minicli](https://github.com/minicli).

Create a folder in your home directory to place your demo files, then `cd` into it:

```shell
mkdir ~/hello-minicli && cd $_
```

Run the following command, which will use the official Composer image to generate a `composer.json` file and download `minicli/minicli`:

```shell
docker run --rm -it -v "${PWD}":/app composer require minicli/minicli
```

Once you receive confirmation that the download was completed, we'll need a second dependency to query the advice slip API. Run the following command to include `minicli/curly`, a simple curl wrapper for Minicli:

```shell
docker run --rm -it -v "${PWD}":/app composer require minicli/curly
```

Next, create a new file called `minicli` using your text editor of choice. This will be the executable we'll ship with our apk package.

```shell
nano minicli
```

The following code will set up a new Minicli application and define a single command called `advice`. This will make a GET query to the advice slip API, check the return code, and print the resulting quote when the query is successful.

Because our app will be built into an apk and later on embedded on a container image, we'll check for the right location of the vendor folder before requiring the `autoload.php` file. This file must be included before the application is instantiated. The `MINICLI_HOME` environment variable can be used to customize the vendor location, which is by default set to `/usr/share/minicli`.

Place the following code in your `minicli` file:

```php
#!/usr/bin/env php

<?php

use Minicli\App;
use Minicli\Curly\Client;
use Minicli\Exception\CommandNotFoundException;

if (php_sapi_name() !== 'cli') {
    exit;
}

$vendor_path = __DIR__ . '/vendor/autoload.php';

if (!file_exists($vendor_path)) {
    $minicli_home = getenv('MINICLI_HOME') ?: '/usr/share/minicli';
    $vendor_path = $minicli_home . '/vendor/autoload.php';
}

require $vendor_path;


$app = new App([
    'debug' => true
]);

$app->setSignature('Usage: ./minicli advice');

$app->registerCommand('advice', function () use ($app) {
    $client = new Client();

    $response = $client->get('https://api.adviceslip.com/advice');
    if ($response['code'] !== 200) {
        $app->getPrinter()->error('An API error has occurred.');
        return;
    }

    $advice = json_decode($response['body'], true);
    $app->getPrinter()->info($advice['slip']['advice']);
});

try {
    $app->runCommand($argv);
} catch (CommandNotFoundException $notFoundException) {
    $app->getPrinter()->error("Command Not Found.");
    return 1;
} catch (Exception $exception) {
    if ($app->config->debug) {
        $app->getPrinter()->error("An error occurred:");
        $app->getPrinter()->error($exception->getMessage());
    }
    return 1;
}

return 0;

```

Save and close the file when you're done. If you're using `nano`, you can do that by typing `CTRL+X`, then `Y` and `ENTER` to confirm.

Set the script as executable with:

```shell
chmod +x minicli
```

Now you can run the application to make sure it's functional. We'll also use Docker for that:

```shell
docker run --rm -it -v "${PWD}":/app php:8.1-cli php /app/minicli advice
```

You should get a random piece of advice such as:

```
Gratitude is said to be the secret to happiness.
```

With the application ready, you can start building your package.

## Step 3 — Creating the melange YAML File
The `melange.yaml` file is where you'll declare the details and specifications of your apk package. For code that generates self-contained binaries, this is typically where you'll build your application artifacts with compiler tools. In the case of interpreted languages, you'll likely build your application by downloading vendor dependencies, setting up relevant paths, and setting the environment up for production.

Create a new file in your `hello-minicli` folder called `melange.yaml`:

```shell
nano melange.yaml
```

The melange specification file contains three main sections:

- **package**: defines package specs, such as name, license, and runtime dependencies. Runtime dependencies will be brought into the system automatically as dependencies when the apk is installed.
- **environment**: defines how the environment should be prepared for the build, including required packages and their source repositories. Anything that is only required at build time goes here, and shouldn't be part of the runtime dependencies.
- **pipeline**: defines the build pipeline for this package.

One of the best advantages of using melange is to be able to control all steps of your build pipeline, and include only what's absolutely necessary. This way, you'll be able to build smaller and more secure container images by removing unnecessary dependencies.

Place the following content in your `melange.yaml` file:

```yaml
package:
  name: hello-minicli
  version: 0.1.0
  description: Minicli melange demo
  target-architecture:
    - all
  copyright:
    - license: Apache-2.0
      paths:
        - "*"
  dependencies:
    runtime:
      - php81
      - php81-common
      - php81-curl
      - php81-openssl

environment:
  contents:
    repositories:
      - https://dl-cdn.alpinelinux.org/alpine/edge/main
      - https://dl-cdn.alpinelinux.org/alpine/edge/community
    packages:
      - alpine-baselayout-data
      - ca-certificates-bundle
      - curl
      - php81
      - php81-common
      - php81-curl
      - php81-openssl
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

Save and close the file when you're done.

Our build pipeline will set up two distinct directories, separating the application dependencies from its executable entry point. The executable `minicli` script will be copied into `/usr/bin`, while the vendor files will be located at `/usr/share/minicli`.

## Step 4 — Building your apk

First make sure you're at the `~/hello-minicli` directory.

To get started, create a temporary keypair to sign your melange packages:

```shell
docker run --rm -v "${PWD}":/work distroless.dev/melange keygen
```
This will generate a `melange.rsa` and `melange.rsa.pub` files in the current directory.

```
2022/08/05 14:46:05 generating keypair with a 4096 bit prime, please wait...
2022/08/05 14:46:08 wrote private key to melange.rsa
2022/08/05 14:46:08 wrote public key to melange.rsa.pub
```

Next, build the apk defined in the `melange.yaml` file with the following command:

```shell
docker run --privileged --rm -v "${PWD}":/work \
  distroless.dev/melange build melange.yaml \
  --arch x86,amd64,aarch64,armv7 \
  --keyring-append melange.rsa
```
This will set up a volume sharing your current folder with the location `/work` inside the container. We'll build packages for `x86`, `amd64`, `aarch64`, and `armv7` platforms and sign them using the `melange.rsa` key.

When the build is finished, you should be able to find a `packages` folder containing the generated apks:

```
packages
├── aarch64
│   └── hello-minicli-0.1.0-r0.apk
├── armv7
│   └── hello-minicli-0.1.0-r0.apk
├── x86
│   └── hello-minicli-0.1.0-r0.apk
└── x86_64
    └── hello-minicli-0.1.0-r0.apk

4 directories, 4 files
```

You have successfully built a multi-architecture software package with melange!

The only thing left to do now is to create an apk index for your packages. This is necessary to install the apks later on within your container image.

Run the following command, which will loop through your `packages` folder, generate an index, and sign it with the melange key:

```shell
docker run --rm -v "${PWD}":/work \
    --entrypoint sh \
    distroless.dev/melange -c \
        'cd packages && for d in `find . -type d -mindepth 1`; do \
            ( \
                cd $d && \
                apk index -o APKINDEX.tar.gz *.apk && \
                melange sign-index --signing-key=../../melange.rsa APKINDEX.tar.gz\
            ) \
        done'
```

For each architecture that you have specified with `--arch` when running the `melange build` command, you should get output similar to this:

```
Index has 1 packages (of which 1 are new)
2022/08/05 14:57:29 signing index apkINDEX.tar.gz with key ../../melange.rsa
2022/08/05 14:57:29 appending signature to index apkINDEX.tar.gz
2022/08/05 14:57:29 writing signed index to apkINDEX.tar.gz
2022/08/05 14:57:29 signed index apkINDEX.tar.gz with key ../../melange.rsa
```
If you receive warnings about unsatisfiable package names at this point, feel free to ignore those as the melange image may not have every runtime dependency installed within it. These dependencies will be brought in automatically when the generated apks are installed.

Note that it is currently in the roadmap of the melange project to [automate this step](https://github.com/chainguard-dev/melange/issues/96), so that the package index is built automatically when you run the `melange build` command.

## Step 5 — Building a Container Image with apko

With the apk packages and apk index in place, you can now build a container image and have your apk(s) installed within it.

Create a new file called `apko.yaml` in your `~/hello-minicli` directory:

```shell
nano apko.yaml
```

The following apko specification will create a container image tailored to the application we built in the previous steps. Because we defined the PHP dependencies as runtime dependencies within the apk, you don't need to require these packages again here. The container entrypoint command will be set to `/usr/bin/minicli`, where the application executable is located.

One important thing to note is how we reference the `hello-minicli` apk as a local package within the `repositories` section of the YAML file. The `@local` notation tells apko to search for apks in the specified directory, in this case `/work/packages`.

Place the following text in your `apko.yaml` file:

```yaml
contents:
  repositories:
    - https://dl-cdn.alpinelinux.org/alpine/edge/main
    - https://dl-cdn.alpinelinux.org/alpine/edge/community
    - '@local /work/packages'
  packages:
    - alpine-baselayout-data
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

Save and close the file when you're done. You are now ready to build your container image.

The following command will set up a volume sharing your current folder with the location `/work` in the apko container, running the `apko build` command to generate an image based on your `apko.yaml` definition file.

```shell
docker run --rm -v ${PWD}:/work distroless.dev/apko \
  build apko.yaml hello-minicli:test hello-minicli.tar \
  -k melange.rsa.pub
```
This will build an OCI image based on your host system's architecture. If you receive warnings at this point, those are likely related to the types of SBOMs being uploaded and can be safely ignored.

The command will generate a few new files in the app's directory:

- `hello-minicli.tar` — the packaged OCI image that can be imported with a `docker load` command
- `sbom-x86_64.cdx` — an SBOM file for `x86_64` architecture in `cdx` format
- `sbom-x86_64.spdx.json` — an SBOM file for `x86_64` architecture in `spdx-json` format

Next, load your image within Docker:

```shell
docker load < hello-minicli.tar
```
```
10f951ac3cd2: Loading layer [==================================================>]  7.764MB/7.764MB
Loaded image: hello-minicli:test
```
Now you can run your Minicli program with:

```shell
docker run --rm hello-minicli:test
```
The demo should output an advice slip such as:

```
Only those who attempt the impossible can achieve the absurd.
```

You have successfully built a minimalist container image with your apk package installed on it. This image is fully [OCI](https://opencontainers.org/) compatible and can be signed with [Cosign](/open-source/sigstore/how-to-sign-a-container-with-cosign/) for provenance attestation.

## Conclusion

In this guide, we built a demo command line application and packaged it with melange. We also built a container image to install and run our custom apk, using the apko tool. For more information about apko, check our [Getting Started with apko](/open-source/apko/getting-started-with-apko/) guide.

The demo files are available at the repository [melange-php-demos](https://github.com/chainguard-dev/melange-php-demos), in the `hello-minicli` subfolder. For more information on how to debug your builds, please refer to the demo's [README](https://github.com/chainguard-dev/melange-php-demos/tree/main/hello-minicli) file and check the official documentation for [melange](https://github.com/chainguard-dev/melange) and [apko](https://github.com/chainguard-dev/apko).
