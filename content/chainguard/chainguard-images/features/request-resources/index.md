---
title: "Requesting New Chainguard Resources"
linktitle: "Requesting Resources"
type: "article"
description: "How to submit requests for Chainguard to build new resources in the Console."
date: 2026-02-26T11:07:52+02:00
lastmod: 2026-02-26T11:07:52+02:00
draft: false
tags: ["Chainguard Containers", "Chainguard Console"]
images: []
menu:
  docs:
    parent: "features"
weight: 015
toc: true
---

The Chainguard Console now includes the Requests section where customers can submit and track requests for resources that Chainguard doesn't currently offer. This improves transparency around which technologies Chainguard is working to build and helps minimize duplicate build requests.

This guide provides an overview of how to submit a request for a new resource to Chainguard, as well as the limitations on what resources can be built.

> **Note**: As of this writing, the Requests section is in beta. Some of the details and instructions included in this guide are likely to change over time.


## Prerequisites

In order to submit requests for new resources in the Chainguard Console, you must be part of a [verified organization](/chainguard/administration/iam-organizations/verified-orgs/). Users with access to only Chainguard's free tier of container images will not be able to submit requests.


## The Requests section

To begin, navigate to the [**Requests** section of the Chainguard Console](https://console.chainguard.dev/org/chainguard/requests/active). This section includes three tabs:

* **My requests**, showing any requests you've initiated or upvoted
* **Active builds**, which includes any resources the Chainguard team is in the process of building
* **Community requests**, showing all the resource requests not currently being built

Each of these tabs contains a table with the following columns:

* A column at the far left where you can upvote requests.
* The **Name** of the resource requested.
* The request's **Status**. This can be one of the following:
    * **Future**
    * **In progress**
    * **Paused**
    * **Reviewing**
    * **Won't build**
* If the original requester included them, **Project Details** that describe the resource being requested

Additionally, the **Community requests** tab includes a **Demand** column, showing what demand percentile the request falls into. Also, the **Active builds** tab includes an **Estimated delivery** column which shows when Chainguard expects the resource to be available. 


## Requesting new resources

Within each tab in the **Requests** section of the console is a button labeled **New request**. Clicking this button will open a modal window where you can enter the details of your resource request. 

This window contains several fields. The following are required for you to submit a request:

* **Type** — Specify the type of resource you're requesting, either an **Image**, a **Package**, or a **Helm chart**.
* **Name** — Enter the existing public name of the resource you're requesting.
* **Open Source project repository** — Include a link to a public repository containing the source code for the open source project you're requesting.
* **Include FIPS-validated variant?** — Select either **Yes** or **No**. 
* Additionally, you must confirm that none of Chainguard's existing artifacts or requests match your request.

There are also a few optional fields you can fill in:

* **Project Dockerfile** — Include a URL to a Dockerfile for the application that includes a build definition; if the project does not include a Dockerfile, provide as much build information as possible.
* **Dependencies** — Specify any other resources the artifact you're requesting needs to function.
* **Deployment method** — Specify how you plan to use this resource; for example, if you're requesting an image, you can specify that you plan to run it using Helm, Cloud Run, Argo, Docker, etc.

Although these fields aren't required, filling them in provides Chainguard with more context for your request and can help speed up the approval process.

After filling out the form, click the **Request image** button to submit your request. Your request will then appear in both the **My requests** and **Community requests** tabs, and other customers will be able to upvote it.

The Chainguard team will then review the request and prioritize it based on demand, as determined by the number of upvotes the request has received from users.


## Limitations

There are a few limitations you should consider before submitting a new request:

* Chainguard will not build resources based on proprietary code.
    * Note that some projects distributed under open source licenses have strict terms that prevent Chainguard from building artifacts based on them.
* If a project is no longer receiving updates or releases, Chainguard typically won't build it since there aren't reliable security fixes upstream.
* There are cases where Chainguard cannot fulfill a FIPS request and be FIPS compliant. In such cases, the standard variant can often still be built but the FIPS variant will get marked as **Won't build**.

Finally, be aware that requesting that Chainguard build a software artifact does not mean it will automatically be accessible to your organization. Once the resource is built, you can reach out to our sales team to add it to your organization; alternatively, if your organization has [Catalog Pricing](/chainguard/chainguard-images/about/pricing/) enabled, you can add it yourself after it's built.
