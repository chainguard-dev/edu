---
title: "Provenance Information for semgrep Images"
type: "article"
unlisted: true
description: "Provenance information for semgrep Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-03-01 12:14:22
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 600
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/semgrep/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/semgrep/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/semgrep/tags_history/" >}}
{{< tab title="Provenance" active=true url="/chainguard/chainguard-images/reference/semgrep/provenance_info/" >}}
{{</ tabs >}}

All Chainguard Images contain verifiable signatures and high-quality SBOMs (software bill of materials), features that enable users to confirm the origin of each image build and have a detailed list of everything that is packed within.

You'll need [cosign](https://docs.sigstore.dev/cosign/overview/) and [jq](https://stedolan.github.io/jq/) in order to download and verify image attestations.

### Registry and Tags for semgrep Image
Attestations are provided per image build, so you'll need to specify the correct tag and registry when pulling attestations from an image with `cosign`.

| Registry                     | Tags                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `cgr.dev/chainguard`         | latest, latest-dev                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `cgr.dev/chainguard-private` | 1, 1-dev, 1.40, 1.40-dev, 1.40.0, 1.40.0-dev, 1.42, 1.42-dev, 1.42.0, 1.42.0-dev, 1.43, 1.43-dev, 1.43.0, 1.43.0-dev, 1.44, 1.44-dev, 1.44.0, 1.44.0-dev, 1.45, 1.45-dev, 1.45.0, 1.45.0-dev, 1.46, 1.46-dev, 1.46.0, 1.46.0-dev, 1.47, 1.47-dev, 1.47.0, 1.47.0-dev, 1.48, 1.48-dev, 1.48.0, 1.48.0-dev, 1.49, 1.49-dev, 1.49.0, 1.49.0-dev, 1.50, 1.50-dev, 1.50.0, 1.50.0-dev, 1.52, 1.52-dev, 1.52.0, 1.52.0-dev, 1.53, 1.53-dev, 1.53.0, 1.53.0-dev, 1.54, 1.54-dev, 1.54.0, 1.54.0-dev, 1.54.1, 1.54.1-dev, 1.55, 1.55-dev, 1.55.1, 1.55.1-dev, 1.55.2, 1.55.2-dev, 1.56, 1.56-dev, 1.56.0, 1.56.0-dev, 1.57, 1.57-dev, 1.57.0, 1.57.0-dev, 1.58, 1.58-dev, 1.58.0, 1.58.0-dev, 1.59, 1.59-dev, 1.59.0, 1.59.0-dev, 1.59.1, 1.59.1-dev, 1.60, 1.60-dev, 1.60.0, 1.60.0-dev, 1.60.1, 1.60.1-dev, latest, latest-dev |


- `cgr.dev/chainguard` - the Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.
- `cgr.dev/chainguard-private` - the Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

The commands listed on this page will default to the `latest` tag, but you can specify a different tag to fetch attestations for.

## Verifying semgrep Image Signatures
The **semgrep** Chainguard Images are signed using Sigstore, and you can check the included signatures using `cosign`.

The `cosign verify` command will pull detailed information about all signatures found for the provided image.

### Public Registry

```shell
cosign verify \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  cgr.dev/chainguard/semgrep | jq
```

### Private/Dedicated Registry

```shell
cosign verify \
--certificate-oidc-issuer=https://token.actions.githubusercontent.com \
--certificate-identity=https://github.com/chainguard-images/images-private/.github/workflows/release.yaml@refs/heads/main \
cgr.dev/chainguard-private/semgrep | jq
```

## Downloading semgrep Image Attestations

The following [attestations](https://slsa.dev/attestation-model) for the semgrep image can be obtained and verified via cosign:

| Attestation Type | Description |
|----------------|-------------|
| `https://slsa.dev/provenance/v1` | The [SLSA 1.0](https://slsa.dev/spec/v1.0/provenance) provenance attestation contains information about the image build environment. |
| `https://apko.dev/image-configuration` | Contains the configuration used by that particular image build, including direct dependencies, user accounts, and entry point. |
| `https://spdx.dev/Document` | Contains the image SBOM (Software Bill of Materials) in SPDX format. |


To download an attestation, use the `cosign download attestation` command and provide both the predicate type and the build platform. For example, the following command will obtain the SBOM for the semgrep image on `linux/amd64`:

### Public Registry

```shell
cosign download attestation \
  --platform=linux/amd64 \
  --predicate-type=https://spdx.dev/Document \
  cgr.dev/chainguard/semgrep | jq -r .payload | base64 -d | jq .predicate
```

### Private/Dedicated Registry

```shell
cosign download attestation \
--platform=linux/amd64 \
--predicate-type=https://spdx.dev/Document \
cgr.dev/chainguard-private/semgrep | jq -r .payload | base64 -d | jq .predicate
```

By default, this command will fetch the SBOM assigned to the `latest` tag. You can also specify the tag you want to fetch the attestation from.

To download a different attestation, replace the `--predicate-type` parameter value with the desired attestation URL identifier.

## Verifying semgrep Image Attestations
You can use the `cosign verify-attestation` command to check the signatures of the semgrep image attestations:

### Public Registry

```shell
cosign verify-attestation \
  --type https://spdx.dev/Document \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  cgr.dev/chainguard/semgrep
```

### Private/Dedicated Registry

```shell
cosign verify-attestation \
--type https://spdx.dev/Document \
--certificate-oidc-issuer=https://token.actions.githubusercontent.com \
--certificate-identity=https://github.com/chainguard-images/images-private/.github/workflows/release.yaml@refs/heads/main \
cgr.dev/chainguard-private/semgrep
```

This will pull in the signature for the attestation specified by the `--type` parameter, which in this case is the SPDX attestation. You will receive output that verifies the SBOM attestation signature in cosign's transparency log:

```
Verification for cgr.dev/chainguard/semgrep --
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
