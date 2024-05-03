---
title: "Chainguard Images End-of-Life Notifications"
linktitle: "EOL Notifications"
aliases:
- /chainguard/chainguard-images/images-features/eol-notifications
lead: "Email-based alerts for EOL events"
type: "article"
description: "User notifications for end-of-life events related to Chainguard Images"
date: 2024-04-30T08:49:31+00:00
lastmod: 2024-04-30T15:22:20+01:00
draft: false
tags: ["Chainguard Images", "Product", "Reference"]
images: []
toc: true
weight: 070
---

Chainguard Images are continually rebuilt with the latest patches released by upstream software. Any time a new software version is released in the open source project, a new Chainguard Image will be built automatically.

Chainguard creates "[version streams](/chainguard/chainguard-images/versions/)" for significant release tracks of open source software, so that each active release of an upstream application always receives every patch that is released for it. 

When an upstream release track comes to an end, and stops receiving updates, the Chainguard Image also stops receiving updates for that software. This is considered to be an **end-of-life (EOL)** event. 

For certain Chainguard Images, customers can receive email notifications when the Image stops receiving updates, in order to plan a transition to a newer, maintained version.

## Criteria for End-of-Life Email Notifications

The following criteria must by met in order to qualify for an end-of-life email notification:

* A given Image has been pulled in your organization registry within the last 30 days.
* A given Image must be based on software with multiple concurrent release tracks, according to our [Product Release Lifecycle document](/chainguard/chainguard-images/versions/). 
    * This means that any Image that only maintains a [single stream of release versions](/chainguard/chainguard-images/versions/#single-release-track-maintained-by-a-given-open-source-project) at a time will not receive EOL notifications. 
* The software that a given Chainguard Image is named for (the main software package in the Image) must reach an EOL milestone according to Chainguard's internal records, which are based on the records at [endoflife.date](https://endoflife.date/).
* Chainguard must have an updated tag available to pull in your organization registry.

If you have questions or concerns about a particular Image, please contact Chainguard Support or your Customer Success Manager.

## How End-of-Life Notifications Work

On the day the Chainguard Image reaches end-of-life status, organizations with recent pulls of that Image from their organization registry will receive an email notification. 

The notification will show which Image has reached EOL and will suggest a newer tag available for updates.

On that day, the EOL Image will also stop receiving patch updates from Chainguard.

The EOL Image will remain available in the organization registry and customers are free to continue using it. However, it is expected that vulnerabilities will accrue in that Image over time that will remain unpatched.

Customers are advised to update their internal usage to a newer version of the image.

## Who Receives End-of-Life Notifications

EOL email notifications will be sent to organization contacts determined by that organization's customer success manager. It is not always possible to direct these messages to users actually pulling the EOL image, since many pulls are performed by anonymous pull tokens and service accounts, so the notification will be sent to an organization administrator or primary contact.

## Unsubscribing

Since these notifications are considered part of the fullfillment of your Chainguard contract, there is no unsubscribe link available in the email footer. However, if you wish to be excluded from these emails, please contact Chainguard Support or your Customer Success Manager for assistance.


