---
title: "Getting Started with OpenVEX and vexctl"
linktitle: "OpenVEX and vexctl"
description: "Using vexctl to manage vulnerability communications"
lead: "A guide to SBOM quality"
type: "article"
date: 2023-01-30T15:21:01+02:00
lastmod: 2026-07-27T15:48:10+00:00
draft: false
tags: ["SBOM", "VEX", "Procedural"]
images: []
menu:
  docs:
    parent: "sbom"
weight: 10
toc: true
---

The `vexctl` CLI is a tool to make VEX work. As part of the open source [OpenVex](/open-source/sbom/what-is-openvex/) project, `vexctl` enables you to create, apply, and attest VEX (Vulnerability Exploitability eXchange) data in order to filter out false positive security alerts.

The `vexctl` tool was built to help with the creation and management of VEX documents, communicate transparently to users as time progresses, and enable the "turning off" of security scanner alerts of vulnerabilities known not to affect a given product. Using VEX, software authors can communicate to their users that an otherwise vulnerable component has no security implications for their product.

This tutorial will walk you through some common commands in `vexctl`.

## Installing vexctl

If you would like to install `vexctl` on your local or virtual machine, you will need a current, supported release of Go. You can install it by following the official [Go documentation](https://go.dev/doc/install).

Using Go, run the following to install `vexctl`:

```sh
go install github.com/openvex/vexctl@latest
```

This command will install the latest version of `vexctl` on your machine.

## Confirming installation

You can confirm that `vexctl` was installed and is ready to use by running the following command:

```sh
vexctl version
```

You should receive output similar to the following.

```output
 _   _  _____ __   __ _____  _____  _
| | | ||  ___|\ \ / //  __ \|_   _|| |
| | | || |__   \ V / | /  \/  | |  | |
| | | ||  __|  /   \ | |      | |  | |
\ \_/ /| |___ / /^\ \| \__/\  | |  | |____
 \___/ \____/ \/   \/ \____/  \_/  \_____/
vexctl: A tool for working with VEX data

GitVersion:   ...
...
Platform:     ...
```

This indicates the current version of `vexctl` on your working machine. You are ready to proceed with working with `vexctl`.

## Creating VEX documents

With `vexctl`, VEX data can be created to a file on disk, or it can be captured in a signed attestation that can be attached to a container image. You can create a VEX document by using the `vexctl create` command.

For example, to create a VEX document with a single statement asserting that the [WolfiOS](https://github.com/wolfi-dev/) package `git-2.38.1-r0` is not affected by a given common vulnerability and exposure (CVE) — let's say,  `CVE-2014-123456` — because it has already been mitigated in the distribution, you can run the following.

```sh
vexctl create --product="pkg:apk/wolfi/git@2.38.1-r0?arch=x86_64" \
               --vuln="CVE-2014-123456" \
               --status="not_affected" \
               --justification="inline_mitigations_already_exist"
```

This command notes the following:

* The software product — `product` — in this case a Wolfi package
* The vulnerability — `vuln` — in this case a specific CVE
* The current status — `status` — which can be `not_affected`, `affected`, `fixed`, or `under_investigation`
* When the `status` is noted as `not_affected`, the reason for the status — `justification` — must be included, and can read `inline_mitigations_already_exist` or `component_not_present`

The `vexctl create` command above renders a document similar to the following. The `@id` and timestamps will differ on each run.

```json
{
  "@context": "https://openvex.dev/ns/v0.2.0",
  "@id": "https://openvex.dev/docs/public/vex-b6081638d51cd5cdf2e810d120353dd48d3c829c169123df3037979ec824df94",
  "author": "Unknown Author",
  "version": 1,
  "statements": [
    {
      "vulnerability": {
        "name": "CVE-2014-123456"
      },
      "products": [
        {
          "@id": "pkg:apk/wolfi/git@2.38.1-r0?arch=x86_64"
        }
      ],
      "status": "not_affected",
      "justification": "inline_mitigations_already_exist",
      "timestamp": "2026-07-27T15:46:08.152188473Z"
    }
  ],
  "timestamp": "2026-07-27T15:46:08Z"
}
```

You can also create a VEX document with abbreviated information. For instance, when a given CVE was addressed in the image and you want to attest that it has been fixed.

```sh
vexctl create "pkg:apk/wolfi/git@2.39.0-r1?arch=x86_64" CVE-2023-12345 fixed
```

The above workflow demonstrates how to create a VEX document with `vexctl` on the command line.

## Merging existing VEX documents

When more than one stakeholder is issuing VEX metadata about a piece of software, `vexctl` can merge the documents to get the most up-to-date impact assessment of a vulnerability.

Let's begin with two test documents. You can create these two test documents with a CLI editor such as nano.

The first document is `document1.vex.json`:

```json
{
  "@context": "https://openvex.dev/ns/v0.2.0",
  "@id": "https://openvex.dev/docs/public/vex-0f3be8817faafa24e4bfb3d17eaf619efb1fe54923b9c42c57b156a936b91431",
  "author": "John Doe",
  "role": "Senior Trusted VEX Issuer",
  "version": 1,
  "statements": [
    {
      "vulnerability": {
        "name": "CVE-1234-5678"
      },
      "products": [
        {
          "@id": "pkg:apk/wolfi/bash@1.0.0"
        }
      ],
      "status": "under_investigation",
      "timestamp": "2023-12-05T05:04:34.77929922Z"
    }
  ],
  "timestamp": "2023-12-05T05:04:34.77929844Z"
}
```

The second document is `document2.vex.json`:

```json
{
  "@context": "https://openvex.dev/ns/v0.2.0",
  "@id": "https://openvex.dev/docs/public/vex-3cd938c9a706eba0915883640116cfe813f7d59150cf758b8c869b4926a7cf11",
  "author": "John Doe",
  "role": "Senior Trusted VEX Issuer",
  "version": 1,
  "statements": [
    {
      "vulnerability": {
        "name": "CVE-1234-5678"
      },
      "products": [
        {
          "@id": "pkg:apk/wolfi/bash@1.0.0"
        }
      ],
      "status": "fixed",
      "timestamp": "2023-12-05T05:06:38.099731287Z"
    }
  ],
  "timestamp": "2023-12-05T05:06:38.099730576Z"
}
```

The two files are generated from a known rule set, also known as "golden data" or a "golden file," which is reused and reapplied to new releases of the same project.

We can merge the two VEX documents with the `vexctl merge` command:

```sh
vexctl merge --product=pkg:apk/wolfi/bash@1.0.0 \
             document1.vex.json \
             document2.vex.json
```

The resulting document combines the VEX statements that express data about `bash@1.0.0` into a single document.

```json
{
  "@context": "https://openvex.dev/ns/v0.2.0",
  "@id": "merged-vex-6b33f63783819578804350ba1cde277ddd8f90aa2bbcb706d19a61d211a8443f",
  "author": "Unknown Author",
  "version": 1,
  "statements": [
    {
      "vulnerability": {
        "name": "CVE-1234-5678"
      },
      "products": [
        {
          "@id": "pkg:apk/wolfi/bash@1.0.0"
        }
      ],
      "status": "under_investigation",
      "timestamp": "2023-12-05T05:04:34.77929922Z"
    },
    {
      "vulnerability": {
        "name": "CVE-1234-5678"
      },
      "products": [
        {
          "@id": "pkg:apk/wolfi/bash@1.0.0"
        }
      ],
      "status": "fixed",
      "timestamp": "2023-12-05T05:06:38.099731287Z"
    }
  ],
  "timestamp": "2026-07-27T15:46:08Z"
}
```

This final document tells the whole story of how `CVE-1234-5678` was `under_investigation` and then `fixed` about two minutes later, all documented in a single VEX file that was merged with `vexctl`. The merged document preserves each statement's original timestamp, so the order of events is retained.

## Attesting and attaching VEX documents

To attest to and attach VEX statements within a given document to a container image, you can use the `vexctl attest` command with the `--attach` and `--sign` flags.

For example, if you have a container image `your-username/your-container-image:latest` in a container registry, and a related VEX document `hello.vex.json`, you can run the following command to attest to that document, attach the document and sign that attestation. If you want to try this example, make sure to replace `your-username/your-container-image:latest` with the path to your container.

```sh
vexctl attest --attach --sign hello.vex.json your-username/your-container-image:latest
```

Upon running this command, you'll be taken through a signing workflow with [Sigstore](https://www.sigstore.dev/). Your terminal output will indicate your progress.

```output
Generating ephemeral keys...
Retrieving signed certificate...
```

A browser window will open for you to select an OIDC provider. When the attestation is complete, you'll receive feedback that it was successful.

```output
Successfully verified SCT...
{"payloadType":"application/vnd.in-toto+json","payload":"e...o=","signatures":[{"keyid":"","sig":"MEY...z"}]}
```

This attestation with `.att` extension will now live in the container registry as an attachment to your container.

## Chronology and VEX documents

Assessing the impact of CVEs on a software product is a process that takes time and the status will change over time. VEX is designed to communicate with users as the status changes, and there may therefore be multiple VEX documents associated with a product.

To understand how this may work in practice, below is an example timeline for the VEX documents associated with a given product and CVE.

1. The software product _Linky App_ becomes aware of `CVE-2014-123456`, associated with one of its components.
2. _Linky App_ developers issue a VEX data file with a status of `under_investigation` to inform their users that they are aware of the CVE, but are reviewing whether it has an impact on _Linky App_.
3. After investigation, the developers determine the CVE has no impact on _Linky App_ because the vulnerable function in the component is never executed.
4. The developers issue a second VEX document with a status of `not_affected` using the `vulnerable_code_not_in_execute_path` justification.

When analyzing the VEX documents associated with _Linky App_, `vexctl` will review them chronologically and "replay" the known impact statuses in the order they were found, effectively computing the `not_affected` status.

If a SARIF report is formatted as a VEX document with `vexctl`, any entries alerting of `CVE-2014-123456` will be filtered out.

## Learn more

The `vexctl` tool is open source, you can review the [`vexctl` repository on GitHub](https://github.com/openvex/vexctl), as well as the [`go-vex` Go library](https://github.com/openvex/go-vex) for generating, consuming, and operating on VEX documents.

The following blog posts have some background about VEX and OpenVEX:

* [What is OpenVex](/open-source/sbom/what-is-openvex/)
* [Putting VEX To Work](https://www.chainguard.dev/unchained/putting-vex-to-work)
* [Reflections on Trusting VEX (or when humans can improve SBOMs)](https://www.chainguard.dev/unchained/reflections-on-trusting-vex-or-when-humans-can-improve-sboms)
* [Understanding The Promise of VEX](https://www.chainguard.dev/unchained/understanding-the-promise-of-vex)

The [OpenVEX Specification](https://github.com/openvex/spec/blob/main/OPENVEX-SPEC.md) is owned and steered by the community. You can find the organization page with additional repositories at [openvex.dev](https://openvex.dev).
