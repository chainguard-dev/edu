---
title: "Migration"
linktitle: "Migration"
lead: ""
description: "Move existing workloads to Chainguard: container migration guides, library migration guides for Java, Python, and JavaScript, and tooling that automates the conversion."
type: "article"
date: 2024-02-26T08:48:45+00:00
lastmod: 2026-08-11T00:00:00+00:00
draft: false
images: []
weight: 045
crosslinks:
- title: "Containers overview"
  url: "/chainguard/containers/migration/migrations-overview/"
- title: "Containers guides"
  url: "/chainguard/containers/migration/migration-guides/"
- title: "Libraries: Java"
  url: "/chainguard/libraries/java/migration/"
- title: "Libraries: JavaScript"
  url: "/chainguard/libraries/javascript/migration/"
- title: "Libraries: Python"
  url: "/chainguard/libraries/python/migration/"
- title: "API: v1 to v2"
  url: "/platform/api/api-v2-migration/"
- title: "Chainguard Guardener"
  url: "/chainguard/guardener/"
---

Already using Chainguard and ready to move existing workloads over? Start with the product you're migrating.

## Migrate containers

Replace the base images in your Dockerfiles with Chainguard Containers. Because Chainguard Containers are minimal — most have no shell or package manager — migration usually means adjusting how your image installs dependencies, which user it runs as, and what its entrypoint expects.

- **[Container migration overview](/chainguard/containers/migration/migrations-overview/)** — key differences, rollout strategy, and troubleshooting.
- **[Porting a sample application](/chainguard/containers/migration/porting-apps-to-chainguard/)** — a full walkthrough converting a three-service application.
- **[Migrating Dockerfiles](/chainguard/containers/migration/migrating-to-chainguard-images/)** — instruction-by-instruction guidance.
- **[Migration checklist](/chainguard/containers/migration/migration-checklist/)** — best practices to work through before and during a rollout.
- **[Compatibility guides](/chainguard/containers/migration/compatibility/)** — what changes when moving from Alpine, Debian, Red Hat, or Ubuntu.
- **[Language and platform guides](/chainguard/containers/migration/migration-guides/)** — Python, Node, PHP, .NET, Go, and Java.

## Migrate libraries

Point your package manager at Chainguard Libraries and reinstall. Libraries are rebuilt from verified source as drop-in replacements, so migration is a configuration change rather than a code change.

- **[Java](/chainguard/libraries/java/migration/)** — switch an existing Maven or Gradle project over.
- **[JavaScript](/chainguard/libraries/javascript/migration/)** — switch an existing npm project over.
- **[Python](/chainguard/libraries/python/migration/)** — switch an existing pip, uv, or Poetry project over.

Libraries are currently available for Java, Python, and JavaScript. For background on how access and configuration work, refer to the [Chainguard Libraries overview](/chainguard/libraries/overview/).

## Migrate an API integration

If you call the Chainguard API directly, v2 is Generally Available and endpoints have moved from `/v1/` to `/v2/`.

- **[API v1 to v2 migration](/platform/api/api-v2-migration/)** — what changed and how to move a direct integration over.

`chainctl`, the Chainguard Console, and the Terraform provider handle versioning themselves, so this only applies to `curl`, gRPC, or custom SDK integrations.

## Automate the migration

Three tools reduce the manual work, and they suit different situations:

- **[Guardener Dockerfile migration](/chainguard/guardener/dockerfile-migration/)** — an AI agent that converts, builds, and validates your Dockerfiles until they work. Use it when a Dockerfile is complex enough that a mechanical translation won't hold up.
- **[Dockerfile Converter (dfc)](/chainguard/containers/migration/dockerfile-conversion/)** — an open source tool that rewrites `apt`, `yum`, and `apk` instructions deterministically. Use it when you want a fast, predictable first pass you can review yourself.
- **[Image Matcher](/chainguard/containers/migration/image-matcher/)** — an API that reads an existing image's SBOM and ranks the closest Chainguard equivalents. Use it when you know what you run today but not what to replace it with.

Guardener also migrates GitHub Actions to hardened, SHA-pinned equivalents and enforces signed commits. Refer to the [Guardener overview](/chainguard/guardener/) for its full set of capabilities.
