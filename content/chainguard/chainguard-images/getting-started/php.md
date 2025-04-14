---
title: "Getting Started with the PHP Chainguard Container"
type: "article"
linktitle: "PHP"
aliases:
- /chainguard/chainguard-images/getting-started/getting-started-php
description: "Tutorial on how to get started with the Chainguard PHP container image "
date: 2023-01-09T11:07:52+02:00
lastmod: 2025-03-24T11:07:52+02:00
tags: ["Chainguard Containers", "Products"]
draft: false
images: []
menu:
  docs:
    parent: "getting-started"
weight: 045
toc: true
---

The PHP container images maintained by Chainguard include both our standard, minimal images and development variants, both of which are suitable for building and running PHP workloads. The `latest-fpm` variant serves PHP applications over FastCGI, while the `latest` variant runs PHP applications from the command line.

In this guide, we'll set up a demo and demonstrate how you can use Chainguard Containers to develop, build, and run PHP applications.

This tutorial requires Docker to be installed on your local machine. If you don't have Docker installed, you can download and install it from the [official Docker website](https://docs.docker.com/get-docker/).

{{< details "What is distroless?" >}}
{{< blurb/distroless >}}
{{< /details >}}

{{< details "What is Wolfi?" >}}
{{< blurb/wolfi >}}
{{< /details >}}

{{< details "Chainguard Images" >}}
{{< blurb/images >}}
{{< /details >}}

## 1. Setting up a (CLI) Demo Application

We'll start by getting the demo application ready. This CLI app generates random names based on a list of nouns and adjectives. To exemplify usage with Composer, the app has a single dependency on [minicli](https://github.com/minicli/minicli), a minimalist CLI framework for PHP.

Start by cloning the demos repository to your local machine:

```shell
git clone git@github.com:chainguard-dev/edu-images-demos.git
```

Locate the `namegen` demo and cd into its directory:

```shell
cd edu-images-demos/php/namegen
```

You can use the `php:latest-dev` image variant with a volume in order to install application dependencies with Composer. We'll use the `root` user to be able to write to the volume mounted in the container:

```shell
docker run --rm -v ${PWD}:/app --entrypoint composer --user root \
    cgr.dev/chainguard/php:latest-dev \
    install --no-progress --no-dev --prefer-dist
```

You'll get output like this, indicating that the package `minicli/minicli` was installed:

```shell
Installing dependencies from lock file
Verifying lock file contents can be installed on current platform.
Package operations: 1 install, 0 updates, 0 removals
  - Downloading minicli/minicli (4.2.0)
  - Installing minicli/minicli (4.2.0): Extracting archive
Generating autoload files
1 package you are using is looking for funding.
Use the `composer fund` command to find out more!
```
Next, make sure permissions are set correctly on the generated files.

On Linux systems run the following:

```shell
sudo chown -R ${USER}:${USER} .
```

On macOS systems, run this:

```shell
sudo chown -R ${USER} .
```

The application should now be ready to be executed. For transparency, here is the code that will be executed, which you'll find in the `namegen` script:

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

You can now execute the app to test it out. Run the following command:

```shell
docker run --rm -v ${PWD}:/work \
    cgr.dev/chainguard/php:latest \
    /work/namegen get
```

The command should output a random name combination:

```shell
ludicrous-walrus
```
In the next step, you'll build the application in a multi-stage Dockerfile.

## 2. Building a Distroless Container for the Application

We'll now build a distroless container for the application. To be able to install dependencies with Composer, our build will consist of **two** stages. First, we'll build the application using the development variant, a Wolfi-based image that includes Composer and other useful tools for development. Then, we'll create a separate stage for the final container. The resulting container will be based on the distroless PHP Wolfi image, which means it doesn't come with Composer or even a shell.

For reference, here is the content of the included `Dockerfile`:

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

ENTRYPOINT [ "php", "/app/namegen" ]
```
This Dockerfile will:

1. Start a new build stage based on the `php:latest-dev` container image and call it `builder`;
2. Copy files from the current directory to the `/app` location in the container;
3. Enter the `/app` directory and run `composer install` to install any dependencies;
4. Start a new build stage based on the `php:latest` image;
5. Copy the application from the `builder` stage;
6. Set up the application as entry point for this container.

You can now build the container with:

```shell
docker build . --pull -t php-namegen
```
You'll get output similar to this:

```shell
[+] Building 0.1s (12/12) FINISHED                                                                        docker:default
 => [internal] load build definition from Dockerfile                                                                0.0s
 => => transferring dockerfile: 322B                                                                                0.0s
 => [internal] load metadata for cgr.dev/chainguard/php:latest-dev                                                  0.0s
 => [internal] load metadata for cgr.dev/chainguard/php:latest                                                      0.0s
 => [internal] load .dockerignore                                                                                   0.0s
 => => transferring context: 2B                                                                                     0.0s
 => [internal] load build context                                                                                   0.0s
 => => transferring context: 4.86kB                                                                                 0.0s
 => [builder 1/4] FROM cgr.dev/chainguard/php:latest-dev                                                            0.0s
 => [stage-1 1/2] FROM cgr.dev/chainguard/php:latest                                                                0.0s
 => CACHED [builder 2/4] COPY . /app                                                                                0.0s
 => CACHED [builder 3/4] RUN chown -R php /app                                                                      0.0s
 => CACHED [builder 4/4] RUN cd /app &&     composer install --no-progress --no-dev --prefer-dist                   0.0s
 => CACHED [stage-1 2/2] COPY --from=builder /app /app                                                              0.0s
 => exporting to image                                                                                              0.0s
 => => exporting layers                                                                                             0.0s
 => => writing image sha256:e617d7afd472d4a78d82060eaacd3a1c33310d6a267f6aaf9aa34b44e3ef8e5c                        0.0s
 => => naming to docker.io/library/php-namegen                                                                      0.0s
