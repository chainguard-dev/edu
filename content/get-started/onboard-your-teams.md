---
title: "Onboard your teams"
linktitle: "Onboard your teams"
lead: "Your organization has adopted Chainguard. This guide helps administrators and software engineers understand what your teams can pull from Chainguard Containers and Chainguard Libraries, how that depends on your subscription, and how to retrieve the SBOMs and provenance that ship with every image and package."
description: "Onboard your teams to Chainguard Containers and Chainguard Libraries: what your organization can pull, how subscriptions differ, and how to retrieve SBOMs and provenance."
type: "article"
date: 2026-08-26T00:00:00+00:00
lastmod: 2026-09-02T13:31:42+00:00
draft: false
tags: ["Getting Started"]
images: []
weight: 010
toc: true
---

Your organization has adopted Chainguard, and now you need to bring your teams on board. This guide explains what your teams can pull from Chainguard Containers and Chainguard Libraries, why that depends on your subscription, and how to retrieve the SBOMs and provenance that ship with every image and package.

It's written for two readers:

- **Platform and security administrators** who manage Chainguard for the organization and need to explain it to the teams they support. Early on, you may be the only people with [Chainguard Console](/platform/console/) access, so your teams rely on you to communicate how this works.
- **Software engineers** who were pointed here and want to know how to find and pull the resources they're cleared to use.

