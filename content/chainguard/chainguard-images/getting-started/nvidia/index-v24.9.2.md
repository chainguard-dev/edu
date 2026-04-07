---
title: "Getting Started with the NVIDIA Container Toolkit Chainguard Container"
type: "article"
linktitle: "NVIDIA Container Toolkit"
aliases:
- /chainguard/chainguard-images/getting-started/getting-started-nvidia-container-toolkit
description: "Learn how to deploy NVIDIA Container Toolkit on GKE using Chainguard's security-hardened container image and the NVIDIA GPU Operator Helm chart"
date: 2026-03-16T00:00:00+00:00
lastmod: 2026-03-16T00:00:00+00:00
tags: ["Chainguard Containers"]
draft: false
images: []
menu:
  docs:
    parent: "getting-started"
weight: 035
toc: true
---

Chainguard's [NVIDIA Container Toolkit container image](https://images.chainguard.dev/directory/image/nvidia-container-toolkit/overview) provides a security-hardened foundation for enabling GPU workloads in Kubernetes with significantly fewer vulnerabilities than the upstream image. The [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html) configures the container runtime on each node so that GPU devices are visible and accessible inside containers. Built on Wolfi OS, Chainguard's minimal image integrates seamlessly with the NVIDIA GPU Operator, which manages the full lifecycle of GPU drivers, plugins, and tooling in a Kubernetes cluster.

This guide demonstrates how to deploy the Chainguard NVIDIA Container Toolkit image on a Google Kubernetes Engine (GKE) cluster using the [NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html) Helm chart. The steps follow the [official NVIDIA GKE installation guide](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/google-gke.html).

{{< blurb/free-tier-message >}}

{{< details "What is Wolfi" >}}
{{< blurb/wolfi >}}
{{< /details >}}

{{< details "Chainguard Containers" >}}
{{< blurb/images >}}
{{< /details >}}

## Prerequisites

You will need the following tools installed before proceeding:

- [gcloud CLI](https://cloud.google.com/sdk/docs/install) — for creating and managing GKE clusters
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) — for interacting with the Kubernetes API
- [Helm](https://helm.sh/docs/intro/install/) — for installing the GPU Operator chart

You will also need a Google Cloud project with the GKE API enabled and sufficient quota to provision a GPU node. This guide uses an `nvidia-tesla-t4` GPU in the `us-west1-a` zone.

## Set Environment Variables

The commands in this guide reference two environment variables. Set them now so you can copy and paste commands directly:

```shell
export PROJECT=<your-gcp-project-id>
export ORGANIZATION=<your-chainguard-organization>
```

`PROJECT` is your Google Cloud project ID, and `ORGANIZATION` is your organization's repository name within the Chainguard registry (for example, `cgr.dev/example.com` would use `example.com`).

## Create a GKE Cluster

Create a single-node GKE cluster with a GPU-attached node pool. The `--accelerator` flag attaches one NVIDIA Tesla T4 GPU to each node, and `UBUNTU_CONTAINERD` is required as the node image type for GPU Operator compatibility. The `gpu-driver-version=disabled` option prevents GKE from auto-installing NVIDIA drivers, allowing the GPU Operator to manage the driver lifecycle instead.

```shell
gcloud beta container clusters create gpu-cluster \
    --project $PROJECT \
    --zone us-west1-a \
    --release-channel "regular" \
    --machine-type "n1-standard-4" \
    --accelerator "type=nvidia-tesla-t4,count=1,gpu-driver-version=disabled" \
    --image-type "UBUNTU_CONTAINERD" \
    --disk-type "pd-standard" \
    --disk-size "30" \
    --no-enable-intra-node-visibility \
    --metadata disable-legacy-endpoints=true \
    --max-pods-per-node "110" \
    --num-nodes "1" \
    --logging=SYSTEM,WORKLOAD \
    --monitoring=SYSTEM \
    --enable-ip-alias \
    --default-max-pods-per-node "110" \
    --no-enable-master-authorized-networks \
    --tags=nvidia-ingress-all
```

Once the cluster is ready, fetch credentials so `kubectl` can communicate with it:

```shell
gcloud container clusters get-credentials gpu-cluster \
    --zone us-west1-a \
    --project $PROJECT
```

## Apply the GPU Operator ResourceQuota

The GPU Operator runs several components with elevated priority classes (`system-node-critical` and `system-cluster-critical`). GKE enforces a default quota on pods using these classes, so you need to create the `gpu-operator` namespace and apply a `ResourceQuota` to it before installing the Operator.

```shell
kubectl create namespace gpu-operator
```

```shell
cat <<EOF | kubectl apply -n gpu-operator -f -
apiVersion: v1
kind: ResourceQuota
metadata:
  name: gpu-operator-quota
spec:
  hard:
    pods: 100
  scopeSelector:
    matchExpressions:
    - operator: In
      scopeName: PriorityClass
      values:
        - system-node-critical
        - system-cluster-critical
EOF
```

## Configure Registry Credentials

The Chainguard NVIDIA Container Toolkit image is hosted in a private registry and requires authentication. You need to create an image pull secret in the `gpu-operator` namespace so that GKE nodes can pull the image.

Create a pull secret in the `gpu-operator` namespace using a short-lived token from `chainctl`:

```shell
kubectl create secret docker-registry chainguard-pull-secret \
    --docker-server=cgr.dev \
    --docker-username=_token \
    --docker-password=$(chainctl auth token --audience=cgr.dev) \
    -n gpu-operator
```

> **Note**: The token embedded in this secret expires after approximately one hour. For production use, create a long-lived [pull token](https://edu.chainguard.dev/chainguard/chainguard-images/pulling-images-overview/) and use its credentials in place of `_token` and the `chainctl auth token` output.

## Configure Helm Values

Create a `values.yaml` file that points the GPU Operator's toolkit component to the Chainguard image. Be sure to change `$ORGANIZATION` to reflect your organization's repository within the Chainguard registry:

```shell
cat <<EOF > values.yaml
toolkit:
  repository: cgr.dev/$ORGANIZATION
  image: nvidia-container-toolkit
  version: latest
  imagePullSecrets:
    - chainguard-pull-secret
EOF
```

This overrides only the toolkit image. All other GPU Operator components (driver daemonset, device plugin, DCGM exporter, etc.) continue to use their default upstream images.

## Install the GPU Operator

Add the NVIDIA Helm repository and install the GPU Operator into a dedicated namespace, passing in the values file you created above:

```shell
helm repo add nvidia https://nvidia.github.io/gpu-operator
helm upgrade --install gpu-operator nvidia/gpu-operator \
    --version v24.9.2 \
    -n gpu-operator \
    --create-namespace \
    -f values.yaml
```

> **Note**: For the first few minutes after installation, only the `gpu-operator-node-feature-discovery-*` workloads will be running. The GPU Operator initializes and validates each component sequentially before creating the remaining workloads. Allow approximately 10 minutes for all Pods to reach `Running` state.

## Verify the Installation

Run the following command to watch the GPU Operator workloads come up:

```shell
watch kubectl get daemonsets,deployments -n gpu-operator
```

When all workloads are healthy, you should see output similar to the following:

```
NAME                                                DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR
gpu-feature-discovery-k8q6x                         1/1       Running   0       5m43s
gpu-operator-7bbf8bb6b7-g7z99                       1/1       Running   0       6m10s
gpu-operator-node-feature-discovery-gc-...          1/1       Running   0       8m55s
gpu-operator-node-feature-discovery-master-...      1/1       Running   0       8m55s
gpu-operator-node-feature-discovery-worker-...      1/1       Running   0       8m55s
nvidia-container-toolkit-daemonset-sscl9            1/1       Running   0       5m43s
nvidia-cuda-validator-95ph2                         0/1       Completed 0       42s
nvidia-dcgm-exporter-2jfqc                          1/1       Running   0       5m43s
nvidia-device-plugin-daemonset-2t62r                1/1       Running   0       5m43s
nvidia-driver-daemonset-9cnfm                       1/1       Running   0       5m59s
nvidia-operator-validator-zt2mt                     1/1       Running   0       5m43s
```

The `nvidia-cuda-validator` pod is expected to show `Completed` — it runs a one-time CUDA validation job and exits successfully when the GPU is accessible.

Press `Ctrl+C` to exit the watch once all Pods are in the expected state.

## Check the Toolkit Logs

Before checking logs, confirm the toolkit pod is in `Running` state:

```shell
kubectl get pods -n gpu-operator -l app=nvidia-container-toolkit-daemonset
```

If the pod is still in `Init` state, wait for it to finish initializing before proceeding.

Once the pod is `Running`, inspect the logs of the toolkit daemonset:

```shell
kubectl logs daemonset/nvidia-container-toolkit-daemonset \
    -c nvidia-container-toolkit-ctr \
    -n gpu-operator \
    --follow
```

A healthy initialization produces output similar to the following:

```
time="2024-05-03T17:25:19Z" level=info msg="Starting nvidia-toolkit"
time="2024-05-03T17:25:19Z" level=info msg="Installing toolkit"
time="2024-05-03T17:25:19Z" level=info msg="Installing NVIDIA container toolkit to '/usr/local/nvidia/toolkit'"
time="2024-05-03T17:25:19Z" level=info msg="Installing NVIDIA container library to '/usr/local/nvidia/toolkit'"
...
time="2024-05-03T17:25:19Z" level=info msg="Completed 'setup' for containerd"
time="2024-05-03T17:25:19Z" level=info msg="Waiting for signal"
```

The final line, `Waiting for signal`, indicates that the toolkit has been installed successfully and the daemonset is idle, waiting for a restart or shutdown signal. If you see errors in the logs, refer to the [NVIDIA GPU Operator troubleshooting guide](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/troubleshooting.html).

## Clean Up

When you are done, delete the GKE cluster to avoid incurring further charges:

```shell
gcloud container clusters delete gpu-cluster \
    --zone us-west1-a \
    --project $PROJECT
```

## Advanced Usage

{{< blurb/images-advanced image="NVIDIA Container Toolkit" >}}
