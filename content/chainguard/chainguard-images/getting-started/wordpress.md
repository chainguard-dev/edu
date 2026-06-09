---
title: "Getting Started with the WordPress Chainguard Container"
type: "article"
linktitle: "WordPress"
description: "Learn how to deploy WordPress using Chainguard's security-hardened container image with reduced vulnerabilities and distroless runtime options"
date: 2024-07-19T11:07:52+02:00
lastmod: 2025-07-23T15:09:59+00:00
tags: ["Chainguard Containers"]
draft: false
images: []
menu:
  docs:
    parent: "getting-started"
weight: 70
toc: true
---

Chainguard's [WordPress container image](https://images.chainguard.dev/directory/image/wordpress/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-getting-started-wordpress) is a drop-in replacement for the official [WordPress FPM-Alpine image](https://hub.docker.com/_/wordpress), with significantly fewer vulnerabilities than the standard image. It includes a [distroless](/chainguard/chainguard-images/getting-started-distroless/) variant for production use that removes shells, package managers, and other unnecessary components. The image ships with the latest PHP and WordPress versions and all required PHP extensions.

This guide covers three ways to use the WordPress Chainguard Container to build and run WordPress projects.

{{< details "What is distroless?" >}}
{{< blurb/distroless >}}
{{< /details >}}

{{< details "What is Wolfi?" >}}
{{< blurb/wolfi >}}
{{< /details >}}

{{< details "What are multi-stage builds?" >}}
{{< blurb/multistage >}}
{{< /details >}}

{{< details "Chainguard Containers" >}}
{{< blurb/images >}}
{{< /details >}}

