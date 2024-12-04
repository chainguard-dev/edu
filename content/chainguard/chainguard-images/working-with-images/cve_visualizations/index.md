---
title: "Using CVE Visualizations"
linktitle: "CVE Visualizations"
type: "article"
description: "Getting started with the CVE Visualization feature."
date: 2024-12-04T11:07:52+02:00
lastmod: 2024-12-04T11:07:52+02:00
draft: false
tags: ["CONCEPTUAL", "CHAINGUARD IMAGES", "PRODUCT"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 020
toc: true
---

The CVE Visualizations feature helps teams measure the engineering, security and economic
benefits gained from using Chainguard Images. The primary feature is a comparison of CVE counts in
Chainguard Images vs equivalent images from other sources.

NOTE: This is a beta feature and changes should be expected. In particular, we plan to add more
metrics such as counts of CVEs identified and remediated, MTTR and image size comparisons.


## Accessing CVE Visualizations

Visualizations can be found at http://console.chainguard.dev/reports and via the "Reports" section
on the left-hand navigation bar.

The reports page should look similar to the following:

![Screenshot showing CVE Visualization Report](cve_report.png)


The top left drop down in the main page is used to select the Chainguard image you want to compare.
Once an image is selected, a second drop down will be populated with data on "alternative" images,
if available. In some cases there will be more than one alternative available, in which case you can
select between them using the drop down.

The period drop down is used to select a time-period for the report.

Below the controls, you will find several boxes with statistics and graphs:
  - An overview section showing the current and average CVE counts for the images
  - The "CVEs by Severity" section holds bar graphs showing the CVE count per day for both
    images, broken down by severity. Any grey bars indicate we are missing data for that day.
  - The "Total CVEs over time" section shows a line graph with the total number of CVEs for any
    given day for each image. This gives a simple visual comparison of the difference in CVE
    count between the images.

![Screenshot showing CVEs Over Time graph](cves_over_time.png)

You will also see the same comparison data when navigating to a specific image in your Organization
images, under the "Comparison" tab.

## Limitations

We only have data for a limited subset of alternative images. We will expand this set over time, but
please let us know of any particular comparison data you are looking for.

