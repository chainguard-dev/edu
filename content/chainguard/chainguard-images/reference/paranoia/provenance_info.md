---
title: "Provenance Information for paranoia Images"
type: "article"
unlisted: true
description: "Provenance information for paranoia Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 600
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/paranoia/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/paranoia/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/paranoia/tags_history/" >}}
{{< tab title="Provenance" active=true url="/chainguard/chainguard-images/reference/paranoia/provenance_info/" >}}
{{</ tabs >}}

All Chainguard Images contain verifiable signatures and high-quality SBOMs (software bill of materials), features that enable users to confirm the origin of each image built and have a detailed list of everything that is packed within.

## Verifying paranoia Image Signatures
The **paranoia** Chainguard Images are signed using Sigstore, and you can check the included signatures using `cosign`.

The following command requires [cosign](https://docs.sigstore.dev/cosign/overview/) and [jq](https://stedolan.github.io/jq/) to be installed on your machine. It will pull detailed information about all signatures found for the provided image.

```shell
cosign verify --certificate-oidc-issuer=https://token.actions.githubusercontent.com --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main cgr.dev/chainguard/paranoia | jq
```

By default, this command will fetch signatures for the `latest` tag. You can also specify the tag you want to fetch signatures for.

## Downloading paranoia Image Attestations

The following [attestations](https://slsa.dev/attestation-model) for the paranoia image can be obtained and verified via cosign:

| Attestation Type | Description |
|----------------|-------------|
| `https://slsa.dev/provenance/v1` | The [SLSA 1.0](https://slsa.dev/spec/v1.0/provenance) provenance attestation contains information about the image build environment. |
| `https://apko.dev/image-configuration` | Contains the configuration used by that particular image build, including direct dependencies, user accounts, and entry point. |
| `https://spdx.dev/Document` | Contains the image SBOM (Software Bill of Materials) in SPDX format. |


To download an attestation, use the `cosign download attestation` command and provide both the predicate type and the build platform. For example, the following command will obtain the SBOM for the paranoia image on `unix/amd64`:

```shell
cosign download attestation \
  --platform=unix/amd64 \
  --predicate-type=https://spdx.dev/Document \
  cgr.dev/chainguard/paranoia | jq -r .payload | base64 -d | jq .predicate
```
By default, this command will fetch the SBOM assigned to the `latest` tag. You can also specify the tag you want to fetch the attestation from.

To download a different attestation, replace the `--predicate-type` parameter value with the desired attestation URL identifier.

## Verifying paranoia Image Attestations
You can use the `cosign verify-attestation` command to check the signatures of the paranoia image attestations:

```shell
cosign verify-attestation \
--type https://spdx.dev/Document \
--certificate-oidc-issuer=https://token.actions.githubusercontent.com \
--certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
cgr.dev/chainguard/paranoia
```

This will pull in the signature for the attestation specified by the `--type` parameter, which in this case is the SPDX attestation. You should get output that verifies the SBOM attestation signature in cosign's transparency log:

```
Verification for cgr.dev/chainguard/paranoia --
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
