---
title: "Image Matcher Overview"
linktitle: "Image Matcher Overview"
description: "Learn how the Chainguard Image Matcher uses SBOMs to recommend the closest Chainguard image equivalent for your existing container images."
type: "article"
date: 2026-05-26T00:00:00+00:00
draft: false
tags: ["Chainguard Images", "Migration", "SBOM", "API"]
---

The [Chainguard Image Matcher](/chainguard/api/spec-api-v1/#tag/imagematcher) is an API-based tool that analyzes the software bill of materials (SBOM) of an existing container image and returns a ranked list of Chainguard images that most closely match it. It is designed to support migration workflows where you know what you are running today and want to find the best Chainguard equivalent.
 
## How it works
 
You supply an SBOM for your current image, along with the source Linux distribution. The Image Matcher maps the packages in your SBOM to Chainguard APK packages, scores each candidate Chainguard image based on how well its contents cover your requirements, and returns a ranked list of recommendations with confidence scores.
 
The matcher is deterministic: the same SBOM submitted to the same API will always produce the same results. There is no machine learning model involved. Results may change slightly over time as Chainguard improves its mapping data and publishes new images, but there is no per-request variation.
 
### What the matcher returns
 
Each recommendation includes:
 
- The recommended Chainguard image reference
- A probability score (0–100) indicating how closely the image matches your SBOM
- The packages from your SBOM that are satisfied by the recommended image
- The packages that would be missing if you migrated to that image
- Any extra packages present in the image that your SBOM did not request

The number of candidates returned by the API is configurable, and the results are ranked by score. For well-known stacks such as `nginx`, `postgres`, or `redis`, the top result is typically the right choice. For less common images, the results may warrant human review.
 
## Understanding the probability score
 
The probability score is the matcher's confidence estimate, normalized to a 0–100 scale. It is calculated from three weighted components:
 
- **Satisfied score**: the sum of weights of SBOM packages present in the candidate image. This is the dominant factor.
- **Missing score**: the sum of weights of SBOM packages absent from the candidate image. This is weighted lightly. Chainguard images are intentionally minimal, so some missing packages are expected and do not significantly penalize the score.
- **Extra score**: the sum of weights of packages in the candidate image that your SBOM did not request. This carries a moderate penalty.

The combined raw score is passed through a sigmoid-like transform and clamped to 0–100.
 
A score of 90 or above is a strong match. Scores in the 50–70 range warrant human review. The score is capped at 100, so multiple candidates may report the same top score while differing in their underlying ranking — use the `overallScore` field to differentiate them when needed.
 
Package weights are not uniform. The package that defines an image's primary purpose (for example, `postgres` in the `postgres` image) carries a weight orders of magnitude larger than common shared dependencies like `openssl` or `ca-certificates`. This is why the matcher reliably identifies the right base image even when many low-level library names differ between distributions.
 
## How packages are mapped across distributions
 
Linux distributions use different names for packages that provide the same upstream software. The matcher translates source package names from your SBOM into Chainguard APK names before scoring. This translation is where most of the recommendation logic is concentrated.
 
The following table shows representative examples of how the same upstream software appears across distributions and in the Chainguard catalog:
 
| Upstream project   | Debian / Ubuntu              | Alpine               | Red Hat / Amazon Linux | Chainguard APK(s)                |
|--------------------|------------------------------|----------------------|------------------------|----------------------------------|
| GNU C Library      | `libc6`, `libc-bin`          | (musl libc instead)  | `glibc`                | `glibc`                          |
| OpenSSL library    | `libssl3`                    | `libssl3`            | `openssl-libs`         | `libssl3`, `libcrypto3`          |
| Apache HTTP Server | `apache2`                    | `apache2`            | `httpd`                | `httpd`                          |
| nginx web server   | `nginx`                      | `nginx`              | `nginx`                | `nginx-mainline`, `nginx-stable` |
| PostgreSQL server  | `postgresql-16`, `postgresql-17` | `postgresql16`   | `postgresql-server`    | `postgresql-16`, `postgresql-17` |
| curl HTTP client   | `curl` + `libcurl4`          | `curl` + `libcurl`   | `curl` + `libcurl`     | `curl`                           |
 
Two patterns are common:
 
- **Many source packages map to one Chainguard APK.** Debian splits the GNU C Library into `libc6`, `libc-bin`, and other sub-packages, while Chainguard ships the same software under the single name `glibc`. An SBOM listing `libc6` is translated to `glibc` before any image is scored.
- **One source package maps to multiple Chainguard APKs.** Some upstream packages correspond to more than one Chainguard APK because Chainguard publishes multiple variants. A reference to `nginx` fans out to both `nginx-mainline` and `nginx-stable`; a reference to `postgresql` fans out to `postgresql-16`, `postgresql-17`, and so on.
### Mapping sources
 
The matcher builds its package map from three sources, applied in priority order:
 
1. **Curated equivalences.** Hand-maintained rules for cases where automatic matching would be ambiguous or incorrect, such as the `apache2` → `httpd` rename and version-specific PostgreSQL fan-out.
2. **CPE and PURL matching.** Each Chainguard APK carries CPE and PURL identifiers from its `melange` build definition. When a source package's identifiers overlap with a Chainguard APK's, the matcher treats them as equivalent. This handles the long tail of common dependencies without per-package curation.
3. **Runtime module overlap.** For packages whose value is a bundled language ecosystem (Go modules, Python packages, Node modules), the matcher can detect shared underlying modules and treat packages as equivalent even when their distro-level names differ.
Source packages that cannot be mapped appear in the `unmatchedExternalPkgs` field of the response. A long list of unmatched packages is normal for general-purpose distributions like Debian: most entries are build-time tools, base-image scaffolding, or documentation packages that Chainguard's minimal images do not include.
 
## Limitations
 
- **Distribution must be specified.** The matcher works against a per-distribution package universe. You must supply `dist_name` with each request. Providing `dist_version` and `arch` is optional but improves results.
- **Results depend on SBOM quality.** The matcher maps packages primarily via `purl` and `cpe` fields. SBOMs that lack these fields on components will produce weaker results.
- **Chainguard images are intentionally minimal.** Expect missing packages in recommendations. This is by design: Chainguard images ship fewer packages than upstream equivalents in order to reduce attack surface.
- **The image catalog is refreshed daily.** Newly published Chainguard images typically appear in recommendations within one to two days of release.
- **The score is an estimate, not a guarantee.** A high probability score means the matcher is confident, not that the migration will be drop-in compatible. Always validate the recommended image in your environment before replacing production images.
