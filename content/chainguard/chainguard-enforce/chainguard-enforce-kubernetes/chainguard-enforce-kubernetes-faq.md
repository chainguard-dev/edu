---
title: "Chainguard Enforce for Kubernetes FAQs"
type: "article"
description: "Frequently asked questions about Chainguard Enforce for Kubernetes"
date: 2022-10-18T08:49:31+00:00
lastmod: 2023-01-12T08:49:31+00:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-enforce-kubernetes"
weight: 800
toc: true
---

> _This document relates to Chainguard Enforce. In order to follow along, you will need access to Chainguard Enforce. You can request access through selecting **Chainguard Enforce for Kubernetes** on the [inquiry form](https://www.chainguard.dev/get-demo?utm_source=docs)._

### What is Chainguard Enforce for Kubernetes?
Chainguard Enforce is our comprehensive software supply chain security risk management solution for cloud native workloads. Enforce enables you to build, manage, and enforce policies across your Kubernetes clusters that protect your organization from supply chain threats, and continuously ensures that your clusters stay in compliance with those policies.

Chainguard Enforce allows CISOs to have more control and confidence in what software is allowed in their production environments, and makes developers more productive with deep insight into production workloads.


### What problems does Chainguard Enforce for Kubernetes solve?
Most organizations don’t have a clear picture of what code is running in production, where it came from, or how it was built. This problem is compounded with the use of open-source software and the sheer number of dependencies that are included in container images. It becomes nearly impossible to decide what should be trusted or not in production environments.

Furthermore, organizations spend an exorbitant amount of time after a supply chain attack trying to assess if they’re running vulnerable software or are otherwise impacted. Chainguard Enforce enables organizations to make evidence-based decisions for what should and should not be allowed to run in their production environments by providing the integrations, tooling insights, and security controls that make this problem tractable. 


### What is continuous verification?

Chainguard Enforce's [continuous verification](../understanding-continuous-verification/) continuously scans all of the deployed applications against all of the latest policies, so if a deployed application violates a new policy or falls out of compliance, then it will catch the policy violation immediately. A policy may fail out of compliance, for example, when a new critical CVE is discovered. These violations are sent as Cloud Events, so you can integrate with your preferred notification system and respond effectively: whether that’s filing a JIRA ticket, paging the oncall, deleting pods, or triggering a CI/CD pipeline to redeploy the application.


### How does Chainguard Enforce compare to runtime tools? 

Chainguard Enforce is designed to be proactive by preventing tampered artifacts from ever entering the environment in the first place. This differs from runtime security tools which are, by their very nature, reactive; they typically do not detect a problem until after a malicious event occurs.

This continuous verification approach complements runtime tools nicely; Enforce builds trust with untampered artifacts, and runtime tools verify that those workloads are behaving as expected. By defending from both sides you will have far fewer incidents that warrant monitoring and alerting which is also beneficial in reducing alert fatigue and making alerts actionable.

Another feature that differentiates Chainguard Enforce for Kubernetes from runtime tools is Enforce's Agentless mode. Agentless mode is a zero footprint connection for Kubernetes clusters running in supported cloud providers. This means you can get all the benefits of Chainguard Enforce for Kubernetes without having to install another tool in your cluster.

Additionally, since they intercept system calls at the host level, these runtime tools require a great deal of CPU and memory resources. Because monitoring is done per cluster, Chainguard Enforce requires only 1 CPU / 1 GB memory per cluster. Again, though, these are different tools tackling different problems, so their resource footprints are not the best points of comparison.


### How does Chainguard Enforce's Agentless architecture work?

Agentless connections operate directly over the Kubernetes API, just like clients such as `kubectl`. All the operations for your cluster run in a dedicated tenant space in Chainguard's own environment.  This means that we handle the work for your clusters so your resources can better serve your organization's needs.  


### How big is the Chainguard Enforce Agent's resource footprint?

The amount of CPU and RAM that Enforce uses is configurable, and you can raise or lower the requests and limits based on policy and enforcement prioritization. By default, Chainguard Enforce's resource request is 0.05 CPU and 50MB RAM per pod, with a maximum limit of 1 CPU and 1GB of RAM. Our goal is to ensure that your applications have the most access to your resources — not our agent.

```
requests:
      cpu: 50m
      memory: 50Mi
    limits:
      cpu: 1000m
      memory: 1000Mi
```


### Does Chainguard Enforce for Kubernetes also perform vulnerability scanning?
Chainguard Enforce doesn't perform vulnerability scanning itself. Instead, it serves to complement scanning tools by ingesting their SBoMs and vulnerability results. It then implements policies that check for updated package versions, SBoM availability, and CVE status before allowing an image to be deployed.


### What container platforms does Chainguard Enforce support?

Chainguard Enforce can run anywhere Kubernetes runs, including the top Kubernetes runtime platforms like GKE and EKS.


### What build systems can I use with Chainguard Enforce for Kubernetes?

We integrate with all of the most popular CI/CD systems, including Jenkins, CircleCI, GitHub Actions, Gitlab CI, and Tekton. 


### What are the differences between using the Chainguard Enforce Agent and Agentless Connections?

The Enforce Agent is a flexible, general purpose way to connect your clusters to Chainguard Enforce. Clusters using the Chainguard Enforce Agent are required to have [Service Account Token Volume Projection](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#service-account-token-volume-projection) and [Service Account Issuer Discovery](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#service-account-issuer-discovery) enabled.

Chainguard Enforce Agentless connections allow you to connect a cluster with zero resource footprint. Agentless connections are currently limited to Google Cloud Platform’s GKE and AWS’s EKS clusters. Agentless connections also require clusters to have a public API endpoint. These connections work by allowing Chainguard Enforce to access your cloud account resources on your behalf using [Cloud Account Associations](https://edu.chainguard.dev/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/cloud-account-associations). This requires you to configure IAM roles to allow Enforce to perform impersonation, which is handled by Chainguard's [GCP](https://github.com/chainguard-dev/terraform-google-chainguard-account-association) and [AWS](https://github.com/chainguard-dev/terraform-aws-chainguard-account-association) terraform modules.


### How is Chainguard Enforce for Kubernetes priced?
Pricing is per node on a sliding scale. Use the [inquiry form](https://www.chainguard.dev/get-demo?utm_source=docs) to request access or [contact us](https://www.chainguard.dev/contact) if you'd like to learn more.