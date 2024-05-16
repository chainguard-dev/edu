---
title: "Provenance Information for stakater-reloader Images"
type: "article"
unlisted: true
description: "Provenance information for stakater-reloader Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-05-16 00:37:58
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 600
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/stakater-reloader/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/stakater-reloader/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/stakater-reloader/tags_history/" >}}
{{< tab title="Provenance" active=true url="/chainguard/chainguard-images/reference/stakater-reloader/provenance_info/" >}}
{{</ tabs >}}

All Chainguard Images contain verifiable signatures and high-quality SBOMs (software bill of materials), features that enable users to confirm the origin of each image build and have a detailed list of everything that is packed within.

You'll need [cosign](https://docs.sigstore.dev/cosign/overview/) and [jq](https://stedolan.github.io/jq/) in order to download and verify image attestations.

### Registry and Tags for stakater-reloader Image
Attestations are provided per image build, so you'll need to specify the correct tag and registry when pulling attestations from an image with `cosign`.

| Registry                     | Tags                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `cgr.dev/chainguard`         | latest, latest-dev                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `cgr.dev/chainguard-private` | 0, 0-dev, 0.0, 0.0-dev, 0.0.119, 0.0.119-dev, 0.0.128, 0.0.128-dev, 1, 1-dev, 1.0, 1.0-dev, 1.0.29, 1.0.29-dev, 1.0.30, 1.0.30-dev, 1.0.32, 1.0.32-dev, 1.0.34, 1.0.34-dev, 1.0.35, 1.0.35-dev, 1.0.36, 1.0.36-dev, 1.0.38, 1.0.38-dev, 1.0.39, 1.0.39-dev, 1.0.40, 1.0.40-dev, 1.0.41, 1.0.41-dev, 1.0.42, 1.0.42-dev, 1.0.43, 1.0.43-dev, 1.0.44, 1.0.44-dev, 1.0.46, 1.0.46-dev, 1.0.47, 1.0.47-dev, 1.0.48, 1.0.48-dev, 1.0.50, 1.0.50-dev, 1.0.51, 1.0.51-dev, 1.0.52, 1.0.52-dev, 1.0.53, 1.0.53-dev, 1.0.54, 1.0.54-dev, 1.0.56, 1.0.56-dev, 1.0.57, 1.0.57-dev, 1.0.58, 1.0.58-dev, 1.0.60, 1.0.60-dev, 1.0.62, 1.0.62-dev, 1.0.63, 1.0.63-dev, 1.0.64, 1.0.64-dev, 1.0.65, 1.0.65-dev, 1.0.67, 1.0.67-dev, 1.0.68, 1.0.68-dev, 1.0.69, 1.0.69-dev, 1.0.71, 1.0.71-dev, 1.0.72, 1.0.72-dev, 1.0.74, 1.0.74-dev, 1.0.75, 1.0.75-dev, 1.0.76, 1.0.76-dev, 1.0.77, 1.0.77-dev, 1.0.78, 1.0.78-dev, 1.0.79, 1.0.79-dev, 1.0.80, 1.0.80-dev, 1.0.82, 1.0.82-dev, 1.0.84, 1.0.84-dev, 1.0.87, 1.0.87-dev, 1.0.88, 1.0.88-dev, 1.0.90, 1.0.90-dev, 1.0.91, 1.0.91-dev, 1.0.92, 1.0.92-dev, 1.0.93, 1.0.93-dev, 1.0.94, 1.0.94-dev, 1.0.95, 1.0.95-dev, 1.0.97, 1.0.97-dev, latest, latest-dev |


- `cgr.dev/chainguard` - the Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.
- `cgr.dev/chainguard-private` - the Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

The commands listed on this page will default to the `latest` tag, but you can specify a different tag to fetch attestations for.

## Verifying stakater-reloader Image Signatures
The **stakater-reloader** Chainguard Images are signed using Sigstore, and you can check the included signatures using `cosign`.

The `cosign verify` command will pull detailed information about all signatures found for the provided image.

### Public Registry

```shell
cosign verify \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  cgr.dev/chainguard/stakater-reloader | jq
```

### Private/Dedicated Registry

```shell
cosign verify \
--certificate-oidc-issuer=https://token.actions.githubusercontent.com \
--certificate-identity=https://github.com/chainguard-images/images-private/.github/workflows/release.yaml@refs/heads/main \
cgr.dev/chainguard-private/stakater-reloader | jq
```

## Downloading stakater-reloader Image Attestations

The following [attestations](https://slsa.dev/attestation-model) for the stakater-reloader image can be obtained and verified via cosign:

| Attestation Type | Description |
|----------------|-------------|
| `https://slsa.dev/provenance/v1` | The [SLSA 1.0](https://slsa.dev/spec/v1.0/provenance) provenance attestation contains information about the image build environment. |
| `https://apko.dev/image-configuration` | Contains the configuration used by that particular image build, including direct dependencies, user accounts, and entry point. |
| `https://spdx.dev/Document` | Contains the image SBOM (Software Bill of Materials) in SPDX format. |


To download an attestation, use the `cosign download attestation` command and provide both the predicate type and the build platform. For example, the following command will obtain the SBOM for the stakater-reloader image on `linux/amd64`:

### Public Registry

```shell
cosign download attestation \
  --platform=linux/amd64 \
  --predicate-type=https://spdx.dev/Document \
  cgr.dev/chainguard/stakater-reloader | jq -r .payload | base64 -d | jq .predicate
```

### Private/Dedicated Registry

```shell
cosign download attestation \
--platform=linux/amd64 \
--predicate-type=https://spdx.dev/Document \
cgr.dev/chainguard-private/stakater-reloader | jq -r .payload | base64 -d | jq .predicate
```

By default, this command will fetch the SBOM assigned to the `latest` tag. You can also specify the tag you want to fetch the attestation from.

To download a different attestation, replace the `--predicate-type` parameter value with the desired attestation URL identifier.

## Verifying stakater-reloader Image Attestations
You can use the `cosign verify-attestation` command to check the signatures of the stakater-reloader image attestations:

### Public Registry

```shell
cosign verify-attestation \
  --type https://spdx.dev/Document \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  cgr.dev/chainguard/stakater-reloader
```

### Private/Dedicated Registry

```shell
cosign verify-attestation \
--type https://spdx.dev/Document \
--certificate-oidc-issuer=https://token.actions.githubusercontent.com \
--certificate-identity=https://github.com/chainguard-images/images-private/.github/workflows/release.yaml@refs/heads/main \
cgr.dev/chainguard-private/stakater-reloader
```

This will pull in the signature for the attestation specified by the `--type` parameter, which in this case is the SPDX attestation. You will receive output that verifies the SBOM attestation signature in cosign's transparency log:

```
Verification for cgr.dev/chainguard/stakater-reloader --
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
