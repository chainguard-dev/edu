---
title: "Getting Started with the Chainguard Istio Images"
type: "article"
linktitle: "Istio"
description: "Tutorial on how to get started with the Chainguard Istio Images"
date: 2023-12-14T00:00:00+00:00
lastmod: 2023-09-22T11:07:52+02:00
tags: ["Chainguard Images", "Products"]
draft: false
images: []
menu:
  docs:
    parent: "getting-started"
weight: 610
toc: true
---

[Istio](https://istio.io) extends Kubernetes to establish a programmable,
application-aware network using the powerful Envoy service proxy. Working with
both Kubernetes and traditional workloads, Istio brings standard, universal
traffic management, telemetry, and security to complex deployments. Chainguard
offers a set of minimal, security-hardened Istio images, built on top the Wolfi
OS.

We will demonstrate how to get started with the Chainguard Istio images on an
example KinD cluster. To get started, you'll need Docker, KinD, `kubectl`, and `istioctl`
installed.

* [Docker](https://docs.docker.com/get-docker/)
* [KinD](https://kind.sigs.k8s.io/docs/user/quick-start/)
* [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
* [istioctl](https://istio.io/latest/docs/setup/getting-started/#download)


{{< details "What is Wolfi" >}}
{{< blurb/wolfi >}}
{{< /details >}}

{{< details "Chainguard Images" >}}
{{< blurb/images >}}
{{< /details >}}

## Start up a KinD cluster

First, we'll start up a KinD cluster to install Istio
```sh
kind create cluster
```

This will return output similar to the following:
```
Creating cluster "kind" ...
 ✓ Ensuring node image (kindest/node:v1.27.3) 🖼 
 ✓ Preparing nodes 📦  
 ✓ Writing configuration 📜 
 ✓ Starting control-plane 🕹️ 
 ✓ Installing CNI 🔌 
 ✓ Installing StorageClass 💾 
Set kubectl context to "kind-kind"
You can now use your cluster with:

kubectl cluster-info --context kind-kind

Thanks for using kind! 😊
```

## Install Istio using Chainguard Images

We will be using the `istioctl` command to install Istio. In order to use the
Chainguard images, we will need to set these following values:
- `hub = cgr.dev/chainguard`
- `tag = latest`
- `values.pilot.image = istio-pilot`
- `values.global.proxy.image = istio-proxy`
- `values.global.proxy_init.image = istio-proxy`

Those translate to the following `istioctl` command:
```
istioctl install --set tag=latest --set hub=cgr.dev/chainguard \
  --set values.pilot.image=istio-pilot \
  --set values.global.proxy.image=istio-proxy \
  --set values.global.proxy_init.image=istio-proxy
```

## Stand up a Gateway and a VirtualService 

To see the Istio installation in action, we will create two Istio resources:
* An Istio gateway serving the "http://hello.example.com" domain
* A VirtualService to always reply with "Hello, world!" to requests to the
  "http://hello.example.com" domain 

Create a YAML manifest file with the following contents to define the Istio resources: 
```sh
cat > example.yaml <<EOF
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: sample-gateway
spec:
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - "hello.example.com"
---
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: sample-virtual-service
spec:
  gateways:
  - sample-gateway
  hosts:
  - "hello.example.com"
  http:
  - directResponse:
      status: 200
      body:
        string: "Hello, world!\n"
EOF
```

Apply the YAML file to the cluster:
```sh
kubectl apply -f example.yaml
```

Now, in one terminal, start a port-forward to the Istio Ingress Gateway:
```
kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80
```

In another terminal, send a request to the Istio Ingress Gateway:
```
curl -H "Host: hello.example.com" localhost:8080
```
You should see `Hello, world!` output to the terminal.

## Clean up your KinD cluster 

Once you are done, you can delete your KinD cluster with `kind delete cluster`.
