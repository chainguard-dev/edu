---
title: "Build Configuration"
linktitle: "Build Configuration  "
description: "Configuring Chainguard Libraries for JavaScript on your workstation"
type: "article"
date: 2025-06-05T09:00:00+00:00
lastmod: 2025-10-22T20:44:26+00:00
draft: false
tags: ["Chainguard Libraries", "JavaScript"]
menu:
  docs:
    parent: "javascript"
weight: 053
toc: true
contentType: "product-docs"
---

The configuration for the use of Chainguard Libraries depends on your build
tools, continuous integration, and continuous deployment setups.

At a high level adopting the use of Chainguard Libraries consists of the
following steps:

* Remove local caches on workstations and CI/CD pipelines. This step ensures that
  any libraries that were already sourced from other repositories are requested
  again and the version from Chainguard Libraries is used instead of other
  binaries.
* Change configuration to access Chainguard Libraries via your repository
  manager after the changes from the [global
  configuration](/chainguard/libraries/javascript/global-configuration/) are
  implemented.

These changes must be performed on all workstations of individual developers and
other engineers running relevant application builds. They must also be performed
on any build server such as Jenkins, TeamCity, GitHub or other infrastructure
that builds the applications or otherwise downloads and uses relevant libraries.

## JFrog Artifactory

Build configuration to retrieve artifacts from Artifactory typically requires
you to authenticate and use the identity token in the configuration of your
build tool.

