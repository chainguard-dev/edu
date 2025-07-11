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

Previously, Chainguard created containers specially designed for compatibility with community Helm charts to deliver added benefits to customers already using those charts. We are now publishing our own collection of Helm charts, labeled as “iamguarded,” that come configured out-of-the box to be compatible with Chainguard Container Images.

Chainguard’s `iamguarded`-labeled Helm charts take the place of the earlier methods and the charts are pulled directly from Chainguard. This new experience makes the provenance of these charts clear, and comes with the added benefit that they are designed to work with your Chainguard images.

The following is an instruction guide for Chainguard users that were previously using community charts with Chainguard images to migrate over to the new `iamguarded` charts.


## Configuration Requirements

A `global.org` value is required. You can set this using a `--set` flag during installation, like in our first example below, or in a file, like in our sample `values.yaml` in the second example.

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


### Use Helm values with `global.imagePullSecrets`

Include this in your `values.yaml` file.

```yaml
global:
  imagePullSecrets:
    - name: chainguard-pull-secret
```


### Deploy a Chainguard Helm chart using a Kubernetes pull secret

1. Authenticate with chainctl and generate a pull token

    ```sh
    chainctl auth login
    chainctl auth configure-docker --pull-token --save --ttl=24h
    ```

    This creates a short-lived pull token (24 hours). Change the `ttl=` switch to adjust how long your token will exist.

2. Find the username and password that are contained in the pull token, as in this sample output:

    ```sh
    chainctl auth configure-docker --pull-token --save --ttl=24h
                                        
      ✔ Selected folder chainguard.edu.

    To use this pull token in another environment, run this command:

        docker login "cgr.dev" --username "45a0c61ea6fd977f050c5fb9ac06a69eed764595/095b0c7ea9d68679" --password "eyJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJodHRwczovL2lzc3Vlci5lbmZvcmNlLmRldiIsImV4cCI6MTc0OTczODQ2NSwiaWF0IjoxNzQ5NjUyMDY2LCJpc3MiOiJodHRwczovL3B1bGx0b2tlbi5pc3N1ZXIuY2hhaW5ndWFyZC5kZXYiLCJzdWIiOiJwdWxsLXRva2VuLTAxY2MwODkwYzA5N2ZmMzk1MDUyMWY4NWFmYmEyZDUwMGM0ODQxOWEifQ.ET7ywPUkMk5wN6p0INqhNtdnOVELySqdjp-qWedVmJkLrWlZhdFodU43P4uuR-LJ3Z9mVmd9fjDWpBtZnsCFHbczkENPzOiAFP9fsJhO_2dXT3rXCPK84ddJgRLe6oDlMA3VSa0XEclfTyBcaG4RlrgkVaGhtS7gone4Egff7bKX5Y6-TUxxLiVvCA_l_YmOixUss_Mj1Qxxb81sCeh7x4FSpOGWtmU2Z7Hy6B_rGk17zXMO_GYcuyzAMxfFdQl1Ov18t7KxymQwIoS7UF1fx_5ECR8fgArLM8NikGOjzkiQZuSzeI_hl_GnUFdPTAAhmjpJEWO0isiSPWgpkUPx5scoSUm6jzfduvRgGcmjRxT_pq6MWzFJNw9gv9gVehJuW5lKzNIgMTfJXO5Roba8WCwwxiUknhZXP8DeD_kdAN2-JbkfOYg3aPVU5jFTtA6TJKlh0uQA5OGN5hG_PnyzIr0vu4VVninJTWm66RppdlffhG-1xY9lpXgD2k2TIhygFL8iEBNszq0siLVA3uTH6NZY8iGRFqziUAGnyD80aHn52tIeCBBAOyS6qfcRLzqO6dQX95uscdCOuy-5rxU9n4208m5duLXdZtVWa9gp2vg-OmxnCPVdXmPCTA6RF43gDVkxKGMfvkUkTW1nKNvIUx_ikC9tLHDuZdi8FKLeYEg"

    Configuring identity "45a0c61ea6fd977f050c5fb9ac06a69eed764595/095b0c7ea9d68679" for pulls from cgr.dev (expires 2025-06-12T09:27:45-05:00).
    Overwriting existing credentials.
    ```

    Save the credentials as variables, like this.

    ```sh
    HELMUSER=45a0c61ea6fd977f050c5fb9ac06a69eed764595/095b0c7ea9d68679

    HELMPASS=eyJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJodHRwczovL2lzc3Vlci5lbmZvcmNlLmRldiIsImV4cCI6MTc0OTczODQ2NSwiaWF0IjoxNzQ5NjUyMDY2LCJpc3MiOiJodHRwczovL3B1bGx0b2tlbi5pc3N1ZXIuY2hhaW5ndWFyZC5kZXYiLCJzdWIiOiJwdWxsLXRva2VuLTAxY2MwODkwYzA5N2ZmMzk1MDUyMWY4NWFmYmEyZDUwMGM0ODQxOWEifQ.ET7ywPUkMk5wN6p0INqhNtdnOVELySqdjp-qWedVmJkLrWlZhdFodU43P4uuR-LJ3Z9mVmd9fjDWpBtZnsCFHbczkENPzOiAFP9fsJhO_2dXT3rXCPK84ddJgRLe6oDlMA3VSa0XEclfTyBcaG4RlrgkVaGhtS7gone4Egff7bKX5Y6-TUxxLiVvCA_l_YmOixUss_Mj1Qxxb81sCeh7x4FSpOGWtmU2Z7Hy6B_rGk17zXMO_GYcuyzAMxfFdQl1Ov18t7KxymQwIoS7UF1fx_5ECR8fgArLM8NikGOjzkiQZuSzeI_hl_GnUFdPTAAhmjpJEWO0isiSPWgpkUPx5scoSUm6jzfduvRgGcmjRxT_pq6MWzFJNw9gv9gVehJuW5lKzNIgMTfJXO5Roba8WCwwxiUknhZXP8DeD_kdAN2-JbkfOYg3aPVU5jFTtA6TJKlh0uQA5OGN5hG_PnyzIr0vu4VVninJTWm66RppdlffhG-1xY9lpXgD2k2TIhygFL8iEBNszq0siLVA3uTH6NZY8iGRFqziUAGnyD80aHn52tIeCBBAOyS6qfcRLzqO6dQX95uscdCOuy-5rxU9n4208m5duLXdZtVWa9gp2vg-OmxnCPVdXmPCTA6RF43gDVkxKGMfvkUkTW1nKNvIUx_ikC9tLHDuZdi8FKLeYEg
    ```

