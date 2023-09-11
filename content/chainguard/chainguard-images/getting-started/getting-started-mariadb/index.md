---
title: "Getting Started with the MariaDB Chainguard Image"
type: "article"
lead: "Tutorial on how to get started with the MariaDB Chainguard Image"
date: 2023-07-28T11:07:52+02:00
lastmod: 2023-08-10T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "getting-started"
weight: 610
toc: true
---

The MariaDB Image based on Wolfi and maintained by Chainguard provide a distroless container Image that is suitable for building and running MariaDB workloads.

Because Chainguard Images (including the MariaDB image) are rebuilt daily with the latest sources and include the absolute minimum of dependencies, they have significantly less vulnerabilities than equivalent images, typically zero. This means you can use the Chainguard MariaDB Image to run MariaDB databases in containerized environments with a smaller footprint and greater security.

In order to illustrate how the MariaDB Chainguard Image might be used in practice, this tutorial involves setting up an example PHP application that uses a MariaDB database. This guide assumes you have Docker installed to run the demo; specifically, the procedure outlined in this guide uses [Docker Compose](https://docs.docker.com/compose/install/) to manage the environment on your local machine.

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

Because this guide's demo application code is stored in a repository with other examples, we don't need to pull down every file from this repository. For this reason, this command includes the `--sparse` option. This will initialize a sparse-checkout file, causing the working directory to contain only the files in the root of the repository until the sparse-checkout configuration is modified.

Navigate into this new directory and list its contents to confirm this.

```sh
cd edu-images-demos/ && ls
```

For now, this directory will only contain the repository's `LICENSE` and `README` files.

```
LICENSE  README.md
```

To retrieve the files you need for this tutorial's sample application, run the following `git` command.

```sh
git sparse-checkout set mariadb
```

This modifies the sparse-checkout configuration initialized in the previous `git clone` command so that the checkout only consists of the repo's `mariadb` directory.

Navigate into this new directory.

```sh
cd mariadb/
```

From here, you can run the application and use a web browser to observe it working in real time, which we'll do in the next section.


## Step 2: Inspect, run, and test the sample application

We encourage you to check out [the application code on GitHub](https://github.com/chainguard-dev/edu-images-demos/tree/main/mariadb) to better understand how this application works, but we'll provide a brief overview here.

This demo creates a LEMP (Linux, (E)NGINX, MariaDB and PHP-FPM) environment based on Wolfi Chainguard Images. We will use Docker Compose to bring up the environment, which will spin up three containers: an `app` container, a `mariadb` container, and an `nginx` container. These will run as services.

Once the environment is up, you can visit the demo in your web browser. The `index.php` file contains code that does the following:

* Connects to the MariaDB server running in the `mariadb` container
* Creates a new table named `data` if it doesn't already exist
* Inserts a new entry into the table with a random number
* Queries the table to show all the entries

Every time you reload the page, a new entry will be added to the table.

Execute the following command to create and start each of the three containers and bring up the application.

```sh
docker compose up -d
```

The `-d` option is short for `--detach`; this will cause the containers to run in the background, allowing you to continue using the same terminal window. If you run into permissions issues when running this command, try running it again with `sudo` privileges.

> **Note**: If at any point you'd like to stop and remove these containers, run `docker compose down`.

Once all the containers have started, you'll be able to visit the application and observe it working. Open up your preferred web browser and navigate to `localhost:8000`. There, you'll be presented with text like the following.

![Screenshot showing a Firefox web browser window with "localhost:8000" in the address bar. On the page is the following text: "Array ( [data_key] => code [data_value] => 7064 )"](mdb-demo-success-1.png)

Every time you refresh your browser, a new entry will appear.

![Screenshot showing a Firefox web browser window with "localhost:8000" in the address bar. On the page is the following text: "Array ( [data_key] => code [data_value] => 7064 ), Array ( [data_key] => code [data_value] => 7006 ) Array ( [data_key] => code [data_value] => 7507 )". This indicates that the page was refreshed twice since the previous screenshot.](mdb-demo-success-2.png)

This shows that the application is recording each visit in the MariaDB database and that the application is working correctly.

After confirming that the application is functioning as expected, you can read through the next section to explore how else you can work with the `mariadb` container.


## Step 3: Working with the database

The `docker-compose.yml` file contains some configuration details regarding the MariaDB database used in this example application. Run the following command to inspect the contents of this file.

```sh
cat docker-compose.yml
```

We're interested in the `mariadb` service:

```
. . .

  mariadb:
	image: cgr.dev/chainguard/mariadb
	restart: unless-stopped
	environment:
  	MARIADB_ALLOW_EMPTY_ROOT_PASSWORD: 1
  	MARIADB_USER: php
  	MARIADB_PASSWORD: password
  	MARIADB_DATABASE: php-test
	ports:
  	- 3306:3306
	volumes:
  	- ./:/app
	networks:
  	- wolfi

. . .
```

This section defines a few environment variables relating to the database used in the example application. Importantly, they specify that the application database runs under a user named `php` with the password "password". Using this information, you can connect to the `php` database running in the container with a command like the following.

```sh
docker exec -it mariadb-mariadb-1 mariadb --user php -p
```

`docker exec` allows you to execute commands within a running container. The `-i` argument allows you to execute an interactive command while the `-t` option allocates a pseudo-TTY to the process within the container. Because our goal is to access the sample database through the `mariadb` command line client, these options are necessary. Next, enter the name of the container running the MariaDB database; by default, this will be named `mariadb-mariadb-1`.

Following that, the remainder of this command represents the command that will be run within the container. Here, we run the `mariadb` command to access the database specifying that we want to connect as the `php` user. The final `-p` option indicates that we want to be prompted to enter the password.

```
Enter password:
```

Enter `password` and you'll then be presented with the MariaDB command line SQL shell.

```
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 3
Server version: 10.11.4-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

From here, you can interact with the database from within the `mariadb-mariadb-1` container as you would with any other MariaDB database. For example, you could update existing tables, create new ones, and insert or delete data.

To close the MariaDB prompt, you can enter the following command.

```MariaDB
\q
```

Of course, you likely won't be regularly managing your containerized databases over the command line. The purpose of this section is to only show that you can interact with the database running in this container just like you would with any other MariaDB database.

## Advanced Usage

{{< blurb/images-advanced image="MariaDB" >}}