Follow the steps from the [global
configuration](/chainguard/libraries/javascript/global-configuration/#jfrog-artifactory)
to determine URL and authentication details.

## Sonatype Nexus Repository

Build configuration to retrieve artifacts from Nexus may require authentication.
Use your username and password for Nexus in your build tool configuration.

Follow the steps from the [global
configuration](/chainguard/libraries/javascript/global-configuration/#sonatype-nexus-repository)
to determine URL and authentication details.

<a id="direct-access"></a>

## Direct access

Build configuration to retrieve artifacts **directly** from the Chainguard
Libraries for JavaScript repository at `https://libraries.cgr.dev/javascript/`
requires authentication with username and password from a pull token as detailed
in [access documentation](/chainguard/libraries/access/#pull-token).

<a id="npm"></a>

## npm

[npm](https://www.npmjs.com/) is the default package manager for Node.js, widely
used for managing JavaScript dependencies and scripts. It allows developers to
install, share, and manage packages for their projects. For more details, see
the [npm documentation](https://docs.npmjs.com/).

With npm, you declare JavaScript package dependencies in a `package.json` file
and separated into development and runtime dependencies. The following snippet
shows a minimal example with a couple of dependencies each:

```json
{
  "dependencies": {
    "@emotion/react": "^11.14.0",
    "@emotion/styled": "^11.14.0",
    "@fontsource/roboto": "^5.1.1",
    "node": "^22.18.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-router-dom": "^7.1.5",
  },
  "devDependencies": {
    "@eslint/js": "^9.14.0",
    "@types/react": "^18.3.18",
    "@types/react-dom": "^18.3.5"
  }
}
```

By default, npm retrieves packages from the npm Registry at
`https://registry.npmjs.org` and stores them locally in the `node_modules`
directory of the project after running `npm install`. This operation also
creates the `package-lock.json` file. 

Note that dependency versions are typically declared with the `^` before the
version string. This indicates higher, compatible versions, following the
semantic versioning scheme of the package are used automatically. For example,
the declaration of version `^22.18.0` for `node`, actually results in the use of
version `22.20.0` or even a higher version once available and npm install is
run.  

Any dependency or dependency version changes require another install and
therefore an update to the lock file. The lock file also encodes the checksum
values in the `integrity` field and the download URL in the `resolved` field for
each module.

To change a project to use Chainguard Libraries for JavaScript, set the registry
URL to point to your repository manager in your user `.npmrc` file: 

```shell
npm config set registry https://repo.example.com:8443/repository/javascript-all/
```

The command results in the following line in the `.npmrc` file:

```properties
registry=https://repo.example.com:8443/repository/javascript-all/
```

Refer to the [`npmrc`
documentation](https://docs.npmjs.com/cli/v11/configuring-npm/npmrc) for
alternative configurations, for example per project or globally, and details for
configuring authentication.

Example URLs:

* JFrog Artifactory: https://example.jfrog.io/artifactory/javascript-all/
* Sonatype Nexus: https://repo.example.com:8443/repository/javascript-all/
* Direct access: https://libraries.cgr.dev/javascript/

To change the packages, remove the `node_modules` directory and the
`package-lock.json` file and run the `npm install` command again. 

Now you can proceed with your development and testing. 

<a id="pnpm"></a>

## pnpm

[pnpm](https://pnpm.io/) is a fast, disk space-efficient package manager for
JavaScript, designed as an alternative to npm and Yarn. For
more information, see the [pnpm documentation](https://pnpm.io/motivation).

With pnpm, you declare JavaScript package dependencies in a `package.json` file
and separated into development and runtime dependencies. The following snippet
shows a minimal example with a couple of dependencies each:

```json
{
  "dependencies": {
    "@emotion/react": "^11.14.0",
    "@emotion/styled": "^11.14.0",
    "@fontsource/roboto": "^5.1.1",
    "node": "^22.18.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-router-dom": "^7.1.5",
  },
  "devDependencies": {
    "@eslint/js": "^9.14.0",
    "@types/react": "^18.3.18",
    "@types/react-dom": "^18.3.5"
  }
}
```

By default, pnpm retrieves the packages the npm Registry at
`https://registry.npmjs.org` and stores them locally in the `node_modules`
directory of the project after running `pnpm install`. This operation also
creates the `pnpm-lock.yaml` file. 

Note that dependency versions are typically declared with the `^` before the
version string. This indicates higher, compatible versions, following the
semantic versioning scheme of the package, are used automatically. For example,
the declaration of version `^22.18.0` for `node`, actually results in the use of
version `22.20.0` or even a higher version once available and pnpm install is
run.  

Any dependency or dependency version changes require another install and
therefore an update to the lock file. The lock file also encodes the checksum
values in the `integrity` field and other information for each module.

To change a project to use Chainguard Libraries for JavaScript, set the registry
URL to point to your repository manager in your user `.npmrc` file: 

```shell
pnpm config set registry https://repo.example.com:8443/repository/javascript-all/
```

The command results in the following line in the `.npmrc` file:

```properties
registry=https://repo.example.com:8443/repository/javascript-all/
```

Refer to the [pnpm registry
documentation](https://pnpm.io/settings#registry--authentication-settings) for
alternative configurations, for example per project or globally, and details for
configuring authentication.

Example URLs:

* JFrog Artifactory: https://example.jfrog.io/artifactory/javascript-all/
* Sonatype Nexus: https://repo.example.com:8443/repository/javascript-all/
* Direct access: https://libraries.cgr.dev/javascript/

To change the packages, remove the `node_modules` directory and the
`pnpm-lock.yaml` file and run the `pnpm install` command again. 

Now you can proceed with your development and testing. 

### Minimal example project

Use the following steps to create a minimal example project for pnpm  with
Chainguard Libraries for JavaScript.

```shell
mkdir pnpm-example
cd pnpm-example
pnpm init
```

For testing purposes, you can use direct access and environment variables as
detailed in the [access documentation](/chainguard/libraries/access/#env). Once
the environment variables are set, the following steps configure registry
access with authentication in the `.npmrc` file in the current project
directory:

```shell
export token=$(echo -n "${CHAINGUARD_JAVASCRIPT_IDENTITY_ID}:${CHAINGUARD_JAVASCRIPT_TOKEN}" | base64 -w 0)

pnpm config set registry https://libraries.cgr.dev/javascript/ --location=project
pnpm config set //libraries.cgr.dev/javascript/:_auth "${token}" --location=project
```

Add dependencies for your project into the `package.json` file to test retrieval
from Chainguard Libraries:

```shell
pnpm add commander@4.1.1
pnpm install
pnpm list
```

Following this, you find the downloaded package in
`node_modules/.pnpm/commander@4.1.1`. The commands also result in the creation
of the lock file `pnpm-lock.yaml`.

Adjust the registry configuration to use your repository manager and any other
desired packages for further testing.

<a id="yarn"></a>

## Yarn

[Yarn](https://yarnpkg.com/) is a popular package manager for JavaScript
projects, offering fast, reliable, and secure dependency management as an
alternative to npm. It is widely used for managing
project dependencies, scripts, and workflows in Node.js and other JavaScript
development environments. For more details, refer to the [Yarn
documentation](https://yarnpkg.com/getting-started). 

This section applies to modern versions of Yarn, also known as Yarn Berry, with
versions 2.x and higher. If you are using Yarn 1.x refer to the [Yarn Classic
section](#yarn-classic).

With Yarn, you declare JavaScript package dependencies in a `package.json` file
and separated into different scoped dependencies such as development and runtime
dependencies. The following block shows a minimal example with `react` and
`node` as main runtime dependencies and `eslint` as development dependency:

```json
{
  "name": "yarn-berry-example",
  "packageManager": "yarn@4.10.3",
  "dependencies": {
    "node": "^22.20.0",
    "react": "^19.1.1"
  },
  "devDependencies": {
    "eslint": "^9.36.0"
  }
}
```
By default, Yarn retrieves the packages from the registry at
`https://registry.yarnpkg.com` and stored locally folder `.yarn` in the users
home directory after running `yarn`. Specific packages are linked into the
project. This operation also creates the `yarn.lock` file.

Note that dependency versions are typically declared with the `^` before the
version string. This indicates higher, compatible versions, following the
semantic versioning scheme of the package, are used automatically. For example,
the declaration of version `^22.18.0` for `node`, actually results in the use of
version `22.20.0` or even a higher version once available and `yarn` is run.  

Any dependency or dependency version changes require another install and
therefore an update to the lock file. The lock file also encodes the checksum
values in the `checksum` field.

To change a project to use Chainguard Libraries for JavaScript, set the registry
URL to point to your repository manager in your project `.yarnrc.yml` file: 

```shell
yarn config set npmRegistryServer https://repo.example.com:8443/repository/javascript-all/
```

The command results in the following line in the `.yarnrc.yml` file:

```
npmRegistryServer: "https://repo.example.com:8443/repository/javascript-all/"
```

Refer to the [`config set` documentation](https://yarnpkg.com/cli/config/set) for
more details such as authentication support.

Example URLs:

* JFrog Artifactory: https://example.jfrog.io/artifactory/javascript-all/
* Sonatype Nexus: https://repo.example.com:8443/repository/javascript-all/
* Direct access: https://libraries.cgr.dev/javascript/

To change the packages, run the `yarn` command again. This forces an updated of
all packages from the new registry and regeneration of the lock file.

Now you can proceed with your development and testing. 

<a id="yarn-classic"></a>

## Yarn Classic

[Yarn Classic](https://classic.yarnpkg.com/) is the legacy 1.x release of
[Yarn](#yarn).

With Yarn, you declare JavaScript package dependencies in a `package.json` file
and separated into different scoped dependencies such as development and runtime
dependencies. The following block shows a minimal example with `react` and
`node` as main runtime dependencies and `eslint` as development dependency:

```json
{
  "name": "yarn-classic-example",
  "version": "1.0.0",
  "description": "A minimal example project for using yarn classic",
  "main": "index.js",
  "author": "Chainguard",
  "license": "MIT",
  "private": false,
  "dependencies": {
    "node": "^22.18.0",
    "react": "^19.1.1"
  },
  "devDependencies": {
    "eslint": "^9.36.0"
  }
}
```

By default, Yarn retrieves the packages from the registry at
`https://registry.yarnpkg.com` and stores them locally in the `node_modules`
directory of the project after running `yarn`. This operation also creates the
`yarn.lock` file.

Note that dependency versions are typically declared with the `^` before the
version string. This indicates higher, compatible versions, following the
semantic versioning scheme of the package, are used automatically. For example,
the declaration of version `^22.18.0` for `node`, actually results in the use of
version `22.20.0` or even a higher version once available and `yarn` is run.  

Any dependency or dependency version changes require another install and
therefore an update to the lock file. The lock file also encodes the checksum
values in the `integrity` field and the download URL in the `resolved` field for
each module.

To change a project to use Chainguard Libraries for JavaScript, set the registry
URL to point to your repository manager in your user `.yarnrc` file: 

```shell
yarn config set registry https://repo.example.com:8443/repository/javascript-all/
```

The command results in the following line in the `.yarnrc` file:

```
registry "https://repo.example.com:8443/repository/javascript-all/"
```

Refer to the [`.yarnrc`
documentation](https://classic.yarnpkg.com/lang/en/docs/yarnrc/) for more
details.

Example URLs:

* JFrog Artifactory: https://example.jfrog.io/artifactory/javascript-all/
* Sonatype Nexus: https://repo.example.com:8443/repository/javascript-all/
* Direct access: https://libraries.cgr.dev/javascript/

To change the packages, remove the `node_modules` directory and the `yarn.lock`
file and run the `yarn` command again. This forces a new download of all
packages from the new registry and regeneration of the lock file. Alternatively,
you can run `yarn upgrade` to update all dependencies to their latest allowed
versions and regenerate the lock file.

Now you can proceed with your development and testing. 


<a id="bun"></a>

## Bun

[Bun](https://bun.com/) is a fast, all-in-one JavaScript runtime, bundler, and
package manager designed as an alternative to Node.js tooling. It provides an
integrated package manager that is compatible with the npm ecosystem.

With Bun you declare dependencies in a `package.json` file just like
[npm](#npm). The following snippet shows a minimal example:

```json
{
  "dependencies": {
    "@emotion/react": "^11.14.0",
    "@emotion/styled": "^11.14.0",
    "@fontsource/roboto": "^5.1.1",
    "node": "^22.18.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-router-dom": "^7.1.5"
  },
  "devDependencies": {
    "@eslint/js": "^9.14.0",
    "@types/react": "^18.3.18",
    "@types/react-dom": "^18.3.5"
  }
}
```

By default Bun installs packages from the npm Registry at
`https://registry.npmjs.org` and stores them locally in the `node_modules`
directory after running `bun install`. Bun creates a binary lockfile named
`bun.lock` to record resolved versions and checksums.

Note that dependency versions are typically declared with `^` to allow
compatible newer releases under semantic versioning. For example, `^22.18.0` for
`node` can result in `22.20.0` or higher when `bun install` runs.

Any dependency or version changes require running `bun install` again, which
updates the lockfile.

To switch a project to use Chainguard Libraries for JavaScript, point Bun at
your repository manager. Add the [registry
configuration](https://bun.com/docs/runtime/bunfig#install-registry) to the
`bunfig.toml` file of your project: `

```toml
[install]
# set default registry as a string
registry = "https://repo.example.com:8443/repository/javascript-all/"
```

Alternatively you can use an [`.npmrc` file](#npm)

You can also temporarily override for install:

```shell
bun install --registry=https://repo.example.com:8443/repository/javascript-all/
```

Refer to [Bun documentation]() for additional registry and authentication options.

Example registry URLs:

* JFrog Artifactory: https://example.jfrog.io/artifactory/javascript-all/
* Sonatype Nexus: https://repo.example.com:8443/repository/javascript-all/
* Direct access: https://libraries.cgr.dev/javascript/

To apply the registry change to an existing project, remove `node_modules` and
the `bun.lock` file and run:

```shell
bun install
```

This forces packages to be re-fetched from the configured registry and
regenerates the lockfile. Now you can continue development and testing with
Chainguard Libraries.
