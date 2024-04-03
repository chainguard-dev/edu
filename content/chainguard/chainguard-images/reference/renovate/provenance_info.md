---
title: "Provenance Information for renovate Images"
type: "article"
unlisted: true
description: "Provenance information for renovate Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-04-03 00:49:16
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 600
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/renovate/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/renovate/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/renovate/tags_history/" >}}
{{< tab title="Provenance" active=true url="/chainguard/chainguard-images/reference/renovate/provenance_info/" >}}
{{</ tabs >}}

All Chainguard Images contain verifiable signatures and high-quality SBOMs (software bill of materials), features that enable users to confirm the origin of each image build and have a detailed list of everything that is packed within.

You'll need [cosign](https://docs.sigstore.dev/cosign/overview/) and [jq](https://stedolan.github.io/jq/) in order to download and verify image attestations.

### Registry and Tags for renovate Image
Attestations are provided per image build, so you'll need to specify the correct tag and registry when pulling attestations from an image with `cosign`.

| Registry                     | Tags                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `cgr.dev/chainguard`         | No public tags are available for this image.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `cgr.dev/chainguard-private` | 37, 37-dev, 37.100, 37.100-dev, 37.100.0, 37.100.0-dev, 37.100.2, 37.100.2-dev, 37.102, 37.102-dev, 37.102.0, 37.102.0-dev, 37.103, 37.103-dev, 37.103.1, 37.103.1-dev, 37.105, 37.105-dev, 37.105.3, 37.105.3-dev, 37.107, 37.107-dev, 37.107.0, 37.107.0-dev, 37.108, 37.108-dev, 37.108.0, 37.108.0-dev, 37.115, 37.115-dev, 37.115.0, 37.115.0-dev, 37.116, 37.116-dev, 37.116.0, 37.116.0-dev, 37.118, 37.118-dev, 37.118.0, 37.118.0-dev, 37.119, 37.119-dev, 37.119.0, 37.119.0-dev, 37.122, 37.122-dev, 37.122.0, 37.122.0-dev, 37.126, 37.126-dev, 37.126.1, 37.126.1-dev, 37.126.2, 37.126.2-dev, 37.126.3, 37.126.3-dev, 37.126.4, 37.126.4-dev, 37.127, 37.127-dev, 37.127.0, 37.127.0-dev, 37.128, 37.128-dev, 37.128.0, 37.128.0-dev, 37.128.2, 37.128.2-dev, 37.128.3, 37.128.3-dev, 37.128.5, 37.128.5-dev, 37.129, 37.129-dev, 37.129.1, 37.129.1-dev, 37.130, 37.130-dev, 37.130.0, 37.130.0-dev, 37.131, 37.131-dev, 37.131.0, 37.131.0-dev, 37.135, 37.135-dev, 37.135.0, 37.135.0-dev, 37.137, 37.137-dev, 37.137.0, 37.137.0-dev, 37.137.1, 37.137.1-dev, 37.140, 37.140-dev, 37.140.0, 37.140.0-dev, 37.140.10, 37.140.10-dev, 37.140.4, 37.140.4-dev, 37.140.5, 37.140.5-dev, 37.142, 37.142-dev, 37.142.1, 37.142.1-dev, 37.143, 37.143-dev, 37.143.0, 37.143.0-dev, 37.144, 37.144-dev, 37.144.0, 37.144.0-dev, 37.149, 37.149-dev, 37.149.1, 37.149.1-dev, 37.151, 37.151-dev, 37.151.0, 37.151.0-dev, 37.152, 37.152-dev, 37.152.1, 37.152.1-dev, 37.162, 37.162-dev, 37.162.0, 37.162.0-dev, 37.162.1, 37.162.1-dev, 37.162.2, 37.162.2-dev, 37.163, 37.163-dev, 37.163.0, 37.163.0-dev, 37.164, 37.164-dev, 37.164.0, 37.164.0-dev, 37.165, 37.165-dev, 37.165.0, 37.165.0-dev, 37.165.3, 37.165.3-dev, 37.165.5, 37.165.5-dev, 37.165.7, 37.165.7-dev, 37.168, 37.168-dev, 37.168.3, 37.168.3-dev, 37.168.4, 37.168.4-dev, 37.172, 37.172-dev, 37.172.4, 37.172.4-dev, 37.174, 37.174-dev, 37.174.0, 37.174.0-dev, 37.174.5, 37.174.5-dev, 37.174.7, 37.174.7-dev, 37.175, 37.175-dev, 37.175.0, 37.175.0-dev, 37.176, 37.176-dev, 37.176.0, 37.176.0-dev, 37.176.1, 37.176.1-dev, 37.180, 37.180-dev, 37.180.0, 37.180.0-dev, 37.180.1, 37.180.1-dev, 37.181, 37.181-dev, 37.181.11, 37.181.11-dev, 37.182, 37.182-dev, 37.182.3, 37.182.3-dev, 37.186, 37.186-dev, 37.186.1, 37.186.1-dev, 37.191, 37.191-dev, 37.191.0, 37.191.0-dev, 37.191.1, 37.191.1-dev, 37.192, 37.192-dev, 37.192.2, 37.192.2-dev, 37.198, 37.198-dev, 37.198.0, 37.198.0-dev, 37.198.1, 37.198.1-dev, 37.198.3, 37.198.3-dev, 37.202, 37.202-dev, 37.202.0, 37.202.0-dev, 37.202.2, 37.202.2-dev, 37.203, 37.203-dev, 37.203.2, 37.203.2-dev, 37.203.3, 37.203.3-dev, 37.203.5, 37.203.5-dev, 37.206, 37.206-dev, 37.206.1, 37.206.1-dev, 37.208, 37.208-dev, 37.208.0, 37.208.0-dev, 37.211, 37.211-dev, 37.211.2, 37.211.2-dev, 37.214, 37.214-dev, 37.214.0, 37.214.0-dev, 37.214.1, 37.214.1-dev, 37.214.5, 37.214.5-dev, 37.221, 37.221-dev, 37.221.0, 37.221.0-dev, 37.221.1, 37.221.1-dev, 37.234, 37.234-dev, 37.234.1, 37.234.1-dev, 37.235, 37.235-dev, 37.235.1, 37.235.1-dev, 37.239, 37.239-dev, 37.239.0, 37.239.0-dev, 37.244, 37.244-dev, 37.244.1, 37.244.1-dev, 37.246, 37.246-dev, 37.246.1, 37.246.1-dev, 37.249, 37.249-dev, 37.249.1, 37.249.1-dev, 37.249.3, 37.249.3-dev, 37.252, 37.252-dev, 37.252.0, 37.252.0-dev, 37.256, 37.256-dev, 37.256.1, 37.256.1-dev, 37.261, 37.261-dev, 37.261.0, 37.261.0-dev, 37.262, 37.262-dev, 37.262.1, 37.262.1-dev, 37.263, 37.263-dev, 37.263.0, 37.263.0-dev, 37.263.1, 37.263.1-dev, 37.264, 37.264-dev, 37.264.0, 37.264.0-dev, 37.265, 37.265-dev, 37.265.0, 37.265.0-dev, 37.267, 37.267-dev, 37.267.0, 37.267.0-dev, 37.267.1, 37.267.1-dev, 37.269, 37.269-dev, 37.269.3, 37.269.3-dev, 37.269.5, 37.269.5-dev, 37.270, 37.270-dev, 37.270.0, 37.270.0-dev, 37.272, 37.272-dev, 37.272.0, 37.272.0-dev, 37.273, 37.273-dev, 37.273.0, 37.273.0-dev, 37.274, 37.274-dev, 37.274.0, 37.274.0-dev, 37.276, 37.276-dev, 37.276.0, 37.276.0-dev, 37.277, 37.277-dev, 37.277.0, 37.277.0-dev, 37.279, 37.279-dev, 37.279.0, 37.279.0-dev, 37.91, 37.91-dev, 37.91.0, 37.91.0-dev, 37.91.4, 37.91.4-dev, 37.93, 37.93-dev, 37.93.2, 37.93.2-dev, 37.98, 37.98-dev, 37.98.0, 37.98.0-dev, latest, latest-dev |


