---
title: "Using Chainguard with Kiro"
linktitle: "Kiro"
lead: "Using Chainguard container images and libraries in AI-assisted development with Kiro"
description: "Install the Chainguard Power for Kiro and use it to migrate projects to Chainguard container images and libraries."
type: "article"
date: 2026-06-18T00:00:00-04:00
lastmod: 2026-06-18T00:00:00-04:00
draft: false
weight: 020
---

[Kiro](https://kiro.dev/) helps developers move quickly, but speed alone does not reduce supply chain risk.
Every `docker pull`, `pip install`, `npm install`, or Maven dependency resolution an AI assistant initiates is still a trust decision against a software source.

The Chainguard Power for Kiro brings Chainguard context directly into that workflow.
Kiro remains the place where developers and agents plan, write, and review code.
Chainguard provides the trusted artifacts those workflows depend on: hardened container images, malware-resistant language packages, and related supply chain guidance.

This page explains how to install the Chainguard Power for Kiro and use it to start migrating projects to Chainguard.

## Prerequisites

Before you begin, you'll need:

* A [Kiro](https://kiro.dev/) account
* A [Chainguard account](https://console.chainguard.dev/) and organization in domain format (for example, `acme-corp.com`).
* [`chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/) installed and authenticated
* Access to the Chainguard products you plan to use
  * Chainguard Images for container image migration
  * Chainguard Libraries for Java, JavaScript, or Python dependency migration. Learn how to create an entitlement in the [Libraries Access docs](/chainguard/libraries/access/#manage-library-entitlements).

The Chainguard Power uses your existing `chainctl` session for image and package lookups in Kiro.
If you want Kiro to help reconfigure a project to use Chainguard Libraries, make sure your organization also has access to the relevant Libraries ecosystem.

## Install the Chainguard Power

The Kiro integration is delivered through the Kiro Powers panel.

To install it:

1. Open Kiro and navigate to the **Powers** panel in the sidebar.
1. Search for `Chainguard`.
1. Select the Chainguard Power and click **Install**.

After installation, Kiro automatically registers the Chainguard MCP servers included with the power.
You do not need to manually edit JSON configuration files or perform separate CLI setup for the power itself.

## Using the Chainguard Power

When the Chainguard Power is installed, Kiro can use Chainguard context to help with tasks such as:

* Migrating Dockerfiles to [Chainguard Containers](https://images.chainguard.dev/)
* Reconfiguring Java, JavaScript, and Python projects to use [Chainguard Libraries](/chainguard/libraries/overview/)
* Looking up Chainguard image tags
* Finding Wolfi package equivalents for packages currently installed with `apt` or similar package managers
* Guiding Chainguard platform tasks such as policy, cluster, and IAM workflows

The power includes the following MCP servers:

* `cg-api` for Chainguard platform and organization workflows
* `cg-apk` for Wolfi package discovery
* `cg-oci` for container image discovery and tag lookup
* `cg-versions` for version and upgrade-path lookup

## Migrate a project to use Chainguard

After installing the power, open your project in Kiro and describe the migration you want.

For example:

```prompt
Can you help me migrate this project to use Chainguard images and libraries?
```

Kiro can then inspect the relevant files in your project and suggest changes such as:

* Replacing public base images with Chainguard container images
* Translating OS packages to Wolfi equivalents
* Updating package manager configuration to use Chainguard Libraries
* Explaining the changes it made so you can review them before building or deploying

As with any AI-assisted code change, review the output before you run a build or ship it to production.

### Example: Migrate a Dockerfile

One of the most direct ways to get started is to paste a Dockerfile into Kiro and ask for help migrating it.

For example:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y curl git libpq-dev
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

Prompt Kiro with a request such as:

```prompt
Can you help me migrate this Dockerfile to use Chainguard Images?
```

Kiro can then look up a Chainguard replacement image, translate system package installation to the appropriate Wolfi packages, rewrite the Dockerfile, and explain any important tradeoffs.

A resulting Dockerfile might look similar to this:

```dockerfile
FROM cgr.dev/chainguard/python:3.11-dev
WORKDIR /app
RUN apk add --no-cache curl git libpq-dev
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

In this example, Kiro may also point out that:

* a `-dev` image is useful when build-time tooling is required
* a production runtime image may use a different tag
* Chainguard images run as non-root by default

To browse available images and tags, see the [Chainguard Images directory](https://images.chainguard.dev/).

## Use Chainguard Libraries with Kiro

The Chainguard Power can also help migrate language dependencies to Chainguard Libraries.

For example, you can ask Kiro to help with prompts such as:

* `Help me configure npm to use Chainguard Libraries`
* `How do I set up my Maven project to use Chainguard Libraries?`
* `Help me migrate this Python project to Chainguard Libraries`

Kiro can help update build files and package manager configuration, but your build environment still needs valid Chainguard credentials for package installation.

For ecosystem-specific instructions, see:

* [Chainguard Libraries for JavaScript](/chainguard/libraries/javascript/overview/)
* [Chainguard Libraries for Python](/chainguard/libraries/python/overview/)
* [Chainguard Libraries for Java](/chainguard/libraries/java/overview/)


## Troubleshooting

### The power installs, but I cannot use Chainguard artifacts in my build

The Kiro power can guide configuration and migration steps, but your local or remote build environment still needs the right Chainguard access configured.

Check the following:

* `chainctl` is installed and authenticated
* you have access to the relevant Chainguard product
* if you are using Chainguard Libraries, you have credentials or tokens configured for the correct ecosystem

### A referenced image tag does not exist

If Kiro suggests a Chainguard image tag that is unavailable:

* check the image and available tags in the [Chainguard Images directory](https://images.chainguard.dev/)
* start with a broadly available tag such as a current versioned runtime or `latest-dev` equivalent when appropriate for evaluation
* pin to a specific version or digest before production use

### A package is not available from Chainguard Libraries

Chainguard Libraries does not mirror every package version from public registries.
If a dependency is unavailable, your build may fail until you adjust configuration or enable an allowed fallback path.

Common examples:

* JavaScript: configure upstream fallback according to your Chainguard Repository or Libraries policy
* Python: if your policy allows it, add PyPI as an additional index for packages that are not yet available from Chainguard
* Java: add Maven Central after the Chainguard repository entry if your workflow allows upstream fallback

See the ecosystem documentation for the exact configuration patterns and policy considerations.

## Learn more

* [Chainguard Images directory](https://images.chainguard.dev/)
* [Chainguard Libraries](https://www.chainguard.dev/libraries)
* [Install chainctl](/chainguard/chainctl-usage/how-to-install-chainctl/)
* [Kiro Powers directory](https://kiro.dev/powers/)
