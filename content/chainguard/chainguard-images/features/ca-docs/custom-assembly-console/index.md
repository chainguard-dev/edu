---
title: "Using the Chainguard Console to Manage Custom Assembly Resources"
linktitle: "Manage in the Console"
type: "article"
description: "How to use Chainguard's Custom Assembly tool in the Chainguard console."
date: 2025-07-09T11:07:52+02:00
lastmod: 2025-07-15T11:07:52+02:00
draft: false
tags: ["Chainguard Containers", "Custom Assembly"]
images: []
menu:
  docs:
    parent: "features"
weight: 005
toc: true
---

Chainguard's [Custom Assembly feature](/chainguard/chainguard-images/features/ca-docs/custom-assembly/) allows you to build customized container images that include only the packages your application needs. This tutorial will walk you through using the [Chainguard console's web interface](https://console.chainguard.dev) to manage Custom Assembly resources, including selecting packages, building customized containers, and monitoring build status.

By the end of this guide, you'll be able to create, customize, and manage your own container images through the Chainguard console, giving you full control over your container dependencies while maintaining Chainguard's security and compliance standards.

> **Note**: This overview highlights using the Chainguard console's UI to interact with Custom Assembly resources. However, you can also interact with Custom Assembly using [`chainctl`, Chainguard's command-line interface tool](/chainguard/chainguard-images/features/ca-docs/custom-assembly-chainctl/), as well as [the Chainguard API](/chainguard/chainguard-images/features/ca-docs/custom-assembly-api-demo/).


## Selecting Packages and Building a Customized Container

