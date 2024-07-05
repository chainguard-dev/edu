---
title: "Image Overview: whereabouts"
linktitle: "whereabouts"
type: "article"
layout: "single"
description: "Overview: whereabouts Chainguard Image"
date: 2024-07-05 00:42:00
lastmod: 2024-07-05 00:42:00
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/whereabouts/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/whereabouts/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/whereabouts/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/whereabouts/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->

Whereabouts is a simple IPAM (IP Address Management) solution for Kubernetes. To get more information about Whereabouts, please visit the [official project repository](https://github.com/k8snetworkplumbingwg/whereabouts).

<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/whereabouts:latest
```


<!--body:start-->

## Usage

There is an official [Whereabouts documentation](https://github.com/k8snetworkplumbingwg/whereabouts/#installation) that provides detailed information on how to deploy and configure Whereabouts.

To deploy whereabouts, you can use the manifests available in the official repository at ./docs/crds folder.

```bash
git clone https://github.com/k8snetworkplumbingwg/whereabouts && cd whereabouts
kubectl apply \
    -f doc/crds/daemonset-install.yaml \
    -f doc/crds/whereabouts.cni.cncf.io_ippools.yaml \
    -f doc/crds/whereabouts.cni.cncf.io_overlappingrangeipreservations.yaml
```

Then patch the image to use the Chainguard image:

```bash
kubectl -n kube-system patch daemonset whereabouts --type='json' -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/imagePullPolicy", "value":"IfNotPresent"}]'
kubectl -n kube-system set image daemonset/whereabouts whereabouts=cgr.dev/chainguard/whereabouts:latest
```

To test the deployment, you can create a pod with a network attachment definition:

> **Note:** The following example assumes you have deployed multus cni in your cluster. If you haven't, you can follow the instructions in the official repository at [k8snetworkplumbingwg/multus-cni](https://github.com/k8snetworkplumbingwg/multus-cni).

```bash
cat <<'EOF' | kubectl apply -f -
apiVersion: "k8s.cni.cncf.io/v1"
kind: NetworkAttachmentDefinition
metadata:
  name: whereabouts-conf
spec:
  config: '{
      "cniVersion": "0.3.0",
      "name": "whereaboutsexample",
      "type": "macvlan",
      "master": "eth0",
      "mode": "bridge",
      "ipam": {
        "type": "whereabouts",
        "range": "192.168.2.225/28"
      }
    }'
EOF
```

Then create a deployment that uses the network attachment definition:

```bash
cat <<'EOF' | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: netshoot-deployment
  labels:
    app: netshoot-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: netshoot-pod
  template:
    metadata:
      annotations:
        k8s.v1.cni.cncf.io/networks: whereabouts-conf
      labels:
        app: netshoot-pod
    spec:
      containers:
      - name: netshoot
        image: nicolaka/netshoot
        command:
          - sleep
          - "3600"
        imagePullPolicy: IfNotPresent
EOF
```

After creating the deployment, you should see a pod running:

```bash
$ k get po
NAME                                  READY   STATUS    RESTARTS   AGE
netshoot-deployment-8dcd8565b-zm49h   1/1     Running   0          45m
```

Then you can exec into the pod and check the IP address:

```bash
$ k exec -it netshoot-deployment-8dcd8565b-zm49h -- ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host proto kernel_lo
       valid_lft forever preferred_lft forever
2: eth0@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 12:27:a2:24:3a:10 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.244.2.2/24 brd 10.244.2.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::1027:a2ff:fe24:3a10/64 scope link proto kernel_ll
       valid_lft forever preferred_lft forever
3: net1@if7: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 2a:d2:d1:26:b3:3c brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 192.168.2.225/28 brd 192.168.2.239 scope global net1
       valid_lft forever preferred_lft forever
    inet6 fe80::28d2:d1ff:fe26:b33c/64 scope link proto kernel_ll
       valid_lft forever preferred_lft forever
```

Voila! You have successfully deployed Whereabouts and assigned an IP address to a pod.

<!--body:end-->

