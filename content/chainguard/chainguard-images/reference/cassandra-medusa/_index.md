---
title: "Image Overview: cassandra-medusa"
linktitle: "cassandra-medusa"
type: "article"
layout: "single"
description: "Overview: cassandra-medusa Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-02-16 00:30:51
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/cassandra-medusa/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/cassandra-medusa/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/cassandra-medusa/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cassandra-medusa/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[cassandra-medusa](https://github.com/thelastpickle/cassandra-medusa), is a Apache Cassandra Backup and Restore Tool.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/cassandra-medusa:latest
```
<!--getting:end-->

<!--body:start-->

## Usage
Medusa for Apache Cassandra® is deployed by a K8ssandra Operator install, based on the Medusa Custom Resource Definition (CRD). Once K8ssandra Operator is deployed, you can refer to the [official documentation](https://docs.k8ssandra.io/tasks/backup-restore/) for further usage of Medusa 

To use our minimal, wolfi-based image with this Helm chart you'll need to override the image used by the official helm chart and specify the chainguard image as per below example:

```shell
kubectl create ns cassandra-medusa

helm repo add k8ssandra https://helm.k8ssandra.io/stable
helm repo update

helm install cassandra-medusa k8ssandra/k8ssandra-operator -n cassandra-medusa

# create a secret, needed for medusa
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Secret
metadata:
 name: medusa-bucket-key
 namespace: cassandra-medusa
type: Opaque
stringData:
 # Note that this currently has to be set to credentials!
 credentials: |-
   [default]
   aws_access_key_id = k8ssandra
   aws_secret_access_key = k8ssandra
EOF

# create a K8ssandraCluster using Chainguard's cassandra-medusa image
cat <<EOF | kubectl apply -n ${NAMESPACE} -f -
apiVersion: k8ssandra.io/v1alpha1
kind: K8ssandraCluster
metadata:
  name: demo
  namespace: "${NAMESPACE}"
spec:
  cassandra:
    serverVersion: "4.0.1"
    datacenters:
      - metadata:
          name: dc1
        size: 1
        storageConfig:
          cassandraDataVolumeClaimSpec:
            storageClassName: standard
            accessModes:
              - ReadWriteOnce
            resources:
              requests:
                storage: 5Gi
        config:
          jvmOptions:
            heapSize: 512M
        stargate:
          size: 1
          heapSize: 256M
  medusa:
    containerImage:
      registry: cgr.dev
      repository:chainguard
      name: cassandra-medusa
      tag: latest
      pullPolicy: Always
    storageProperties:
    #   storageProvider: s3_compatible
      bucketName: k8ssandra-medusa
      prefix: test
      storageSecretRef:
        name: medusa-bucket-key
    #   host: minio-service.minio.svc.cluster.local
    #   port: 9000
      secure: false
EOF
```

For further checks and operations on backup and restore with Medusa, please refere to this [official documentaion](https://docs.k8ssandra.io/tasks/backup-restore/)

As per [project documentation](https://github.com/k8ssandra/k8ssandra-operator/blob/main/docs/content/en/install/local/single-cluster-helm/_index.md#deploy-cert-manager), by default, the Helm installation requires cert-manager to be present in the Kubernetes installation. If you do not have cert-manager installed, follow the steps at (https://cert-manager.io/docs/installation/helm/)[cert-manager's] documentation.
<!--body:end-->

