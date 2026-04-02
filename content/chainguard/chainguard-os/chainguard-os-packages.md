---
title : "Chainguard OS Packages"
lead: ""
description: "Chainguard OS Packages"
type: "article"
date: 2026-04-01T00:48:23+00:00
lastmod: 2026-04-01T00:48:23+00:00
draft: false
weight: 020
---

Chainguard OS Packages is an opt-in beta feature that expands the packages available to your [private APK repository](/chainguard/chainguard-images/features/packages/private-apk-repos/) by giving you access to the full set of 30,000 enterprise-grade, zero-CVE packages built as part of Chainguard OS and Wolfi. It also includes a small set of Chainguard base images, for example, `chainguard-base`.

Chainguard OS Packages is designed for larger customers who already build their own images from packages using tools like Bazel, Dockerfiles, and rules\_apko, and want to use a wider set of packages from Chainguard. Because you are creating custom builds, you are responsible for the image builds, the build tooling, validation, and compatibility. You still benefit from the fact that Chainguard builds the packages in the Chainguard Factory with complete SBOMs and our standard enterprise-grade, zero-CVE process.

If you're interested and are a current customer, reach out to your account team to be added to the beta.

If you need to achieve FIPS compliance, the FIPS variant of Chainguard OS Packages includes access packages with the latest versions of Chainguard’s [FIPS-validated modules](https://www.chainguard.dev/legal/fips-commitment).

Chainguard OS Packages is not compatible with [Chainguard Custom Assembly](/chainguard/chainguard-images/features/ca-docs/custom-assembly/).