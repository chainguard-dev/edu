---
title: "Getting Started with the PHP Chainguard Images"
type: "article"
description: "Documentation on how to get started with the PHP Chainguard Images"
date: 2023-01-09T11:07:52+02:00
lastmod: 2023-01-09T11:07:52+02:00
draft: false
images: []
referenceimage: php
menu:
  docs:
    parent: "php-guides"
weight: 10
toc: true
---

The PHP images maintained by Chainguard are a mix of development and production distroless images that are suitable for building and running command-line PHP workloads.

Because PHP applications typically require user-land package installs via Composer, using a pure distroless image for building your application would not work. In cases like this, you'll need to implement a [multi-stage Docker build]() that uses one of the `-dev` images to set up the application.

In this guide, we'll set up a distroless container image based on Wolfi as a runtime to execute a command-line PHP application.

{{< details "What is distroless" >}}
Distroless images are minimalist container images containing only essential software required to build or execute an application. That means no package manager, no shell, and no bloat from software that only makes sense on bare metal servers.
{{< /details >}}

{{< details "What is Wolfi" >}}
Wolfi is a community Linux undistro created specifically for containers. This brings distroless to a new level, including additional features targeted at securing the software supply chain of your application environment: comprehensive SBOMs, signatures, daily updates, and timely CVE fixes.
{{< /details >}}

{{< details "Chainguard Images" >}}
[Chainguard Images](https://www.chainguard.dev/chainguard-images?utm_source=docs) are a mix of distroless and development images that have glibc (Wolfi-based) and Musl (Alpine-based) variants.
{{< /details >}}

## Step 1: Setting up a Demo Application

We'll start by creating a basic command-line PHP application to serve as a demo. This app will generate random names based on a list of nouns and adjectives. To exemplify usage with Composer, the app will have a single dependency on [minicli](https://github.com/minicli/minicli), a minimalist CLI framework for PHP.

First, create a directory for your app. In this guide we'll use `wolfi-php`:

```shell
mkdir ~/wolfi-php && cd ~/wolfi-php
```

If you have a local PHP development environment with Composer, you can run the following command to download the single dependency of this app.

```
composer require minicli/minicli
```

If you don't have a local PHP development environment, you can use the `php:latest-glibc-dev` image variant with a volume in order to install application dependencies with Composer:

```shell
docker run --rm -v ${PWD}:/work --entrypoint composer \
    cgr.dev/chainguard/php:latest-glibc-dev \
    require minicli/minicli --working-dir=/work
```

If you used the Docker method, make sure permissions are right on the generated files:

```shell
sudo chown -R ${USER}.${USER} .
```

Create a new file to serve as the application entry point. We'll call it "namegen":

```shell
touch namegen
```

Next, open the file in your code editor of choice.

The following PHP script defines a minimalist CLI app with a single command called "get". It returns a random name based on a list of nouns and a list of adjectives.

```php
#!/usr/bin/php
<?php

require __DIR__ . '/vendor/autoload.php';

use Minicli\App;

$app = new App();

$app->registerCommand('get', function () use ($app) {

    $animals = [ 'turtle', 'seagull', 'octopus', 'shark', 'whale', 'dolphin', 'walrus', 'penguin', 'seahorse'];
    $adjectives = [ 'ludicrous', 'mischievous', 'graceful', 'fortuitous', 'charming', 'ravishing', 'gregarious'];

    $app->getPrinter()->info($adjectives[array_rand($adjectives)] . '-' . $animals[array_rand($animals)]);
});

$app->runCommand($argv);

```

Copy this content to your `namegen` script, save and close the file. Next, make the script executable with:

```shell
chmod +x namegen
```

You can now execute the app to test it out. If you have `php` locally, run:

```shell
php namegen get
```

If you're using the Docker setup, run:

```shell
docker run --rm -v ${PWD}:/work \
    cgr.dev/chainguard/php:latest-glibc \
    /work/namegen get
```

The command should output a random name combination:

```shell
ludicrous-walrus
```

The demo application is now ready. In the next step, you'll create a Dockerfile to run your app.

## Step 2: Creating the Dockerfile

To make sure our final image is _distroless_ while still being able to install dependencies with Composer, our build will consist of **two** stages: first, we'll build the application using the `glibc-dev` image variant, which is Wolfi-based and includes Composer and other useful tools for development.
Then, we'll create a separate stage for the final image, which will be based on the `glibc` variant. That is a distroless image also based on Wolfi, which means it doesn't come with Composer or even a shell.

Create a Dockerfile with:

```shell
touch Dockerfile
```

The following Dockerfile will:

1. Start a new build stage based on the `php:latest-glibc-dev` image and call it `builder`;
2. Copy files from the current directory to the `/app` location in the container;
3. Enter the `/app` directory and run `composer install` to install any dependencies;
4. Start a new build stage based on the `php:latest-glibc`;
5. Copy the application from the `builder` stage;
6. Set up the application as entry point for this image.

Copy this content to your own `Dockerfile`:

```Dockerfile
FROM cgr.dev/chainguard/php:latest-glibc-dev AS builder
COPY guides /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

FROM cgr.dev/chainguard/php:latest-glibc
COPY --from=builder /app /app

ENTRYPOINT [ "php", "/app/namegen" ]
```
Save the file when you're finished.

You can now build the image with:

```shell
docker build . -t php-namegen get
```

Once the build is finished, run the image with:

```shell
docker run --rm php-namegen get
```

And you should get output similar to what you got before, with a random name combination.

```
fortuitous-octopus
```

## Advanced Usage

If your use case requires a more specific set of packages that the general-purpose PHP Chainguard Images don't provide, you'll first need to check if the package you need is available for the base distro you choose.

For Wolfi-based images, check the [Wolfi](https://github.com/wolfi-dev/os) distro repository. If the package you want is there, you can use the [wolfi-base](/chainguard/chainguard-images/reference/wolfi-base/overview) image in a Dockerfile and install what you need with `apk`, then use the resulting image as base for your app.

For Alpine-based images, if the packages you need are available in the [Alpine](https://pkgs.alpinelinux.org/packages) repositories, you can use the [alpine-base](/chainguard/chainguard-images/reference/alpine-base/overview) image in a Dockerfile and install what you need with `apk`, then use the resulting image as base for your app.

If the packages you need are not available for your your base distro of choice, you can build your own apks using [melange](/open-source/melange/overview). Please refer to [this guide](/open-source/melange/tutorials/getting-started-with-melange/) for more information on how to do that.
