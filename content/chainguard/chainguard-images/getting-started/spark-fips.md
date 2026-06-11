---
title: "Getting started with the Chainguard Spark FIPS container"
type: "article"
linktitle: "Spark FIPS"
description: "Learn how to run Apache Spark workloads with FIPS 140-3 cryptography using Chainguard's Spark FIPS container, including BCFKS keystore setup and Kubernetes cluster-mode deployment with the Spark Operator"
date: 2026-06-04T00:00:00+00:00
lastmod: 2026-06-04T00:00:00+00:00
tags: ["Chainguard Containers", "FIPS"]
draft: false
images: []
menu:
  docs:
    parent: "getting-started"
weight: 070
toc: true
---

Apache Spark is a distributed computing engine for batch processing, stream processing, and machine learning at scale. Organizations subject to federal compliance requirements—including FedRAMP, FISMA, and Department of Defense frameworks—must use FIPS 140-3 validated cryptography for all cryptographic operations in Spark.

Chainguard's Spark FIPS container packages Apache Spark with the Bouncy Castle FIPS cryptographic provider, replacing the standard JVM cryptographic modules with NIST-validated equivalents. In FIPS mode, TLS connections require BCFKS-format keystores rather than the standard PKCS12 or JKS formats, and only FIPS-approved cipher suites are permitted.

This guide covers two deployment patterns. The first demonstrates how to generate BCFKS keystores and verify that Spark runs correctly with FIPS TLS configured. The second shows how to deploy Spark in Kubernetes cluster mode using the Spark Operator FIPS container, which is the recommended approach for production workloads.

{{< details "What is distroless?" >}}
{{< blurb/distroless >}}
{{< /details >}}

{{< details "What is Wolfi?" >}}
{{< blurb/wolfi >}}
{{< /details >}}

{{< details "What are multi-stage builds?" >}}
{{< blurb/multistage >}}
{{< /details >}}

{{< details "Chainguard Containers" >}}
{{< blurb/images >}}
{{< /details >}}

## Prerequisites

Both examples require Docker and access to the Chainguard private registry. Example 2 also requires `kubectl`, `helm`, and `kind`.

