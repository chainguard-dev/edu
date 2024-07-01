---
title: "Image Overview: postgres"
linktitle: "postgres"
type: "article"
layout: "single"
description: "Overview: postgres Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-07-01 00:36:20
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu: 
  docs: 
    parent: "images-reference"
weight: 500
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/postgres/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/postgres/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/postgres/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/postgres/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal PostgreSQL image.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/postgres:latest
```


<!--body:start-->
## Usage

The only mandatory environment variable needed by the PostgreSQL Image is `POSTGRES_PASSWORD`. 

You can test the PostgreSQL Image by running the following command:

```sh
docker run --rm -e POSTGRES_PASSWORD=password -ti --name postgres-test cgr.dev/chainguard/postgres:latest
```

This command will run the Image, but no data within the PostgreSQL database will persist after the Image stops running.

To persist PostgreSQL data you can mount a volume mapped to the data folder:

```sh
docker run --rm -v $PWD/data:/var/lib/postgresql/data -e POSTGRES_PASSWORD=password -ti --name postgres-test cgr.dev/chainguard/postgres:latest
```

In a __new__ terminal,  `exec` into the running container:

```sh
docker exec -ti postgres-test bash
```

Connect using the postgres user:

```sh
su postgres
```

Use the `createdb` wrapper to create a test database:

```sh
createdb test
```

Then use the PostgreSQL client to Connect to the new database: 

```sh
psql test
```

From there you can interact with the database as you would with any other PostgreSQL database. For instance, you can create a sample table:

```sh
CREATE TABLE accounts (
	user_id serial PRIMARY KEY,
	username VARCHAR ( 50 ) UNIQUE NOT NULL,
	password VARCHAR ( 50 ) NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
	last_login TIMESTAMP
);
```

You could then insert data into the table:

```sh
INSERT INTO accounts (username, password, email, created_on, last_login)
VALUES (
'Inky',
'p@$$w0rD',
'inky@example.com',
'2017-07-23',
'2017-07-23'
);
```

You can also use all of PostgreSQL's internal meta-commands. For example, `\dt` will list all the tables stored within the database:

```sh
\dt
```
```
          List of relations
 Schema |   Name   | Type  |  Owner
--------+----------+-------+----------
 public | accounts | table | postgres
(1 row)
```

## Further Reading

Please refer to our guide on [getting started with the PostgreSQL Chainguard Image](https://edu.chainguard.dev/chainguard/chainguard-images/getting-started/getting-started-postgres/) for an in-depth walk-through of how you can use the PostgreSQL Image in practice. This getting started guide outlines how to set up and run a PHP application that stores its data in a PostgreSQL database running within a containerized environment. 
<!--body:end-->

