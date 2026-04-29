---
title : "Using Chainguard with Cursor"
linktitle: "Cursor"
lead: "Using Chainguard container images and libraries in AI-generated code with Cursor"
description: "Using Chainguard container images and libraries in AI-generated code with Cursor"
type: "article"
date: 2026-04-20T14:00:00-04:00
lastmod: 2026-04-20T14:00:00-04:00
draft: false
weight: 010
---

AI coding agents write code and install dependencies faster than any security team can review them manually. Every `pip install`, `npm install`, or `docker pull` an agent kicks off is a trust decision being made on your behalf against public registries. 

The [Chainguard and Cursor partnership](https://www.chainguard.dev/partners/cursor) follows a clear separation of responsibilities: Cursor is where your developers and agents plan, write, and review code. Chainguard is where developers reach for open source artifacts: Python, Java, and JavaScript libraries plus 2,300+ container images, all rebuilt from verifiable sources in the Chainguard Factory. 

This page explains how to start using Chainguard artifacts in Cursor.

## Prerequisites

Before you begin, you'll need:
* A [Cursor](https://cursor.com/) account
* A [Chainguard account](https://console.enforce.dev/) and organization in domain format (for example, `acme-corp.com`).
* [`chainctl` installed and authenticated](/chainguard/administration/how-to-install-chainctl/)
    * Chainguard authentication should be configured in the environment where Cursor runs commands.
    * Your Chainguard pull token credentials should be injected via environment variables, and not hard-coded in source.

## Migrate a project to use Chainguard

The fastest way to get started is to tell Cursor what you want and let it handle the migration. Open a project in Cursor, then in the chat, use a prompt like:

```prompt
I'd like to migrate this project to use Chainguard images and libraries. My Chainguard org is <your-org>.
```
Cursor will update your Dockerfiles to reference Chainguard container images and reconfigure your build files to pull dependencies from Chainguard Libraries.

> **Note**: Cursor's output is prompt-driven and may vary depending on your project's structure and complexity. Review all changes before running a build or deploying to production.

### Using Chainguard container images
Chainguard provides thousands of minimal, CVE-free container images. When Cursor updates a Dockerfile to use Chainguard images, it will reference the images like the following example:

```dockerfile
FROM cgr.dev/chainguard/python:latest-dev AS builder
FROM cgr.dev/chainguard/python:latest
```

You can browse available images and their tags in the [Chainguard Images directory](https://images.chainguard.dev/). 

This Dockerfile references both the `python` image's `latest` and `latest-dev` variants. Learn more about Chainguard image variants in [Chainguard’s container variants docs](/chainguard/chainguard-images/about/differences-development-production/).

> **Note**: `latest` tags are not recommended for production workloads. For production, we recommend pinning to a specific version or digest to ensure reproducible builds. 

Learn more about Chainguard's container images in the [Containers documentation](/chainguard/chainguard-images/).

### Using Chainguard libraries

[Chainguard Libraries](/chainguard/libraries/) provide malware-resistant Python, Java, and JavaScript packages. When Cursor migrates a project, it reconfigures your build files to pull dependencies from Chainguard instead of public registries. 

You can browse available packages in the [Chainguard Console](https://console.chainguard.dev/), under the **Libraries** section. 

> **Note**: Chainguard Libraries does not mirror every package available on public registries. If a required package is unavailable, your build may fail. See [Package not found / build fails after migration](#package-not-found--build-fails-after-migration) for ecosystem-specific fallback options.

Learn more about configuring libraries in the documentation for each ecosystem: 
- [Chainguard Libraries for JavaScript](/chainguard/libraries/javascript/)
- [Chainguard Libraries for Python](/chainguard/libraries/python/)
- [Chainguard Libraries for Java](/chainguard/libraries/java/)

## Troubleshooting

### Authentication errors on install

If you see a 401 or 403 when running `npm install`, `pip install`, or a Maven build after Cursor configures your project:
* Confirm the pull token was created for the correct ecosystem (`java`, `python`, or `javascript`).
* Check that the token hasn't expired. The default TTL is 720 hours (30 days).
* For npm: verify your `.npmrc` has both the registry line and the auth line for the correct host.

### Image not found / tag doesn't exist
If Cursor references an image tag that doesn't exist:
* Check available tags for the image in the [Chainguard Images directory](https://images.chainguard.dev/). Ensure that you have access to the tag.
* Use `latest` or `latest-dev` as a reliable starting point. Image digests are also available for production use.

### Package not found / build fails after migration

If your build fails because a package is unavailable from Chainguard:
- **JavaScript**: The Chainguard Repository includes a configurable upstream fallback for npm packages; [enable fallback](/chainguard/libraries/javascript/overview/#upstream-fallback-policy-and-controls) if you want to pull from upstream when a package isn't available from Chainguard. 
- **Python**: To enable fallback to PyPI for unavailable packages, add `extra-index-url = https://pypi.org/simple/` to your `pip.conf` or `pyproject.toml`.
- **Java**: To enable upstream fallback, add `mavenCentral()` after the Chainguard Libraries for Java repository in your Gradle configuration, or add Maven Central as a second `repository` entry in your `pom.xml`.
