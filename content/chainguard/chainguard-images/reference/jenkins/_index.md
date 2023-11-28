---
title: "Image Overview: jenkins"
linktitle: "jenkins"
type: "article"
layout: "single"
description: "Overview: jenkins Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2023-11-28 00:31:13
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/jenkins/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/jenkins/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/jenkins/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jenkins/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal [Jenkins](https://jenkins.io) container image. **Currently experimental.**
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/jenkins:latest
```
<!--getting:end-->

<!--body:start-->
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
<!--body:end-->

