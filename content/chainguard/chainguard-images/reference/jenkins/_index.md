---
title: "Image Overview: jenkins"
linktitle: "jenkins"
type: "article"
layout: "single"
description: "Overview: jenkins Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-03-14 00:37:02
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
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jenkins/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/jenkins/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jenkins/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
A minimal, Wolfi-based container image for Jenkins - an open-source CI/CD server that enables developers to build, test, and deploy their software.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/jenkins:latest
```
<!--getting:end-->

<!--body:start-->
## Use It

The following example runs a local instance of Jenkins, specifying a local
volume as the jenkins_home for data persistence:

```bash
docker run --rm -v jenkins_home:/var/jenkins_home \
  -p 8080:8080 -it \
  cgr.dev/chainguard/jenkins:latest
```

In the console output, the initial admin password will be logged. Use this to
login to the Jenkins UI:

- [http://localhost:8080/](http://localhost:8080/)

Refer to the [upstream documentation](https://github.com/jenkinsci/docker/blob/master/README.md)
for full instructions on running and configuring Jenkins.
<!--body:end-->

