---
title: "Global configuration"
linktitle: "Global configuration"
description: "Configuring Chainguard Libraries for Python in your organization"
type: "article"
date: 2025-03-25T08:04:00+00:00
lastmod: 2026-08-28T16:31:04+00:00
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
fallback](/chainguard/libraries/introduction/overview/#upstream-fallback-and-controls)
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

Chainguard recommends using the [Chainguard Repository built-in upstream fallback](/chainguard/libraries/introduction/overview/#upstream-fallback-and-controls) rather than configuring a public PyPI fallback in your repository manager. Configuring your own fallback bypasses the protection and policy behavior provided by Chainguard Repository.

However, if you intentionally want to manage fallback ordering yourself, you can continue using the repository manager patterns described on this page to combine Chainguard and PyPI sources.

### Updating lockfile hashes

If you are migrating an existing Python project to Chainguard Libraries through a repository manager, your lockfile likely contains integrity hashes generated against packages previously downloaded from PyPI or through your repository manager. The [`chainctl libraries update-hashes` command](/chainguard/chainctl/chainctl-docs/chainctl_libraries_update-hashes/) automates lockfile hash updates
for all supported Python lockfile formats.

When you are using a repository manager, pass the full repository manager URL with `--registry-url` and authenticate with one of the supported methods: `--username` and `--password`, `--token`, or a `.netrc` entry for the registry host. For example:

```bash
chainctl libraries update-hashes \
  --registry-url https://repo.example.com:8443/repository/python-all/ \
  --token "$REPO_TOKEN"
```

> **Note**: Running `chainctl libraries update-hashes` requires the `libraries.python.pull` permission or the Owner role.

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

The recommended approach is to rely on Chainguard Repository's [upstream
fallback](/chainguard/libraries/introduction/overview/#upstream-fallback-and-controls),
configuring a single upstream proxy pointed at `https://libraries.cgr.dev/python/`
rather than adding a separate public PyPI proxy. Refer to [Manually managing
fallback](#manually-managing-fallback) if you need to control fallback ordering
yourself.

### Initial configuration

Use the following steps to add a repository with Chainguard Libraries for
Python as the upstream source.

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
      access](/chainguard/libraries/introduction/access/) in **Authentication Settings**
1. Select **Create Upstream Proxy**.
1. If you want to use the separate repository with
   [remediated Python libraries](/chainguard/libraries/python/overview/#cve-remediation),
   repeat the preceding two steps with the name `python-chainguard-remediated`,
   the priority `2`, the same authentication details, and the URL
   `https://libraries.cgr.dev/python-remediated/`.
1. If you are manually managing fallback rather than using the [Chainguard Repository's built-in fallback](/chainguard/libraries/introduction/overview/#upstream-fallback-and-controls), configure another upstream proxy with the following details:
    * **Name**: `python-public`
    * **Priority**: `3`
    * **Upstream URL**: `https://pypi.org/`
    * **Mode**: `Cache and Proxy`
1. Select **Create Upstream Proxy**.

### Build tool access

Refer to the page on [build tool configuration for Chainguard Libraries for
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

The recommended approach is to rely on Chainguard Repository's [upstream
fallback](/chainguard/libraries/introduction/overview/#upstream-fallback-and-controls),
configuring a single remote repository pointed at `https://libraries.cgr.dev/python/`
rather than adding a separate public PyPI remote. Refer to [Manually managing
fallback](#manually-managing-fallback) if you need to control fallback ordering
yourself.

### Initial configuration

Use the following steps to add the Chainguard Libraries for Python repository
as a remote repository and expose it through a virtual repository.

1. Log in to the Google Cloud console as a user with administrator privileges.
1. Navigate to your project and find the **Artifact Registry** with the search.
1. Activate Artifact Registry if necessary.
1. Navigate to your project and find the **Secret Manager** with the search.
1. Activate **Secret Manager** if necessary.

Before configuring the repositories, you must create a secret with the [password
value as retrieved with chainctl](/chainguard/libraries/introduction/access/):

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
   with chainctl](/chainguard/libraries/introduction/access/).
    1. Select the *chainguard-libraries-python* secret in the list for the **Secret** input.
    1. Choose the a **Region** for your development in **Location type**.
1. Click **Create**.
1. If you want to use the separate repository with [remediated Python
libraries](/chainguard/libraries/python/overview/#cve-remediation) repeat the
preceding steps with the name `python-chainguard-remediated`, the same
authentication details, and the URL
`https://libraries.cgr.dev/python-remediated/`.

If you are manually managing fallback rather than using the [Chainguard Repository's built-in fallback](/chainguard/libraries/introduction/overview/#upstream-fallback-and-controls), configure an additional remote repository for the public PyPI.

Combine the `python-chainguard` repository, and optionally the `python-chainguard-remediated` repository, into a new virtual repository:

1. Click **+** to add another repository.
1. Set the **Name** to `python-all`.
1. Set the **Format** to `Python`.
1. Set the **Mode** to `Virtual`.
1. Click **Add upstream repository** in **Virtual upstream repositories**.
1. Click **Browse**, then locate and select the `python-chainguard`
   repository as **Repository 1** and set the **Policy name 1** to
   `python-chainguard`.
1. Choose a **Region** for your development in **Location type**.
1. Click **Create**.

If you are manually managing fallback rather than using the recommended
[upstream fallback](/chainguard/libraries/introduction/overview/#upstream-fallback-and-controls),
add the public PyPI index as a second remote repository (`python-public`) and
give the `python-chainguard` policy a higher priority than `python-public`.

<a id="artifactory"></a>

## JFrog Artifactory

[JFrog Artifactory](https://jfrog.com/artifactory/) supports PyPI repositories
for proxying and virtual repositories to combine multiple sources into a single
repository. The following instructions are based on the [PyPI Repository
documentation for
Artifactory](https://docs.jfrog.com/artifactory/docs/pypi-repositories).

If you follow the recommended approach to rely on Chainguard Repository's
[upstream
fallback](/chainguard/libraries/introduction/overview/#upstream-fallback-and-controls), disable or remove any existing Artifactory remote repository
that points at the public PyPI index, and remove it from the virtual repository your
builds resolve against. A remote pointing directly at the public upstream bypasses
those protections. Since Artifactory resolves through the virtual repository in
order, a misconfiguration can result in Artifactory serving an unprotected
package.

### Initial configuration

Use the following steps to add Chainguard Libraries for Python as a remote repository:

1. Log in as a user with administrator privileges.
1. Click **Administration** in the top navigation bar.
1. Select **Repositories** in the left hand navigation.

Configure a remote repository for the Chainguard Libraries for Python index:

1. Select **Create a Repository** and choose the **Remote** option.
1. For **Package type**, select `PyPI`.
1. Set the **Repository Key** to `python-chainguard`.
1. Set the **URL** to `https://libraries.cgr.dev/`.
    * Do not include `/python` in
   the URL. Python's [Simple Repository
   API](https://peps.python.org/pep-0503/) keeps the package index on its own
   path which goes in the **PyPI Settings** fields below, and the base
   URL also needs to cover the `/python-upstream/` paths for upstream fallback packages.
1. Set **User Name** and **Password / Access Token** to the [values as retrieved
   with chainctl](/chainguard/libraries/introduction/access/).
    * Note: The **Test** button is not a reliable indicator; to verify your setup, refer to the [validation steps](#validate-the-remote-repository) later on this page.
1. Set the **PyPI Settings - Registry URL** to
   `https://libraries.cgr.dev/`.
1. Set the **PyPI Settings - Registry Index Location URL Suffix** to `python/simple`.
1. Click the **Advanced** configuration tab, then configure the following settings:
    * In the **Network** section:
        * Confirm **Lenient Host Authentication** is unchecked, so that your credentials are not forwarded across the redirect.
        * Optionally check **Enable Cookie Management**. JFrog recommends this for remote repositories that involve redirects.
    * In the **Others** section:
        * Check **Bypass HEAD Requests**, so that Artifactory retrieves each package file with a GET request instead of probing with a HEAD request first.
        * Uncheck **Block Mismatching Mime Types**.
        * Check **Disable URL Normalization**, so that Artifactory does not rewrite the pre-signed redirect URL.
1. Click **Create Remote Repository**.
1. If you want to use the separate repository with [remediated Python
libraries](/chainguard/libraries/python/overview/#cve-remediation) repeat the
preceding steps with the name `python-chainguard-remediated`, the same
authentication details, and the URL
`https://libraries.cgr.dev/python-remediated/`.

These settings are required because Chainguard Libraries stores artifacts in
Cloudflare R2. A package file download from `libraries.cgr.dev` returns a 302
redirect to a pre-signed URL on a different host, and the redirect response itself
is an HTML document. Without these settings, Artifactory may rewrite the
pre-signed URL, forward your credentials across the redirect, or cache the
redirect response in place of the wheel or source distribution. A cached redirect
response fails checksum verification at install time.

If you are manually managing fallback, rather than using the recommended [Chainguard Repository built-in fallback](/chainguard/libraries/introduction/overview/#upstream-fallback-and-controls) approach, configure an additional remote repository for the public PyPI index.

Create a virtual repository to give your build tools a single access point:

1. Click **Create a Repository** and choose the **Virtual** option.
1. Select `PyPI` as the Package type.
1. Set the **Repository Key** to `python-all`.
1. In the **Repositories** section, add `python-chainguard`. If you are using the remediated index, also add `python-chainguard-remediated` and ensure it is first in the displayed list, so that remediated versions resolve first. Use the icon on the right of the repository name to drag and drop repositories into the desired position.
    * If you are manually managing fallback, add the `python-public` repository and ensure it is last in the list.
1. Select **Create Virtual Repository**.

At this point, you have a virtual repository set up in Artifactory that allows
you or others in your organization to access Chainguard Libraries for Python,
optionally including remediated versions, with your chosen tools.

### Validate the remote repository

After creating the `python-chainguard` remote repository, validate that Artifactory is successfully proxying through to Chainguard before proceeding. A misconfigured remote repository fails silently; if any remote pointing at the public PyPI index is still present, Artifactory resolves through it instead and the build succeeds with no visible error. This can result in pulling an unprotected package.

Common sources of misconfiguration include invalid or expired credentials, or an incorrect or incomplete repository URL. As noted in the configuration steps, the Artifactory **Test connection** button is not a reliable indicator; it fails for a correctly configured Chainguard repository, and it may pass for an incorrectly configured one. Use the following steps instead to verify that fetching an artifact through Artifactory produces the same checksum as fetching it directly from `libraries.cgr.dev`.

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

* URL: The remote repository URL must be set to `https://libraries.cgr.dev/`.
* Credentials: You may need to regenerate your pull token with `chainctl auth pull-token --repository=python` and update the Artifactory repository credentials. Expired tokens fail silently.
* Advanced Configuration: Ensure all recommended Advanced settings from the [initial configuration steps](#initial-configuration-2) have been applied.
* Corrupted cached artifacts: if the repository previously ran without these settings, Artifactory may still be serving a cached redirect response. In Artifactory, browse the `python-chainguard` remote cache and locate the affected files. Right-click each artifact, select **Delete content**, then re-run your install.

Do not proceed to virtual repository setup or build configuration until the checksums match.

### Build tool access

Refer to the page on [build tool configuration for Chainguard Libraries for
Python](/chainguard/libraries/python/build-configuration/#artifactory) for
information on accessing credentials and setting up build tools.

<a id="nexus"></a>

## Sonatype Nexus Repository

[Sonatype Nexus
Repository](https://www.sonatype.com/products/sonatype-nexus-repository) allows
for merging multiple remote repositories as a repository group. The below
instructions are based on the [Nexus documentation for
PyPI](https://help.sonatype.com/en/pypi-repositories.html)

The recommended approach is to rely on Chainguard Repository's [upstream
fallback](/chainguard/libraries/introduction/overview/#upstream-fallback-and-controls),
configuring a single proxy repository pointed at `https://libraries.cgr.dev/python/`
rather than adding a separate public PyPI proxy. Refer to [Manually managing
fallback](#manually-managing-fallback) if you need to control fallback ordering
yourself.

### Initial configuration

The following steps create a remote repository for Chainguard Libraries for
Python and a repository group that exposes it to your build tools.

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
   chainctl](/chainguard/libraries/introduction/access/).
1. Select **Create repository**.

If you want to use the separate repository with [remediated Python
libraries](/chainguard/libraries/python/overview/#cve-remediation) repeat the
preceding steps with the name `python-chainguard-remediated`, the same
authentication details, and the URL
`https://libraries.cgr.dev/python-remediated/`.

If you are manually managing fallback rather than using the [Chainguard Repository's built-in fallback](/chainguard/libraries/introduction/overview/#upstream-fallback-and-controls), configure an additional remote repository for the public PyPI.

Finally, create a new repository group and add the repositories:

1. Select **Repository - Repositories** in the left hand navigation.
1. Select **Create repository**.
1. Select the **PyPI (group)** recipe.
1. Provide a new name, such as `python-all`.
1. In the section **Group - Member repositories**, move the new repositories
   `python-chainguard-remediated` and `python-chainguard` to the right. Move the  `python-chainguard-remediated` repository to the top of the list.

### Build tool access

Refer to the page on [build tool configuration for Chainguard Libraries for
Python](/chainguard/libraries/python/build-configuration/#nexus) for information on
accessing credentials and setting up build tools.

## Troubleshooting and FAQ

### Sonatype build failures and 404 errors for uv and pip requests ending in `.whl.metadata`

Builds fail intermittently when Sonatype Nexus is configured as a PyPI proxy in front of `libraries.cgr.dev`, even though authentication, entitlements, and network connectivity all check out. The failures look like missing packages, but the packages themselves are present and downloadable. The Nexus outbound request logs show 404 responses specifically for URLs ending in `.whl.metadata`, while the same URL without the `.metadata` suffix succeeds.

Modern Python installers (pip 23.1+, uv) implement [PEP 658](https://peps.python.org/pep-0658/) and request a small per-package metadata file by appending `.metadata` to the wheel's download URL, ahead of downloading the wheel itself. When Nexus is serving a stale cached index page, it can point clients at a metadata URL format that `libraries.cgr.dev` no longer honors. Chainguard's upstream returns 400 for that request, which Nexus in turn surfaces to the client as a 404. The result presents as a missing package, when the underlying issue is a stale cached index.

#### Fix: Recreate the proxy repository

To fix this, delete and recreate the Chainguard PyPI proxy repository in Nexus. This clears all cached index pages and metadata assets for that repository, forcing Nexus to pull fresh copies on the next request.

Alternatively, you could add a Nexus routing rule to block metadata requests outright. Clients fall back to standard resolution automatically when the metadata request fails cleanly, without surfacing an error:

1. In Nexus, go to **Administration** > **Routing Rules** and create a new rule.
1. Set the Mode to `Block`.
1. Set the matcher to `.*\.metadata$`.
1. Assign the rule to your Chainguard PyPI proxy repository.
1. Remove the routing rule once you've recreated the proxy repository, so clients can resume using PEP 658 metadata requests.
