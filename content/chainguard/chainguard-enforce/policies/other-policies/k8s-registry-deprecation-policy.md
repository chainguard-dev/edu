---
title: "Policy to Notify on Kubernetes Registry Deprecation"
linktitle: "Kubernetes Registry Deprecation"
aliases:
- /chainguard/chainguard-enforce/chainguard-enforce-kubernetes/k8s-registry-deprecation-policy/
type: "article"
description: "How to prepare for the Kubernetes registry deprecation with Chainguard Enforce"
lead: "The old Kubernetes registry will be deprecated and frozen in April 2023"
date: 2023-03-19T13:11:29+08:29
lastmod: 2023-03-19T13:11:29+08:29
draft: false
images: []
tags: ["Enforce", "Kubernetes"]
menu:
  docs:
    parent: "policies"
weight: 050
toc: true
---

As of March 20, 2023, the Kubernetes project will be changing registries, from its `k8s.gcr.io` registry to a community-owned registry at `registry.k8s.io`. Pull requests to the previous registry will be redirected to the new one, and, on April 3, 2023, the old registry will be deprecated and frozen. You can read more about this on the Kubernetes blogpost, "[k8s.gcr.io Image Registry Will Be Frozen From the 3rd of April 2023](https://kubernetes.io/blog/2023/02/06/k8s-gcr-io-freeze-announcement/)."

In order to avoid using Kubernetes images from the deprecated registry, you will need to update pipelines to the new registry. Chainguard Enforce can help you fix workloads so that you can ensure you are using images from the new registry by using a new policy Chainguard created to support organizations who will need to be aware of this registry migration.

This document assumes that you are using Chainguard Enforce. If you would like to learn more about Enforce, please review our [overview](/chainguard/chainguard-enforce/enforce-overview/) and our [user onboarding](/chainguard/chainguard-enforce/). You can request access through selecting **Chainguard Enforce** on the [inquiry form](https://www.chainguard.dev/contact?utm_source=docs).

## Kubernetes Registry Deprecation Warning Policy

Chainguard Enforce users can deploy the following policy to their environment to send a warning for any running or newly-deployed workload coming from the deprecated k8s.gcr.io registry.

```yaml
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
 name: deprecated-k8s-grc-io-registry-rego
 annotations:
   catalog.chainguard.dev/title: Deprecated registry
   catalog.chainguard.dev/description: Warn of a registry deprecation
   catalog.chainguard.dev/labels: rego
   catalog.chainguard.dev/learnMoreLink: https://kubernetes.io/blog/2023/02/06/k8s-gcr-io-freeze-announcement/
spec:
 mode: warn
 images:
 - glob: "k8s.gcr.io/**"
 authorities:
 - name: k8s-deprecated
   static:
     action: pass
 policy:
   type: rego
   data: |
     package sigstore
     isCompliant[response] {
       response := {
         "result" : true,
         "error" : "",
         "warning" : "This repo has been deprecated: https://kubernetes.io/blog/2023/02/06/k8s-gcr-io-freeze-announcement/"
       }
     }

# Copyright 2023 Chainguard, Inc.
```

Written in the [Rego policy language](/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/chainguard-enforce-rego-policies/), this policy will instruct Chainguard Enforce to continuously monitor all your running workloads and notify you if you are impacted by this change. It will also monitor any new deployment requests to your cluster for images coming from the old registry at k8s.gcr.io. Since the policy is in ["warn" mode](/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/how-to-disable-policy-enforcement/), it will allow the deployment to proceed, but will generate a warning in the Enforce platform and back to the user that an image has been deployed from the deprecated registry.

This policy will run on all of your clusters across clouds continuously, so if any image violates the policy, it will record a violation immediately and notify you. You can use this information to let your development teams know that they need to update their pipelines before the freeze date.

If you would like to prohibit these images from entering you cluster, you can comment out the `mode: warn` line, which will disallow the admission of these images.