---
title: "Image Overview: flink"
linktitle: "flink"
type: "article"
layout: "single"
description: "Overview: flink Chainguard Image"
date: 2024-05-20 00:48:18
lastmod: 2024-05-20 00:48:18
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/flink/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/flink/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/flink/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/flink/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->

## Overview
Apache Flink is a framework and distributed processing engine for stateful computations over unbounded and bounded data streams. Flink has been designed to run in all common cluster environments, perform computations at in-memory speed and at any scale.

To get more information about Apache Flink, please visit the [official website](https://flink.apache.org/).

<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/flink:latest
```


<!--body:start-->

## Usage

One of the simplest ways to get started with Apache Flink on Kubernetes is to use the Flink Kubernetes Operator provided by the Apache Flink community. The Flink Kubernetes Operator is a Kubernetes custom controller that simplifies the deployment and management of Apache Flink applications on Kubernetes.


### Deploying Apache Flink on Kubernetes

The following example shows how to deploy Apache Flink on Kubernetes using the Flink Kubernetes Operator.

1. Install the Flink Kubernetes Operator by following the instructions in the [Flink Kubernetes Operator documentation](https://nightlies.apache.org/flink/flink-kubernetes-operator-docs-main/docs/try-flink-kubernetes-operator/quick-start/).

2. Create a FlinkDeployment resource to deploy Apache Flink on Kubernetes. The following example shows a basic FlinkDeployment resource that deploys a Flink job using the StateMachineExample.jar example JAR file.

> ⚠️ **Note:** Do not forget to deploy the FlinkDeployment with the same namespace where the Flink Kubernetes Operator is running.

```yaml
apiVersion: flink.apache.org/v1beta1
kind: FlinkDeployment
metadata:
  name: basic-example
spec:
  image: cgr.dev/chainguard-private/flink:latest
  flinkVersion: v1_17
  flinkConfiguration:
    taskmanager.numberOfTaskSlots: "2"
  serviceAccount: flink
  jobManager:
    resource:
      memory: "2048m"
      cpu: 1
  taskManager:
    resource:
      memory: "2048m"
      cpu: 1
  job:
    jarURI: local:///opt/flink/examples/streaming/StateMachineExample.jar
    parallelism: 2
    upgradeMode: stateless
```

3. Apply the FlinkDeployment resource to deploy Apache Flink on Kubernetes.

```shell
kubectl apply -f flink-deployment.yaml
```

4. Monitor the Flink job by viewing the logs of the Flink job manager and task manager pods.

```shell

kubectl logs -f deploy/basic-example
```

5. To access the Flink web UI, port-forward the Flink job manager service to your local machine.

```shell

kubectl port-forward svc/basic-example-rest 8081
```

6. Open a web browser and navigate to `http://localhost:8081` to access the Flink web UI.

That's it! You have successfully deployed Apache Flink on Kubernetes using the Flink Kubernetes Operator.

<!--body:end-->

