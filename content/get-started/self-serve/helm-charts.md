---
title: "Self-serve Helm charts"
linktitle: "Self-serve Helm charts"
description: "Provision Chainguard Helm charts and their required images from the Chainguard Console as a Catalog customer"
type: "article"
date: 2026-08-06T00:00:01+00:00
lastmod: 2026-11-12T00:00:00+00:00
draft: false
weight: 20
toc: true
---

Catalog customers can provision Chainguard Helm charts, along with the container images each chart depends on, directly from the Chainguard Console. This replaces the previous manual request process, which required coordination with Chainguard sales, customer success, and support and could take 1 to 4 days.

{{< note >}}
This capability is available to Catalog customers whose plan includes the APPLICATION tier. Chainguard Starter and Chainguard Team organizations add charts with `chainctl`, as described in [Chainguard Starter and Chainguard Team organizations](#chainguard-starter-and-chainguard-team-organizations). Customers on per-image pricing can request charts through a support workflow, described in [Per-image pricing customers](#per-image-pricing-customers).
{{< /note >}}

## Add a chart in the Chainguard Console

To add a Helm chart to your organization from the Console, complete the following steps:

1. In the Chainguard Console, go to the **Helm charts** section in the sidebar.
1. Review the available charts. Charts already enabled for your organization are marked.
1. Find the chart you want to add and click **Add to org** in its row. You can add one chart at a time.
1. The dialog that opens lists the images the chart requires, along with any optional images. Choose the optional images you want to add.
1. Optional: If your organization is entitled to FIPS images, select **Use FIPS-validated images** to add FIPS variants where they are available.
1. Click **Add chart and images** to add the chart and its images to your organization.

Provisioning runs in the background. The Console shows in-progress and completion states while it adds the chart and images, which can take some time to finish. If a chart doesn't appear, refer to [Troubleshoot a chart that doesn't appear](#troubleshoot-a-chart-that-doesnt-appear).

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

## Troubleshoot a chart that doesn't appear

Provisioning usually finishes without any action from you, but it can take longer than expected for either of these reasons:

- Chainguard is working through a large queue of catalog updates.
- The chart, or one or more of the images it requires, is waiting for a version update.

While you wait, you can add the chart again from the Console or with `chainctl`. If the chart still hasn't appeared 48 hours after you first added it, [open a support request](/get-started/get-support/) that includes your organization name and the chart name.

## Chainguard Starter and Chainguard Team organizations

A [Chainguard Starter or Chainguard Team](/get-started/self-serve/plans/) organization can add a chart with `chainctl images helm add-chart`, as described in [Add a chart with `chainctl`](#add-a-chart-with-chainctl). Each image the chart depends on that your organization doesn't already have uses one of its five image slots. To see which images a chart would add before you use any slots, run the command with `--dry-run` first.

Chainguard refuses charts in the following cases:

- The chart needs more image slots than your organization has left. The error says so.
- The chart's metadata lists no image dependencies. The error reports an entitlement problem, even though the cause is the chart's metadata.

## Per-image pricing customers

If your organization uses per-image pricing, or a chart requires images outside your active tiers, the Console doesn't provision the chart instantly. Instead, it generates a single support request that lists the chart and any missing images, prefilled with your organization's details. Chainguard support then provisions the chart and images, typically within 1 to 2 days.

## Use your charts

After provisioning completes, authenticate and deploy your charts by following [How to Use Chainguard Helm Charts](/chainguard/containers/using-and-deploying/helm-charts/use-chainguard-helm-charts/).
