---
title: "Provenance Information for go Images"
type: "article"
unlisted: true
description: "Provenance information for go Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 600
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/go/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/go/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/go/tags_history/" >}}
{{< tab title="Provenance" active=true url="/chainguard/chainguard-images/reference/go/provenance_info/" >}}
{{</ tabs >}}

All Chainguard Images contain verifiable signatures and high-quality SBOMs (software bill of materials), features that enable users to confirm the origin of each image built and have a detailed list of everything that is packed within.

## Verifying Image Signatures
The **go** Chainguard Images are signed using Sigstore, and you can check the included signatures using `cosign`.

The following command requires [cosign](https://docs.sigstore.dev/cosign/overview/) and [jq](https://stedolan.github.io/jq/) to be installed on your machine. It will pull detailed information about all signatures found for the provided image.

```shell
cosign verify --certificate-oidc-issuer=https://token.actions.githubusercontent.com --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main cgr.dev/chainguard/go | jq
```

By default, this command will fetch signatures for the `latest` tag. You can also specify the tag you want to fetch signatures for.

## Downloading and Verifying SBOMs

All Chainguard Images come with a high-quality Software Bill Of Materials (SBOM) attested at build-time. The SBOM can be downloaded using the cosign tool:

```shell
cosign download attestation \
  --predicate-type=https://spdx.dev/Document \
  cgr.dev/chainguard/go | jq -r .payload | base64 -d | jq
```
By default, this command will fetch the SBOM assigned to the `latest` tag. You can also specify the tag you want to fetch the SBOM from.

With cosign 2.0+, you can use the `cosign verify-attestation` command to check the signature of an SBOM:

```shell
cosign verify-attestation \
  --type https://spdx.dev/Document \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  --platform=linux/amd64 \
  cgr.dev/chainguard/go
```

And you should get output that verifies the SBOM signature in cosign's transparency log:

```
Verification for cgr.dev/chainguard/go --
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
