---
title: "Provenance Information for rqlite Images"
type: "article"
unlisted: true
description: "Provenance information for rqlite Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-03-01 12:14:22
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 600
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/rqlite/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/rqlite/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/rqlite/tags_history/" >}}
{{< tab title="Provenance" active=true url="/chainguard/chainguard-images/reference/rqlite/provenance_info/" >}}
{{</ tabs >}}

All Chainguard Images contain verifiable signatures and high-quality SBOMs (software bill of materials), features that enable users to confirm the origin of each image build and have a detailed list of everything that is packed within.

You'll need [cosign](https://docs.sigstore.dev/cosign/overview/) and [jq](https://stedolan.github.io/jq/) in order to download and verify image attestations.

### Registry and Tags for rqlite Image
Attestations are provided per image build, so you'll need to specify the correct tag and registry when pulling attestations from an image with `cosign`.

| Registry                     | Tags                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `cgr.dev/chainguard`         | 7, 7-dev, 7.21, 7.21-dev, 7.21.4, 7.21.4-dev, latest, latest-dev                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `cgr.dev/chainguard-private` | 7, 7-dev, 7.21, 7.21-dev, 7.21.0, 7.21.0-dev, 7.21.1, 7.21.1-dev, 7.21.2, 7.21.2-dev, 7.21.3, 7.21.3-dev, 7.21.4, 7.21.4-dev, 8, 8-dev, 8.0, 8.0-dev, 8.0.0, 8.0.0-dev, 8.0.1, 8.0.1-dev, 8.0.2, 8.0.2-dev, 8.0.3, 8.0.3-dev, 8.11, 8.11-dev, 8.11.0, 8.11.0-dev, 8.11.1, 8.11.1-dev, 8.12, 8.12-dev, 8.12.0, 8.12.0-dev, 8.12.1, 8.12.1-dev, 8.12.3, 8.12.3-dev, 8.13, 8.13-dev, 8.13.0, 8.13.0-dev, 8.13.2, 8.13.2-dev, 8.13.4, 8.13.4-dev, 8.13.5, 8.13.5-dev, 8.14, 8.14-dev, 8.14.0, 8.14.0-dev, 8.14.1, 8.14.1-dev, 8.15, 8.15-dev, 8.15.0, 8.15.0-dev, 8.16, 8.16-dev, 8.16.0, 8.16.0-dev, 8.16.1, 8.16.1-dev, 8.16.2, 8.16.2-dev, 8.16.3, 8.16.3-dev, 8.16.4, 8.16.4-dev, 8.16.5, 8.16.5-dev, 8.16.6, 8.16.6-dev, 8.16.7, 8.16.7-dev, 8.16.8, 8.16.8-dev, 8.17, 8.17-dev, 8.17.0, 8.17.0-dev, 8.18, 8.18-dev, 8.18.0, 8.18.0-dev, 8.18.1, 8.18.1-dev, 8.18.2, 8.18.2-dev, 8.18.3, 8.18.3-dev, 8.18.4, 8.18.4-dev, 8.18.5, 8.18.5-dev, 8.18.6, 8.18.6-dev, 8.18.7, 8.18.7-dev, 8.19, 8.19-dev, 8.19.0, 8.19.0-dev, 8.20, 8.20-dev, 8.20.0, 8.20.0-dev, 8.20.1, 8.20.1-dev, 8.20.3, 8.20.3-dev, 8.21, 8.21-dev, 8.21.0, 8.21.0-dev, 8.21.1, 8.21.1-dev, 8.21.2, 8.21.2-dev, 8.21.3, 8.21.3-dev, 8.22, 8.22-dev, 8.22.0, 8.22.0-dev, 8.22.1, 8.22.1-dev, latest, latest-dev |


- `cgr.dev/chainguard` - the Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.
- `cgr.dev/chainguard-private` - the Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

The commands listed on this page will default to the `latest` tag, but you can specify a different tag to fetch attestations for.

## Verifying rqlite Image Signatures
The **rqlite** Chainguard Images are signed using Sigstore, and you can check the included signatures using `cosign`.

The `cosign verify` command will pull detailed information about all signatures found for the provided image.

### Public Registry

```shell
cosign verify \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  cgr.dev/chainguard/rqlite | jq
```

### Private/Dedicated Registry

```shell
cosign verify \
--certificate-oidc-issuer=https://token.actions.githubusercontent.com \
--certificate-identity=https://github.com/chainguard-images/images-private/.github/workflows/release.yaml@refs/heads/main \
cgr.dev/chainguard-private/rqlite | jq
```

## Downloading rqlite Image Attestations

The following [attestations](https://slsa.dev/attestation-model) for the rqlite image can be obtained and verified via cosign:

| Attestation Type | Description |
|----------------|-------------|
| `https://slsa.dev/provenance/v1` | The [SLSA 1.0](https://slsa.dev/spec/v1.0/provenance) provenance attestation contains information about the image build environment. |
| `https://apko.dev/image-configuration` | Contains the configuration used by that particular image build, including direct dependencies, user accounts, and entry point. |
| `https://spdx.dev/Document` | Contains the image SBOM (Software Bill of Materials) in SPDX format. |


To download an attestation, use the `cosign download attestation` command and provide both the predicate type and the build platform. For example, the following command will obtain the SBOM for the rqlite image on `linux/amd64`:

### Public Registry

```shell
cosign download attestation \
  --platform=linux/amd64 \
  --predicate-type=https://spdx.dev/Document \
  cgr.dev/chainguard/rqlite | jq -r .payload | base64 -d | jq .predicate
```

### Private/Dedicated Registry

```shell
cosign download attestation \
--platform=linux/amd64 \
--predicate-type=https://spdx.dev/Document \
cgr.dev/chainguard-private/rqlite | jq -r .payload | base64 -d | jq .predicate
```

By default, this command will fetch the SBOM assigned to the `latest` tag. You can also specify the tag you want to fetch the attestation from.

To download a different attestation, replace the `--predicate-type` parameter value with the desired attestation URL identifier.

## Verifying rqlite Image Attestations
You can use the `cosign verify-attestation` command to check the signatures of the rqlite image attestations:

### Public Registry

```shell
cosign verify-attestation \
  --type https://spdx.dev/Document \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  cgr.dev/chainguard/rqlite
```

### Private/Dedicated Registry

```shell
cosign verify-attestation \
--type https://spdx.dev/Document \
--certificate-oidc-issuer=https://token.actions.githubusercontent.com \
--certificate-identity=https://github.com/chainguard-images/images-private/.github/workflows/release.yaml@refs/heads/main \
cgr.dev/chainguard-private/rqlite
```

This will pull in the signature for the attestation specified by the `--type` parameter, which in this case is the SPDX attestation. You will receive output that verifies the SBOM attestation signature in cosign's transparency log:

```
Verification for cgr.dev/chainguard/rqlite --
The following checks were performed on each of these signatures:
- The cosign claims were validated
- Existence of the claims in the transparency log was verified offline
- The code-signing certificate was verified using trusted certificate authority certificates
Certificate subject:  https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main
Certificate issuer URL:  https://token.actions.githubusercontent.com
GitHub Workflow Trigger: schedule
GitHub Workflow SHA: da283c26829d46c2d2883de5ff98bee672428696
GitHub Workflow Name: .github/workflows/release.yaml
GitHub Workflow Trigger chainguard-images/images
GitHub Workflow Ref: refs/heads/main
...
```
