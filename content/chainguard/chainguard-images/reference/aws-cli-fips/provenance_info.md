---
title: "Provenance Information for aws-cli-fips Images"
type: "article"
unlisted: true
description: "Provenance information for aws-cli-fips Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-03-16 00:33:13
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 600
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/aws-cli-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/aws-cli-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/aws-cli-fips/tags_history/" >}}
{{< tab title="Provenance" active=true url="/chainguard/chainguard-images/reference/aws-cli-fips/provenance_info/" >}}
{{</ tabs >}}

All Chainguard Images contain verifiable signatures and high-quality SBOMs (software bill of materials), features that enable users to confirm the origin of each image build and have a detailed list of everything that is packed within.

You'll need [cosign](https://docs.sigstore.dev/cosign/overview/) and [jq](https://stedolan.github.io/jq/) in order to download and verify image attestations.

### Registry and Tags for aws-cli-fips Image
Attestations are provided per image build, so you'll need to specify the correct tag and registry when pulling attestations from an image with `cosign`.

| Registry                     | Tags                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `cgr.dev/chainguard`         | No public tags are available for this image.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `cgr.dev/chainguard-private` | 1, 1-dev, 1.32, 1.32-dev, 1.32.11, 1.32.11-dev, 1.32.12, 1.32.12-dev, 1.32.13, 1.32.13-dev, 1.32.14, 1.32.14-dev, 1.32.15, 1.32.15-dev, 1.32.16, 1.32.16-dev, 1.32.17, 1.32.17-dev, 1.32.18, 1.32.18-dev, 1.32.19, 1.32.19-dev, 1.32.20, 1.32.20-dev, 1.32.21, 1.32.21-dev, 1.32.22, 1.32.22-dev, 1.32.23, 1.32.23-dev, 1.32.24, 1.32.24-dev, 1.32.25, 1.32.25-dev, 1.32.26, 1.32.26-dev, 1.32.27, 1.32.27-dev, 1.32.28, 1.32.28-dev, 1.32.29, 1.32.29-dev, 1.32.30, 1.32.30-dev, 1.32.31, 1.32.31-dev, 1.32.32, 1.32.32-dev, 1.32.33, 1.32.33-dev, 1.32.34, 1.32.34-dev, 1.32.35, 1.32.35-dev, 1.32.36, 1.32.36-dev, 1.32.37, 1.32.37-dev, 1.32.38, 1.32.38-dev, 1.32.39, 1.32.39-dev, 1.32.40, 1.32.40-dev, 1.32.41, 1.32.41-dev, 1.32.42, 1.32.42-dev, 1.32.43, 1.32.43-dev, 1.32.44, 1.32.44-dev, 1.32.45, 1.32.45-dev, 1.32.46, 1.32.46-dev, 1.32.47, 1.32.47-dev, 1.32.48, 1.32.48-dev, 1.32.49, 1.32.49-dev, 1.32.50, 1.32.50-dev, 1.32.51, 1.32.51-dev, 1.32.52, 1.32.52-dev, 1.32.53, 1.32.53-dev, 1.32.54, 1.32.54-dev, 1.32.55, 1.32.55-dev, 1.32.56, 1.32.56-dev, 1.32.57, 1.32.57-dev, 1.32.58, 1.32.58-dev, 1.32.59, 1.32.59-dev, 1.32.60, 1.32.60-dev, 1.32.61, 1.32.61-dev, 1.32.62, 1.32.62-dev, 1.32.63, 1.32.63-dev, 1.32.64, 1.32.64-dev, latest, latest-dev |


- `cgr.dev/chainguard` - the Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.
- `cgr.dev/chainguard-private` - the Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

The commands listed on this page will default to the `latest` tag, but you can specify a different tag to fetch attestations for.

## Verifying aws-cli-fips Image Signatures
The **aws-cli-fips** Chainguard Images are signed using Sigstore, and you can check the included signatures using `cosign`.

The `cosign verify` command will pull detailed information about all signatures found for the provided image.

### Public Registry

```shell
cosign verify \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  cgr.dev/chainguard/aws-cli-fips | jq
```

### Private/Dedicated Registry

```shell
cosign verify \
--certificate-oidc-issuer=https://token.actions.githubusercontent.com \
--certificate-identity=https://github.com/chainguard-images/images-private/.github/workflows/release.yaml@refs/heads/main \
cgr.dev/chainguard-private/aws-cli-fips | jq
```

## Downloading aws-cli-fips Image Attestations

The following [attestations](https://slsa.dev/attestation-model) for the aws-cli-fips image can be obtained and verified via cosign:

| Attestation Type | Description |
|----------------|-------------|
| `https://slsa.dev/provenance/v1` | The [SLSA 1.0](https://slsa.dev/spec/v1.0/provenance) provenance attestation contains information about the image build environment. |
| `https://apko.dev/image-configuration` | Contains the configuration used by that particular image build, including direct dependencies, user accounts, and entry point. |
| `https://spdx.dev/Document` | Contains the image SBOM (Software Bill of Materials) in SPDX format. |


To download an attestation, use the `cosign download attestation` command and provide both the predicate type and the build platform. For example, the following command will obtain the SBOM for the aws-cli-fips image on `linux/amd64`:

### Public Registry

```shell
cosign download attestation \
  --platform=linux/amd64 \
  --predicate-type=https://spdx.dev/Document \
  cgr.dev/chainguard/aws-cli-fips | jq -r .payload | base64 -d | jq .predicate
```

### Private/Dedicated Registry

```shell
cosign download attestation \
--platform=linux/amd64 \
--predicate-type=https://spdx.dev/Document \
cgr.dev/chainguard-private/aws-cli-fips | jq -r .payload | base64 -d | jq .predicate
```

By default, this command will fetch the SBOM assigned to the `latest` tag. You can also specify the tag you want to fetch the attestation from.

To download a different attestation, replace the `--predicate-type` parameter value with the desired attestation URL identifier.

## Verifying aws-cli-fips Image Attestations
You can use the `cosign verify-attestation` command to check the signatures of the aws-cli-fips image attestations:

### Public Registry

```shell
cosign verify-attestation \
  --type https://spdx.dev/Document \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  cgr.dev/chainguard/aws-cli-fips
```

### Private/Dedicated Registry

```shell
cosign verify-attestation \
--type https://spdx.dev/Document \
--certificate-oidc-issuer=https://token.actions.githubusercontent.com \
--certificate-identity=https://github.com/chainguard-images/images-private/.github/workflows/release.yaml@refs/heads/main \
cgr.dev/chainguard-private/aws-cli-fips
```

This will pull in the signature for the attestation specified by the `--type` parameter, which in this case is the SPDX attestation. You will receive output that verifies the SBOM attestation signature in cosign's transparency log:

```
Verification for cgr.dev/chainguard/aws-cli-fips --
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
