---
title: "Quick start for Chainguard Libraries"
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
verified, the package doesn't appear in the Chainguard Libraries repository. They are
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
    * Run the following [chainctl libraries](/chainguard/chainctl/chainctl-docs/chainctl_libraries_entitlements/) command to create an entitlement for libraries:

```bash
chainctl libraries entitlements create --ecosystems=JAVASCRIPT
```
The available `ecosystems` are `JAVASCRIPT`, `JAVA`, and `PYTHON`.

Alternatively, you can create an entitlement and pull token in the Chainguard Console: while viewing a library ecosystem page, follow the prompts to create an access token.

## Step 1: Choose your access method

There are two ways to access Chainguard Libraries: using an [artifact manager](#artifact-manager-recommended) (recommended), or [direct access](#direct-access).

### Artifact manager (recommended)

Configure credentials once in a tool like JFrog Artifactory, Sonatype Nexus, or Cloudsmith. This centralizes policy, logging, and fallback behavior, and is the safest approach for organizations with multiple teams and applications.

Note that built-in [configurable upstream fallback](/chainguard/libraries/javascript/overview/#upstream-fallback-policy-and-controls) is available for Chainguard Libraries for JavaScript via the Chainguard Repository, but not yet available for Chainguard Libraries for Python or Java. Before configuring your repository manager, consider how you want to handle packages that aren't available in the Chainguard repository:

**Python and Java fallback approach**

* **Chainguard only (recommended)**: Configure your repository manager to
  use the Chainguard Libraries repository as the only upstream source. If a package isn't
  available in the Chainguard repository, your build will fail until coverage is
  added. Alternatively, you may be able to use a version or alternative library that Chainguard has already built.
* **Chainguard with public registry fallback**: Configure your repository
manager to fall back to Maven Central or PyPI for packages not available in the
Chainguard Libraries repository. This prevents build failures due to missing packages, but
packages sourced from public registries are **not** covered by Chainguard's
malware-resistance guarantees. If you choose this option, we strongly recommend
configuring a quarantine or cooldown period on your fallback repository so that
newly published or updated packages are not immediately available to developers.
Chainguard has no control over malware protection for packages sourced from
public registries.

**JavaScript fallback approach**

For JavaScript, use the Chainguard Repository's [built-in npm
fallback](/chainguard/libraries/javascript/overview/#upstream-fallback-policy-and-controls)
instead of configuring a public registry fallback in your artifact manager. The
Chainguard Repository handles fallback safely, ensuring you receive the last
known safe version of a package rather than the latest available on npm. Note
that the repository does not host the entire npm catalog and may block or delay
some upstream packages. 

If you configure your own npm fallback in your artifact manager, it bypasses
this protection.

### Direct access

Configure authentication directly in each project's build configuration.

This option is faster to set up initially, but requires per-project and
per-workstation configuration. This increases the risk of credentials being
committed to source control or going stale. For production use, Chainguard
strongly recommends using an artifact manager.

Learn how to set up direct access in the build configuration documentation for
[Python](/chainguard/libraries/python/build-configuration/),
[JavaScript](/chainguard/libraries/javascript/build-configuration/), and
[Java](/chainguard/libraries/java/build-configuration/). 

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

Learn more about pull tokens, and using environment variables for pull token credentials, in the [Libraries Access documentation](/chainguard/libraries/access/).

## Step 3: Configure your build tools

Once you have a pull token, you can configure your build tool. Configuration
steps vary by build tool and ecosystem. See the ecosystem-specific documentation
pages for instructions. 

### Java 

* [Repository manager](/chainguard/libraries/java/global-configuration/)
  **(recommended)**: Configure your repository manager or build tool to use
  `https://libraries.cgr.dev/java/` as the first repository for artifact
  resolution, falling back to Maven Central for unavailable libraries. 
* [Direct access](/chainguard/libraries/java/build-configuration/): Configure
  your tool to retrieve artifacts directly from the Chainguard Libraries for
  Java repository at `https://libraries.cgr.dev/java/`. Use direct access for
  small teams or evaluations, or when you have an existing repository
  configuration you can't change yet.
  
Check out minimal example projects for
[Maven](/chainguard/libraries/java/build-configuration/#minimal-example-project)
and
[Gradle](/chainguard/libraries/java/build-configuration/#minimal-example-project-1) to understand how to use these repositories.

### Python

* [Repository manager](/chainguard/libraries/python/global-configuration/)
  **(recommended)**: Add Chainguard Libraries as a remote repository in your
  repository manager, alongside PyPI as a fallback. 
* [Direct access](/chainguard/libraries/python/build-configuration/): Configure
  your tool to retrieve artifacts directly from the Chainguard Libraries for
  Python. 

Note that there are multiple repositories:
* `https://libraries.cgr.dev/python/` with the simple index at
  `https://libraries.cgr.dev/python/simple`
* `https://libraries.cgr.dev/python-remediated` with the simple index at
  `https://libraries.cgr.dev/python-remediated/simple` for libraries with [CVE
  remediation](/chainguard/libraries/cve-remediation/)

Check out minimal example projects for
[uv](/chainguard/libraries/python/build-configuration/#uv-minimal) and [pip](/chainguard/libraries/python/build-configuration/#pip-minimal) to understand how to use these repositories.

> In addition to malware-resistance, Chainguard Libraries for Python includes
> CVE remediation for select libraries. These patched versions help reduce known
> risk while you plan your next major version upgrade. You can view which
> libraries have CVE remediation available in the Chainguard Console. CVE
> remediation is currently available for Python libraries only.

### JavaScript

* [Repository
  manager](/chainguard/libraries/javascript/global-configuration/)
  **(recommended)**: Add the Chainguard Libraries registry as a remote repository
  and configure it as the first choice for package resolution, with npm as a
  fallback only where necessary. 
* [Direct access](/chainguard/libraries/javascript/build-configuration/): Configure your `.npmrc` to use `https://libraries.cgr.dev/javascript/` as the registry. 

<a id="upstream-note"></a>

> **Note on upstream fallback for JavaScript**: The npm upstream fallback is
> available as an opt-in setting for both repository manager or direct access
> approaches, and is turned off by default. Upstream packages are proxied
> directly from npm and are not rebuilt or authored by Chainguard as part of our
> Libraries product. The cooldown period and malware scanning provide a
> supplemental baseline of protection to your own security practices, but you
> are solely responsible for independently evaluating and validating all
> upstream artifacts before use in your environment.  
> <br>Learn more about upstream
> fallback policy and controls in the [JavaScript
> overview](/chainguard/libraries/javascript/overview/#upstream-fallback-policy-and-controls).

Check out minimal example projects for
[npm](/chainguard/libraries/javascript/build-configuration/#minimal-example-project),
[pnpm](/chainguard/libraries/javascript/build-configuration/#minimal-example-project-1),
[Yarn](/chainguard/libraries/javascript/build-configuration/#minimal-example-project-2),
[Yarn
Classic](/chainguard/libraries/javascript/build-configuration/#minimal-example-project-3),
and
[Bun](/chainguard/libraries/javascript/build-configuration/#minimal-example-project-4) to understand how to use these repositories.

## Step 4: Verify your libraries

After setup, you can verify that your dependencies are sourced from Chainguard using:

```bash
chainctl libraries verify /path/to/artifact
```

Learn more in [Chainguard Libraries verification](/chainguard/libraries/verification/).

## FAQs

See the [Chainguard Libraries FAQ page](/chainguard/libraries/faq/) for common questions and issues.