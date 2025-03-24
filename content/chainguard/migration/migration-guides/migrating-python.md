---
title: "Migrating to Python Chainguard Images"
linktitle: "Python"
aliases:
- /chainguard/migration-guides/migrating-python/
- /chainguard/migration/migrating-python/
- /chainguard/migration/migration-guides/migrating-python/
type: "article"
description: "Guide on migrating containerized Python applications to Chainguard Images"
date: 2024-05-02T15:06:00-07:00
lastmod: 2024-05-02T15:06:00-07:00
draft: false
tags: ["Images", "Product", "Conceptual"]
images: []
weight: 020
toc: true
---

This guide is a high-level overview for migrating an existing containerized Python application to Chainguard Images. 

Chainguard Images are built on [Wolfi](/open-source/wolfi/), a [distroless](/software-security/videos/distroless/) Linux distribution designed for security and a reduced attack surface. Chainguard Images are smaller and have [low to no CVE](/chainguard/chainguard-images/vuln-comparison/python/). Our Chainguard Images for Python are built nightly for extra freshness, so they're always up-to-date with the latest remediations.

{{< details "What is Distroless?" >}}
{{< blurb/distroless >}}
{{< /details >}}

{{< details "What is Wolfi OS?" >}}
{{< blurb/wolfi >}}
{{< /details >}}

Because Chainguard Images aim to be minimal, including providing separate development and production tags, adapting your containerized application requires that you consider some additional factors that will be discussed below.

## Chainguard Images for Python Overview

