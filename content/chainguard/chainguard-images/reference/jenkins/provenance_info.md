---
title: "Provenance Information for jenkins Images"
type: "article"
unlisted: true
description: "Provenance information for jenkins Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 600
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jenkins/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jenkins/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/jenkins/tags_history/" >}}
{{< tab title="Provenance" active=true url="/chainguard/chainguard-images/reference/jenkins/provenance_info/" >}}
{{</ tabs >}}

All Chainguard Images contain verifiable signatures and high-quality SBOMs (software bill of materials), features that enable users to confirm the origin of each image build and have a detailed list of everything that is packed within.

You'll need [cosign](https://docs.sigstore.dev/cosign/overview/) and [jq](https://stedolan.github.io/jq/) in order to download and verify image attestations.

### Registry and Tags for jenkins Image
Attestations are provided per image build, so you'll need to specify the correct tag and registry when pulling attestations from an image with `cosign`.

| Registry                     | Tags                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `cgr.dev/chainguard`         | latest, latest-dev                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `cgr.dev/chainguard-private` | 2, 2-dev, 2.400, 2.401, 2.402, 2.409, 2.410, 2.411, 2.412, 2.413, 2.414, 2.415, 2.417, 2.419, 2.420, 2.421, 2.422, 2.423, 2.424, 2.425, 2.426, 2.427, 2.428, 2.429, 2.429-dev, 2.431, 2.431-dev, 2.432, 2.432-dev, 2.434, 2.434-dev, 2.435, 2.435-dev, 2.437, 2.437-dev, 2.439, 2.439-dev, 2.441, 2.441-dev, 2.442, 2.442-dev, 2.443, 2.443-dev, 2.444, 2.444-dev, 2.445, 2.445-dev, 2.446, 2.446-dev, 2.447, 2.447-dev, 2.448, 2.448-dev, 2.449, 2.449-dev, 2.450, 2.450-dev, 2.451, 2.451-dev, 2.452, 2.452-dev, 2.453, 2.453-dev, latest, latest-dev |


- `cgr.dev/chainguard` - the Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.
- `cgr.dev/chainguard-private` - the Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

The commands listed on this page will default to the `latest` tag, but you can specify a different tag to fetch attestations for.

## Verifying jenkins Image Signatures
The **jenkins** Chainguard Images are signed using Sigstore, and you can check the included signatures using `cosign`.

The `cosign verify` command will pull detailed information about all signatures found for the provided image.

### Public Registry

```shell
cosign verify \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  cgr.dev/chainguard/jenkins | jq
```

### Private/Dedicated Registry

```shell
cosign verify \
--certificate-oidc-issuer=https://token.actions.githubusercontent.com \
--certificate-identity=https://github.com/chainguard-images/images-private/.github/workflows/release.yaml@refs/heads/main \
cgr.dev/chainguard-private/jenkins | jq
```

## Downloading jenkins Image Attestations

The following [attestations](https://slsa.dev/attestation-model) for the jenkins image can be obtained and verified via cosign:

| Attestation Type | Description |
|----------------|-------------|
| `https://slsa.dev/provenance/v1` | The [SLSA 1.0](https://slsa.dev/spec/v1.0/provenance) provenance attestation contains information about the image build environment. |
| `https://apko.dev/image-configuration` | Contains the configuration used by that particular image build, including direct dependencies, user accounts, and entry point. |
| `https://spdx.dev/Document` | Contains the image SBOM (Software Bill of Materials) in SPDX format. |


To download an attestation, use the `cosign download attestation` command and provide both the predicate type and the build platform. For example, the following command will obtain the SBOM for the jenkins image on `linux/amd64`:

### Public Registry

```shell
cosign download attestation \
  --platform=linux/amd64 \
  --predicate-type=https://spdx.dev/Document \
  cgr.dev/chainguard/jenkins | jq -r .payload | base64 -d | jq .predicate
```

### Private/Dedicated Registry

```shell
cosign download attestation \
--platform=linux/amd64 \
--predicate-type=https://spdx.dev/Document \
cgr.dev/chainguard-private/jenkins | jq -r .payload | base64 -d | jq .predicate
```

By default, this command will fetch the SBOM assigned to the `latest` tag. You can also specify the tag you want to fetch the attestation from.

To download a different attestation, replace the `--predicate-type` parameter value with the desired attestation URL identifier.

## Verifying jenkins Image Attestations
You can use the `cosign verify-attestation` command to check the signatures of the jenkins image attestations:

### Public Registry

```shell
cosign verify-attestation \
  --type https://spdx.dev/Document \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  cgr.dev/chainguard/jenkins
```

### Private/Dedicated Registry

```shell
cosign verify-attestation \
--type https://spdx.dev/Document \
--certificate-oidc-issuer=https://token.actions.githubusercontent.com \
--certificate-identity=https://github.com/chainguard-images/images-private/.github/workflows/release.yaml@refs/heads/main \
cgr.dev/chainguard-private/jenkins
```

This will pull in the signature for the attestation specified by the `--type` parameter, which in this case is the SPDX attestation. You will receive output that verifies the SBOM attestation signature in cosign's transparency log:

```
Verification for cgr.dev/chainguard/jenkins --
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
