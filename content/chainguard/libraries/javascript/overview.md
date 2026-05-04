---
title: "Chainguard Libraries for JavaScript overview"
linktitle: "JavaScript overview"
aliases:
- /chainguard/libraries/chainguard-repository/
description: "JavaScript libraries for your application development"
type: "article"
date: 2025-06-05T09:00:00+00:00
lastmod: 2025-06-05T09:00:00+00:00
draft: false
tags: ["Chainguard Libraries", "JavaScript", "Overview"]
menu:
  docs:
    parent: "javascript"
weight: 051
toc: true
---

**Chainguard Libraries for JavaScript** is a major ecosystem supported by
[Chainguard Libraries](/chainguard/libraries/overview/). The JavaScript
ecosystem consists of thousands of open source projects from the communities
around [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript),
[TypeScript](https://www.typescriptlang.org/), [Node.js](https://nodejs.org/),
[React](https://react.dev/), [Vue.js](https://vuejs.org/),
[Angular](https://angular.io/), [Svelte](https://svelte.dev/),
[Next.js](https://nextjs.org/), [Express](https://expressjs.com/), and many
others.

Chainguard Libraries for JavaScript provides access to a growing collection of
popular Javascript packages rebuilt from source. New releases of packages
requested by customers are built and added to the index by an automated system.
These libraries can also be consumed through the [Chainguard
Repository](/chainguard/libraries/chainguard-repository/), which provides a
single endpoint for package retrieval and supports configurable security
policies for both Chainguard-built and upstream packages.

### Background

The main public repository for JavaScript packages is the [npm
Registry](https://npmjs.com/). Launched in 2010, the npm Registry has grown to
become the largest software registry in the world, hosting over three million
packages. It serves as the central hub for open source JavaScript libraries,
tools, and frameworks, supporting a vibrant and rapidly evolving ecosystem. The
registry is widely used by developers for both client-side and server-side
JavaScript projects, and its scale and history make it a critical resource for
modern application development.

It is the default repository in all commonly used build tools from the
JavaScript community, including [npm](https://www.npmjs.com/),
[pnpm](https://pnpm.io/), [Yarn](https://classic.yarnpkg.com/), and [Yarn
Berry](https://yarnpkg.com/), and uses the npm repository format. Chainguard
Libraries for JavaScript covers many of the open source artifacts found in the 
npm Registry.

You can use Chainguard Libraries for Javascript with [your repository
manager](/chainguard/libraries/javascript/global-configuration/), such as JFrog
Artifactory or Sonatype Nexus.

## Runtime requirements

The runtime requirements for packages available from Chainguard
Libraries for JavaScript are identical to the requirements of the original
upstream project. For example, if a package retrieved from the npm Registry
requires Node.JS v22 or higher, the same Node.JS v22 requirement applies to the
package from Chainguard Libraries for JavaScript. The same applies to JavaScript,
Typescript, or React versions, as well as any other requirements of the original
upstream project.

## Technical details

The [username and password retrieved with
chainctl](/chainguard/libraries/access/) are required to access the Chainguard
Libraries for JavaScript repository. The URL for the repository is:

```
https://libraries.cgr.dev/javascript/
```

The URL does not expose a browsable directory structure.

The Chainguard Libraries for JavaScript repository is exposed through the Chainguard Repository endpoint for JavaScript libraries. It uses the npm repository protocol and serves both libraries that Chainguard has rebuilt from verifiable source and, when configured, packages proxied from the public npm registry under configurable policy controls. All packages served through this endpoint are subject to Chainguard security controls such as malware scanning and a configurable cooldown period for newly published upstream versions.

Even with upstream fallback enabled, the repository does not include every package from npm. Packages may be unavailable when:

* No verifiable source code is available. For example, malicious or proprietary packages where Chainguard cannot validate the source.
* The package is blocked by Chainguard or your organization’s policies. For example, packages flagged as malware or packages currently within the configurable cooldown period.

We recommend configuring the Chainguard Repository (or a repository manager that proxies it) as the primary registry for all JavaScript dependency resolution. This ensures your builds always prefer Chainguard‑built libraries first and automatically fall back to policy‑protected upstream packages when a Chainguard build is not yet available.

You can continue to use additional registries alongside Chainguard for needs outside this scope, such as your own private or scoped packages from npm or another internal registry.

Configure this endpoint [globally through a repository manager](/chainguard/libraries/javascript/global-configuration/) for centralized access control across your organization, or use it for [direct access](/chainguard/libraries/javascript/build-configuration/) from individual build tools. If you prefer to manage your own npm fallback rather than using the built-in upstream fallback, see the [global configuration documentation](/chainguard/libraries/javascript/global-configuration/) for setup guides per repository manager.

## Updating lockfile hashes

When migrating an existing JavaScript project to Chainguard Libraries, your
lockfile contains integrity hashes generated against npm registry artifacts.
Because Chainguard rebuilds packages in a secured build environment rather than
distributing upstream artifacts directly, the resulting checksums differ even
for identical package versions. These hashes must be updated before your package
manager will accept packages from Chainguard.

> **Note:** `chainctl libraries update-hashes` does not currently support
> authentication through a repository manager. You will need to
> [configure direct access](/chainguard/libraries/javascript/build-configuration/#direct-access)
> credentials before running the command, or update the lockfiles manually.

The `chainctl libraries update-hashes` command automates lockfile hash updates
for all supported JavaScript lockfile formats. Rather than deleting your
lockfile and reinstalling from scratch, you can run the command directly against
your existing lockfile to update integrity hashes and resolved URLs to use
Chainguard, while preserving the file's format and structure.

Supported formats include `package-lock.json` (npm v2/v3), `yarn.lock` (Yarn
Classic and Berry), `pnpm-lock.yaml`, and `bun.lock`.

Run the command in the directory containing the lockfile:

```bash
chainctl libraries update-hashes
```

Or specify a lockfile path directly:

```bash
chainctl libraries update-hashes path/to/lockfile
```

By default, Chainguard hashes are appended alongside existing upstream hashes
and resolved URLs are updated to point to Chainguard. After updating the
lockfile, ensure your `.npmrc` or equivalent is configured with Chainguard
credentials, then reinstall to apply the changes. The `chainctl libraries update-hashes` command will output
a "Next steps" section that includes the tool-specific command for reinstalling.

> **Note:** Packages that resolve through the Chainguard Repository's upstream
> npm fallback may still point to `registry.npmjs.org` in your lockfile after
> running the command. See [Upstream packages](#upstream-packages) for
> details.

#### Upstream packages

If your organization uses the Chainguard Repository with upstream npm fallback
enabled, packages that resolve through the upstream registry may still point to
`registry.npmjs.org` in your lockfile after running `chainctl libraries
update-hashes`. These packages are not automatically redirected to route through
Chainguard. Once Chainguard has rebuilt the package from source, a subsequent
run of `update-hashes` will update it automatically.

## Provenance and attestations
Chainguard Libraries for JavaScript include SLSA provenance with signed attestations. 
These attestations cryptographically link each package to the Chainguard 
Factory build environment, providing verifiable proof of where and how each package 
was produced. Provenance attestations follow the npm attestation standard. The 
Chainguard publisher identity is verifiable via the Sigstore signing certificate 
embedded in the attestation bundle, which links back to https://issuer.enforce.dev,  
the Chainguard OIDC issuer.

You can verify a package tarball in a single command using `chainctl`:

```bash
chainctl libraries verify PACKAGE-VERSION.tgz
```

See [Verification](/chainguard/libraries/verification/) for setup and usage details.

### Verify attestation manually

Alternatively, you can verify a specific package's provenance attestation manually using `cosign`, which is useful for debugging or integrating individual steps into custom workflows. In the following commands, replace `PACKAGE` 
and `VERSION` with the package name and version (for example, `axios-mock-adapter` 
and `1.17.0`):

**Download the tarball**
```
curl -L -H "Authorization: Bearer $(chainctl auth token --audience=libraries.cgr.dev)" \
  "https://libraries.cgr.dev/javascript/PACKAGE/-/PACKAGE-VERSION.tgz" \
  -o PACKAGE-VERSION.tgz
```

**Extract the SLSA provenance bundle**
```
curl -H "Authorization: Bearer $(chainctl auth token --audience=libraries.cgr.dev)" \
  "https://libraries.cgr.dev/javascript/-/npm/v1/attestations/PACKAGE@VERSION" | \
  jq -c '.attestations[] | select(.predicateType | contains("slsa")) | .bundle' \
  > PACKAGE-provenance.sigstore.json
```

**Verify the attestation was signed by Chainguard**
```
cosign verify-blob-attestation \
  --bundle PACKAGE-provenance.sigstore.json \
  --new-bundle-format \
  --certificate-oidc-issuer=https://issuer.enforce.dev \
  --certificate-identity-regexp="^https://issuer.enforce.dev/" \
  --check-claims=false \
  PACKAGE-VERSION.tgz
```

A successful verification returns:
```
Verified OK
```

The `--certificate-oidc-issuer` and `--certificate-identity-regexp` flags confirm 
the attestation was signed by Chainguard. 

### Retrieve SBOMs

Chainguard Libraries for JavaScript also include Software Bills of Materials (SBOMs) in SPDX format. 

To check whether an SBOM is available for a package, use npm show with the dist.sboms field:

```bash
npm show PACKAGE@VERSION dist.sboms
```

To retrieve the SBOM directly:

```bash
curl -H "Authorization: Bearer $(chainctl auth token --audience=libraries.cgr.dev)" https://libraries.cgr.dev/javascript/-/npm/v1/sbom/spdx/PACKAGE@VERSION
```

Replace `PACKAGE` and `VERSION` with the package name and version (for example, `react-router` and `7.11.0`).

## Upstream fallback policy and controls

Chainguard Libraries for JavaScript supports an optional built-in fallback to
the upstream npm Registry, managed through the [Chainguard
Repository](/chainguard/chainguard-repository/overview/). By default, the endpoint serves
only Chainguard-built packages. When the upstream fallback is enabled, upstream packages are
subject to additional security controls before being served.

### Enable the upstream repository

To enable or change upstream fallback configuration, use the [`chainctl
libraries entitlements`
command](/chainguard/chainctl/chainctl-docs/chainctl_libraries_entitlements_create/).

The following command creates or updates an entitlement to Chainguard Libraries
for JavaScript, adds the npm upstream fallback policy, and configures a 7-day cooldown:

```bash
chainctl libraries entitlements create --ecosystems=JAVASCRIPT --policy=CHAINGUARD_AND_UPSTREAM --cooldown-days=7
```

### Fallback options
The following options are available:
* **No upstream fallback (default)**: Only Chainguard-built packages are served.
* **Upstream fallback enabled with cooldown**: Upstream packages are available after passing a cooldown period and malware scan. The same cooldown period is also enforced for Chainguard-built packages when the upstream repository is enabled, so dependency trees resolve consistently across both sources.

#### Configuring the cooldown period

When upstream fallback is enabled, users with the Owner role can configure the cooldown with `chainctl`:

```bash
chainctl libraries entitlements create --ecosystems=JAVASCRIPT --policy=CHAINGUARD_AND_UPSTREAM --cooldown-days=3
```
The default cooldown period is 7 days. Note that shorter cooldown periods increase the risk of pulling malicious or compromised upstream packages before the broader ecosystem can detect and report them.

> **Upstream fallback best practices**
> Upstream packages are proxied directly from npm and are not rebuilt or authored by Chainguard as part of our Libraries product. The cooldown period and malware scanning provide a supplemental baseline of protection to your own security practices, but you are solely responsible for independently evaluating and validating all upstream artifacts before use in your environment.

### Security controls

#### Malware scanning
All packages served from the upstream fallback are scanned for malware before being made available. Any package version with a detected malware identifier (MAL ID) from the public OSV feed is blocked and will not be served.

Malware detection is continuous. If a version that was previously cached is later identified as malicious, it is added to the block list and will be blocked on subsequent requests.

#### Cooldown period

When fallback is enabled, upstream npm packages are subject to a cooldown period from their publication date before the Chainguard Repository will serve them. The cooldown applies globally across Chainguard-built packages and upstream npm packages served through the fallback. The cooldown is an additional layer of security that provides a window for the security community to identify and report malicious packages before your builds can pull them. 

The cooldown applies globally across Chainguard-built packages and upstream npm packages served through the fallback. This prevents installs from failing when a Chainguard-built package depends on an upstream dependency that is still under the cooldown window.

If a package version is requested and falls within the cooldown period, the package manager will output a 404 error. The package becomes available once it has passed the cooldown period and cleared malware scanning.

### How package resolution works

When you request a JavaScript package from the Chainguard Repository, the following logic applies:
* **Chainguard-built package available**: The package is served directly from Chainguard's rebuilt artifact store, complete with SBOM, provenance, and signatures, subject to the configured cooldown.
* **Package not yet built by Chainguard**: If upstream fallback is enabled, the repository checks whether the package has passed the cooldown period and malware scan.
    * **Within the cooldown period**: The request returns an error. This prevents newly published packages — which carry higher malware risk — from being served immediately.
    * **After the cooldown period**: If upstream fallback is enabled and the version is outside the cooldown window and passes malware scanning, the repository pulls the version through from the npm registry, serves it to the client, and caches it in the upstream mirror for future requests.
* **Malware detected**: Any package version with a known malware identifier (MAL ID) is blocked and never served, whether it originates from Chainguard builds or the npm upstream. Malware scanning runs on all packages, including those proxied from npm.
    * Malware scanning checks all packages against the Open Source Vulnerabilities (OSV) database, which includes the OpenSSF Malicious Packages feed among other sources. Any package version flagged with a malware identifier is blocked. This covers reported malicious packages across the npm ecosystem.

> **Note**: Chainguard Repository for JavaScript is not a full mirror of npm by design. Packages are screened for malware before being made available. Some packages may be delayed by the cooldown period or permanently blocked if flagged as malicious.
