---
title: "Using the Compliance Dashboard in the Chainguard Console"
linktitle: "Compliance Dashboard"
type: "article"
description: "Review STIG scan results, download XCCDF reports, and view FIPS certificate information for your organization's container images in the Chainguard Console."
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-08T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Chainguard Console", "FIPS"]
images: []
weight: 45
toc: true
---

The Compliance Dashboard in the [Chainguard Console](/platform/console/images-directory/) shows two kinds of compliance evidence for your organization's container images:

* **Security Technical Implementation Guide (STIG) results.** Chainguard scans its container images against a hardening profile based on the Defense Information Systems Agency (DISA) General Purpose Operating System (GPOS) Security Requirements Guide (SRG). The dashboard shows the result of every rule and lets you download the full report.
* **Federal Information Processing Standards (FIPS) certificates.** The dashboard lists the validated cryptographic modules in each container image and links to their National Institute of Standards and Technology (NIST) certificates.

The dashboard has results only for Chainguard's [FIPS container images](/chainguard/containers/concepts/container-categories/#fips-containers), which are images whose names include `-fips`, such as `go-fips` or `python-fips`. Other container images in your organization still have a **Compliance** tab, but it shows a message that no compliance report is available.

You can use the Compliance Dashboard to review a container image's compliance posture or to collect evidence for an auditor without scanning it yourself. To learn what STIGs are and how Chainguard applies the GPOS SRG to containers, refer to [STIGs for Chainguard Containers](/chainguard/containers/security-and-compliance/stigs/).

## Prerequisites

To use the Compliance Dashboard, you need the following:

* A Chainguard account with access to an organization that includes at least one FIPS container image. The dashboard covers only images in your organization's catalog. It isn't available in the **Chainguard catalog** tab or in the public [Chainguard Directory](/chainguard/containers/registry/chainguard-directory/).
* A role in that organization that can download image content, such as `owner`, `editor`, or `viewer`. The `console_viewer` and `registry.pull` roles can't open the dashboard. For details on each role, refer to [Roles and role bindings](/platform/administration/iam-organizations/roles-role-bindings/roles-role-bindings/).

## Open the Compliance tab

You can reach the Compliance Dashboard from a container image's details page or from the details panel for a single tag.

To open the full dashboard for a container image, follow these steps:

