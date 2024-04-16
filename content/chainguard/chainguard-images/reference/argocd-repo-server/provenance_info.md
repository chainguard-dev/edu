---
title: "Provenance Information for argocd-repo-server Images"
type: "article"
unlisted: true
description: "Provenance information for argocd-repo-server Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-04-16 00:44:43
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 600
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/argocd-repo-server/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/argocd-repo-server/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/argocd-repo-server/tags_history/" >}}
{{< tab title="Provenance" active=true url="/chainguard/chainguard-images/reference/argocd-repo-server/provenance_info/" >}}
{{</ tabs >}}

All Chainguard Images contain verifiable signatures and high-quality SBOMs (software bill of materials), features that enable users to confirm the origin of each image build and have a detailed list of everything that is packed within.

You'll need [cosign](https://docs.sigstore.dev/cosign/overview/) and [jq](https://stedolan.github.io/jq/) in order to download and verify image attestations.

### Registry and Tags for argocd-repo-server Image
Attestations are provided per image build, so you'll need to specify the correct tag and registry when pulling attestations from an image with `cosign`.

| Registry                     | Tags                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `cgr.dev/chainguard`         | latest, latest-dev                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `cgr.dev/chainguard-private` | 2, 2-dev, 2.10, 2.10-dev, 2.10.1, 2.10.1-dev, 2.10.2, 2.10.2-dev, 2.10.4, 2.10.4-dev, 2.10.5, 2.10.5-dev, 2.10.6, 2.10.6-dev, 2.10.7, 2.10.7-dev, 2.7, 2.7-dev, 2.7.10, 2.7.10-dev, 2.7.13, 2.7.13-dev, 2.7.14, 2.7.14-dev, 2.7.15, 2.7.15-dev, 2.7.16, 2.7.16-dev, 2.7.17, 2.7.17-dev, 2.7.6, 2.7.6-dev, 2.7.7, 2.7.7-dev, 2.7.8, 2.7.8-dev, 2.7.9, 2.7.9-dev, 2.8, 2.8-dev, 2.8.0, 2.8.0-dev, 2.8.1, 2.8.1-dev, 2.8.10, 2.8.10-dev, 2.8.13, 2.8.13-dev, 2.8.14, 2.8.14-dev, 2.8.15, 2.8.15-dev, 2.8.16, 2.8.16-dev, 2.8.2, 2.8.2-dev, 2.8.3, 2.8.3-dev, 2.8.4, 2.8.4-dev, 2.8.5, 2.8.5-dev, 2.8.6, 2.8.6-dev, 2.8.7, 2.8.7-dev, 2.8.8, 2.8.8-dev, 2.8.9, 2.8.9-dev, 2.9, 2.9-dev, 2.9.10, 2.9.10-dev, 2.9.11, 2.9.11-dev, 2.9.12, 2.9.12-dev, 2.9.2, 2.9.2-dev, 2.9.3, 2.9.3-dev, 2.9.4, 2.9.4-dev, 2.9.5, 2.9.5-dev, 2.9.6, 2.9.6-dev, 2.9.7, 2.9.7-dev, 2.9.9, 2.9.9-dev, latest, latest-dev, v2, v2.8, v2.8.4 |


- `cgr.dev/chainguard` - the Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.
- `cgr.dev/chainguard-private` - the Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

The commands listed on this page will default to the `latest` tag, but you can specify a different tag to fetch attestations for.

## Verifying argocd-repo-server Image Signatures
The **argocd-repo-server** Chainguard Images are signed using Sigstore, and you can check the included signatures using `cosign`.

The `cosign verify` command will pull detailed information about all signatures found for the provided image.

### Public Registry

```shell
cosign verify \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  cgr.dev/chainguard/argocd-repo-server | jq
```

### Private/Dedicated Registry

```shell
cosign verify \
--certificate-oidc-issuer=https://token.actions.githubusercontent.com \
--certificate-identity=https://github.com/chainguard-images/images-private/.github/workflows/release.yaml@refs/heads/main \
cgr.dev/chainguard-private/argocd-repo-server | jq
```

## Downloading argocd-repo-server Image Attestations

The following [attestations](https://slsa.dev/attestation-model) for the argocd-repo-server image can be obtained and verified via cosign:

| Attestation Type | Description |
|----------------|-------------|
| `https://slsa.dev/provenance/v1` | The [SLSA 1.0](https://slsa.dev/spec/v1.0/provenance) provenance attestation contains information about the image build environment. |
| `https://apko.dev/image-configuration` | Contains the configuration used by that particular image build, including direct dependencies, user accounts, and entry point. |
| `https://spdx.dev/Document` | Contains the image SBOM (Software Bill of Materials) in SPDX format. |


To download an attestation, use the `cosign download attestation` command and provide both the predicate type and the build platform. For example, the following command will obtain the SBOM for the argocd-repo-server image on `linux/amd64`:

### Public Registry

```shell
cosign download attestation \
  --platform=linux/amd64 \
  --predicate-type=https://spdx.dev/Document \
  cgr.dev/chainguard/argocd-repo-server | jq -r .payload | base64 -d | jq .predicate
```

### Private/Dedicated Registry

```shell
cosign download attestation \
--platform=linux/amd64 \
--predicate-type=https://spdx.dev/Document \
cgr.dev/chainguard-private/argocd-repo-server | jq -r .payload | base64 -d | jq .predicate
```

By default, this command will fetch the SBOM assigned to the `latest` tag. You can also specify the tag you want to fetch the attestation from.

To download a different attestation, replace the `--predicate-type` parameter value with the desired attestation URL identifier.

## Verifying argocd-repo-server Image Attestations
You can use the `cosign verify-attestation` command to check the signatures of the argocd-repo-server image attestations:

### Public Registry

```shell
cosign verify-attestation \
  --type https://spdx.dev/Document \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  cgr.dev/chainguard/argocd-repo-server
```

### Private/Dedicated Registry

```shell
cosign verify-attestation \
--type https://spdx.dev/Document \
--certificate-oidc-issuer=https://token.actions.githubusercontent.com \
--certificate-identity=https://github.com/chainguard-images/images-private/.github/workflows/release.yaml@refs/heads/main \
cgr.dev/chainguard-private/argocd-repo-server
```

This will pull in the signature for the attestation specified by the `--type` parameter, which in this case is the SPDX attestation. You will receive output that verifies the SBOM attestation signature in cosign's transparency log:

```
Verification for cgr.dev/chainguard/argocd-repo-server --
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
