---
title: "Getting Started with the Laravel Chainguard Container"
type: "article"
linktitle: "Laravel"
description: "Tutorial on how to get started with the Chainguard Laravel container image"
date: 2024-05-17T11:07:52+02:00
lastmod: 2025-03-24T11:07:52+02:00
tags: ["Chainguard Containers", "Products"]
draft: false
images: []
menu:
  docs:
    parent: "getting-started"
weight: 020
toc: true
---

The [Laravel Chainguard Container](https://images.chainguard.dev/directory/image/laravel/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-getting-started-laravel) is a container image that has the tooling necessary to develop, build, and execute [Laravel](https://laravel.com) applications, including required extensions. Laravel is a full-stack PHP framework that enables developers to build complex applications using modern tools and techniques that help streamline the development process.

In this guide, we'll set up a demo and demonstrate how you can use Chainguard Containers to develop, build, and run Laravel applications.

This tutorial requires Docker to be installed on your local machine. If you don't have Docker installed, you can download and install it from the [official Docker website](https://docs.docker.com/get-docker/).

## 1. Setting Up a Demo Application

We'll start by getting the demo application ready. The demo is called **OctoFacts**, and it shows a random fact about Octopuses alongside a random Octopus image each time the page is reloaded. Quotes are loaded from a `.txt` file into the database through a database migration.

By default, the application uses an [SQLite](https://www.sqlite.org/) database. This allows us to test the application with the built-in web server provided by the `artisan serve` command, without having to set up a full PHP development environment first. In the next step, we'll configure a multi-node environment using Docker Compose to demonstrate a typical LEMP (Linux, (E)Nginx, MariaDB, and PHP) environment using Chainguard Containers.

Start by cloning the demos repository to your local machine:

```shell
git clone git@github.com:chainguard-dev/edu-images-demos.git
```

Locate the `octo-facts` demo and cd into its directory:

```shell
cd edu-images-demos/php/octo-facts
```

The demo includes a `.env.dev` file with the app's configuration for development. You should create a copy of this file and save it as `.env`, so that the application can load default settings:

```shell
cp .env.dev .env
```

You can now use the builder Laravel container image to install dependencies via Composer. Notice that we're using the **laravel** system user in order to be able to write to the shared folder without issues:

```shell
docker run --rm -v ${PWD}:/app --entrypoint composer --user laravel \
    cgr.dev/chainguard/laravel:latest-dev \
    install
```

You can now run the database migrations and seed the database with sample data. This will populate a `.sqlite` database with facts obtained from the `octofacts.txt` file in the root of the application.

```shell
docker run --rm -v ${PWD}:/app --entrypoint php --user laravel \
    cgr.dev/chainguard/laravel:latest-dev \
    /app/artisan migrate --seed
```

Next, run `npm install` to install Node dependencies. You can use the `node:latest-dev` container image for that, but you'll need to use the **root** container user in order to be able to write to the shared folder using this image:

```shell
docker run --rm -v ${PWD}:/app --entrypoint npm --user root \
    cgr.dev/chainguard/node:latest-dev \
    install
```
Then, fix permissions on node modules with:

```shell
sudo chown -R ${USER} node_modules/
```
The next step is to build front end assets. You can use the `npm run build` command for that. Like with `npm install`, you'll need to set the container user to **root**.

```shell
docker run --rm -v ${PWD}:/app --entrypoint npm --user root \
    cgr.dev/chainguard/node:latest-dev \
    run build
```

Fix permissions on the public folder:

```shell
sudo chown -R ${USER} public/
```

The application is all set. Next, run the built-in web server with:

```shell
docker run -p 8000:8000 --rm -it -v ${PWD}:/app \
  --entrypoint /app/artisan --user laravel \
  cgr.dev/chainguard/laravel:latest-dev serve --host=0.0.0.0
```

This command will create a port redirect that allows you to access the built-in web server running in the container. It uses a volume share for the application files, and sets the entrypoint to the `artisan serve` command.

You should now be able to access the application from your browser at `localhost:8000`. You'll get a page similar to this:

![Preview of the OctoFacts demo Laravel application](https://github.com/chainguard-dev/edu-images-demos/raw/main/php/octo-facts/public/octofacts.png)

## 2. Creating a LEMP Environment with Docker Compose
To demonstrate a full LEMP setup using Chainguard Containers, we'll now set up a Docker Compose environment to serve the application via Nginx. This setup can be used as a more robust development environment that replicates a production setting based on secure container images.

The following `docker-compose.yaml` file is already included in the root of the application folder:

```yaml
services:
  app:
    image: cgr.dev/chainguard/laravel:latest-dev
    restart: unless-stopped
    working_dir: /app
    volumes:
      - .:/app
    networks:
      - wolfi

  nginx:
    image: cgr.dev/chainguard/nginx
    restart: unless-stopped
    ports:
      - 8000:8080
    volumes:
      - .:/app
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
      MARIADB_DATABASE: octofacts
    ports:
      - 3306:3306
    networks:
      - wolfi

networks:
  wolfi:
    driver: bridge
```

This `docker-compose.yaml` file defines 3 services to run the application (**app**, **nginx**, **mariadb**), using volumes to share the application files within the container and a configuration file for the Nginx server, which we'll showcase in a moment. Notice the database credentials within the `mariadb` service: these environment variables are used to set up the database. This is done automatically by the MariaDB container image entrypoint upon container initialization. We'll use these credentials to configure the new database within Laravel's `.env` file.

>Please note this Docker Compose setup is intended for local development only. For production environments, you should never keep sensitive data like database credentials in plain text. Check the [Docker Compose Documentation](https://docs.docker.com/compose/use-secrets/) for more information on how to handle sensitive data in Compose files.

The following `nginx.conf` file is also included within the root of the application folder. This file is based on the [recommended Nginx deployment configuration](https://laravel.com/docs/11.x/deployment#nginx) from official Laravel docs.

```nginx configuration
pid /var/run/nginx.pid;

events {
  worker_connections  1024;
}

http {
    server {
    listen 8080;
    root /app/public;

    add_header X-Frame-Options "SAMEORIGIN";
    add_header X-Content-Type-Options "nosniff";

    index index.php;

    charset utf-8;

    location / {
        include  /etc/nginx/mime.types;
        try_files $uri $uri/ /index.php?$query_string;
    }

    location = /favicon.ico { access_log off; log_not_found off; }
    location = /robots.txt  { access_log off; log_not_found off; }

    error_page 404 /index.php;

    location ~ \.php$ {
        try_files $uri =404;
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_pass app:9000;
        fastcgi_index index.php;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param PATH_INFO $fastcgi_path_info;
    }

    location ~ /\.(?!well-known).* {
        deny all;
    }
  }
}
```

This file sets up the document root to `app/public` and configures Nginx to redirect `.php` requests to the container running PHP-FPM (`app:9000`).

You can bring the environment up with:

```shell
docker compose up
```

This command will block your terminal and show live logs from each of the running services. With the MariaDB database up and running, you can now update Laravel's main `.env` file to change the database connection from **sqlite** to **mysql**.

Open the `.env` file in your editor of choice and locate the database settings. The `DB_CONNECTION` parameter is set to `sqlite`, you should change that to `mysql` and uncomment the remaining variables to reflect the settings from your `docker-compose.yaml` file. This is how the database section should look like when you're finished editing:

```ini
DB_CONNECTION=mysql
DB_HOST=mariadb
DB_PORT=3306
DB_DATABASE=octofacts
DB_USERNAME=laravel
DB_PASSWORD=password
```

Save and close the file. If you reload the application on your browser now, you should get a database error, because the database is empty. You'll need to re-run migrations and seed the database. To do that, you can run a `docker exec` command on the live container.

First, look for the container running the `app` service and copy its name.

```shell
docker compose ps
```
```shell
NAME                   IMAGE                                   COMMAND                  SERVICE   CREATED          STATUS          PORTS
octo-facts-app-1       cgr.dev/chainguard/laravel:latest-dev   "/bin/s6-svscan /sv"     app       11 seconds ago   Up 10 seconds
octo-facts-mariadb-1   cgr.dev/chainguard/mariadb              "/usr/local/bin/dock…"   mariadb   11 seconds ago   Up 10 seconds   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp
octo-facts-nginx-1     cgr.dev/chainguard/nginx                "/usr/sbin/nginx -c …"   nginx     11 seconds ago   Up 10 seconds   0.0.0.0:8000->8080/tcp, :::8000->8080/tcp
```
Then, you can run migrations like this:

```shell
docker exec octo-facts-app-1 php /app/artisan migrate --seed
```

You can use the same method to execute other Artisan commands while the environment is up. After running migrations and seeding the database, you should be able to reload the app from your browser at `localhost:8000` and get a new octopus fact.

## 3. Creating a Distroless Laravel Runtime for the Application
So far, we have been using the `laravel:latest-dev` builder image to run the application in a development setting. For production workloads, the recommended approach for additional security is to create a [distroless](/chainguard/chainguard-images/getting-started-distroless/) runtime for the application that will contain only what's absolutely necessary for running the app on production. This is done by combining a **build** phase in a **multi-stage** Dockerfile.

To demonstrate this approach, we'll now build a distroless container image and test it using the Docker Compose setup exemplified in the previous section.

The following Dockerfile is included within the root of the application:

```Dockerfile
FROM cgr.dev/chainguard/laravel:latest-dev AS builder
USER root
RUN apk update && apk add nodejs npm
COPY . /app
RUN cd /app && chown -R php.php /app
USER php
RUN composer install --no-progress --no-dev --prefer-dist
RUN npm install && npm run build

FROM cgr.dev/chainguard/laravel:latest
COPY --from=builder /app /app
```

This Dockerfile starts with a build stage that copies the application files to the container, installs Node and NPM, installs the application dependencies, and dumps front-end assets to the public folder. A second stage based on `laravel:latest` copies the application from the build stage to the final distroless image. It's important to notice that we don't run any database migrations here, because at build time the database might not be ready yet. In other production scenarios, you may be able to include the migration within the Dockerfile, as long as the database is already up and running.

The file `docker-compose-distroless.yaml` included within the root of the application folder has a few changes compared to the previous `docker-compose.yaml` file. The `app` service now uses the `octofacts` image, which is built from the Dockerfile referenced above. The `user: laravel` directive is also removed so commands run as the default **php** user. This is how the `app` service looks like in the new file:

```yaml
  app:
    image: octofacts
    build:
      context: .
    restart: unless-stopped
    working_dir: /app
    user: laravel
    volumes:
      - .:/app
    networks:
      - wolfi
...
```

If your environment is still running, you should stop it before proceeding. Hit `CTRL+C` and then run:

```shell
docker compose down
```
This will stop and remove all containers, networks, and volumes created by the previous `docker-compose.yaml` file. You can now bring the new environment up with:

```shell
docker compose -f docker-compose-distroless.yaml up
```

Once the environment is up and running, you can now run the database migrations with:

```shell
docker exec octo-facts-app-1  php /app/artisan migrate --seed
```

You should now be able to reload your browser and obtain a new octopus fact.

## Advanced Usage

{{< blurb/images-advanced image="Laravel" >}}
