---
title: "How to Use Chainguard iamguarded Helm Charts"
linktitle: "Using Chainguard Helm Charts"
aliases:
type: "article"
description: "A primer on how to use the Chainguard-produced iamguarded Helm charts to deploy Chainguard container images"
lead: "A primer on how to use the Chainguard-produced iamguarded Helm charts to deploy Chainguard container images"
date: 2025-07-11T08:49:31+00:00
lastmod: 2025-07-11T08:49:31+00:00
draft: false
tags: ["Chainguard Containers", "Helm charts", "iamguarded", "Product"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 007
toc: true
---

[Helm](https://helm.sh) is the package manager for Kubernetes that simplifies the installation and management of applications by automating the creation of Kubernetes resources. Helm charts are reusable, versioned packages that define a collection of Kubernetes resources required to run an application or service. You use Helm to define, install, and perform upgrades to your applications on Kubernetes.

Previously, Chainguard created containers specially designed for compatibility with community Helm charts to deliver added benefits to customers already using those charts. We are now publishing our own collection of Helm charts, labeled as “iamguarded,” that come configured out-of-the box for use with Chainguard container images.

Chainguard’s `iamguarded`-labeled Helm charts take the place of the earlier methods and the charts are pulled directly from Chainguard. This new experience makes the provenance of these charts clear, and comes with the added benefit that they are designed to work with your Chainguard images.

The following is an instructional guide for Chainguard users that were previously using community charts with Chainguard images to migrate over to the new `iamguarded` charts as well as for those who wish to begin using Chainguard's `iamguarded` Helm charts.


## Configuration Requirements

If you are pulling container images directly from Chainguard, then you must set a `global.org` value. You don't need this if you are pulling from your own internal registry.

You can set a `global.org` value using a `--set` flag during installation, as shown in this example:

```sh
helm install rabbitmq oci://cgr.dev/$ORGANIZATION/iamguarded-charts/rabbitmq \
  --set "global.org=$ORGANIZATION"
```

Alternately, you can set this value in a YAML file:

```yaml
global:
  org: $ORGANIZATION
```

In addition, users who mirror images to custom repositories should use `global.imageRegistry` to override the default `cgr.dev`. If you have a complex mirroring strategy, consult the chart’s `values.yaml` for individual image configuration options including `registry`, `repository`, `tag` and `digest`. Here’s a sample from the RabbitMQ `iamguarded` chart documentation:

```yaml
image:
  registry: myregistry.example.com
  repository: mirrored/rabbitmq-iamguarded
  digest: sha256:... # Use specific digest instead of tag

# OS Shell image for volume permissions
volumePermissions:
  enabled: true
  image:
    registry: myregistry.example.com
    repository: mirrored/os-shell-iamguarded
    digest: sha256:... # Use specific digest instead of tag
```


## Authentication

You will need to authenticate to pull charts. These instructions explain how to use charts and images with the `cgr.dev` repository. If you have mirrored or copied the charts and images to an organization-specific registry, you will need to adapt these instructions to authenticate to your registry, as appropriate.

This section presents multiple authentication methods:
- Use Helm values with `gloal.imagePullSecrets`
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

Reference the secret in your Helm installation.

```sh
helm install rabbitmq oci://cgr.dev/$ORGANIZATION/iamguarded-charts/rabbitmq \
  --set "global.org=$ORGANIZATION" \
  --set "global.imagePullSecrets[0].name=chainguard-pull-secret"
```


When the install is successful, it returns a confirmation message, like this:

```sh
Pulled: cgr.dev/chainguard-private/iamguarded-charts/rabbitmq:16.0.2
Digest: sha256:cfc18fe651760c91c7596f7d9d44512b162f19e4bfd8ba81b5ff6cb6d8e61d6d
NAME: rabbitmq
LAST DEPLOYED: Mon Jun  9 08:35:39 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
CHART NAME: rabbitmq
CHART VERSION: 16.0.2
APP VERSION: 4.1.0** Please be patient while the chart is being deployed **

Credentials:
    echo "Username      : user"
    echo "Password      : $(kubectl get secret --namespace default rabbitmq -o jsonpath="{.data.rabbitmq-password}" | base64 -d)"
    echo "ErLang Cookie : $(kubectl get secret --namespace default rabbitmq -o jsonpath="{.data.rabbitmq-erlang-cookie}" | base64 -d)"

Note that the credentials are saved in persistent volume claims and will not be changed upon upgrade or reinstallation unless the persistent volume claim has been deleted. If this is not the first installation of this chart, the credentials may not be valid.
This is applicable when no passwords are set and therefore the random password is autogenerated. In case of using a fixed password, you should specify it when upgrading.
More information about the credentials may be found at https://docs.iamguarded.com/general/how-to/troubleshoot-helm-chart-issues/#credential-errors-while-upgrading-chart-releases.

RabbitMQ can be accessed within the cluster on port 5672 at rabbitmq.default.svc.cluster.local

To access for outside the cluster, perform the following steps:

To Access the RabbitMQ AMQP port:

    echo "URL : amqp://127.0.0.1:5672/"
    kubectl port-forward --namespace default svc/rabbitmq 5672:5672

To Access the RabbitMQ Management interface:

    echo "URL : http://127.0.0.1:15672/"
    kubectl port-forward --namespace default svc/rabbitmq 15672:15672

WARNING: There are "resources" sections in the chart not set. Using "resourcesPreset" is not recommended for production. For production installations, please set the following values according to your workload needs:
  - resources
+info https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
```


### Use cluster node-scoped registry permissions

If you manage access and permissions at cluster-wide and node-specific levels, these are some best practices to consider.

**Pin to Digest:** While charts follow the same tagging scheme as Chainguard images, always pin to a specific chart digest to prevent unexpected updates:

```sh
helm install rabbitmq \ 
oci://cgr.dev/$ORGANIZATION/iamguarded-charts/rabbitmq@sha256:DIGEST \
     --set "global.org=$ORGANIZATION"
```

**Review Default Values:** The chart provides security-minded defaults that are sensible but may not suit all use cases. Review the chart's `values.yaml` for the full range of configuration options and adjust as needed.

**Use Image Pinning:** All `iamguarded` charts pin images to specific digests that have been tested for compatibility, ensuring reliable deployments.


## Helm chart usage examples

### Install with details passed in a flag

To install an `iamguarded` Helm chart using standard Helm commands and passing details as flag values in the command itself, add the flags and values at the end like this example, substituting your organization for `$ORGANIZATION`.

```sh
helm install rabbitmq oci://cgr.dev/$ORGANIZATION/iamguarded-charts/rabbitmq \
 --set "global.org=$ORGANIZATION"
```

### Install with details in a file

Alternatively, you can put values in a file, such as our `values.yaml` sample, and then refer to the file in your install command.

```sh
image:
  registry: cgr.dev
  repository: $ORGANIZATION/rabbitmq # replace $ORGANIZATION
  tag: latest # pin to specific version instead of latest
```

Then you refer to the file like this:

```sh
helm install test oci://cgr.dev/chainguard-private/iamguarded-charts/rabbitmq --values ./values.yaml
```

## Troubleshooting 

To check the Helm configuration, you can run `helm install` with `--dry-run` flag. This will output the generated Kubernetes YAML. Double check the values for the image and `imagePullSecrets` to ensure they point to the correct registry and authentication is in place.

To see the files, run:

```sh
helm pull --untar oci://cgr.dev/chainguard-private/iamguarded-charts/rabbitmq
```

To get the `values.yaml` so you can examine it, run:

```sh
helm show values oci://cgr.dev/chainguard-private/iamguarded-charts/rabbitmq
```

See the [Helm commands documentation](https://helm.sh/docs/helm/) for more information.
