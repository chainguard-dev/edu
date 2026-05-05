---
title: "Build configuration"
linktitle: "Build configuration"
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
---

The configuration for the use of Chainguard Libraries depends on your build
tools, continuous integration, and continuous deployment setups.

At a high level, adopting Chainguard Libraries consists of the
following steps:

* Remove local caches on workstations and CI/CD pipelines. This step ensures that
  any libraries that were already sourced from upstream repositories are requested
  again, and the version from Chainguard Libraries is used instead.
* Change configuration to access Chainguard Libraries via your repository
  manager after the changes from the [global
  configuration](/chainguard/libraries/javascript/global-configuration/) are
  implemented, or via direct access.

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

See the minimal example projects on this page for demonstrations using direct access for each build tool.

> Note: Direct access requires per-project and per-workstation configuration.
For organizations with multiple teams, proxying through an artifact manager is
recommended. See the [global
configuration](/chainguard/libraries/javascript/global-configuration/) for setup
guides.

## Updating lockfile hashes for existing projects

> **Note**: `chainctl libraries update-hashes` does not currently support authentication through a repository manager. You will need to configure [direct access](#direct-access) credentials before running the command.

If you are migrating an existing JavaScript project to Chainguard Libraries,
your lockfile likely contains integrity hashes generated against the npm
registry. Because Chainguard rebuilds packages in a secured build environment rather than distributing upstream artifacts directly, the resulting checksums differ even for identical package versions; they must be updated before reinstalling.

Use the following command, in the directory containing the lockfile, to update hashes in place across all supported lockfile formats (`package-lock.json`, `yarn.lock`,
`pnpm-lock.yaml`, `bun.lock`) without regenerating the lockfile from scratch:

```bash
chainctl libraries update-hashes
```

After running the command, ensure your `.npmrc` is configured with Chainguard
credentials, then reinstall to apply the updated hashes. The `chainctl libraries update-hashes` command will output
a "Next steps" section that includes the tool-specific command for reinstalling.

> **Note:** If your organization uses the [Chainguard Repository with upstream
> npm fallback
> enabled](/chainguard/libraries/javascript/overview/#upstream-fallback-policy-and-controls),
> packages that resolve through the upstream registry may still point to
> `registry.npmjs.org` in your lockfile after running `chainctl libraries
> update-hashes`. These packages are not automatically redirected to route
> through Chainguard. To fully migrate these packages, update their resolved
> URLs to use `libraries.cgr.dev/javascript-upstream/` manually.

<a id="npm"></a>

## npm

[npm](https://www.npmjs.com/) is the default package manager for Node.js, widely
used for managing JavaScript dependencies and scripts. It allows developers to
install, share, and manage packages for their projects. For more details, see
the [npm documentation](https://docs.npmjs.com/).

**Declare dependencies in package.json**

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
version `22.20.0` or even a higher version once available and `npm install` is
run.  

Any dependency or dependency version changes require another install and
therefore an update to the lock file. The lock file also encodes the checksum
values in the `integrity` field and the download URL in the `resolved` field for
each module.

**Direct access: Point registry to Chainguard**

To change a project to use Chainguard Libraries for JavaScript, set the registry
URL to point to Chainguard in your user `.npmrc` file: 

```bash
npm config set registry https://libraries.cgr.dev/javascript/
```


### Using a repository manager

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

* JFrog Artifactory: `https://example.jfrog.io/artifactory/javascript-all/`
* Sonatype Nexus: `https://repo.example.com:8443/repository/javascript-all/`
* Direct access: `https://libraries.cgr.dev/javascript/`

### Apply registry changes

To apply the registry changes, remove the `node_modules` directory and the
`package-lock.json` file and run the `npm install` command again. This re-fetches all
packages from Chainguard and regenerates the lockfile with updated hashes.

If you encounter stale or corrupted package data, clear the cache with:

```bash
npm cache clean --force
```

To verify the cache is empty:

```bash
npm cache verify
```

### Update lockfile hashes

If you are migrating an existing project and want to preserve your current
lockfile, use [`chainctl libraries update-hashes`](#updating-lockfile-hashes-for-existing-projects)
to update only the integrity hashes in place instead.

Now you can proceed with your development and testing. 

### Using private npm packages alongside Chainguard Repository

If your organization publishes its own packages to the public npm Registry under
a scoped prefix (for example, `@your-org/package-name`), you may want those
packages to be fetched directly from npm rather than going through the
[Chainguard Repository](/chainguard/libraries/chainguard-repository/); for
example, to bypass the cooldown period for packages you own and trust.

npm supports per-scope registry configuration, which lets you route packages
with a specific prefix to a different registry:

```
# .npmrc
registry=https://libraries.cgr.dev/javascript/
//libraries.cgr.dev/javascript/:_auth=${token}

@your-org:registry=https://registry.npmjs.org/
```

However, npm has a behavior where, when it fetches package metadata from a
scoped registry, it may rewrite the resolved tarball URL in the lockfile to use
the primary registry host (in this case, Chainguard Repository) instead of the
scoped registry. This causes subsequent `npm install` runs to attempt to fetch
your scoped packages from Chainguard Repository, resulting in a 404 or
authentication error.

To prevent this, add the following line to your `.npmrc`:

```
replace-registry-host=never
```

This tells npm never to rewrite the registry host in resolved URLs, so scoped
packages remain associated with their correct upstream registry in the lockfile.

After adding this line, verify your lockfile reflects the
correct resolved URLs: scoped packages should resolve to `registry.npmjs.org`
and all other packages should resolve to `libraries.cgr.dev/javascript`.


<a id="npm-minimal"></a>

### Minimal example project

For testing purposes, you can use direct access and environment variables as
detailed in the [access documentation](/chainguard/libraries/access/#env). 

**1. Create a JavaScript project**

Use the following steps to create a minimal example project for npm with
Chainguard Libraries for JavaScript.

```shell
mkdir npm-example
cd npm-example
npm init -y
```

**2. Configure the .npmrc file**

Once the environment variables are set, configure the `.npmrc` file. 

Run the following command to configure registry
access and authentication in the `.npmrc` file in the current project
directory:

```shell
chainctl auth configure-npm
```

[This command](/chainguard/chainctl/chainctl-docs/chainctl_auth_configure-npm/) writes a project-level `.npmrc` with the registry URL and base64-encoded credentials. It also prints the equivalent `npm config set` commands for use in CI or other environments where you need to configure `.npmrc` manually. If this command returns an error, ensure that you are using the [latest version of `chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/#updating-chainctl).

Alternatively, you can configure the `.npmrc` file manually:

{{< details "Configure .npmrc manually" >}}
The following steps configure registry
access with authentication in the `.npmrc` file in the current project
directory:

```shell
export token=$(echo -n "${CHAINGUARD_JAVASCRIPT_IDENTITY_ID}:${CHAINGUARD_JAVASCRIPT_TOKEN}" | base64 -w 0)

npm config set registry https://libraries.cgr.dev/javascript/ --location=project
npm config set //libraries.cgr.dev/javascript/:_auth "${token}" --location=project
```

Note that the trailing slash in the registry URL is required, and that setting
`username` and `_password` instead of `auth` with a token does not work with
npm. The `-w 0` option for `base64` is required and supported by the GNU
coreutils versions included in most operating systems.
{{< /details >}}

**Example .npmrc file**

```
registry=https://libraries.cgr.dev/javascript/
//libraries.cgr.dev/javascript/:_auth=aWRlbnRpdHktaWQ6dG9rZW4=
```
The value of `auth` is the base64 encoding of `identity-id:token`, including the `/` character in the username.

**3. Verify authentication with npm ping**

Before installing packages, you can verify that authentication is configured correctly by running:

```bash
npm ping --userconfig .npmrc
```

A successful respoonse looks like:
```bash
npm notice PING https://libraries.cgr.dev/javascript/
npm notice PONG 1065ms
```

The PONG response confirms that your credentials are valid and the registry is reachable. If the command fails, check that the .npmrc file exists in the current directory and that your token has not expired.

**4. Add dependencies and build the project**

Add dependencies for your project into the `package.json` file to test retrieval
from Chainguard Libraries, build the project, and list the dependencies:

```shell
npm add commander@4.1.1
npm install
npm list
```

Following this, find the downloaded package in `node_modules/commander`. The
commands also result in the creation of the lock file `package-lock.json`, which
contains the source URL for each package in the `resolved` field.

Adjust the registry configuration to use your repository manager and add any
other desired packages for further testing.

<a id="pnpm"></a>

## pnpm

[pnpm](https://pnpm.io/) is a fast, disk space-efficient package manager for
JavaScript, designed as an alternative to npm and Yarn. For
more information, see the [pnpm documentation](https://pnpm.io/motivation).

**Declare dependencies in package.json**

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

**Direct access: Point registry to Chainguard**

To change a project to use Chainguard Libraries for JavaScript, set the registry
URL to point to Chainguard in your user `.npmrc` file: 

```bash
pnpm config set registry https://libraries.cgr.dev/javascript/
```

### Using a repository manager 

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

* JFrog Artifactory: `https://example.jfrog.io/artifactory/javascript-all/`
* Sonatype Nexus: `https://repo.example.com:8443/repository/javascript-all/`
* Direct access: `https://libraries.cgr.dev/javascript/`

### Apply registry changes

To apply the registry change, remove the `node_modules` directory and the
`pnpm-lock.yaml` file and run the `pnpm install` command again. This re-fetches all
packages from Chainguard and regenerates the lockfile with updated hashes.

pnpm has two separate layers of cached data. If you encounter stale or corrupted package data, you can clear both of these caches:

{{< details "Clear pnpm caches" >}}

There is an [experimental command](https://pnpm.io/cli/cache-delete) to delete the metadata cache:

```bash
pnpm cache delete
```

To find and manually remove the full store:

```bash
pnpm store path
```

Then delete the directory that command outputs: 

On macOS/Linux - 

```bash
rm -rf "$(pnpm store path)"
```

On Windows - 

Use the path returned by `pnpm store path` and delete it via File Explorer or `rmdir`.

> Note: pnpm prune removes unused tarballs but does not remove packument metadata. If you are seeing 404 errors after switching to or updating the Chainguard registry endpoint, use the commands above rather than pnpm prune.

{{< /details >}}

### Update lockfile hashes

If you are migrating an existing project and want to preserve your current
lockfile, use [`chainctl libraries update-hashes`](#updating-lockfile-hashes-for-existing-projects)
to update only the integrity hashes in place instead.

Now you can proceed with your development and testing. 

<a id="pnpm-minimal"></a>

### Minimal example project

Use the following steps to create a minimal example project for pnpm with
Chainguard Libraries for JavaScript.

```shell
mkdir pnpm-example
cd pnpm-example
pnpm init
```

For testing purposes, you can use direct access and environment variables as
detailed in the [access documentation](/chainguard/libraries/access/#env). 

Once
the environment variables are set, the following steps configure registry
access and authentication in the `.npmrc` file in the current project
directory:

```shell
chainctl auth configure-npm --pull-token
```

[This command](/chainguard/chainctl/chainctl-docs/chainctl_auth_configure-npm/) creates a pull token (valid for 30 days by default) scoped to your organization and writes a project-level `.npmrc` with the registry URL and base64-encoded credentials. If this command returns an error, ensure that you are using the [latest version of `chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/#updating-chainctl).

Add dependencies for your project into the `package.json` file to test retrieval
from Chainguard Libraries, build the project, and list the dependencies:

```shell
pnpm add commander@4.1.1
pnpm install
pnpm list
```

Following this, find the downloaded package in
`node_modules/.pnpm/commander@4.1.1` and `node_modules/commander`. The commands
also result in the creation of the lock file `pnpm-lock.yaml`, which contains
the source URL for each package in the `tarball` field.

Adjust the registry configuration to use your repository manager and add any
other desired packages for further testing.

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

**Declare dependencies in package.json**

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
`https://registry.yarnpkg.com` and stores them locally in the `.yarn` folder in the user's
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

**Direct access: Point registry to Chainguard**

To change a project to use Chainguard Libraries for JavaScript, set the registry
URL to point to Chainguard in your user `.yarnrc` file: 

```bash
yarn config set npmRegistryServer https://libraries.cgr.dev/javascript/
```

### Using a repository manager

To change a project to use Chainguard Libraries for JavaScript, set the registry
URL to point to your repository manager in your project `.yarnrc.yml` file: 

```shell
yarn config set npmRegistryServer https://repo.example.com:8443/repository/javascript-all
```

The command results in the following line in the `.yarnrc.yml` file:

```
npmRegistryServer: "https://repo.example.com:8443/repository/javascript-all"
```

Refer to the [`config set` documentation](https://yarnpkg.com/cli/config/set) for
more details such as authentication support.

Example URLs:

* JFrog Artifactory: `https://example.jfrog.io/artifactory/javascript-all`
* Sonatype Nexus: `https://repo.example.com:8443/repository/javascript-all`
* Direct access: `https://libraries.cgr.dev/javascript`

### Apply registry changes

To apply the registry change, run the `yarn` command again. This forces an update of
all packages from the new registry and regeneration of the lock file.

If you encounter stale or corrupted package data, clear the cache with:

```bash
yarn cache clean --all
```

### Update lockfile hashes

If you are migrating an existing project and want to preserve your current
lockfile, use [`chainctl libraries update-hashes`](#updating-lockfile-hashes-for-existing-projects)
to update only the integrity hashes in place instead.

Now you can proceed with your development and testing. 

<a id="yarn-berry-minimal"></a>

### Minimal example project

Use the following steps to create a minimal example project for yarn with
Chainguard Libraries for JavaScript. The script sets the policy to use the
latest stable release of Yarn.

```shell
mkdir yarn-berry-example
cd yarn-berry-example
yarn policies set-version stable
yarn init
```

For testing purposes, you can use direct access and environment variables as
detailed in the [access documentation](/chainguard/libraries/access/#env). Once
the environment variables are set, the following steps configure registry
access with authentication in the `.yarnrc.yml` file in the current project
directory:

```shell
export authInfo="${CHAINGUARD_JAVASCRIPT_IDENTITY_ID}:${CHAINGUARD_JAVASCRIPT_TOKEN}"

yarn config set npmRegistryServer https://libraries.cgr.dev/javascript
yarn config set 'npmRegistries["//libraries.cgr.dev/javascript"].npmAuthIdent' "${authInfo}"
yarn config set 'npmRegistries["//libraries.cgr.dev/javascript"].npmAlwaysAuth' "true"
```

Note the following details:

* The `authInfo` token is passed as authentication identity `npmAuthIdent` and only uses 
  the username and password values from the pull token separated by colon without any further encoding.
* Setting `npmAlwaysAuth` is required.

Add dependencies for your project into the `package.json` file to test retrieval
from Chainguard Libraries, build the project, and list the dependencies:

```shell
yarn add commander@4.1.1
yarn install
yarn info
```

Following this, find the downloaded package in the local shared cache. The
commands also result in the creation of the lock file `yarn.lock`, which
contains the source URL for each package in the `archiveUrl` parameter of the
`resolution` field.

Adjust the registry configuration to use your repository manager and add any
other desired packages for further testing.

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

**Direct access: Point registry to Chainguard**

To change a project to use Chainguard Libraries for JavaScript, first export your pull token as base64-encoded environment variables:

```bash
export token=$(echo -n "${CHAINGUARD_JAVASCRIPT_IDENTITY_ID}:${CHAINGUARD_JAVASCRIPT_TOKEN}" | base64 -w 0)
```

Then, set auth and set the registry URL to point to Chainguard in your user `.npmrc` file: 

```bash
cat > .npmrc << 'EOF'
registry=https://libraries.cgr.dev/javascript/
//libraries.cgr.dev/javascript/:_auth="$token"
//libraries.cgr.dev/javascript/:always-auth=true
EOF
```

### Using a repo manager

To change a project to use Chainguard Libraries for JavaScript, set the registry
URL to point to your repository manager in your `.npmrc` file:

```
cat > .npmrc << EOF
registry=https://repo.example.com:8443/repository/javascript-all
EOF
```

Example URLs:

* JFrog Artifactory: `https://example.jfrog.io/artifactory/javascript-all`
* Sonatype Nexus: `https://repo.example.com:8443/repository/javascript-all`
* Direct access: `https://libraries.cgr.dev/javascript`


### Apply registry changes

Note that you can also use the `yarn config set registry` command to set the
registry in the `.yarnrc` file, however this approach does not support
authentication as typically required for repository managers as well as for
direct access to Chainguard Libraries for JavaScript.

Refer to the [`.yarnrc`
documentation](https://classic.yarnpkg.com/lang/en/docs/yarnrc/) for more
details.

To apply the registry change, remove the `node_modules` directory and the `yarn.lock`
file and run the `yarn` command again. This forces a new download of all
packages from the new registry and regeneration of the lock file. Alternatively,
you can run `yarn upgrade` to update all dependencies to their latest allowed
versions and regenerate the lock file.

If you encounter stale or corrupted package data, clear the cache with:

```bash
yarn cache clean
```

### Update lockfile hashes

If you are migrating an existing project and want to preserve your current
lockfile, use [`chainctl libraries update-hashes`](#updating-lockfile-hashes-for-existing-projects)
to update only the integrity hashes in place instead.

Now you can proceed with your development and testing. 

<a id="yarn-classic-minimal"></a>

### Minimal example project

Use the following steps to create a minimal example project for yarn with
Chainguard Libraries for JavaScript.

```shell
mkdir yarn-classic-example
cd yarn-classic-example
yarn init -y
```

For testing purposes, you can use direct access and environment variables as
detailed in the [access documentation](/chainguard/libraries/access/#env). Once
the environment variables are set, the following steps configure registry access
with authentication in the `.npmrc` file directory:

```shell
export token=$(echo -n "${CHAINGUARD_JAVASCRIPT_IDENTITY_ID}:${CHAINGUARD_JAVASCRIPT_TOKEN}" | base64 -w 0) 
cat > .npmrc << EOF
registry=https://libraries.cgr.dev/javascript/
//libraries.cgr.dev/javascript/:_auth="$token"
//libraries.cgr.dev/javascript/:always-auth=true
EOF
```

Note the following details:

* Using yarn configuration files such as `.yarnrc` and commands like `yarn
  config set registry` does not work with authentication details, and the
  proposed approach with `.npmrc` file is preferable. 
* The `token` token is passed as authentication token `_auth` and uses the
  username and password values from the pull token separated by colon in
  `base64` encoding. Note that the `-w 0` option for `base64` is required and
  supported by the GNU coreutils versions included in most operating systems. 
* Setting `always-auth` is required.
* The trailing slash in the registry URL and authentication references to it is required.

Add dependencies for your project into the `package.json` file to test retrieval
from Chainguard Libraries, build the project, and list the dependencies:

```shell
yarn add commander@4.1.1
yarn install
yarn list
```

Following this, find the downloaded package in the `node_modules` directory.
The commands also result in the creation of the lock file `yarn.lock`, which
contains the source URL for each package in the `resolved` field.

Adjust the registry configuration to use your repository manager and add any
other desired packages for further testing.

<a id="bun"></a>

## Bun

[Bun](https://bun.com/) is a fast, all-in-one JavaScript runtime, bundler, and
package manager designed as an alternative to Node.js tooling. It provides an
integrated package manager that is compatible with the npm ecosystem.

**Declare dependencies in package.json**

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

### Using a repository manager 

To switch a project to use Chainguard Libraries for JavaScript, point Bun at
your repository manager. Add the [registry
configuration](https://bun.com/docs/runtime/bunfig#install-registry) to the
`bunfig.toml` file of your project: `

```toml
[install]
# set default registry as a string
registry = "https://repo.example.com:8443/repository/javascript-all/"
```

Alternatively you can use an [`.npmrc` file](#npm).

You can also temporarily override for install:

```shell
bun install --registry=https://repo.example.com:8443/repository/javascript-all/
```

Refer to [Bun documentation](https://bun.com/docs) for additional registry and authentication options.

Example registry URLs:

* JFrog Artifactory: https://example.jfrog.io/artifactory/javascript-all/
* Sonatype Nexus: https://repo.example.com:8443/repository/javascript-all/
* Direct access: https://libraries.cgr.dev/javascript/

### Apply registry changes

To apply the registry change to an existing project, remove `node_modules` and
the `bun.lock` file and run:

```shell
bun install
```

This forces packages to be re-fetched from the configured registry and
regenerates the lockfile. Now you can continue development and testing with
Chainguard Libraries.

<a id="bun-minimal"></a>

### Minimal example project

Use the following steps to create a minimal example project for bun with
Chainguard Libraries for JavaScript.

```shell
mkdir bun-example
cd bun-example
bun init -y
```

For testing purposes, you can use direct access and environment variables as
detailed in the [access documentation](/chainguard/libraries/access/#env). Once
the environment variables are set, the following steps configure registry
access with authentication in the `bunfig.toml` file in the current project
directory:

```shell
cat > bunfig.toml << EOF
[install.registry]
url = "https://libraries.cgr.dev/javascript/"
username = "$CHAINGUARD_JAVASCRIPT_IDENTITY_ID"
password = "$CHAINGUARD_JAVASCRIPT_TOKEN"
EOF
```

Note that the trailing slash in the registry URL is required.

Add dependencies for your project into the `package.json` file to test retrieval
from Chainguard Libraries, build the project, and list the dependencies:

```shell
bun add commander@4.1.1
bun install
bun pm ls
```

Following this, find the downloaded package in `node_modules/commander`. The
 commands also result in the creation of the lock file `bun.lock`, which
contains the source URL for each package in the `packages` section.

Adjust the registry configuration to use your repository manager and add any
other desired packages for further testing.
