---
title: "Verifying signatures in air-gapped environments"
linktitle: "Verify in air-gapped environments"
type: "article"
description: "Use Cosign to verify container signatures and attestations without outbound network access"
lead: "Cosign can verify signatures and attestations with no connection to the public Sigstore infrastructure"
date: 2026-09-08T00:00:00+00:00
lastmod: 2026-09-09T19:52:03+00:00
draft: false
tags: ["Cosign", "Procedural"]
images: []
menu:
  docs:
    parent: "cosign"
weight: 010
toc: true
---

Cosign verifies keyless signatures against the public Sigstore infrastructure, which an air-gapped environment can't reach. You can still verify signatures and attestations there. You need to carry two things across the air gap ahead of time: the Sigstore trust root, and the signatures themselves.

This guide uses Chainguard Containers as the example artifact, but the technique applies to any container image signed with Cosign.

## What Cosign needs from the network

A keyless verification normally makes three kinds of network request. Only the first blocks you in a disconnected environment:

- **The Sigstore trust root**, fetched over [The Update Framework](https://theupdateframework.io/) (TUF) from `tuf-repo-cdn.sigstore.dev`. Cosign refreshes this metadata on every verification, so an air-gapped run fails unless you supply the trust root from a file.
- **The registry**, to fetch the image and its signature. Inside the air gap, this is your internal registry or a directory on disk.
- **The Rekor transparency log**, to confirm the signature was logged. Cosign doesn't need this. A Chainguard signature carries its own transparency log entry and a signed timestamp, which Cosign checks offline.

The last point matters: you keep transparency-log verification in an air-gapped environment. You don't need `--insecure-ignore-tlog`, and you shouldn't use it, because it discards a check that still works.

## Prerequisites

- [Cosign](/open-source/sigstore/cosign/how-to-install-cosign/) v3.1.1 or later, installed on both a connected machine and inside the air-gapped environment. Chainguard Containers require 3.1.1 to verify [Sigstore bundle signatures](/chainguard/containers/security-and-compliance/migrating-to-sigstore-bundles/), and v3.0.3 fixed several problems with offline verification. Earlier releases need different flags, so upgrade rather than work around them.
- [ORAS](https://oras.land/docs/installation) 1.2 or later on the connected machine, to copy images together with their signatures.
- A connected machine that can reach `cgr.dev` and the public Sigstore infrastructure.
- An approved way to move files into the air-gapped environment.

## Export the Sigstore trust root

Run this on the connected machine. `cosign initialize` downloads the current TUF metadata and writes it to a local cache:

```sh
cosign initialize
```

Copy the trust root out of that cache:

```sh
cp ~/.sigstore/root/tuf-repo-cdn.sigstore.dev/targets/trusted_root.json .
```

The file is about 7 KB. It holds the Fulcio certificate authorities, the Rekor transparency log keys, the certificate transparency log keys, and the timestamp authority certificates that Cosign checks a signature against.

{{< note >}}
Copying the whole `~/.sigstore` directory into the air-gapped environment doesn't work. Cosign refreshes its TUF metadata over the network on every verification, so a copied cache still fails. Pass the trust root as a file with `--trusted-root` instead.
{{< /note >}}

## Move the images and their signatures

A Cosign signature is a separate artifact in the registry. Chainguard publishes signatures and attestations as Sigstore bundles attached to the image as OCI referrers, and, during the migration to that format, also under legacy tags derived from the image digest. Copying an image alone leaves both behind, and verification inside the air gap then fails with `no signatures found`.

To see what's attached to an image, run `cosign tree` on the connected machine:

```sh
cosign tree cgr.dev/chainguard/go:latest
```

The output lists the bundles attached to the image as OCI referrers, one per signature or attestation type. Images that still carry the legacy layout also show `Signatures for an image tag` and `Attestations for an image tag` entries:

```
📦 Supply Chain Security Related artifacts for an image: cgr.dev/chainguard/go:latest
└── 🔗 https://sigstore.dev/cosign/sign/v1 artifacts via OCI referrer: cgr.dev/chainguard/go@sha256:a06a9b6d...
   └── 🍒 sha256:14cf554baff036e5e1f75ef35cc988a099566268723b3fb934d5e482c08ebae9
└── 🔗 https://spdx.dev/Document artifacts via OCI referrer: cgr.dev/chainguard/go@sha256:f1fc7521...
   └── 🍒 sha256:f23ccc2edc59eac11ce753fc590a45cde72ea1d8fe63fb287f681ab0fe868ea0
└── 🔗 https://slsa.dev/provenance/v1 artifacts via OCI referrer: cgr.dev/chainguard/go@sha256:bf5cb292...
   └── 🍒 sha256:c6f25e5fbef68e24daefc36dc563e4b8cdc4e05bbb309be65975a23c1339da5f
```

Choose one of the following two transports.

### Option 1: Copy into a mirrored registry

Use `oras cp -r`, which carries the image, its signatures, and its attestations together. For a multi-architecture image it also copies the referrers attached to each per-platform manifest, which matters if the air-gapped environment pulls a single architecture:

```sh
oras cp -r cgr.dev/chainguard/go:latest registry.internal/chainguard/go:latest
```

Confirm the signature arrived before you rely on the mirror:

```sh
cosign tree registry.internal/chainguard/go:latest
```

{{< note >}}
Tools that copy an image by tag do not carry its Sigstore bundles. `crane copy` and `skopeo copy` copy the image alone, `cosign copy` is deprecated in Cosign 3.x and copies only the legacy tags reliably, and `cosign save`/`cosign load` do not carry bundle referrers. See [Mirroring Chainguard Containers with their signatures](/chainguard/containers/registry/mirroring-signed-images/) for the tested comparison.
{{< /note >}}

### Option 2: Save to a directory

If the air-gapped environment has no registry on the connected side, write the image and its referrers to an OCI layout on disk with ORAS:

```sh
oras cp -r cgr.dev/chainguard/go:latest --to-oci-layout ./transfer:go
```

Move the `transfer` directory and `trusted_root.json` across the air gap together. On the other side, load the layout into your internal registry and verify it there:

```sh
oras cp -r --from-oci-layout ./transfer:go registry.internal/chainguard/go:latest
```

## Verify inside the air-gapped environment

Pass the trust root with `--trusted-root`. Everything else matches a connected verification.

### Verify a mirrored image

```sh
cosign verify \
  --trusted-root ./trusted_root.json \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  registry.internal/chainguard/go:latest
```

A successful run reports the offline transparency-log check:

```
Verification for registry.internal/chainguard/go:latest --
The following checks were performed on each of these signatures:
  - The cosign claims were validated
  - Existence of the claims in the transparency log was verified offline
  - The code-signing certificate was verified using trusted certificate authority certificates
```

{{< note >}}
The verified output still reports a `docker-reference` of `cgr.dev/chainguard/go`, even though you verified a mirrored copy. This is expected. The signature covers the image digest, not the registry it's served from.
{{< /note >}}

### Verify a loaded layout

After loading a layout into the internal registry with `oras cp -r --from-oci-layout`, verify it exactly as a mirrored image. Cosign cannot verify an ORAS layout directory in place: `--local-image` expects a single image or index at the root of the layout, and an ORAS layout also holds the referrer manifests.

### Verify attestations

`cosign verify-attestation` works the same way. This example checks the SPDX SBOM attestation:

```sh
cosign verify-attestation \
  --trusted-root ./trusted_root.json \
  --type https://spdx.dev/Document \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  --certificate-identity=https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  registry.internal/chainguard/go:latest
```

### Verify images from a private registry

Images in your organization's registry are signed by your organization's `image-syncer` and `custom-image-builder` identities rather than by Chainguard's public signing identity. Resolve those identifiers on the connected machine, because `chainctl` needs to reach the Chainguard control plane:

```sh
PARENT=your-organization
IMAGE_SYNCER=$(chainctl iam account-associations describe $PARENT -o json | jq -r '.[].chainguard.service_bindings.CATALOG_SYNCER')
CUSTOM_IMAGE_BUILDER=$(chainctl iam account-associations describe $PARENT -o json | jq -r '.[].chainguard.service_bindings.APKO_BUILDER')
```

Record both values and carry them across the air gap with the trust root. Verification then uses them in place of the public identity:

```sh
cosign verify \
  --trusted-root ./trusted_root.json \
  --certificate-oidc-issuer=https://issuer.enforce.dev \
  --certificate-identity-regexp="https://issuer.enforce.dev/(${IMAGE_SYNCER}|${CUSTOM_IMAGE_BUILDER})" \
  registry.internal/chainguard/go:latest
```

For more on these identities, see [Verifying Chainguard Containers and metadata signatures with Cosign](/chainguard/containers/how-to-use/verifying-chainguard-images-and-metadata-signatures-with-cosign/).

### Signatures in a separate repository

Some registry layouts keep legacy `.sig` and `.att` tags apart from the images they sign, and `COSIGN_REPOSITORY` tells Cosign where to find them. That setting applies to the legacy layout only. Sigstore bundles are referrers of the image and must live in the image's own repository, so keep the referrers with the image when you mirror.

## Refresh the trust root

Sigstore rotates the keys and certificate authorities in the trust root from time to time. A trust root you exported months ago can fail to verify a signature made after a rotation.

Re-export `trusted_root.json` from a connected machine on the same schedule you use to refresh images, and move the two together. Treat the trust root as part of every transfer rather than as one-time setup.

## Re-signing with your own key

Some organizations verify Chainguard signatures on the connected side, then re-sign the images with an internally managed key before import. Inside the air gap, admission policies check only that internal key.

That's a decision about trust domains and key custody, not a technical requirement. The verification described earlier works with no outbound connectivity, so you can also keep verifying Chainguard's signatures directly. If you do re-sign, see [How to sign a container with Cosign](/open-source/sigstore/cosign/how-to-sign-a-container-with-cosign/).

## Troubleshooting

| Message | Cause |
|---------|-------|
| `tuf: failed to download 13.root.json` | Cosign tried to refresh TUF metadata over the network. Pass `--trusted-root`. |
| `no signatures found` | The signature wasn't copied with the image, usually because it was copied by tag with `crane copy`, `skopeo copy`, or a registry replication feature that ignores referrers. Check with `cosign tree` and re-copy with `oras cp -r`. |
| `none of the expected identities matched what was in the certificate` | The `--certificate-identity` or `--certificate-oidc-issuer` value doesn't match the signer. The error lists the subject that was found. |
| `Flag --offline has been deprecated` | Remove `--offline`. Supplying `--trusted-root` covers this case. |
| `if any flags in the group [local-image new-bundle-format] are set none of the others can be` | Remove `--new-bundle-format`. Older guides pair it with `--local-image`, which Cosign v3.0.3 rejects. |

## Learn more

For background on how Cosign verification works, read [An introduction to Cosign](/open-source/sigstore/cosign/an-introduction-to-cosign/). To verify Chainguard Containers in a connected environment, see [Verifying Chainguard Containers and metadata signatures with Cosign](/chainguard/containers/how-to-use/verifying-chainguard-images-and-metadata-signatures-with-cosign/). For mirroring Chainguard Containers into an internal registry, see [Mirroring Chainguard Containers with their signatures](/chainguard/containers/registry/mirroring-signed-images/) and the [pull-through guides](/chainguard/containers/chainguard-registry/pull-through-guides/).
