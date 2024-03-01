---
title: "Image Overview: jre-fips"
linktitle: "jre-fips"
type: "article"
layout: "single"
description: "Overview: jre-fips Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/jre-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jre-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/jre-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jre-fips/provenance_info/" >}}
{{</ tabs >}}

# OpenJDK JRE FIPS images with Bouncy Castle

This is a base image containing both the OpenJDK JRE and the Bouncy Castle crypto
libraries for FIPS.

The FIPS verified version of Bouncy Castle is only compliant to the FIPS 140-2
standard when used in accordance with the [Bouncy Castle Security Policy].
When using the OpenJDK JRE Chainguard Image for FIPS compliance, please make sure
to read the security policy and adequate your code as needed.

> **Note**:
> In this document, the registry and repository path will be referred as
> `<registry>/<repository>`. Make sure to replace those with the correct
> path of where your image is located.

## Available versions and variants

This image is currently available in the following versions and variants:

| Java version | Image name                | Variant           |
|--------------|---------------------------|-------------------|
| Java 11      | `jre-fips:openjdk-11`     | FIPS              |
| Java 11      | `jre-fips:openjdk-11-dev` | FIPS, development |
| Java 17      | `jre-fips:openjdk-17`     | FIPS              |
| Java 17      | `jre-fips:openjdk-17-dev` | FIPS, development |

## How are the `java.policy` and `java.security` files configured?

An updated version of the `java.security` configuration file is shipped under
the default location (`$JAVA_HOME/conf/security/java.security`) in this image and
is configured as described below:
* It excludes every default security provider except for the `SUN` provider,
    leaving only the following configuration:
    ```none
    security.provider.1=org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider C:DEFRND[SHA256];ENABLE{ALL};
    security.provider.2=org.bouncycastle.jsse.provider.BouncyCastleJsseProvider fips:BCFIPS
    security.provider.3=SUN
    ```

* It loads the `java.policy` file shipped under `/usr/lib/jvm/jdk-fips-config/java.policy`
    as an additional policy file, at position 2, leaving the policy configuration
    as:
    ```none
    policy.url.1=file:${java.home}/conf/security/java.policy
    policy.url.2=file:/usr/lib/jvm/jdk-fips-config/java.policy
    ```

    The additional policy file is configured as described in the BCFIPS user manual:
    ```none
    grant {
        permission java.lang.PropertyPermission "java.runtime.name", "read";

        permission java.lang.RuntimePermission "accessClassInPackage.sun.security.internal.spec";
        permission java.lang.RuntimePermission "getProtectionDomain";
        permission java.lang.RuntimePermission "accessDeclaredMembers";

        permission org.bouncycastle.crypto.CryptoServicesPermission "tlsAlgorithmsEnabled";
        permission org.bouncycastle.crypto.CryptoServicesPermission "exportKeys";
    };
    ```

* It configures the `keystore.type` as `bcfks`, in order for Keystores to be
    FIPS-compliant.

* It sets the algorithms for the `KeyManagerFactory` and `TrustManagerFactory` as PKIX:
    ```none
    ssl.KeyManagerFactory.algorithm=PKIX
    ssl.TrustManagerFactory.algorithm=PKIX
    ```

* It sets BCFIPS to `approved_only` mode:
    ```none
    org.bouncycastle.fips.approved_only=true
    ```

## Using the provided Bouncy Castle libraries

> **TL;DR**: FIPS configuration via environment variables is exported by default,
> but if the application requires more configuration these must be patched accordingly.
> All environment variables and/or command-line options must be configured before
> running the application.
>
> The Bouncy Castle APIs must be used in accordance with the Security Policy provided
> for compliance. See the [Bouncy Castle Security Policy] for more information.

This image ships with the following components:
* BouncyCastle libraries for FIPS, shipped under `/usr/share/java/bouncycastle-fips`:
    * `bc-fips.jar` v1.0.2.4
    * `bctls-fips.jar` v1.0.17
    * `bcpkix-fips.jar` v1.0.6
* Java security configurations tailored to work with Bouncy Castle FIPS as established
  in the [user guide] and described in the previous section:
    * `$JAVA_HOME/conf/security/java.security`
    * `/usr/lib/jvm/jdk-fips-config/java.policy`

This image ships with the following environment variables exported by default:
* `JDK_JAVA_FIPS_OPTIONS="--add-exports java.base/sun.security.internal.spec=ALL-UNNAMED --add-exports=java.base/sun.security.provider=ALL-UNNAMED"`
* `JAVA_FIPS_CLASSPATH=/usr/share/java/bouncycastle-fips/*`
* `JAVA_TRUSTSTORE_OPTIONS="-Djavax.net.ssl.trustStoreType=FIPS"`

> **Warning**:
> These variable values **must not** be changed. If you need to use custom `CLASSPATH`
> or other JDK options, make sure to include these variables in your new variable declarations.
> Ensure that `JAVA_TRUSTSTORE_OPTIONS` is part of your `JDK_JAVA_OPTIONS` variable when
> using this image as a base image.

