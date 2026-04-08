---
title: "Build configuration"
linktitle: "Build configuration"
description: "Configuring Chainguard Libraries for Python on your workstation"
type: "article"
date: 2025-03-25T08:04:00+00:00
lastmod: 2025-04-07T14:11:00+00:00
draft: false
tags: ["Chainguard Libraries", "Python"]
menu:
  docs:
    parent: "python"
weight: 053
toc: true
---

The configuration for the use of Chainguard Libraries depends on how you've set up your build tools and CI/CD workflows. At a high level, adopting the use of Chainguard Libraries in your development, build, and deployment workflows involves the following steps:

- If you or an administrator have not done so already, [set up your organization's repository manager to use Chainguard Libraries for Python](/chainguard/libraries/python/global-configuration/).
- Log into your organization's repository manager and retrieve credentials for the build tool you are configuring.
- Configure your development or build tool with this information.
- Remove local caches on workstations and CI/CD pipelines. This step ensures that dependencies are preferentially sourced from Chainguard Libraries.
- Finally, confirm that your development tools and CI/CD workflows are correctly ingesting dependencies from Chainguard Libraries.

These changes must be performed on all workstations of individual developers and other engineers running relevant application builds. They must also be performed on any build tool such as Jenkins, TeamCity, GitHub Actions, or other infrastructure that draws in dependencies.

See the [minimal example projects](#minimal-example-projects) on this page for demonstrations using uv and pip.

## Step 1: Retrieve authentication credentials

To configure any build tool, you must first access credentials from your
organization's repository manager or for direct access.

<a id="cloudsmith"></a>

### Cloudsmith

The following steps allow you to determine the URL and authentication details
for accessing your organization's Cloudsmith repository manager.

1. Log into Cloudsmith.
1. Select the **Repositories** tab and click on the *python-all* repository.
1. Select the **Packages** tab.
1. Select **Push/Pull Packages** on the right.
1. Choose the **Python** format.
1. Select your desired authentication method for **Entitlement tokens** and copy
   the URL to use in your build tool - for example
   `https://dl.cloudsmith.io/.../exampleorg/python-all/python/simple/`. In the
   URL `...` is replaced with a default token or your personal token depending
   on your selection and `exampleorg` is replaced with the name of your
   organization. The URL contains both the name of the repository `python-all`
   as well as `python` as an identifier for the format. 
1. Alternatively, use the **API Key** and copy the URL to use in your build tool
   - for example
   `https://username:{{apiKey}}@dl.cloudsmith.io/basic/exampleorg/python-all/python/simple/`.
   Replace `username` and `exampleorg` with your Cloudsmith details and replace
   `{{apiKey}}` with the API key from the **Personal API Keys** section from the
   drop down on your username.

Note that for use with build tools you must include the `simple/` context so that
the package index is used successfully.

<a name="gar"></a>

### Google Artifact Registry

Use the [Google Cloud Artifact Registry documentation](https://docs.cloud.google.com/artifact-registry/docs/python/authentication) to authenticate to your Python Artifact Registry.

<a id="artifactory"></a>

### JFrog Artifactory

The following steps allow you to determine the identity token and URL for
accessing your organization's JFrog Artifactory repository manager.

1. Select **Administration** in the top navigation bar.
1. Select **Repositories** in the left hand navigation.
1. Select the **Virtual** tab in the repositories view.
1. Locate the **python-all** repository row and press the three dots
   (**...**) in the last column on the right.
1. Select **Set Me Up** in the dialog.
1. Select **Generate Token & Create Instructions**
1. Copy the generated token value to use as the password for authentication.
1. Select **Generate Settings**.
1. Copy the value from one of the *URL* fields. They are all identical. For
   example, `https://exampleorg.jfrog.io/artifactory/python-all` with
   `exampleorg`. Note that for use with build tools you must append `simple/` to
   the URL so that the package index is used successfully -
   `https://exampleorg.jfrog.io/artifactory/python-all/simple/`.

<a id="nexus"></a>

### Sonatype Nexus Repository

The following steps allow you to determine the URL and authentication details
for accessing your organization's Sonatype Nexus repository group.

1. Click **Browse** in the **Welcome** view or the browse icon (cube) in the top
   navigation bar.
1. Locate the **URL** column for the *python-all* repository group and press
   **copy**. The URL should take the following format:
   `https://repo.example.com/repository/python-all/`. Note that for use with
   build tools you must append `simple/` to the URL so that the package index is
   used successfully - `https://repo.example.com/repository/python-all/simple/`.
1. No further configuration is necessary if your repository manager is
   configured for anonymous access with **Security** - **Anonymous Access** -
   **Access** - **Allow anonymous users to access the server** is activated. If
   authentication is required, you must use the relevant details such as
   username and password in your build tool configuration.

### Direct access

The build configuration to retrieve artifacts **directly** from the Chainguard
Libraries for Python repositories requires authentication with username and
password from a pull token as detailed in [access
documentation](/chainguard/libraries/access/#pull-token). 

Note that there are multiple repositories:

- `https://libraries.cgr.dev/python/` with the simple index at `https://libraries.cgr.dev/python/simple` 
- `https://libraries.cgr.dev/python-remediated` with the simple index at `https://libraries.cgr.dev/python-remediated/simple`

Configuration for multiple index use and authentication varies for each
packaging tool. Typically Python tools include support for
[.netrc](/chainguard/libraries/access/#netrc).

See examples using `pip` and `uv` under [Minimal example projects](#minimal-example-projects).

## Step 2: Configure your build tools

Once you have credentials and the index URL from your organization's repository
manager, you're ready to set up specific build tools for local development or
CI/CD.

### Authentication

[pip](#pip), [uv](#uv), poetry, and other Python build and packaging tools have
dedicated support for configuring authentication to the repository manager or
the Chainguard Libraries for Python directly. As an alternative that works
across tools and is often preferred, use [.netrc for
authentication](/chainguard/libraries/access/#netrc).

<a id="pip"></a>

### pip

The [pip tool](https://pip.pypa.io/en/stable/) is the most widely used utility
for installing Python packages. In this section, we use the credentials from
your organization's repository manager to configure `pip` to ingest dependencies
from Chainguard Libraries.

First, clear your local `pip` cache to ensure that packages are sourced
from Chainguard Libraries for Python:

```shell
pip cache purge
```

#### Using a repository manager

To update `pip` to use our repository manager's URL globally, create or edit
your `~/.pip/pip.conf` file. You may need to create the `~/.pip` folder as
well. For example:

```sh
mkdir -p ~/.pip
nano ~/.pip/pip.conf
```

Update this configuration file with the following, replacing `<repository-url>`
with the URL provided by your repository manager including the `simple/`
context:

```pip.conf
[global]
index-url = <repository-url>
```

Updating this global configuration affects all projects built on the
workstation. Alternately, if your project uses a `requirements.txt` file in
projects, you can add the following to it to configure on a project-by-project
basis:

```
--index-url <repository-url>
package-name==version
```

Note the different syntax for `index-url` in the two files.

Refer to the official documentation for [configuring authentication with
pip](https://pip.pypa.io/en/stable/topics/authentication/) if you are not using
[.netrc for authentication](/chainguard/libraries/access/#netrc).

#### Using direct access

When using [direct access](#direct-access) to the Chainguard Libraries for
Python repository with `pip`, you must ensure the following are set in your
configuration file:

* Replace any `/` in the username value `CG_PULLTOKEN_USERNAME` with `_`.
* Ensure the `simple` context is used for the URL.
* The password value `CG_PULLTOKEN_PASSWORD` remains unchanged.

Example for `requirements.txt`:

```
--index-url https://CG_PULLTOKEN_USERNAME:CG_PULLTOKEN_PASSWORD@libraries.cgr.dev/python/simple/
```

Example for `~/.pip/pip.conf`:

```
[global]
index-url = https://CG_PULLTOKEN_USERNAME:CG_PULLTOKEN_PASSWORD@libraries.cgr.dev/python/simple/
```

Note that `pip` supports installing Python libraries from one main repository
URL specified with `index-url` and one or more additional repositories specified
with `extra-index-url` without any specific prioritization beyond resolving
semantic versions. The following example uses authentication from a local
`.netrc` file and places the remediated repository first as the primary source,
falling back to the standard Chainguard Libraries repository when a remediated
version is not available: 

```
--index-url https://libraries.cgr.dev/python-remediated/simple/
--extra-index-url https://libraries.cgr.dev/python/simple/
```

If you are using `pip` and prefer to pull from multiple repositories while
prioritizing Chainguard Libraries for Python, we recommend using a repository
manager. Alternatively, other Python package managers, detailed in the following
sections, provide support for index priority resolution behavior.

See a demonstration using `pip` under [Minimal example projects](#pip-minimal).

<a id="poetry"></a>

### Poetry

[Poetry](https://python-poetry.org/) helps you declare, manage, and install
dependencies of Python projects, and can be used with Chainguard Libraries for
Python."

List the Python package caches used by your Poetry project:

```shell
poetry cache list
```

The following commands clear the default cache, the cache for a repository named
`pypi`, and the cache of packages of the repo `python-all` from your repository
manager as configured in [the global
configuration](/chainguard/libraries/python/global-configuration/):

```shell
poetry cache clear --all _default_cache
poetry cache clear --all pypi
poetry cache clear --all python-all
```

#### Using a repository manager

Set up HTTP authentication to the repository `python-all` on your repository
manager with the username `example` and the password `secret` in your project
directory:

```shell
poetry config http-basic.python-all example secret
```

The authentication is used for the `python-all` repository that you add to the
`pyproject.toml` with the following command:

```shell
poetry source add python-all https://repo.example.com/../python-all/simple/
```

Example URLs including the required `simple` context:

* JFrog Artifactory: `https://example.jfrog.io/artifactory/api/pypi/python-all/simple/`
* Sonatype Nexus: `https://repo.example.com:8443/repository/python-all/simple/`

The following configuration is added:

```toml
[[tool.poetry.source]]
name = "python-all"
url = "https://repo.example.com/../python-all/simple/"
priority = "primary"
```

Trigger a new download of the dependencies:

```shell
poetry install
```

If necessary, you can fix or even regenerate your `poetry.lock` file:

```shell
poetry lock
poetry lock --regenerate
```

Proceed to build your project:

```shell
poetry build
```

#### Using direct access

For [direct access](#direct-access) to Chainguard Libraries for Python with
Poetry, use your username `CG_PULLTOKEN_USERNAME` and password
`CG_PULLTOKEN_PASSWORD` values from the pull token creation and the URL with the
simple context `https://libraries.cgr.dev/python/simple/`:

In order to install Python libraries from multiple repositories with Chainguard
Libraries for Python as the priority, `poetry` supports setting a [primary
package
source](https://python-poetry.org/docs/repositories/#project-configuration). You
can use this to configure Chainguard Libraries for Python as the first choice
for any library access, remediated packages from Chainguard as another choices
and a fallback to the PyPI public index for any missing packages:

```shell
poetry config http-basic.chainguard CG_PULLTOKEN_USERNAME CG_PULLTOKEN_PASSWORD
```

The authentication is used for the `chainguard` repository that you add to the
`pyproject.toml` with the following command:

```shell
poetry source add --priority=primary chainguard https://libraries.cgr.dev/python/simple/
```

Optionally, add the remediated Python libraries as supplemental source:

```shell
poetry source add chainguard-remediated https://libraries.cgr.dev/python-remediated/simple/
```

If you require a fallback to PyPI, you can add it as supplemental source:

```shell
poetry source add PyPI
```

Alternatively, edit the `pyproject.toml` file directly:

```toml
[[tool.poetry.source]]
name = "chainguard"
url = "https://libraries.cgr.dev/python-remediated/simple"
priority = "primary"

[[tool.poetry.source]]
name = "chainguard-remediated"
url = "https://libraries.cgr.dev/python-remediated/simple"

[[tool.poetry.source]]
name = "PyPI"
```

The [Poetry documentation](https://python-poetry.org/docs/) contains more
information about your project build, dependencies, versions, and other aspects. 

### uv

[uv](https://docs.astral.sh/uv) is a fast Python package and project manager
written in Rust. It uses PyPI by default, but also [supports the use of
alternative package indexes](https://docs.astral.sh/uv/configuration/indexes/).

#### Using a repository manager 

To update your global configuration to use your organization's repository
manager with `uv`, create or edit the `~/.config/uv/uv.toml` configuration file.
You may also need to create the `~/.config/uv/` folder first. For example:

```sh
mkdir -p ~/.config/uv
nano ~/.config/uv/uv.toml
```

Add the following to your `uv` global configuration file:

```toml
[[tool.uv.index]]
name = "<repository-manager-name>"
url = "<repository-url>"
```

Add the name for your repository, such as `corppypi`, within the quotes.

Replace the `<repository-url>` with the URL provided by your repository manager
including the `simple/` context.

Note that updating the global configuration affects all projects built on the
workstation. Alternately, you can update each project by adding the same
configuration in `pyproject.toml`.

Refer to the official documentation for [configuring authentication with
uv](https://docs.astral.sh/uv/configuration/authentication/) and [using
alternative package
indexes](https://docs.astral.sh/uv/guides/integration/alternative-indexes/) if
you are not using [.netrc for
authentication](/chainguard/libraries/access/#netrc).

#### Using direct access

For [direct access](#direct-access) to Chainguard Libraries for Python with
uv, use `.netrc` or your username `CG_PULLTOKEN_USERNAME` and password
`CG_PULLTOKEN_PASSWORD` values from the pull token creation and the URL with the
simple context `https://libraries.cgr.dev/python/simple/`:

Example for `pyproject.toml`:

```toml
[[tool.uv.index]]
name = "chainguard"
url = "https://CG_PULLTOKEN_USERNAME:CG_PULLTOKEN_PASSWORD@libraries.cgr.dev/python/simple/"
default = true
```

Example for `uv.toml`:

```toml
[[index]]
url = "https://CG_PULLTOKEN_USERNAME:CG_PULLTOKEN_PASSWORD@libraries.cgr.dev/python/simple/"
```

See a demonstration using `uv` under [Minimal example projects](#uv-minimal).

#### Multiple indexes

In order to install Python libraries from multiple repositories with Chainguard
Libraries for Python as the priority, `uv` supports [searching across multiple
indexes](https://docs.astral.sh/uv/concepts/indexes/#searching-across-multiple-indexes).

You can use this to configure Chainguard Libraries for Python as the first
choice for any library access, with a fallback to the PyPI public index. In
addition, if you are consuming from our remediated Python libraries index, we
recommend setting the [index-strategy
setting](https://docs.astral.sh/uv/reference/settings/#index-strategy) to
`unsafe-best-match`. This ensures that index resolution continues to work when
remediated libraries have dependencies on non-remediated libraries.

Example `pyproject.toml` index setup for direct access to remediated and default
packages with netrc-based authentication and lowest priority fallback to PyPI.
Note that the order of the entries in the configuration file is significant and
determines the order for resolving dependencies:

```toml
[[tool.uv.index]]
name = "cgr-pr"
url = "https://libraries.cgr.dev/python-remediated/simple"
authenticate = "always"

[[tool.uv.index]]
name = "cgr-p"
url = "https://libraries.cgr.dev/python/simple"
authenticate = "always"

[[tool.uv.index]]
name = "pypi"
url = "https://pypi.org/simple/"
default = true # important to treat it as lowest priority
```

Set the index strategy to allow fallback from the remediated package index to
the Chainguard index and even PyPI as final fallback in `pyproject.toml`:

```toml
[tool.uv]
index-strategy = "unsafe-best-match"
```

Run a build to observe the resolved packages. For example, the declared
dependency to `flask` version `2.0.0` results in the use of version `2.0.0+cgr.1`.

## Minimal example projects

<a id="uv-minimal"></a>

### uv

Use the following steps to create a minimal example project for uv with
Chainguard Libraries for Python. For testing purposes, you can use direct access
and environment variables as detailed in the [access
documentation](/chainguard/libraries/access/#use-environment-variables-for-pull-token-credentials). 

**1. Configure credentials**

Once the environment variables are set, configure credentials in `~/.netrc`:

```bash
cat >> ~/.netrc << EOF
machine libraries.cgr.dev
login ${CHAINGUARD_PYTHON_IDENTITY_ID}
password ${CHAINGUARD_PYTHON_TOKEN}
EOF
chmod 600 ~/.netrc
```
> **Note**: The `machine libraries.cgr.dev` entry is shared across ecosystems.
> Make sure your entry is using a pull token with Python entitlement.

In this example, the global uv index is set to the Chainguard Python repositories
without embedded credentials, allowing uv to authenticate automatically using
`.netrc`. 

Create the global index file `~/.config/uv/uv.toml` then open it in a text
editor such as `nano`:

```bash
mkdir -p ~/.config/uv
nano ~/.config/uv/uv.toml
```
Update it to include the remediated and standard Chainguard indexes:

```toml
[[index]]
url = "https://libraries.cgr.dev/python-remediated/simple/"
authenticate = "always"

[[index]]
url = "https://libraries.cgr.dev/python/simple/"
authenticate = "always"
```

**2. Initialize a new project**

This command creates a new directory, moves to the new directory, then initializes it with uv:

```bash
mkdir uv-example && cd $_
uv init
```

**3. Edit pyproject.toml**

Open `pyproject.toml` with a text editor, such as `nano`:

```bash
nano pyproject.toml
```

Add `flask==2.0.0` to the `dependencies` list in the `[project]` section, and add the following index configurations for the Python libraries to the end of the file:

```toml
[project]
name = "uv-example"
version = "0.1.0"
requires-python = ">=3.9"
dependencies = [
    "flask==2.0.0",
]

[tool.uv]
index-strategy = "unsafe-best-match"
# This allows uv to search across multiple indexes to find remediated versions of Python libraries

[[tool.uv.index]]
name = "cgr-pr"
url = "https://libraries.cgr.dev/python-remediated/simple"
authenticate = "always"

[[tool.uv.index]]
name = "cgr-p"
url = "https://libraries.cgr.dev/python/simple"
authenticate = "always"
```

**4. Build the project**

Build the project and sync dependencies:

```bash
uv sync
```

Following this, confirm the patched Chainguard version of flask was resolved:

```bash
uv pip list | grep flask
```

The output should show `flask 2.0.0+cgr.1`, confirming the remediated version was installed.

#### Verify the project works as expected

To verify the installed packages were built by Chainguard, use `chainctl`:

```bash
chainctl libraries verify --detailed .venv/
```

A successfully verified project produces output similar to the following:

```bash
  - flask
    Status: Verified as built from source
    Details: Version: 2.0.0+cgr.1 (verified via per-package SBOM - built from source by Chainguard)
    Python package: flask==2.0.0+cgr.1
```

<a id="pip-minimal"></a>

### pip

Use the following steps to create a minimal example project for pip with Chainguard Libraries for Python.
For testing purposes, you can use direct access and environment variables as detailed in the [access
documentation](/chainguard/libraries/access/#use-environment-variables-for-pull-token-credentials).  


**1. Update your configuration to point to Chainguard**

Once the environment variables are set, update `~/.pip/pip.conf` to point to Chainguard Libraries. 

You may need to create the `~/.pip` directory first:

```bash
mkdir -p ~/.pip
nano ~/.pip/pip.conf
```

In `~/.pip/pip.conf`, add the following:

```pip.conf
[global]
index-url = https://CHAINGUARD_PYTHON_IDENTITY_ID_SAFE:CHAINGUARD_PYTHON_TOKEN@libraries.cgr.dev/python/simple/
```

> **Note**: Replace any `/` in your `CHAINGUARD_PYTHON_IDENTITY_ID`'s value with `_` in the URL. The password value remains unchanged.

**2. Create a virtual environment**

Create a new directory, navigate to it, and create and activate a virtual environment:

```bash
mkdir pip-example && cd $_
python3 -m venv .venv
source .venv/bin/activate
```

**3. Add and install dependencies**

Create a `requirements.txt` file:

```bash
nano requirements.txt
```

In the `requirements.txt`, add the following:

```
flask==2.0.0
```

Run the following command to install the dependencies:

```bash
pip install -r requirements.txt
```

#### Verify the project works as expected

To verify the installed packages were built by Chainguard, use `chainctl`:

```bash
chainctl libraries verify --detailed .venv/
```

A successfully verified project produces output similar to the following:

```bash
Artifact: .venv/
Verification Coverage: 55.56%
Verified packages: 5 of 9
...
  - flask
    Status: Verified as built from source
    Details: Version: 2.0.0 (verified via per-package SBOM - built from source by Chainguard)
    Python package: flask==2.0.0
```

Adjust the index URL to use your repository manager and add any other desired packages for further testing.