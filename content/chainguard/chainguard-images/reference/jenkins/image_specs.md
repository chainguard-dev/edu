---
title: "jenkins Image Variants"
type: "article"
description: "Detailed specs for jenkins Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "jenkins"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **jenkins** Image.

## Variants Compared
The **jenkins** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                                                                                 |
|--------------|----------------------------------------------------------------------------------------|
| Default User | `jenkins`                                                                              |
| Entrypoint   | `/usr/bin/java -Duser.home=/var/jenkins_home -jar /usr/share/java/jenkins/jenkins.war` |
| CMD          | not specified                                                                          |
| Workdir      | `/app`                                                                                 |
| Has apk?     | no                                                                                     |
| Has a shell? | yes                                                                                    |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `wolfi-baselayout`       | X      |
| `glibc-locale-en`        | X      |
| `jenkins`                | X      |
| `openjdk-17-jre`         | X      |
| `bash`                   | X      |
| `coreutils`              | X      |
| `busybox`                | X      |
| `tzdata`                 | X      |

