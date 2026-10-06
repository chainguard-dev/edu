---
title: "Using the Chainguard Console to manage Custom Assembly resources"
linktitle: "Manage in the Console"
type: "article"
description: "How to use Chainguard's Custom Assembly tool in the Chainguard console."
date: 2025-07-09T11:07:52+02:00
lastmod: 2026-10-05T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Custom Assembly"]
images: []
menu:
  docs:
    parent: "features"
weight: 20
toc: true
aliases:
- /chainguard/chainguard-images/features/ca-docs/custom-assembly-console/
- /chainguard/containers/features/ca-docs/custom-assembly-console/
---

Chainguard's [Custom Assembly feature](/chainguard/containers/custom-assembly/overview/) allows you to build customized container images that include only the packages your application needs. This tutorial walks you through using the [Chainguard console's web interface](https://console.chainguard.dev) to manage Custom Assembly resources, including selecting packages, building customized containers, and monitoring build status.

By the end of this guide, you'll be able to create, customize, and manage your own container images through the Chainguard console, giving you full control over your container dependencies while maintaining Chainguard's security and compliance standards.

{{< note >}}
This overview highlights using the Chainguard console's UI to interact with Custom Assembly resources. However, you can also interact with Custom Assembly using [`chainctl`, Chainguard's command-line interface tool](/chainguard/containers/custom-assembly/custom-assembly-chainctl/), as well as [the Chainguard API](/chainguard/containers/custom-assembly/custom-assembly-api-demo/).
{{< /note >}}

## Selecting packages and building a customized container

After logging in to the [Chainguard console](https://console.chainguard.dev/auth/login), the console opens to your account overview page. If you belong to more than one organization, be sure to select an organization with access to Custom Assembly from the drop-down menu in the top-left corner.

Click on **Images** and scroll or search for the container image that you want to customize. Note that you can use Custom Assembly to customize any Chainguard Container that your organization has access to.

Click your chosen container image to open its entry in the console. In the upper right corner of this page, you'll find the **Customize image** button and a **More** menu.

Click **Customize image** to open a window displaying a list of all of the packages available to be added or removed from your selected container image. This list of packages includes all the packages your organization is entitled to. If there's a package you'd like to include in your image but it isn't available in this list, please open a Chainguard support ticket.

You can scroll through the list and select or deselect packages to tailor the image to your needs by checking their respective boxes. Alternatively, you can use the search box to filter for the packages you're looking for.

After selecting your chosen packages, click the **Continue** button. Custom Assembly then prompts you to select one of the following two options for how you want to apply the customizations:

* **Create a new image**: This option creates a new container image, based on the current image you've chosen to customize.
    * This option requires you to select a new name for the container image. Note that whatever name you select can only contain lowercase alphanumeric characters, `-`, or `_`.
* **Customize current image**: This option overrides the existing container image with your customizations. Note that any customizations applied to this image also apply to any users in your organization who are already consuming it.

After selecting one of these options, click the **Preview changes** button to view all the packages you've selected for the customized image.

If you'd like to make further changes, click the **Back** button to return to the package selection.

If you're satisfied with the selection of packages, click the **Apply changes** button to build the new customized image. If you opted to create a new image, this button instead says **Create $IMAGE_NAME**. A confirmation message at the top of the Customize Container display tells you that the image was successfully customized.

If a build fails, you'll need to make the appropriate changes before attempting another build. You can check the build's logs for information about what went wrong and what to fix.

## Listing builds and viewing logs

You can view a list of all the available builds of your customized container image by clicking the customized image's **Builds** tab in the console.

The table in the Builds tab has six columns:

* **Status**: The status of the given build. When a build is successful, this column shows a green check inside of a circle. When a build has failed, this column displays a red exclamation mark in a triangle.
* **ID**: A unique identifier representing a specific customized container image build.
* **Tag**: The container image version the build represents.
* **Digest**: A unique, content-based hash representing the given container image build.
* **Duration**: The amount of time it took to build the container image.
* **Created**: How long it's been since the build was created.

Note that if you only recently customized the container image it may take a few minutes for the latest builds to populate.

Additionally, builds stay listed in the console for only 24 hours. This is because Chainguard Containers, including Custom Assembly container images, are rebuilt frequently and would quickly congest the user interface.

You can click on the row of any build listed in the Builds tab to access its logs. A window opens from the right with more details about the build, including build failures.

## Making changes to a customized container image

If you need to make further modifications to a customized image, or revert changes you've already made, you can do so with just a few clicks in the Chainguard console.

Going back to the container image you just customized, click **Customize image** again. The panel where you added packages lists the packages added to the customized image, below the **Search package names** box.

You can add more packages to the customized image by following the process outlined previously. To remove a package from the container image, click its **X** symbol.

To remove all of the container image's customizations, click **More** at the top right of the customize panel, then select **Remove customizations**. Removing all the added packages returns the image to its original state.

Note that you can also edit the packages in a customized image [using the `chainctl images repos build edit` command](/chainguard/containers/custom-assembly/custom-assembly-chainctl/#adding-packages-to-a-customized-container-image).

If you elected to create a new container image with Custom Assembly, you can rename it from the image's page. Click **More** next to the **Customize image** button. Select **Rename** and enter a new name for the image. Note that after you rename the customized image, any references to the previous name stop working.

You can also delete new container images that you've created with Custom Assembly. To do so, click **More** (again, next to the **Customize image** button) and select **Delete**. This opens a window that prompts you to enter the name of the container image to confirm that you want to delete it.

## Learn more

You can also use the Chainguard Console to add Chainguard-managed certificates to Custom Assembly images. Refer to our guide on [Adding custom certificates with Custom Assembly](/chainguard/containers/custom-assembly/custom-assembly-certs/#chainguard-managed-certificate-bundles) for more information.

For more advanced workflows or automation, consider exploring the [`chainctl` CLI tool](/chainguard/containers/custom-assembly/custom-assembly-chainctl/) or the [Chainguard API](/chainguard/containers/custom-assembly/custom-assembly-api-demo/) for programmatic access to Custom Assembly features.