- [Docker](https://docs.docker.com/get-docker/) installed and running
- Chainguard customer credentials for `cgr.dev/chainguard-private`
- For Example 2: [`kubectl`](https://kubernetes.io/docs/tasks/tools/), [`helm`](https://helm.sh/docs/intro/install/), and [`kind`](https://kind.sigs.k8s.io/docs/user/quick-start/)

Authenticate your Docker client to the Chainguard registry:

```shell
chainctl auth configure-docker
```

## Understanding BCFKS keystores

Standard Java applications use JKS or PKCS12 keystores. Neither format is available in FIPS mode. Bouncy Castle FIPS requires BCFKS (Bouncy Castle Keystore), a proprietary keystore format that complies with FIPS 140-3 storage requirements.

The Spark FIPS container pre-installs the Bouncy Castle FIPS libraries at `/usr/share/java/bouncycastle-fips/` and pre-configures the JVM to load the BCFIPS provider. Any `keytool` operation that creates or reads a BCFKS keystore must explicitly specify the BCFIPS provider:

```
-storetype BCFKS
-providername BCFIPS
-providerclass org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider
-providerpath /usr/share/java/bouncycastle-fips/bc-fips.jar
```

Before running `keytool`, clear `JAVA_TOOL_OPTIONS` and `JDK_JAVA_OPTIONS`, then set them explicitly with the Bouncy Castle module path. The image's default values for those variables include global JVM options that conflict with the keytool BCFIPS provider arguments.

## Example 1: Generate BCFKS keystores and run a local smoke test

This example generates BCFKS keystores inside the Spark FIPS container and then runs the built-in SparkPi example to verify that Spark starts correctly with FIPS TLS configured.

### Generate a BCFKS keystore and truststore

Create a working directory, then run the keystore generation inside the container as root so it can write to the mounted output volume. The script creates a local certificate authority, a server keystore signed by that CA, and a truststore containing the CA certificate.

Set your keystore passwords as environment variables. Use the same values throughout both examples:

```shell
export KEY_PASSWORD=$KEY_PASSWORD
export TRUSTSTORE_PASSWORD=$TRUSTSTORE_PASSWORD
```

```shell
mkdir -p spark-ssl
```

```shell
docker run --rm --user 0:0 \
  -v "$(pwd)/spark-ssl":/out \
  -e KEY_PASSWORD=$KEY_PASSWORD \
  -e TRUSTSTORE_PASSWORD=$TRUSTSTORE_PASSWORD \
  --entrypoint /bin/sh \
  cgr.dev/chainguard-private/spark-fips:latest -c '
set -e
BC_JAR=/usr/share/java/bouncycastle-fips/bc-fips.jar
BC_DIR=/usr/share/java/bouncycastle-fips

run_kt() {
  env -u JAVA_TOOL_OPTIONS -u JDK_JAVA_OPTIONS \
    JAVA_TOOL_OPTIONS="--module-path=${BC_DIR} --add-modules=jdk.crypto.ec,jdk.crypto.cryptoki" \
    keytool "$@" \
    -providername BCFIPS \
    -providerclass org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider \
    -providerpath "${BC_JAR}"
}

# Create a local CA keypair
run_kt -genkeypair \
  -alias root-ca \
  -dname "CN=Spark CA, OU=Test, O=Test, C=US" \
  -keyalg RSA -keysize 2048 -validity 3650 \
  -ext bc=ca:true \
  -keystore /out/ca-keystore.bcfks -storetype BCFKS \
  -storepass "${TRUSTSTORE_PASSWORD}" -keypass "${TRUSTSTORE_PASSWORD}"

# Export the CA certificate
run_kt -exportcert -rfc \
  -alias root-ca \
  -keystore /out/ca-keystore.bcfks -storetype BCFKS \
  -storepass "${TRUSTSTORE_PASSWORD}" \
  -file /out/ca.crt

# Create the server keystore
run_kt -genkeypair \
  -alias spark-server \
  -dname "CN=localhost, OU=Test, O=Test, C=US" \
  -keyalg RSA -keysize 2048 -validity 825 \
  -ext "SAN=dns:localhost,ip:127.0.0.1" \
  -keystore /out/keystore.bcfks -storetype BCFKS \
  -storepass "${KEY_PASSWORD}" -keypass "${KEY_PASSWORD}"

# Create the truststore and import the CA certificate
run_kt -importcert -noprompt \
  -alias root-ca -file /out/ca.crt \
  -keystore /out/truststore.bcfks -storetype BCFKS \
  -storepass "${TRUSTSTORE_PASSWORD}"

echo "Keystores written to /out:"
ls -lh /out/*.bcfks
'
```

After the script completes, the `spark-ssl/` directory contains three files:

| File | Purpose |
|------|---------|
| `keystore.bcfks` | Server certificate and private key |
| `truststore.bcfks` | CA certificate used to verify peers |
| `ca-keystore.bcfks` | CA keypair used to sign the server certificate (not needed at runtime) |

For production deployments, replace the self-signed CA with certificates from your organization's PKI, and store passwords in your secrets management system rather than inline in shell commands.

### Verify the keystore

Confirm the keystore was created correctly:

```shell
docker run --rm --user 0:0 \
  -v "$(pwd)/spark-ssl":/out \
  -e KEY_PASSWORD=$KEY_PASSWORD \
  --entrypoint /bin/sh \
  cgr.dev/chainguard-private/spark-fips:latest -c '
BC_JAR=/usr/share/java/bouncycastle-fips/bc-fips.jar
BC_DIR=/usr/share/java/bouncycastle-fips
env -u JAVA_TOOL_OPTIONS -u JDK_JAVA_OPTIONS \
  JAVA_TOOL_OPTIONS="--module-path=${BC_DIR} --add-modules=jdk.crypto.ec,jdk.crypto.cryptoki" \
  keytool -list \
  -keystore /out/keystore.bcfks \
  -storetype BCFKS \
  -providername BCFIPS \
  -providerclass org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider \
  -providerpath "${BC_JAR}" \
  -storepass "${KEY_PASSWORD}"
'
```

The output lists the alias `spark-server` as a `PrivateKeyEntry`, confirming that the keystore is accessible by the BCFIPS provider.

### Run SparkPi with FIPS TLS

Run the built-in SparkPi example in local mode with FIPS TLS configured. The command sets both the Spark SSL layer (`spark.ssl.*`) and the JVM JSSE layer (`javax.net.ssl.*`). In local mode both sets of settings apply to the same JVM, but you need both in Kubernetes cluster mode where executor JVMs are separate processes.

```shell
docker run --rm --user 0:0 \
  -v "$(pwd)/spark-ssl":/ssl \
  -e KEY_PASSWORD=$KEY_PASSWORD \
  -e TRUSTSTORE_PASSWORD=$TRUSTSTORE_PASSWORD \
  cgr.dev/chainguard-private/spark-fips:latest \
  spark-submit \
  --master local[1] \
  --class org.apache.spark.examples.SparkPi \
  --conf spark.ssl.enabled=true \
  --conf spark.ssl.keyStore=/ssl/keystore.bcfks \
  --conf spark.ssl.keyStoreType=BCFKS \
  --conf spark.ssl.keyStoreProvider=BCFIPS \
  --conf spark.ssl.keyStorePassword=$KEY_PASSWORD \
  --conf spark.ssl.trustStore=/ssl/truststore.bcfks \
  --conf spark.ssl.trustStoreType=BCFKS \
  --conf spark.ssl.trustStoreProvider=BCFIPS \
  --conf spark.ssl.trustStorePassword=$TRUSTSTORE_PASSWORD \
  --conf "spark.driver.extraJavaOptions=-Dorg.bouncycastle.fips.approved_only=true -Djavax.net.ssl.keyStore=/ssl/keystore.bcfks -Djavax.net.ssl.keyStoreType=BCFKS -Djavax.net.ssl.keyStoreProvider=BCFIPS -Djavax.net.ssl.keyStorePassword=$KEY_PASSWORD -Djavax.net.ssl.trustStore=/ssl/truststore.bcfks -Djavax.net.ssl.trustStoreType=BCFKS -Djavax.net.ssl.trustStoreProvider=BCFIPS -Djavax.net.ssl.trustStorePassword=$TRUSTSTORE_PASSWORD" \
  /usr/lib/spark/examples/jars/spark-examples.jar 10
```

A successful run prints output similar to:

```
Pi is roughly 3.14...
```

## Example 2: Deploy on Kubernetes with the Spark Operator

In Kubernetes cluster mode, Spark creates a driver pod and one or more executor pods. At driver pod startup, the Spark Operator mounts a runtime ConfigMap at `/usr/lib/spark/conf`, which overwrites any files baked into the image at that path. This means you cannot rely on keystores or `spark-defaults.conf` files placed there at image build time.

The solution is to store keystores in a Kubernetes Secret and mount it at a path outside the Spark configuration directory. Spark properties, including the TLS configuration, go into the `sparkConf` section of the SparkApplication resource. The operator writes those values directly into the driver and executor configurations at submission time, bypassing the mounted ConfigMap entirely.

### Set up a local Kubernetes cluster

Create a kind cluster for testing:

```shell
kind create cluster --name spark-fips-test
```

Pull the Chainguard images and load them into the kind cluster. Kind nodes do not share the host Docker image cache, so this step is required for local testing:

```shell
docker pull cgr.dev/chainguard-private/spark-fips:latest
docker pull cgr.dev/chainguard-private/spark-operator-fips:latest

kind load docker-image cgr.dev/chainguard-private/spark-fips:latest \
  --name spark-fips-test

kind load docker-image cgr.dev/chainguard-private/spark-operator-fips:latest \
  --name spark-fips-test
```

For production clusters, configure an image pull secret for `cgr.dev` rather than pre-loading images. See the [Chainguard registry authentication documentation](/chainguard/chainguard-images/chainguard-registry/authenticating/) for details.

### Create namespaces and RBAC

Create separate namespaces for the operator and the Spark jobs, and grant the Spark service account the permissions it needs to create driver and executor pods:

```shell
kubectl create namespace spark-operator
kubectl create namespace spark-jobs
kubectl create serviceaccount spark --namespace spark-jobs
kubectl create rolebinding spark-role \
  --clusterrole=edit \
  --serviceaccount=spark-jobs:spark \
  --namespace spark-jobs
```

### Create the keystore secret

If you completed Example 1, the `spark-ssl/` directory already contains the generated files. Otherwise, run the keystore generation step from that example first.

Store the keystores in a Kubernetes Secret:

```shell
kubectl create secret generic spark-ssl-stores \
  --from-file=keystore.bcfks=./spark-ssl/keystore.bcfks \
  --from-file=truststore.bcfks=./spark-ssl/truststore.bcfks \
  --namespace spark-jobs
```

### Install the Spark Operator

Install the Spark Operator using the Chainguard Spark Operator FIPS image. The `spark.jobNamespaces` setting tells the operator to watch the `spark-jobs` namespace for SparkApplication resources:

```shell
helm repo add spark-operator https://kubeflow.github.io/spark-operator
helm repo update

helm install spark-operator spark-operator/spark-operator \
  --namespace spark-operator \
  --set image.registry=cgr.dev \
  --set image.repository=chainguard-private/spark-operator-fips \
  --set image.tag=latest \
  --set image.pullPolicy=Never \
  --set "spark.jobNamespaces[0]=spark-jobs"
```

Wait for the operator to become ready:

```shell
kubectl wait deployment/spark-operator-controller \
  --namespace spark-operator \
  --for=condition=Available \
  --timeout=120s
```

### Run a SparkApplication with FIPS TLS

Save the following manifest as `spark-pi-fips.yaml`. It runs the built-in SparkPi example in cluster mode with FIPS TLS configured. The keystores are mounted from the Secret at `/keystores`, and the FIPS TLS settings are passed through `sparkConf` so they apply to both the driver and executor JVMs.

```yaml
apiVersion: sparkoperator.k8s.io/v1beta2
kind: SparkApplication
metadata:
  name: spark-pi-fips
  namespace: spark-jobs
spec:
  type: Scala
  mode: cluster
  image: cgr.dev/chainguard-private/spark-fips:latest
  imagePullPolicy: Never
  mainClass: org.apache.spark.examples.SparkPi
  mainApplicationFile: local:///usr/lib/spark/examples/jars/spark-examples.jar
  arguments:
    - "10"
  sparkVersion: "4.1.2"
  restartPolicy:
    type: Never

  volumes:
    - name: keystores
      secret:
        secretName: spark-ssl-stores

  sparkConf:
    spark.ssl.enabled: "true"
    spark.ssl.keyStore: "/keystores/keystore.bcfks"
    spark.ssl.keyStoreType: "BCFKS"
    spark.ssl.keyStoreProvider: "BCFIPS"
    spark.ssl.keyStorePassword: "$KEY_PASSWORD"
    spark.ssl.trustStore: "/keystores/truststore.bcfks"
    spark.ssl.trustStoreType: "BCFKS"
    spark.ssl.trustStoreProvider: "BCFIPS"
    spark.ssl.trustStorePassword: "$TRUSTSTORE_PASSWORD"
    spark.kubernetes.driverEnv.JAVA_TOOL_OPTIONS: "--module-path=/usr/share/java/bouncycastle-fips --add-modules=jdk.crypto.ec,jdk.crypto.cryptoki"
    spark.kubernetes.executorEnv.JAVA_TOOL_OPTIONS: "--module-path=/usr/share/java/bouncycastle-fips --add-modules=jdk.crypto.ec,jdk.crypto.cryptoki"

  driver:
    serviceAccount: spark
    volumeMounts:
      - name: keystores
        mountPath: /keystores
        readOnly: true
    env:
      - name: JDK_JAVA_OPTIONS
        value: >-
          -Dorg.bouncycastle.fips.approved_only=true
          -Djavax.net.ssl.keyStore=/keystores/keystore.bcfks
          -Djavax.net.ssl.keyStoreType=BCFKS
          -Djavax.net.ssl.keyStoreProvider=BCFIPS
          -Djavax.net.ssl.keyStorePassword=$KEY_PASSWORD
          -Djavax.net.ssl.trustStore=/keystores/truststore.bcfks
          -Djavax.net.ssl.trustStoreType=BCFKS
          -Djavax.net.ssl.trustStoreProvider=BCFIPS
          -Djavax.net.ssl.trustStorePassword=$TRUSTSTORE_PASSWORD

  executor:
    instances: 1
    volumeMounts:
      - name: keystores
        mountPath: /keystores
        readOnly: true
    env:
      - name: JDK_JAVA_OPTIONS
        value: >-
          -Dorg.bouncycastle.fips.approved_only=true
          -Djavax.net.ssl.keyStore=/keystores/keystore.bcfks
          -Djavax.net.ssl.keyStoreType=BCFKS
          -Djavax.net.ssl.keyStoreProvider=BCFIPS
          -Djavax.net.ssl.keyStorePassword=$KEY_PASSWORD
          -Djavax.net.ssl.trustStore=/keystores/truststore.bcfks
          -Djavax.net.ssl.trustStoreType=BCFKS
          -Djavax.net.ssl.trustStoreProvider=BCFIPS
          -Djavax.net.ssl.trustStorePassword=$TRUSTSTORE_PASSWORD
```

The `JDK_JAVA_OPTIONS` value in the driver and executor sections overrides the image's default, which sets only the trust store type. The full value here adds FIPS approved-only mode and JSSE settings for both the keystore and truststore. The `JAVA_TOOL_OPTIONS` override in `sparkConf` extends the image's default module path with the EC and CRYPTOKI modules that Bouncy Castle FIPS requires at runtime.

For production deployments, do not hardcode passwords in the manifest. Store them in a Kubernetes Secret and reference them via `valueFrom.secretKeyRef` in the `env` sections. `sparkConf` values like `spark.ssl.keyStorePassword` cannot reference environment variables directly. The production pattern is to use an init container or a wrapper script that generates `spark-defaults.conf` from environment variables before the Spark entrypoint runs.

Apply the manifest:

```shell
kubectl apply -f spark-pi-fips.yaml
```

### Verify the job

Watch the `spark-jobs` namespace until the driver pod completes:

```shell
kubectl get pods --namespace spark-jobs --watch
```

Once the driver pod shows `Completed`, retrieve the Pi estimate from its logs:

```shell
POD=$(kubectl get pods --namespace spark-jobs \
  -l spark-role=driver \
  -o jsonpath='{.items[-1:].metadata.name}')

kubectl logs "$POD" --namespace spark-jobs | grep "Pi is"
```

A successful run prints output similar to:

```
Pi is roughly 3.14...
```

You can also confirm that FIPS approved-only mode was active by checking the `JDK_JAVA_OPTIONS` line near the top of the driver logs:

```shell
kubectl logs "$POD" --namespace spark-jobs | grep "JDK_JAVA_OPTIONS"
```

The output includes `-Dorg.bouncycastle.fips.approved_only=true`.

### Clean up

Delete the SparkApplication and the kind cluster when you're done:

```shell
kubectl delete -f spark-pi-fips.yaml
kind delete cluster --name spark-fips-test
```
