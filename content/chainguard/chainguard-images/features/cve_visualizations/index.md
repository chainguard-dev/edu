---
title: "Using CVE Visualizations"
linktitle: "CVE Visualizations"
aliases:
- /chainguard/chainguard-images/working-with-images/cve_visualizations/
- /chainguard/chainguard-images/features/cve_visualizations/
type: "article"
description: "Getting started with the CVE Visualization feature."
date: 2024-12-19T11:07:52+02:00
lastmod: 2025-03-21T11:07:52+02:00
draft: false
tags: ["Conceptual", "Chainguard Containers", "Product", "Reference"]
images: []
menu:
  docs:
    parent: "features"
weight: 025
toc: true
---

Chainguard provides CVE Visualizations for all of its container images. This feature creates reports with CVE comparisons between Chainguard Containers and popular alternatives, as well as historical CVE remediation metrics. CVE Visualizations provide insight into image health and can help teams measure the engineering, security, and economic benefits gained from using Chainguard Containers.

This guide outlines how you can access a container image's CVE Visualization in both the Chainguard Console and in the Containers Directory. 


## Accessing CVE Visualizations in the Console

You can find CVE Visualizations and reports two separate places in the [Chainguard Console](https://console.chainguard.dev): in the **Reports** section of the left-hand navigation menu and in the **Comparison** tab of an individual Container's overview.

### Reports section

Visualizations can be found under the [**Reports**](https://console.chainguard.dev/reports) section in the left-hand navigation bar.

The Reports page will look similar to the following:

<center><img src="cve-viz-1.png" alt="Screenshot showing CVE Visualization Report page, with the Python container image selected." style="width:1100px;"></center>
<br /> 

At the top of the Reports page will be two tabs: **Compare Containers** and **Historical CVEs**. Let's first review the Compare Containers tab.

At the top left of the Compare Containers tab is a drop-down menu which you can use to select the Chainguard Container you want to compare. The contents of this menu are organized in alphabetical order, starting with Organization Containers at the top (if your selected organization has access to specific Chainguard Containers) followed by free-tier Chainguard Containers.

<center><img src="cve-viz-2.png" alt="Screenshot showing the image selection drop-down menu in the Reports page." style="width:500px;"></center>
<br /> 

After you select a container image, a second drop-down will appear. This will be populated with data on "alternative" images which (if available) you can compare against the selected Chainguard Container. In some cases there will be more than one alternative available, in which case you can select between them using the drop-down. To the right of the alternatives menu you can select a time range for the report.

Below the controls, you will find several boxes with statistics and graphs:

* An overview section showing the current and average CVE counts as well as container image size for the images.
* A **CVEs by Severity** section with bar graphs showing the CVE count per day for both images, broken down by severity.

> **Note**: Be aware that this section also includes an **Export** button you can use to download this data as a JSON file. 

* A **Total CVEs Over Time** section showing a line graph with the total number of CVEs for any given day for each container image. This provides a visual comparison of the difference in CVE count between the images.
* A **Cumulative CVEs Identified** section,  with a line graph showing the total number of newly identified CVEs since the beginning of the time range selected, for each image. This provides a visual comparison of the CVE accumulation rate between the images.

<center><img src="cve-viz-3.png" alt="Screenshot showing CVEs Over Time and Cumulative CVEs Identified graphs. The CVEs Over Time graph shows that the Chainguard Container regularly has few or zero CVEs while the alternative jumps between 10 and 80 CVEs. The Cumulative CVEs Identified graph ends with nearly zero CVEs for the Chainguard Container and over 80 for the alternative." style="width:1100px;"></center>
<br /> 

The **Historical CVEs** tab shows data relating to CVEs that have appeared over the past three months in container images that your organization has access to. Be aware that the totals shown only represent your Organization Containers, and not free-tier images. 

> **Note**: If you are a member of more than one organization you can switch to another organization by clicking the drop-down menu in the top left corner of the Console. 

The **Historical CVEs** tab has two boxes. The first box is labeled **Resolved CVEs in Organization Containers** and shows a bar chart displaying the number of resolved CVEs by date over the last three months. The second box is labeled **Total Resolved CVEs by Severity** and shows a horizontal bar chart showing all the resolved CVEs from the past three months. In both graphs, the CVEs are color-coded by severity.

<center><img src="cve-viz-4.png" alt="Screenshot from an example Historical CVEs tab in the Reports section of the Chainguard Console. This example shows that there have been ten resolved CVEs in the last three months, with one being a High severity CVE and the rest Unknown." style="width:1100px;"></center>
<br /> 

### Comparison tab

You can find this same comparison data when navigating to a specific container image in either the **Browse Containers** section or in your **Organization Containers**. After navigating to either of these sections, click on or search for any image you like.

By default, you will be taken to the container image's **Versions** tab. Click on the **Comparison** tab at the far right. There, you'll be presented with the same comparison information found in the **Reports** section. At the top are some control menus, allowing you to select the date range for the comparison and, if available, the alternative you'd like to compare the Chainguard Container against. This example shows the PHP container image:

<center><img src="cve-viz-5.png" alt="Screenshot of the Chainguard PHP image's Comparison tab in the Browse Containers section of the Chainguard Console, with data showing how it compares against the php:latest image." style="width:1100px;"></center>
<br /> 


## Accessing CVE Visualizations in the Containers Directory

Similar to the CVE reports found in the **Browse Containers** and **Organization Containers** section of the Chainguard Console, you can find CVE reports for every one of Chainguard's container images in the [Containers Directory](https://images.chainguard.dev/).

After navigating to the directory, click on or search for any container image you like. Again, you will be taken to the image's **Versions** tab by default. Click on the **Comparison** tab at the right to view the CVE Comparison data. This example shows the nginx image:

<center><img src="cve-viz-6.png" alt="Screenshot from Chainguard's Public Containers Directory showing a portion of the Chainguard nginx image's Comparison tab, with data showing how it compares against the nginx:alpine image." style="width:1100px;"></center>
<br /> 


## Limitations

Some container images do not currently have a comparative alternative. In these cases, the Comparison report will only show data for the Chainguard Container. 

## Learn More

The CVE data used in these reports is from the [Grype vulnerability scanner](/chainguard/chainguard-images/staying-secure/working-with-scanners/grype-tutorial/). Vulnerability data is constantly evolving, so we scan container images each day and store the results. The results shown are the vulnerabilities found on the day in question; scanning the container images again with a newer database will show different results.

For more information on CVEs see [What Are Software Vulnerabilities and CVEs](/software-security/cves/cve-intro/). You may also find our guide on [Using the Chainguard Directory and Console](/chainguard/chainguard-images/how-to-use/images-directory/) to be of interest.