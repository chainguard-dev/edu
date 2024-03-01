---
title: "Image Overview: keycloak-fips"
linktitle: "keycloak-fips"
type: "article"
layout: "single"
description: "Overview: keycloak-fips Chainguard Image"
date: 2024-02-29 16:25:55
lastmod: 2024-02-29 16:25:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/keycloak-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/keycloak-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/keycloak-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/keycloak-fips/provenance_info/" >}}
{{</ tabs >}}

# Keycloak-fips

A [wolfi](https://github.com/wolfi-dev)-based image tailored for Keycloak,
incorporating the required bouncycastle FIPS modules (bcfips) to facilitate
Keycloak's operation in FIPS mode.

Both OpenJDK and Keycloak have been configured to harness the BouncyCastle FIPS
API at their core. The included bcfips module meets FIPS 140-2 compliance
requirements and is accredited under:
_[FIPS certificate 4616](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4616)_.

## Disclaimer

This image is equipped with the essential components for Keycloak to operate in
FIPS mode. However, it's important for users to ensure they use it in line with
FIPS compliance standards.

This includes tasks such as keystore generation, configuration, and launching
Keycloak with the correct configuration parameters. More guidance is provided in
the sections below.

## Keystore

Keycloak requires a bcfips-compatible keystore to manage its SSL/TLS
certificates.

Although Keycloak supports various keystore types, only BCKFS offers the
capability to operate in approved _(strict)_ mode under FIPS standards, ensuring
only approved ciphers are used.

### BCKFS Keystore creation

**Refer to the [official documentation](https://www.bouncycastle.org/fips-java)**
**for information on how to create and configure a Keystore.**

**Note:** The keystore needs to be generated on a seperate image, as the keytool
application will not operate when bcfips is running in approved mode. Here is a
snippet from our communication with the BouncyCastle maintainers:

> keytool will not run if bcfips is running in approved mode. It is hard coded
> to pass a new SecureRandom(), which will always fail the approved RNG test.

Below is an example, using a wolfi-base container to generate a bckfs keystore:

```bash
docker run -v $(pwd):/tmp/keystore -it cgr.dev/chainguard/wolfi-base:latest sh
...

apk update && apk add curl openjdk-17-default-jvm

# Refer to Keycloak docs: 'BCFKS keystore' section for context.
echo "securerandom.strongAlgorithms=PKCS11:SunPKCS11-NSS-FIPS" > kc-keystore.java.security

# https://www.bouncycastle.org/fips-java for latest `bc-fips` version
curl https://downloads.bouncycastle.org/fips-java/bc-fips-<VERSION>.jar \
-o bc-fips.jar

keytool -v -keystore /tmp/keystore/server.keystore \
  -J--add-exports=java.base/sun.security.provider=ALL-UNNAMED \
  -storetype bcfks \
  -providername BCFIPS \
  -providerclass org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider \
  -providerpath bc-fips.jar \
  -alias localhost \
  -genkeypair -sigalg SHA512withRSA -keyalg RSA \
  -storepass '<DESIRED-KEYSTORE-PASSWORD>' \
  -dname CN=localhost \
  -J-Djava.security.properties=kc-keystore.java.security
```

## Run image

> This image aligns with the original
> [upstream image](https://quay.io/repository/Keycloak/Keycloak?tab=info) regarding
> its entrypoint and command-line arguments. Also see the
> Keycloak [GitHub repository](https://github.com/Keycloak/Keycloak/tree/main),
and the [KeyCloak FIPS documentation](https://www.Keycloak.org/server/fips).

### Running in development mode

Example of launching Keycloak in `development` mode, with HTTP enabled and
strict hostname resolution not enforced:

```bash
docker run -v $(pwd)/server.keystore:/usr/share/java/keycloak/conf/server.keystore \
  --rm --name local-Keycloak -p 8080:8080 \
  -e KEYCLOAK_ADMIN=admin \
  -e KEYCLOAK_ADMIN_PASSWORD='<PASSWORD-FOR-ADMIN-USER>' \
    <YOUR-REGISTRY>/keycloak-fips:latest \
    start-dev \
      --features=fips \
      --fips-mode=strict \
      --https-key-store-password='<KEYSTORE-PASSWORD>' \
      --hostname=localhost \
      --log-level='INFO,org.keycloak.common.crypto:TRACE,org.keycloak.crypto:TRACE'
```

In this example, the Keycloak UI is accessible via:
[http://localhost:8080](http://localhost:8080).

### Running in production mode

Example of running Keycloak in `production` mode, enforcing the use of HTTPS
and requiring a hostname to be provided:

```bash
docker run -v /local/path/to/server.keystore:/usr/share/java/keycloak/conf/server.keystore \
  --rm --name local-Keycloak -p 8443:8443 \
  -e KEYCLOAK_ADMIN=admin \
  -e KEYCLOAK_ADMIN_PASSWORD='<PASSWORD-FOR-ADMIN-USER>' \
  	cgr.dev/chainguard/Keycloak-fips:latest \
  	start \
      --features=fips \
      --fips-mode=strict \
      --https-key-store-password='<KEYSTORE-PASSWORD>' \
      --hostname=localhost \
      --log-level='INFO,org.keycloak.common.crypto:TRACE,org.keycloak.crypto:TRACE'
```

In this example, the Keycloak UI is accessible via:
[https://localhost:8443](https://localhost:8443).

### FIPS validation

You'll see debug logs such as the below if Keycloak is running in FIPS mode:

```bash
KC(BCFIPS version 1.000204 Approved Mode) version 1.0 - class org.Keycloak.crypto.fips.KeycloakFipsSecurityProvider,
 BCFIPS version 1.000204 - class org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider
```

Additionally, you can check bcfips is enforcing minimum password lengths, by
running the container with a non-compliant admin password, such as `1234`:

```bash
Caused by: org.bouncycastle.crypto.fips.FipsUnapprovedOperationError:
password must be at least 112 bits
```

## Customizing the image

Keycloak provides a mechanism to configure and customize the image. This process
is outlined in the [Keycloak image documentation](https://github.com/Keycloak/Keycloak/blob/main/docs/guides/server/containers.adoc).

There are subtle differences in the executable paths used in the Chainguard
image. Below is the example copied from the documentation, updated with the
correct paths:

```bash
FROM cgr.dev/chainguard/Keycloak-fips:latest as builder

# Enable health and metrics support
ENV KC_HEALTH_ENABLED=true
ENV KC_METRICS_ENABLED=true

# Configure a database vendor
ENV KC_DB=postgres

WORKDIR /usr/share/java/Keycloak

# for demonstration purposes only, please make sure to use proper certificates in production instead
RUN keytool -genkeypair -storepass password -storetype PKCS12 -keyalg RSA -keysize 2048 -dname "CN=server" -alias server -ext "SAN:c=DNS:localhost,IP:127.0.0.1" -keystore conf/server.keystore
RUN /usr/share/java/Keycloak/bin/kc.sh build

FROM cgr.dev/chainguard/Keycloak-fips:latest
COPY --from=builder /usr/share/java/Keycloak/ /usr/share/java/Keycloak/

# change these values to point to a running postgres instance
ENV KC_DB=postgres
ENV KC_DB_URL=<DBURL>
ENV KC_DB_USERNAME=<DBUSERNAME>
ENV KC_DB_PASSWORD=<DBPASSWORD>
ENV KC_HOSTNAME=localhost
ENTRYPOINT ["/usr/share/java/Keycloak/bin/kc.sh"]
```

## Debugging

#### Invalid Keystore Format with BCFKS in `production` mode

**Error Message**:
```bash
# kc.sh start --features=fips --hostname=localhost --https-key-store-password='**********'
ERROR: Failed to start server in (production) mode
ERROR: Unable to start HTTP server
ERROR: java.io.IOException: Invalid keystore format
```
**Solution:**
BCFKS Keystores default to strict mode, and it's likely you omitted
`--fips-mode=strict` in your arguments. If you wish to run in non-strict mode
with BCFKS, you need to include `--https-key-store-type=bcfks`.

This is called out in the [official documentation](https://www.keycloak.org/server/fips),
but perhaps could benefit from additional clarification.


#### Keystore corrupted error upon launch

**Error Message**:
```bash
ERROR: Unable to start HTTP server
ERROR: java.io.IOException: BCFKS KeyStore corrupted: MAC calculation failed.
ERROR: BCFKS KeyStore corrupted: MAC calculation failed.
```

**Solution:**
The error indicates that a Keystore was detected, but there was an issue
parsing it. Usually this means that the password used to create the keystore
does not match what was provided as the `--https-key-store-password` argument
to Keycloak.

#### Key material not provided error in `production` mode

**Error Message**:
```bash
ERROR: Failed to start server in (production) mode
ERROR: Key material not provided to setup HTTPS. Please configure your
keys/certificates or start the server in development mode.
```

**Solution:**
This error usually indicates that a `.keystore` was not detected in the
`/usr/share/java/keycloak/conf` directory. Ensure you have created a Keystore
and it is accessible to the container in the expected directory.

#### Password must be at least 112 bits

**Error Message**:
```bash
Failed to add user '<admin-user>' to realm 'master': org.keycloak.models.ModelException:
password must be at least 112 bits
FipsUnapprovedOperationError: password must be at least 112 bits
```

**Solution:**
This is expected whenever Keycloak is running in `strict` (approved) mode for
FIPS. Choose a longer admin password which is compliant. Refer to the Keycloak
FIPS [documentation](https://www.keycloak.org/server/fips) for more information.

