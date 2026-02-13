---
title: "How to Use Chainguard Helm Charts"
linktitle: "Using Chainguard Helm Charts"
aliases:
type: "article"
description: "A primer on how to use Chainguard-provided upstream Helm charts to deploy Chainguard container images"
lead: "A primer on how to use Chainguard-provided upstream Helm charts to deploy Chainguard container images"
date: 2025-07-11T08:49:31+00:00
lastmod: 2026-01-29T08:49:31+00:00
draft: false
tags: ["Chainguard Containers", "Helm charts", "Product"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 050
toc: true
---

[Helm](https://helm.sh) is a package manager for Kubernetes that simplifies the installation and management of applications by automating the creation of Kubernetes resources. Helm charts are reusable, versioned packages that define a collection of Kubernetes resources required to run an application or service. You use Helm to define, install, and perform upgrades to your applications on Kubernetes.

For organizations looking to deploy their Chainguard container images with Helm, Chainguard provides upstream-produced Helm charts. These charts are available from the Chainguard Registry and are intended for customers who are either looking to get started with Helm or are looking for better, trusted alternatives to the public charts they may already be using.

> Chainguard also offers a limited set of Helm charts to go with a set of Chainguard-created containers labeled as iamguarded, designed specifically to support organizations migrating off of Bitnami. Learn more about these in [How to use Chainguard iamguarded Helm Charts](/chainguard/chainguard-images/how-to-use/use-chainguard-iamguarded-helm-charts/).

The community charts have been tested by Chainguard to confirm they produce expected deployment results using the following policies:

- Version streaming: Chainguard commits to supporting chart and image versions that match the latest upstream project chart. Within that latest chart we will support the associated image versions.
- Testing policy: We test the latest charts with the supported version streams and functionally validate by deploying the Helm chart in its representative environment and exercising the various functionality of the chart(s). We’ll also continue publishing end-of-life (EOL) version streams as long as they continue to pass our functional validation.

Chainguard makes the provenance of these charts clear. Helm charts are packaged as [OCI artifacts](/open-source/oci/what-are-oci-artifacts/) using the upstream version adding an appended revision suffix for updates that include material changes to the chart; otherwise, tags will float based as their dependent images update. The OCI artifacts are signed and generate provenance attestations that link to the exact image digests used to ensure that all artifacts are cryptographically verifiable end-to-end for integrity and origin.

You can find Helm charts in the [Chainguard Console](/chainguard/chainguard-images/how-to-use/images-directory/#find-helm-charts-in-the-chainguard-console) and in the [Chainguard Directory](/chainguard/chainguard-images/how-to-use/chainguard-directory/#find-helm-charts-in-the-chainguard-directory).

The following is an instructional guide for Chainguard users that are looking for Helm charts to use with their Chainguard container images.


## Authentication

You will need to authenticate to pull charts. These instructions explain how to use charts and images with the `cgr.dev` repository. If you have mirrored or copied the charts and images to an organization-specific registry, you will need to adapt these instructions to authenticate to your registry, as appropriate.

This section presents multiple authentication methods:
- Use Helm values with `global.imagePullSecrets`
- Deploy a Chainguard Helm chart using a Kubernetes pull secret
- Use cluster node-scoped registry permissions


### Use Helm values with `global.imagePullSecrets`

When performing authentication via a `global.imagePullSecrets` key-value pair, include the following in your `values.yaml` file.

```yaml
global:
  imagePullSecrets:
    - name: chainguard-pull-secret
```


### Deploy a Chainguard Helm chart using a Kubernetes pull secret

To begin, authenticate with chainctl and generate a pull token.

```sh
chainctl auth login
chainctl auth configure-docker --pull-token --save --ttl=24h
```

This token expires in 24 hours by default, which can be modified using the
`--ttl` flag. It sets the duration for the validity of the token. The maximum
valid value is `8760h` (equivalent to 365 days), Valid unit strings range from
nanoseconds to hours and are `ns`, `us`, `ms`, `s`, `m`, and `h`, for example
`--ttl=24h`.

Find the username and password that are contained in the pull token, as in this sample output:

```sh
chainctl auth configure-docker --pull-token --save --ttl=24h
                                    
  ✔ Selected folder chainguard.edu.

To use this pull token in another environment, run this command:

    docker login "cgr.dev" --username "45a0c61ea6fd977f050c5fb9ac06a69eed764595/095b0c7ea9d68679" --password "eyJhbGciOiJSUzI1NiJ9.eyJhdWQ... # Token truncated"

Configuring identity "45a0c61ea6fd977f050c5fb9ac06a69eed764595/095b0c7ea9d68679" for pulls from cgr.dev (expires 2025-06-12T09:27:45-05:00).
Overwriting existing credentials.
```

Save the credentials as variables, like this.

```sh
HELMUSER=45a0c61ea6fd977f050c5fb9ac06a69eed764595/095b0c7ea9d68679

HELMPASS=eyJhbGciOiJSUzI1NiJ9.eyJhdWQ... # Token truncated
```

Create your Kubernetes secret using the variables you just created.	

```sh
kubectl create secret docker-registry chainguard-pull-secret \
  --docker-server=cgr.dev \
  --docker-username=$(echo $HELMUSER) \
  --docker-password=$(echo $HELMPASS) \
  -n <your-namespace>
```

Log in to the `cgr.dev` Helm registry.

```sh
helm registry login cgr.dev \
  --username=$HELMUSER \
  --password=$HELMPASS
```

Reference the secret in your Helm installation:

```sh
helm install grafana oci://cgr.dev/$ORGANIZATION/charts/grafana \
  --set "global.org=$ORGANIZATION" \
  --set "global.imagePullSecrets[0].name=chainguard-pull-secret"
```


When the install is successful, it returns a confirmation message, like this:

```sh
Pulled: cgr.dev/chainguard.edu/charts/grafana:10.5.13
Digest: sha256:2629f907b15f26c706b5668b5700340b851176a10f55cf709f89a3701f2b4220
NAME: grafana
LAST DEPLOYED: Thu Jan 29 08:19:23 2026
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get your 'admin' user password by running:

   kubectl get secret --namespace default grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo


2. The Grafana server can be accessed via port 80 on the following DNS name from within your cluster:

   grafana.default.svc.cluster.local

   Get the Grafana URL to visit by running these commands in the same shell:
     export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=grafana" -o jsonpath="{.items[0].metadata.name}")
     kubectl --namespace default port-forward $POD_NAME 3000

3. Login with the password from step 1 and the username: admin
#################################################################################
######   WARNING: Persistence is disabled!!! You will lose your data when   #####
######            the Grafana pod is terminated.                            #####
#################################################################################
```


### Use cluster node-scoped registry permissions

If you manage access and permissions at cluster-wide and node-specific levels, these are some best practices to consider.

**Pin to tag:** The best practice for community charts is to pin to the image tag, like this:

```sh
helm install grafana oci://cgr.dev/$ORGANIZATION/charts/grafana --version 10.5.13 \
  --set "global.org=$ORGANIZATION"
```

**Review Default Values:** The chart provides security-minded defaults that are sensible but may not suit all use cases. Review the chart's `values.yaml` for the full range of configuration options and adjust as needed.


## Helm chart usage examples

### Install with details in a file

You can put values in a file, such as our `values.yaml` sample, and then refer to the file in your install command by passing the detail in a flag.

```sh
image:
  registry: cgr.dev
  repository: $ORGANIZATION/grafana # replace $ORGANIZATION
  tag: latest # pin to specific version instead of latest
```

Then you refer to the file like this:

```sh
helm install grafana oci://cgr.dev/$ORGANIZATION/charts/grafana \
  --values ./values.yaml
```


### Install on AWS Elastic Kubernetes Service (EKS) Auto Mode
When installing on EKS Auto Mode, you may need to create a storage class for the Helm chart's pod(s). This can be done by creating a storage class:

```sh
cat <<EOF | kubectl apply -f -
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: gp3-automode
provisioner: ebs.csi.eks.amazonaws.com
parameters:
  type: gp3
  encrypted: "true"
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
EOF
```

You then pass the storage class's name to the `helm install` command. Here, we use `grafana` as an example:

```sh
helm install grafana oci://cgr.dev/$ORGANIZATION/charts/grafana \
  --set "global.imagePullSecrets[0].name=chainguard-pull-secret" \
  --set "persistence.storageClass=gp3-automode"
```


## Troubleshooting 

To check the Helm configuration, you can run `helm install` with `--dry-run` flag. This will output the generated Kubernetes YAML. Double check the values for the image and `imagePullSecrets` to ensure they point to the correct registry and authentication is in place.

To see the files, run:

```sh
helm pull --untar oci://cgr.dev/$ORGANIZATION/charts/grafana \
```

To get the `values.yaml` so you can examine it, run:

```sh
helm show values oci://cgr.dev/$ORGANIZATION/charts/grafana \
```

See the [Helm commands documentation](https://helm.sh/docs/helm/) for more information.
