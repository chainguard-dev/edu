---
title: "Build Configuration"
linktitle: "Build Configuration  "
description: "Configuring Chainguard Libraries for JavaScript on your workstation"
type: "article"
date: 2025-06-05T09:00:00+00:00
lastmod: 2025-09-11T20:11:49+00:00
draft: false
tags: ["Chainguard Libraries", "JavaScript"]
menu:
  docs:
    parent: "javascript"
weight: 053
toc: true
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

Using npm, dependencies to JavaScript packages are declared in a `package.json`
file and separated into development and runtime dependencies. The following
snippet shows a minimal example with a couple of dependencies each:

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

By default, the packages are retrieved from the npm Registry at
`https://registry.npmjs.org` and stored locally in the `node_modules` directory
after running `npm install`. This operation also creates the `package-lock.json`
file. 

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

To switch a project to use Chainguard Libraries for JavaScript, set the registry
URL to point to your repository manager in your user `.npmrc` file: 

```shell
npm config set registry https://repo.example.com:8443/repository/javascript-all/
```

The command results in the following line:

```properties
registry=https://repo.example.com:8443/repository/javascript-all/
```

Check the [npmrc
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
more information, see the [pnpm documentation](https://pnpm.io/).

Using pnpm, dependencies to JavaScript packages are declared in a `package.json`
file and separated into development and runtime dependencies. The following
snippet shows a minimal example with a couple of dependencies each:

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

By default, the packages are retrieved from the npm Registry at
`https://registry.npmjs.org` and stored locally in the `node_modules` directory
after running `pnpm install`. This operation also creates the `pnpm-lock.yaml`
file. 

Note that dependency versions are typically declared with the `^` before the
version string. This indicates higher, compatible versions, following the
semantic versioning scheme of the package are used automatically. For example,
the declaration of version `^22.18.0` for `node`, actually results in the use of
version `22.20.0` or even a higher version once available and pnpm install is
run.  

Any dependency or dependency version changes require another install and
therefore an update to the lock file. The lock file also encodes the checksum
values in the `integrity` field and other information for each module.

To switch a project to use Chainguard Libraries for JavaScript, set the registry
URL to point to your repository manager in your user `.npmrc` file: 

```shell
pnpm config set registry https://repo.example.com:8443/repository/javascript-all/
```

The command results in the following line:

```properties
registry=https://repo.example.com:8443/repository/javascript-all/
```

Check the [pnpm registry
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

<!--
<a id="yarn"></a>

## Yarn

[Yarn](https://yarnpkg.com/) is a popular package manager for JavaScript
projects, offering fast, reliable, and secure dependency management as an
alternative to npm. It is widely used for managing project dependencies,
scripts, and workflows in Node.js and other JavaScript development environments.
For more details, refer to the [Yarn
documentation](https://yarnpkg.com/getting-started/documentation). 

This section applies to modern versions of Yarn, also known as Yarn Berry, with
versions 2.x and higher.

```
yarn config set registry http://localhost:8081/repository/javascript-all/
```

for newer yarn

```
yarn config set npmRegistryServer http://localhost:8081/repository/javascript-all/
``` 

<a id="yarn-classic"></a>

## Yarn Classic

[Yarn Classic](https://classic.yarnpkg.com/) is the legacy release of Yarn using
versions 1.x.

-->
