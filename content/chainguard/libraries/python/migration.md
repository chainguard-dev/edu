---
title: "Migrating a Python project to Chainguard Libraries"
type: "article"
linktitle: "Migrate to Chainguard"
description: "How to migrate an existing Python project to pull dependencies from Chainguard Libraries"
date: 2026-07-14T00:00:00+00:00
lastmod: 2026-07-14T00:00:00+00:00
tags: ["Chainguard Libraries", "Python"]
menu:
  docs:
    parent: python
    identifier: Python Migration
weight: 056
toc: true
---

Chainguard Libraries for Python provides a curated index of PyPI packages rebuilt from source and verified against Chainguard's build provenance. Because Chainguard Libraries uses the standard pip simple-index protocol, switching an existing project requires only an index configuration change — no changes to your application code or dependency declarations.

This guide walks through migrating an existing Python project to Chainguard Libraries, covering the two most common setups:

* **Direct access**: Your build tool connects directly to `libraries.cgr.dev`. This option is faster for initial evaluation and smaller-scale setups.  
* **Repository manager**: Your build tool connects to a repository manager (such as JFrog Artifactory or Sonatype Nexus), which proxies requests to Chainguard Libraries. This option is recommended for teams and organizations.

## Prerequisites

Before you begin, you need:

* An existing, working Python project with a `requirements.txt`, `poetry.lock`, `uv.lock`, `pdm.lock`, `Pipfile.lock`, or `pylock.toml`
* [A pull token](#create-a-pull-token) or the [Python keyring provider](/chainguard/libraries/access/#python-keyring-provider)
  * The keyring provider requires pip 23.1 or later. Older pip versions cannot automatically discover or invoke a keyring backend.
* **Python 3.11 or later** is recommended. Chainguard's index can return package upload timestamps with fractional-second precision that Python's `datetime.fromisoformat()` does not accept before 3.11
* [chainctl installed and authenticated](/chainguard/chainctl-usage/how-to-install-chainctl/)
* An [entitlement to Chainguard Libraries](/chainguard/chainctl/chainctl-docs/chainctl_libraries_entitlements_create/) for Python

### Create an entitlement

To create an entitlement to Chainguard Libraries for Python and enable upstream fallback, run:

```shell
chainctl libraries entitlements create --ecosystems=PYTHON --policy=CHAINGUARD_AND_UPSTREAM
```

Alternatively, you can create an entitlement and pull token in the Chainguard Console: while viewing the Python ecosystem page, follow the prompts to create an access token.

It can take up to 30 minutes for fallback policy changes to take effect.

### Authentication prerequisites

For authentication, you need a pull token or the Python keyring provider.

{{< tabs >}}

{{% tab title="Pull token" %}}

If you plan to use a repository manager, or a non-interactive environment such as CI/CD, you will need a pull token. You must be an Owner or have the `libraries.python.pull_token_creator` permission to create one.

```shell
chainctl auth pull-token --repository=python --name=my-python-token --ttl=720h
```

To export environment variables directly:

```shell
eval $(chainctl auth pull-token --output env --repository=python --name=my-python-token)
```

Learn more about creating and managing pull tokens in the [Libraries Access documentation](/chainguard/libraries/access/#creating-pull-tokens-for-libraries).

{{% /tab %}}

{{% tab title="Python keyring" %}}

The keyring leverages `chainctl` to fetch temporary credentials whenever your environment requests packages from Chainguard. Supported environments include local development and CI/CD platforms that can use assumable identities. 

Learn how to install this package in the [Chainguard Libraries Access documentation](chainguard/libraries/access/#python-keyring-provider).

Note that `.netrc` takes precedence over the keyring. Verify that you do not have an existing registry entry in `.netrc` for Chainguard Libraries:

```shell
grep -A2 "libraries.cgr.dev" ~/.netrc
```

Remove or correct any stale entry before proceeding.

{{% /tab %}}

{{< /tabs >}}

> **Note: Do not commit credentials to version control.** Store tokens as environment variables or CI secrets, not as literal values in `pip.conf`, `.netrc`, or any file that might be checked into a repository.

## Step 1: Configure authentication and registry

How you configure the index depends on your environment. Follow the instructions that match your setup.

The `https://libraries.cgr.dev/python/` endpoint is also the [Chainguard Repository](/chainguard/chainguard-repository/overview/) endpoint for Python. By default, it serves only Chainguard-built artifacts. When upstream fallback is enabled for your organization, the same endpoint can also serve requested versions from PyPI under Chainguard security controls.

### Direct access

#### Configure authentication

First, configure authentication using a pull token in `.netrc` or the Python keyring provider.

{{< tabs >}}

{{% tab title="Pull token" %}}

`.netrc` only supports one set of credentials per hostname. Since all Chainguard Libraries are served from `libraries.cgr.dev`, configuring `.netrc` for Python will override credentials for any other ecosystem.

Check for an existing registry entry in `.netrc`:

```shell
grep -A2 "libraries.cgr.dev" ~/.netrc
```

Remove or correct any stale entry before proceeding. 

Then, configure your [pull token credentials](#authentication-prerequisites) in `.netrc`:

```shell
cat >> ~/.netrc << EOF
machine libraries.cgr.dev
login ${CHAINGUARD_PYTHON_IDENTITY_ID}
password ${CHAINGUARD_PYTHON_TOKEN}
EOF
chmod 600 ~/.netrc
```

{{% /tab %}}

{{% tab title="Python keyring" %}}

The `keyrings-chainguard-libraries` package supplies short-lived credentials automatically via `chainctl`, avoiding static tokens on your local workstation. 

Follow the [instructions to install the keyring package](#python-keyring-provider).

> **Note**: After switching to Chainguard, you can [reinstall the keyring package](/chainguard/libraries/access/#python-keyring-provider) to use the Chainguard-built version.

{{% /tab %}}

{{< /tabs >}}

#### Point your build tool at Chainguard

Next, point your build tool at the Chainguard index.

Note that Chainguard publishes both standard and [remediated Python indexes](/chainguard/libraries/cve-remediation/). Remediated versions use a `+cgr.N` local-version suffix, and Python package managers treat those as compatible higher-precedence replacements for the base version. In addition, CUDA-enabled Python libraries use separate CUDA-specific indexes such as `https://libraries.cgr.dev/cu128/simple/`, and they are not dependency-complete for NVIDIA toolkit components.  

{{< tabs >}}

{{% tab title="pip" %}}

Run the following commands to set the remediated repository first, then the simple repository:

```bash
pip config set global.index-url https://libraries.cgr.dev/python-remediated/simple/
pip config set global.extra-index-url https://libraries.cgr.dev/python/simple/
```

{{% /tab %}}

{{% tab title="uv" %}}

Edit the `pyproject.toml` for project-level or the `~/.config/uv/uv.toml` to make global-level changes, setting the remediated repository first:

```toml
[tool.uv]
index-strategy = "unsafe-best-match"

[[tool.uv.index]]
name = "cgr-pr"
url = "https://libraries.cgr.dev/python-remediated/simple"
authenticate = "always"

[[tool.uv.index]]
name = "cgr-p"
url = "https://libraries.cgr.dev/python/simple"
authenticate = "always"
```

When using the remediated index, set `index-strategy = "unsafe-best-match"` so uv can resolve dependencies that fall back from remediated to non-remediated packages.

If you are using the Python keyring, enable support for it in `pyproject.toml`:

```toml
[tool.uv]
keyring-provider = "subprocess"
```

{{% /tab %}}

{{% tab title="Poetry" %}}

Configure the Chainguard sources, setting the remediated index as the primary:

```shell
poetry source add --priority=primary chainguard-remediated https://libraries.cgr.dev/python-remediated/simple/
poetry source add chainguard https://libraries.cgr.dev/python/simple/
```

{{% /tab %}}

{{< /tabs >}}

### Repository manager

If your organization uses a repository manager, configure Chainguard Libraries as an upstream source in that proxy first. Follow the [global configuration documentation](/chainguard/libraries/python/global-configuration/) for your repository manager.

Once configured, point your build tool at your repository manager URL instead of `libraries.cgr.dev` directly. In this setup, the credentials are your repository manager credentials — not a Chainguard pull token.

{{< tabs >}}

{{% tab title="pip" %}}

```shell
pip config set global.index-url https://<your-repo-manager-url>/repository/python-all/simple/
```

{{% /tab %}}

{{% tab title="uv" %}}

Configure `~/.config/uv/uv.toml` for a global default across all projects:

```bash
[[tool.uv.index]]
   name = "chainguard"
   url = "https://<your-repo-manager-url>/repository/python-all/simple/"
   default = true
```

For a per-project configuration, configure the `pyproject.toml`:

```pyproject.toml
[[tool.uv.index]]
name = "python-all"
url = "https://repo.example.com/repository/python-all/simple/"
```

{{% /tab %}}

{{% tab title="Poetry" %}}

Run the following command:

```shell
poetry config http-basic.python-all REPO_MANAGER_USERNAME REPO_MANAGER_PASSWORD
poetry source add python-all https://repo.example.com/repository/python-all/simple/
```

{{% /tab %}}

{{< /tabs >}}

Example URLs by repository manager:

| Repository manager | URL pattern |
| ----- | ----- |
| JFrog Artifactory | `https://example.jfrog.io/artifactory/api/pypi/python-all/simple/` |
| Sonatype Nexus | `https://repo.example.com:8443/repository/python-all/simple/` |
| Google Artifact Registry | `https://<location>-python.pkg.dev/<project>/python-all/simple/` |
| Cloudsmith | `https://dl.cloudsmith.io/.../<org>/python-all/python/simple/` |

For authentication details specific to your repository manager, see the [global configuration documentation](/chainguard/libraries/python/global-configuration/).

## Step 2: Update your lockfile

Your existing lockfile or hash-pinned requirements.txt contains checksums generated against packages downloaded from PyPI or through your repository manager. Because Chainguard rebuilds packages from verified source rather than mirroring upstream artifacts, checksums differ even for identical version numbers. If your file uses `--hash` entries or `--require-hashes`, installation will fail with a hash mismatch after switching to Chainguard until these are updated.

### Recommended: Update checksums in place

Use `chainctl libraries update-hashes` to rewrite only the integrity hashes in your existing lockfile to match Chainguard's artifacts, without re-resolving your dependency graph. Supported formats include `requirements.txt`, `poetry.lock`, `uv.lock`, `pdm.lock`, `Pipfile.lock`, and `pylock.toml`.

Run the following command to auto-detect and update the lockfile in the current project:

```bash
chainctl libraries update-hashes
```

Or specify the lockfile when running the command. For example:

```bash
chainctl libraries update-hashes requirements.txt
```

When using a repo manager, run a command similar to the following:

```bash
chainctl libraries update-hashes 
  --registry-url https://repo.example.com/repository/python-all/ 
  --token "$REPO_TOKEN"
```

By default, Chainguard hashes are appended alongside your existing hashes rather than replacing them. If your installer fails on a dual-hash entry, use the `--replace` flag.

### Alternative: Regenerate the lockfile

Regenerating is **not recommended** as a first approach. Dependency resolvers pick the newest version satisfying your constraints, which may not yet be available from Chainguard, and may also introduce unrelated dependency upgrades.

{{< details "Delete and regenerate a lockfile" >}}

If you have a specific reason to regenerate - for example, if you are intentionally refreshing your dependency versions -  use the following commands:

pip:

```bash
pip-compile --generate-hashes --index-url https://libraries.cgr.dev/python/simple/ requirements.in
```

uv:

```bash
rm -f uv.lock  
uv sync
```

Poetry 1.x:

```bash
poetry lock --no-update
```

Poetry 2.x:

```bash
poetry lock
```

{{< /details >}}

## Step 3: Clear caches

{{< tabs >}}

{{% tab title="pip" %}}

```shell
pip cache purge
```

{{% /tab %}}

{{% tab title="uv" %}}

```bash
uv cache clean
```

{{% /tab %}}

{{% tab title="Poetry" %}}

```bash
poetry cache clear --all pypi
```

{{% /tab %}}

{{< /tabs >}}

Also invalidate cached packages in any repository manager that previously proxied PyPI, and rebuild containers without cached layers if your Dockerfile installs dependencies during build:

```shell
docker build --no-cache .
```

## Step 4: Reinstall dependencies

Reinstall dependencies and confirm that the lockfile reflects Chainguard as the source.

{{< tabs >}}

{{% tab title="pip" %}}

```shell
pip install --force-reinstall --no-cache-dir -r requirements.txt
```

{{% /tab %}}

{{% tab title="uv" %}}

Delete the virtual environment outright and let uv rebuild it from the current lockfile:

```bash
rm -rf .venv
uv sync
```

{{% /tab %}}

{{% tab title="Poetry" %}}

```bash
poetry env remove --all
poetry install
```

{{% /tab %}}

{{< /tabs >}}

## Step 5: Verify your libraries

After reinstalling, verify that your dependencies are sourced from Chainguard:

{{< tabs >}}

{{% tab title="pip and uv" %}}

```shell
chainctl libraries verify --detailed ./.venv/
```

{{% /tab %}}

{{% tab title="Poetry" %}}

Poetry's `virtualenv` location depends on your configuration. If `virtualenvs.in-project` is enabled, it's `.venv` in the project directory. Otherwise, find it with:

```bash
poetry env info --path
```

Then:

```bash
chainctl libraries verify --detailed $(poetry env info --path)
```

{{% /tab %}}

{{< /tabs >}}

A successful result shows verification coverage for your project's dependencies. 

For full details on verification options and output, see [Verification: Analyze Python packages](/chainguard/libraries/verification/#analyze-python-packages).

## Step 6: Commit and roll out

Commit the updated lockfile and any non-sensitive configuration changes. Apply the same index, cache, and hash-update steps to other developer workstations and build servers as you migrate them, including CI/CD platforms and any infrastructure that builds the application or installs dependencies.

For organization-wide rollout using a repository manager, see the [global configuration documentation](/chainguard/libraries/python/global-configuration/).

## Packages not available in Chainguard Libraries

Chainguard Libraries covers a large and growing collection of PyPI packages, but not every package or version is available. If a package is missing, your install will fail with a 404 unless you have configured [upstream fallback](/chainguard/libraries/overview/#upstream-fallback-and-controls). 

With upstream fallback enabled, packages not yet available from Chainguard are proxied from PyPI, subject to Chainguard's security controls. Confirm your current policy with:

```shell
chainctl libraries entitlements list
```

For repository manager setups, Chainguard recommends using the configurable fallback rather than configuring a separate public registry fallback in your repository manager, to preserve Chainguard’s security controls. 

Learn more about upstream fallback configurations in the [Libraries Overview](/chainguard/libraries/overview/#upstream-fallback-and-controls).

## Troubleshooting

### 403 Forbidden from the index despite a working keyring

Check for an old or incorrectly scoped `.netrc` entry for `libraries.cgr.dev`, which silently takes priority over keyring authentication. Run with full verbosity to confirm the credential source:

```shell
pip install -vvv <package> 2>&1 | grep -B2 -A2 "credentials\|40[13]"
```

### ValueError: Invalid isoformat string during install

Your version of Python cannot parse the timestamp format used in some Chainguard index responses. Upgrade to Python 3.11 or later.

### A pinned dependency shows "not verified" after running `chainctl libraries verify`

Check your install output for a local wheel build (`Building wheel for <package>`), which indicates Chainguard has only a source distribution for that specific pinned version.

## Next steps

* To apply this configuration across your whole organization using a repository manager, see the [global configuration](/chainguard/libraries/python/global-configuration/) documentation.  
* To verify downloaded packages were built by Chainguard, see the [verification](/chainguard/libraries/verification/) documentation.  
* For full per-tool configuration reference, see the [build configuration](/chainguard/libraries/python/build-configuration/) documentation.
