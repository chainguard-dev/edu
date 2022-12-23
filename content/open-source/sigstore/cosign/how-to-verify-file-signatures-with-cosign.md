---
title: "How to Verify File Signatures with Cosign"
type: "article"
description: "Use Cosign to verify non-container software artifacts"
lead: "Cosign can verify software artifacts beyond containers"
date: 2022-12-21T15:22:20+01:00
lastmod: 2022-12-21T15:22:20+01:00
draft: false
images: []
menu:
  docs:
    parent: "cosign"
weight: 005
toc: true
---

Cosign can be used to verify file signatures as these are binary artifacts, as long as these are published to an OCI registry. This tutorial assumes you have Cosign installed, which you can achieve by following our [How to Install Cosign guide](/open-source/sigstore/cosign/how-to-sign-a-container-with-cosign/).

We’ll verify a binary artifact, in this case, a copy of [`apko`](/open-source/apko/overview/), which is a command-line tool for building container images using a declarative language based on YAML. The methods in this tutorial apply to any blob file Cosign has signed with a keyless signature.

### Verifying a binary with Cosign keyless signatures

All apko releases are released with [keyless signatures using Cosign](open-source/sigstore/cosign/an-introduction-to-cosign/#keyless-signing). You can verify the signature for an apko release using the `cosign` tool directly, or by calculating the SHA256 hash of the release and finding the corresponding Rekor transparency log entry.

If you would like to learn how to verify a binary using Rekor or curl, follow the steps in our guide [How to Verify File Signatures with Rekor or curl](/open-source/sigstore/rekor/how-to-verify-file-signatures-with-rekor-or-curl/).

We'll use the `apko_0.6.0_linux_arm64.tar.gz` tar archive from the apko [GitHub Release v0.6.0 page](https://github.com/chainguard-dev/apko/releases/tag/v0.6.0) in this example.

There are three URLs from the list of assets on that page that you will need to copy:

1. The release itself: `https://github.com/chainguard-dev/apko/releases/download/v0.6.0/apko_0.6.0_linux_amd64.tar.gz`
2. The signature file: `https://github.com/chainguard-dev/apko/releases/download/v0.6.0/apko_0.6.0_linux_amd64.tar.gz.sig`
3. The public certificate: `https://github.com/chainguard-dev/apko/releases/download/v0.6.0/apko_0.6.0_linux_amd64.tar.gz.crt`

With these URLs, construct (or copy) the following command to verify the tar archive:

```sh
COSIGN_EXPERIMENTAL=1 cosign verify-blob \
   --signature https://github.com/chainguard-dev/apko/releases/download/v0.6.0/apko_0.6.0_linux_amd64.tar.gz.sig \
   --certificate https://github.com/chainguard-dev/apko/releases/download/v0.6.0/apko_0.6.0_linux_amd64.tar.gz.crt \
   https://github.com/chainguard-dev/apko/releases/download/v0.6.0/apko_0.6.0_linux_amd64.tar.gz
```

Running the command may take a moment, but when it completes you will receive the following output:

```
tlog entry verified with uuid: 9ec23abb6326ebbaa6932f720847080e8f5e0b2925a1643b63962691917c8137 index: 8538988
Verified OK
```

If any of the URLs are incorrect, of if there was a problem with the apko release file, a mismatching signature or certificate, or if the release file was not signed, you will receive an error like the following:

```
Error: verifying blob https://github.com/chainguard-dev/apko/releases/download/v0.6.0/apko_0.6.0_linux_amd64.tar.gz: invalid signature when validating ASN.1 encoded signature
main.go:62: error during command execution: verifying blob https://github.com/chainguard-dev/apko/releases/download/v0.6.0/apko_0.6.0_linux_amd64.tar.gz: invalid signature when validating ASN.1 encoded signature
```

You can also download each or any of the files and verify them locally like this:

```sh
curl -L -O https://github.com/chainguard-dev/apko/releases/download/v0.6.0/apko_0.6.0_linux_amd64.tar.gz \
  -O https://github.com/chainguard-dev/apko/releases/download/v0.6.0/apko_0.6.0_linux_amd64.tar.gz.sig \
  -O https://github.com/chainguard-dev/apko/releases/download/v0.6.0/apko_0.6.0_linux_amd64.tar.gz.crt
```

Then you can verify the files that you downloaded using Cosign:

```sh
COSIGN_EXPERIMENTAL=1 cosign verify-blob \
   --signature apko_0.6.0_linux_amd64.tar.gz.sig \
   --certificate apko_0.6.0_linux_amd64.tar.gz.crt \
   apko_0.6.0_linux_amd64.tar.gz
```

If you receive an error while verifying a binary with Cosign, then you know that there was a problem with creating the artifact, or that the file that you are verifying is corrupted or invalid. If that is the case, you should download a fresh copy and verify it again, or try a different version of the software with a working signature.
