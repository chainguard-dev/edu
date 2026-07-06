---
aliases:
- /chainguard/integrations/kiro/
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

* A [Kiro](https://kiro.dev/) account, with [Kiro IDE](https://kiro.dev/downloads/) downloaded.
* A [Chainguard account](https://console.chainguard.dev/) and organization in domain format (for example, `acme-corp.com`).
* [`chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/) installed and authenticated
* Access to the Chainguard products you plan to use
  * [Chainguard Containers](/chainguard/chainguard-images/overview/) for container image migration
  * [Chainguard Libraries](/chainguard/libraries/overview/) for Java, JavaScript, or Python dependency migration. Learn how to create an entitlement in the [Libraries Access docs](/chainguard/libraries/access/#manage-library-entitlements).

The Chainguard Power uses your existing `chainctl` session for image and package lookups in Kiro.
If you want Kiro to help reconfigure a project to use Chainguard Libraries, make sure your organization also has access to the relevant Libraries ecosystem.

Note: Chainguard MCP authentication depends on the Chainguard authentication flows available to your organization. If your users do not sign in through one of the currently supported social identity providers (Google, GitHub, or GitLab), then MCP-based IDE workflows may not work as expected. If your organization uses a different IdP, confirm the authentication path before rolling out the Kiro integration broadly.

## Install the Chainguard Power

The Kiro integration is delivered through the Kiro Powers panel.

To install it:

1. Open Kiro IDE and navigate to the **Powers** panel in the sidebar.
1. Scroll down to the Chainguard Power. 
1. Select the Chainguard Power and click **Install**.

After installation, Kiro automatically registers the Chainguard MCP servers included with the power.
You do not need to manually edit JSON configuration files or perform separate CLI setup for the power itself.

## Using the Chainguard Power

Kiro can use Chainguard context to help with tasks such as:

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

### Migrate a project to use Chainguard

After installing the power, open your project in Kiro and describe the migration you want.

For example:

```Prompt
Can you help me migrate this project to use Chainguard container images and libraries?
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

```Prompt
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

To browse available images and tags, see the [Chainguard Containers directory](https://images.chainguard.dev/).

### Use Chainguard Libraries with Kiro

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

## Learn more

* [Chainguard Images directory](https://images.chainguard.dev/)
* [Chainguard Libraries](https://www.chainguard.dev/libraries)
* [Kiro Powers directory](https://kiro.dev/powers/)
