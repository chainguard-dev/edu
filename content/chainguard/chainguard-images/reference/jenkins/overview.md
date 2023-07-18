---
title: "Image Overview: jenkins"
type: "article"
description: "Overview: jenkins Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "images-reference"
weight: 500
toc: true
---

[cgr.dev/chainguard/jenkins](https://github.com/chainguard-images/images/tree/main/images/jenkins)

| Tag (s)   | Last Changed | Digest                                                                    |
|-----------|--------------|---------------------------------------------------------------------------|
|  `latest` | July 11th    | `sha256:6606a4f0874612031e0862d7f6f690b9077e8f723deef63b5b478f21faca5557` |
|           | July 8th     | `sha256:13fc9f3167106e2d9a912b0be4434b675c122561efb4342e3d448b6d0f939cb8` |
|           | July 4th     | `sha256:8d6b482e9214e0711be2d57a3da2c045efa9775bfd80f8b472ff35d4799b4643` |
|           | June 26th    | `sha256:552a48de64318cbde7367e77d6c7ce9e23d15a22fef167446874eb9f1cb61587` |
|           | June 21st    | `sha256:0f3edbcd969202a24552e6d123db8417095d8edffd367c4374c776bf20db3a28` |



Minimal [Jenkins](https://jenkins.io) container image. **Currently experimental.**

- [Documentation](https://edu.chainguard.dev/chainguard/chainguard-images/reference/jenkins)
- [Getting Started Guide](https://edu.chainguard.dev/chainguard/chainguard-images/reference/jenkins/overview/#use-it)
- [Provenance Information](https://edu.chainguard.dev/chainguard/chainguard-images/reference/jenkins/provenance_info/)

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/jenkins:latest
```

## Use It

This is an experimental image and subject to change.  We welcome all feedback.

To test out the Chainguard Jenkins image, run the following command, which will create a volume to persist build and configuration data from the container's `$JENKINS_HOME`:

```sh
docker run --rm -v jenkins_home:/var/jenkins_home -p 8080:8080 -ti cgr.dev/chainguard/jenkins
```

And visit Jenkins in your brower http://localhost:8080

If you want to backup your Jenkins data, create a local directory for the files and mount it along with the `jenkins_home` volume. You can then start a Jenkins container and copy the files out:

```sh
mkdir -m 777 jenkins-backup
docker run --rm \
  -v $PWD/jenkins-backup:/backup-dir \
  -v jenkins_home:/var/jenkins_home \
  -p 8080:8080 -ti \
  --entrypoint=/bin/bash \
  cgr.dev/chainguard/jenkins
cp -r /var/jenkins_home /backup-dir/
exit
```

