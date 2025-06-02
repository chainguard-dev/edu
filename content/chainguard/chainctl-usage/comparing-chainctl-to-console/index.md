---
title: "Compare chainctl usage with the Chainguard Console"
linktitle: "chainctl vs The Console"
type: "article"
description: "A comparison of completing tasks using chainctl vs the Chainguard Console."
date: 2025-06--2T11:07:52+02:00
lastmod: 2025-06--2T11:07:52+02:00
draft: false
tags: ["Chainguard Control", "chainctl", "Chainguard Console", "Product", ]
images: []
menu:
  docs:
    parent: "chainctl-usage"
weight: 025
toc: true
---

When should I use the Chainguard Console? When is it better to use `chainctl`? This page gives some guidance on the benefits of each method for managing your Chainguard Containers to help you make that decision.


## Prerequisites

To access the [Chainguard Console](/chainguard/chainguard-images/how-to-use/images-directory/) you need to [create an account and sign in](https://console.chainguard.dev/auth/login). The Console is accessible to everyone, including users who aren't Chainguard customers.

To use `chainctl`, start by [installing chainctl](/chainguard/chainctl-usage/how-to-install-chainctl/). See [Get Started with chainctl](/chainguard/chainctl-usage/getting-started-with-chainctl/) to help you begin using it; the examples on this page assume you have `chainctl` installed and are authenticated.


## High-level Comparison

The Console is especially useful for one-off information searches, such as when you don't know precisely what you want to know. It's also good at providing detailed information after a few clicks to zoom in. You can perform useful container-related query tasks from within the Console, as this page will demonstrate with some examples.

If you know specifically what you are looking for or what you want to accomplish, `chainctl` is a powerful way to do so. It can perform some additional tasks that are not yet available in the Console, such as [comparing images with a diff](/chainguard/chainctl-usage/comparing-images/).


## Example - Find Available Images

To find the images available to you in the Console, do this:

1. Open the [Console](https://console.chainguard.dev)
![Screenshot showing the Overview page in the Console.](console-overview.png)

1. On the Overview page that opens, click **Organization Images** in the sidebar.
![Screenshot showing the Organization Images page in the Console, which lists all of the images available along with data for each including Status, Latest tag, Pull URL, and when the image was last updated.](console-org-images.png)


To find the images available to you using `chainctl`, use this command. The list of available images is likely to be long and will scroll past you quickly in the terminal.

```
chainctl images list

```


## Example - Invite Users

1. Open the Console.

1. On the Overview page that opens, click the **Manage pull tokens** tab, just below the search box.

1. On the Settings page that opens, click **Users** in the sidebar.
![Screenshot showing the Settings page in the Console.](console-settings.png)

1. Click **Invite users**.
![Screenshot showing the list of users in the Console.](console-users.png)

1. Enter the **Email address** of the user you are inviting and use the dropdown menu to assign a **Role** for this user. Click **Invite**.


To invite a user using `chainctl`, use this command, substituting your organization name for ORGANIZATION along with setting the role, email address, length of time for the invite to be valid, and whether this invite may only be used once:

```
chainctl iam invite create ORGANIZATION
--role=viewer
--email=sample@organization.dev
--ttl=7d
--single-use

```

## Learn more

To learn more about the `chainctl`, see the
[chainctl Usage](/chainguard/chainctl/chainctl-usage/) docs or the [chainctl Reference] for more detail.

To learn more about the Chainguard Console, see [Using the Chainguard Directory and Console](/chainguard/chainguard-images/how-to-use/images-directory/).


### Compare a Chainguard Container to a non-Chainguard Alternative in the Console

This is a feature unique to the Console and is described in detail in [Using CVE Visualizations](/chainguard/chainguard-images/features/cve_visualizations/).

### Compare Two Chainguard Containers With chainctl

This is a feature unique to `chainctl` and is described in detail in [How To Compare Chainguard Containers with chainctl](/chainguard/chainctl-usage/comparing-images.md).