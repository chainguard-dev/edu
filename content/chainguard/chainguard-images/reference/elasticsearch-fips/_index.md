---
title: "Image Overview: elasticsearch-fips"
linktitle: "elasticsearch-fips"
type: "article"
layout: "single"
description: "Overview: elasticsearch-fips Chainguard Image"
date: 2024-05-06 00:43:57
lastmod: 2024-05-06 00:43:57
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/elasticsearch-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/elasticsearch-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/elasticsearch-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/elasticsearch-fips/provenance_info/" >}}
{{</ tabs >}}

# Elasticsearch FIPS

## An elastic license is required to use this image!

A [Wolfi](https://github.com/wolfi-dev)-based image tailored for Elasticsearch,
incorporating the required bouncycastle FIPS modules (bcfips) to facilitate
Elasticsearch's operation in FIPS mode.

Both OpenJDK and Elasticsearch have been configured to harness the BouncyCastle
FIPS API at their core. The included bcfips module meets FIPS 140-2 compliance
requirements and is accredited under:
_[FIPS certificate 4616](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4616)_.

## Disclaimer

To run Elasticsearch in FIPS mode, you will need to provide a license key. To obtain
a license for Elasticsearch, see their subscriptions page [here](https://www.elastic.co/subscriptions).

This image is equipped with the essential components for Elasticsearch to operate in
FIPS mode. However, it's important for users to ensure they use it in line with
FIPS compliance standards.

This includes tasks such as KeyStore generation, configuration, and launching
Elasticsearch with the correct configuration parameters. More guidance is provided
in the sections below.

## KeyStore

Elasticsearch requires a bcfips-compatible KeyStore to manage its SSL/TLS
certificates.

Although Elasticsearch supports various KeyStore types, only BCKFS offers the
capability to operate in approved _(strict)_ mode under FIPS standards, ensuring
only approved ciphers are used.

### BCKFS KeyStore creation

**Refer to the [official documentation](https://www.bouncycastle.org/fips-java)**
**for information on how to create and configure a KeyStore.**

**Note:** The KeyStore needs to be generated on a seperate image, as the keytool
application will not operate when bcfips is running in approved mode. Here is a
snippet from our communication with the BouncyCastle maintainers:

> keytool will not run if bcfips is running in approved mode. It is hard coded
> to pass a new SecureRandom(), which will always fail the approved RNG test.

Below is an example, using a wolfi-base container to generate a bckfs KeyStore:

```bash
docker run -v $(pwd):/tmp/keystore -it cgr.dev/chainguard/wolfi-base:latest sh
...

apk update && apk add curl openjdk-17-default-jvm

# https://www.bouncycastle.org/fips-java for latest `bc-fips` version
curl https://downloads.bouncycastle.org/fips-java/bc-fips-<VERSION>.jar \
-o bc-fips.jar

keytool -v -keystore /tmp/keystore/server.keystore \
  -J--add-exports=java.base/sun.security.provider=ALL-UNNAMED \
  -storetype bcfks \
  -providername BCFIPS \
  -providerclass org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider \
  -providerpath bc-fips.jar \
  -alias "localhost" \
  -genkeypair -sigalg SHA512withRSA -keyalg RSA \
  -dname CN="localhost" \
  -storepass "<YOUR TLS KEYSTORE PASSWORD>"
```

## Run image

> This image aligns with the original
> [upstream image](https://hub.docker.com/_/elasticsearch) regarding
> its entrypoint and command-line arguments. Also see the
> Elasticsearch [GitHub repository](https://github.com/elastic/elasticsearch),
and the [Elasticsearch FIPS documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/fips-140-compliance.html).

### Running in a production environment

First, we need to start the container and open a shell. The reason we must
do this is because, by default, Elasticsearch will create its own KeyStore
with a non-compliant password length:

```bash
docker run \
  -it --rm \
  -p 9200:9200 \
  -e "discovery.type=single-node" \
  -e "xpack.security.transport.ssl.keystore.password=<YOUR TLS KEYSTORE PASSWORD>" \
  --entrypoint bash \
  --name elasticsearch \
  cgr.dev/images-private/elasticsearch-fips:latest
```

Now, from a different terminal, copy over the TLS KeyStore:

```bash
docker cp server.keystore elasticsearch:/usr/share/elasticsearch/config/server.keystore
```

Return to the terminal running the Elasticsearch container and generate the
KeyStore for Elasticsearch. You'll be prompted to enter and confirm a password.
Like the TLS KeyStore, the password set for the Elasticsearch KeyStore must be
FIPS compliant (at least 112 bits):

```bash
elasticsearch-keystore create -p
```

Now we can start Elasticsearch! You'll be prompted for your Elasticsearch
KeyStore password:

```bash
elasticsearch
```

In this example, the Elasticsearch is accessible via:
[http://localhost:9200](http://localhost:9200).

### FIPS validation

You'll see the JVM security providers loaded after starting Elasticsearch if
it is running in FIPS mode:

```bash
JVM Security Providers: [bcjsse, bcfips, sun]
```

Additionally, you can check bcfips is enforcing minimum password lengths, by
running the container with a non-compliant Elasticsearch KeyStore password,
such as `1234`:

```bash
Caused by: org.bouncycastle.crypto.fips.FipsUnapprovedOperationError:
password must be at least 112 bits
```

## Adding plugins to the image

Elasticsearch provides a mechanism to add plugins to the image. This process
is outlined in the [Elasticsearch ECK documentation](https://www.elastic.co/guide/en/cloud-on-k8s/current/k8s-custom-images.html).

Unlike the upstream Elasticsearch image, we provide all Elasticsearch utilities
in the local path so that they can be ran directly. Due to this, we do not need
to prefix `bin/` to the executable path for `elasticsearch-plugin`, and we can
just invoke it directly. Here's an example installing the `analysis-icu` plugin:

```bash
FROM cgr.dev/<REGISTRY>/elasticsearch-fips:latest
RUN elasticsearch-plugin install --batch analysis-icu
```

## Debugging

#### KeyStore corrupted error upon launch

**Error Message**:
```bash
BCFKS KeyStore corrupted: MAC calculation failed.
```

**Solution:**
The error indicates that a KeyStore was detected, but there was an issue
parsing it. Usually this means that the password used to create the KeyStore
does not match what was provided to Elasticsearch.

#### Password must be at least 112 bits

**Error Message**:
```bash
Exception in thread "main" java.security.GeneralSecurityException: Error generating an encryption key from the provided password
...
Caused by: org.bouncycastle.crypto.fips.FipsUnapprovedOperationError: password must be at least 112 bits
```

**Solution:**
This is expected whenever Elasticsearch is running in `strict` (approved) mode for
FIPS. Choose a longer user or KeyStore password which is compliant.

