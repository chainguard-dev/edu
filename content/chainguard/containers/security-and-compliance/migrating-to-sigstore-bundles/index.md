---
title: "Migrating to Sigstore bundle signatures for Chainguard Containers"
linktitle: "Sigstore bundle migration"
type: "article"
description: "What changes when Chainguard Containers move from legacy Cosign signature tags to Sigstore bundles, which tools are affected, and what to do about it"
date: 2026-09-08T00:00:00+00:00
lastmod: 2026-09-08T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Cosign", "Migration", "Overview"]
images: []
weight: 035
toc: true
---

Chainguard is changing how container image signatures and attestations are published. Today they are stored as separate tags next to the image (`sha256-<digest>.sig` and `sha256-<digest>.att`) and logged to the Rekor v1 transparency log. They are moving to [Sigstore bundles](https://docs.sigstore.dev/about/bundle/) attached to the image as [OCI referrers](https://github.com/opencontainers/distribution-spec/blob/main/spec.md#listing-referrers) and logged to Rekor v2 with a signed timestamp.

This page explains what changes, who is affected, and what to do. Dates are communicated through Chainguard's breaking-change notices; this page describes the change itself.

## What changes

The migration happens in two steps:

1. **Dual publishing.** Every image gets both the legacy tags and the new bundle referrers. Nothing is removed. Most verification tooling keeps working unchanged, with one exception listed below.
2. **Bundles only.** The legacy `.sig` and `.att` tags are no longer published for new builds. Tooling that only understands the legacy tags stops finding signatures.

What does not change:

- The identities Chainguard signs with. The public registry is still signed by the `chainguard-images/images` GitHub Actions workflow identity, and images in your private registry are still signed by your organization's `image-syncer` and `custom-image-builder` identities. Existing `--certificate-identity` and `--certificate-oidc-issuer` values stay valid.
- The `cosign verify` and `cosign verify-attestation` commands in [Verifying Chainguard Containers with Cosign](/chainguard/containers/security-and-compliance/verifying-chainguard-images-and-metadata-signatures-with-cosign/). Cosign 3.1.1 and newer detects the format automatically.
- The attestation types Chainguard publishes: SPDX and CycloneDX SBOMs, SLSA provenance, and the apko image configuration.

## Am I affected?

Check each of the following:

- **Cosign version.** Run `cosign version`. You need **3.1.1 or newer**. See the compatibility table below for older releases.
- **How you find signatures.** Anything that lists or pulls `sha256-<digest>.sig` or `.att` tags directly, including `cosign tree` from Cosign 2.x, stops working once bundles are the only format. Use `oras discover <image>` or Cosign 3.x to list the referrers instead.
- **How you copy images.** Tools that copy an image by tag do not copy its referrers. If you mirror Chainguard Containers into your own registry or across an air gap, see [Verifying signatures in air-gapped environments](/open-source/sigstore/cosign/verifying-in-air-gapped-environments/).
- **Admission control.** If you enforce signatures with sigstore policy-controller or Kyverno, your policies need a configuration change before bundles become the only format. See the sections below.
- **Attestation scripts.** Scripts that parse `cosign download attestation` output need a small change; see the [note on download output](#cosign-download-attestation-output).

## Compatibility

### Cosign

| Cosign release | Legacy image | Dual-published image | Bundle-only image |
|---|---|---|---|
| 3.1.1 and newer | Verifies | Verifies | Verifies |
| 2.6.3 to 2.6.5 | Verifies | Fails unless you pass `--use-signed-timestamps` | Fails unless you pass `--use-signed-timestamps` |
| 2.6.2 and older | Verifies | Verifies (bundles are ignored) | Fails with `no signatures found` |

Cosign 2.6.3 to 2.6.5 detect the bundle but do not, by default, accept the signed timestamp that Rekor v2 entries carry, so verification fails with `threshold not met for verified log entry integrated timestamps`. Upgrade to Cosign 3.1.1 or newer, or add `--use-signed-timestamps` to `cosign verify` and `cosign verify-attestation`.

### sigstore policy-controller

Existing `ClusterImagePolicy` resources keep working while images are dual published. Once bundles are the only format, policies that use the legacy signature path fail closed. The released policy-controller versions cannot verify bundle image signatures directly, but they can verify the signature bundle as an attestation. See [Using policy-controller to verify signed Chainguard Containers](/open-source/sigstore/policy-controller/policies/using-policy-controller-to-verify-signed-chainguard-images/).

### Kyverno

Existing `verifyImages` rules of type `Cosign` keep working while images are dual published and fail closed once bundles are the only format. Kyverno 1.19.0 and newer verifies bundles with `type: SigstoreBundle`. See [Enforcing Chainguard Container signatures with Kyverno](/chainguard/containers/security-and-compliance/enforcement/kyverno/).

### chainctl

Attestation commands in `chainctl images` require a chainctl release with bundle support. Update to the version named in the breaking-change notice.

## `cosign download attestation` output

For bundle attestations, `cosign download attestation` prints the whole Sigstore bundle as one JSON object per line instead of the bare DSSE envelope. The statement moves from `.payload` to `.dsseEnvelope.payload`. Use a `jq` expression that handles both:

```shell
cosign download attestation --predicate-type=https://spdx.dev/Document cgr.dev/chainguard/go \
  | jq -r '.dsseEnvelope.payload // .payload' | base64 -d | jq .predicate
```

`cosign verify-attestation` output is unchanged and remains the recommended way to read attestations, because it also verifies them.

## What to do

1. Upgrade Cosign to 3.1.1 or newer everywhere you verify Chainguard Containers, including CI pipelines.
2. If you mirror images, switch to a tool that copies referrers, such as `oras cp -r`, and confirm with `oras discover` that the signatures arrived.
3. If you use policy-controller or Kyverno, apply the configuration described on their pages while images are still dual published, so the change is tested before the cutover.
4. Fix any script that parses `cosign download attestation` output.

## Learn more

- [Verifying Chainguard Containers and metadata signatures with Cosign](/chainguard/containers/security-and-compliance/verifying-chainguard-images-and-metadata-signatures-with-cosign/)
- [How to retrieve attestations and SBOMs for Chainguard Containers](/chainguard/containers/security-and-compliance/retrieve-image-sboms/)
- [Verifying signatures in air-gapped environments](/open-source/sigstore/cosign/verifying-in-air-gapped-environments/)
- [Sigstore bundle specification](https://docs.sigstore.dev/about/bundle/) and [Rekor v2](https://blog.sigstore.dev/rekor-v2-ga/)
