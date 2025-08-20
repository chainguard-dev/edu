---
title: "Chainguard Container Catalog Pricing"
linktitle: "Catalog Pricing"
type: "article"
description: "Explains Chainguard Container catalog pricing, repository quotas, renaming, and sync, and helps you understand how to make the most of your subscription."
date: 2025-08-19T08:49:31+00:00
lastmod: 2025-08-19T08:49:31+00:00
draft: false
tags: ["Chainguard Containers", "pricing"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 055
toc: true
---

Catalog pricing is Chainguard's pricing model for container usage that replaces the manual ticket process for adding images to an organization. This enables you to self-service request individual images to be added to your repository from the wider Chainguard catalog.

The catalog pricing model is an option that requires you to be on the Catalog Pricing plan.

> NOTE: If you would like to provide feedback, need troubleshooting assistance, or if your organization is not yet participating and would like to, please reach out to your account team.

---

## Catalog Pricing

Chainguard offers catalog pricing for our container catalog, providing access across the Chainguard Container images catalog.

- **What’s included**: Unlimited access to the full Chainguard-maintained container image catalog.
- **Benefits**:  
  - One subscription covers the entire catalog.  
  - No more per-repository licenses.  
  - Predictable monthly or annual costs.  
- **Use cases**: Perfect for organizations that pull many different Chainguard images across multiple teams or projects.  

---

## Repository Quotas

Your subscription includes a repository quota, which is the number of private repositories you can create or link.  

- **Checking quota**: Go to **Dashboard → Usage & Billing** to see your current quota and usage.  
- **Exceeding quota**:  
  - You’ll receive a warning if you approach your limit.  
  - To continue adding repositories, upgrade your plan or remove unused ones.  
- **Public repositories**: May not count toward your quota (check your plan details).  

---

## Repository Renaming

Repositories can now be renamed safely without disrupting your workflows.  

- **Backward compatibility**: Old repository names will continue to work temporarily.  
- **Recommended action**: Update CI/CD pipelines and image references to the new name as soon as possible.

To rename a repository, first open the repository in the Chainguard console.

Then, in **Settings → Rename Repository**, enter the new name and save.  

---

## Repository Sync

The repository sync feature keeps your repositories aligned with the upstream Chainguard catalog.  

- **What it does**:  
  - Automatically updates your repository with the latest secure image builds.  
  - Helps ensure compliance and reduces supply-chain risks.  
- **When to use**: Ideal for teams that want guaranteed up-to-date images without manual intervention.  

To enable repository sync, first open the repository in the console.

Then, navigate to **Repository Settings → Sync** and toggle **Sync with Catalog** on.

---

## Learn More

- [Blog announcement: Unlock the Full Chainguard Containers Catalog – Now with a Catalog Pricing Option](https://www.chainguard.dev/unchained/unlock-the-full-chainguard-containers-catalog-now-with-a-catalog-pricing-option)
- [Chainguard Pricing](https://www.chainguard.dev/pricing?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement)  