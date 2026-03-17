---
title: "Chainguard Repository for JavaScript Libraries"
linktitle: "Chainguard Repository"
description: "Learn how to use Chainguard Repository to configure how Chainguard-built and upstream packages are consumed"
type: "article"
date: 2025-03-25T00:08:04+00:00
lastmod: 2025-07-23T15:09:59+00:00
draft: false
tags: ["Chainguard Libraries"]
menu:
  docs:
    parent: "libraries"
weight: 005
toc: true
---
Chainguard Repository is a unified Chainguard-managed experience for pulling
secure-by-default open source artifacts. Chainguard Libraries for JavaScript is
the first artifact type available through it, with configurable policies that
control how both Chainguard-built packages and upstream npm packages are
consumed. Upstream packages are subject to additional security controls,
including malware scanning and an optional cooldown period.

Pointing your existing build tools or repository manager tools at the Chainguard
Repository gives you:
* Access to both Chainguard-built packages and upstream npm packages (when
  fallback is enabled), so you don't need to maintain a parallel npm fallback
  configuration.
* Malware scanning and a cooldown period applied to all packages the repository
  serves, including those proxied from npm.
* One endpoint to configure, whether or not you use an artifact manager.

## Using the Chainguard Repository endpoint for JavaScript
The Chainguard Repository for Javascript uses the same endpoint and
authentication as Chainguard Libraries for JavaScript:
`https://libraries.cgr.dev/javascript/`.

You can use your existing `chainctl` token. See [Chainguard Libraries
Access](/chainguard/libraries/access/) for instructions for retrieving
credentials with `chainctl`. 

Learn about [fallback configuration](#configuring-upstream-fallback) and
[cooldown periods](#cooldown-period) later on this page.

### Use Chainguard Repository with build tools
If you don’t use an artifact manager, you can point your build tools directly at
the Chainguard Libraries for JavaScript endpoint. The Chainguard Repository
handles fallback, so no additional registry configuration is needed alongside
it.

#### Step 1: Generate credentials and set them in your project

Authentication is required. The recommended way to set up credentials for direct
npm access is using `chainctl`:

```bash
# Generate credentials and set them in your project .npmrc in one step
eval $(chainctl auth pull-token --output env --repository=javascript --parent=<your-org>)
export token=$(echo -n "${CHAINGUARD_JAVASCRIPT_IDENTITY_ID}:${CHAINGUARD_JAVASCRIPT_TOKEN}" | base64 -w 0)
npm config set registry https://libraries.cgr.dev/javascript/ --location=project
npm config set //libraries.cgr.dev/javascript/:_auth "${token}" --location=project
```

Note that npm requires credentials as a base64-encoded token in `.npmrc` — the
`.netrc` credential format used for other Chainguard Libraries ecosystems does
not work with npm.

#### Step 2: Configure your tool to use the Chainguard endpoint

Next, configure your tool of choice to use the Chainguard endpoint as its
registry:

```bash
# pnpm
pnpm config set registry https://libraries.cgr.dev/javascript/

# Yarn
yarn config set npmRegistryServer https://libraries.cgr.dev/javascript/
```

For full setup instructions including authentication, see [Build Configuration:
Direct
Access](/chainguard/libraries/javascript/build-configuration/#direct-access/).

### Use Chainguard Repository with a repository manager
If you use JFrog Artifactory, Sonatype Nexus, or a similar repository manager,
you can point it to the Chainguard Repository endpoint as your single upstream
npm source. This replaces the previous pattern of configuring Chainguard
Libraries and npm as separate upstreams with a priority ordering.

Point your repository manager's virtual or group repository at
`libraries.cgr.dev/javascript` as the single upstream. The Chainguard Repository
handles fallback and policy; your repo manager handles local caching and access
control for your organization.

See [Global
configuration](/chainguard/libraries/javascript/global-configuration/) for setup
guides per repository manager.

### Configuring upstream fallback
By default, the Chainguard Repository serves only Chainguard-built packages. You can contact your Chainguard account team or customer support to enable the built-in fallback to the upstream npm registry, which allows the repository to serve packages not yet built by Chainguard. All upstream packages are subject to additional [security controls](#security-controls) before they are served.

### Fallback options
Contact your Chainguard account team or Chainguard support to configure an upstream fallback. The options are:
* **No upstream fallback (default)**: Only Chainguard-built packages are served.
* **Upstream fallback enabled with cooldown**: Upstream packages are available after passing a cooldown period and malware scan.

> **Upstream fallback best practices**
> Upstream packages are proxied directly from npm and are not rebuilt or authored by Chainguard as part of our Libraries product. The cooldown period and malware scanning provide a supplemental baseline of protection to your own security practices, but you are solely responsible for independently evaluating and validating all upstream artifacts before use in your environment.

## Security controls

### Malware scanning
All packages served from the upstream fallback are scanned for malware before being made available.Any package version with a detected malware identifier (MAL ID) from the public OSV feed is blocked and will not be served.

### Cooldown period
When fallback is enabled, upstream npm packages are subject to a default 7-day cooldown from their publication date before the Chainguard Repository will serve them. The cooldown is an additional layer of security on top of malware scanning. It provides a window for the security community to identify and report malicious packages before your builds can pull them.

If a package version is requested and falls within the cooldown period, the package manager will output a 404 error. The package becomes available once it has passed the cooldown period and cleared malware scanning.

## How package resolution works
When you request a JavaScript package from the Chainguard Repository, the following logic applies:
* **Chainguard-built package available**: The package is served directly from Chainguard's rebuilt artifact store, complete with SBOM, provenance, and signatures.
* **Package not yet built by Chainguard**: If upstream fallback is enabled, the repository checks whether the package has passed the cooldown period and malware scan.
    * **Within the cooldown period**: The request returns an error. This prevents newly published packages — which carry higher malware risk — from being served immediately.
    * **After the cooldown period**: The package is checked against malware scanning. If it passes, it is proxied from the npm Registry.
* **Malware detected**: Any package version with a known malware identifier (MAL ID) is blocked and never served, whether it originates from Chainguard builds or the npm upstream. Malware scanning runs on all packages, including those proxied from npm.
    * Malware scanning checks all packages against the Open Source Vulnerabilities (OSV) database, which includes the OpenSSF Malicious Packages feed among other sources. Any package version flagged with a known MAL ID is blocked before it can be served. This covers reported malicious packages across the npm ecosystem; packages with unreported or novel malware may not be detected by scanning alone, which is why building from verified source remains the primary defense.

## View repository configuration in the Chainguard Console
The Chainguard Console provides visibility into your repository configuration and the packages being served. When the upstream fallback is configured for your organization, you will see all packages including those built-by Chainguard and those that are mirrored from upstream npm.

