---
title: "Chainguard Libraries for JavaScript overview"
linktitle: "JavaScript overview"
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

## Background

The main public repository for JavaScript packages is the [npm
Registry](https://npmjs.com/). Launched in 2010, the npm Registry has grown to
become the largest software registry in the world, hosting over two million
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

Chainguard Libraries for JavaScript provides access to a growing collection of
popular Javascript packages rebuilt from source. New releases of common packages
requested by customer builds are added to the index by an automated system.

You can use your repository manager, such as JFrog Artifactory or Sonatype Nexus, as a single source of truth, pulling packages from Chainguard Libraries for JavaScript and from public software repositories like the npm Registry.

## Runtime requirements

The runtime requirements for JavaScript packages available from Chainguard
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

This Chainguard Libraries for JavaScript repository uses the npm repository
format and only includes release artifacts for libraries built by Chainguard
from source. It also does not include all packages from the npm registry.

Specifically, the following components are not included:

* Packages without any source code available, including malicious packages and
  proprietary packages.
* Packages that use post-install scripts.
* Packages that are flagged as malware during our build process.

As a result, you must configure the repository as the first point of contact for
all package retrievals. This setup directs requests to Chainguard, ensuring that
all available libraries are used. If a request fails, Chainguard flags it and
runs backfill processes where possible.

At the same time, you might need to continue to use other repositories that
fills the needs for libraries that are not available from the Chainguard
Libraries repository, including your own private or scoped packages from the npm
Registry or another private registry.

Typically the access is [configured globally on a repository manager for your
organization](/chainguard/libraries/javascript/global-configuration/). This
approach is strongly recommended. 

Alternatively, you can use the token for direct access from a build tool as
discussed in [Build
configuration](/chainguard/libraries/javascript/build-configuration/).

## SBOM and attestation files

Chainguard Libraries for JavaScript include files that contain software bill of
material (SBOM) information. Additional files attest details about build
infrastructure with  the [Supply-chain Levels for Software Artifacts
(SLSA)](https://slsa.dev/) provenance information.

The related files for Chainguard Libraries for JavaScript are located separately
from the registry and the packages themselves.

More tbd

From FAQ

* SBOMs are available in SPDX format in the `sbom.spdx.json` file.
* Provenance is available in the files: `putument.build.json`,
  `putument.publish.json`, `build.provenance.json`, `provenance.json` ,
  `rebuilder.provenance.json`, and  `source.provenance.json`.
