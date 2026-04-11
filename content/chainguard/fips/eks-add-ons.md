---
title: "Overview of Chainguard EKS Add-ons"
linktitle: "EKS Add-ons"
description: "Learn about Chainguard EKS add-ons, which provide zero-CVE and FIPS-validated container images for core Amazon EKS cluster components through AWS Marketplace."
type: "article"
date: 2026-04-10T00:00:00+00:00
lastmod: 2026-04-10T00:00:00+00:00
draft: false
tags: ["FIPS", "Chainguard Containers"]
images: []
menu:
  docs:
    parent: "fips"
weight: 035
toc: true
---

Chainguard EKS add-ons are hardened, minimal container images for the foundational software components that power Amazon Elastic Kubernetes Service (EKS) clusters. Available through [AWS Marketplace](https://aws.amazon.com/marketplace) with FIPS-validated variants, they serve as drop-in replacements for AWS default add-ons, providing zero known CVEs and optional FIPS 140-3 validated cryptography without requiring custom image builds or manifest overrides.


## What are EKS add-ons?

Amazon EKS add-ons are software components that provide supporting operational capabilities to Kubernetes applications — things like networking drivers, storage integrations, and observability agents that allow the cluster to interact with underlying AWS resources, but aren't specific to any application running on it.

They handle cluster functions like internal DNS resolution, pod networking, persistent storage, and traffic routing, and are managed independently from your application workloads. AWS installs several add-ons in every EKS cluster by default.

For a full explanation of how EKS add-ons work (including how to install, configure, and update them), refer to the [Amazon EKS add-ons documentation](https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html).


## Available Chainguard EKS add-ons

Chainguard provides hardened images for six widely used EKS add-ons. All are available in both standard and FIPS-validated variants.

| Add-on | Description |
|--------|-------------|
| **kube-proxy** | Routes network traffic between pods within the cluster |
| **CoreDNS** | Handles internal DNS — how services discover and communicate with each other |
| **Amazon VPC CNI** | Connects pods to the AWS VPC network backbone |
| **Amazon EBS CSI Driver** | Enables persistent block storage volumes backed by Amazon EBS |
| **Amazon EFS CSI Driver** | Enables shared, persistent file storage backed by Amazon EFS |
| **AWS Load Balancer Controller** | Routes external traffic into the cluster through AWS Application and Network Load Balancers |


## Why use Chainguard EKS add-ons?

### Zero known CVEs

AWS's default EKS add-on images ship with known CVEs. Because customers do not own the upstream source code, they aren't able to patch these vulnerabilities.

Chainguard rebuilds each add-on using its minimal, hardened container image approach, removing unnecessary packages and dependencies that are the most common source of CVEs. Like Chainguard Containers, Chainguard EKS add-ons are rebuilt continuously to incorporate available security patches, keeping the known CVE count at or near zero.

### FIPS 140-3 validated cryptography

For organizations operating under FedRAMP, NIST, or other compliance frameworks that require FIPS-validated cryptography, AWS's default add-ons do not qualify. Chainguard EKS add-ons are the only available option that provides FIPS 140-3 validated variants for core EKS cluster infrastructure. No other provider offers FIPS-validated replacements for these components.

To learn more about how Chainguard approaches FIPS, refer to the [Chainguard FIPS documentation](/chainguard/fips/).

### Drop-in compatibility

Chainguard EKS add-ons are designed as direct replacements for the corresponding AWS-managed components. They use the same Helm-based deployment workflow as any other EKS add-on and require no changes to your existing cluster configuration.

Chainguard EKS add-ons are available through AWS Marketplace and can be found through the AWS Console. There's no manual setup, you don't need a Chainguard account to subscribe, and billing is consolidated with your existing AWS bill.


## Who should use Chainguard EKS add-ons?

Chainguard EKS add-ons are well-suited for:

- **Regulated industries**: Healthcare, financial services, defense, and government organizations that require FIPS 140-3 validated cryptography or operate under FedRAMP, NIST 800-53, or similar compliance frameworks.
- **Security-conscious engineering teams**: Platform and DevOps teams that want a clean, auditable baseline for cluster infrastructure without maintaining custom image builds or accepting audit exceptions.
- **Organizations requiring infrastructure control**: Enterprises that need more control over their EKS deployments than EKS Auto Mode provides, and for whom FIPS compliance through Auto Mode is not a viable option.


## Using Chainguard EKS add-ons

### Prerequisites

In order to use Chainguard EKS add-ons, you will need the following:

- An active AWS account
- An existing Amazon EKS cluster, or permission to create one
- AWS IAM permissions sufficient to subscribe to AWS Marketplace offerings

### Subscribe through AWS Marketplace

Chainguard EKS add-ons are listed in AWS Marketplace and can be found within the EKS Console. To subscribe:

1. In the AWS Console, navigate to your EKS cluster and open the **Add-ons** tab.
2. Search for the Chainguard add-on you want to install.
3. Select the desired variant (standard or FIPS) and subscribe.

### Deploy with Helm

Once subscribed, deployment follows the standard EKS Helm workflow. No new tooling, no Chainguard account, and no changes to your existing Kubernetes manifests are required.

For step-by-step installation guidance, refer to the deployment instructions included with each add-on listing in AWS Marketplace.
