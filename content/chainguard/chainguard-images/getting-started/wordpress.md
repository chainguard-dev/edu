---
title: "Getting Started with the WordPress Chainguard Image"
type: "article"
linktitle: "WordPress"
description: "Tutorial on how to get started with the WordPress Chainguard Image"
date: 2024-07-19T11:07:52+02:00
lastmod: 2024-07-19T11:07:52+02:00
tags: ["Chainguard Images", "Products"]
draft: false
images: []
menu:
  docs:
    parent: "getting-started"
weight: 70
toc: true
---

The [WordPress](https://images.chainguard.dev/directory/image/wordpress/overview) Chainguard Image is a container image suitable for creating and running WordPress projects. Designed to work as a drop-in replacement for the official [WordPress FPM-Alpine image](https://hub.docker.com/_/wordpress), the Chainguard WordPress Image features a [distroless](/chainguard/chainguard-images/getting-started-distroless/) variant for increased security on production environments. The image is built with the latest PHP and WordPress versions, and includes the necessary PHP extensions to run WordPress.

In this guide, we'll demonstrate 3 different ways in which you can use the WordPress Chainguard Image to build and run WordPress projects.

## Preparation
This tutorial requires Docker to be installed on your local machine. If you don't have Docker installed, you can download and install it from the [official Docker website](https://docs.docker.com/get-docker/).

### Cloning the Demos Repository
Start by cloning the demos repository to your local machine:

```shell
git clone git@github.com:chainguard-dev/edu-images-demos.git
```

Locate the `wordpress` demo and cd into its directory:

```shell
cd edu-images-demos/php/wordpress
```

Here you will find three folders, each with a different demo that we'll cover in this guide.

## Example 1: Testing the Image with a Fresh WordPress Install
You can use the `latest-dev` variant of the Chainguard WordPress Image to create a project from scratch and go through the installation wizard. This method is useful for testing the image and getting familiar with its features, however, changes made to the WordPress installation will not persist unless you set up a volume with proper permissions to share container contents with the host machine. We'll see how to do that in the next example.

The files for this demo are located in the `01-preview` directory. You can access this directory and open the `docker-compose.yaml` file in your editor of choice to follow along.

Here's the content of the `docker-compose.yaml` file from our first demo:

```yaml
services:
  app:
    image: cgr.dev/chainguard/wordpress:latest-dev
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

In this Docker Compose example, we define 3 services: `app`, `nginx`, and `mariadb`. Here's a breakdown of each service:

- The `app` service uses the `latest-dev` variant of the Chainguard WordPress Image, and is configured to connect to the `mariadb` service. The entrypoint script in the WordPress image looks for environment variables to set up a custom `wp-config.php` file. The volume `document-root` defines a volume that will be shared between the `app` and the `nginx` services.
- The `nginx` service uses the [Chainguard nginx Image](https://images.chainguard.dev/directory/image/nginx/overview), and is configured to serve the WordPress application on port 8000.
- The `mariadb` service uses the [Chainguard MariaDB Image](https://images.chainguard.dev/directory/image/mariadb/overview), and is configured with the necessary environment variables to create a database for the WordPress application.

The environment variables used in this example are defined in a `.env` file located in the same directory as the `docker-compose.yaml` file. To check for its contents, run:

```bash
cat .env
```

```ini
WORDPRESS_DB_HOST=mariadb
WORDPRESS_DB_USER=wp-user
WORDPRESS_DB_PASSWORD=wp-password
WORDPRESS_DB_NAME=wordpress
```

Although not necessary, you can change these values to suit your needs. Notice this is a hidden file and might not be visible in your file explorer, but you can open it in your terminal using a text editor like `nano` or `vim`.

To start the services, run:

```bash
docker compose up
```

If you navigate to `http://localhost:8000` in your browser, you should access the WordPress installation page. Follow the on-screen instructions to complete the WordPress setup. Keep in mind that any customizations will be lost once the environment is turned down.

To stop the services, type `CTRL+C` in the terminal where the services are running, and then run:

```bash
docker compose down
```

This will remove the containers and networks created by the `docker compose up` command. In the next example, we'll demonstrate how you can set up a volume with proper permissions to be able to persist customizations such as themes and plugins.

## Example 2: Customizing a New WordPress Installation
To persist customizations made to your WordPress site, such as the installation of new themes and plugins, you'll need to set up a volume with proper permissions in order to keep data between container rebuilds. This requires having a system user in the container with the same UID as your local system user on the host machine. To set this up, we'll create a custom Dockerfile that adds a `wordpress` user with the specified UID (set to `1000` by default, which is typically the UID of a regular user on Linux-based systems) to the `latest-dev` variant of the Chainguard WordPress Image. The Dockerfile also changes default permissions on the `/var/www/html` directory to allow the `wordpress` user to write to it.

Navigate to the `02-customizing` directory to follow along. This is how the described Dockerfile included in this directory looks:

```Dockerfile
FROM cgr.dev/chainguard/wordpress:latest-dev
ARG UID=1000

USER root
RUN addgroup wordpress && adduser -SD -u "$UID" -s /bin/bash wordpress wordpress
RUN chown -R wordpress:wordpress /var/www/html

USER wordpress
```

In the `docker-compose.yaml` file, we'll reference the custom Dockerfile and pass the UID as a build argument:

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

Only the `app` service has changed in this example. We've added a `build` section that references the custom Dockerfile, and we've set the `UID` build argument to `1000` by default. This can be overwritten at runtime when you call `docker compose up`. We've also added a volume share to persist the contents of the `wp-content` folder to the host machine.

To build your custom image and pass along your own UID as build argument, run:

```shell
docker compose build --build-arg UID=$(id -u) app
```

You should get output indicating that the image was successfully built. Now you can get your environment up with:

```shell
docker compose up
```

Once the environment is up and running, you can access your WordPress installation from your browser at `localhost:8000`.

If you go to another terminal window and check the contents of the `02-customizing/wp-content` folder, you'll notice that it was populated with the default WordPress themes and plugins:

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

This is only possible because of the custom Dockerfile we created, which added a `wordpress` user with the same UID as the local user on the host machine.

You can now install new themes and plugins, and they will persist between container rebuilds.

To stop the services, type `CTRL+C` in the terminal where the services are running, and then run:

```bash
docker compose down
```

In the next example, we'll see how you can create a distroless WordPress runtime for your production environment.

## Example 3: Using the Distroless Variant of the WordPress Image
This demo uses a multi-stage Docker build to create a final distroless image to improve overall security. The distroless image contains the necessary dependencies to run WordPress and won't allow for new package installations or shell access, reducing the image attack surface.

The main difference here is that we're calling the entrypoint script at **build time** instead of run time. This is done to ensure the image is self-contained and doesn't rely on volumes set up within the host machine in order to work. Any customizations should be included in the `wp-content` folder that will be copied to the image at build time. Although this increases final image size due to the inclusion of custom content at build time, it limits what can be changed or added to the image once it's built.

This demo includes a theme ([Cue](https://wordpress.org/themes/cue/), a simple blogging theme) and a plugin ([Imsanity](https://wordpress.org/plugins/imsanity/), a popular plugin used to resize images) to demonstrate how to include custom content in the image.

Navigate to the `03-distroless` directory to follow along. This is what the Dockerfile included in this directory looks like:

```Dockerfile
FROM cgr.dev/chainguard/wordpress:latest-dev as builder
#trigger wp-config.php creation
ENV WORDPRESS_DB_HOST=foo

#copy wp-content folder
COPY ./wp-content /usr/src/wordpress/wp-content

#run entrypoint script
RUN /usr/local/bin/docker-entrypoint.sh php-fpm --version

FROM cgr.dev/chainguard/wordpress:latest

COPY --from=builder --chown=php:php /var/www/html /var/www/html
```

Notice that we're copying the contents of the local `wp-content` folder to the `/usr/src/wordpress` folder in the container. This is the location of the WordPress source files. These will be copied to the document root by the entrypoint script that is executed right afterward. At the `builder` stage, we're also setting up a single environment variable to trigger the creation of the `wp-config.php` file that relies on a set of environment variables to configure database access.

In the `docker-compose.yaml` file, we reference the custom Dockerfile:

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

You can now build and run your environment with:

```shell
docker compose up --build
```

The behavior of this WordPress setup should be the same as in the previous examples, but this time, the image is self-contained and doesn't rely on volumes set up within the host machine to work, in addition to not allowing new package installations or login through a shell.

To stop the services, type `CTRL+C` in the terminal where the services are running, and then run:

```bash
docker compose down
```
Please notice that although this setup allows for customizations through the WordPress dashboard, changes won't be persisted through container rebuilds.

## Advanced Usage

{{< blurb/images-advanced image="WordPress" >}}
