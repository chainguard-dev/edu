---
title: "Provenance Information for git Images"
type: "article"
unlisted: true
description: "Provenance information for git Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-03-01 12:14:22
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 600
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/git/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/git/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/git/tags_history/" >}}
{{< tab title="Provenance" active=true url="/chainguard/chainguard-images/reference/git/provenance_info/" >}}
{{</ tabs >}}

All Chainguard Images contain verifiable signatures and high-quality SBOMs (software bill of materials), features that enable users to confirm the origin of each image build and have a detailed list of everything that is packed within.

You'll need [cosign](https://docs.sigstore.dev/cosign/overview/) and [jq](https://stedolan.github.io/jq/) in order to download and verify image attestations.

### Registry and Tags for git Image
Attestations are provided per image build, so you'll need to specify the correct tag and registry when pulling attestations from an image with `cosign`.

| Registry                     | Tags                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `cgr.dev/chainguard`         | latest, latest-dev, latest-glibc, latest-glibc-dev, latest-glibc-nonroot, latest-glibc-nonroot-dev, latest-glibc-root, latest-glibc-root-dev, latest-nonroot, latest-nonroot-dev, latest-root, latest-root-dev                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `cgr.dev/chainguard-private` | 2, 2-dev, 2.40, 2.40-dev, 2.40.0, 2.40.0-dev, 2.40.1, 2.40.1-dev, 2.41, 2.41-dev, 2.41.0, 2.41.0-dev, 2.42, 2.42-dev, 2.42.0, 2.42.0-dev, 2.42.1, 2.42.1-dev, 2.43, 2.43-dev, 2.43.0, 2.43.0-dev, glibc-2, glibc-2-dev, glibc-2.40, glibc-2.40-dev, glibc-2.40.0, glibc-2.40.0-dev, glibc-2.40.1, glibc-2.40.1-dev, glibc-2.41, glibc-2.41-dev, glibc-2.41.0, glibc-2.41.0-dev, glibc-2.42, glibc-2.42-dev, glibc-2.42.0, glibc-2.42.0-dev, glibc-2.42.1, glibc-2.42.1-dev, glibc-2.43, glibc-2.43-dev, glibc-2.43.0, glibc-2.43.0-dev, glibc-2.43.1, glibc-2.43.1-dev, glibc-2.43.2, glibc-2.43.2-dev, glibc-2.44, glibc-2.44-dev, glibc-2.44.0, glibc-2.44.0-dev, glibc-root-2, glibc-root-2-dev, glibc-root-2.40, glibc-root-2.40.0, glibc-root-2.40.1, glibc-root-2.41, glibc-root-2.41-dev, glibc-root-2.41.0, glibc-root-2.41.0-dev, glibc-root-2.42, glibc-root-2.42-dev, glibc-root-2.42.0, glibc-root-2.42.0-dev, glibc-root-2.42.1, glibc-root-2.42.1-dev, glibc-root-2.43, glibc-root-2.43-dev, glibc-root-2.43.0, glibc-root-2.43.0-dev, glibc-root-2.43.1, glibc-root-2.43.1-dev, glibc-root-2.43.2, glibc-root-2.43.2-dev, glibc-root-2.44, glibc-root-2.44-dev, glibc-root-2.44.0, glibc-root-2.44.0-dev, latest, latest-dev, latest-glibc, latest-glibc-dev, latest-glibc-nonroot, latest-glibc-nonroot-dev, latest-glibc-root, latest-glibc-root-dev, latest-nonroot, latest-nonroot-dev, latest-root, latest-root-dev, root-2, root-2-dev, root-2.40, root-2.40.0, root-2.40.1, root-2.41, root-2.41-dev, root-2.41.0, root-2.41.0-dev, root-2.42, root-2.42-dev, root-2.42.0, root-2.42.0-dev, root-2.42.1, root-2.42.1-dev, root-2.43, root-2.43-dev, root-2.43.0, root-2.43.0-dev |


- `cgr.dev/chainguard` - the Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.
- `cgr.dev/chainguard-private` - the Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

The commands listed on this page will default to the `latest` tag, but you can specify a different tag to fetch attestations for.

## Verifying git Image Signatures
The **git** Chainguard Images are signed using Sigstore, and you can check the included signatures using `cosign`.

The `cosign verify` command will pull detailed information about all signatures found for the provided image.

### Public Registry

```shell
cosign verify \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  cgr.dev/chainguard/git | jq
```

### Private/Dedicated Registry

```shell
cosign verify \
--certificate-oidc-issuer=https://token.actions.githubusercontent.com \
--certificate-identity=https://github.com/chainguard-images/images-private/.github/workflows/release.yaml@refs/heads/main \
cgr.dev/chainguard-private/git | jq
```

## Downloading git Image Attestations

The following [attestations](https://slsa.dev/attestation-model) for the git image can be obtained and verified via cosign:

| Attestation Type | Description |
|----------------|-------------|
| `https://slsa.dev/provenance/v1` | The [SLSA 1.0](https://slsa.dev/spec/v1.0/provenance) provenance attestation contains information about the image build environment. |
| `https://apko.dev/image-configuration` | Contains the configuration used by that particular image build, including direct dependencies, user accounts, and entry point. |
| `https://spdx.dev/Document` | Contains the image SBOM (Software Bill of Materials) in SPDX format. |


To download an attestation, use the `cosign download attestation` command and provide both the predicate type and the build platform. For example, the following command will obtain the SBOM for the git image on `linux/amd64`:

### Public Registry

```shell
cosign download attestation \
  --platform=linux/amd64 \
  --predicate-type=https://spdx.dev/Document \
  cgr.dev/chainguard/git | jq -r .payload | base64 -d | jq .predicate
```

### Private/Dedicated Registry

```shell
cosign download attestation \
--platform=linux/amd64 \
--predicate-type=https://spdx.dev/Document \
cgr.dev/chainguard-private/git | jq -r .payload | base64 -d | jq .predicate
```

By default, this command will fetch the SBOM assigned to the `latest` tag. You can also specify the tag you want to fetch the attestation from.

To download a different attestation, replace the `--predicate-type` parameter value with the desired attestation URL identifier.

## Verifying git Image Attestations
You can use the `cosign verify-attestation` command to check the signatures of the git image attestations:

### Public Registry

```shell
cosign verify-attestation \
  --type https://spdx.dev/Document \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  cgr.dev/chainguard/git
```

### Private/Dedicated Registry

```shell
cosign verify-attestation \
--type https://spdx.dev/Document \
--certificate-oidc-issuer=https://token.actions.githubusercontent.com \
--certificate-identity=https://github.com/chainguard-images/images-private/.github/workflows/release.yaml@refs/heads/main \
cgr.dev/chainguard-private/git
```

This will pull in the signature for the attestation specified by the `--type` parameter, which in this case is the SPDX attestation. You will receive output that verifies the SBOM attestation signature in cosign's transparency log:

```
Verification for cgr.dev/chainguard/git --
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
