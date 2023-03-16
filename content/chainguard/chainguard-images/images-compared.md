---
title: "Comparison of Vulnerabilities in Container Images"
lead: "Detected CVEs Over Time" 
type: "article"
description: "Comparing popular base images with Chainguard Images in number of CVEs detected over time"
date: 2022-09-15T08:49:31+00:00
lastmod: 2022-09-15T08:49:31+00:00
draft: false
tags: ["Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 400
toc: true
---

On this page you can find comparison graphs showing the number of CVEs (common vulnerabilities and exposures) detected by [Trivy](https://github.com/aquasecurity/trivy) on popular official base images versus [Chainguard Images](https://www.chainguard.dev/chainguard-images?utm_source=docs).

{{< rumble title="Nginx" description="Comparing the latest official Nginx image with cgr.dev/chainguard/nginx" left="nginx:latest" right="cgr.dev/chainguard/nginx:latest" >}}

{{< rumble title="PHP" description="Comparing the latest official PHP image with cgr.dev/chainguard/php" left="php:latest" right="cgr.dev/chainguard/php:latest" >}}
