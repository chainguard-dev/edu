---
aliases:
- /chainguard/chainctl-usage/comparing-chainctl-to-console/
title: "Compare chainctl usage with the Chainguard Console"
linktitle: "chainctl vs Console"
type: "article"
description: "Learn when to use chainctl CLI versus Chainguard Console for managing container security, with practical examples and use case recommendations"
date: 2025-06-02T11:07:52+02:00
lastmod: 2026-11-12T00:00:00+00:00
draft: false
tags: ["chainctl", "Chainguard Console"]
images: []
menu:
  docs:
    parent: "chainctl-usage"
weight: 30
toc: true
---

You can manage your Chainguard resources in several ways, including the web-based Chainguard Console, the `chainctl` command-line tool, the [Chainguard API](/platform/api/), and the [Chainguard Terraform provider](/platform/administration/terraform-provider/). This page compares the Console and `chainctl` on a few common tasks.

## Prerequisites

To access the [Chainguard Console](/platform/console/images-directory/), [create an account and sign in](https://console.chainguard.dev/auth/login). The Console is accessible to everyone, including users who aren't Chainguard customers.

To use `chainctl`, start by [installing chainctl](/platform/chainctl-usage/how-to-install-chainctl/). Refer to [Get started with chainctl](/get-started/getting-started-with-chainctl/) to help you begin using it. The examples on this page assume you have `chainctl` installed and are authenticated. They also assume you belong to one organization, which `chainctl` selects automatically. If you have access to more than one, add `--parent=<organization>` to choose one. For `chainctl iam invite create`, pass the organization name as the first argument instead.

## High-level comparison

The Console is useful for one-off searches, such as when you don't know exactly what you're looking for. It provides detailed information, but it can take a few clicks to reach the detail you want.

If you know what you're looking for or what you want to accomplish, `chainctl` gets you there in one command, and you can script it. It can also do some things the Console can't, such as [comparing images with a diff](/platform/chainctl-usage/comparing-images/).

The following table lists the tasks this page covers and where to do each one:

| Task | In the Console | With `chainctl` |
|------|----------------|-----------------|
| [Find available images](#find-available-images) | **Images** | `chainctl images repos list` |
| [Add an image to your organization](#add-an-image-to-your-organization) | **Images** > **Chainguard catalog** | `chainctl images entitlements add-image` |
| [Add a Helm chart](#add-a-helm-chart) | **Helm charts** | `chainctl images helm add-chart` |
| [Create a pull token](#create-a-pull-token) | **Settings** > **Access Tokens** | `chainctl auth pull-token create` |
| [Invite users](#invite-users) | **Settings** > **Users** | `chainctl iam invite create` |
| [Review container image history](#review-container-image-history) | An image's **Tags** tab | `chainctl image history` |
| [Review security advisories](#review-security-advisories) | An image's **Advisories** tab | `chainctl images advisories list` |

## Find available images

### Find available images in the Console

1. Open the [Console](https://console.chainguard.dev).

1. In the sidebar, under **Containers**, click **Images**.

The **Organization** tab lists the images your organization can pull, with each image's **Status**, **Latest tag**, **Pull URL**, and when it was last **Updated**. To browse every image Chainguard publishes, click the **Chainguard catalog** tab.

### Find available images with `chainctl`

To list the image repositories your organization can pull, run the following command:

```sh
chainctl images repos list
```

To list every image Chainguard publishes, along with the upstream images each one replaces, run the following command instead:

```sh
chainctl images catalog
```

Both lists can be long, so consider piping the output into `grep` or redirecting it into a file.

## Add an image to your organization

Whether you can add images to your organization yourself depends on your organization's plan. Refer to [Chainguard container catalog pricing](/chainguard/containers/reference/pricing/) for details.

### Add an image in the Console

1. In the sidebar, under **Containers**, click **Images**.

1. Click the **Chainguard catalog** tab.

1. Find the image you want and click **Add to org** in its row. Depending on your plan, some images show a different option instead, such as **Contact us**.

### Add an image with `chainctl`

To add a catalog image with `chainctl`, run the following command. Replace `<image_name>` with the image's catalog name, such as `nginx`:

```sh
chainctl images entitlements add-image <image_name>
```

## Add a Helm chart

Adding a Helm chart also adds the container images the chart depends on. As with images, what you can add yourself depends on your organization's plan. Refer to [Self-serve Helm charts](/get-started/self-serve/helm-charts/) for the details of each plan.

### Add a Helm chart in the Console

1. In the sidebar, under **Containers**, click **Helm charts**.

1. Find the chart you want and click **Add to org** in its row.

1. The dialog that opens lists the images the chart requires, along with any optional images. Choose the optional images you want, and then click **Add chart and images**.

The Console adds the chart and its images in the background.

### Add a Helm chart with `chainctl`

To add a Helm chart with `chainctl`, run the following command. Replace `<chart_name>` with the chart's name, such as `argo-cd`:

```sh
chainctl images helm add-chart <chart_name>
```

To list the images the command would add before you add anything, include the `--dry-run` flag.

## Create a pull token

A pull token gives a system outside Chainguard, such as a CI pipeline or a Kubernetes cluster, long-lived credentials to pull from your organization's registry. Refer to [Authenticate to Chainguard's Registry](/chainguard/containers/registry/authenticating/) for more about pull tokens and the role you need to create one.

### Create a pull token in the Console

1. In the sidebar, click **Settings**.

1. Click **Access Tokens**.

1. Click **Create token**.

1. In the **Create access token** panel, enter a name and an optional description. Use the **Access** drop-down menu to choose what the token can pull, and the **Expiration** drop-down menu to choose when it expires.

1. Click **Create token**. Copy the token's **Username** and **Password** before you close the panel.

### Create a pull token with `chainctl`

To create a pull token with `chainctl`, run the following command. Replace `<token_name>` with a name for the token:

```sh
chainctl auth pull-token create --name=<token_name>
```

This token pulls container images. To create a token for packages or libraries, add the `--repository` flag, which matches the Console's **Access** setting. To set how long the token stays valid, add the `--ttl` flag with a duration in hours, such as `--ttl=168h`. The longest duration allowed depends on your organization's plan. Refer to [Pull token output formats and credential names](/platform/chainctl-usage/pull-token-output/) for what the command prints.

## Invite users

### Invite users in the Console

1. Open the Console.

1. In the sidebar, click **Settings**.

1. Under **Identities and Roles**, click **Users**.

1. Click **Invite users**.

1. Enter the user's **Email address**, choose a **Role** from the drop-down menu, and click **Invite**.

### Invite users with `chainctl`

To invite a user with `chainctl`, run the following command. Replace `<email_address>` with the address of the user you're inviting. Adjust the role, how long the invite stays valid (`--ttl`), and whether it can be used only once (`--single-use`) to suit your needs:

```sh
chainctl iam invite create \
  --role=viewer \
  --email=<email_address> \
  --ttl=168h \
  --single-use
```

Refer to [List and create invites](/platform/chainctl-usage/chainctl-iam/#list-and-create-invites) for more about inviting users with `chainctl`.

## Review container image history

### Review container image history in the Console

1. Open the Console and find the image you want to examine. Click it in the **Recent image changes** list on the **Overview** page, or click **Images** in the sidebar and find it there.

1. The image page opens on the **Tags** tab, which lists the image's tags, such as `latest` or a release version. For each tag, the list shows its **Pull URL**, **Digest**, **Compressed size**, and when it was **Last changed**.

The other tabs, such as **Vulnerabilities**, **SBOM**, and **Provenance**, give more detail about the image.

### Review container image history with `chainctl`

To examine the history of an image with `chainctl`, run the following command:

```sh
chainctl image history kubectl:latest
```

The output is a reverse-chronological history of each time the tag moved to a new manifest digest. This list can be long. Here's an excerpt:

```output
-- time: 2026-11-11 03:39:22 UTC
  digest: sha256:64002e49274e12df6910d2cba06dd4a11c996db8724a772050a514c6515437c5
  architectures:
    amd64: sha256:f3cb2f46f335a845b5f0eefac1f5acf69f1d0d93bafab68b41955005f81944d9 (18.85 MB)
    arm64: sha256:17ff97941bfec0479c89603764b1341c6f85bf5a6e03f36efe771ba4d13186f0 (16.71 MB)
- time: 2026-11-10 13:14:43 UTC
  digest: sha256:003dcd0754c25e48d962684828471e36eebc2b41360a0dc268c83083dd1ab9ed
  architectures:
    amd64: sha256:ac792aec79f531e44cc457c0164fe74b2af3c7c8af53d41e51904e9bdd38d6db (18.85 MB)
    arm64: sha256:8b2c54d5f97cf504c39f50d3ba64093590490916ff75aff132fe18f80808ec40 (16.70 MB)
- time: 2026-11-07 13:49:31 UTC
  digest: sha256:94853e2211d6c817d69d96c585968ef0acaa91915e1ec6ed0095ad9fbb9eb88a
  architectures:
    amd64: sha256:959adf7cb1d660d461b48e6f575b1e347477b29e686084dc6cedca02e5bf38ba (18.85 MB)
    arm64: sha256:39425ed01787e60aaf01cf1bb640398224c9dd51a9f3038c5f8c012700a01aa5 (16.70 MB)
- time: 2026-11-06 10:54:36 UTC
  digest: sha256:a8e301e6c44b00a0bda889f41ddaed1ea41364cfa3ae906d4277cd219ac92b13
  architectures:
    amd64: sha256:15341bebc88da9c03a4e4f96f8dcac9097e023e724fec9343543de7b37f8d85f (18.85 MB)
    arm64: sha256:13f97e329dc5fd89dbccf34a4a414420c8850c6996f36a97f2474315199b96b4 (16.70 MB)

...

```

The Console and `chainctl` focus on different details, but where they show the same detail, it should match. Refer to [Examine the history of container images](/platform/chainctl-usage/chainctl-images/#examine-the-history-of-container-images) for more information about this command.

## Review security advisories

Security advisories record the CVEs that have affected a container image's packages and what Chainguard did about each one.

### Review security advisories in the Console

1. In the sidebar, under **Containers**, click **Images**, and then click the image you want.

1. Click the **Advisories** tab.

The tab lists the image's advisories, newest first. Each entry gives the date of the advisory, the CVE, the affected package, and its current status.

### Review security advisories with `chainctl`

To list the advisories for an image with `chainctl`, run the following command. Replace `<organization>` with your organization name and `<image>` with the image's name:

```sh
chainctl images advisories list cgr.dev/<organization>/<image>:latest
```

The command reads the image's SBOM to find its packages, and then lists the advisories for each one. To show only advisories with certain statuses, add the `--status` flag, for example `--status=detected`. Refer to [How to use Chainguard Security Advisories](/chainguard/containers/security-and-compliance/security-advisories/how-to-use/) for more about advisories and their statuses.

## Features unique to each tool

### Compare a Chainguard Container to a non-Chainguard alternative in the Console

Only the Console offers this comparison. [Using CVE visualizations](/chainguard/containers/security-and-compliance/vulnerability-management/cve-visualizations/) describes this in detail.

### Compare two Chainguard Containers with `chainctl`

Only `chainctl` offers this comparison. [How to compare Chainguard Containers with chainctl](/platform/chainctl-usage/comparing-images/) describes it in detail.

## Learn more

To learn more about `chainctl`, refer to the following pages:

* [chainctl usage](/platform/chainctl-usage/)
* [chainctl reference](/platform/chainctl/)

To learn more about the Chainguard Console, refer to [Using the Chainguard Console](/platform/console/images-directory/).
