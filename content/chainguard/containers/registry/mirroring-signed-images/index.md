---
title: "Mirroring Chainguard Containers with their signatures"
linktitle: "Mirroring signed containers"
type: "article"
description: "Copy Chainguard Containers into your own registry or across an air gap without losing their Sigstore signatures and attestations"
lead: "Signatures and attestations are separate artifacts. Copy tools that only follow the image tag leave them behind."
date: 2026-09-09T00:00:00+00:00
lastmod: 2026-09-09T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Procedural"]
images: []
toc: true
weight: 045
---

Chainguard publishes each container's signature and attestations (SBOMs, provenance, and build configuration) as [Sigstore bundles](https://docs.sigstore.dev/about/bundle/) attached to the image as OCI referrers. A referrer is a separate manifest in the same repository that points at the image digest. Most image copy tools follow the tag you give them and copy the image alone, so a mirrored image arrives without anything to verify and `cosign verify` reports `no signatures found`.

This guide shows how to copy a Chainguard Container together with its referrers, how to move it across an air gap, and which tools do and do not carry referrers. For the verification commands themselves, see [Verifying Chainguard Containers and metadata signatures with Cosign](/chainguard/containers/security-and-compliance/verifying-chainguard-images-and-metadata-signatures-with-cosign/). For background on the format change, see [Migrating to Sigstore bundle signatures](/chainguard/containers/security-and-compliance/migrating-to-sigstore-bundles/).

## Prerequisites

- [ORAS](https://oras.land/docs/installation) 1.2 or newer. The examples below were run with 1.3.1.
- [Cosign](/open-source/sigstore/cosign/how-to-install-cosign/) 3.1.1 or newer, to confirm the copy.
- Credentials for `cgr.dev` (`chainctl auth configure-docker`) and for your destination registry.

## Copy an image and its referrers between registries

`oras cp` with `-r` (`--recursive`) copies the image, every referrer attached to it, and the referrers attached to each per-platform manifest of a multi-architecture image:

```shell
oras cp -r cgr.dev/chainguard/go:latest registry.internal/chainguard/go:latest
```

Confirm the referrers arrived before relying on the mirror:

```shell
oras discover registry.internal/chainguard/go:latest
```

Then verify the mirrored image the same way you verify the original. The signature covers the image digest, not the registry it is served from, so the identity flags do not change:

```shell
cosign verify \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  registry.internal/chainguard/go:latest
```

Images from your organization's private registry use your `image-syncer` and `custom-image-builder` identities instead; see the [verification guide](/chainguard/containers/security-and-compliance/verifying-chainguard-images-and-metadata-signatures-with-cosign/#chainguards-signing-identities).

## Move an image across an air gap

Write the image and its referrers to an [OCI image layout](https://github.com/opencontainers/image-spec/blob/main/image-layout.md) on disk, move the directory, and push it into the registry on the other side:

```shell
# Connected side
oras cp -r cgr.dev/chainguard/go:latest --to-oci-layout ./transfer:go
tar -czf transfer.tgz transfer

# Air-gapped side
tar -xzf transfer.tgz
oras cp -r --from-oci-layout ./transfer:go registry.internal/chainguard/go:latest
oras discover registry.internal/chainguard/go:latest
```

Verify after loading into the registry. Cosign cannot verify an ORAS layout directory in place (`--local-image` expects a single image or index at the root of the layout), and verifying inside the air gap also needs the Sigstore trust root as a file. See [Verifying signatures in air-gapped environments](/open-source/sigstore/cosign/verifying-in-air-gapped-environments/) for exporting the trust root and passing it with `--trusted-root`.

## Registries without the Referrers API

Referrers are served by the OCI 1.1 Referrers API (`GET /v2/<name>/referrers/<digest>`). If the destination registry does not implement it, ORAS can instead record the referrers under the fallback tag defined by the OCI distribution spec (`sha256-<digest>`), which Cosign and other referrer-aware clients also understand:

```shell
oras cp -r --to-distribution-spec v1.1-referrers-tag \
  cgr.dev/chainguard/go:latest registry.internal/chainguard/go:latest
```

`cgr.dev` itself serves the Referrers API for every repository.

## Tools compared

Tested against a bundle-signed Chainguard Container with the versions shown. "Referrers" means the signature and attestation bundles arrived and `cosign verify` (3.1.3) succeeded on the copy.

| Tool | Version | Referrers | Notes |
|---|---|---|---|
| `oras cp -r` | 1.3.1 | Yes | Recommended. Also handles per-platform referrers and OCI layouts. |
| `crane copy` | 0.20.7 | No | Copies the tag only; `crane` has no referrer option. |
| `skopeo copy` | 1.22.2 | No | Copies the tag only. |
| `cosign copy` | 3.1.3 | Partial | Deprecated in Cosign 3.x. Copies legacy `.sig`/`.att` tags and only some bundles; do not rely on it. |
| `cosign save` / `cosign load` | 3.1.3 | No | Carries legacy tags only; bundle referrers fail to load. Use the OCI layout procedure above. |
| Registry replication features | varies | varies | Check the product's documentation for OCI referrers or "OCI artifact" support, then confirm with `oras discover` through the mirror. |

## Pull-through caches

A pull-through cache proxies requests to `cgr.dev`, so what it serves depends on whether it proxies the Referrers API as well as the manifest and blob endpoints. Check by listing referrers and verifying through the cache:

```shell
oras discover cache.internal/chainguard/go:latest
cosign verify <identity flags> cache.internal/chainguard/go:latest
```

If `oras discover` lists bundles against `cgr.dev` but not through the cache, the cache does not serve referrers. Verify against `cgr.dev` directly, or mirror with `oras cp -r` instead. Product-specific notes are in the [pull-through guides](/chainguard/containers/registry/pull-through-guides/).

## Learn more

- [Verifying Chainguard Containers and metadata signatures with Cosign](/chainguard/containers/security-and-compliance/verifying-chainguard-images-and-metadata-signatures-with-cosign/)
- [Verifying signatures in air-gapped environments](/open-source/sigstore/cosign/verifying-in-air-gapped-environments/)
- [Migrating to Sigstore bundle signatures](/chainguard/containers/security-and-compliance/migrating-to-sigstore-bundles/)
- [ORAS: copying artifacts and referrers](https://oras.land/docs/commands/oras_cp)
