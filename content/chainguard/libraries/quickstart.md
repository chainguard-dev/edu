---
title: "Quick Start for Chainguard Libraries"
linktitle: "Quick Start"
description: "Learn how to get started with Chainguard Libraries"
type: "article"
date: 2025-03-25T00:08:04+00:00
draft: false
tags: ["Chainguard Libraries"]
menu:
  docs:
    parent: "libraries"
weight: 001
toc: true
---

Most supply chain attacks succeed the same way: malicious code is injected into
a package after the source is written — either as a backdoored binary with no
verifiable source, or as a malicious install-time script that runs the moment a
dependency is pulled. Recent attacks on LiteLLM, Telnyx, and Axios all followed
this pattern.

Chainguard Libraries are rebuilt from verified source in an isolated build
environment, making them malware-resistant by design. If the source can't be
verified, the package doesn't appear in the Chainguard Repository. They are
drop-in replacements for the Python, Java, and JavaScript packages your
engineers already use, with no breaking changes.

This guide covers the high-level steps to get up and running. For full reference
documentation on any step, follow the links provided.

## Prerequisites

Before getting started:

* If you're not yet a Chainguard user, you must [create an
      account](https://console.chainguard.dev/auth/login).
* [Install `chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/) and
  log in:

   ```bash
   chainctl auth login
   ```
* Entitle access for yourself to Chainguard Libraries.
    * Chainguard Libraries are available to Catalog Starter and Free tier users,
      and trial users. 
    * Run the following command to create an entitlement for libraries:
    
```bash
chainctl libraries entitlements create --ecosystems=JAVASCRIPT
```
The available `ecosystems` are `JAVASCRIPT`, `JAVA`, and `PYTHON`.

## Step 1: Choose your access method

There are two ways to access Chainguard Libraries:

- **Artifact manager (recommended)**: Configure credentials once in a tool like
 JFrog Artifactory, Sonatype Nexus, or Cloudsmith. All projects and developers automatically inherit the configuration. 
    - This option is best for organizations with multiple teams.

- **Direct access**: Configure authentication directly in each project's build
  configuration.
    - This option is faster to set up initially, but requires per-project and
      per-workstation configuration. This increases the risk of credentials
      being committed to source control or going stale. For production use, an
      artifact manager is strongly recommended.

Learn more about these options in [Chainguard Libraries
access](/chainguard/libraries/access/).

## Step 2: Create a pull token

[Pull tokens](/chainguard/libraries/access/#creating-pull-tokens-for-libraries)
are required for authentication. You can create one using `chainctl`:

```bash
chainctl auth pull-token --repository=java --parent=example.com --ttl=720h
```

- Replace `java` with `python` or `javascript` depending on your chosen ecosystem.
- Replace `example.com` with your organization name.
- The default TTL is `720h` (30 days); the maximum is `8760h` (365 days).

The command returns a username and password for basic authentication. Store
these securely, as they won't be shown again.

You can also [create pull tokens via the Chainguard
Console](/chainguard/libraries/access/#creating-pull-tokens-with-the-chainguard-console)
under **Overview > Manage pull tokens > Create access token**. 

## Step 3: Configure your build tools

Once you have a pull token, you can configure your build tool. Configuration
steps vary by build tool and ecosystem. See the ecosystem-specific documentation
pages for instructions. 

- **Java** 
    - [Repository manager](/chainguard/libraries/java/global-configuration/):
  Configure your repository manager or build tool to use
  `https://libraries.cgr.dev/java/` as the first repository for artifact
  resolution, falling back to Maven Central for unavailable libraries. 
    - [Direct access](/chainguard/libraries/java/build-configuration/):
      Configure your tool to retrieve artifacts directly from the Chainguard
      Libraries for Java repository at `https://libraries.cgr.dev/java/`.
  
Check out minimal example projects for
[Maven](/chainguard/libraries/java/build-configuration/#minimal-example-project)
and
[Gradle](/chainguard/libraries/java/build-configuration/#minimal-example-project-1).

- **Python** 
    - [Repository manager](/chainguard/libraries/python/global-configuration/):
  Add Chainguard Libraries as a remote repository in your repository manager,
  alongside PyPI as a fallback. 
    - [Direct access](/chainguard/libraries/python/build-configuration/):
      Configure your tool to retrieve artifacts directly from the Chainguard
      Libraries for Python. Note that there are multiple repositories:
        - `https://libraries.cgr.dev/python/` with the simple index at
          `https://libraries.cgr.dev/python/simple`
        - `https://libraries.cgr.dev/python-remediated` with the simple index at
          `https://libraries.cgr.dev/python-remediated/simple` for libraries
          with [CVE remediation](/chainguard/libraries/cve-remediation/)

> In addition to malware-resistance, Chainguard Libraries for Python includes
> CVE remediation for select libraries. These patched versions help reduce known
> risk while you plan your next major version upgrade. You can view which
> libraries have CVE remediation available in the Chainguard Console. CVE
> remediation is currently available for Python libraries only.

- **JavaScript** 
    - [Repository manager](/chainguard/libraries/javascript/global-configuration/): Add the Chainguard Libraries registry as a remote
  repository and configure it as the first choice for package resolution. 
    - [Direct access](/chainguard/libraries/javascript/build-configuration/): Configure your `.npmrc` to use
      `https://libraries.cgr.dev/javascript/` as the registry, with upstream npm
      fallback available as an opt-in setting. Learn more about upstream
      fallback policy and controls in the [JavaScript
      overview](/chainguard/libraries/javascript/overview/#upstream-fallback-policy-and-controls).

Check out minimal example projects for
[npm](/chainguard/libraries/javascript/build-configuration/#minimal-example-project),
[pnpm](/chainguard/libraries/javascript/build-configuration/#minimal-example-project-1),
[Yarn](/chainguard/libraries/javascript/build-configuration/#minimal-example-project-2),
[Yarn
Classic](/chainguard/libraries/javascript/build-configuration/#minimal-example-project-3),
and
[Bun](/chainguard/libraries/javascript/build-configuration/#minimal-example-project-4).

> **Note on upstream fallback for JavaScript**: The npm upstream fallback is opt-in and is turned off by
> default. Upstream packages are proxied directly from npm and are not rebuilt or authored by Chainguard as part of our Libraries product. The cooldown period and malware scanning provide a supplemental baseline of protection to your own security practices, but you are solely responsible for independently evaluating and validating all upstream artifacts before use in your environment.


## Step 4: Verify your libraries

After setup, you can verify that your dependencies are sourced from Chainguard using:

```bash
chainctl libraries verify /path/to/artifact
```

Learn more in [Chainguard Libraries verification](/chainguard/libraries/verification/).

## FAQs

See the [Chainguard Libraries FAQ page](/chainguard/libraries/faq/) for common questions and issues.