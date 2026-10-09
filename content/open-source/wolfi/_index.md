---
title: "Wolfi"
description: "Linux undistro to support secure container images"
type: "article"
date: 2022-09-05T08:49:15+00:00
lastmod: 2026-10-08T13:25:53+00:00
draft: false
images: []
---

Wolfi is a Linux _undistro_ built for containers. It uses the apk package format, builds every package from source, and relies on the container runtime to provide the kernel. Chainguard's container images are built on Wolfi.

To learn what Wolfi is and why Chainguard built it, read [What is Wolfi?](https://www.chainguard.dev/supply-chain-security-101/wolfi-overview) in Supply Chain Security 101. The pages in this section show you how to work with Wolfi.

## Try Wolfi

To explore Wolfi, run the [wolfi-base](https://images.chainguard.dev/directory/image/wolfi-base/overview) image. It's intentionally minimal: it contains the Wolfi filesystem, the apk package manager, and a shell.

```sh
docker run -it cgr.dev/chainguard/wolfi-base
```

Inside the container, install the tools you need with apk, for example `apk add curl`.

## Find Wolfi packages

To search for packages, run `apk search` inside a Wolfi container, as described in [Searching for packages](/chainguard/containers/migration/migrating-to-chainguard-images/#searching-for-packages). To search the Wolfi repositories from a browser, use [APK Explorer](https://apk.dag.dev/).

You can't mix Alpine packages with Wolfi packages. If you need a package that's only available for Alpine, open an issue in the [wolfi-os](https://github.com/chainguard-dev/wolfi-os/) repository to request it, or [build your own package with melange](/open-source/wolfi/building-a-wolfi-package/).

## Report security issues

To report a security issue in Wolfi or consume its security data, follow [SECURITY.md](https://github.com/wolfi-dev/.github/blob/main/SECURITY.md).
