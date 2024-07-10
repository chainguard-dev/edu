---
title: "Image Overview: jitsucom-rotor"
linktitle: "jitsucom-rotor"
type: "article"
layout: "single"
description: "Overview: jitsucom-rotor Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-07-10 00:36:03
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/jitsucom-rotor/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jitsucom-rotor/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/jitsucom-rotor/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jitsucom-rotor/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Jitsu is an open-source Segment alternative. Fully-scriptable data ingestion engine for modern data teams. Set-up a real-time data pipeline in minutes, not days
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/jitsucom-rotor:latest
```


<!--body:start-->

## Usage

There is no official Helm chart providied for Jitsu, but you can use the following Helm chart to deploy Jitsu on your Kubernetes cluster.

Here is the issue that they discussed: https://github.com/jitsucom/jitsu/issues/880

And here is the Helm chart that you can use: https://github.com/stafftastic/jitsu-chart 

which is the Helm chart we used to deploy Jitsu on Kubernetes during the tests.


```yaml
$ helm install jitsu oci://registry-1.docker.io/stafftasticcharts/jitsu -f-<<EOF
console:
  image:
    repository: cgr.dev/chainguard/jitsucom-console
    tag: latest
    pullPolicy: IfNotPresent
rotor:
  image:
    repository: cgr.dev/chainguard/jitsucom-rotor
    tag: latest
    pullPolicy: IfNotPresent
EOF
```

<!--body:end-->