3. Create the Kubernetes secret using the variables you just created.	

    ```sh
    kubectl create secret docker-registry chainguard-pull-secret \
      --docker-server=cgr.dev \
      --docker-username=$(echo $HELMUSER) \
      --docker-password=$(echo $HELMPASS) \
      -n <your-namespace>
    ```

4. Log in to the `cgr.dev` Helm registry

    ```sh
    helm registry login cgr.dev \
      --username=$HELMUSER \
      --password=$HELMPASS
    ```

5. Reference the secret in your Helm installation

    ```sh
    helm install rabbitmq oci://cgr.dev/$ORGANIZATION/iamguarded-charts/rabbitmq \
      --set "global.org=$ORGANIZATION" \
      --set "global.imagePullSecrets[0].name=chainguard-pull-secret"
    ```


When the install is successful, you will see something like this:

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

Here are some best practices, if you go this route.

**Pin to Digest:** While charts follow the same tagging scheme as Chainguard images, always pin to a specific chart digest to prevent unexpected updates:

```sh
helm install rabbitmq \ 
oci://cgr.dev/$ORGANIZATION/iamguarded-charts/rabbitmq@sha256:DIGEST \
     --set "global.org=$ORGANIZATION"
```

**Review Default Values:** The chart provides security-minded defaults that are sensible but may not be production-ready for all use cases. Review the chart's `values.yaml` for the full range of configuration options.

**Use Image Pinning:** All `iamguarded` charts pin images to specific digests that have been tested for compatibility, ensuring reliable deployments.


## Example Usage

### Install with details passed in a flag

To install an `iamguarded` Helm chart, use standard Helm commands like this example, substituting your organization for `$ORGANIZATION`.

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
