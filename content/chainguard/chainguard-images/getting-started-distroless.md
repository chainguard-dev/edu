---
title: "Getting Started with Distroless Images"
linktitle: "Going Distroless"
type: "article"
description: "How to leverage distroless images for improved container security"
date: 2024-03-21T08:49:31+00:00
lastmod: 2024-03-21T08:49:31+00:00
draft: false
tags: ["Chainguard Images", "Product", "Overview"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 030
toc: true
---

## About Distroless Images
[Distroless](https://blog.chainguard.dev/minimal-container-images-towards-a-more-secure-future/) container images are a type of container image  that is designed to be minimal. Unlike traditional images based on Debian or Ubuntu — which include package managers, utilities, and shells — distroless images typically contain only essential software required to run an application or service.

This minimal approach offers several benefits, including:

- **Enhanced Security:** By stripping out unnecessary components, distroless images reduce the potential attack surface for vulnerabilities. With fewer extraneous programs, there are fewer opportunities for malicious actors to exploit.
- **Simplified Dependency Management:** Traditional container images can introduce dependency bloat, making it difficult to track and manage exactly what's included. Distroless images keep things clear by only containing what's directly required for the application to function.
- **Potentially Smaller Image Sizes:** By eliminating extraneous OS components, distroless images can be significantly smaller than their full-blown counterparts.

Chainguard offers a mix of distroless and development (or builder) images that are minimalist and contain provenance attestations for increased security. Since distroless images have fewer tools and don't come with a package manager, some adaptation might be necessary when migrating from traditional base images. A typical approach is using multi stage builds to compose a final distroless image containing the additional artifacts required by the application in order to run successfully.

## Multi Stage Builds
A multi stage build is a technique for creating slimmer and more efficient container images. It allows you to define multiple stages within a single Dockerfile. Each stage acts like a separate build environment with its own base image and instructions.

The key benefit of multi stage builds is that they enable you to separate the build process from the final runtime environment. This separation helps in reducing the final image size by:

- **Using different base images**: You can leverage a larger image containing all the build tools in the initial stage and then switch to a smaller, leaner base image for the final stage that only includes the necessary runtime dependencies for your application.
- **Excluding unnecessary layers**: By separating the build and runtime stages, you can exclude all the temporary files, build tools, and intermediate artifacts from the final image. These elements are only required during the build process and not needed when running the application.

Overall, multi stage builds promote efficient container images by minimizing their size and optimizing their contents for execution.

### Example 1: Distroless images as runtime for static binaries
Distroless images are typically designed to work as platforms for running workloads in as minimal an environment as possible. In the case of languages that can compile completely static binaries (such as C and Rust), the **static** base image can be used as a runtime. You'll still need to get your application compiled in a separate build stage that has the tooling necessary to build it.

In this example, we'll build a distroless image to run a "Hello World" program in C. Start by creating a directory for the demo. We'll call it **distroless-demo**.

```sh
mkdir ~/distroless-demo && cd $_
```

Create a new Dockerfile within this directory. You can use `nano` or other command line editor of your choice.

```sh
nano Dockerfile
```

The following Dockerfile will build a final distroless image using two distinct build stages. The first stage, named `build`, builds a C program using the `cgr.dev/chainguard/gcc-glibc:latest` image. The final image, which is then based on the `cgr.dev/chainguard/static:latest` distroless image, will copy the compiled binary from the `build` environment and define it as the entry point command for the final image.

```dockerfile
# syntax=docker/dockerfile:1.4
FROM cgr.dev/chainguard/gcc-glibc:latest as build

COPY <<EOF /hello.c
#include <stdio.h>
int main() { printf("Hello Distroless!%c",0x0A); }
EOF
RUN cc -static /hello.c -o /hello

FROM cgr.dev/chainguard/static:latest

COPY --from=build /hello /hello
CMD ["/hello"]
```

Run the following command to build the demo image and tag it as `c-distroless`:

```shell
DOCKER_BUILDKIT=1 docker build -t c-distroless  .
```

If you receive an error, you may try removing the top line of the Dockerfile. Now you can run the image with:

```shell
docker run c-distroless
```

You should get output like this:

```
Hello Distroless!
```

You can note the size of the resulting image.

```shell
docker images c-distroless
```

```
REPOSITORY     TAG       IMAGE ID       CREATED          SIZE
c-distroless   latest    cd3bb76a84f5   45 seconds ago   2.04MB
```

If you look into the image layers with `docker inspect c-distroless`, you'll also notice that it has only two layers: a single layer from the `static` image that serves as base for the final image, and one layer with the `COPY` command that brings in the compiled binary from the **build** stage.

```shell
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:cfc10a76380242be256af62b8782e536770dee83dcc823fce6c196c1ef5638e5",
                "sha256:bc7690d8bd810d969e6601d8468b4ae42fa411dfe460440e96092db454d80080"
            ]
        },
```

### Example 2: Incorporating Application-Level Dependencies in Distroless Images

When working with language ecosystems that have their own dependency management tools such as PHP (Composer) and Node (npm), a multi stage build is necessary to include application dependencies within the final distroless runtime.

The next example creates a Dockerfile to run a demo PHP application that has third-party dependencies managed by [Composer](https://getcomposer.org/). The application is a single executable that queries the [cat facts API](https://catfact.ninja/) and returns a random fact.

Start by creating a directory for the demo. We'll call it **distroless-php**.

```sh
mkdir ~/distroless-php && cd $_
```

The following command will create a new `composer.json` file with a single dependency, a small curl library called `minicli/curly`. We are using a shared volume so that the `vendor` folder is shared with our local directory.

```shell
docker run --rm --entrypoint composer --user=root -v ${PWD}:/app cgr.dev/chainguard/php:latest-dev require minicli/curly
```
In this case, we had to use the **root** image user in order to be able to write files in the current host directory. The following command will fix file permissions for our current system user:

```shell
sudo chown -R ${USER}:${USER} .
```
Now create the PHP executable. You can call it `catfact.php`:

```shell
nano catfact.php
```

The following code makes a query to the cat facts API, returning the quote as output. Copy the contents to your own `catfact.php` script:

```php
<?php

require __DIR__ . '/vendor/autoload.php';

$curly = new Minicli\Curly\Client();
$response = $curly->get("https://catfact.ninja/fact");
if ($response['code'] === 200) {
    echo "\n" . json_decode($response['body'], true)['fact'] . "\n";
    return 0;
}

echo "query error.";
return 1;
```

Save the file when you're done. Now you can create your Dockerfile.

```sh
nano Dockerfile
```

The following Dockerfile will create a `run.php` script that makes a curl query using the library we just added as a dependency.

```Dockerfile
FROM cgr.dev/chainguard/php:latest-dev AS builder
USER root
COPY . /app
RUN chown -R php /app
USER php
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

FROM cgr.dev/chainguard/php:latest
COPY --from=builder /app /app

ENTRYPOINT [ "php", "/app/catfact.php" ]
```

Now you can build the image with:

```shell
docker build . -t distroless-demo-php
```

Finally, you can run the new app with:

```shell
docker run --rm distroless-demo-php
```

And you should get a cat fact as output, such as:

```shell
A domestic cat can run at speeds of 30 mph.
```

Upon inspection with `docker images`, you can check the image size around 38MB:

```shell
❯ docker images distroless-demo-php
REPOSITORY            TAG       IMAGE ID       CREATED         SIZE
distroless-demo-php   latest    8691d09f56ca   2 minutes ago   37.9MB
```

For comparison, the `php:cli-alpine` image is almost 3 times bigger:

```shell
❯ docker images php:cli-alpine
REPOSITORY   TAG          IMAGE ID       CREATED      SIZE
php          cli-alpine   7879e816aba0   6 days ago   104MB
```

## Final Considerations

Distroless images offer a compelling approach to creating minimal and secure container images by stripping away system components that are unnecessary at execution time, such as package managers and shells. While such images offer many advantages, they might require some adjustments in your existing development and deployment workflows. In this guide we demonstrated how to use multi stage builds to create final distroless images that include additional components, such as static binaries and application-level dependencies.

You can find more examples in our [Getting Started Guides](/chainguard/chainguard-images/getting-started/) page. Check also our article on [Debugging Distroless Images](/chainguard/chainguard-images/debugging-distroless-images/) for important tips when you run into issues and need to debug containers running distroless images.
