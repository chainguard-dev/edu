---
title: "How to Enable Annotation-based Caching for Chainguard Enforce"
type: "article"
description: "Enabling annotation-based caching for Chainguard Enforce"
date: 2022-07-15T15:22:20+01:00
lastmod: 2023-01-12T15:22:20+01:00
draft: false
tags: ["Enforce", "Product", "Procedural"]
images: []
menu:
  docs:
    parent: "chainguard-enforce-kubernetes"
weight: 100
toc: true
---

> _This document relates to Chainguard Enforce. In order to follow along, you will need access to Chainguard Enforce. You can request access by selecting **Chainguard Enforce for Kubernetes** on the [inquiry form](https://www.chainguard.dev/get-demo?utm_source=docs)._

Chainguard Enforce for Kubernetes can leverage annotations on Kubernetes objects to cache verification results to reduce the amount of traffic made to container registries in order to improve latency and scalability of the admission webhook.

This feature will soon be the default for all users. In the meantime, in order to try out this feature on your Kubernetes cluster, you can use a feature flag setting in the ConfigMap `config-policy-controller` within the `cosign-system` namespace.

## Understanding Annotation-based Caching

Because a Kubernetes Pod usually receives most of its images passed down from parent objects like `StatefulSets` or `ReplicaSets`, enabling annotation-based caching allows for the verification results from parent objects to be passed down to Pods. This reduces the traffic made to container registries, reducing latency and making policy enforcement much more scalable.

In Chainguard's own load testing annotation-based caching, with a cache hit we obtained P99 verification latency of under two seconds (meaning that 99% of the requests were within this timeframe), and no egress was made to container registry. Without caching, latency would be highly dependent of registry access latency, where the P99 latency may be ten seconds or more. 

Additionally, there are safeguards in place to make sure that cache annotation values are tamper proof. Chainguard includes a cryptographic signature inside the cache annotation and verifies that this is in place upon rereading. Invalid caches will be discarded.

## Turn on Annotation-based Caching

In order to turn on annotation-based caching in Chainguard Enforce, you first need to create the ConfigMap `config-policy-controller` if it does not exist.

```sh
kubectl create cm config-policy-controller -n cosign-system --dry-run=client -o yaml | kubectl apply -f -
```

Next, set the enable cache flag.


```sh
kubectl patch cm config-policy-controller -n cosign-system --type merge \
    -p '{"data":{"dev.chainguard.enable-cip-cache":"true"}}'
```

To turn annotation-based caching off, remove the setting from the ConfigMap, or set it to `false`.

## Confirm that Annotation-based Caching is Enabled

After enabling annotation-based caching, any new verification going through the Chainguard Enforce admission webhook will have an additional annotation similar to this:

```sh
apiVersion: v1
kind: Pod
metadata:
  annotations:
    clusterimagepolicies.chainguard.dev/cache: |
      records:
          docker.io/image@sha256:digest:
              f1f40fab-2bec-4d29-856d-b75ce7d1ec40:
                  name: policy-name
                  resourceversion: "4943109"
                  ...
      signature: eyJhbGciOi...
```

Your annotation value and format may be slightly different. The important information includes the validation results of the Pod's images against the different policies, as well as a cryptographic signature confirming the authenticity of the cache.
