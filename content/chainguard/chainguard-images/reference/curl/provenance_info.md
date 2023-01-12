---
title: "Provenance Information for curl Images"
type: "article"
description: "Provenance information for curl Chainguard Images"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "curl"
weight: 600
toc: true
---

All Chainguard Images contain verifiable signatures and high-quality SBOMs (software bill of materials), features that enable users to confirm the origin of each image built and have a detailed list of everything that is packed within.

## Verifying Image Signatures
The **curl** Chainguard Images are signed using Sigstore, and you can check the included signatures using `cosign`.

The following command requires [cosign](https://docs.sigstore.dev/cosign/overview/) and [jq](https://stedolan.github.io/jq/) to be installed on your machine. It will pull detailed information about all signatures found for the provided image.

```shell
COSIGN_EXPERIMENTAL=1 cosign verify cgr.dev/chainguard/curl | jq
```

By default, this command will fetch signatures for the `latest` tag. You can also specify the tag you want to fetch signatures for.

## Verifying SBOMs

All Chainguard Images come with a high-quality Software Bill Of Materials (SBOM) generated at build-time. The SBOM can be downloaded using the cosign tool:

```shell
cosign download sbom --platform linux/amd64 cgr.dev/chainguard/curl | jq
```
By default, this command will fetch the SBOM assigned to the `latest` tag. You can also specify the tag you want to fetch the SBOM from.