To decide where to start, identify which Chainguard products your organization uses; many use both. Read [Chainguard Containers](#chainguard-containers) if your teams pull container images, or [Chainguard Libraries](#chainguard-libraries) if they pull language dependencies for Java, Python, or JavaScript. Your administrators know which subscriptions apply.

## Chainguard Containers

### What you can browse compared to what you can pull

There are two different surfaces, and it helps to keep them separate.

The **Chainguard Containers Directory** at [images.chainguard.dev](https://images.chainguard.dev) is public. Anyone can browse the entire catalog there, inspect tags and metadata, and view the SBOM and provenance for each image. Browsing the Directory does not mean your organization can pull every image it lists.

Your **organization's registry** is what your teams pull from, and it holds only the images your organization has access to. Authenticated production images live under your organization's namespace:

```shell
cgr.dev/$ORGANIZATION/$IMAGE:$TAG
```

For example, an organization registered as `example.com` pulls its Python image from `cgr.dev/example.com/python`. Public Starter images remain available to everyone under `cgr.dev/chainguard/`. See the [registry overview](/chainguard/containers/registry/overview/) for the access tiers and [authentication](/chainguard/containers/registry/authenticating/) to set up your credentials.

Your organization may also front the registry with a pull-through cache, such as Artifactory. In that case, the concepts here still hold, but you pull from your cache's address instead of `cgr.dev` directly. Ask your administrators for the path.

### What your organization can pull

Whether an image is available to pull depends on your subscription. If a pull fails for an image you can see in the Directory, it most likely hasn't been added to your organization yet. To work through the possible causes, including a missing version rather than a missing image, see [Troubleshoot container and version availability](/chainguard/containers/troubleshooting/container-version-troubleshooting/).

**Catalog customers.** A Catalog subscription covers the full Chainguard catalog. Even so, only a subset of images is loaded into your organization's registry at any given time, and administrators add more as teams need them. To use an image that isn't there yet, find it in the [Chainguard Containers Directory](https://images.chainguard.dev) and ask an administrator to add it. If you have the `owner` role, you can add it yourself from the Console; refer to [Catalog pricing](/chainguard/containers/reference/pricing/) for the steps and the roles required.

**Per-image customers.** A per-image subscription covers a specific, licensed set of images rather than the whole catalog. You can browse everything in the Directory, but only your licensed images are permitted for builds, deployments, and production workloads. To add an image that isn't in your set, ask your administrators to start a request; once they approve it, they add the image to your organization's registry.

### Access SBOMs and provenance

Every Chainguard container image ships with a signed SBOM and provenance attestations. You can retrieve them three ways; the [full guide](/chainguard/containers/security-and-compliance/retrieve-image-sboms/) covers each in detail.

- **From the Chainguard Containers Directory.** Open an image at [images.chainguard.dev](https://images.chainguard.dev), then download the SBOM from the **SBOM** tab in SPDX or CycloneDX format. This needs no tooling and works for any image in the catalog.
- **With `cosign`.** Download the SBOM attestation for an image directly from the registry:

  ```shell
  cosign download attestation \
    --platform linux/amd64 \
    --predicate-type https://spdx.dev/Document \
    cgr.dev/$ORGANIZATION/$IMAGE | jq -r '.payload' | base64 -d | jq -r '.predicate'
  ```

- **With `syft`.** Generate an SBOM locally from an image you've pulled. Use this for images you've customized, where you want an SBOM of the final artifact.

To pin what you pull so builds stay reproducible, reference images by digest. See [container image digests](/chainguard/containers/troubleshooting/container-image-digests/).

## Chainguard Libraries

Chainguard Libraries is a secure catalog of language dependencies for Java, Python, and JavaScript. Each package goes through multiple layers of defense, including malicious behavior scanning, building from source, and configurable policies. A package pulled from Chainguard is a drop-in replacement for the one you'd normally pull from Maven Central, PyPI, or npm. See the [overview](/chainguard/libraries/introduction/overview/) for how they're built and what guarantees they carry.

### What your organization can access

Libraries don't have a public browse site like the Chainguard Containers Directory. Instead, you browse the packages your organization is entitled to by signing in to the [Chainguard Console](/chainguard/libraries/introduction/browse/). Access is granted per language: your organization is entitled to Java, Python, or JavaScript individually, so which ecosystems you can pull depends on your subscription. There's no catalog-versus-per-image distinction as there is for containers.

### Pull libraries into your project

You consume Chainguard Libraries by pointing your package manager at your organization's Chainguard repository and authenticating with a pull token. Each ecosystem has its own endpoint under `libraries.cgr.dev`:

```shell
https://libraries.cgr.dev/java/
https://libraries.cgr.dev/python/
https://libraries.cgr.dev/javascript/
```

The [quickstart](/chainguard/libraries/introduction/quickstart/) walks through creating a pull token and configuring your build tools, and [access and authentication](/chainguard/libraries/introduction/access/) covers the details.

### Verify provenance and SBOMs

Every package that Chainguard builds from source ships with a signed SBOM and SLSA provenance, attached alongside each package. Use a command similar to the following to verify which of your dependencies were built by Chainguard:

```shell
chainctl libraries verify /path/to/artifact
```

See [verifying Chainguard Libraries](/chainguard/libraries/policies-and-security/verification/) for what the command checks and for retrieving the SBOM and attestation files directly.

## Other products your company may have adopted

Chainguard's platform reaches beyond containers and libraries. Your organization may also use one or more of these:

- **[Chainguard Agent Skills](/chainguard/agent-skills/overview/)** — hardened AI agent skills that Chainguard reviews, scopes, and publishes with a full audit trail, so your teams can install them without inheriting unknown risk.
- **[Chainguard Actions](/chainguard/actions/overview/)** — hardened, drop-in replacements for popular GitHub Actions that protect your CI/CD pipelines from supply chain attacks.
- **[Chainguard Guardener](/chainguard/guardener/)** — a tool for managing and hardening your source code through a suite of capabilities you opt into independently.

## Next steps

- New to the platform? Start with [What is Chainguard?](/get-started/what-is-chainguard/).
- Ready to pull your first container image? Work through a [language- or service-specific example](/get-started/containers-examples/).
- Adopting Chainguard Libraries? Follow the [libraries on-ramp](/get-started/libraries-examples/).
- Managing resources from the command line? See [Get started with chainctl](/get-started/getting-started-with-chainctl/).