We distribute two versions of our [Python Chainguard Image](https://images.chainguard.dev/directory/image/python/overview?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-migration-migrating-python): a development image that includes shells such as ash/bash and package managers such as pip and a production image that removes these tools for increased security. Ourpublic production images are tagged as `latest`, while our public development images are tagged as `latest-dev`.

## Differences from the Docker Official Image

When migrating your Python application , keep in mind these differences between the [Chainguard Image for Python](https://images.chainguard.dev/directory/image/python/overview?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-migration-migrating-python) and the [official Docker image](https://hub.docker.com/_/python).

- The entrypoint for the Chainguard Image for Python is `/usr/bin/python`. When running either the `latest` or `latest-dev` versions of the image interactively, you'll be working in the Python interpreter. When using `CMD` in your Dockerfiles, provided commands will be passed to `python` by default. If you change the path to include binaries from a virtual environment , you should manually set the entrypoint or your Dockerfile will continue to use the included system Python as the entrypoint and you will not have access to installed packages in the virtual environment.
- Chainguard Images for Python run as the `nonroot` user by default. If you need elevated permissions, such as to add packages with `apk`, run the image as `--user root`. You should not use the root user in a production scenario.
- The `/home` and `/home/nonroot` directories are owned by the nonroot user.
- The `python:latest` Chainguard Image intended for production does not include a `sh`, `ash`, or `bash`. See the [Debugging Distroless](/chainguard/chainguard-images/debugging-distroless-images/) guide for advice on resolving issues without the use of these shells.
- The `python:latest` Chainguard Image does not contain package managers such as `pip` or `apk`. See the sections below for guidance on multi-stage builds (recommended)or building your own images on Wolfi (advanced usage).
- Chainguard Images for Python aim to be lightweight, and you may find that specific packages or dependencies are not included by default. The [image details reference](https://images.chainguard.dev/directory/image/python/specifications?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-migration-migrating-python) provides specific information on packages, features, and default environment variables for the image.

## Migrating a Python Application

When migrating most containerized Python applications, we recommend building a virtual environment with any needed Python packages using our provided development images, then copying over the virtual environment to our stripped-down production image. Chainguard Academy hosts [detailed instructions for a multi-stage build for a CLI-based Python script](/chainguard/chainguard-images/getting-started/python). 

The below Dockerfile provides an example of such a multi-stage build for a simple Flask application. You can view a version of this Dockerfile with included sample Flask application and `requirements.txt` in [this repository](https://github.com/chainguard-dev/cg-images-python-migration/tree/python-only), and the original unmigrated application in the [v0 branch](https://github.com/chainguard-dev/cg-images-python-migration/tree/v0). A more complex setup with reverse proxy orchestrated with Docker Compose is provided in the next section.

```Dockerfile
# syntax=docker/dockerfile:1

FROM cgr.dev/chainguard/python:latest-dev AS dev

WORKDIR /flask-app

RUN python -m venv venv
ENV PATH="/flask-app/venv/bin":$PATH
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

FROM cgr.dev/chainguard/python:latest

WORKDIR /flask-app

COPY app.py app.py
COPY --from=dev /flask-app/venv /flask-app/venv
ENV PATH="/flask-app/venv/bin:$PATH"

EXPOSE 8000

ENTRYPOINT ["python", "-m", "gunicorn", "-b", "0.0.0.0:8000", "app:app"]
```

When running an application containerized with the above Dockerfile, the application should be visible on `0.0.0.0:8000`.

As you can see, the primary difference in this Flask application compared to the pre-migration application is the use of a multistage build. In the initial stage, we copy our requirements into the development version of the Python Chainguard Image, initialize a virtual environment, and install needed packages with pip. In the second stage, we copy the virtual environment from the development image, copy the application from the host, set exposed port metadata, and run the application with the [Gunicorn](https://gunicorn.org/) WSGI server.

By default, the entrypoint for the Python Chainguard Image is `/usr/bin/python` rather than `bash`. However, if you shadow the included system `python` with the virtual environment `python`on the path as we do above, you should set the entrypoint explicitly. Otherwise, you will not have access to the packages included in your virtual environment.

We recommend that you pin dependencies to specific versions in your own application. The example Flask application script linked above also enables debug mode, which should be turned off in a production scenario.

You may wish to include the following environmental variables in your Dockerfile. The first prevents the buffering of output, meaning that all messages printed to standard output are immediately printed rather than being held in a cache. The second prevents the creation of cached bytecode, which can marginally reduce image size.

```Dockerfile
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
```

## Serving an Application with nginx and Docker Compose

We provide an [nginx Chainguard Image](https://images.chainguard.dev/directory/image/nginx/overview?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-migration-migrating-python), also with low to no CVEs, that can be used as a secure and performant reverse proxy to serve your application. You can view an [example orchestration of a Flask application and nginx using Chainguard Images](https://github.com/chainguard-dev/cg-images-python-migration/tree/compose-flask-nginx) at the linked repository. The `compose.yml` file is provided as a reference below.

```Dockerfile
services:
  flask-app:
    build:
      context: flask-app
    restart: always
    ports:
      - 8000:8000
    networks:
      - backnet
      - frontnet
  nginx:
    build: nginx
    restart: always
    ports:
      - 80:80
    depends_on: 
      - flask-app
    networks:
      - frontnet

networks:
  backnet:
  frontnet:
```

The backnet and frontnet networks are provided in anticipation of other backend services such as a database container. View the [sample repository branch](https://github.com/chainguard-dev/cg-images-python-migration/tree/compose-flask-nginx) for a full orchestration example with nginx configuration.

## Advanced Usage

If your project image requires a set of packages that cannot be installed with pip using the multi-stage approach above, you can consider building your application on the [Wolfi base image](https://images.chainguard.dev/directory/image/wolfi-base/overview?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-migration-migrating-python) and installing additional Python and non-Python packages as APKs.

## Additional Resources

You may wish to refer to the [Python microservice example](/chainguard/migration/porting-apps-to-chainguard/#updating-the-python-microservice) in the [porting a sample application guide](/chainguard/migration/porting-apps-to-chainguard/) as an additional useful reference while migrating your application.

Debugging distroless containers can be a challenge given their lack of interactive tools such as shells. If you're having difficulty debugging issues with your multi-stage build, you may find the [Debugging Distroless](/chainguard/chainguard-images/debugging-distroless-images/) guide a useful resource.

The following blog posts and videos may also assist with migrating your Python application:

- [Blog Post: Securely Containerize a Python Application with Chainguard Images](https://dev.to/chainguard/securely-containerize-a-python-application-with-chainguard-images-bn8)
- [Video: How to containerize a Python application with a multi-stage build using Chainguard Images](https://www.youtube.com/watch?v=2D0JULd4E5A)
