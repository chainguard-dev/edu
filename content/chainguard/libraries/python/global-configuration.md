---
title: "Global configuration"
linktitle: "Global configuration"
description: "Configuring Chainguard Libraries for Python in your organization"
type: "article"
date: 2025-03-25T08:04:00+00:00
lastmod: 2025-04-07T14:42:00+00:00
draft: false
tags: ["Chainguard Libraries", "Python"]
images: []
menu:
  docs:
    parent: "python"
    identifier: "Python Global Configuration"
weight: 052
toc: true
---

Python library consumption in a large organization is typically managed by a
repository manager. Commonly used repository manager applications are
[Cloudsmith](https://cloudsmith.com/), [JFrog
Artifactory](https://jfrog.com/artifactory/), and [Sonatype Nexus
Repository](https://www.sonatype.com/products/sonatype-nexus-repository). The
repository manager acts as a single point of access for developers and
development tools to retrieve the required libraries.

The recommended approach is to use the [upstream
fallback](/chainguard/libraries/overview/#upstream-fallback-and-controls)
feature of Chainguard Repository, which allows you to configure your repository
manager with a single upstream pointed at `https://libraries.cgr.dev/python/`. The
Chainguard Repository handles fallback and policy enforcement; your repository
manager handles local caching and access control. Chainguard proxies and serves
packages from the public PyPI repository on your behalf when upstream
fallback is enabled. All packages served from Chainguard are protected with
malware scanning and a configurable cooldown policy.

At a high level, adopting the use of Chainguard Libraries consists of the following steps:

* Configure your environment to use `https://libraries.cgr.dev/python/` as the single upstream source for Python package retrieval.
* Add the public [PyPI](https://pypi.org/) repository as a remote repository.
* Create a group, virtual, or polyglot repository combining these repository
  sources with any desired internal repositories. Configure the Chainguard
  Libraries repository as the first choice for any library access after any
  desired internal repositories.

You should also:

* Remove all prior cached artifacts in the virtual server or proxy public
  repository. This step reduces confusion about the origin of libraries and
  assists technical evaluation and adoption of Chainguard Libraries.
* Remove any repositories that are no longer desired or necessary. Depending on
  your library requirements, this step can result in removal of some proxy
  repositories or even removal of all proxy repositories.

If your organization does not use a repository manager, you can still use
Chainguard Libraries. However, this approach requires configuration of multiple
build and development platforms and utilities to use Chainguard Libraries. For
this reason, adopting the use of a repository manager is the recommended
approach. Refer to the [direct access documentation for build
tools](/chainguard/libraries/python/build-configuration/#direct-access) for more
information.

## Manually managing fallback

Chainguard recommends using the [Chainguard Repository built-in upstream fallback](/chainguard/libraries/overview/#upstream-fallback-and-controls) rather than configuring a public PyPI fallback in your repository manager. Configuring your own fallback bypasses the protection and policy behavior provided by Chainguard Repository.

However, if you intentionally want to manage fallback ordering yourself, you can continue using the repository manager patterns described on this page to combine Chainguard and PyPI sources.

### Updating lockfile hashes

If you are migrating an existing Python project to Chainguard Libraries through a repository manager, your lockfile likely contains integrity hashes generated against packages previously downloaded from PyPI or through your repository manager. The [`chainctl libraries update-hashes` command](/chainguard/chainctl/chainctl-docs/chainctl_libraries_update-hashes/) automates lockfile hash updates
for all supported JavaScript lockfile formats.

When you are using a repository manager, pass the full repository manager URL with `--registry-url` and authenticate with one of the supported methods: `--username` and `--password`, `--token`, or a `.netrc` entry for the registry host. For example:

```bash
chainctl libraries update-hashes \
  --registry-url https://repo.example.com:8443/repository/python-all/ \
  --token "$REPO_TOKEN"
```

After updating the lockfile, keep your repository manager configuration in place and reinstall through the same repository manager endpoint to apply the updated hashes.

Learn more in the [Build configuration page](/chainguard/libraries/python/build-configuration/#updating-lockfile-hashes/) and in the [chainctl docs](/chainguard/chainctl/chainctl-docs/chainctl_libraries_update-hashes/).

<a id="cloudsmith"></a>

## Cloudsmith

[Cloudsmith](https://cloudsmith.com/) supports Python repositories for proxying
and hosting and polyglot repositories that combine multiple repositories sources
with compatible formats. Refer to the [Cloudsmith Python Repository
documentation](https://help.cloudsmith.io/docs/python-repository) and the
[Cloudsmith documentation for creating a
repository](https://help.cloudsmith.io/docs/create-a-repository) for more
information.

### Initial configuration

Use the following steps to add a repository with both Chainguard Libraries for
Python and PyPI as upstream sources.

First, create a repository:

1. Log in to your Cloudsmith instance as user with administrator privileges.
1. Select the **Repositories** tab near the top of the screen.
1. Navigate to the **Repositories Overview**, then select **+New repository**.
1. At the new repository form, enter the name *python-all* for your new
   repository. The name should include *python* to identify the repository
   format. This convention helps avoid confusion, since repositories in
   Cloudsmith are multi-format.
1. Select a storage region that is appropriate for your organization and
   infrastructure.
1. Select **+Create Repository**.

Next, configure the upstream proxies:

1. Select the name of the new *python-all* repository on the repositories page
   to configure it.
1. Access the **Upstreams** tab and click **+ Add Upstream Proxy**.
1. Configure an upstream proxy with the format **python** and the following
   details:
    * **Name**: `python-chainguard`
    * **Priority**: `1`
    * **Upstream URL**: `https://libraries.cgr.dev/python/`
    * **Mode**: `Cache and Proxy`
    * Add the **Username** and **Password** value from [Chainguard Libraries
      access](/chainguard/libraries/access/) in **Authentication Settings**
1. Select **Create Upstream Proxy**.
1. If you want to use the separate repository with
   [remediated Python libraries](/chainguard/libraries/python/overview/#cve-remediation),
   repeat the preceding two steps with the name `python-chainguard-remediated`,
   the priority `2`, the same authentication details, and the URL
   `https://libraries.cgr.dev/python-remediated/`.
1. If you are manually managing fallback rather than using the [Chainguard Repository's built-in fallback](/chainguard/libraries/overview/#upstream-fallback-and-controls), configure another upstream proxy with the following details:
    * **Name**: `python-public`
    * **Priority**: `3`
    * **Upstream URL**: `https://pypi.org/`
    * **Mode**: `Cache and Proxy`
1. Select **Create Upstream Proxy**.

### Build tool access

See the page on [build tool configuration for Chainguard Libraries for
Python](/chainguard/libraries/python/build-configuration/#cloudsmith) for
information on accessing credentials and setting up build tools.

<a name="gar"></a>

## Google Artifact Registry

[Google Artifact Registry](https://cloud.google.com/artifact-registry) supports
the Python format for hosting artifacts in **Standard** repositories and proxying
artifacts from public repositories in **Remote** repositories. Use **Virtual**
repositories to combine them for consumption with `pip` and other build tools.
Use the [Python package documentation for Google Artifact
Registry](https://cloud.google.com/artifact-registry/docs/python) as the starting
point for more details.

### Initial configuration

Use the following steps to add the Pypi Package Index and the Chainguard
Libraries for Python repository as remote repositories and combine them as a
virtual repository.

1. Log in to the Google Cloud console as a user with administrator privileges.
1. Navigate to your project and find the **Artifact Registry** with the search.
1. Activate Artifact Registry if necessary.
1. Navigate to your project and find the **Secret Manager** with the search.
1. Activate **Secret Manager** if necessary.

Before configuring the repositories, you must create a secret with the [password
value as retrieved with chainctl](/chainguard/libraries/access/):

1. Navigate to the **Secret Manager**
1. Click **Create secret**.
1. Set the **Name** to `chainguard-libraries-python`.
1. Use the **Password** from chainctl output to set the **Secret value**.
1. Click **Create secret**.

Navigate to Artifact Registry and select **Repositories** in the left hand
navigation under the **Artifact Registry** label to configure a remote
repository for Chainguard Libraries for Python:

1. Click **+Create a Repository**.
1. Configure the repository:
    1. **Name**: `python-chainguard`
    1. **Format**: `Python`
    1. **Mode**: `Remote`
    1. **Remote repository source**: `Custom`. Set the URL for the Custom repository to `https://libraries.cgr.dev/python/`.
    1. **Remote repository authentication mode**: Select `Authenticated`.
    1. Set **Username for the upstream repository** to the [value as retrieved
   with chainctl](/chainguard/libraries/access/).
    1. Select the *chainguard-libraries-python* secret in the list for the **Secret** input.
    1. Choose the a **Region** for your development in **Location type**.
1. Click **Create**.
1. If you want to use the separate repository with [remediated Python
libraries](/chainguard/libraries/python/overview/#cve-remediation) repeat the
preceding steps with the name `python-chainguard-remediated`, the same
authentication details, and the URL
`https://libraries.cgr.dev/python-remediated/`.

If you are manually managing fallback rather than using the [Chainguard Repository's built-in fallback](/chainguard/libraries/overview/#upstream-fallback-and-controls), configure an additional remote repository for the public PyPI.

Combine the repositories in a new virtual repository:

1. Click **+** to add another repository.
1. Set the **Name** to `python-all`.
1. Set the **Format** to `Python`.
1. Set the **Mode** to `Virtual`.
1. Click **Add upstream repository** in **Virtual upstream repositories**.
1. Click **Browse**, then locate and select the `python-chainguard`
   repository as **Repository 1** and set the **Policy name 1** to
   `python-chainguard`.
1. Click **Browse**, then locate and select the `python-public` repository
   as **Repository 2** and set the **Policy name 2** to `python-public`.
1. Click **Add upstream repository** in **Virtual upstream repositories**.
1. Set the **Priority** value for the `python-chainguard` policy name to a higher
   value than the `python-public` priority value.
1. Choose the same suitable **Region** for your development in **Location type**
   as configured for the `python-public` repository.
1. Click **Create**.

<a id="artifactory"></a>

## JFrog Artifactory

[JFrog Artifactory](https://jfrog.com/artifactory/) supports PyPI repositories
for proxying and virtual repositories to combine multiple sources into a single
repository. The following instructions are based on the [PyPI Repository
documentation for
Artifactory](https://docs.jfrog.com/artifactory/docs/pypi-repositories).

### Initial configuration

Use the following steps to add the Chainguard Libraries for Python indexes as remote repositories and combine them as a virtual
repository:

1. Log in as a user with administrator privileges.
1. Click **Administration** in the top navigation bar.
1. Select **Repositories** in the left hand navigation.

Configure a remote repository for the Chainguard Libraries for Python index:

1. Select **Create a Repository** and choose the **Remote** option.
1. Select *PyPI* as the **Package type**.
1. Set the **Repository Key** to `python-chainguard`.
1. Set the **URL** to `https://libraries.cgr.dev/`. Do not include `/python` in the URL.
1. Set **User Name** and **Password / Access Token** to the [values as retrieved
   with chainctl](/chainguard/libraries/access/).
1. Set the **PyPI Settings - Registry URL** to
   `https://libraries.cgr.dev/`.
1. Set the **PyPI Settings - Registry Index Location URL Suffix** to `python/simple`.
1. Optionally click **Test** to verify connection and authentication.
1. Click the **Advanced** configuration tab. In the **Others** section, check the box next to **Disable URL Normalization** and uncheck the box next to **Block Mismatching Mime Types**.
1. Click **Create Remote Repository**.

If you want to use the separate repository with [remediated Python
libraries](/chainguard/libraries/python/overview/#cve-remediation) repeat the
preceding steps with the name `python-chainguard-remediated`, the same
authentication details, and the URL
`https://libraries.cgr.dev/python-remediated/`.

If you are manually managing fallback rather than using the [Chainguard Repository's built-in fallback](/chainguard/libraries/overview/#upstream-fallback-and-controls), configure an additional remote repository for the public PyPI index.

Combine the repositories in a new virtual repository:

1. Click **Create a Repository** and choose the **Virtual** option.
1. Select `PyPI` as the Package type.
1. Set the **Repository Key** to `python-all`.
1. In the **Repositories** section, find `python-chainguard`, `python-chainguard-remediated`, and if manually managing fallback, the `python-public` repository. Ensure the `python-chainguard-remediated` repository is the first in the displayed list. Use the icon on the right of the repository name to drag and drop repositories into the desired position.
1. Select **Create Virtual Repository**.

At this point, you have a virtual repository set up in Artifactory that allows
you or others in your organization to access Chainguard Libraries for Python,
optionally including remediated versions, with your chosen tools.

### Validate the remote repository

After creating the `python-chainguard` remote repository, validate that Artifactory is successfully proxying through to Chainguard before proceeding. Because Artifactory falls back to the public PyPI index when a connection to a remote repository fails, a misconfigured repository may silently resolve packages from PyPI rather than Chainguard — and the build will succeed without any visible error.

Common sources of misconfiguration include invalid or expired credentials, or an incorrect or incomplete repository URL. The Artifactory **Test** button on the repository configuration screen is not a reliable indicator; it may fail for a correctly configured repository, and may pass for an incorrectly configured one. Instead, use the following steps to verify that fetching an artifact through Artifactory produces the same checksum as fetching it directly from `libraries.cgr.dev`.

1. Find the direct URL for a specific package wheel from the Chainguard index. This example uses `urllib3`. You can substitute any artifact you know to be available.

```bash
curl -sSf \
  -u "${CHAINGUARD_PYTHON_IDENTITY_ID}:${CHAINGUARD_PYTHON_TOKEN}" \
  https://libraries.cgr.dev/python/simple/urllib3/ \
  | grep -o 'https://[^"]*\.whl' | head -1
```

1. Fetch a package file directly from `libraries.cgr.dev` and compute its checksum:

```bash
curl -sSf -L \
  -u "${CHAINGUARD_PYTHON_IDENTITY_ID}:${CHAINGUARD_PYTHON_TOKEN}" \
  <url-from-step-1> \
  | sha256sum
```

1. Fetch the same file through the Artifactory remote repository and compute its checksum:

```bash
curl -sSfL \
  -u "${ARTIFACTORY_USERNAME}:${ARTIFACTORY_TOKEN}" \
  "https://<artifactory-host>/artifactory/<python-remote-repository>/${path-to-wheel}" \
  | sha256sum
```

Replace `artifactory-host` with your Artifactory instance hostname and replace `python-remote-repository` with your remote repository name. Replace `path-to-wheel` with the path component of the URL from step 1 (for example: `/files/15f7d141c3b76b85/37e321caa85a8f41/urllib3/urllib3-1.26.9-py2.py3-none-any.whl`)

The checksums returned by the commands must match.

If the checksum from the Artifactory remote repository differs from the direct fetch, or if the Artifactory fetch fails entirely, review the following before proceeding:

* URL: The remote repository URL must be set to `https://libraries.cgr.dev/python/`.
* Credentials: You may need to regenerate your pull token with `chainctl auth pull-token --repository=python` and update the Artifactory repository credentials. Expired tokens fail silently.
* Advanced Configuration: Ensure all recommended Advanced settings from the [initial configuration steps](#initial-configuration-2) have been applied.

Do not proceed to virtual repository setup or build configuration until the checksums match.

### Build tool access

See the page on [build tool configuration for Chainguard Libraries for
Python](/chainguard/libraries/python/build-configuration/#artifactory) for
information on accessing credentials and setting up build tools.

<a id="nexus"></a>

## Sonatype Nexus Repository

[Sonatype Nexus
Repository](https://www.sonatype.com/products/sonatype-nexus-repository) allows
for merging multiple remote repositories as a repository group. The below
instructions are based on the [Nexus documentation for
PyPI](https://help.sonatype.com/en/pypi-repositories.html)

### Initial configuration

The following steps create remote repositories for Chainguard Libraries for
Python, a remote repository for the public PyPI index, and a repository group
combining these sources.

First, log in to Sonatype Nexus as a user with administrator privileges and
access the **Server administration** and configuration section within the gear
icon in the top navigation bar.

Next, configure a remote repository for Chainguard Libraries for Python repository:

1. Select **Repository - Repositories** in the left hand navigation.
1. Select **Create repository**.
1. Select the **PyPI (proxy)** recipe.
1. Provide a new name, such as `python-chainguard`.
1. In the **Proxy - Remote storage**field, add the following URL:
   `https://libraries.cgr.dev/python/`.
1. In **HTTP - Authentication**, set the **Authentication type** to *username*
   and enter the the [username and password values as retrieved with
   chainctl](/chainguard/libraries/access/).
1. Select **Create repository**.

If you want to use the separate repository with [remediated Python
libraries](/chainguard/libraries/python/overview/#cve-remediation) repeat the
preceding steps with the name `python-chainguard-remediated`, the same
authentication details, and the URL
`https://libraries.cgr.dev/python-remediated/`.

If you are manually managing fallback rather than using the [Chainguard Repository's built-in fallback](/chainguard/libraries/overview/#upstream-fallback-and-controls), configure an additional remote repository for the public PyPI.

Finally, create a new repository group and add the repositories:

1. Select **Repository - Repositories** in the left hand navigation.
1. Select **Create repository**.
1. Select the **PyPI (group)** recipe.
1. Provide a new name, such as `python-all`.
1. In the section **Group - Member repositories**, move the new repositories
   `python-chainguard-remediated` and `python-chainguard` to the right. Move the  `python-chainguard-remediated` repository to the top of the list.

### Build tool access

See the page on [build tool configuration for Chainguard Libraries for
Python](/chainguard/libraries/python/build-configuration/#nexus) for information on
accessing credentials and setting up build tools.
