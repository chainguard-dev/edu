---
title: "Migrating to Python Chainguard Images"
linktitle: "Python Migration"
type: "article"
description: "Guide on migrating containerized Python applications to Chainguard Images"
date: 2024-05-02T15:06:00-07:00
lastmod: 2024-05-02T15:06:00-07:00
draft: false
tags: ["Images", "Product", "Conceptual"]
images: []
weight: 705
toc: true
---

This guide is a high-level overview for migrating an existing containerized Python application to Chainguard Images. 

Chainguard Images are built on [Wolfi](/open-source/wolfi/), a distroless Linux image designed for security and a reduced attack surface. Chainguard Images are smaller and have [low to no CVE](/chainguard/chainguard-images/vuln-comparison/python/). Our Chainguard Images for Python are built nightly for extra freshness, so they're always up-to-date with the latest remediations.

{{< details "What is Distroless?" >}}
{{< blurb/distroless >}}
{{< /details >}}

{{< details "What is Wolfi OS?" >}}
{{< blurb/wolfi >}}
{{< /details >}}

Because Chainguard Images aim to be minimal, including providing separate development and production tags, adapting your containerized application requires that you consider some additional factors that will be discussed below.

## Chainguard Images for Python Overview

We distribute two versions of our [Python Chainguard Image](https://edu.chainguard.dev/chainguard/chainguard-images/reference/python/), one for development that includes shells such as bash and package managers such as pip and a production image that removes these tools for increased security. Our production images are tagged as `latest`, while our development images are tagged as `latest-dev`. 

## Migrating a Python Application

When migrating most containerized Python applications, we recommend building a virtual environment with any needed Python packages using our provided development images, then copying over the virtual environment to our stripped-down production image. Chainguard Academy hosts [detailed instructions for a multi-stage build for a CLI-based Python script](/chainguard/chainguard-images/getting-started/python). 

The below Dockerfile provides an example of such a multi-stage build for a simple Flask application. You can view a version of this Dockerfile with included sample Flask application and requirements.txt in [this repository](https://github.com/chainguard-dev/cg-images-python-migration/tree/python-only), and the original unmigrated application in the [v0 branch](https://github.com/chainguard-dev/cg-images-python-migration/tree/v0). A more complex setup with reverse proxy orchestrated with Docker Compose is provided in the next section.

```Dockerfile
# syntax=docker/dockerfile:1

FROM cgr.dev/chainguard/python:latest-dev as dev

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

As you can see, the primary difference in this Flask application compared to the pre-migration application is the use of a multistage build. In the initial stage, we copy our requirements into the development version of the Python Chainguard Image, initialize a virtual environment, and install needed packages with pip. In the second stage, we copy the virtual environment from the development image, copy the application from the host, set exposed port ;metadata, and run the application with the [Gunicorn](https://gunicorn.org/) WSGI server.

By default, the entrypoint for the Python Chainguard Image is `python` rather than `bash`. However, if you replace the included Python binary with the virtual environment binary on the path as we do above, you should set the entrypoint explicitly, otherwise you will not have access to the packages included in your virtual environment.

We recommend that you pin dependencies to specific versions in your own application. The example Flask application script linked above also enables debug mode, which should be turned off in a production scenario.

You may wish to include the following environmental variables in your Dockerfile. They prevent the buffering of output and prevent the creation of cached bytecode, respectively, and can be included in both stages of the multi-stage build.

```Dockerfile
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
```

## Serving an Application with nginx and Docker Compose

We provide an [nginx Chainguard Image](/chainguard/chainguard-images/reference/nginx/), also with low to no CVEs, that can be used as a secure and performant reverse proxy to serve your application. You can view an [example orchestration of a Flask application and nginx using Chainguard Images](https://github.com/chainguard-dev/cg-images-python-migration/tree/compose-flask-nginx) at the linked repository. The `compose.yml` file is provided as a reference below.

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

If your project image requires a set of packages that cannot be installed with pip using the multi-stage approach above, you can consider [building your application on the Wolfi base image](/chainguard/chainguard-images/reference/wolfi-base/) and install additional Python and non-Python packages as APKs. If needed packages are not available on Wolfi OS, you can build your own packages with [melange](/open-source/melange/overview).

## Additional Resources

You may wish to refer to the [Python microservice example](/chainguard/migration/porting-apps-to-chainguard/#updating-the-python-microservice) in the [porting a sample application guide](/chainguard/migration/porting-apps-to-chainguard/) as an additional useful reference while migrating your application.

Debugging distroless containers can be a challenge given their lack of interactive tools such as shells. If you're having difficulty debugging issues with your multi-stage build, you may find the [Debugging Distroless](/chainguard/chainguard-images/debugging-distroless-images/) guide a useful resource.

The following blog posts and videos may also assist with migrating your Python application:

- [Blog Post: Securely Containerize a Python Application with Chainguard Images](https://dev.to/chainguard/securely-containerize-a-python-application-with-chainguard-images-bn8)
- [Video: How to containerize a Python application with a multi-stage build using Chainguard Images](https://www.youtube.com/watch?v=2D0JULd4E5A)
