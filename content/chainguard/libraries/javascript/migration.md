---
title: "Migrating a JavaScript Project to Chainguard Libraries"
type: "article"
linktitle: "Migrate to Chainguard"
description: "How to migrate an existing JavaScript project to pull dependencies from Chainguard Libraries"
date: 2025-05-27T00:00:00+00:00
lastmod: 2025-05-27T00:00:00+00:00
tags: ["Chainguard Libraries", "JavaScript"]
draft: false
images: []
menu:
  docs:
    parent: "getting-started"
weight: 056
toc: true
---

Chainguard Libraries for JavaScript provides a curated registry of npm packages
rebuilt from source, scanned for malware, and verified against the
[OSV database](https://osv.dev/). Because Chainguard Libraries uses the standard
npm registry protocol, switching an existing project requires only a registry
configuration change — no changes to your application code, `package.json`, or
dependency versions.

This guide walks through migrating an existing JavaScript project to Chainguard
Libraries, covering the two most common setups:

- **Direct access** — your build tool connects directly to `libraries.cgr.dev`.
  This option is faster for initial evaluation and smaller-scale setups.
- **Repository manager** — your build tool connects to a repository manager
  (such as JFrog Artifactory or Sonatype Nexus), which proxies requests to
  Chainguard Libraries. This option is recommended for teams and organizations.

## Prerequisites

Before you begin, you'll need:

- An existing JavaScript project with a `package.json` and a lockfile
  (`package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`, or `bun.lock`)
- [`chainctl` installed and authenticated](/chainguard/chainctl-usage/how-to-install-chainctl/)
- An [entitlement to Chainguard Libraries](/chainguard/chainctl/chainctl-docs/chainctl_libraries_entitlements_create/)
  for JavaScript

To create an entitlement to Chainguard Libraries for JavaScript, run:

```shell
chainctl libraries entitlements create --ecosystems=JAVASCRIPT
```

You can also configure [upstream fallback and cooldown policies](#packages-not-available-in-chainguard-libraries)
when creating the entitlement. For example, to enable upstream fallback with a
10-day cooldown:

```shell
chainctl libraries entitlements create --ecosystems=JAVASCRIPT \
  --policy=CHAINGUARD_AND_UPSTREAM --cooldown-days=10
```

### Pull token

If you plan to use a repository manager, or a non-interactive environment such
as CI/CD, you will need a pull token. You must be an Owner or have the
`libraries.javascript.pull_token_creator` permission to create one.

```shell
chainctl auth pull-token --repository=javascript
```

This outputs an identity ID and token, with a default expiration of 30 days.
Set them as environment variables:

```shell
export CHAINGUARD_JAVASCRIPT_IDENTITY_ID="<your-identity-id>"
export CHAINGUARD_JAVASCRIPT_TOKEN="<your-token>"
```

> **Do not commit credentials to version control.** Configuration files
> generated with a literal token value — such as `.npmrc` files written by
> `chainctl auth configure-npm --pull-token` — should not be committed to a
> repository, especially a public one. Add these files to `.gitignore`, and
> store tokens as CI secrets referenced via environment variables instead. If
> you accidentally commit credentials, [delete the exposed
> token](/chainguard/libraries/access/#pull-token-management).

### Audit your current registry configuration

Before making changes, identify where your current registry is configured. npm
and other JavaScript build tools can read registry settings from several
locations — a project-level `.npmrc`, a user-level `~/.npmrc`, environment
variables, or a repository manager — and you may have configuration in more than
one place.

To see all currently active npm configuration and where each value comes from:

```shell
npm config list
```

The `registry` line shows where packages are currently being fetched from. If no
registry is set, npm fetches from `https://registry.npmjs.org` by default.

If you don't have an `.npmrc` file yet, that's fine; you'll create one in the
next step.

## Step 1: Configure authentication and registry

How you configure the registry depends on your environment. Follow the
instructions that match your setup.

> **Choosing what account to use:** For individual evaluation, your personal
> credentials are sufficient. For shared environments, CI/CD pipelines, or team
> rollouts, use a dedicated service account or machine identity rather than a
> personal account. This simplifies token rotation, provides cleaner audit logs,
> and avoids builds breaking if someone leaves the organization.

### Direct access

Session-based authentication is the preferred option when your environment can
use your current Chainguard session or an assumable identity. This keeps
credentials short-lived and avoids passing around static tokens.

#### Local development

For npm, run the following command to write a project-level `.npmrc` with the
registry URL and credentials from your current Chainguard session:

```shell
chainctl auth configure-npm
```

Because [this command](/chainguard/chainctl/chainctl-docs/chainctl_auth_configure-npm/) uses a session-backed bearer token, you will need to re-run it when the token expires. If the command returns an error, ensure you are
using the [latest version of chainctl](/chainguard/chainctl-usage/how-to-install-chainctl/#updating-chainctl).

#### CI/CD and automated environments

For CI/CD environments, [assumable identities](/chainguard/administration/assumable-ids/assumable-ids/)
are the recommended approach. Rather than managing a static token, an assumable
identity lets your CI/CD workload authenticate directly with Chainguard using
its own platform identity; no long-lived credentials to rotate or accidentally
expose.

Once configured, authenticate and write the registry configuration in your
pipeline. For example, in a GitHub Actions workflow using npm:

```yaml
steps:
  - uses: chainguard-dev/setup-chainctl@main
    with:
      identity: "<identity-id>"
  - run: chainctl auth configure-npm
```

For pnpm, Yarn, and Bun, authenticate the workload then apply the
[tool-specific registry configuration](#manual-registry-configuration).

#### Pull token authentication

If your platform does not support assumable identities, you can use a static pull token.

For npm:

```shell
chainctl auth configure-npm --pull-token
```

This generates a project-level `.npmrc` with a pull token.

For pnpm, Yarn Berry, Yarn Classic, and Bun:

First create a pull token as described in the [prerequisites](#pull-token), then configure your build tool manually using the instructions below.

{{< details "Configure registry manually for pnpm, Yarn, and Bun" >}}

> **Note:** The following commands use environment variables to supply
> credentials at runtime. Writing credentials to a local configuration file
> should still be treated as sensitive regardless of the form used. Generate
> credentials at build time where possible, add configuration files to
> `.gitignore` if needed, and store secrets in your CI/CD platform rather than
> in version control.

**pnpm**

```shell
export token=$(echo -n "${CHAINGUARD_JAVASCRIPT_IDENTITY_ID}:${CHAINGUARD_JAVASCRIPT_TOKEN}" | base64 -w 0)

pnpm config set registry https://libraries.cgr.dev/javascript/ --location=project
pnpm config set //libraries.cgr.dev/javascript/:_auth "${token}" --location=project
```

Alternatively, use username and password directly to avoid `base64` encoding
differences across platforms:

```shell
pnpm config set //libraries.cgr.dev/javascript/:username "${CHAINGUARD_JAVASCRIPT_IDENTITY_ID}" --location=project
pnpm config set //libraries.cgr.dev/javascript/:_password "${CHAINGUARD_JAVASCRIPT_TOKEN}" --location=project
```

**Yarn Berry (2.x+)**

```shell
export authInfo="${CHAINGUARD_JAVASCRIPT_IDENTITY_ID}:${CHAINGUARD_JAVASCRIPT_TOKEN}"

yarn config set npmRegistryServer https://libraries.cgr.dev/javascript
yarn config set 'npmRegistries["//libraries.cgr.dev/javascript"].npmAuthIdent' "${authInfo}"
yarn config set 'npmRegistries["//libraries.cgr.dev/javascript"].npmAlwaysAuth' "true"
```

**Yarn Classic (1.x)**

```shell
export token=$(echo -n "${CHAINGUARD_JAVASCRIPT_IDENTITY_ID}:${CHAINGUARD_JAVASCRIPT_TOKEN}" | base64 -w 0)
cat > .npmrc << EOF
registry=https://libraries.cgr.dev/javascript/
//libraries.cgr.dev/javascript/:_auth="$token"
//libraries.cgr.dev/javascript/:always-auth=true
EOF
```

**Bun**

```shell
cat > bunfig.toml << EOF
[install.registry]
url = "https://libraries.cgr.dev/javascript/"
username = "$CHAINGUARD_JAVASCRIPT_IDENTITY_ID"
password = "$CHAINGUARD_JAVASCRIPT_TOKEN"
EOF
```

{{< /details >}}

### Repository manager

If your organization uses a repository manager, configure Chainguard Libraries
as an upstream source in that proxy first. Follow the [global configuration
documentation](/chainguard/libraries/javascript/global-configuration/) for your
repository manager.

Once configured, point your build tool at your repository manager URL. In this
setup, the credentials your build tool uses are your repository manager
credentials — not a Chainguard pull token.

**npm or Yarn Classic:**

```shell
npm config set registry https://<your-repo-manager-url>/repository/javascript-all/ --location=project
```

**pnpm:**

```shell
pnpm config set registry https://<your-repo-manager-url>/repository/javascript-all/ --location=project
```

**Yarn Berry:**

```shell
yarn config set npmRegistryServer https://<your-repo-manager-url>/repository/javascript-all
```

Example URLs by repository manager:

| Repository manager | URL pattern |
|---|---|
| JFrog Artifactory | `https://example.jfrog.io/artifactory/javascript-all/` |
| Sonatype Nexus | `https://repo.example.com:8443/repository/javascript-all/` |

For authentication details specific to your repository manager, see the [global
configuration documentation](/chainguard/libraries/javascript/global-configuration/).

## Step 2: Verify authentication

Before reinstalling packages, confirm your credentials are valid. For direct
access with npm or pnpm, run:

```shell
npm ping --userconfig .npmrc
```

A successful response looks like:

```
npm notice PING https://libraries.cgr.dev/javascript/
npm notice PONG 1065ms
```

For repository manager setups, authentication is handled by your organization's
proxy configuration.

## Step 3: Update your lockfile

Your existing lockfile (`package-lock.json`, `pnpm-lock.yaml`, or `yarn.lock`)
contains checksums and resolved URLs pointing to the original registry. Running
your package manager's install command after changing the registry does **not**
re-fetch already-resolved packages — the lockfile entries are treated as
satisfied, and source URLs will still point to `registry.npmjs.org`.

> **Note:** If you encounter stale or corrupted package data, you may need to
> run additional commands to clear the cache. See the "Apply registry changes"
> sections for your build tool on the [build configuration](/chainguard/libraries/javascript/build-configuration/)
> page.

### Recommended: Update checksums in place

Use [`chainctl libraries update-hashes`](/chainguard/libraries/javascript/build-configuration/#updating-lockfile-hashes-for-existing-projects)
to rewrite only the integrity hashes in your existing lockfile to match
Chainguard's artifacts, without regenerating the lockfile from scratch. This
preserves your pinned dependency versions.

```shell
chainctl libraries update-hashes
```

The command outputs a "Next steps" section with the tool-specific reinstall
command to run after it completes.

### Alternative: Delete and regenerate the lockfile

Deleting the lockfile is **not recommended** as a first approach. When npm
regenerates a lockfile, it re-resolves all dependencies from scratch using the
version constraints in `package.json`. If a constraint uses `^` or `~` (the npm
default), the resolver picks the highest matching version. This may be a version
that Chainguard has not yet built, or a version that is still within the
cooldown window. Either case results in 404 errors that can be difficult to
diagnose. Regenerating the lockfile can also introduce unintended dependency
upgrades that break your application independently of the registry change.

If you have a specific reason to regenerate — for example, if you are
intentionally refreshing your dependency versions — use the following commands:

| Tool | Command |
|---|---|
| npm | `rm -rf node_modules package-lock.json && npm install` |
| pnpm | `rm -rf node_modules pnpm-lock.yaml && pnpm install` |
| Yarn Berry | `rm -rf .yarn/cache yarn.lock && yarn` |
| Yarn Classic | `rm -rf node_modules yarn.lock && yarn` |
| Bun | `rm -rf node_modules bun.lock && bun install` |

If you hit 404 errors after regenerating, the most likely cause is that the
resolved version is not yet available in Chainguard Libraries or is still within
the cooldown window. See [Packages not available in Chainguard
Libraries](#packages-not-available-in-chainguard-libraries) for next steps.

## Step 4: Reinstall dependencies

Run the install command for your package manager:

| Tool | Command |
|---|---|
| npm | `npm install` |
| pnpm | `pnpm install` |
| Yarn Berry or Classic | `yarn` |
| Bun | `bun install` |

After installation, confirm that the lockfile reflects Chainguard as the source
by inspecting resolved URLs:

**npm** — check the `resolved` field in `package-lock.json`:

```shell
grep "resolved" package-lock.json | head -5
```

**pnpm** — check the `tarball` field in `pnpm-lock.yaml`:

```shell
grep "tarball" pnpm-lock.yaml | head -5
```

**Yarn Berry** — check the `archiveUrl` field in `yarn.lock`:

```shell
grep "archiveUrl" yarn.lock | head -5
```

Resolved URLs should point to `libraries.cgr.dev/javascript` (direct access) or
your repository manager host, not `registry.npmjs.org`.

## Step 5: Verify your libraries

After reinstalling, verify that your JavaScript dependencies are sourced from
Chainguard by scanning your local package manager cache or `node_modules`
directory. `chainctl libraries verify` auto-detects npm and pnpm caches by
their directory structure.

**npm** — scan the npm cache:

```shell
chainctl libraries verify ~/.npm
```

**pnpm** — scan the pnpm store:

```shell
chainctl libraries verify $(pnpm store path)
```

**node_modules** — scan the project directory:

```shell
chainctl libraries verify ./node_modules
```

A successful result shows verification coverage for the scanned packages:

```
Artifact: ./node_modules
Verification Coverage: 100.00%
```

For full details on verification options and output, see [Verification: Analyze
JavaScript packages](/chainguard/libraries/verification/#analyze-javascript-packages).

## Step 6: Commit and roll out

Commit the updated lockfile and any registry configuration files that do not
contain literal credentials. Apply the same registry, cache, and hash update
steps to other repositories and developer workstations as you migrate them.

For organization-wide rollout using a repository manager, see the [global
configuration documentation](/chainguard/libraries/javascript/global-configuration/).

## Packages not available in Chainguard Libraries

Chainguard Libraries covers a large and growing collection of popular npm
packages, but not every package in the npm Registry is available. If a package
is missing, your install will fail with a 404 unless you have [configured
upstream fallback](/chainguard/libraries/javascript/overview/#upstream-fallback-policy-and-controls).

- For direct access, the Chainguard Repository includes a built-in, configurable
npm upstream fallback. When fallback is enabled, packages not available from
Chainguard are proxied from npm and subject to a configurable cooldown period
and malware scanning before being served. See the [JavaScript Libraries
overview](/chainguard/libraries/javascript/overview/#upstream-fallback-policy-and-controls)
for details.
- For repository manager setups, Chainguard recommends using the built-in fallback
rather than configuring a separate public registry fallback in your repository
manager, to preserve Chainguard's security controls.

If you have private scoped packages published to npm under a prefix like
`@your-org/`, you can route them back to npm using per-scope registry
configuration. See [Using private npm packages alongside Chainguard
Repository](/chainguard/libraries/javascript/build-configuration/#using-private-npm-packages-alongside-chainguard-repository)
for details.

## Troubleshooting

**Packages still resolving from `registry.npmjs.org` after migration**  
Running the install command after changing the registry does not re-fetch
packages already satisfied by the lockfile. Follow
[Step 3](#step-3-update-your-lockfile) to update checksums in place or
regenerate the lockfile.

**404 errors during install**  
The requested package or version may not yet be available in Chainguard
Libraries, or may still be within the cooldown window. Check the [Chainguard
Console](https://console.chainguard.dev/libraries/javascript), try an earlier
version, or enable upstream fallback. See [Packages not available in Chainguard
Libraries](#packages-not-available-in-chainguard-libraries).

**Authentication errors or `npm ping` failure**  
Confirm your environment variables are set and the token has not expired.
Re-run `chainctl auth pull-token --repository=javascript` to generate a new
token if needed.

**`npm config list` shows an unexpected registry**  
You may have registry configuration at the user level (`~/.npmrc`) or in
environment variables that is overriding your project-level settings. Run
`npm config list` to identify conflicting sources.

**Stale or corrupted package data after switching registries**  
If packages seem to be served from a cache rather than re-fetched, you may need
to clear additional cache layers beyond `node_modules`. See the "Apply registry
changes" sections for your build tool on the [build configuration
page](/chainguard/libraries/javascript/build-configuration/).

## Next steps

- To apply this configuration across your whole organization using a repository
  manager, see the [global configuration](/chainguard/libraries/javascript/global-configuration/)
  documentation.
- To verify downloaded packages were built by Chainguard, see the
  [verification](/chainguard/libraries/verification/) documentation.
- For full per-tool configuration reference, see the [build
  configuration](/chainguard/libraries/javascript/build-configuration/)
  documentation.
