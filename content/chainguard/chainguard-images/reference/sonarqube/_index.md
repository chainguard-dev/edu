---
title: "Image Overview: sonarqube"
linktitle: "sonarqube"
type: "article"
layout: "single"
description: "Overview: sonarqube Chainguard Image"
date: 2024-07-01 00:36:20
lastmod: 2024-07-01 00:36:20
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/sonarqube/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/sonarqube/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/sonarqube/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/sonarqube/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->

## Continuous inspection

[SonarQube](https://www.sonarsource.com/products/sonarqube/) provides the capability to not only show the health of an application but also to highlight issues newly introduced. With a Quality Gate in place, you can achieve Clean Code and therefore improve code quality systematically.

**Note**: This image bundles JREs for provisioning to client machines (see https://sonarsource.atlassian.net/browse/SONAR-22167, https://sonarsource.atlassian.net/browse/SONAR-22034). These JREs _must not_ be removed, as endpoints in SonarQube depend on them.

<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/sonarqube:latest
```


<!--body:start-->

## Trying out SonarQube locally

To try out SonarQube locally, you can run it in a Docker container:

```shell
docker run --rm -d --name sonarqube -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true -p 9000:9000 cgr.dev/chainguard/sonarqube:latest
```

Then access it from your browser via https://localhost:9000.

## Installing with the SonarQube Helm chart

Instructions to deploy SonarQube as a Helm chart can be found on https://docs.sonarsource.com/sonarqube/latest/setup-and-upgrade/deploy-on-kubernetes/sonarqube/

<!--body:end-->

