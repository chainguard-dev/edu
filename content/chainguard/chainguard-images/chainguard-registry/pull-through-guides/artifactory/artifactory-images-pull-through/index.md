---
title: "How to Set Up Pull-through from Chainguard's Container Registry to Artifactory"
linktitle: "Container Pull-through"
aliases: 
- /chainguard/chainguard-registry/artifactory-pull-through/
- /chainguard/chainguard-registry/pull-through-guides/artifactory-pull-through/
- /chainguard/chainguard-registry/pull-through-guides/artifactory/artifactory-images-pull-through/
type: "article"
description: "Tutorial outlining how to set up a remote Artifactory repository to pull images through Chainguard's container registry."
date: 2024-02-13T15:56:52-07:00
lastmod: 2026-02-18T15:56:52-07:00
draft: false
tags: ["Chainguard Containers"]
images: []
menu:
  docs:
    parent: "artifactory"
toc: true
weight: 005
---

Organizations can route container image pulls through Artifactory to centralize artifact management, enforce policy, and integrate Chainguard Containers into existing CI/CD workflows. You can configure Artifactory as a pull-through cache by setting up a remote repository pointed at [Chainguard's container registry](https://edu.chainguard.dev/chainguard/chainguard-registry/overview/).

This tutorial outlines how to set up remote repositories with [JFrog Artifactory](https://jfrog.com/artifactory/). Specifically, it goes over how to set up one repository you can use as a pull-through cache for Chainguard's public [Free Containers](/chainguard/chainguard-images/about/images-categories/#starter-containers) and another you can use for [Production Containers](/chainguard/chainguard-images/about/images-categories/#production-containers) originating from a private Chainguard repository. It also outlines how you can use one of Artifactory's [virtual repositories](https://jfrog.com/help/r/jfrog-artifactory-documentation/virtual-repositories) as a pull-through cache to access resources from multiple remote repositories in a single location.


## Prerequisites

To complete this tutorial, you need the following:

* Administrative privileges over an Artifactory instance. If you're interested in testing out this configuration, you can set up a trial instance on the [JFrog Artifactory landing page](https://jfrog.com/artifactory/).
* Docker installed on your local machine. Refer to [the official documentation](https://docs.docker.com/engine/install/) to set this up.

Part of this guide assumes you have access to a private registry provided by Chainguard with one or more Production container images. If you don't already have access to these, you can [contact our sales team](https://www.chainguard.dev/contact?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement). To complete this portion, you will also need the following:

* Permissions to pull container images from your organization's private Chainguard registry. At minimum, you must be granted the `registry.pull` role, but other built-in roles like `owner`, `editor`, or `viewer` will also work. Refer to our guide on [Built-in Roles and Capabilities Reference](/chainguard/administration/iam-organizations/roles-role-bindings/capabilities-reference/#pull-token-creator-roles) for more details.
* `chainctl`, Chainguard's command line interface tool, installed on your local machine. To set this up, follow our [installation guide for `chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/).


## Setting Up Artifactory as a Pull-through Cache for Free Containers

Chainguard's Free Containers are free to use, publicly available, and always represent versions tagged as `:latest`.

To set up a remote repository in Artifactory from which you can pull Chainguard Free Containers:

1. Log in to the JFrog platform.
2. Select the **Administration** tab near the top of the screen.
3. Select **Repositories** from the left-hand navigation menu. 
4. On the Repositories page, click **Create a Repository**.
5. Select the **Remote** option.
6. In the **Select Package Type** window, select **Docker**.

This takes you to a **Basic** configuration tab where you can enter the following details for your new remote repository:

* **Repository Key** — This is the name used to refer to your repository. You can choose whatever name you like here, but this guide's examples use the name `cgr-public`.
* **URL** — This must be set to `https://cgr.dev/`.
* **Include Patterns** — Ensure that you use the default value (`**/*`) in this field.
* **Enable Token Authentication** — Ensure this setting (under **Docker Settings**) is enabled. This is required, as you must authenticate to the remote repository in order to pull Chainguard Containers through it.
* **Block Mismatching Mime Types** — In the **Advanced** configuration tab, ensure that this option option is checked.

Following that, click **Create Remote Repository**. Next, you can test that you're able to pull a Chainguard Free Container through the remote repository.

### Testing pull-through of a Chainguard Free Container

Before testing whether you're able to pull Chainguard's Free Containers through the remote Artifactory repository, you must retrieve a token generated by Artifactory for your remote repository. Expand the following section to retrieve a token and authenticate:

{{< details "JFrog Artifactory Token Retrieval" >}}
{{< blurb/jfrog-token >}}
{{< /details >}}

After running the `docker login` command, you will be able to pull a Chainguard Free Container through Artifactory. The following example pulls the `go` container image:

```sh
docker pull <my-project>.jfrog.io/cgr-public/chainguard/go
```

Be sure the `docker pull` command you run includes the name of your project as well as your own repository key in place of `cgr-public`, if different.


## Setting Up Artifactory as a Pull-through Cache for Production Containers

Production Chainguard Containers are enterprise-ready container images that come with patch Service Level Agreements (SLAs) and features such as [Federal Information Processing Standard](/chainguard/chainguard-images/working-with-images/fips-images/) (FIPS) readiness. The process for setting up an Artifactory repository that you can use as a pull-through cache for Chainguard Production Containers is similar to the one outlined previously for Free Containers, but with a few extra steps.

To get started, create [a pull token](/chainguard/chainguard-registry/authenticating/#authenticating-with-a-pull-token) for your organization's registry. Pull tokens are longer-lived tokens that can be used to pull Chainguard Containers from other environments that don't support OIDC, such as some CI environments, Kubernetes clusters, or registry mirroring tools like Artifactory.

To create a pull token with `chainctl`, run the following command: 

```sh
chainctl auth configure-docker --pull-token --parent <organization>
```

Be sure to replace `<organization>` with your organization's name or ID.

> **Note**: You can find your Chainguard organization's name or ID by running `chainctl iam organizations list -o table`.

This command returns a `docker login` command like the following:

```output
. . .

    docker login "cgr.dev" --username "<pull_token_ID>" --password "<password>"
```

Record the values for `<pull_token_ID>` and `<password>` as you'll need these credentials when you configure a new remote Artifactory repository for pulling through Production Containers.

After noting your credentials, you can begin setting up an Artifactory repository from which you can pull Chainguard Production Containers. This process is similar to the one outlined previously: 

1. Log in to the JFrog platform.
2. Select the **Administration** tab near the top of the screen.
3. Select **Repositories** from the left-hand navigation menu. 
4. On the Repositories page, click **Create a Repository**.
5. Select the **Remote** option.
6. In the **Select Package Type** window, select **Docker**.

Next, enter the following details for your new remote repository in the **Basic** configuration tab:

* **Repository Key** — Choose whatever name you like here, but this guide's examples use the name `cgr-private`.
* **URL** — This must be set to `https://cgr.dev/`.
* **User Name** — Enter the `<pull_token_ID>` value you noted from the `docker login` command.
* **Password / Access Token** — Enter the `<password>` value you noted from the `docker login` command.
* **Include Patterns** — Ensure that you use the default value (`**/*`) in this field.
* **Enable Token Authentication** — Ensure this setting (under **Docker Settings**) is enabled. This is required, as you must authenticate to the remote repository in order to pull Chainguard Containers through it.
* **Block Mismatching Mime Types** — In the **Advanced** configuration tab, ensure that this option option is checked.

Finally, click **Create Remote Repository**. You can then move on to testing that you're able to pull Chainguard Production container images through this remote repository.

### Testing pull-through of a Chainguard Production Container 

As with the `cgr-public` repository example, you must retrieve a token generated by Artifactory for your repository before testing whether you're able to pull Chainguard Production container images through the remote repository you just created. Expand the following section to retrieve a token and authenticate:

{{< details "JFrog Artifactory Token Retrieval" >}}
{{< blurb/jfrog-token >}}
{{< /details >}}

After running the `docker login` command, you will be able to pull Chainguard Production Containers through Artifactory. The following example pulls the `chainguard-base` image if your organization has access to it:

```sh
docker pull <my-project>.jfrog.io/cgr-private/<organization>/chainguard-base:latest
```

Be sure the `docker pull` command you run includes the name of your Artifactory project and the name of your organization's registry. Additionally, if you entered a different repository key in the setup section, use it in place of `cgr-private`.


## Setting Up an Artifactory Virtual Repository as a Pull-through Cache

Artifactory allows you to create what it refers to as [*virtual repositories*](https://jfrog.com/help/r/jfrog-artifactory-documentation/virtual-repositories). A virtual repository is a collection of one or more repositories (such as local, remote, or other virtual repositories) that have the same package type. The benefit of this is that you can access resources from multiple locations using a single logical URL.

You can also use a virtual repository as a pull-through cache. To set this up, create a new virtual repository:

1. Navigate to the **Repositories** tab.
2. Click **Create a Repository**.
3. Select the **Virtual** option.
4. In the **Select Package Type** window, select **Docker**.

When you reach the **New Virtual Repository** page, enter a key of your choosing into the **Repository Key** field. This guide's examples refer to this repository as `cgr-virt`.

Next, you must select existing repositories to include within this virtual repository. To keep things simple, this guide uses the `cgr-public` and `cgr-private` repositories created previously. Select your repositories by clicking their respective checkboxes. Then be sure to click the right-pointing chevron to move them to the **Selected Repositories** column.

Finally, click **Create Virtual Repository**. Then, you can retrieve the token and `docker login` command as before.

### Testing pull-through with a virtual repository

As with the previous examples, you must retrieve a token generated by Artifactory before testing whether you're able to pull Chainguard Containers through the virtual repository. Expand the following section to retrieve a token and authenticate:

{{< details "JFrog Artifactory Token Retrieval" >}}
{{< blurb/jfrog-token >}}
{{< /details >}}

After retrieving your token and logging into `docker`, you will be able to pull Chainguard Containers through the Artifactory virtual repository.

To pull a public image, you would run a command like the following, which pulls the public `mariadb` image:

```sh
docker pull <my-project>.jfrog.io/cgr-virt/chainguard/mariadb:latest
```

To pull a Production Container, replace `chainguard` with the name of your organization's registry. The following example pulls the `chainguard-base` image if your organization has access to it:

```sh
docker pull <my-project>.jfrog.io/cgr-virt/<organization>/chainguard-base:latest
```

For both of these commands, be sure the `docker pull` command you run includes the name of your Artifactory project and the name of your organization's registry. Also, if you used a different repository key, substitute it for `cgr-virt` in the previous commands.


## Debugging Pull-through from Chainguard’s Registry to Artifactory

If you run into issues when trying to pull images from Chainguard's container registry to Artifactory, ensure the following requirements are met:

* Ensure that all Containers [network requirements](/chainguard/chainguard-images/network-requirements/) are met.
* If you attempt to pull a nonexistent image via pull-through, Artifactory will also make calls to `chainguard.dev` and `www.chainguard.dev`. Calls to these domains should not occur when pulling a valid image.
* When configuring a remote Artifactory repository, ensure that the **URL** field is set to `https://cgr.dev/`. This field **must not** contain additional components. 
* You can troubleshoot by running `docker login` from another node (using the Artifactory pull token credentials) and then trying to pull a Container from `cgr.dev/chainguard/<image name>` or `cgr.dev/<organization>/<image name>`.
* It may help to [clear the Artifactory cache](https://jfrog.com/help/r/artifactory-cleanup-best-practices/clearing-an-oversized-cache).
* Your Artifactory repository may be misconfigured. In this case, create and configure a new remote Artifactory repository to test with.


## Learn more

If you haven't already done so, you may find it useful to review our [Registry Overview](/chainguard/chainguard-registry/overview/) to learn more about the Chainguard container registry. You can also learn more about Chainguard Containers by referring to our [Containers documentation](/chainguard/chainguard-images/overview/). If you'd like to learn more about JFrog Artifactory, refer to the [official Artifactory documentation](https://jfrog.com/help/r/jfrog-artifactory-documentation).
