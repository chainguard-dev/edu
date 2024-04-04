---
title: "Migrating to PHP Chainguard Images"
linktitle: "Migrating PHP"
type: "article"
description: "Guidance on how to migrate PHP Dockerfile workloads to use Chainguard Images"
date: 2024-04-04T15:56:52-07:00
lastmod: 2024-04-04T15:56:52-07:00
draft: false
tags: ["Images", "Product", "Conceptual"]
images: []
weight: 100
toc: true
---

Chainguard Images are built on top of [Wolfi](/chainguard/open-source/wolfi/), a Linux _undistro_ designed specifically for containers. Our PHP images have a minimal design that ensures a smaller attack surface, which results in smaller images [with low to zero](/chainguard/chainguard-images/vuln-comparison/php/) CVEs. Nightly builds deliver fresh images whenever updated packages are available, which also helps to reduce the toil of manually patching CVEs in PHP images.

This article will assist you in the process of migrating your existing PHP Dockerfiles to leverage the benefits of Chainguard Images, for a smaller attack surface and a more secure application footprint.

## Chainguard PHP Images

Chainguard PHP Images offer multiple variants catering to distinct use cases, such as command-line interfaces (CLI) and web applications. Each variant comes in two flavors: a minimal runtime image (distroless) and a builder image distinguished by the `-dev` suffix (e.g., `latest-dev`).

In a nutshell, distroless images don't include a package manager or a shell, being used exclusively as runtimes to keep the environment to a minimum. Builder images, on the other hand, include packages such as `apk` and `composer` for building PHP applications. Builder images can be used _as-is_ to provide a more straightforward migration path, but we encourage users to combine both images in a multi stage environment to build a final distroless image that serves as a strict application runtime, whenever that is possible.

For a deeper exploration of distroless images and their differentiation from standard base images, refer to the guide on [Getting Started with Distroless images](/chainguard/chainguard-images/getting-started-distroless/).

### Migrating from non-apk systems
When migrating from distributions that are not based on the `apk` ecosystem, you'll need to update your Dockerfile accordingly. Our high-level guide on [Migrating to Chainguard Images](https://edu.chainguard.dev/chainguard/migration-guides/migrating-to-chainguard-images/) contains details about distro-based migration and package compatibility when migrating from Debian, Ubuntu, and Red Hat UBI base images.

### Installing PHP Extensions
Wolfi offers most of the built-in PHP extensions as optional packages installable via `apk`. Because PHP extensions are system-level packages, they require `apk` which is only available in our **builder** images. The following extensions are already included within all variants:

- `php-mbstring`
- `php-curl`
- `php-openssl`
- `php-iconv`
- `php-mbstring`
- `php-mysqlnd`
- `php-pdo`
- `php-pdo_sqlite`
- `php-pdo_mysql`
- `php-sodium`
- `php-phar`


To check for available extensions, you can run a temporary container based on the `php:latest-dev` image:

```shell
docker run -it --rm --entrypoint /bin/sh --user root cgr.dev/chainguard/php:latest-dev
```

Make sure to update the package manager cache:

```shell
apk update
```
If you want to search for PHP 8.2 XML extensions, for example, you can run the following:

```shell
apk search php*8.2*xml*
```
And this should give you a list of all PHP 8.2 XML extensions available in Wolfi. For more searching tips, check the [Searching for Packages](/chainguard/migration-guides/migrating-to-chainguard-images/#searching-for-packages) section of our base migration guide.

## Migrating PHP CLI workloads to use Chainguard Images
Our `latest` and `latest-dev` PHP image variants are designed to run CLI applications and scripts that don't need a web server. As a first step towards migration, you might want to change your base image to the `latest-dev` variant, since that would be the closest option for a drop-in base image replacement. Once you have your dependencies and steps dialed in, you can optionally migrate to a multi stage build to create a strict runtime containing only what the application needs to run.

The following `Dockerfile` uses the `php:latest-dev` image to build the application, which in this case means copying the application files and installing dependencies via `composer`. A second build stage copies the application to a final distroless image based on `php:latest`.

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

ENTRYPOINT [ "php", "/app/myscript.php" ]
```

Our [PHP Getting Started](/chainguard/chainguard-images/getting-started/php/) guide has step-by-step instructions on how to build and run a PHP CLI application with Chainguard Images.

## Migrating PHP Web applications to use Chainguard Images
For PHP web applications that serve content through a web server, you should use the `latest-fpm` and `latest-fpm-dev` variants of our PHP image. Combine it with our [Nginx image](/chainguard/chainguard-images/reference/nginx) and an optional database for a traditional LEMP setup.

The overall migration process is essentially the same as described in the previous section, with the difference that you won't set up application entry points, since these images run as services. Your Dockerfile may require additional steps to set up front end dependencies, initialize databases, and perform any additional tasks needed for the application to run through a web server.

You can use [Docker Compose](https://docs.docker.com/compose/) to create a LEMP environment and test your setup locally. The following `docker-compose.yaml` file creates a local environment to serve a PHP web application using our PHP-FPM, Nginx, and MariaDB images:

```yaml
version: "3.7"
services:
  app:
    image: cgr.dev/chainguard/php:latest-fpm-dev
    restart: unless-stopped
    working_dir: /app
    volumes:
      - ./app:/app
    networks:
      - wolfi

  nginx:
    image: cgr.dev/chainguard/nginx
    restart: unless-stopped
    ports:
      - 8000:8080
    volumes:
      - ./app:/app
      - ./nginx.conf:/etc/nginx/nginx.conf
    networks:
      - wolfi

  mariadb:
    image: cgr.dev/chainguard/mariadb
    restart: unless-stopped
    environment:
      MARIADB_ALLOW_EMPTY_ROOT_PASSWORD: 1
      MARIADB_USER: laravel
      MARIADB_PASSWORD: password
      MARIADB_DATABASE: php-test
    ports:
      - 3306:3306
    networks:
      - wolfi

networks:
  wolfi:
    driver: bridge

```

Notice that the environment creates a few shared volumes to share the application files and also the `nginx.conf` file with the specific web server configuration. You'll need that to tell Nginx to redirect `.php` requests to the `php-fpm` service.

An example `nginx.conf` file to handle PHP requests with default settings:

```yaml
pid /var/run/nginx.pid;

events {
  worker_connections  1024;
}

http {
    server {
        listen 8080;
        index index.php index.html;
        root /app/laravel-demo/public;
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

## Additional Resources

Our [PHP image documentation](/chainguard/chainguard-images/reference/php/) covers details about all PHP image variants, including the list of available tags for both development and production images. For another example of LEMP setup using MariaDB, check our [Getting Started with the MariaDB Chainguard Image](https://edu.chainguard.dev/chainguard/chainguard-images/getting-started/mariadb/).

The [Debugging Distroless](/chainguard/chainguard-images/debugging-distroless-images/) guide contains important information for debugging issues with distroless images. Check also the [Verifying Images](/chainguard/chainguard-images/verifying-chainguard-images-and-metadata-signatures-with-cosign/) resource for details around provenance, SBOMs, and image signatures.