After logging in to the [Chainguard console](https://console.chainguard.dev/auth/login), you will be greeted with your account overview page. If you belong to more than one organization, be sure to select an organization with access to Custom Assembly from the drop-down menu in the top-left corner:

<center><img src="ca-1.png" alt="Screenshot of the Chainguard console, with the Organization selection drop-down menu highlighted in a yellow box." style="width:1100px;"></center>
<br /> 

Click on **Images** and scroll or search for the container image that you want to customize. Note that you can use Custom Assembly to customize any Chainguard Container that your organization has access to.

Clicking on your chosen container image will take you to its entry in the console. In the upper right corner of this page, you'll find three buttons, one of which says **Customize image**: 

<center><img src="ca-2.png" alt="Screenshot of a Custom Assembly container (named 'customized_node') page with the 'Customize Container' button highlighted in a yellow box." style="width:1100px;"></center>
<br /> 

Click on this button to open a window displaying a list of all of the packages available to be added or removed from your selected container image. This list of packages includes all the packages your organization is entitled to. If there's a package you'd like to include in your image but it isn't available in this list, please open a Chainguard support ticket.

You can scroll through the list and select or deselect packages to tailor the image to your needs by checking their respective boxes. Alternatively, you can use the search box to filter for the packages you're looking for.

After selecting your chosen packages, click the **Continue** button. After doing so, Custom Assembly will prompt you to select one of the two following options for how you want to apply the customizations:

* **Create a new image**: This option will create a new container image, based on the current image you've chosen to customize. 
    * This option requires you to select a new name for the container image. Note that whatever name you select can only contain lowercase alphanumeric characters, `-`, or `_`. 
* **Customize current image**: This option overrides the existing container image with your customizations. Note that any customizations applied to this image will also apply to any users in your organization that are already consuming it.

<center><img src="ca-3.png" alt="Screenshot of the Customize Image display, showing the two customization options. The 'Create new image' option is selected, with the name 'customized_node' entered into the naming field." style="width:650px;"></center>
<br /> 

After selecting one of these options, click the **Preview changes** button to view all the packages you've selected for the customized image:

<center><img src="ca-4.png" alt="Screenshot of the customized_node image's customization preview. It shows three packages selected: bash, curl, and wget." style="width:650px;"></center>
<br /> 

If you'd like to make further changes, click the **Back** button to return to the package selection.

If you're satisfied with the selection of packages, click the **Apply changes** button to build the new customized image. If you opted to create a new image, this button will instead say **Create $IMAGE_NAME**. You will receive a confirmation message at the top of the Customize Container display letting you know that the image was successfully customized.

If a build fails, you'll need to make the appropriate changes before attempting another build. You can check the build's logs for information about what went wrong and what to fix.


## Listing Builds and Viewing Logs

You can view a list of all the available builds of your customized container image by clicking the customized image's **Builds** tab in the console:

<center><img src="ca-5.png" alt="Screenshot of a Custom Assembly container image's Builds tab, with the Builds tab highlighted in a yellow box." style="width:1100px;"></center>
<br /> 

The table in the Builds tab has six columns:

* **Status**: The status of the given build. When a build is successful, this column will show a green check inside of a circle. When a build has failed, this column will display a red exclamation mark in a triangle.
* **ID**: A unique identifier representing a specific customized container image build.
* **Tag**: The container image version the build represents.
* **Digest**: A unique, content-based hash representing the given container image build. 
* **Duration**: The amount of time it took to build the container image.
* **Created**: How long it's been since the build was created. 

Note that if you only recently customized the container image it may take a few minutes for the latest builds to populate.

Additionally, builds will only stay listed in the console for 24 hours. This is because Chainguard Containers, including Custom Assembly container images, are rebuilt frequently and would quickly congest the user interface.

You can click on the row of any build listed in the Builds tab to access its logs. This will cause a window to appear from the right where you can get more details about the build, including build failures:

<center><img src="ca-6.png" alt="Screenshot of a customized container image build's logs, showing a successful build." style="width:650px;"></center>
<br /> 


## Making Changes to a Customized Container Image

If you need to make further modifications to a customized image, or revert changes you've already made, you can do so with just a few clicks in the Chainguard console.

Going back to the container image you just customized, click once again on the **Customize Image**. In the panel where you added packages, there will be a list of the packages added to the customized image below the **Filter packages** search box:

<center><img src="ca-7.png" alt="Screenshot of the customized_node image's customization menu, before the preview screen. It shows three packages that have been added but can also be removed: bash, curl, and wget." style="width:650px;"></center>
<br /> 

You can add more packages to the customized image by following the process outlined previously. To remove a package from the container image, click its **X** symbol.

To remove all of the container image's customizations, click the **More Actions** button at the top right then select **Remove customizations**. Removing all the added packages will return the image to its original state.

Note that you can also edit the packages in a customized image [using the `chainctl image repo build edit` command](/chainguard/chainguard-images/features/ca-docs/custom-assembly-chainctl/#editing-a-customized-container-image). 

If you elected to create a new container image with Custom Assembly, you can rename it by clicking the **Rename** button (next to the **Customize image** button) and entering a new name for the image. Note that after renaming the customized image, any references to the previous name will no longer work.

You can also delete new container images that you've created with Custom Assembly. To do so, click the **More** button and select **Delete**. This will open a window prompting you to enter the name of the container image to confirm that you want to delete it:

<center><img src="ca-8.png" alt="Screenshot of the image deletion window for the customized_node container image. It shows a warning reading 'This action cannot be undone. The image will be permanently deleted from your organization and will no longer be available.' The name of the image ('customized_node') has been entered into the prompt." style="width:650px;"></center>
<br />


## Learn More

You now have the knowledge to effectively manage Custom Assembly resources through the Chainguard console. This web interface provides a user-friendly way to customize container images by adding or removing packages, monitor build status, and review build logs without needing to use command-line tools.

Remember that customized images are rebuilt frequently, and build history is retained for 24 hours. For more advanced workflows or automation, consider exploring the [`chainctl` CLI tool](/chainguard/chainguard-images/features/ca-docs/custom-assembly-chainctl/) or the [Chainguard API](/chainguard/chainguard-images/features/ca-docs/custom-assembly-api-demo/) for programmatic access to Custom Assembly features.