In addition, the following environment variables are also exported by default and can
be updated as needed:
* `CLASSPATH=$JAVA_FIPS_CLASSPATH:.:./*`
* `JDK_JAVA_OPTIONS=$JDK_JAVA_FIPS_OPTIONS $JAVA_TRUSTSTORE_OPTIONS`

When updating your classpath variable, make sure to keep the path to the
`bouncycastle-fips` folder in your classpath, so the Bouncy Castle libraries
are discoverable:
```shell
CLASSPATH="${JAVA_FIPS_CLASSPATH}:${CLASSPATH}"
```

When updating the `JDK_JAVA_OPTIONS` environment variable, make sure to specify
the exports options required for Bouncy Castle to work properly:
```shell
JDK_JAVA_OPTIONS="${JDK_JAVA_FIPS_OPTIONS} ${JDK_JAVA_OPTIONS}"
```

If you need the use of the converted keystore, make sure to also add the
`JAVA_TRUSTSTORE_OPTIONS` variable to your `JDK_JAVA_OPTIONS`:
```shell
JDK_JAVA_OPTIONS="${JAVA_TRUSTSTORE_OPTIONS} ${JDK_JAVA_OPTIONS}"
```

Alternatively, these can be also set as an argument to the JVM tools via the
`--class-path`/`-cp` and `-D` options. Please note these arguments take
precedence over the environment variables:
```shell
javac --class-path "${JAVA_FIPS_CLASSPATH}:." ${JDK_JAVAC_FIPS_OPTIONS} TestClass.java
java -cp "${JAVA_FIPS_CLASSPATH}:." ${JDK_JAVA_FIPS_OPTIONS} TestClass
jshell --class-path "${JAVA_FIPS_CLASSPATH}:." ${JDK_JAVAC_FIPS_OPTIONS}
```

> **Note**:
> `java -jar` ignores classpath options. If your target application is a runnable jar, you will need to
> run it by including the jar in your classpath and invoking the main class. For example:
> ```shell
> java -cp "${JAVA_FIPS_CLASSPATH}:.:./*:<path to your jar here>" org.example.Main
> ```

## Checking the configuration is being loaded correctly

As part of the effort to build this image, a set of tests was created that validates
that the BCFIPS and BCJSSE providers are in use.

These are provided in different Java source files:
* `ValidateFIPS.java` verifies the following are true:
    * Cipher algorithms listed in section 3.1 of the [Bouncy Castle FIPS Java API] are available for use within the
        generated image.
    * Cipher algorithms listed in section 3.2 of the [Bouncy Castle FIPS Java API] are not available for use within the
        image.
    * Public key algorithms defined in section 4 are either not available, or available only for specific approved usages.
    * Prohibited SSL cipher algorithms are not available.
    * MD5 is unavailable.
* `TestKeyWrapping.java` checks that only approved key wrapping algorithms are
    available and working.
* `TestSymmetricEncryption.java` checks that only approved symmetric encryption
    algorithms are available and working.
* `TestSecureRandom.java` checks that `SecureRandom`s work as expected.

The entrypoint for running tests is `TestMain.java`. The main method in this entrypoint
will run all the previously described tests.

## Using this as a base image

### Java 11 JRE

To consume this image as a base image, add it in the `FROM` statement of your Dockerfile. In order for the predefined
environment variables to be correctly consumed, `java -jar` **must not** be used, as it overrides `CLASSPATH` options.
Instead, add your jars to the `CLASSPATH` and invoke the main class directly:
```dockerfile
FROM <registry>/<repository>/jre-fips:openjdk-11

ENV CLASSPATH="${JAVA_FIPS_CLASSPATH}:./*"

CMD ["MyApp"]
```

This can also be worked into a multistage build using the JDK FIPS variant for compiling your application:
```dockerfile
FROM <registry>/<repository>/jdk-fips:openjdk-11

WORKDIR /src
COPY MyClass.java .

RUN javac MyClass.java && \
    jar cvf my-app.jar *.class

FROM <registry>/<repository>/jre-fips:openjdk-11

WORKDIR /jars
COPY --from=builder /src/my-app.jar .

ENV CLASSPATH="${JAVA_FIPS_CLASSPATH}:/jars/*"
CMD ["MyApp"]
```

### Java 17 JRE

The process is the same as Java 11, but using the tag `openjdk-17` instead:
```dockerfile
FROM <registry>/<repository>/jre-fips:openjdk-17
FROM <registry>/<repository>/jdk-fips:openjdk-17
```

[Bouncy Castle Security Policy]: https://csrc.nist.gov/CSRC/media/projects/cryptographic-module-validation-program/documents/security-policies/140sp4616.pdf
[Bouncy Castle FIPS Java API]: https://downloads.bouncycastle.org/fips-java/BC-FJA-UserGuide-1.0.2.pdf
[user guide]: https://downloads.bouncycastle.org/fips-java/BC-FJA-UserGuide-1.0.2.pdf

