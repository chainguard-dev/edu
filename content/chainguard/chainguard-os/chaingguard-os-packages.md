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

Chainguard OS Packages extends the set of available packages in your private APK repository to include the full 30,000 packages Chainguard has built so far.

- If you are a **catalog** customer, you get the full set of packages available in Chainguard OS.
- If you're a **per-image** customer, you get most of the available packages, but won't have access to the *main* packages for images you aren't entitled to, preventing you from recreating our images.

If you're interested and are a current customer, reach out to your account team to be added to the Beta.

Chainguard OS Packages is designed for larger customers who already build their own images from packages using tools like Bazel, Dockerfiles, and rules\_apko, and want to use a wider set of packages from Chainguard. Because you are creating custom builds, you are responsible for the image builds, the build tooling, validation, and compatibility. You still benefit from the fact that Chainguard builds the packages in the Chainguard Factory with complete SBOMs and our standard enterprise-grade, zero-CVE process.

Chainguard OS Packages are not currently available for use with [Chainguard Custom Assembly](/chainguard/chainguard-images/features/ca-docs/custom-assembly/).