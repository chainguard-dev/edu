---
aliases:
- /chainguard/migration/image-matcher/find-match/
title: "Find a Matching Chainguard Image Using the API"
linktitle: "Find a Matching Image"
description: "How to call the Chainguard Image Matcher API with an existing SBOM to find the closest Chainguard image equivalent."
type: "article"
date: 2026-05-26T00:00:00+00:00
weight: 02
draft: false
tags: ["Chainguard Images", "Migration", "SBOM", "API"]
---

This guide walks through calling the [Chainguard Image Matcher API](/chainguard/api/spec-api-v1/#tag/imagematcher) to find the best Chainguard equivalent for an existing container image. It assumes you already have an SBOM for the image you want to migrate.

For background on how the matcher works and how it scores recommendations, see [Image Matcher Overview](/chainguard/migration/image-matcher/overview/).

## Prerequisites

Before getting started, you will need:

- An SBOM for your source image in CycloneDX JSON format, with `purl` values on each component.
    - SBOMs produced by [Syft](https://github.com/anchore/syft), Trivy, `docker sbom`, or cdxgen all work.
- `chainctl` [installed and authenticated](/chainguard/api/authentication/).
- `jq` installed.
- Your Chainguard organization UID.
    - Retrieve it from **Settings > General** in the [Chainguard Console](https://console.chainguard.dev/org/-/settings/general), or run `chainctl iam groups list`.

## Step 1: Reshape your SBOM for the API

The Image Matcher API does not accept a raw CycloneDX document. It expects an `sbomComponents` array containing only distribution packages, with a small number of fields per component.

Save the following as `build-request.jq`:

```jq
{
  parent_id: $org_id,
  dist_name: $dist,
  arch: $arch,
  sbom: {
    sbomComponents: [
      .components[]
      | select(.purl != null and (.purl | startswith($purl_prefix)))
      | {
          type: .type,
          purl: .purl,
          name: .name,
          cpe: .cpe,
          bomref: ."bom-ref",
          version: .version
        }
    ]
  }
}
```

This filter does three things: it selects only distribution packages by PURL prefix, drops irrelevant CycloneDX fields (licenses, properties, publisher, etc.) that the API ignores, and renames `bom-ref` to `bomref` to match the API's expected field name.

Run it with values for your source distribution:

```bash
export ORG_ID="<your-org-uid>"

jq \
  --arg org_id "$ORG_ID" \
  --arg dist   "debian" \
  --arg arch   "x86_64" \
  --arg purl_prefix "pkg:deb/" \
  -f build-request.jq \
  your-image.cdx.json \
  > request.json
```

Use the following table to match `dist`, `arch`, and `purl_prefix` to your source image:

| Distribution      | `dist`         | `purl_prefix` |
|-------------------|----------------|---------------|
| Debian            | `debian`       | `pkg:deb/`    |
| Ubuntu            | `ubuntu`       | `pkg:deb/`    |
| Alpine            | `alpine`       | `pkg:apk/`    |
| Red Hat / RHEL    | `redhat`       | `pkg:rpm/`    |
| SUSE              | `suse`         | `pkg:rpm/`    |
| Amazon Linux      | `amazon-linux` | `pkg:rpm/`    |

Pass `dist_version` as an additional `--arg` if you know the exact version (for example, `12` for Debian 12, `24.04` for Ubuntu 24.04). This is optional, but it narrows the candidate set and improves results.

### Example request body

The reshaped request body for a Debian nginx image looks like the following:

```json
{
  "parent_id": "<your-org-uid>",
  "dist_name": "debian",
  "arch": "x86_64",
  "sbom": {
    "sbomComponents": [
      {
        "type": "library",
        "purl": "pkg:deb/debian/nginx@1.28.0-1~bookworm?arch=amd64&distro=debian-12",
        "name": "nginx",
        "cpe": "cpe:2.3:a:nginx:nginx:1.28.0-1~bookworm:*:*:*:*:*:*:*",
        "bomref": "pkg:deb/debian/nginx@1.28.0-1~bookworm?arch=amd64&distro=debian-12&package-id=...",
        "version": "1.28.0-1~bookworm"
      },
      {
        "type": "library",
        "purl": "pkg:deb/debian/libssl3@3.0.17-1~deb12u3?arch=amd64&distro=debian-12&upstream=openssl",
        "name": "libssl3",
        "cpe": "cpe:2.3:a:libssl3:libssl3:3.0.17-1~deb12u3:*:*:*:*:*:*:*",
        "bomref": "pkg:deb/debian/libssl3@3.0.17-1~deb12u3?arch=amd64&distro=debian-12&package-id=...",
        "version": "3.0.17-1~deb12u3"
      }
    ]
  }
}
```

## Step 2: Call the API

Run the following:

```bash
curl -sS \
  -H "Authorization: Bearer $(chainctl auth token)" \
  -H "Content-Type: application/json" \
  -X POST "https://console-api.enforce.dev/image-recommendation/v1/match" \
  -d @request.json
```

## Step 3: Interpret the results

The response contains a ranked `images` array, ordered from highest to lowest `probabilityScore`. For example:

```json
{
  "images": [
    {
      "imageRef": "cgr.dev/<your-org>/nginx:latest",
      "probabilityScore": 98.57,
      "satisfiedCount": 6,
      "totalRequired": 86,
      "coverage": 0.07,
      "satisfiedPackages": [...],
      "missingPackages": [...],
      "extraPackages": 14
    }
  ],
  "totalExternalPackages": 143,
  "requiredApks": ["nginx-mainline", "libgcc", "glibc", ...],
  "unmatchedExternalPkgs": ["adduser", "apt", "base-files", ...]
}
```

Key fields to check:

- **`probabilityScore`**: the matcher's confidence estimate (0–100). A score of 90 or above is a strong match. Scores in the 50–70 range warrant human review.
- **`imageRef`**: the full OCI reference for the recommended image. Use the final path segment and tag (for example, `nginx:latest`) when displaying this to users or comparing against the [Chainguard image catalog](https://images.chainguard.dev/). Keep the full reference if you intend to pull the image.
- **`missingPackages`**: packages from your SBOM that are not present in the recommended image. Some missing packages are expected: Chainguard images are intentionally minimal. Review this list to identify any packages your application requires at runtime.
- **`unmatchedExternalPkgs`**: source packages the matcher could not map to any Chainguard APK. A long list is normal for general-purpose distributions like Debian, where many entries are build-time tools or base-image scaffolding.

### Low `coverage` with a high `probabilityScore`

You may notice that `coverage` (the fraction of required APKs present in the image) can be low even when `probabilityScore` is high. This is expected behavior. Package weights are not uniform: the package that defines an image's purpose carries a weight orders of magnitude larger than common shared dependencies. A `probabilityScore` of 98 with `coverage` of 0.07 means the matcher is highly confident it has found the right image, even though many low-level library names differ between your source distribution and Chainguard's APK catalog.

Learn more about the probability score in the [Image Matcher overview](/chainguard/migration/image-matcher/overview/#understanding-the-probability-score).

### Reviewing multiple candidates

The API returns up to 10 candidates by default. For common stacks the top result is typically correct, but it is good practice to review the second and third results, particularly when:

- The top score is below 90.
- The top two scores are within a few points of each other.
- The source image is not a well-known public image.

To request more or fewer candidates, add a `count` field to your request body. To suppress weak matches, add a `threshold` field (default: `50.0`).

