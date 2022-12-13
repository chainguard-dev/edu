---
title: "Enabled Annotation-based Caching for Chainguard Enforce"
type: "article"
description: "How to enable annotation-based caching for Chainguard Enforce"
date: 2022-07-15T15:22:20+01:00
lastmod: 2022-11-29T15:22:20+01:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-enforce-kubernetes"
weight: 100
toc: true
---

Chainguard Enforce for Kubernetes has a new feature that leverage annotations on Kubernetes object to cache verification results to reduce the amount of traffic made to Container Registries to improve latency and scalability of the admission webhook.

This feature will eventually be the default for all users, but in the mean time, in order to try out this feature on your Kubernetes cluster you can use a feature flag setting in the Config Map `config-policy-controller` in the `cosign-system` namespace.

```sh
# Create the Config Map `config-policy-controller` if it does not exist
kubectl create cm config-policy-controller -n cosign-system --dry-run=client -o yaml | kubectl apply -f -

# Set the feature flag
kubectl patch cm config-policy-controller -n cosign-system --type merge \
    -p '{"data":{"dev.chainguard.enable-cip-cache":"true"}}'
```

To turn this off, remove that setting from the ConfigMap, or set it to `false`.

## FAQs

### Why should I use this feature?

Usually Kubernetes Pod receives the most of the images passed down from parents objects like StatefulSets or ReplicaSets. Enabling this feature allows the verification results from parents objects to pass down to the Pods, thus reducing the traffic made to container registries. Not only that this would reduce latency, it would make policy enforcement a lot scalable.

In our load testing it we see that with cache hit, we see P99 verification latency of under 2s, and no egress was made to container registry. Without caching, latency would be highly dependent of registry access latency, which and the P99 latency may be ~10s or more. 

### What safeguards are there to make sure cache annotation values are tamper proof
We include a cryptographic signature inside the cache annotation and verifying such upon rereading. Invalid caches will be discarded.
