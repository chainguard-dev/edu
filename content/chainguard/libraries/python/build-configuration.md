---
title: "Build Configuration"
linktitle: "Build Configuration "
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
- Log into your organization's repository manager and retrieve credentials for the build tool you are configuration.
- Configure your development or build tool with this information.
- Remove local caches on workstations and CI/CD pipelines. This step ensures that dependencies are preferentially sourced from Chainguard Libraries.
- Finally, confirm that your development tools and CI/CD workflows are correctly ingesting dependencies from Chainguard Libraries.

These changes must be performed on all workstations of individual developers and other engineers running relevant application builds. They must also be performed on any build tool such as Jenkins, TeamCity, GitHub Actions, or other infrastructure that draws in dependencies.

## Retrieving authentication credentials

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

<a id="artifactory"></a>

### JFrog Artifactory

The following steps allow you to determine the identity token and URL for
accessing your organization's JFrog Artifactory repository manager.

1. Select **Administration** in the top navigation bar.
1. Select **Repositories** in the left hand navigation.
1. Select the **Virtual** tab in the repositories view.
1. Locate the *python-all** repository row and press the three dots
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

Build configuration to retrieve artifacts **directly** from the Chainguard Libraries
for Python repository at `https://libraries.cgr.dev/python/` with the simple
index at `https://libraries.cgr.dev/python/simple` requires authentication with
username and password from a pull token as detailed in [access
documentation](/chainguard/libraries/access/#pull-token).

Note that not all Python package managers support the ability to pull from multiple indexes while setting a priority for a specific index. If you want to keep PyPI as a fallback index repository while pulling direct, `uv` supports [searching across multiple indexes](https://docs.astral.sh/uv/concepts/indexes/#searching-across-multiple-indexes) while setting a prirority index.

## Configuring build tools

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

First, let's clear your local `pip` cache to ensure that packages are sourced
from Chainguard Libraries for Python:

```sh
pip cache purge
```

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

```
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

When using [direct access](#direct-access) to the Chainguard Libraries for
Python repository with `pip`, you must ensure the following are set in your
configuration file:

* Replace any `/` in the username value `CG_PULLTOKEN_USERNAME` with `_`.
* Ensure the `simple` context is used for the URL.
* The password value `CG_PULLTOKEN_PASSWORD` remains unchanged.

Example for `requirements.txt`:

```example
--index-url https://CG_PULLTOKEN_USERNAME:CG_PULLTOKEN_PASSWORD@libraries.cgr.dev/python/simple/
```

Example for `~/.pip/pip.conf`:

```example
[global]
index-url = https://CG_PULLTOKEN_USERNAME:CG_PULLTOKEN_PASSWORD@libraries.cgr.dev/python/simple/
```

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

For [direct access](#direct-access) to Chainguard Libraries for Python with
Poetry, use your username `CG_PULLTOKEN_USERNAME` and password
`CG_PULLTOKEN_PASSWORD` values from the pull token creation and the URL with the
simple context `https://libraries.cgr.dev/python/simple/`:


```shell
poetry config http-basic.chainguard CG_PULLTOKEN_USERNAME CG_PULLTOKEN_PASSWORD
```

The authentication is used for the `chainguard` repository that you add to the
`pyproject.toml` with the following command:

```shell
poetry source add chainguard https://libraries.cgr.dev/python/simple/
```

The [Poetry documentation](https://python-poetry.org/docs/) contains more
information about your project build, dependencies, versions, and other aspects. 

### uv

[uv](https://docs.astral.sh/uv) is a fast Python package and project manager
written in Rust. It uses PyPI by default, but also [supports the use of
alternative package indexes](https://docs.astral.sh/uv/configuration/indexes/).

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

For [direct access](#direct-access) to Chainguard Libraries for Python with
uv, use .netrc or your username `CG_PULLTOKEN_USERNAME` and password
`CG_PULLTOKEN_PASSWORD` values from the pull token creation and the URL with the
simple context `https://libraries.cgr.dev/python/simple/`:

Example for `pyproject.toml`:

```
[[tool.uv.index]]
name = "chainguard"
url = "https://CG_PULLTOKEN_USERNAME:CG_PULLTOKEN_PASSWORD@libraries.cgr.dev/python/simple/
```

Example for `uv.toml`:

```
[[index]]
url = "https://CG_PULLTOKEN_USERNAME:CG_PULLTOKEN_PASSWORD@libraries.cgr.dev/python/simple/
```
