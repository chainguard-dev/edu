---
title: "Getting Started with the PostgreSQL Chainguard Image"
type: "article"
linktitle: "PostgreSQL"
aliases: 
- /chainguard/chainguard-images/getting-started/getting-started-postgres
description: "Tutorial on how to get started with the PostgreSQL Chainguard Image"
date: 2023-08-10T11:07:52+02:00
lastmod: 2023-09-22T11:07:52+02:00
tags: ["Chainguard Images", "Products"]
draft: false
images: []
menu:
  docs:
    parent: "getting-started"
weight: 610
toc: true
---

PostgreSQL — commonly known as "Postgres" — is a popular open-source relational database. The PostgreSQL Images based on Wolfi and maintained by Chainguard provide distroless Images that are suitable for building and running PostgreSQL workloads.

Because Chainguard Images (including the PostgreSQL image) are rebuilt daily with the latest sources and include the absolute minimum of dependencies, they have significantly fewer vulnerabilities than equivalent images, typically zero. This means you can use the Chainguard PostgreSQL Image to run Postgres databases in containerized environments with a smaller footprint and greater security.

In order to illustrate how the PostgreSQL Chainguard Image might be used in practice, this tutorial involves setting up an example PHP application that uses a Postgres database. This guide assumes you have Docker installed to run the demo; specifically, the procedure outlined in this guide uses [Docker Compose](https://docs.docker.com/compose/install/) to manage the environment on your local machine.

{{< details "What is distroless" >}}
{{< blurb/distroless >}}
{{< /details >}}

{{< details "What is Wolfi" >}}
{{< blurb/wolfi >}}
{{< /details >}}

{{< details "Chainguard Images" >}}
{{< blurb/images >}}
{{< /details >}}


## Step 1: Setting up a demo application

This step involves downloading the demo application code to your local machine. To ensure that the application files don't remain on your system navigate to a temporary directory like `/tmp/`.

```sh
cd /tmp/
```

Your system will automatically delete the `/tmp/` directory's contents the next time it shuts down or reboots.

The code that comprises this demo application is hosted in a public GitHub repository managed by Chainguard. Pull down the example application files from GitHub with the following command.

```sh
git clone --sparse https://github.com/chainguard-dev/edu-images-demos.git
```

Because this guide's demo application code is stored in a repository with other examples, we don't need to pull down every file from this repository. For this reason, this command includes the `--sparse` option. This will initialize a sparse-checkout file; this causes the working directory to contain only the files in the root of the repository until the sparse-checkout configuration is modified.

Navigate into this new directory.

```sh
cd edu-images-demos
```

To retrieve the files you need for this tutorial's sample application, run the following `git` command.

```sh
git sparse-checkout set postgres
```

This modifies the sparse-checkout configuration initialized in the previous `git clone` command so that the checkout only consists of the repo's `postgres` directory.

Navigate into this new directory.

```sh
cd postgres/
```

From here, you can run the application and use a web browser to observe it working in real time, which we'll do in the next section.


## Step 2: Inspect, run, and test the sample application

We encourage you to check out [the application code on GitHub](https://github.com/chainguard-dev/edu-images-demos/tree/main/postgres) to better understand how this application works, but we'll provide a brief overview here.

This demo creates a LEPP (Linux, (E)NGINX, PostgreSQL and PHP-FPM) environment based on Wolfi Chainguard Images. We will use Docker Compose to bring up the environment, which will spin up three containers: an `app` container, a `postgres` container, and an `nginx` container. These will run as services.

Once the environment is up, you can visit the demo in your web browser. The `index.php` file contains code that does the following:

* Connects to the PostgreSQL server running in the `postgres` container
* Creates a new table named `data` if it doesn't already exist
* Inserts a new entry into the table with a random number
* Queries the table to show all the entries

Every time you reload the page, a new entry will be added to the table.

Note that this application includes a Dockerfile.

```sh
cat Dockerfile
```
```
FROM cgr.dev/chainguard/php:latest-fpm-dev

USER root
RUN apk update && apk add php-pgsql

USER php
```

This Dockerfile takes the public `php:latest-fpm-dev` Chainguard Image and installs the `php-pgsql` package onto it. This image comes with drivers that allow PHP applications to connect to MySQL or MariaDB databases by default but it doesn't have an equivalent for PostgreSQL. For this reason, we use this Dockerfile to install this package in order for the PHP application to be able to connect to the Postgres database.

Execute the following command to build an image with this Dockerfile, and then create and start each of the three containers and bring up the application.

```sh
docker compose up -d
```

The `-d` option is short for `--detach`; this will cause the containers to run in the background, allowing you to continue using the same terminal window. If you run into permissions issues when running this command, try running it again with `sudo` privileges.

> **Note**: If at any point you'd like to stop and remove these containers, run `docker compose down`.

Once all the containers have started, you'll be able to visit the application and observe it working. Open up your preferred web browser and navigate to `localhost:8000`. There, you'll be presented with text like the following

![Screenshot showing a Firefox web browser window with "localhost:8000" in the address bar. On the page is the following text: "Array ( [data_key] => code [data_value] => 8404 )"](pg-demo-success-1.png)

Every time you refresh your browser, a new entry will appear.

![Screenshot showing a Firefox web browser window with "localhost:8000" in the address bar. On the page is the following text: "Array ( [data_key] => code [data_value] => 8404 ), Array ( [data_key] => code [data_value] => 5124 ) Array ( [data_key] => code [data_value] => 1527 )". This indicates that the page was refreshed twice since the previous screenshot.](pg-demo-success-2.png)

This shows that the application is recording each visit in the PostgreSQL database and that the application is working correctly.

After confirming that the application is functioning as expected, you can read through the next section to explore how else you can work with the `postgres` container.


## Step 3: Working with the database

The `docker-compose.yml` file contains some configuration details regarding the PostgreSQL database used in this example application. Run the following command to inspect the contents of this file.

```sh
cat docker-compose.yml
```

We're interested in the `postgres` service:

```
. . .

  postgres:
	image: cgr.dev/chainguard/postgres
	restart: unless-stopped
	environment:
  	POSTGRES_USER: php
  	POSTGRES_PASSWORD: password
  	POSTGRES_DB: php-test
	ports:
  	- 5432:5432
	networks:
  	- wolfi

. . .
```

This section defines a few environment variables relating to the database used in the example application. Importantly, they specify that the application database is named `php-test` and runs under a user named `php` with the password "password". Using this information, you can connect to the `php-test` database running in the container with a command like the following.

```sh
docker exec -it postgres-postgres-1 \
psql -p 5432 -U php -W -d php-test
```

`docker exec` allows you to execute commands within a running container. The `-i` argument allows you to execute an interactive command while the `-t` option allocates a pseudo-TTY to the process within the container. Because our goal is to access the sample database through the `psql` command line client, these options are necessary. Next, enter the name of the container running the PostgreSQL database; by default, this will be named `postgres-postgres-1`.

Following that, the remainder of this command represents the command that will be run within the container. Here, we run the `psql` command to access the database specifying that we want to connect over port `5432` as the `php` user. The `-W` option indicates that we want to be prompted to enter the password interactively, and `-d php-test` specifies that we want to connect to the `php-test` database.

```
Password:
```

Enter `password` and you'll then be presented with the `psql` command prompt.

```
psql (15.3)
Type "help" for help.

php-test=#
```

From here, you can interact with the database from within the `postgres-postgres-1` container as you would with any other PostgreSQL database. For example, you could update existing tables, create new ones, and insert or delete data.

To close the `psql` prompt, you can enter the following command.

```PostgreSQL
\q
```

Of course, you likely won't be regularly managing your containerized databases over the command line. The purpose of this section is to only show that you can interact with the database running in this container just like you would with any other Postgres database.

## Advanced Usage

{{< blurb/images-advanced image="PostgreSQL" >}}
