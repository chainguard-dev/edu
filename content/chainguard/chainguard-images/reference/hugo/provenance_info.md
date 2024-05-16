---
title: "Provenance Information for hugo Images"
type: "article"
unlisted: true
description: "Provenance information for hugo Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-05-16 00:37:58
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 600
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/hugo/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/hugo/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/hugo/tags_history/" >}}
{{< tab title="Provenance" active=true url="/chainguard/chainguard-images/reference/hugo/provenance_info/" >}}
{{</ tabs >}}

All Chainguard Images contain verifiable signatures and high-quality SBOMs (software bill of materials), features that enable users to confirm the origin of each image build and have a detailed list of everything that is packed within.

You'll need [cosign](https://docs.sigstore.dev/cosign/overview/) and [jq](https://stedolan.github.io/jq/) in order to download and verify image attestations.

### Registry and Tags for hugo Image
Attestations are provided per image build, so you'll need to specify the correct tag and registry when pulling attestations from an image with `cosign`.

| Registry                     | Tags                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `cgr.dev/chainguard`         | latest, latest-dev                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `cgr.dev/chainguard-private` | 0, 0-dev, 0.111, 0.111-dev, 0.111.3, 0.111.3-dev, 0.112, 0.112-dev, 0.112.1, 0.112.1-dev, 0.112.2, 0.112.2-dev, 0.112.3, 0.112.3-dev, 0.112.5, 0.112.5-dev, 0.112.6, 0.112.6-dev, 0.112.7, 0.112.7-dev, 0.113, 0.113-dev, 0.113.0, 0.113.0-dev, 0.114, 0.114-dev, 0.114.0, 0.114.0-dev, 0.114.1, 0.114.1-dev, 0.115, 0.115-dev, 0.115.0, 0.115.0-dev, 0.115.1, 0.115.1-dev, 0.115.2, 0.115.2-dev, 0.115.3, 0.115.3-dev, 0.115.4, 0.115.4-dev, 0.116, 0.116-dev, 0.116.0, 0.116.0-dev, 0.116.1, 0.116.1-dev, 0.117, 0.117-dev, 0.117.0, 0.117.0-dev, 0.118, 0.118-dev, 0.118.2, 0.118.2-dev, 0.123, 0.123-dev, 0.123.6, 0.123.6-dev, 0.123.7, 0.123.7-dev, 0.123.8, 0.123.8-dev, 0.124, 0.124-dev, 0.124.0, 0.124.0-dev, 0.124.1, 0.124.1-dev, 0.125, 0.125-dev, 0.125.0, 0.125.0-dev, 0.125.1, 0.125.1-dev, 0.125.3, 0.125.3-dev, 0.125.4, 0.125.4-dev, 0.125.5, 0.125.5-dev, 0.125.6, 0.125.6-dev, 0.125.7, 0.125.7-dev, 0.126, 0.126-dev, 0.126.0, 0.126.0-dev, 0.126.1, 0.126.1-dev, latest, latest-dev |


- `cgr.dev/chainguard` - the Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.
- `cgr.dev/chainguard-private` - the Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

The commands listed on this page will default to the `latest` tag, but you can specify a different tag to fetch attestations for.

## Verifying hugo Image Signatures
The **hugo** Chainguard Images are signed using Sigstore, and you can check the included signatures using `cosign`.

The `cosign verify` command will pull detailed information about all signatures found for the provided image.

### Public Registry

```shell
cosign verify \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  cgr.dev/chainguard/hugo | jq
```

### Private/Dedicated Registry

```shell
cosign verify \
--certificate-oidc-issuer=https://token.actions.githubusercontent.com \
--certificate-identity=https://github.com/chainguard-images/images-private/.github/workflows/release.yaml@refs/heads/main \
cgr.dev/chainguard-private/hugo | jq
```

## Downloading hugo Image Attestations

The following [attestations](https://slsa.dev/attestation-model) for the hugo image can be obtained and verified via cosign:

| Attestation Type | Description |
|----------------|-------------|
| `https://slsa.dev/provenance/v1` | The [SLSA 1.0](https://slsa.dev/spec/v1.0/provenance) provenance attestation contains information about the image build environment. |
| `https://apko.dev/image-configuration` | Contains the configuration used by that particular image build, including direct dependencies, user accounts, and entry point. |
| `https://spdx.dev/Document` | Contains the image SBOM (Software Bill of Materials) in SPDX format. |


To download an attestation, use the `cosign download attestation` command and provide both the predicate type and the build platform. For example, the following command will obtain the SBOM for the hugo image on `linux/amd64`:

### Public Registry

```shell
cosign download attestation \
  --platform=linux/amd64 \
  --predicate-type=https://spdx.dev/Document \
  cgr.dev/chainguard/hugo | jq -r .payload | base64 -d | jq .predicate
```

### Private/Dedicated Registry

```shell
cosign download attestation \
--platform=linux/amd64 \
--predicate-type=https://spdx.dev/Document \
cgr.dev/chainguard-private/hugo | jq -r .payload | base64 -d | jq .predicate
```

By default, this command will fetch the SBOM assigned to the `latest` tag. You can also specify the tag you want to fetch the attestation from.

To download a different attestation, replace the `--predicate-type` parameter value with the desired attestation URL identifier.

## Verifying hugo Image Attestations
You can use the `cosign verify-attestation` command to check the signatures of the hugo image attestations:

### Public Registry

```shell
cosign verify-attestation \
  --type https://spdx.dev/Document \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  cgr.dev/chainguard/hugo
```

### Private/Dedicated Registry

```shell
cosign verify-attestation \
--type https://spdx.dev/Document \
--certificate-oidc-issuer=https://token.actions.githubusercontent.com \
--certificate-identity=https://github.com/chainguard-images/images-private/.github/workflows/release.yaml@refs/heads/main \
cgr.dev/chainguard-private/hugo
```

This will pull in the signature for the attestation specified by the `--type` parameter, which in this case is the SPDX attestation. You will receive output that verifies the SBOM attestation signature in cosign's transparency log:

```
Verification for cgr.dev/chainguard/hugo --
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