1. Sign in to the [Chainguard Console](https://console.chainguard.dev/).
2. In the left-hand navigation, click **Images**. The **Images** page opens to the **Organization** tab.
3. Click the name of a container image.
4. On the image's details page, click the **Compliance** tab.

If the **Compliance** tab is unavailable, the Console has no metadata for the image's current version yet.

To view compliance results for one tag, follow these steps:

1. On the image's details page, click the **Tags** tab.
2. Click a tag. A panel with the tag's details opens.
3. In the panel, click the **Compliance** tab.

The tag panel shows a condensed version of the dashboard. To open the full dashboard from the panel, click **View OSCAP report**.

## Choose a tag and architecture

The full dashboard opens on the image's most recent version. At the top of the dashboard, you can change what it shows:

* **Tag:** Select the tag to review. Results apply to the image index that the tag points to.
* **Architecture:** Select the CPU architecture, `x86_64` or `arm64`. This choice scopes both the STIG results and the FIPS certificates.

Next to these menus, the dashboard shows the **Index digest** of the selected tag, with a button that copies the digest, and the date the tag last changed.

In the tag panel, the dashboard uses the architecture selected for that tag.

## Review STIG results

The STIG section is titled **STIG validated: DISA General Purpose Operating System SRG**. It shows reference results for the baseline container image in the Chainguard Catalog.

Your results can differ depending on your environment and on any customizations made to the image, such as packages added with [Custom Assembly](/chainguard/containers/custom-assembly/overview/). If a tag has no STIG report, as with any non-FIPS container image, the dashboard shows the message **No compliance report available for**, followed by the image name and tag, in place of both the STIG and FIPS sections.

### Summary

The summary row contains the following fields:

* **Checklist:** The datastream checklist and version used for the scan.
* **Rule results:** A bar that shows the share of evaluated rules that passed or failed. Rules that resulted in **Not applicable** aren't part of the bar.
* A count of rules for each result, such as **Pass**, **Fail**, and **Not applicable**.
* **Scanned:** The date and time the scan finished.

For more information on how the scan ran, hold the pointer over **Scan details**. The panel that appears lists these values:

| Field | Description |
| ----- | ----------- |
| **Profile ID** | The XCCDF profile used for the scan. |
| **Datastream version** | The version of the STIG datastream. |
| **Scanner image** | The container image that ran the scan. |
| **Architecture** | The architecture that was scanned. |
| **Started at** and **Finished at** | When the scan started and finished. |
| **Scanned digest** | The digest of the image that was scanned. |
| **XCCDF SHA-256** | The SHA-256 checksum of the XCCDF report. Use this to confirm that a downloaded report matches the one the dashboard displays. |

The **Scanned digest** can differ from the **Index digest** at the top of the page. For current reports, the scanned digest is the image within the index that matches the selected architecture. For a container image built with Custom Assembly that has no report of its own, the dashboard can show the report for the image it's based on. In that case, the scanned digest identifies the base image.

### Rule results

After the summary, a table lists each rule in the checklist, organized into groups. Each row shows the rule's **Title**, **Severity**, and **Result**.

To find specific rules, use these controls:

* Enter text in the **Filter XCCDF rules** box to search the rules.
* Use the **Result** menu to show only rules with one result, such as **Pass** or **Fail**.
* Click **Expand all groups** or **Collapse all groups** to show or hide every rule at once.

To open a rule's details, click the rule. The details include the **Rule ID**, **Result**, **Time**, **Severity**, and **Description**.

A rule can have any of the following results:

| Result | Meaning |
| ------ | ------- |
| **Pass** | The image meets the rule. |
| **Fail** | The image doesn't meet the rule. |
| **Error** | The scanner couldn't evaluate the rule. |
| **Not applicable** | The rule doesn't apply to the image. |
| **Not checked** | The scanner didn't evaluate the rule because the rule has no check defined or its checks are turned off. |
| **Not selected** | The rule isn't part of the selected profile. |
| **Fixed** | The rule failed and was remediated. |
| **Informational** | The rule reports information and has no pass or fail outcome. |
| **Unknown** | The scanner couldn't determine the result. |

Many GPOS SRG requirements cover the container host rather than the container image, so expect some failures when you scan a container. For an explanation of common cases, refer to [False positives and the General Purpose OS STIG](/chainguard/containers/security-and-compliance/stigs/#false-positives-and-the-general-purpose-os-stig).

### Historical reports

Chainguard previously attached each STIG report to the image index instead of to a specific architecture. When the dashboard shows one of these older reports, it displays an **Architecture unknown** notice. These reports don't record the scanned architecture, so the results don't confirm coverage for the architecture you selected.

## Download the XCCDF report

The dashboard lets you download the complete scan results as an XCCDF XML file. This file is the canonical report, and you can open it in any SCAP-compatible tool or share it with an auditor.

To download the report, select a tag and architecture, then click **Download XCCDF**. For a historical report, the button reads **Download historical index XCCDF** and downloads the report attached to the image index. The file name includes the architecture, so you can tell reports for different architectures apart.

To confirm that the file is intact, compare its SHA-256 checksum with the **XCCDF SHA-256** value in **Scan details**:

```sh
sha256sum DOWNLOADED_FILE.xml
```

To reproduce the scan yourself with OpenSCAP, refer to [Getting started](/chainguard/containers/security-and-compliance/stigs/#getting-started) in the STIGs guide.

## View FIPS certificate information

The FIPS section is titled **FIPS validated**, followed by the FIPS standard the modules are validated against, such as FIPS 140-3. It lists the validated cryptographic modules in the container image for the selected architecture.

The FIPS table has the following columns:

| Column | Description |
| ------ | ----------- |
| **Certification** | The type of certificate: **NIST CMVP Certificate** for a validated cryptographic module, or **NIST Entropy Certificate** for a validated entropy source. |
| **Description** | A description of the validated module. |
| **Depends on** | The component in the image that the certificate covers. |
| **Certificate** | The certificate number. Click it to open the certificate record on the NIST website. |

If the image has no FIPS certificates for the selected architecture, the section shows **No FIPS certificates for this architecture**. In the tag panel, the FIPS section appears only when the image has certificates.

For more about Chainguard's FIPS container images, refer to [FIPS-ready container images](/platform/fips/fips-images/).

## Learn more

* [STIGs for Chainguard Containers](/chainguard/containers/security-and-compliance/stigs/) explains the GPOS SRG profile and how to run the scan locally with OpenSCAP.
* [FedRAMP technical considerations and risk factors](/chainguard/containers/security-and-compliance/fedramp-considerations/) covers how Chainguard Containers fit into a FedRAMP authorization.
* [Using the Chainguard Console](/platform/console/images-directory/) walks through the rest of the image details page.
