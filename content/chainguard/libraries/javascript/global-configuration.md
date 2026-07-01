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

If your organization uses the [upstream fallback](/chainguard/libraries/javascript/overview/#upstream-fallback-policy-and-controls)
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

### Manually managing fallback
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
[npm registry documentation for
Artifactory](https://jfrog.com/help/r/jfrog-artifactory-documentation/npm-registry)
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
1. Click the **Advanced** configuration tab. Disable **URL Normalization**
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
    - **Enable Bypass HEAD Requests** — prevents Artifactory from sending HEAD
      requests that may not be handled correctly by redirect-based registries.
    - **Disable Lenient Host Authentication** — disabling this setting ensures
      credentials are not forwarded across the redirect. 
    - **Enable Cookie Management** - this setting is optional, but recommended
      by JFrog for remote repositories that involve redirects.
2. Clear the corrupted cached tarballs: in Artifactory, right-click the
   `javascript-chainguard` repository and click **Zap Caches**, then re-run your
   install.
    - Alternatively, you could delete specific corrupted `.tgz` artifacts from
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

2. Fetch the same artifact through the Artifactory remote repository and compute its checksum:

```bash
curl -sSf -L \
  -H "Authorization: Bearer ${ARTIFACTORY_TOKEN}" \
  https://<artifactory-host>/artifactory/api/npm/javascript-chainguard/picocolors/-/picocolors-1.1.1.tgz \
  | openssl dgst -sha512 -binary | base64
```
Replace `artifactory-host` with your Artifactory instance hostname, and replace `${ARTIFACTORY_TOKEN}` with your Artifactory identity token.

3. If your configuration includes a virtual repository combining `javascript-chainguard` with a public npm fallback, test that as well:

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

This guide uses a script named `npm-codeartifact-mirror.sh`. Expand the following to view the script:

{{< details "CodeArtifact mirror script" >}}

```sh
#!/bin/bash

# npm-codeartifact-mirror.sh
# Mirrors npm packages from Chainguard Libraries to AWS CodeArtifact
# This script reads package-lock.json or pnpm-lock.yaml, checks availability in
# Chainguard Libraries, downloads packages with proper authentication, and publishes
# them to CodeArtifact.
#
# DISCLAIMER:
# This script is provided as an example without warranty of any kind, either expressed
# or implied, including but not limited to the implied warranties of merchantability
# and fitness for a particular purpose. Use at your own risk. No support is provided.
#
# Usage: ./npm-codeartifact-mirror.sh [path-to-lock-file]
#   Supports package-lock.json (npm) and pnpm-lock.yaml (pnpm)
#   Auto-detects the lock file if no argument is provided

set -e

# Configuration
CHAINGUARD_REGISTRY="https://libraries.cgr.dev/javascript/"
TEMP_DIR="${TEMP_DIR:-./temp_packages}"
LOG_FILE="${LOG_FILE:-./mirror.log}"
NPM_CONFIG_CHAINGUARD=".npmrc.chainguard"
NPM_CONFIG_CODEARTIFACT=".npmrc.codeartifact"

# npm transport robustness. These handle TRANSIENT failures (network blips,
# socket timeouts, 429/5xx) — note they do NOT retry 404/ETARGET, which npm
# treats as definitive; that case is handled by the multi-pass retry loop in
# process_packages instead.
NPM_FETCH_RETRIES="${NPM_FETCH_RETRIES:-5}"
NPM_FETCH_TIMEOUT="${NPM_FETCH_TIMEOUT:-60000}"

# Required environment variables (set these before running)
# CGR_USER - Chainguard user/identity
# CGR_TOKEN - Chainguard authentication token
# AWS_REGION (e.g., us-east-1)
# CODEARTIFACT_DOMAIN
# CODEARTIFACT_REPOSITORY
# CODEARTIFACT_DOMAIN_OWNER (optional, will use AWS account ID if not set)

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Logging functions
log() {
    echo -e "${GREEN}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1" | tee -a "$LOG_FILE"
}

warn() {
    echo -e "${YELLOW}[$(date +'%Y-%m-%d %H:%M:%S')] WARNING:${NC} $1" | tee -a "$LOG_FILE"
}

error() {
    echo -e "${RED}[$(date +'%Y-%m-%d %H:%M:%S')] ERROR:${NC} $1" | tee -a "$LOG_FILE"
}

# Check required environment variables
check_env() {
    local missing=0

    if [ -z "$CGR_USER" ]; then
        error "CGR_USER is not set"
        missing=1
    fi

    if [ -z "$CGR_TOKEN" ]; then
        error "CGR_TOKEN is not set"
        missing=1
    fi

    if [ -z "$AWS_REGION" ]; then
        error "AWS_REGION is not set"
        missing=1
    fi

    if [ -z "$CODEARTIFACT_DOMAIN" ]; then
        error "CODEARTIFACT_DOMAIN is not set"
        missing=1
    fi

    if [ -z "$CODEARTIFACT_REPOSITORY" ]; then
        error "CODEARTIFACT_REPOSITORY is not set"
        missing=1
    fi

    if [ $missing -eq 1 ]; then
        error "Missing required environment variables. Please set them and try again."
        exit 1
    fi

    log "Environment variables validated"
}

# Setup authentication for Chainguard registry
setup_chainguard_auth() {
    log "Setting up Chainguard registry authentication..."

    # Create base64 encoded token for direct API calls
    export CHAINGUARD_AUTH_TOKEN=$(echo -n "${CGR_USER}:${CGR_TOKEN}" | base64)

    # Configure npm to use Chainguard registry for downloads (in local .npmrc)
    local cgr_host=$(echo "$CHAINGUARD_REGISTRY" | sed 's|^http://||' | sed 's|^https://||' | sed 's|/.*$||')
    local cgr_path=$(echo "$CHAINGUARD_REGISTRY" | sed 's|^http://[^/]*||' | sed 's|^https://[^/]*||')

    # Create Chainguard npm config file in temp directory
    mkdir -p "$TEMP_DIR"
    echo "//${cgr_host}${cgr_path}:_auth=$CHAINGUARD_AUTH_TOKEN" > "${TEMP_DIR}/${NPM_CONFIG_CHAINGUARD}"

    log "Chainguard authentication configured"
}

# Setup authentication for CodeArtifact
setup_codeartifact_auth() {
    log "Setting up AWS CodeArtifact authentication..."

    # Get domain owner (AWS account ID) if not provided
    if [ -z "$CODEARTIFACT_DOMAIN_OWNER" ]; then
        CODEARTIFACT_DOMAIN_OWNER=$(aws sts get-caller-identity --query Account --output text)
        log "Using AWS account ID: $CODEARTIFACT_DOMAIN_OWNER"
    fi

    # Get CodeArtifact auth token
    local ca_token=$(aws codeartifact get-authorization-token \
        --domain "$CODEARTIFACT_DOMAIN" \
        --domain-owner "$CODEARTIFACT_DOMAIN_OWNER" \
        --region "$AWS_REGION" \
        --query authorizationToken \
        --output text)

    if [ -z "$ca_token" ]; then
        error "Failed to get CodeArtifact authorization token"
        exit 1
    fi

    # Get CodeArtifact repository endpoint
    export CODEARTIFACT_REGISTRY=$(aws codeartifact get-repository-endpoint \
        --domain "$CODEARTIFACT_DOMAIN" \
        --domain-owner "$CODEARTIFACT_DOMAIN_OWNER" \
        --repository "$CODEARTIFACT_REPOSITORY" \
        --format npm \
        --region "$AWS_REGION" \
        --query repositoryEndpoint \
        --output text)

    if [ -z "$CODEARTIFACT_REGISTRY" ]; then
        error "Failed to get CodeArtifact repository endpoint"
        exit 1
    fi

    # Create CodeArtifact npm config file in temp directory
    # Extract registry URL without protocol, keep trailing slash
    local ca_registry_path=$(echo "$CODEARTIFACT_REGISTRY" | sed 's|^http://||' | sed 's|^https://||')
    # Ensure exactly one trailing slash before the colon
    ca_registry_path=$(echo "$ca_registry_path" | sed 's|/*$|/|')
    echo "//${ca_registry_path}:_authToken=$ca_token" > "${TEMP_DIR}/${NPM_CONFIG_CODEARTIFACT}"

    log "CodeArtifact authentication configured"
    log "CodeArtifact registry: $CODEARTIFACT_REGISTRY"
}

# Check if a specific package version already exists in CodeArtifact.
check_package_in_codeartifact() {
    local package_name=$1
    local version=$2

    # CodeArtifact stores an npm scope as a separate namespace.
    local ns_args=()
    local pkg="$package_name"
    if [[ "$package_name" == @*/* ]]; then
        local scope="${package_name%%/*}"
        scope="${scope#@}"
        pkg="${package_name#*/}"
        ns_args=(--namespace "$scope")
    fi

    if aws codeartifact describe-package-version \
        --domain "$CODEARTIFACT_DOMAIN" \
        --domain-owner "$CODEARTIFACT_DOMAIN_OWNER" \
        --repository "$CODEARTIFACT_REPOSITORY" \
        --format npm \
        "${ns_args[@]}" \
        --package "$pkg" \
        --package-version "$version" \
        --region "$AWS_REGION" \
        --output text > /dev/null 2>&1; then
        return 0
    else
        return 1
    fi
}

# Download a package from the Chainguard registry via `npm pack`.
# Return codes let the caller react to the specific npm failure:
#   0 = downloaded (tarball path on stdout)
#   2 = ETARGET (version not currently served)
#   3 = 404 (package/version not currently served)
#   4 = auth/permission error (401/403)
#   1 = other failure (network, tarball-name mismatch, etc.)
# Codes 2 and 3 are usually transient: Chainguard ingests upstream packages on
# demand, so a retry after a short wait typically succeeds (see process_packages).
download_package_from_chainguard() {
    local package_name=$1
    local version=$2
    local output_dir=$3
    local prefer_online=$4   # non-empty -> add --prefer-online (used on retry passes)

    log "Downloading ${package_name}@${version}..." >&2

    cd "$output_dir" || return 1

    # --prefer-online revalidates cached metadata (registry sends max-age=300),
    # so retry passes see freshly-ingested versions instead of a stale packument.
    local online_flag=()
    [ -n "$prefer_online" ] && online_flag=(--prefer-online)

    # Capture npm's output so we can classify the failure reason.
    local npm_output
    npm_output=$(npm pack "${package_name}@${version}" \
        --registry="${CHAINGUARD_REGISTRY}" \
        --userconfig="$NPM_CONFIG_CHAINGUARD" \
        --fetch-retries="$NPM_FETCH_RETRIES" \
        --fetch-timeout="$NPM_FETCH_TIMEOUT" \
        "${online_flag[@]}" 2>&1)
    local npm_exit=$?

    cd - > /dev/null || return 1

    # If npm pack succeeded, find the tarball that was created
    if [ $npm_exit -eq 0 ]; then
        # The tarball name follows the pattern: packagename-version.tgz
        # For scoped packages: @scope/packagename becomes scope-packagename
        local expected_name=$(echo "${package_name}" | sed 's/@//' | sed 's/\//-/')
        local tarball_path="${output_dir}/${expected_name}-${version}.tgz"

        if [ -f "$tarball_path" ]; then
            echo "$tarball_path"
            return 0
        fi
        warn "Package ${package_name}@${version}: npm pack succeeded but tarball not found at expected path" >&2
        return 1
    fi

    # Classify the npm failure so the caller can retry transient ones (2/3).
    if echo "$npm_output" | grep -q 'code ETARGET'; then
        warn "${package_name}@${version}: not yet available (ETARGET)" >&2
        return 2
    elif echo "$npm_output" | grep -Eq 'code E404|404 Not Found'; then
        warn "${package_name}@${version}: not yet available (404)" >&2
        return 3
    elif echo "$npm_output" | grep -Eq 'code E401|code E403|EAUTHUNKNOWN|Unauthorized|Forbidden'; then
        error "${package_name}@${version}: auth/permission error from Chainguard" >&2
        return 4
    else
        warn "${package_name}@${version}: npm pack failed: $(echo "$npm_output" | grep -m1 'npm error' || echo 'unknown error')" >&2
        return 1
    fi
}

# Publish package to CodeArtifact
publish_to_codeartifact() {
    local tarball_file=$1
    local package_name=$2
    local version=$3

    log "Publishing ${package_name}@${version} to CodeArtifact..."

    # Verify tarball exists
    if [ ! -f "$tarball_file" ]; then
        error "Tarball file not found: $tarball_file"
        return 1
    fi

    # Publish tarball directly to CodeArtifact
    local publish_output=$(npm publish "$tarball_file" \
        --registry="$CODEARTIFACT_REGISTRY" \
        --userconfig="${TEMP_DIR}/${NPM_CONFIG_CODEARTIFACT}" \
        --fetch-retries="$NPM_FETCH_RETRIES" \
        --fetch-timeout="$NPM_FETCH_TIMEOUT" 2>&1)
    local exit_code=$?

    if [ $exit_code -eq 0 ]; then
        log "Successfully published ${package_name}@${version}"
        return 0
    else
        error "Failed to publish ${package_name}@${version}: $publish_output"
        return 1
    fi
}

# Extract packages from package-lock.json (npm)
extract_packages_npm() {
    local lock_file=$1

    log "Parsing package-lock.json..." >&2

    # Output format: NAME|VERSION (using | as delimiter to handle scoped packages with @)
    jq -r '
        .packages // {} |
        to_entries[] |
        select(.key != "") |
        select(.value.version != null) |
        {
            path: .key,
            name: (if (.value.name != null) then .value.name else (.key | split("node_modules/") | last) end),
            version: .value.version
        } |
        "\(.name)|\(.version)"
    ' "$lock_file" | sort -u
}

# Extract packages from a pnpm lockfile (pnpm-lock.yaml / package-lock.yaml)
#
# Unlike npm, pnpm stores a package's identity in the map KEY as name@version
# (there are no separate name/version fields), and the key format varies by
# lockfileVersion:
#   v9: "name@version"            / "@scope/name@version"
#   v6: "/name@version"           (leading slash; peer deps as "(dep@1.0.0)")
#   v5: "/name/version"           (slash separator, no @ before version)
# We convert the .packages map to JSON once and normalize all three shapes in
# jq, so the result is identical regardless of which pnpm wrote the lockfile.
extract_packages_pnpm() {
    local lock_file=$1

    log "Parsing pnpm lockfile (YAML)..." >&2

    # How many packages does the lockfile claim to have?
    local pkg_count
    pkg_count=$(yq e '.packages | length' "$lock_file" 2>/dev/null)
    [ -z "$pkg_count" ] && pkg_count=0

    local extracted
    extracted=$(yq -o=json '.packages // {}' "$lock_file" | jq -r '
        keys[]
        | sub("^/"; "")                       # v6: strip leading slash
        | sub("\\(.*$"; "")                   # strip "(peer@x)" suffix
        | . as $k
        | (ltrimstr("@") | test("@")) as $hasAt   # ignore a leading scope "@"
        | (if $hasAt
             then ($k | capture("^(?<name>.+)@(?<version>[^@]+)$"))   # v6/v9
             else ($k | capture("^(?<name>.+)/(?<version>[^/]+)$"))   # v5
           end)
        | select(.name != "" and .version != "")
        | select(.version | test("://") | not)   # drop tarball/git "versions"
        | "\(.name)|\(.version)"
    ' | sort -u)

    local extracted_count=0
    [ -n "$extracted" ] && extracted_count=$(printf '%s\n' "$extracted" | grep -c '|')

    # Fail loud: a populated lockfile that yields nothing is a tooling/format
    # mismatch (wrong yq flavor, unsupported lockfileVersion) — NOT "nothing to
    # mirror". Silently reporting 0 here is the bug we're guarding against.
    # NOTE: this exit only aborts the script because process_packages captures
    # our output in the main shell (see the call site), not via a subshell.
    if [ "$pkg_count" -gt 0 ] && [ "$extracted_count" -eq 0 ]; then
        error "Lockfile lists ${pkg_count} packages but extraction produced none." >&2
        error "Verify yq is the mikefarah build (v4) and the lockfileVersion is supported." >&2
        exit 1
    fi

    printf '%s\n' "$extracted"
}

# Extract packages — dispatches to the right parser based on file extension
extract_packages() {
    local lock_file=$1

    if [ ! -f "$lock_file" ]; then
        error "Lock file not found at: $lock_file"
        exit 1
    fi

    case "$lock_file" in
        *.yaml|*.yml)
            extract_packages_pnpm "$lock_file"
            ;;
        *)
            extract_packages_npm "$lock_file"
            ;;
    esac
}


# Main processing function
process_packages() {
    local lock_file=$1
    local temp_dir=$2

    mkdir -p "$temp_dir"

    local downloaded=0
    local published=0
    local already_exists=0
    local failed=0
    # Final breakdown of packages still unavailable after all retry passes.
    local version_gap=0
    local pkg_missing=0
    local auth_err=0
    local other_fail=0
    local unresolved=""   # "REASON<tab>name@version" lines for the report

    # Chainguard's upstream fallback ingests packages ON DEMAND and
    # ASYNCHRONOUSLY, so the first request for an un-cached package/version returns
    # 404/ETARGET while Chainguard fetches it from npm in the background, and it
    # becomes downloadable moments later. A single npm pack call works too fast for this process. 
    # Accordingly, make multiple passes where the first pass primes ingestion for every miss, and 
    # subsequent passes (after a short wait) pick up the now-populated packages. Tunable via env vars.
    local max_passes="${INGEST_MAX_PASSES:-4}"
    local retry_delay="${INGEST_RETRY_DELAY:-30}"

    # Extract into a variable in THIS shell first. Capturing here (rather than
    # feeding the loop via process substitution) lets a fail-loud exit inside
    # extract_packages abort the whole run under `set -e`, instead of dying
    # silently in a subshell and leaving the loop to report 0.
    local pkg_list
    pkg_list=$(extract_packages "$lock_file")
    local total
    total=$(printf '%s\n' "$pkg_list" | grep -c '|' || true)

    # Work queue. First pass holds "name|version"; retry passes hold
    # "rc|name|version" so each miss carries its last classification forward.
    local pending="$pkg_list"
    local pass=0

    while [ -n "$(printf '%s' "$pending" | tr -d '[:space:]')" ] && [ "$pass" -lt "$max_passes" ]; do
        pass=$((pass + 1))
        local is_first=0; [ "$pass" -eq 1 ] && is_first=1
        local count_this; count_this=$(printf '%s\n' "$pending" | grep -c '|' || true)
        log "=== Pass ${pass}/${max_passes}: attempting ${count_this} package(s) ==="
        local next_pending=""

        while IFS='|' read -r f1 f2 f3; do
            local package_name package_version
            if [ "$is_first" -eq 1 ]; then
                package_name="$f1"; package_version="$f2"
            else
                package_name="$f2"; package_version="$f3"   # f1 is the carried rc
            fi
            [ -z "$package_name" ] && continue

            # Only check CodeArtifact (and count already-exists) on the first pass;
            # retry queue only ever holds packages we already know aren't there.
            if [ "$is_first" -eq 1 ]; then
                log "Processing ${package_name}@${package_version}..."
                if check_package_in_codeartifact "$package_name" "$package_version"; then
                    log "${package_name}@${package_version} already exists in CodeArtifact, skipping"
                    already_exists=$((already_exists + 1))
                    continue
                fi
            else
                log "Retry ${package_name}@${package_version}..."
            fi

            # On retry passes, force fresh metadata (--prefer-online) so the
            # registry's 5-minute packument cache doesn't keep returning ETARGET
            # for a version that has since been ingested.
            local prefer_online=""
            [ "$is_first" -eq 0 ] && prefer_online="1"

            # `&& rc=0 || rc=$?` keeps this in a tested context so a non-zero
            # return doesn't trip `set -e`.
            local tarball_file rc
            tarball_file=$(download_package_from_chainguard "$package_name" "$package_version" "$temp_dir" "$prefer_online") && rc=0 || rc=$?

            case $rc in
                0)
                    downloaded=$((downloaded + 1))
                    if publish_to_codeartifact "$tarball_file" "$package_name" "$package_version"; then
                        published=$((published + 1))
                        rm -f "$tarball_file"
                    else
                        failed=$((failed + 1))
                        unresolved+="PUBLISH"$'\t'"${package_name}@${package_version}"$'\n'
                    fi
                    ;;
                4)  # auth won't resolve by retrying — record now, don't re-queue
                    auth_err=$((auth_err + 1))
                    unresolved+="AUTH"$'\t'"${package_name}@${package_version}"$'\n'
                    ;;
                *)
                    # 1/2/3: not served yet — may still be ingesting. Re-queue,
                    # carrying the rc so we can classify it if it never resolves.
                    next_pending+="${rc}|${package_name}|${package_version}"$'\n'
                    ;;
            esac
        done <<< "$pending"

        pending="$next_pending"
        local remaining; remaining=$(printf '%s\n' "$pending" | grep -c '|' || true)
        if [ "$remaining" -gt 0 ] && [ "$pass" -lt "$max_passes" ]; then
            log "Pass ${pass} done; ${remaining} still unavailable — waiting ${retry_delay}s for Chainguard fallback to ingest, then retrying..."
            sleep "$retry_delay"
        fi
    done

    # Whatever is still pending after the final pass is genuinely unavailable
    # (truly nonexistent, malware-blocked, still in cooldown, or no verifiable
    # source). Classify by the last rc each carried.
    while IFS='|' read -r rc package_name package_version; do
        [ -z "$package_name" ] && continue
        case $rc in
            2) version_gap=$((version_gap + 1)); unresolved+="ETARGET"$'\t'"${package_name}@${package_version}"$'\n' ;;
            3) pkg_missing=$((pkg_missing + 1));  unresolved+="404"$'\t'"${package_name}@${package_version}"$'\n' ;;
            *) other_fail=$((other_fail + 1));    unresolved+="OTHER"$'\t'"${package_name}@${package_version}"$'\n' ;;
        esac
    done <<< "$pending"

    # Summary
    local not_mirrored=$((version_gap + pkg_missing + auth_err + other_fail))
    log "=========================================="
    log "Mirror Summary:"
    log "  Total packages:                 $total"
    log "  Already in CodeArtifact:        $already_exists"
    log "  Downloaded from Chainguard:     $downloaded"
    log "  Published to CodeArtifact:      $published"
    log "  Unavailable after ${max_passes} passes:  $not_mirrored"
    log "    - ETARGET (version still not served):   $version_gap"
    log "    - 404 (still not served):               $pkg_missing"
    log "    - Auth/permission errors:               $auth_err"
    log "    - Other failures:                       $other_fail"
    log "  Publish failures:               $failed"
    log "=========================================="
    if [ -n "$unresolved" ]; then
        local report="${UNRESOLVED_REPORT:-./chainguard-unresolved.txt}"
        printf '%s' "$unresolved" | sort > "$report"
        log "Unresolved packages (reason<tab>name@version) written to: $report"
    fi
    if [ "$not_mirrored" -gt 0 ]; then
        log "NOTE: still unavailable after ${max_passes} passes — likely within the cooldown"
        log "window, malware-blocked, no verifiable source, or nonexistent. Re-running"
        log "later may pick up packages past cooldown. Tune: INGEST_MAX_PASSES / INGEST_RETRY_DELAY."
    fi
}

# Main script execution
main() {
    # Parse command line arguments
    if [ $# -gt 0 ]; then
        PACKAGE_LOCK_FILE="$1"
    elif [ -n "$PACKAGE_LOCK_FILE" ]; then
        : # Use value from environment
    elif [ -f "./package-lock.json" ]; then
        PACKAGE_LOCK_FILE="./package-lock.json"
    elif [ -f "./pnpm-lock.yaml" ]; then
        PACKAGE_LOCK_FILE="./pnpm-lock.yaml"
    else
        PACKAGE_LOCK_FILE="./package-lock.json"
    fi

    log "Starting npm package mirror to AWS CodeArtifact..."
    log "Package lock file: $PACKAGE_LOCK_FILE"
    log "Chainguard registry: $CHAINGUARD_REGISTRY"

    # Check if lock file exists
    if [ ! -f "$PACKAGE_LOCK_FILE" ]; then
        error "Lock file not found: $PACKAGE_LOCK_FILE"
        echo ""
        echo "Usage: $0 [path-to-lock-file]"
        echo ""
        echo "Examples:"
        echo "  $0                              # Auto-detects package-lock.json or pnpm-lock.yaml"
        echo "  $0 /path/to/package-lock.json  # Uses npm lock file"
        echo "  $0 /path/to/pnpm-lock.yaml     # Uses pnpm lock file"
        exit 1
    fi

    # Check prerequisites
    if ! command -v jq &> /dev/null; then
        error "jq is required but not installed. Please install jq and try again."
        exit 1
    fi

    # yq is required for pnpm lockfiles — and it MUST be the Go (mikefarah) v4
    # build. The Python (kislyuk) yq uses different argument semantics, so
    # `yq e '...'` silently parses nothing and the run reports 0 packages.
    case "$PACKAGE_LOCK_FILE" in
        *.yaml|*.yml)
            if ! command -v yq &> /dev/null; then
                error "yq is required for pnpm lockfiles but not installed. Install mikefarah yq v4 (e.g. brew install yq)."
                exit 1
            fi
            if ! yq --version 2>&1 | grep -qi 'mikefarah'; then
                error "Wrong yq detected — this script needs the Go 'mikefarah' yq v4, not the Python (kislyuk) yq."
                error "Found: $(yq --version 2>&1). Install the correct one with: brew install yq"
                exit 1
            fi
            ;;
    esac

    if ! command -v curl &> /dev/null; then
        error "curl is required but not installed. Please install curl and try again."
        exit 1
    fi

    if ! command -v npm &> /dev/null; then
        error "npm is required but not installed. Please install npm and try again."
        exit 1
    fi

    if ! command -v aws &> /dev/null; then
        error "AWS CLI is required but not installed. Please install aws-cli and try again."
        exit 1
    fi

    # Validate environment
    check_env

    # Setup authentication
    setup_chainguard_auth
    setup_codeartifact_auth

    # Process packages
    process_packages "$PACKAGE_LOCK_FILE" "$TEMP_DIR"

    # Cleanup
    rmdir "$TEMP_DIR" 2>/dev/null || true

    log "Mirror process completed!"
}

# Run main function
main "$@"
```

{{< /details >}}

Before running it, save the script to a local working directory and make it executable:

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


