---
title: "Using the Chainguard Directory and Console"
linktitle: "Containers Directory"
aliases: 
- /chainguard/chainguard-images/working-with-images/images-directory
type: "article"
description: "A walkthrough of the Chainguard directory and console."
date: 2024-02-23T11:07:52+02:00
lastmod: 2025-10-23T11:07:52+02:00
draft: false
tags: ["Chainguard Containers"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 020
toc: true
---

There are hundreds of Chainguard Containers available for use. To help users explore and better understand all of these container images, we've developed the Chainguard Directory. This guide serves as a walkthrough of the browsing experience for Chainguard Containers in the Directory and Console, including how to access it and get the most out of its features.


## Accessing the Chainguard Directory and Console

This guide is primarily framed around the Chainguard Directory and the Chainguard Console. The Directory is public facing and doesn't require any authentication to access it. The Console is also accessible to anyone, including users who aren't Chainguard customers. However, to access the Console, you'll first need to [create an account and log in](https://console.chainguard.dev/auth/login).

If you would like to open the console with your Organization already selected, you can use (and bookmark) a link like this, replacing `ORGANIZATION` with your organization's name:

```html
https://console.chainguard.dev/auth/login?org=ORGANIZATION
```

If you're not ready to create a Chainguard account, you can follow along with the public [Chainguard Directory](https://images.chainguard.dev/?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-working-with-images-images-directory). As of this writing, there are some differences between the two websites, but both should provide a similar experience for browsing Chainguard Containers.


## Browse Chainguard Containers

The Chainguard Console and Directory offer slightly different experiences for browsing container images.

### Browsing in the Console

After signing in to the [Chainguard Console](https://console.chainguard.dev), your browser will take you to the Overview page:

<center><img src="imgs-dir-A.png" alt="Screenshot showing the Chainguard Console's Overview page." style="width:1100px;"></center>
<br /> 

Click **Images** in the left-hand navigation. By default, takes you to the **Organization** images tab. If you're part of an organization, you may have access to private Chainguard Containers (or *Production Containers*) that can be found here. 

Navigate to the **Chainguard catalog** tab. There, you'll be presented with a list of all of Chainguard's available images:

<center><img src="imgs-dir-B.png" alt="Screenshot of the public container images directory in the Console. The table is sorted by the 'Updated' column in descending order, meaning that the most recently updated container images are shown first." style="width:1100px;"></center>
<br /> 

The **Chainguard catalog** tab has a table with four columns:

* **Name**: the name of each given container image
* **Latest tag**: the latest available version of the image
* **Description**: a brief description of each container image
* **Updated**: how long it's been since the container image was last updated

Additionally, container images listed in the **Organization** container images tab have an extra column labeled **Status**. This column specifies what resources an organization has purchased and has access to. This column can show one of two possible values: **Active**, meaning that your organization is able to download and use the container image, or **Expired**, meaning that your organization had access to the container image in the past but not anymore:

<center><img src="imgs-dir-C.png" alt="Screenshot showing a portion of an Organization container images directory, including the 'Status' column. This example shows five container: metrics-server, a customized metrics-server image, mongodb, nginx, and node." style="width:700px;"></center>
<br /> 

You can click on any of these column names to sort the list of container images in ascending or descending order based on the values in these columns.

Above the table is a search box you can use to find specific container images by their name or latest version number. To the right of this box is a drop-down menu labeled **Category**. You can use this to filter the images listed based on which of [Chainguard's Container Image categories](/chainguard/chainguard-images/about/images-categories/) they belong to.

### Browsing in the Directory

The [Chainguard Containers Directory](https://images.chainguard.dev/) landing page has a card-based layout of container images:

<center><img src="imgs-dir-D.png" alt="Screenshot of the Chainguard Containers Directory landing page, showing nine cards representing nine featured container images. The 'Featured' category is selected in the left-hand menu." style="width:1100px;"></center>
<br /> 

Each card represents a container image available from Chainguard, and shows the image's name and logo, when it was last changed, the latest tag available. These cards include other details when relevant, like whether the image is part of Chainguard's free tier of Starter Containers, if there is a FIPS-enabled version of the container image available, or if it's a STIG-hardened image.

By default, the Directory only shows a set of featured container images. You can select other categories of container images to view from the menu to the left of the cards. This menu has the following options:

* **Featured**
* **Starter**
* **AI**
* **Application**
* **Base** 
* **FIPS**

Below this menu is a button labeled **View all images** which you can click to view all the images at once. Above the cards is a search box you can use to search for specific Chainguard Containers. Clicking on any card or search result takes you to that container image's details page.

## Container image information

Next, let's inspect an individual container image. Click on any container image you'd like. This example shows the page for `argocd` in the Console:

<center><img src="imgs-dir-E.png" alt="Screenshot of the Container Details page for the argocd image, showing the 'Tags' tab." style="width:1100px;"></center>
<br /> 

Each container image details page has several tabs that provide information about various facets of the given image.


### Tags

The default page for each image is the **Tags** tab which contains information about the version tags available for each image. This contains a table with columns:

* **Tag**: this column lists each tag available for the container image
* **Pull URL**: the URL you can use to download each version of the image. In the Console, Production containers you don't already have access to will show a message reading `Add to organization for access` if you're logged in under an organization with access to Production Containers; if you're logged in under an unverified organization, the message reads `Request image for access`. In the Directory, this message reads `Contact us for access to this image` with a link to Chainguard's [contact form](https://www.chainguard.dev/contact?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement)
* **Compressed size**: the size of the image, in megabytes
* **Last changed**: when each version of the image was last updated

Above the table is a search box which you can use to filter the different versions available for the image. There is also a **Variant** drop-down menu you can use to filter for all images, only development variants, or only non-development variants.

### Overview

The **Overview** tab contains the container image's README. Typically, READMEs include instructions on how to download the container image, any relevant compatibility notes, and instructions on how to get started with using the image.

### Comparison

The **Comparisons** tab includes useful data that shows how a given Chainguard Container compares against a non-Chainguard alternative in terms of CVE count. It also includes helpful visualizations of these comparisons. For more information, check out our guide on [CVE Visualizations](/chainguard/chainguard-images/features/cve_visualizations/).

### Provenance

All Chainguard Containers contain verifiable signatures and high-quality [software bills of materials](/open-source/sbom/what-is-an-sbom/) (SBOMs). These features allow you to confirm the origin of each image and provide you with a detailed list of everything included in the container image.

The **Provenance** tab outlines how you can verify container signatures and download and verify container image attestations, all with examples using [`cosign`](/open-source/sigstore/cosign/an-introduction-to-cosign/).

### Specifications

The **Specifications** tab is where you can find a number of important details about a given container image, such as whether it ships with the `apk` package manager or a shell. It also includes information like the image's default user ID, environment variables, and its entrypoint.

It also shows the container image's **Raw configuration**, which includes many of these details as well as its OCI labels (similar to [annotations](/chainguard/chainguard-images/overview/#annotations)). 

<center><img src="imgs-dir-F.png" alt="Screenshot showing the 'Specifications' tab for the argocd image." style="width:1100px;"></center>
<br />

### SBOM

The **SBOM** tab contains a list of packages in the image. Chainguard Containers are built so that everything contained in the image is a package, meaning that this package list gives a complete view of what's in the container image. You won't find anything hidden in the image that isn't listed in its SBOM tab.

<center><img src="imgs-dir-G.png" alt="Screenshot of the argocd container image's 'SBOM' tab, showing nine rows of the latest version's SBOM." style="width:1100px;"></center>
<br />

The table listing an image's packages has four columns.

* **Package**: the name of each package included in the image's SBOM
* **Version**: the version of the listed package
* **Repository**: every package found in Chainguard Containers is either built and managed by the Chainguard team or sourced from [Wolfi](/open-source/wolfi/overview/). For packages falling into the latter category, this column will include a link to the [Wolfi GitHub repository](https://github.com/wolfi-dev/os) showing the package source
* **License**: the license under which each package is published

Above the table is a search box you can use to find and filter the packages listed. To the left of this search box is a drop-down menu you can use to select which version of the image you want to find the SBOM for as well as what architecture (either x86_64 or arm64). 

Finally, to the right of the search box is a button labeled **Download SBOM**. If the image is a free Starter Container or a container image your organization has access to, you can click this button to download the SBOM (in the SPDX format) to your machine.

Note that Chainguard began generating SBOMs for its images on November 15, 2023. For this reason, any versions of a given container image that were released before that date will not have any SBOM data to show. 

### Vulnerabilities

The **Vulnerabilities** tab contains a list of every CVE one can find within the image. As with the SBOMs tab, the Vulnerabilities tab has a search box you can use to find and filter specific vulnerabilities within the image. There is also a drop-down menu to the left allowing you to select different versions of the container image.

Below these is a table listing the vulnerabilities. However, most Chainguard Containers won't show any vulnerabilities for the `latest` version. This isn't an error, as we aim to remove vulnerabilities from images as soon as they arise.

To illustrate how this table appears when vulnerabilities are actually present, you can select different versions in the drop-down until you find one with a vulnerability. This example shows the vulnerabilities in version `3.1.7` of the `argocd` image.

<center><img src="imgs-dir-H.png" alt="Screenshot of the argocd image's 'Vulnerabilities' tab, with '3.1.7' selected in the Tag drop-down menu. The table shows four rows, all highlighting the same vulnerability (CVE-2025-30258) but associated with different packages: gnupg, gnupg-gpgconf, gpg, and gpg-agent." style="width:1100px;"></center>
<br />

The Vulnerabilities table has five columns.

* **CVE ID**: the official identification number of each vulnerability present in the table
* **Severity**: the severity of each given vulnerability. This can either read **Critical**, **High**, **Medium**, **Low**, or **Unknown**
* **Package**: the package where the vulnerability was found
* **Version**: the version of the package containing the vulnerability
* **Last detected**: the date and time when the vulnerability last appeared in a scan of the container image

To the left of each row in the table is down-pointing chevron (**˅**). Clicking on this expands the row to show more information about the given vulnerability.

<center><img src="imgs-dir-I.png" alt="Screenshot showing the expanded view of the 'CVE-2025-30258' vulnerability. This expanded view includes a brief description of the CVE as well as some reference links." style="width:1100px;"></center>
<br />

Specifically, this highlights the **Package** name and **Version** number of the package associated with the vulnerability. It also shows the **Fixed version** of the package, a brief **Description** of the vulnerability, and one or more **References** you can review to learn more about the vulnerability.

Please be aware that, as with SBOM data, Chainguard began generating vulnerability information for its images on November 15, 2023. For this reason, any versions of a given image that were released before that date won't have any vulnerability data to show. 

### Advisories

When you scan a newly-built Chainguard Container with a vulnerability scanner, the scanner typically won't report any CVEs. However, as software packages age, more vulnerabilities are reported and CVEs will begin to accumulate in images. When this happens, Chainguard releases security advisories to communicate these vulnerabilities to downstream container image users. You can find all the advisories issued for a given image in its Advisories tab. 

This tab contains a timeline of each security advisory released for a given container image, starting with the most recent. Each entry specifies the date and time the advisory was released, the CVE in question, the affected package, and the [current status](/chainguard/chainguard-images/staying-secure/security-advisories/how-chainguard-issues/#summary-of-advisory-statuses). 

To learn more about Chainguard security advisories, we encourage you to read our article on [How Chainguard Issues Security Advisories](/chainguard/chainguard-images/staying-secure/security-advisories/how-chainguard-issues/) as well as our guide on [How to Use Chainguard Security Advisories](/chainguard/chainguard-images/staying-secure/security-advisories/how-to-use/). You an also find every security advisory published for Chainguard Containers by exploring our self-service [Security Advisories page](https://images.chainguard.dev/security?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-working-with-images-images-directory).

### Builds

Chainguard Containers viewed in the Console have an additional **Builds** tab. However, this tab is only accessible if the container image in question has been customized with Chainguard's [Custom Assembly](/chainguard/chainguard-images/features/ca-docs/custom-assembly/) tool.

Our guide on [Using the Chainguard Console to Manage Custom Assembly Resources](/chainguard/chainguard-images/features/ca-docs/custom-assembly-console/) provides an in-depth overview of the Builds tab, as well as working with Custom Assembly in the Chainguard Console.


## Learn More

The Chainguard Console and Containers Directory are useful tools for understanding what Chainguard Containers are available. To better understand how to work with individual container images, you can see if we have a [getting started guide](/chainguard/chainguard-images/getting-started/) available. We also provide a guide on [how to view security advisories](/chainguard/chainguard-images/security-advisories/) through our [self-service public Security Advisories page](https://images.chainguard.dev/security?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-working-with-images-images-directory).