---
title: "Chainguard Container Catalog Pricing"
linktitle: "Catalog Pricing"
type: "article"
description: "Explains Chainguard Container catalog pricing, repository quotas, renaming, and sync, and helps you understand how to make the most of your subscription."
date: 2025-08-19T08:49:31+00:00
lastmod: 2025-08-19T08:49:31+00:00
draft: false
tags: ["Chainguard Containers"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 055
toc: true
---

Chainguard offers catalog pricing for our container catalog, providing access across the Chainguard Container images catalog.

Catalog pricing is an alternative pricing model for container usage that replaces the manual ticket process for adding images to an organization, like must be done using a per-image pricing model. Catalog pricing enables you to request individual images in the console to be added to your repository from the wider Chainguard catalog.

The catalog pricing model is an option that requires you to be on the Catalog Pricing plan.

> NOTE: If you would like to provide feedback, need troubleshooting assistance, or if your organization is not yet participating and would like to, please reach out to your account team.


## Catalog Pricing

- **What’s included**: Unlimited access to the full Chainguard-maintained container image catalog.
- **Benefits**:
  - One subscription covers the entire catalog within your purchased options, for example whether or not your license includes FIPS images.
  - No more per-repository licenses.
  - Predictable monthly or annual costs.
- **Use cases**: Ideal for organizations that pull many different Chainguard images across multiple teams or projects.


## Add a Container Image

To add an image to your organization, select **Images** in the sidebar menu and then select the **Chainguard catalog** tab.

Scroll through the list or use search to find the image you want. If the image is available to your organization, use the **Add to org** button in the row for the image listing. If your organization does not have access to FIPS images, you will not be able to add them. The **Add image** dialog will appear. Click **Add image** to close the dialog and finish.

> NOTE: If you see **Available in org** in the place of the add button, return to **Images** and click the **Add image** button above the list of organization images. Use search in the dialog that appears to find the image and click the bookmark icon next to the image name. You will be required to enter a different name for the new image, which will be added alongside the existing image when you click **Add image**.

Please allow up to 60 minutes for the image to be added to your organization.


## Repository Quotas

Your subscription includes a repository quota, which is the number of custom assembled images you can add to your organization.

To see your current quota and usage go to **Settings → Plan & Subscription**.

- **Exceeding quota**:
  - You’ll receive a warning if you approach your limit.
  - To continue adding repositories, upgrade your plan or remove unused ones.
- **Public repositories**: May not count toward your quota (check your plan details).


## Repository Sync

The repository sync feature keeps your repositories aligned with the upstream Chainguard catalog by automatically updating your repository with the latest secure image builds. This helps ensure compliance and reduces supply-chain risks.

This is ideal for teams that want guaranteed up-to-date images without manual intervention.


## Learn More

Chainguard's catalog pricing provides access across the Chainguard container images catalog.

To learn more, you may be interested in the following resources:

- [Blog announcement: Unlock the Full Chainguard Containers Catalog – Now with a Catalog Pricing Option](https://www.chainguard.dev/unchained/unlock-the-full-chainguard-containers-catalog-now-with-a-catalog-pricing-option?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement)
- [Chainguard Pricing](https://www.chainguard.dev/pricing?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement)