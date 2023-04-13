---
title: "Understanding Continuous Verification in Enforce"
type: "article"
description: "A Conceptual Article Outlining Enforce's Continuous Verification Feature"
date: 2022-21-09T15:22:20+01:00
lastmod: 2022-21-09T15:22:20+01:00
draft: false
tags: ["Enforce", "Product", "Conceptual"]
images: []
menu:
  docs:
    parent: "chainguard-enforce-kubernetes"
weight: 100
toc: true
---

> _This documentation is related to Chainguard Enforce. You can request access to the product by selecting **Chainguard Enforce** on the [inquiry form](https://www.chainguard.dev/contact?utm_source=docs)._

One feature unique to Chainguard Enforce is its ability to check whether a container or cluster contains any vulnerabilities continually over time. This feature is referred to as "continuous verification."

To better understand why this might be useful, imagine an organization using typical container analysis tools to scan its containers before each deployment. Say that one day, prior to a new deployment, the organization scans all its running containers like usual. Not finding any vulnerabilities, they continue on with the deployment.

So far in this example, everything seems to be working smoothly and going as expected. However, now imagine that the application becomes exposed to a vulnerability after the deployment. For example, a previously unknown vulnerability that impacts one or more of the containers could be discovered after the deployment. Or perhaps a malicious actor managed to install a harmful package into one of the application's running containers. 

In a real world scenario like this, an organization might not have any way of knowing about these vulnerabilities until the next deployment, which could be days or weeks into the future. Until then, any undetected vulnerabilities could seriously jeopardize their application or even their customers' data.

Chainguard Enforce's continuous verification continually checks whether software artifacts are compliant with the latest defined policies and known information. It enables your organization to have an inventory of everything currently running in your Kubernetes clusters, as well as everything that ran in the past. This includes what packages are deployed, SBOMs (software bills of materials), provenance, signature data, and more. It’s now possible to understand if, where and when a vulnerable image previously ran. The time to resolution thus turns into seconds instead of weeks.


## How Continuous Verification Works

The Chainguard Enforce agent uses an [admission controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) to block any requests that violate a cluster's policy. An admission controller is a special piece of code that reads requests to the Kubernetes API before the requested object is made persistent, but after the request has been authenticated.

However, admission controllers only check policies when Kubernetes resources are being created. If new policies are rolled out, or the state of an application’s compliance degrades over time, then admission controllers will not catch the compliance degradation. With continuous verification, though, Enforce continuously scans the cluster against all of the latest policies, so if a deployed application violates a new policy or falls out of compliance, then it will catch the policy violation before Kubernetes acts on the request. 

Chainguard Enforce then sends a webhook with relevant metadata about the object along to compare it with the cluster's policy, which is stored within the Enforce platform. This metadata might include things like an SBOM. By comparing this metadata with the established policy, Chainguard Enforce can verify whether the request satisfies the policy. If it does satisfy the policy, Chainguard Enforce approves it and the requested object gets created and deployed.

If a request fails to satisfy your cluster's policy, it will trigger a violation. These violations are sent as Cloud Events, so you can respond in the most appropriate way for your policies and applications. This might be to file a JIRA ticket, page the oncall, delete pods, or trigger a CI/CD pipeline to redeploy the application. Regardless of how you configure your response, the violation will be logged for future reference.

Following that, this process repeats itself indefinitely. Because it revolves around the use of webhooks — which themselves are essentially specialized HTTP requests — the continuous verification process has a fairly low performance impact. 


## Understanding the data Chainguard Enforce uses for continuous verification

It might be a concern to some that Chainguard Enforce scans and verifies requests made to the Kubernetes API. And this would be understandable, given that one must place a great deal of trust in any entity that has access to sensitive data. 

However, Chainguard Enforce doesn't read or store any code or information from the requests it scans. Instead, it only reads the metadata about the request, such as signature information or data about the packages constituting the image (an SBOM). Aside from the data that Chainguard collects and stores in order to function — including information about the connected Kubernetes cluster and user-provided data, like policy or IAM group information — Enforce only handles and stores this metadata.

Bear in mind that Chainguard Enforce may also retrieve certain information — but not store it — in order to verify that a request satisfies the policy. For instance, say you attempt to use a container image in your cluster and your Enforce policy dictates that the image be signed. Chainguard Enforce will check the container's signature against the hash found in its specified container registry, but it won't ingest the signature information.

## Configuring Continuous Verification

Continuous verification in Chainguard Enforce defaults to 10 seconds, and it is configurable through the ConfigMap's `config-image-policies` inside the `cosign-system namespace`. Here, you will find a `resync` annotation which will inform Enforce how frequently to run continuous verification.

```sh
apiVersion: v1
kind: ConfigMap
metadata:
  name: config-image-policies
  namespace: cosign-system
  annotations:
    # Have continuous verification constantly checking for new containers
    # subject to policies and reflecting their status to the API.
    gulfstream.dev/resync: "10s"       # <---- Continuous verification is set at this line
```

Updating this line setting will change the scan frequency.

You can run the following shell command to overwrite the ConfigMap. For example, if you would like continuous verification to run every 20 seconds, you can complete that with `kubectl`.

```sh
kubectl annotate configmap -n cosign-system config-image-policies gulfstream.dev/resync=20s --overwrite
```

If you would alternatively like continuous verification to run every 5 seconds, you can set the resync to `gulfstream.dev/resync=5s` instead.

Chainguard Enforce is flexible across workloads, and if you want to be able to dictate a certain frequency of verification, this setting can offer you greater control. 
