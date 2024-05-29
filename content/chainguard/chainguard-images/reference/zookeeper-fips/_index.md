---
title: "Image Overview: zookeeper-fips"
linktitle: "zookeeper-fips"
type: "article"
layout: "single"
description: "Overview: zookeeper-fips Chainguard Image"
date: 2024-05-29 00:38:53
lastmod: 2024-05-29 00:38:53
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/zookeeper-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/zookeeper-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/zookeeper-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/zookeeper-fips/provenance_info/" >}}
{{</ tabs >}}

# ZooKeeper FIPS

## SASL should not be enabled without additional configuration when running in FIPS mode due to its use of DIGEST-MD5 for authentication

A [Wolfi](https://github.com/wolfi-dev)-based image tailored for ZooKeeper,
incorporating the required bouncycastle FIPS modules (bcfips) to facilitate
ZooKeeper's operation in FIPS mode.

Both OpenJDK and ZooKeeper have been configured to harness the BouncyCastle
FIPS API at their core. The included bcfips module meets FIPS 140-2 compliance
requirements and is accredited under:
_[FIPS certificate 4616](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4616)_.

## Disclaimer

If SASL authentication is enabled, Zookeeper will default to using DIGEST-MD5 which is not FIPS compliant. Instead, configure Zookeeper to use mTLS, or GSSAPI and Kerberos for authentication. Note that the Kerberos KDC server will need to be configured to run with FIPS approved algorithms.

This image is equipped with the essential components for ZooKeeper to operate in
FIPS mode. However, it's important for users to ensure they use it in line with
FIPS compliance standards.

This includes tasks such as KeyStore generation, configuration, and launching
ZooKeeper with the correct configuration parameters. More guidance is provided
in the sections below.

## KeyStore

ZooKeeper requires a bcfips-compatible KeyStore to manage its SSL/TLS certificates.

Although ZooKeeper supports various KeyStore types, only BCKFS offers the capability
to operate in approved _(strict)_ mode under FIPS standards, ensuring only approved
ciphers are used.

### BCKFS KeyStore creation

**Refer to the [official documentation](https://www.bouncycastle.org/fips-java)**
**for information on how to create and configure a KeyStore.**

**Note:** The KeyStore needs to be generated on a seperate image, as the `keytool`
application will not operate when bcfips is running in approved mode. `keytool` is hard coded to pass a new `SecureRandom()`, which will always fail the approved RNG test. However, the generated KeyStore will use FIPS compliant ciphers and will operate correctly in a FIPS enabled environment.

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

> This image aligns with the current
> [Bitnami image](https://hub.docker.com/r/bitnami/zookeeper/) regarding
> its entrypoint and command-line arguments. Also see the
> ZooKeeper [GitHub repository](https://github.com/apache/zookeeper)

### Running in a production environment

#### Deploy with Helm

To deploy ZooKeeper FIPS using Helm, open a terminal and run the following command:

```bash
helm install -n zookeeper zookeeper oci://registry-1.docker.io/bitnamicharts/zookeeper \
  --set image.registry=cgr.dev,image.repository=<REGISTRY>/zookeeper,image.tag=latest
```

For additional configuration options provided in the chart, please
see Bitnami's documentation [here](https://artifacthub.io/packages/helm/bitnami/zookeeper).

The KeyStore will need to be passed through as a volume (via `extraVolumes`),
and TLS will need to be configured to match your environment.

#### Deploy with Docker

Alternatively, ZooKeeper FIPS can be deployed with Docker. Create a config file for ZooKeeper:

```bash
# ZooKeeper config
tickTime=2000
initLimit=10
syncLimit=5
dataDir=/tmp/zookeeper
clientPort=2181

# Use BCFKS
ssl.keyStore.location=/usr/share/java/zookeeper/conf/server.keystore
ssl.keyStore.type=bcfks
```

This uses a standard ZooKeeper configuration with the default KeyStore format
set to BCFKS. In this example, we've set the path for the KeyStore to
`/usr/share/java/zookeeper/conf/server.keystore`.

Run it with Docker:

```bash
docker run \
  -v /path/to/server.keystore:/usr/share/java/zookeeper/conf/server.keystore \
  -v /path/to/your/zoo.cfg:/usr/share/java/zookeeper/conf/zoo.cfg \
  -p <YOUR PORT>:2181 \
  -e JDK_JAVA_OPTIONS="-Djavax.net.ssl.trustStoreType=FIPS -Dzookeeper.ssl.keyStore.password=<KEYSTORE PASSWORD>" \
  --entrypoint zkServer.sh \
  cgr.dev/<REGISTRY>/zookeeper-fips:latest \
  start-foreground
```

Where `<YOUR PORT>` is the port on the host you'd like to forward to.

Note that if you've configured a secure port for ZooKeeper FIPS, you'll
forward that instead of the standard port.

ZooKeeper will likely need additional configuration depending on your
environment. For more resources, please see ZooKeeper's [admin guide](https://zookeeper.apache.org/doc/r3.9.0/zookeeperAdmin.html).

### FIPS validation

ZooKeeper itself does not provide any verbosity on systems running in
FIPS mode. However, when ZooKeeper starts the BC FIPS libraries should
be visible.

You can check bcfips is enforcing minimum password lengths, by running
the container with a non-compliant ZooKeeper KeyStore password, such
as `1234`:

```bash
Caused by: org.bouncycastle.crypto.fips.FipsUnapprovedOperationError:
password must be at least 112 bits
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
does not match what was provided to ZooKeeper.

#### Password must be at least 112 bits

**Error Message**:
```bash
Exception in thread "main" java.security.GeneralSecurityException: Error generating an encryption key from the provided password
...
Caused by: org.bouncycastle.crypto.fips.FipsUnapprovedOperationError: password must be at least 112 bits
```

**Solution:**
This is expected whenever ZooKeeper is running in `strict` (approved) mode for
FIPS. Choose a KeyStore password which is compliant.