```
Once the build is finished, run the container with:

```shell
docker run --rm php-namegen get
```

And you should get output similar to what you got before, with a random name combination.

```
fortuitous-octopus
```

If you inspect the container image with a `docker image inspect php-namegen`, you'll notice that it has only **two** layers, thanks to the use of a multi-staging Docker build.

```shell
docker image inspect php-namegen
```
```shell
...
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:52cf795862535c5f22dac055428527508088becebbe00293457693a5f8fa1df2",
                "sha256:95a8dc6d81c92158ac032e5167768a04e45f25b3bf4009c5698673c19d36d5c2"
            ]
        },
        "Metadata": {
            "LastTagTime": "2024-11-15T12:52:18.412117879+01:00"
        }
    }
]

```
In such cases, the last `FROM` section from the Dockerfile is the one that composes the final image. That's why in our case it only adds one layer on top of the base `php:latest` image, containing the `COPY` command we use to copy the application from the build stage to the final container.

It's worth highlighting that nothing is carried from one stage to the other unless you copy it. That facilitates creating a slim final image with only what's necessary to execute the application.

## 3. Working with the PHP-FPM Image Variant

The `latest-fpm` image variant is suitable for running PHP applications over FastCGI, to be served by a web server such as Nginx. In this section, we'll run a Docker Compose setup using the `latest-fpm` image variant and the Chainguard Nginx image.

The `namegen-api` demo is a variation of the previous demo, but it serves the random name generation over HTTP. The application responds with a JSON payload containing the animal and adjective combination, and accepts an optional `animal` parameter to specify the animal for the final suggested name.

Start by accessing the `namegen-api` demo folder. This should be at the same level as the previous `namegen` demo in the `edu-images-demos` repository. If your terminal is still open on the previous demo, you can navigate to the `namegen-api` folder with:

```shell
cd ../namegen-api
```

The `index.php` file contains the following code:

```php
<?php

$animals = [ 'turtle', 'seagull', 'octopus', 'shark', 'whale', 'dolphin', 'walrus', 'penguin', 'seahorse'];
$adjectives = [ 'ludicrous', 'mischievous', 'graceful', 'fortuitous', 'charming', 'ravishing', 'gregarious'];

$chosenAdjective = $adjectives[array_rand($adjectives)];
$chosenAnimal = $_GET['animal'] ?? $animals[array_rand($animals)];

echo json_encode(['animal' => $chosenAnimal, 'adjective' => $chosenAdjective]);
```

To serve this application over HTTP, we'll use the `latest-fpm` image variant in a Docker Compose setup. The following `docker-compose.yml` is included within the `namegen-api` folder:

```yaml
services:
  app:
    image: cgr.dev/chainguard/php:latest-fpm
    restart: unless-stopped
    working_dir: /app
    volumes:
      - ./:/app

  nginx:
    image: cgr.dev/chainguard/nginx
    restart: unless-stopped
    ports:
      - 8000:80
    volumes:
      - ./:/app
      - ./nginx.conf:/etc/nginx/nginx.conf
```

This Docker Compose setup defines two services: `app` and `nginx`. The `app` service uses the `latest-fpm` image variant and mounts the current directory to the `/app` directory in the container. The `nginx` service uses the Chainguard Nginx container image and also mounts the current directory to the `/app` directory in the container, setting it as the document root with a custom configuration. A second volume replaces the default Nginx configuration with our custom one, included as `nginx.conf` in the same directory:

```
events {
  worker_connections  1024;
}

http {
    server {
        listen 80;
        index index.php index.html;
        root /app/public;
        location ~ \.php$ {
            try_files $uri =404;
            fastcgi_split_path_info ^(.+\.php)(/.+)$;
            fastcgi_pass app:9000;
            fastcgi_index index.php;
            include fastcgi_params;
            fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
            fastcgi_param PATH_INFO $fastcgi_path_info;
        }
        location / {
            try_files $uri $uri/ /index.php?$query_string;
            gzip_static on;
        }
    }
}
```

To run this setup, execute:

```shell
docker-compose up
```

This command will start the services defined in the `docker-compose.yml` file. You can access the application at `http://localhost:8000` in your browser, or you can make a curl request to it:

```shell
curl http://localhost:8000
```
You should get a JSON response with a random name combination:

```
{"animal":"octopus","adjective":"ludicrous"}
```

You can also try passing an `animal` parameter to the URL:

```shell
curl 'http://localhost:8000?animal=cat'
```

```
{"animal":"cat","adjective":"mischievous"}
```

To stop the services, you can press `Ctrl+C` in the terminal where you ran `docker-compose up`.

## Advanced Usage

{{< blurb/images-advanced image="PHP" >}}
