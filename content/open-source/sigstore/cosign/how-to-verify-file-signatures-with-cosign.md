---
title: "How to Verify File Signatures with Cosign"
linktitle: "Verify File Signatures"
aliases:
- /open-source/sigstore/rekor/how-to-verify-file-signatures-with-rekor-or-curl/
type: "article"
description: "Use Cosign to verify non-container software artifacts"
lead: "Cosign can verify software artifacts beyond containers"
date: 2022-12-21T15:22:20+01:00
lastmod: 2024-11-13T15:16:50+01:00
draft: false
tags: ["Cosign", "Procedural"]
images: []
menu:
  docs:
    parent: "cosign"
weight: 006
toc: true
---

Cosign can be used to verify binary artifacts ("blobs") using provided signatures as long as they are published to an OCI registry. In this tutorial, we’ll verify a binary artifact — in this case, a release of [`apko`](/open-source/apko/overview/), a command-line tool for building container images using a declarative language based on YAML. The methods in this tutorial apply to any blob file Cosign has signed with a keyless signature.

This tutorial assumes you [have Cosign installed](/open-source/sigstore/cosign/how-to-install-cosign/).

### Verifying a binary with Cosign keyless signatures

All `apko` releases include [keyless signatures using Cosign](/open-source/sigstore/cosign/an-introduction-to-cosign/#keyless-signing). You can verify the signature for an apko release using the `cosign` tool directly, or by calculating the SHA256 hash of the release and finding the corresponding Rekor transparency log entry.

If you would like to learn how to verify a binary using Rekor or `curl`, follow the steps in our guide on [How to Verify File Signatures with Rekor or curl](/open-source/sigstore/rekor/how-to-verify-file-signatures-with-rekor-or-curl/).

We'll use the `apko_0.19.9_linux_arm64.tar.gz` tar archive from the `apko` [GitHub Release v0.19.9 page](https://github.com/chainguard-dev/apko/releases/tag/v0.19.9) in this example.

There are three URLs from the list of assets on that page that you will need to copy:

1. The release itself: `https://github.com/chainguard-dev/apko/releases/download/v0.19.9/apko_0.19.9_linux_arm64.tar.gz`
2. The signature file: `https://github.com/chainguard-dev/apko/releases/download/v0.19.9/apko_0.19.9_linux_arm64.tar.gz.sig`
3. The public certificate: `https://github.com/chainguard-dev/apko/releases/download/v0.19.9/apko_0.19.9_linux_arm64.tar.gz.crt`

With these URLs, construct (or copy) the following command to verify the tar archive:

```sh
cosign verify-blob \
  --signature https://github.com/chainguard-dev/apko/releases/download/v0.19.9/apko_0.19.9_linux_arm64.tar.gz.sig \
  --certificate https://github.com/chainguard-dev/apko/releases/download/v0.19.9/apko_0.19.9_linux_arm64.tar.gz.crt \
  --certificate-oidc-issuer "https://token.actions.githubusercontent.com" \
  --certificate-identity "https://github.com/chainguard-dev/apko/.github/workflows/release.yaml@refs/tags/v0.19.9" \
  https://github.com/chainguard-dev/apko/releases/download/v0.19.9/apko_0.19.9_linux_arm64.tar.gz
```

Running the command may take a moment, but when it completes you will receive the following output:

```
Verified OK
```

If any of the URLs are incorrect, if there was a problem with the `apko` release file, if the signature or certificate identity don't match, or if the release file was not signed, you will receive an error like the following:

```
Error: searching log query: [POST /api/v1/log/entries/retrieve][400] searchLogQueryBadRequest  &{Code:400 Message:verifying signature: invalid signature when validating ASN.1 encoded signature}
main.go:74: error during command execution: searching log query: [POST /api/v1/log/entries/retrieve][400] searchLogQueryBadRequest  &{Code:400 Message:verifying signature: invalid signature when validating ASN.1 encoded signature}
```

You can also download the files and verify them locally:

```sh
curl -L -O https://github.com/chainguard-dev/apko/releases/download/v0.19.9/apko_0.19.9_linux_arm64.tar.gz \
  -O https://github.com/chainguard-dev/apko/releases/download/v0.19.9/apko_0.19.9_linux_arm64.tar.gz.sig \
  -O https://github.com/chainguard-dev/apko/releases/download/v0.19.9/apko_0.19.9_linux_arm64.tar.gz.crt
```

You can then verify the files that you downloaded using Cosign:

```sh
cosign verify-blob \
   --signature apko_0.19.9_linux_arm64.tar.gz.sig \
   --certificate apko_0.19.9_linux_arm64.tar.gz.crt \
   --certificate-oidc-issuer "https://token.actions.githubusercontent.com" \
   --certificate-identity "https://github.com/chainguard-dev/apko/.github/workflows/release.yaml@refs/tags/v0.19.9" \
   apko_0.19.9_linux_arm64.tar.gz
```

If you receive an error while verifying a binary with Cosign, then you know that there was a problem with creating the artifact, or that the file that you are verifying is corrupted or invalid. If that is the case, you should download a fresh copy and verify it again, or try a different version of the software with a working signature.