## Preparation
This guide requires Docker. Download and install it from the [official Docker website](https://docs.docker.com/get-docker/) if you don't have it.

The images in this guide require a free Chainguard account. Sign up at [chainguard.dev](https://www.chainguard.dev/) if you don't have one, then authenticate:

```shell
chainctl auth login
```

If you encounter credential errors when pulling images, pull them individually before running `docker compose`:

```shell
docker pull cgr.dev/chainguard/wordpress:latest-dev
docker pull cgr.dev/chainguard/wordpress:latest
docker pull cgr.dev/chainguard/mariadb
docker pull cgr.dev/chainguard/nginx
```

### Clone the demos repository
Clone the demos repository to your local machine:

```shell
git clone git@github.com:chainguard-dev/edu-images-demos.git
```

Navigate to the `wordpress` demo directory:

```shell
cd edu-images-demos/php/wordpress
```

You'll find three directories, one for each example in this guide.

## Example 1: Testing the container image with a fresh WordPress install
The `latest-dev` variant of the Chainguard WordPress Container lets you run a fresh WordPress installation and explore the setup wizard. Changes you make won't persist after you stop the environment — the next example shows how to persist customizations using a volume.

The files for this example are in the `01-preview` directory. Open `docker-compose.yml` in your editor to follow along.

This example includes a `Dockerfile` that copies WordPress source files into the document root and sets ownership at build time:

```Dockerfile
FROM cgr.dev/chainguard/wordpress:latest-dev
USER root
RUN cp -r /usr/src/wordpress/. /var/www/html/ && \
    cp /var/www/html/wp-config-docker.php /var/www/html/wp-config.php && \
    chown -R php:php /var/www/html
USER php
```

The `docker-compose.yml` for this example:

```yaml
services:
  app:
    build: .
    image: wordpress-preview
    restart: unless-stopped
    environment:
      WORDPRESS_DB_HOST: mariadb
      WORDPRESS_DB_USER: $WORDPRESS_DB_USER
      WORDPRESS_DB_PASSWORD: $WORDPRESS_DB_PASSWORD
      WORDPRESS_DB_NAME: $WORDPRESS_DB_NAME
    volumes:
      - document-root:/var/www/html

  nginx:
    image: cgr.dev/chainguard/nginx
    restart: unless-stopped
    ports:
      - 8000:8080
    volumes:
      - document-root:/var/www/html
      - ./nginx.conf:/etc/nginx/nginx.conf

  mariadb:
    image: cgr.dev/chainguard/mariadb
    restart: unless-stopped
    environment:
      MARIADB_ALLOW_EMPTY_ROOT_PASSWORD: 1
      MARIADB_USER: $WORDPRESS_DB_USER
      MARIADB_PASSWORD: $WORDPRESS_DB_PASSWORD
      MARIADB_DATABASE: $WORDPRESS_DB_NAME
    ports:
      - 3306:3306

volumes:
  document-root:
```

This Docker Compose file defines three services: `app`, `nginx`, and `mariadb`:

- The `app` service builds a local image using the included `Dockerfile`, which copies WordPress source files from `/usr/src/wordpress` into the document root and renames `wp-config-docker.php` to `wp-config.php`. That config file reads database credentials from environment variables at runtime. The `document-root` volume is shared between `app` and `nginx`.
- The `nginx` service uses the [Chainguard nginx Container](https://images.chainguard.dev/directory/image/nginx/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-getting-started-wordpress), configured to serve the WordPress application on port 8000.
- The `mariadb` service uses the [Chainguard MariaDB Container](https://images.chainguard.dev/directory/image/mariadb/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-getting-started-wordpress), configured with the environment variables needed to create the WordPress database.

The environment variables are stored in a `.env` file in the same directory. To view them, run:

```bash
cat .env
```

```ini
WORDPRESS_DB_HOST=mariadb
WORDPRESS_DB_USER=wp-user
WORDPRESS_DB_PASSWORD=wp-password
WORDPRESS_DB_NAME=wordpress
```

You can change these values as needed. The `.env` file is hidden and won't appear in most file explorers, but you can open it in any terminal text editor.

Build the image and start the services:

```bash
docker compose up --build
```

Open `http://localhost:8000` in your browser to reach the WordPress installation page. Follow the on-screen instructions to complete setup. Any customizations will be lost when you stop the environment.

To stop the services, press `CTRL+C` in the terminal, then run:

```bash
docker compose down
```

This removes the containers and networks. The next example shows how to mount a volume so that customizations like themes and plugins persist.

## Example 2: Customizing a new WordPress installation
To keep customizations — themes, plugins, and other changes — between container rebuilds, you need a volume with the correct permissions. This requires a user inside the container with the same UID as your host user. This example uses a custom Dockerfile to add a `wordpress` user with a configurable UID (defaulting to `1000`, the typical UID for a non-root user on Linux) and sets ownership of the document root accordingly.

Navigate to `02-customizing` to follow along. Here's the Dockerfile:

```Dockerfile
FROM cgr.dev/chainguard/wordpress:latest-dev
ARG UID=1000

USER root
RUN cp -r /usr/src/wordpress/. /var/www/html/ && \
    cp /var/www/html/wp-config-docker.php /var/www/html/wp-config.php && \
    cp -r /usr/src/wordpress/wp-content /usr/src/wp-content-default
RUN addgroup wordpress && adduser -SD -u "$UID" -s /bin/bash wordpress wordpress
RUN chown -R wordpress:wordpress /var/www/html /usr/src/wp-content-default

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

USER wordpress
ENTRYPOINT ["/docker-entrypoint.sh"]
```

In addition to creating the `wordpress` user, the Dockerfile copies WordPress source files into the document root at build time and saves a copy of the default `wp-content` directory to `/usr/src/wp-content-default`. A custom entrypoint script uses that copy to populate the host-mounted `wp-content` directory on first run if it doesn't yet contain a `themes` subdirectory:

```bash
#!/bin/sh
# Populate wp-content from defaults on first run (when themes directory is absent)
if [ ! -d /var/www/html/wp-content/themes ]; then
    cp -r /usr/src/wp-content-default/. /var/www/html/wp-content/
fi
exec php-fpm
```

The `docker-compose.yml` file references the custom Dockerfile and accepts a UID build argument:

```yaml
services:
  app:
    image: wordpress-local-dev
    build:
      context: .
      dockerfile: Dockerfile
      args:
        UID: 1000
    user: wordpress
    restart: unless-stopped
    environment:
      WORDPRESS_DB_HOST: mariadb
      WORDPRESS_DB_USER: $WORDPRESS_DB_USER
      WORDPRESS_DB_PASSWORD: $WORDPRESS_DB_PASSWORD
      WORDPRESS_DB_NAME: $WORDPRESS_DB_NAME
    volumes:
      - ./wp-content:/var/www/html/wp-content
      - document-root:/var/www/html

  nginx:
    image: cgr.dev/chainguard/nginx
    restart: unless-stopped
    ports:
      - 8000:8080
    volumes:
      - document-root:/var/www/html
      - ./nginx.conf:/etc/nginx/nginx.conf

  mariadb:
    image: cgr.dev/chainguard/mariadb
    restart: unless-stopped
    environment:
      MARIADB_ALLOW_EMPTY_ROOT_PASSWORD: 1
      MARIADB_USER: $WORDPRESS_DB_USER
      MARIADB_PASSWORD: $WORDPRESS_DB_PASSWORD
      MARIADB_DATABASE: $WORDPRESS_DB_NAME
    ports:
      - 3306:3306

volumes:
  document-root:
```

Only the `app` service differs from the previous example. The `build` section references the custom Dockerfile and sets `UID` to `1000` by default; pass your own UID at build time to match your host user. The bind mount at `./wp-content` persists the WordPress content directory to the host.

Build the image, passing your UID as a build argument:

```shell
docker compose build --build-arg UID=$(id -u) app
```

Once the build completes, start the services:

```shell
docker compose up
```

Open `http://localhost:8000` in your browser to access the WordPress installation.

In a separate terminal, check that the `wp-content` directory was populated with the default WordPress themes and plugins:

```shell
❯ ls -la wp-content
total 24
drwxrwxr-x  4 erika erika 4096 Jul 18 21:16 .
drwxrwxr-x  3 erika erika 4096 Jul 18 21:15 ..
-rw-rw-r--  1 erika erika   14 Jul 18 21:05 .gitignore
-rw-r--r--  1 erika 65533   28 Jan  1  1970 index.php
drwxr-xr-x  2 erika 65533 4096 Jul 18 21:16 plugins
drwxr-xr-x 16 erika 65533 4096 Jul 18 21:16 themes
```

The matching UID between the container's `wordpress` user and your host user is what allows files written by the container to be owned by your host account.

Any themes and plugins you install now persist between container rebuilds.

To stop the services, press `CTRL+C` in the terminal, then run:

```bash
docker compose down
```

The next example shows how to build a distroless WordPress image for production.

## Example 3: Using the distroless variant of the WordPress container image
This example uses a multi-stage Docker build to produce a distroless image with a smaller attack surface. The distroless image includes only the dependencies needed to run WordPress, without a shell or package manager.

The key difference from the previous examples is that all WordPress files — including any customizations in `wp-content` — are baked into the image at build time rather than populated at runtime. This makes the image self-contained: it doesn't rely on init steps or host volumes. Adding custom content at build time increases the final image size, but prevents filesystem changes once the container is running.

To demonstrate custom content, this example includes the [Cue](https://wordpress.org/themes/cue/) blogging theme and the [Imsanity](https://wordpress.org/plugins/imsanity/) image-resizing plugin.

Navigate to `03-distroless` to follow along. Here's the Dockerfile:

```Dockerfile
FROM cgr.dev/chainguard/wordpress:latest-dev AS builder

#copy wp-content folder
COPY ./wp-content /usr/src/wordpress/wp-content

USER root
#copy WordPress source to document root and set up config
RUN cp -r /usr/src/wordpress/. /var/www/html/ && \
    cp /var/www/html/wp-config-docker.php /var/www/html/wp-config.php

FROM cgr.dev/chainguard/wordpress:latest

COPY --from=builder --chown=php:php /var/www/html /var/www/html
```

The `COPY` instruction places your local `wp-content` into `/usr/src/wordpress/wp-content` before the `RUN` step merges it with the rest of the WordPress source. `USER root` is required because the WordPress source directory in this image is only readable by root. The `RUN` command copies everything to `/var/www/html` and renames `wp-config-docker.php` to `wp-config.php`, which reads database credentials from environment variables at runtime. The final stage copies the populated document root into the distroless image with `php:php` ownership.

The `docker-compose.yml` file references the custom Dockerfile:

```yaml
services:
  app:
    image: wordpress-local-distroless
    build:
      context: .
      dockerfile: Dockerfile
    restart: unless-stopped
    environment:
      WORDPRESS_DB_HOST: mariadb
      WORDPRESS_DB_USER: $WORDPRESS_DB_USER
      WORDPRESS_DB_PASSWORD: $WORDPRESS_DB_PASSWORD
      WORDPRESS_DB_NAME: $WORDPRESS_DB_NAME
      WORDPRESS_CONFIG_EXTRA: |
        # Disable plugin and theme update and installation
        define( 'DISALLOW_FILE_MODS', true );
        # Disable automatic updates
        define( 'AUTOMATIC_UPDATER_DISABLED', true );
    volumes:
      - document-root:/var/www/html

  nginx:
    image: cgr.dev/chainguard/nginx
    restart: unless-stopped
    ports:
      - 8000:8080
    volumes:
      - document-root:/var/www/html
      - ./nginx.conf:/etc/nginx/nginx.conf

  mariadb:
    image: cgr.dev/chainguard/mariadb
    restart: unless-stopped
    environment:
      MARIADB_ALLOW_EMPTY_ROOT_PASSWORD: 1
      MARIADB_USER: $WORDPRESS_DB_USER
      MARIADB_PASSWORD: $WORDPRESS_DB_PASSWORD
      MARIADB_DATABASE: $WORDPRESS_DB_NAME
    ports:
      - 3306:3306

volumes:
  document-root:

```

Build and start the environment:

```shell
docker compose up --build
```

This WordPress setup behaves like the previous examples, but the image is self-contained — it requires no host volumes and allows no new package installations or shell access. The `WORDPRESS_CONFIG_EXTRA` environment variable disables theme and plugin installation and automatic updates, preventing filesystem changes inside the running container.

To stop the services, press `CTRL+C` in the terminal, then run:

```bash
docker compose down
```

To keep your WordPress installation up to date, use [digestabot](https://edu.chainguard.dev/chainguard/chainguard-images/videos/digestabot/), a GitHub Action that works like Dependabot — it sends a pull request to your repository whenever a new version of a container image is available, ensuring you're always running the latest WordPress version from Wolfi.

## Advanced Usage

{{< blurb/images-advanced image="WordPress" >}}
