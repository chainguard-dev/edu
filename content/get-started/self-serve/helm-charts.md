---
title: "Self-serve Helm charts"
linktitle: "Self-serve Helm charts"
description: "Provision Chainguard Helm charts and their required images from the Chainguard Console as a Catalog customer"
type: "article"
date: 2026-08-06T00:00:01+00:00
lastmod: 2026-08-06T18:00:35+00:00
draft: false
weight: 020
toc: true
---

Catalog customers can provision Chainguard Helm charts, along with the container images each chart depends on, directly from the Chainguard Console. This replaces the previous manual request process, which required coordination with Chainguard sales, customer success, and support and could take 1 to 4 days.

{{< note >}}
This capability is available to Catalog customers whose plan includes the APPLICATION tier. It does not apply to the free [Catalog Starter](/chainguard/chainguard-images/about/catalog-starter/) plan. Customers on per-image pricing can request charts through a support workflow, described in [Per-image pricing customers](#per-image-pricing-customers).
{{< /note >}}

## Add a chart in the Chainguard Console

To add Helm charts to your organization from the Console, complete the following steps:

1. In the Chainguard Console, go to the **Helm charts** section in the sidebar.
1. Review the available charts. Charts already enabled for your organization are marked.
1. Select one or more charts to add. The Console checks whether your organization already has the container images each chart requires, then lists any missing images by name.
1. Optional: If your organization is entitled to FIPS images, select the FIPS option to add FIPS variants where they are available.
1. Confirm your selection to add the charts and their required images to your organization.

Provisioning runs in the background. The Console shows in-progress and completion states while it adds the charts and images, which can take some time to finish.

## Add a chart with `chainctl`

You can perform the same action from the command line with `chainctl`. For a Catalog customer, the following command resolves the chart's image dependencies and creates any missing chart and image repositories in your organization, matching the Console flow:

```shell
chainctl images helm add-chart $CHART
```

Replace `$CHART` with the chart you want to add. The command will output a small chart showing the name of every image in the Helm chart and the image status, such as whether it already exists in your org or is being added.

{{< note >}}
This command is available starting in a specific `chainctl` release. If it isn't available in your installation, update `chainctl` to the latest version.
{{< /note >}}

You can use the command to add `iamguarded` charts, too:

```shell
chainctl images helm add-chart iamguarded-charts/$CHART
```

If you want to test the process before actually adding the chart, use:

```shell
chainctl images helm add-chart $CHART --dry-run
```

To learn more, use `chainctl images helm add-chart --help` or refer to the [`chainctl` Reference documentation](/platform/chainctl/).

## Per-image pricing customers

If your organization uses per-image pricing, or a chart requires images outside your active tiers, the Console doesn't provision the chart instantly. Instead, it generates a single support request that lists the chart and any missing images, prefilled with your organization's details. Chainguard support then provisions the chart and images, typically within 1 to 2 days.

## Use your charts

After provisioning completes, authenticate and deploy your charts by following [How to Use Chainguard Helm Charts](/chainguard/chainguard-images/how-to-use/use-chainguard-helm-charts/).
