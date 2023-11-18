---
title: "How to Retrieve SBOMs for Chainguard Images"
linktitle: "Retrieve an Image's SBOM"
type: "article"
description: "A brief tutorial on how to use Cosign to retrieve Chainguard Image SBOMs."
date: 2023-11-17T11:07:52+02:00
lastmod: 2023-11-17T11:07:52+02:00
draft: false
tags: ["Conceptual", "Chainguard Images", "SBOM"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 710
toc: true
---


Chainguard Images contain only the minimum number of packages needed to use the software they contain. The purpose of this is to reduce the image's attack surface and minimize the risk that CVEs will impact software that depends on these container images. 

Even though they contain the minimum number of packages, there may come a time when you want to know exactly what's running inside of a certain Chainguard Image. For this reason, we include a signed SBOM (also known as an *attestation*) with each image.

[Cosign](/open-source/sigstore/cosign/an-introduction-to-cosign/) — a part of the Sigstore project — supports software artifact signing, verification, and storage in an [OCI (Open Container Initiative)](/open-source/oci/what-is-the-oci/) registry, as well as the retrieval of said artifacts. This tutorial outlines how you can use the `cosign` command to retrieve a Chainguard Image's SBOM using Cosign. 


## Prerequisites

In order to follow this guide, you'll need the following installed on your local machine:

* **Cosign** — to retrieve SBOMs associated with Chainguard Images, check out [our guide on installing Cosign](/open-source/sigstore/cosign/how-to-install-cosign/) to configure it.
* **jq** — to process JSON, visit the [jq downloads](https://jqlang.github.io/jq/download/) page to set it up.


## Using Cosign to retrieve an Image's SBOM

Cosign includes a `download` command that allows you to retrieve a Chainguard Image's SBOM over the command line. To do so, you would use this command with syntax like the following.

```shell
cosign download attestation \ 
cgr.dev/chainguard/$IMAGE | jq -r .payload | base64 -d | jq .predicate
```

Notice that this example syntax includes `download attestation` rather than `download sbom`. While there are a few [differences between SBOMs and attestations](/open-source/sbom/sboms-and-attestations/), you can generally think of an attestation as a more accurate representation of the contents of the container image than an SBOM. This is because attestations must be signed by the software producer, thereby ensuring the accuracy of the SBOM and the quality of the software. 

This attestation data is encoded in base64, making it unreadable without further processing. 
This is why the output from the first part of the command is piped into `jq` in order to filter out the payload section of the output containing the SBOM.

This filtered output is then passed into the `base64` command to be decoded before that output is piped into another `jq` command. This final `jq` command extracts the attestation predicate from the `base64` output and returns it to your terminal.

As an example, to retrieve the `argocd` image's attestation you would run a command like the following.

```shell
cosign download attestation \
  --platform=linux/amd64 \
  --predicate-type=https://spdx.dev/Document \
  cgr.dev/chainguard/argocd | jq -r .payload | base64 -d | jq .predicate
```

This example includes two extra arguments not included in the example syntax outlined previously. First, it includes the `--platform` flag which allows you to download the attestation for a specific platform image. This example specifies the `linux/amd64` platform, but you could enter alternatives such as `linux/arm64` or `darwin/amd64`. Be aware, though, that in order to use the `--platform` option you'll need to have Cosign version 2.2.1 or newer installed.

The other extra argument is the `--predicate-type` flag. This allows you to specify which format you'd like the SBOM you're downloading to follow. This example retrieves the SBOM in the SPDX format, but to download a CycloneDX SBOM you could instead have the `--predicate-type` option point to `https://cyclonedx.org/Document`.


## Learn more

We provide provenance information for every Chainguard Image in their respective [Reference docs](/chainguard/chainguard-images/reference/). After reaching the **Overview** for the image of your choice, navigate to the **Provenance** tab for information on how to retrieve the image's attestation, as well as how to verify the image's attestation and signatures. 