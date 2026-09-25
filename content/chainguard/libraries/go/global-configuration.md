---
title: "Global configuration"
linktitle: "Global configuration"
description: "Configuring Chainguard Libraries for Go in your organization"
type: "article"
date: 2026-09-25T00:00:00+00:00
lastmod: 2026-09-25T20:37:28+00:00
draft: false
tags: ["Chainguard Libraries", "Go"]
images: []
menu:
  docs:
    parent: "go"
    identifier: "Go Global Configuration"
weight: 052
toc: true
---

Go module consumption in a large organization is typically managed by a repository manager. The repository manager acts as a single point of access for developers and development tools to retrieve Go modules.

Configure Artifactory with a single remote repository pointed at `https://libraries.cgr.dev/go/`. Chainguard Repository handles upstream fallback and policy enforcement; Artifactory handles local caching, access control, and the endpoint used by your Go toolchains.

## JFrog Artifactory

JFrog Artifactory supports Go repositories for proxying and hosting Go modules, and virtual repositories for combining sources into one endpoint. Refer to the [Go repositories documentation for Artifactory](https://docs.jfrog.com/artifactory/docs/go-repositories) for more information.

If an existing Artifactory remote repository points directly to a public Go module proxy, disable or remove it from the virtual repository that your builds use. Artifactory resolves virtual repositories according to their configured order, so a misconfiguration can cause an unprotected module to be served without an obvious build failure.

### Prerequisites

Before you begin, you need:

- An [entitlement to Chainguard Libraries for Go](/chainguard/libraries/go/migration/#create-an-entitlement)
- Administrator access to your repository manager instance
- A [pull token for Chainguard Libraries for Go](/chainguard/libraries/go/migration/#create-a-pull-token)

### Initial configuration

Use the following steps to add Chainguard Libraries for Go as an Artifactory remote repository:

1. Sign in to Artifactory as a user with administrator privileges.
1. Click **Administration** in the top navigation bar.
1. In the left navigation, click **Repositories**.
1. Click **Create a Repository**, then choose **Remote**.
1. Configure the remote repository with the following values:
    - **Package type**: Go
    - **Repository key**: `go-chainguard`
    - **URL**: `https://libraries.cgr.dev/go/`
    - **Username**: the username returned by `chainctl`
    - **Password**: the password returned by `chainctl`
1. Open the **Advanced configuration** tab and configure the following:
    - In the **Network** section, confirm that **Lenient Host Authentication** is unchecked. This prevents Artifactory from forwarding credentials across a redirect.
    - Optionally select **Enable Cookie Management**. JFrog recommends this for remote repositories that use redirects.
    - In the **Others** section, select **Bypass HEAD Requests** so that Artifactory retrieves package files with GET requests instead of probing with HEAD requests first.
    - In the **Others** section, uncheck **Block Mismatching Mime Types**.
    - Select **Disable URL Normalization** so that Artifactory does not rewrite a pre-signed redirect URL.
1. Click **Create Remote Repository**.

Chainguard Libraries serves module metadata and source archives through the standard Go module proxy protocol. Some module files may be served through redirects to pre-signed storage URLs. These settings prevent Artifactory from rewriting the redirect, forwarding credentials to another host, or caching a redirect response instead of the module file.

### Create a virtual repository

Create a virtual repository to give developers and CI systems a single Go module endpoint:

1. Click **Create a Repository**, then choose **Virtual**.
1. Configure the virtual repository with the following values:
    - **Package type**: Go
    - **Repository Key**: `go-all`
    - **Repositories**: add `go-chainguard`
1. Click **Create Virtual Repository**.

For the recommended configuration, `go-chainguard` should be the only external upstream in `go-all`.

### Validate the remote repository

Validate the Artifactory remote before configuring developer workstations or CI/CD systems. The Artifactory **Test** button is not a reliable indicator of a working Chainguard configuration; a remote can pass the test but still be misconfigured for package retrieval.

Use a module and version that are available through your organization's Chainguard Libraries for Go entitlement. The following example uses `rsc.io/quote` version `v1.5.2`:

Fetch the module archive directly from Chainguard and compute its checksum:

```bash
 curl -fsS -L \\
   -u "${CHAINGUARD_GO_IDENTITY_ID}:${CHAINGUARD_GO_TOKEN}" \\
   "https://libraries.cgr.dev/go/rsc.io/quote/@v/v1.5.2.zip" \\
   | sha256sum
```

Fetch the same archive through the Artifactory remote repository and compute its checksum:

```bash
 curl -fsS -L \\
   -u "${ARTIFACTORY_USERNAME}:${ARTIFACTORY_TOKEN}" \\
   "https://<artifactory-host>/artifactory/go-chainguard/rsc.io/quote/@v/v1.5.2.zip" \\
   | sha256sum
```

Replace `artifactory-host` with your Artifactory hostname. Replace `ARTIFACTORY_USERNAME` and `ARTIFACTORY_TOKEN` with credentials that can read from Artifactory.

Fetch the archive through the virtual repository that developers and CI systems will use:

```bash
 curl -fsS -L \\
   -u "${ARTIFACTORY_USERNAME}:${ARTIFACTORY_TOKEN}" \\
   "https://<artifactory-host>/artifactory/go-all/rsc.io/quote/@v/v1.5.2.zip" \\
   | sha256sum
```

The three checksums must match. Do not proceed to production rollout if the Artifactory checksum differs from the direct Chainguard checksum or if either Artifactory request fails.

If validation fails, review the following settings:

- URL: confirm that the remote repository URL is exactly https://libraries.cgr.dev/go/.
- Credentials: regenerate the pull token with `chainctl auth pull-token create --repository=go` and update the Artifactory remote repository credentials. Expired tokens can fail without a clear error in the Artifactory user interface.
- Advanced configuration: confirm that the redirect and request settings from the initial configuration are applied.
- Cached files: if the remote repository was previously configured with incorrect settings, delete the affected cached module files from the `go-chainguard` cache and repeat the validation.
- Virtual repository order: confirm that no public Go proxy appears ahead of `go-chainguard` or is still included in `go-all`.

### Configure build tools

Use the URL of the `go-all` virtual repository in Go configuration. In Artifactory, select the `go-all` repository and use **Set Me Up** or **Generate Settings** to obtain the URL and authentication instructions for your Artifactory version. The URL commonly has the following form: `https://exampleorg.jfrog.io/artifactory/go-all`.

See [Configuring your build tool](/chainguard/libraries/go/build-configuration/#repository-manager) for more information.
