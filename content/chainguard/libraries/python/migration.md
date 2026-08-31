---
title: "Migrating a Python project to Chainguard Libraries"
type: "article"
linktitle: "Migrate to Chainguard"
description: "How to migrate an existing Python project to pull dependencies from Chainguard Libraries"
date: 2026-07-14T00:00:00+00:00
lastmod: 2026-08-31T14:23:56+00:00
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

To follow along with a ready-made project instead of your own, use the [Chainguard Libraries for Python demo repository](https://github.com/chainguard-demo/chainguard-libraries-python). It provides example projects for pip, uv, and Poetry, each with a `demo.sh` script that configures access and installs sample packages.

For a reference of the configuration options for each supported build tool, check out [Configure Python build tools](/chainguard/libraries/python/build-configuration/).

## Prerequisites

Before you begin, you need:

* An existing, working Python project with a `requirements.txt`, `poetry.lock`, `uv.lock`, `pdm.lock`, `Pipfile.lock`, or `pylock.toml`
* [chainctl installed and authenticated](/chainguard/chainctl-usage/how-to-install-chainctl/)
* An [entitlement to Chainguard Libraries](/chainguard/chainctl/chainctl-docs/chainctl_libraries_entitlements_create/) for Python.

If you do not have an entitlement to Chainguard Libraries for Python yet, run the following command to create an entitlement and enable upstream fallback:

```shell
chainctl libraries entitlements create --ecosystems=PYTHON --policy=CHAINGUARD_AND_UPSTREAM
```

It can take up to 30 minutes for fallback policy changes to take effect.

### Authentication prerequisites

For authentication, you need a pull token or the Python keyring provider.

{{< tabs >}}

{{% tab title="Pull token" %}}

If you plan to use a repository manager, or a non-interactive environment such as CI/CD, you will need a pull token. You must have the `owner` role or have the `libraries.python.pull_token_creator` permission to create one.

```shell
chainctl auth pull-token create --repository=python --name=my-python-token --ttl=720h
```

To export environment variables directly:

```shell
eval $(chainctl auth pull-token --output env --repository=python --name=my-python-token)
```

Learn more about creating and managing pull tokens in the [Libraries access documentation](/chainguard/libraries/access/#creating-pull-tokens-for-libraries).

{{% /tab %}}

{{% tab title="Python keyring" %}}

The keyring leverages `chainctl` to fetch temporary credentials whenever your environment requests packages from Chainguard. Supported environments include local development and CI/CD platforms that can use assumable identities. The keyring provider requires pip 23.1 or later.

Learn how to install this package in the [Chainguard Libraries access documentation](/chainguard/libraries/access/#python-keyring-provider).

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

First, configure authentication using a pull token or the Python keyring provider.

Setting pull token credentials in `.netrc` is a common approach for individual work stations. Setting authentication in `pip.conf` is preferred for CI/CD, where you need credentials isolated per project or per pipeline rather than a single shared home-directory file.

{{< tabs >}}

{{% tab title="Pull token in .netrc" %}}

> **Note**: `.netrc` only supports one set of credentials per hostname. Since all Chainguard Libraries are served from `libraries.cgr.dev`, configuring `.netrc` for Python will override credentials for any other ecosystem.

First, check for an existing registry entry in `.netrc`:

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

{{% tab title="Pull token in pip.conf" %}}

Unlike `.netrc`, `pip.conf` can be scoped per project or per pipeline rather than shared globally across a whole workstation.

First, check whether an index or credentials are already configured
elsewhere, since a global `pip.conf` or environment variable can silently
override a project-scoped one:

```shell
pip config list -v
env | grep -i pip
```

Then create a project-scoped config file rather than editing the global
`~/.pip/pip.conf`. This example sets the remediated repository first, with
the standard repository as a fallback, and embeds [pull token credentials](#authentication-prerequisites) directly in
each URL:

```shell
mkdir -p .pip
cat > .pip/pip.conf << EOF
[global]
index-url = https://${CHAINGUARD_PYTHON_IDENTITY_ID}:${CHAINGUARD_PYTHON_TOKEN}@libraries.cgr.dev/python-remediated/simple/
extra-index-url = https://${CHAINGUARD_PYTHON_IDENTITY_ID}:${CHAINGUARD_PYTHON_TOKEN}@libraries.cgr.dev/python/simple/
EOF
```

Point pip at it with the `PIP_CONFIG_FILE` environment variable, scoped to
your current shell or CI job:

```shell
export PIP_CONFIG_FILE="$(pwd)/.pip/pip.conf"
```

This method sets both the index and its credentials in one step.

> **Note**: Do not commit credentials to version control. Generate `.pip/pip.conf`
> at build time from CI secrets, as shown in this section, rather than committing a
> version with a literal token embedded in the URL. Add `.pip/` to
> `.gitignore` if you create it locally with real credentials for testing.

{{% /tab %}}

{{% tab title="Python keyring" %}}

The `keyrings-chainguard-libraries` package supplies short-lived credentials automatically via `chainctl`, avoiding static tokens on your local workstation.

Follow the [instructions to install the keyring package](/chainguard/libraries/access/#python-keyring-provider).

> **Note**: After switching to Chainguard, you can [reinstall the keyring package](/chainguard/libraries/access/#python-keyring-provider) to use the Chainguard-built version.

{{% /tab %}}

{{< /tabs >}}

#### Point your build tool at Chainguard

Next, point your build tool at the Chainguard index.

Note that Chainguard publishes both standard and [remediated Python indexes](/chainguard/libraries/cve-remediation/). Remediated versions use a `+cgr.N` local-version suffix, and Python package managers treat those as compatible higher-precedence replacements for the base version. In addition, CUDA-enabled Python libraries use separate CUDA-specific indexes such as `https://libraries.cgr.dev/cu128/simple/`, and they are not dependency-complete for NVIDIA toolkit components.  

{{< tabs >}}

{{% tab title="pip" %}}

If you configured authentication via `.netrc` or the Python keyring provider, run the following commands to set the remediated repository first, then the simple repository:

```bash
pip config set global.index-url https://libraries.cgr.dev/python-remediated/simple/
pip config set global.extra-index-url https://libraries.cgr.dev/python/simple/
```

If you configured authentication via pull token credentials in `pip.conf`, this step
is already done; the `index-url` you set in `.pip/pip.conf` already points
at Chainguard with credentials embedded.

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

For authentication details specific to your repository manager, refer to the [global configuration documentation](/chainguard/libraries/python/global-configuration/).

## Step 2: Update your lockfile

Your existing lockfile or hash-pinned `requirements.txt` contains checksums generated against packages downloaded from PyPI or through your repository manager. Because Chainguard rebuilds packages from verified source as well as providing security controls for upstream artifacts, checksums differ even for identical version numbers. If your file uses `--hash` entries or `--require-hashes`, installation will fail with a hash mismatch after switching to Chainguard until these are updated.

You can update your lockfile in one of two ways. Update the checksums in place to keep your existing pinned versions, or regenerate the lockfile if you also want to refresh your dependency versions.

{{< tabs >}}

{{% tab title="Update checksums in place" %}}

Use `chainctl libraries update-hashes` to rewrite only the integrity hashes in your existing lockfile or requirements file to match Chainguard's artifacts, without re-resolving your dependency graph. Supported formats include `requirements.txt`, `poetry.lock`, `uv.lock`, `pdm.lock`, `Pipfile.lock`, and `pylock.toml`.

Run the following command to auto-detect and update the lockfile in the current project:

```bash
chainctl libraries update-hashes
```

> **Note**: Running `chainctl libraries update-hashes` requires the `libraries.python.pull` permission or the Owner role.

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

{{% /tab %}}

{{% tab title="Regenerate the lockfile" %}}

Regenerating the lockfile is another valid approach, and many teams use the migration as an opportunity to update dependencies at the same time. Before you regenerate, keep two things in mind:

* Pinning versions is a security best practice. Regenerating re-resolves your dependencies and can change versions, so you lose your existing pins unless you re-pin afterward.
* Resolvers pick the newest version that satisfies each constraint. Whether Chainguard has that version available depends on the cooldown period you've configured: a release still inside your cooldown window isn't available yet and returns a 404 error. Check the cooldown period you've set before you regenerate.

To regenerate — for example, to intentionally refresh your dependency versions — use the following commands.

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

{{% /tab %}}

{{< /tabs >}}

## Step 3: Clear caches

Reinstalling after switching indexes can silently reuse a cached artifact
from your previous index, with no error indicating this happened. To avoid this, clear caches.

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

```bash
uv sync --reinstall
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

After reinstalling, you can use `chainctl` to verify which dependencies are built by Chainguard. When upstream fallback is enabled, [libraries that aren't built by Chainguard](#packages-not-available-in-chainguard-libraries) are subject to Chainguard's security controls.

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

> **Note**: Running `chainctl libraries verify` requires the `libraries.python.pull` permission or the Owner role.

A successful result shows what percentage of your project's dependencies were built by Chainguard.

For full details on verification options and output, check out [Verification: Analyze a Python wheel file](/chainguard/libraries/verification/#analyze-a-python-wheel-file).

## Step 6: Commit and roll out

Commit the updated lockfile and any non-sensitive configuration changes. Apply the same index, cache, and hash-update steps to other developer workstations and build servers as you migrate them, including CI/CD platforms and any infrastructure that builds the application or installs dependencies.

For organization-wide rollout using a repository manager, refer to the [global configuration documentation](/chainguard/libraries/python/global-configuration/).

## Packages not available in Chainguard Libraries

Chainguard Libraries covers a large and growing collection of PyPI packages, but not every package or version is available. If a package is missing, your install will fail with a 404 unless you have configured [upstream fallback](/chainguard/libraries/overview/#upstream-fallback-and-controls).

With upstream fallback enabled, packages not yet available from Chainguard are proxied from PyPI, subject to Chainguard's security controls. Confirm your current policy with:

```shell
chainctl libraries entitlements list
```

For repository manager setups, Chainguard recommends using the configurable fallback rather than configuring a separate public registry fallback in your repository manager, to preserve Chainguard’s security controls.

Learn more about upstream fallback configurations in the [Libraries overview](/chainguard/libraries/overview/#upstream-fallback-and-controls).

## Troubleshooting

### "403 Forbidden" from the index despite a working keyring

Check for an old or incorrectly scoped `.netrc` entry for `libraries.cgr.dev`, which silently takes priority over keyring authentication. Run with full verbosity to confirm the credential source:

```shell
pip install -vvv <package> 2>&1 | grep -B2 -A2 "credentials\|40[13]"
```

### A pinned dependency shows "not verified" after running `chainctl libraries verify`

Check your install output for a local wheel build (`Building wheel for <package>`), which indicates Chainguard has only a source distribution for that specific pinned version.

## Next steps

* To apply this configuration across your whole organization using a repository manager, refer to the [global configuration](/chainguard/libraries/python/global-configuration/) documentation.  
* To verify downloaded packages were built by Chainguard, refer to the [verification](/chainguard/libraries/verification/) documentation.  
* For full per-tool configuration reference, refer to the [build configuration](/chainguard/libraries/python/build-configuration/) documentation.
* To keep pinned versions stable when Chainguard publishes new builds, refer to the [build pinning](/chainguard/libraries/build-pinning/) documentation.
