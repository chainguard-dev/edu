---
title: "Image Overview: cloudnative-pg-fips"
linktitle: "cloudnative-pg-fips"
type: "article"
layout: "single"
description: "Overview: cloudnative-pg-fips Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/cloudnative-pg-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cloudnative-pg-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/cloudnative-pg-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cloudnative-pg-fips/provenance_info/" >}}
{{</ tabs >}}

# CloudNative PG FIPS

CloudNative PG is a platform for managing PostgreSQL databases within Kubernetes environments.

These images consist of the CloudNative PG operator as well as PostgreSQL images that have been
extended to support the full functionality of the CloudNative PG platform.

## Deploying CloudNative PG

To deploy CloudNative PG, install the CNPG Helm chart repository:

```bash
helm repo add cnpg https://cloudnative-pg.github.io/charts
```

Deploy the operator:

```bash
helm upgrade --install cnpg \
  --namespace cnpg-system \
  --create-namespace \
  cnpg/cloudnative-pg \
  --set image.repository="cgr.dev/<REGISTRY>/cloudnative-pg-fips" \
  --set image.tag="latest"
```

And now deploy the database:

```bash
helm upgrade --install database \
  --namespace database \
  --create-namespace \
  cnpg/cluster \
  --set cluster.imageName="cgr.dev/<REGISTRY>/postgres-cloudnative-pg-fips:<POSTGRES VERSION>"
```

Note, you must provide a Postgres version (I.E. 15, 16, etc) as the operator expects the versioned
tag for migrations.

Alternatively, deploy the database with pooler enabled using Chainguard's PgBouncer image:

```bash
helm upgrade --install database \
  --namespace database \
  --create-namespace \
  cnpg/cluster \
  --set cluster.imageName="cgr.dev/<REGISTRY>/postgres-cloudnative-pg-fips:<POSTGRES VERSION>"
  --set pooler.enabled=true \
  --set pooler.template.spec.containers[0].name="pgbouncer" \
  --set pooler.template.spec.containers[0].image="cgr.dev/<REGISTRY>/pgbouncer-fips:latest"
```

