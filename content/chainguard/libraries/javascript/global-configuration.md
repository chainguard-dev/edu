---
title: "Global configuration"
linktitle: "Global configuration"
description: "Configuring Chainguard Libraries for JavaScript in your organization"
type: "article"
date: 2025-06-05T09:00:00+00:00
lastmod: 2025-06-05T09:00:00+00:00
draft: false
tags: ["Chainguard Libraries", "JavaScript"]
images: []
menu:
  docs:
    parent: "javascript"
    identifier: "JavaScript Global Configuration"
weight: 052
toc: true
---

JavaScript and npm package consumption in a large organization is typically
managed by a repository manager. Commonly used repository manager applications
are [JFrog Artifactory](https://jfrog.com/artifactory/), [Sonatype Nexus
Repository](https://www.sonatype.com/products/sonatype-nexus-repository), and
others. The repository manager acts as a single point of access for developers
and development tools to retrieve the required libraries.

If your organization uses the [upstream fallback](/chainguard/libraries/overview/#upstream-fallback-and-controls)
feature of Chainguard Repository, you can configure your repository manager
with a single upstream pointed at `https://libraries.cgr.dev/javascript/`. This
is the recommended setup. The Chainguard Repository handles fallback and policy
enforcement; your repository manager handles local caching and access control.
Chainguard also retrieves packages from the public npm Registry on your
behalf when upstream fallback is enabled. This includes protections such as
malware detection and a cooldown period for newly published
packages.

At a high level, adopting the use of Chainguard Libraries consists of the following steps:

* Configure your environment to use `https://libraries.cgr.dev/javascript/`
  as the single upstream source for JavaScript package retrieval. This can be done
  either:
    * As a remote repository in your repository manager, or
    * Directly in your JavaScript build configuration (for example, npm,
      pnpm, or yarn).
* Additional steps depend on your visibility and validation goals and can include the following optional measures:
    * Remove all cached libraries in existing proxy repositories. This step
      allows you to validate which libraries are not available from
      Chainguard Libraries and ensures they are retrieved through
      Chainguard for evaluation.
    * Remove any repositories that are no longer desired or necessary.
      Depending on your library requirements, this step can result in
      removal of some proxy repositories or simplification of your
      repository configuration.

Adopting the use of a repository manager is the recommended approach to minimize complexity. If your organization does not use a repository manager, refer to the [direct access documentation](/chainguard/libraries/javascript/build-configuration/) for build tools.

## Manually managing fallback

Chainguard recommends using the Chainguard Repository's built-in [upstream
fallback](/chainguard/libraries/javascript/overview/#upstream-fallback-policy-and-controls)
rather than configuring a public registry fallback in your repo manager.
Configuring your own fallback bypasses the protection that the Chainguard
Repository provides.

However, if upstream fallback is not enabled or you prefer to manage your own fallback
ordering, you can configure `https://libraries.cgr.dev/javascript/` as a remote
repository alongside your npm upstream, and combine them in a virtual or group
repository with Chainguard as the first priority. The per-tool instructions on
this page follow this pattern.

### Updating lockfile hashes

If you are migrating an existing JavaScript project to Chainguard Libraries through a repository manager, your lockfile likely contains integrity hashes generated against packages previously downloaded from npm or through your repository manager. The [`chainctl libraries update-hashes` command](/chainguard/chainctl/chainctl-docs/chainctl_libraries_update-hashes/) automates lockfile hash updates
for all supported JavaScript lockfile formats.

When you are using a repository manager, pass the full repository manager URL with `--registry-url` and authenticate with one of the supported methods: `--username` and `--password`, `--token`, or a `.netrc` entry for the registry host. For example:

```bash
chainctl libraries update-hashes \
  --registry-url https://repo.example.com:8443/repository/javascript-all/ \
  --token "$REPO_TOKEN"
```

After updating the lockfile, keep your repository manager configuration in place and reinstall through the same repository manager endpoint to apply the updated hashes.

Learn more in the [Build configuration page](/chainguard/libraries/javascript/build-configuration/#updating-lockfile-hashes/) and in the [chainctl docs](/chainguard/chainctl/chainctl-docs/chainctl_libraries_update-hashes/).

<a name="cloudsmith"></a>

## Cloudsmith

[Cloudsmith](https://cloudsmith.com/) supports npm registries for
proxying and hosting. Refer to the [npm registry
documentation](https://help.cloudsmith.io/docs/npm-registry) and the [npm
Upstream
documentation](https://help.cloudsmith.io/docs/upstream-proxying-caching#create-a-npm-upstream)
for Cloudsmith for more information. Cloudsmith supports combining repositories
by defining multiple upstream repositories.

### Initial configuration

Use the following steps to configure a repository with the Chainguard Libraries for
JavaScript repository as an upstream.

Configure a *javascript-all* repository. This repository acts as a single access point
for JavaScript packages and may also include private packages or additional upstream
sources, depending on your configuration.

1. Log in as a user with administrator privileges.
1. Select the **Repositories** tab near the top of the screen.
1. On the **Repositories** page, click **+ New repository**.
1. Enter the name *javascript-all* for your new repository. The name should
   include *javascript* to identify the ecosystem. This convention helps
   avoid confusion since repositories in Cloudsmith are multi-format.
1. Select a storage region that is appropriate for your organization and
   infrastructure.
1. Click **+ Create Repository**.

Configure an upstream proxy for the Chainguard Libraries for JavaScript
repository:

1. Click the name of the new *javascript-all* repository on the
   repositories page to configure it.
1. Access the **Upstreams** tab and click **+ Add Upstream Proxy**.
1. Configure an upstream proxy with the format **npm** and the following details:
    * **Name** *javascript-chainguard*
    * **Priority** *1*
    * **Proxy URL** `https://libraries.cgr.dev/javascript/`
    * **Mode** *Cache and Proxy*
    * Add the **Username** and **Password** value from [Chainguard Libraries
      access](/chainguard/libraries/access/) in **Authentication Settings**
1. Click **Create Upstream Proxy**.

If you are manually managing fallback, you can add an additional upstream
proxy for the public npm registry with a lower priority than
`javascript-chainguard`.

Use this setup for initial testing with Chainguard Libraries for JavaScript. For
production usage, add the `javascript-chainguard` upstream proxy to your production
repository.

### Build tool access

The following steps allow you to determine the URL and authentication details
for accessing the repository:

1. Select the **Packages** tab.
1. Click **Push/Pull Packages**.
1. Choose the format **NPM**.
1. Refer to the **Pull Package** tab.
1. Note the registry URL and syntax from the code snippets for npm. For example,
   the URL for the registry in the `example` organization is
   `https://npm.cloudsmith.io/example/javascript-all/`.
1. Note that authentication is using an authentication token and the syntax for
   npm in the `example` organization is
   `//npm.cloudsmith.io/example/javascript-all/:_authToken=YOUR-API-KEY`

Use the provided code snippets directly for your use with npm, or adjust as
necessary for other JavaScript build and packaging tools. Find relevant details
in the [Build
Configuration](/chainguard/libraries/javascript/build-configuration/) and
specific packaging tool documentation.

Use the following steps to retrieve the necessary API key as an authentication
token for the registry access:

1. Click on your user name at the top right corner.
1. Select **Personal API keys**.
1. Authenticate again in the **Confirm access** dialog.
1. Create a new token or refresh the existing one in case you lost the token
   value.

<a name="artifactory"></a>

## JFrog Artifactory

[JFrog Artifactory](https://jfrog.com/artifactory/) supports npm repositories
for proxying and hosting, and virtual repositories to combine them. Refer to the
[npm Repository documentation for
Artifactory](https://docs.jfrog.com/artifactory/docs/npm-repositories)
for more information.

### Initial configuration

Use the following steps to add Chainguard Libraries for
JavaScript as a remote repository:

1. Log in as a user with administrator privileges.
1. Click **Administration** in the top navigation bar.
1. Select **Repositories** in the left hand navigation.

Configure a remote repository for the Chainguard Libraries for JavaScript
repository:

1. Click **Create a Repository** and choose the **Remote** option.
1. Select *Npm* as the **Package type**.
1. Set the **Repository Key** to `javascript-chainguard`.
1. Set the **URL** to `https://libraries.cgr.dev/javascript/`.
1. Set **User Name** and **Password / Access Token** to the [values as retrieved
   with chainctl](/chainguard/libraries/access/).
1. Click the **Advanced** configuration tab, then check the box next to **Disable URL Normalization**.
1. Click **Create Remote Repository**.

Create a virtual repository, or add the remote repository to an existing
virtual repository used for npm packages. A virtual repository may also include private npm packages or
additional upstream sources, depending on your configuration.

1. Click **Create a Repository** → **Virtual**.
1. Select **Npm**.
1. Set key to *javascript-all*.
1. Add `javascript-chainguard`.
1. Click **Create Virtual Repository**.

If you are manually managing fallback, you can configure an additional npm
remote repository with lower priority.

Use this setup for initial testing with Chainguard Libraries for JavaScript. For
production usage add the `javascript-chainguard` repository to your production
virtual repository.

### Advanced settings for redirect handling

Chainguard Libraries uses Cloudflare R2 storage, meaning tarball downloads from
`libraries.cgr.dev` return a 302 redirect to a different host. Without
additional configuration, Artifactory may cache the redirect response instead of
the actual tarball, causing npm integrity checksum failures at install time.

To prevent this:

1. Apply the following settings to your Artifactory `javascript-chainguard`
   remote repository, within in the **Advanced** tab:
    * **Enable Bypass HEAD Requests** — prevents Artifactory from sending HEAD
      requests that may not be handled correctly by redirect-based registries.
    * **Disable Lenient Host Authentication** — disabling this setting ensures
      credentials are not forwarded across the redirect.
    * **Enable Cookie Management** - this setting is optional, but recommended
      by JFrog for remote repositories that involve redirects.
2. Clear the corrupted cached tarballs: in Artifactory, right-click the
   `javascript-chainguard` repository and click **Zap Caches**, then re-run your
   install.
    * Alternatively, you could delete specific corrupted `.tgz` artifacts from
      the remote cache, rather than deleting all, before re-running the install.

### Validate the remote repository

After creating and configuring the `javascript-chainguard` remote repository, validate that Artifactory is successfully proxying through to Chainguard before proceeding. Because Artifactory falls back to the upstream npm registry when a connection to a remote repository fails, a misconfigured repository may silently resolve packages from npm rather than Chainguard — and the build will succeed without any visible error.

Common sources of misconfiguration include invalid or expired credentials, an incorrect or incomplete URL, and misconfigured [settings in the Advanced tab](#advanced-settings-for-redirect-handling). The Artifactory **Test** button on the repository configuration screen is not a reliable indicator; it may fail for a correctly configured repository, and may pass for an incorrectly configured one. Instead, use the following steps to verify that fetching an artifact through Artifactory produces the same checksum as fetching it directly from `libraries.cgr.dev`.

1. Fetch the artifact directly from Chainguard and compute its checksum, using the same credentials you configured in Artifactory. This example uses `picocolors-1.1.1`. You can substitute any artifact you know to be available.

```bash
curl -sSf -L \
  -u "${CHAINGUARD_JAVASCRIPT_IDENTITY_ID}:${CHAINGUARD_JAVASCRIPT_TOKEN}" \
  https://libraries.cgr.dev/javascript/picocolors/-/picocolors-1.1.1.tgz \
  | openssl dgst -sha512 -binary | base64
```

1. Fetch the same artifact through the Artifactory remote repository and compute its checksum:

```bash
curl -sSf -L \
  -H "Authorization: Bearer ${ARTIFACTORY_TOKEN}" \
  https://<artifactory-host>/artifactory/api/npm/javascript-chainguard/picocolors/-/picocolors-1.1.1.tgz \
  | openssl dgst -sha512 -binary | base64
```

Replace `artifactory-host` with your Artifactory instance hostname, and replace `${ARTIFACTORY_TOKEN}` with your Artifactory identity token.

1. If your configuration includes a virtual repository combining `javascript-chainguard` with a public npm fallback, test that as well:

```bash
curl -sSf -L \
  -H "Authorization: Bearer ${ARTIFACTORY_TOKEN}" \
  https://<artifactory-host>/artifactory/api/npm/javascript-all/picocolors/-/picocolors-1.1.1.tgz \
  | openssl dgst -sha512 -binary | base64
```

The checksums returned by the commands must match.

If the checksum from the Artifactory remote or virtual repository differ from the direct fetch, or if the Artifactory fetch fails entirely, review the following before proceeding:

* URL: The remote repository URL must be set to `https://libraries.cgr.dev/javascript/`.
* Credentials: You may need to regenerate your pull token with `chainctl auth pull-token --repository=javascript` and update the Artifactory repository credentials. Expired tokens fail silently.
* [Advanced tab settings](#advanced-settings-for-redirect-handling): Confirm that **Bypass HEAD Requests** is enabled and **Lenient Host Authentication** is disabled.

Do not proceed to virtual repository setup or build configuration until the checksums match.

### Build tool access

The following steps allow you to determine the URL and authentication details
for accessing the repository:

1. Click **Administration** in the top navigation bar.
1. Select **Repositories** in the left hand navigation.
1. Select the **Virtual** tab in the repositories view.
1. Locate the *javascript-all* repository.
1. Hover over the row and click the **...** in the last column on the right.
1. Select **Set Me Up** in the dialog.
1. Click **Generate Token & Create Instructions**.
1. Copy the generated token value to use as the password for authentication.
1. Click **Generate Settings**.
1. Copy the value from a **url** field. They are all identical. For example,
   `https://exampleorg.jfrog.io/artifactory/javascript-all/` with `exampleorg`
   replaced with the name of your organization.

Use the URL of the virtual repository in the [build
configuration](/chainguard/libraries/javascript/build-configuration/) and build a
first test project. In a working setup the chainguard remote repository contains
all libraries retrieved from Chainguard.

<a name="nexus"></a>

## Sonatype Nexus Repository

[Sonatype Nexus
Repository](https://www.sonatype.com/products/sonatype-nexus-repository) allows
for merging multiple remote repositories as a repository group. The below
instructions are based on the [Nexus documentation for
npm](https://help.sonatype.com/en/npm-registry.html).

### Initial configuration

For initial testing and adoption it is advised to create a separate proxy repository
for the Chainguard Libraries for JavaScript repository, and include it in a repository group:

1. Log in as a user with administrator privileges.
1. Access the **Server administration** and configuration section with the gear
   icon in the top navigation bar.

Configure a proxy repository for the Chainguard Libraries for JavaScript
repository:

1. Select **Repository - Repositories** in the left hand navigation.
1. Click **Create repository**.
1. Select the **npm (proxy)** recipe.
1. Provide a new name *javascript-chainguard*.
1. In the **Proxy - Remote storage** input add the URL
   `https://libraries.cgr.dev/javascript/`.
1. In **HTTP - Authentication** with the **Authentication type** *Username*,
   provide the [username and password values as retrieved with
   chainctl](/chainguard/libraries/access/).
1. Click **Create repository**.

Create a repository group, or add to an existing repository group:

1. Select **Repository - Repositories** in the left hand navigation.
1. Click **Create repository**.
1. Select the **npm (group)** recipe.
1. Provide a new name *javascript-all*.
1. In the section **Group - Member repositories**, move the new repository
   `javascript-chainguard` to the right to include it in the group. Position
   `javascript-chainguard` at the top of the list using the arrow controls.

Repository groups can include multiple repositories, such as hosted
repositories for private packages or additional proxy repositories. In a
typical configuration, the Chainguard repository is placed first to ensure
packages are retrieved through Chainguard when available.

If you are manually managing fallback, you can configure an additional npm
proxy repository and add it to the group after *javascript-chainguard*.

### Build tool access

The following steps allow you to determine the URL and authentication details
for accessing the repository:

1. Click **Browse** in the **Welcome** view or the browse icon (cube) in the top
   navigation bar.
1. Locate the **URL** column for the *javascript-all* repository group and click
   **copy**. For example, `https://repo.example.com/repository/javascript-all/`
   with `repo.example.com` replaced with the hostname of your repository manager.
1. Copy the URL in the dialog.
1. Use your configured username and password unless **Security** - **Anonymous
   Access** - **Access** - **Allow anonymous users to access the server** is
   activated. Details vary based on your configured authentication system.

Use the URL of the repository group, such as
`https://repo.example.com/repository/javascript-all/` in the [build
configuration](/chainguard/libraries/javascript/build-configuration/) and build a
first test project. In a working setup the `javascript-chainguard` proxy
repository contains all libraries retrieved from Chainguard.

## Google Artifact Registry

Google Artifact Registry (GAR) is not an officially supported repository manager for Chainguard Libraries for JavaScript. However, it has been shown to work with the following configuration.

Configure two GAR remote repositories, with upstream validation disabled on the second:

* First remote repository: `javascript-chainguard` pointing to `https://libraries.cgr.dev/javascript` with upstream validation enabled
* Second remote repository: `javascript-chainguard-upstream` pointing to `https://libraries.cgr.dev/javascript-upstream` with upstream validation disabled.

When using `artifactregistry-auth`, note that it only injects credentials for repositories explicitly listed in your `.npmrc`. Ensure you add a credentials entry for the `javascript-chainguard-upstream` repository alongside your existing `javascript-chainguard` entry, otherwise you will receive 404s for upstream-fallback packages.

## AWS CodeArtifact

AWS CodeArtifact is not an officially supported repository manager for Chainguard Libraries for JavaScript. However, it has been shown to work with the following configuration.

Because CodeArtifact doesn't support proxying authenticated upstream repositories, these instructions show how to mirror JavaScript packages from Chainguard Libraries into CodeArtifact. After configuring a mirror, configure developers and CI systems to install packages from your private CodeArtifact repository.

If you use Chainguard Repository with upstream fallback enabled, npm clients can point directly to the Chainguard endpoint and retrieve either Chainguard-built packages or policy-protected upstream packages through that single registry. Use the CodeArtifact mirroring workflow only if your organization needs to keep AWS CodeArtifact as the registry your developers install from.

### Prerequisites

You will need the following:

* An AWS account with the following IAM permissions:
    * `codeartifact:PublishPackageVersion`
    * `codeartifact:PutPackageMetadata`
    * `codeartifact:GetAuthorizationToken`
    * `codeartifact:GetRepositoryEndpoint`
* A Chainguard account with entitlement to Chainguard Libraries for JavaScript and credentials you can use to authenticate to the registry.
* The AWS CLI, Node.js and npm, `jq`, and `bash`. If you use pnpm lockfiles, you also need the Go `mikefarah` build of `yq` v4.

This workflow supports both `package-lock.json` and `pnpm-lock.yaml`. For pnpm, the parser supports lockfile versions v5, v6, and v9. Scoped packages such as `@types/node` and `@babel/core` are also supported.

> Note: This workflow preserves standard npm attestations embedded in tarballs, but Chainguard-specific registry metadata is not preserved in the mirrored repository. Because AWS CodeArtifact charges for storage and requests, you should monitor repository growth over time and clean up unused package versions as needed.

### Step 1: Create a CodeArtifact domain and repository

You can create the CodeArtifact resources manually with the AWS CLI:

```bash
export AWS_REGION="us-east-1"

aws codeartifact create-domain \
  --domain npm-mirror-test \
  --region $AWS_REGION

aws codeartifact create-repository \
  --domain npm-mirror-test \
  --repository cg-npm-packages \
  --description "npm packages mirror from Chainguard" \
  --region $AWS_REGION
```

After setup, export the values the mirroring workflow uses:

```bash
export AWS_REGION="us-east-1"
export CODEARTIFACT_DOMAIN="npm-mirror-test"
export CODEARTIFACT_REPOSITORY="cg-npm-packages"
export CGR_USER="your-chainguard-identity"
export CGR_TOKEN="your-chainguard-token"
```

`CODEARTIFACT_DOMAIN_OWNER` is optional. If you do not set it, the workflow can use your current AWS account ID.

### Step 2: Mirror packages from a lockfile

This guide uses a script named `npm-codeartifact-mirror.sh`. Access the bash script and learn more about it in [Chainguard's example on GitHub](https://github.com/chainguard-demo/platform-examples/tree/main/library-copy-aws-code-artifact).

Before running the script, save it to a local working directory and make it executable:

```bash
chmod +x npm-codeartifact-mirror.sh
```

The mirroring workflow reads a project lockfile, extracts package names and versions, checks whether each version already exists in CodeArtifact, downloads missing packages from Chainguard Libraries, and publishes them into your private CodeArtifact repository.

Run the script against either an npm or pnpm lockfile:

```bash
./npm-codeartifact-mirror.sh ./package-lock.json
```

```bash
./npm-codeartifact-mirror.sh ./pnpm-lock.yaml
```

If you do not pass a file path, the script automatically looks for `package-lock.json` and then `pnpm-lock.yaml` in the current directory.

### How mirroring behaves

The mirroring workflow runs in multiple passes. On the first pass, it skips versions that already exist in CodeArtifact and attempts to download and publish everything else. If a package is not yet available because Chainguard is still ingesting it from upstream, the workflow queues that package for a later retry.

By default, the workflow retries unavailable packages up to four times with a 30-second delay between passes. You can tune this behavior with `INGEST_MAX_PASSES` and `INGEST_RETRY_DELAY`.

For transient npm transport failures such as socket timeouts, rate limits, or 5xx responses, you can also tune `NPM_FETCH_RETRIES` and `NPM_FETCH_TIMEOUT`.

### Step 3: Verify mirrored packages

After the mirror completes, use the AWS CLI to verify that packages were published to CodeArtifact:

```bash
aws codeartifact list-packages \
  --domain $CODEARTIFACT_DOMAIN \
  --repository $CODEARTIFACT_REPOSITORY \
  --format npm

aws codeartifact list-package-versions \
  --domain $CODEARTIFACT_DOMAIN \
  --repository $CODEARTIFACT_REPOSITORY \
  --package lodash \
  --format npm
```

For scoped packages, use the `--namespace` parameter:

```bash
aws codeartifact list-package-versions \
  --domain $CODEARTIFACT_DOMAIN \
  --repository $CODEARTIFACT_REPOSITORY \
  --package fs-minipass \
  --namespace isaacs \
  --format npm
```

If any packages could not be mirrored, the workflow writes an unresolved package report. Each line includes the reason and package version, such as `404`, `ETARGET`, or `AUTH`.

### Step 4: Configure npm clients to install from CodeArtifact

Once the packages are mirrored, authenticate to CodeArtifact and point npm at your repository endpoint:

```bash
export CODEARTIFACT_AUTH_TOKEN=$(aws codeartifact get-authorization-token \
  --domain $CODEARTIFACT_DOMAIN \
  --query authorizationToken \
  --output text \
  --region $AWS_REGION)

export CODEARTIFACT_REGISTRY=$(aws codeartifact get-repository-endpoint \
  --domain $CODEARTIFACT_DOMAIN \
  --repository $CODEARTIFACT_REPOSITORY \
  --format npm \
  --query repositoryEndpoint \
  --output text \
  --region $AWS_REGION)

npm config set registry $CODEARTIFACT_REGISTRY
npm config set //$(echo $CODEARTIFACT_REGISTRY | sed 's|https://||')/:_authToken $CODEARTIFACT_AUTH_TOKEN
```

You can then install packages as usual:

```bash
npm install
```

As an alternative, you can use `aws codeartifact login` for npm:

```bash
aws codeartifact login \
  --tool npm \
  --domain $CODEARTIFACT_DOMAIN \
  --repository $CODEARTIFACT_REPOSITORY \
  --region $AWS_REGION
```

### Troubleshooting

#### Authentication and AWS permissions

If you cannot get a CodeArtifact authorization token or publish packages, verify your AWS credentials and IAM permissions. The workflow specifically relies on permissions such as `codeartifact:PublishPackageVersion`, `codeartifact:PutPackageMetadata`, `codeartifact:GetAuthorizationToken`, and `codeartifact:GetRepositoryEndpoint`.

CodeArtifact tokens expire after 12 hours. If authentication starts failing later, request a new token and retry.

#### Packages are still unavailable

If packages remain unavailable after all retry passes, Chainguard may still be ingesting them, they may be in a cooldown period, they may be blocked for security reasons, or the requested version may not exist. Re-running the workflow later, or increasing `INGEST_MAX_PASSES` and `INGEST_RETRY_DELAY`, can help pick up packages that were still within the ingestion window during an earlier run.

#### pnpm parsing issues

If you use pnpm and the workflow reports zero packages or fails because of `yq`, make sure you are using the Go `mikefarah` build of `yq` v4 rather than the Python `kislyuk` implementation.
