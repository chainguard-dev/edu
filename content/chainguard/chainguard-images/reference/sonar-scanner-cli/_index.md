---
title: "Image Overview: sonar-scanner-cli"
linktitle: "sonar-scanner-cli"
type: "article"
layout: "single"
description: "Overview: sonar-scanner-cli Chainguard Image"
date: 2024-06-23 00:43:06
lastmod: 2024-06-23 00:43:06
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/sonar-scanner-cli/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/sonar-scanner-cli/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/sonar-scanner-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/sonar-scanner-cli/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Scanner CLI for SonarQube and SonarCloud
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/sonar-scanner-cli:latest
```


<!--body:start-->
To use this image, ensure SonarQube is installed and accessible to the host where you will invoke the scanner. The scanner image will default to connecting to the SonarQube API on port 9000.

The following command shows example invocation of the image, assuming `$PWD` is the directory containing code to be scanned and `-Dsonar.host.url` is the address of a SonarQube server:

```
docker run --rm -v $PWD:/usr/src $IMAGE_NAME \
    -Dsonar.login=admin \
    -Dsonar.password=admin \
    -Dsonar.projectKey=default \
    -Dsonar.host.url=http://192.0.2.1:9000
```

 Refer to the [SonarScanner CLI documentation](https://docs.sonarsource.com/sonarqube/latest/analyzing-source-code/scanners/sonarscanner/#sonarscanner-from-docker-image) for detailed instructions on how to configure environment variables for the running container and for additional properties that can be configured at runtime.
<!--body:end-->