- `cgr.dev/chainguard` - the Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.
- `cgr.dev/chainguard-private` - the Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

The commands listed on this page will default to the `latest` tag, but you can specify a different tag to fetch attestations for.

## Verifying renovate Image Signatures
The **renovate** Chainguard Images are signed using Sigstore, and you can check the included signatures using `cosign`.

The `cosign verify` command will pull detailed information about all signatures found for the provided image.

### Public Registry

```shell
cosign verify \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  cgr.dev/chainguard/renovate | jq
```

### Private/Dedicated Registry

```shell
cosign verify \
--certificate-oidc-issuer=https://token.actions.githubusercontent.com \
--certificate-identity=https://github.com/chainguard-images/images-private/.github/workflows/release.yaml@refs/heads/main \
cgr.dev/chainguard-private/renovate | jq
```

## Downloading renovate Image Attestations

The following [attestations](https://slsa.dev/attestation-model) for the renovate image can be obtained and verified via cosign:

| Attestation Type | Description |
|----------------|-------------|
| `https://slsa.dev/provenance/v1` | The [SLSA 1.0](https://slsa.dev/spec/v1.0/provenance) provenance attestation contains information about the image build environment. |
| `https://apko.dev/image-configuration` | Contains the configuration used by that particular image build, including direct dependencies, user accounts, and entry point. |
| `https://spdx.dev/Document` | Contains the image SBOM (Software Bill of Materials) in SPDX format. |


To download an attestation, use the `cosign download attestation` command and provide both the predicate type and the build platform. For example, the following command will obtain the SBOM for the renovate image on `linux/amd64`:

### Public Registry

```shell
cosign download attestation \
  --platform=linux/amd64 \
  --predicate-type=https://spdx.dev/Document \
  cgr.dev/chainguard/renovate | jq -r .payload | base64 -d | jq .predicate
```

### Private/Dedicated Registry

```shell
cosign download attestation \
--platform=linux/amd64 \
--predicate-type=https://spdx.dev/Document \
cgr.dev/chainguard-private/renovate | jq -r .payload | base64 -d | jq .predicate
```

By default, this command will fetch the SBOM assigned to the `latest` tag. You can also specify the tag you want to fetch the attestation from.

To download a different attestation, replace the `--predicate-type` parameter value with the desired attestation URL identifier.

## Verifying renovate Image Attestations
You can use the `cosign verify-attestation` command to check the signatures of the renovate image attestations:

### Public Registry

```shell
cosign verify-attestation \
  --type https://spdx.dev/Document \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  cgr.dev/chainguard/renovate
```

### Private/Dedicated Registry

```shell
cosign verify-attestation \
--type https://spdx.dev/Document \
--certificate-oidc-issuer=https://token.actions.githubusercontent.com \
--certificate-identity=https://github.com/chainguard-images/images-private/.github/workflows/release.yaml@refs/heads/main \
cgr.dev/chainguard-private/renovate
```

This will pull in the signature for the attestation specified by the `--type` parameter, which in this case is the SPDX attestation. You will receive output that verifies the SBOM attestation signature in cosign's transparency log:

```
Verification for cgr.dev/chainguard/renovate --
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
