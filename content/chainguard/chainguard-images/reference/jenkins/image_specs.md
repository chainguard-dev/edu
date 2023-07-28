---
title: "Jenkins Image Variants"
type: "article"
description: "Detailed information about the Jenkins Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Jenkins"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Jenkins** Image.

## Variants Compared
The **jenkins** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

## Default Image Settings
`USER`:		`jenkins`

`WORKDIR`:	`/app`

`ENTRYPOINT`:	`/usr/bin/java -Duser.home=/var/jenkins_home -jar /usr/share/java/jenkins/jenkins.war`

`CMD`:		not specified

The following table has additional information about each of these variants.

|              | latest | latest-dev |
|--------------|--------|------------|
| Has apk?     | no     | yes        |
| Has a shell? | yes    | yes        |

Check the [tags history page](/chainguard/chainguard-images/reference/jenkins/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `glibc-locale-en`        | X      | X          |
| `jenkins`                | X      | X          |
| `openjdk-17-jre`         | X      | X          |
| `openjdk-17-default-jvm` | X      | X          |
| `bash`                   | X      | X          |
| `coreutils`              | X      | X          |
| `busybox`                | X      | X          |
| `tzdata`                 | X      | X          |
