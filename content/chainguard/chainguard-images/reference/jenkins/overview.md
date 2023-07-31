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
|  `latest` | July 28th    | `sha256:bab0d611a5e4b1c32903c33f5b5dc8dc185203b7978fa7e92897df4732ca274a` |



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

