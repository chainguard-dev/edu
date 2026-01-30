---
title: "Using GitOps to Manage Custom Assembly Resources"
linktitle: "Manage with GitOps"
type: "article"
description: "How to use GitOps to manage Custom Assembly resources."
date: 2025-05-01T11:07:52+02:00
lastmod: 2025-07-15T11:07:52+02:00
draft: false
tags: ["Chainguard Containers", "Procedural", "Custom Assembly"]
images: []
menu:
  docs:
    parent: "features"
weight: 011
toc: true
---

Chainguard's [Custom Assembly](/chainguard/chainguard-images/features/ca-docs/custom-assembly/) is a tool that allows customers to create customized container images with extra packages and annotations added. This enables customers to reduce their risk exposure by creating container images that are tailored to their internal organization and application requirements while still having few-to-zero CVEs. It can be managed in the [Chainguard Console](/chainguard/chainguard-images/features/ca-docs/custom-assembly-console/), [with chainctl](/chainguard/chainguard-images/features/ca-docs/custom-assembly-chainctl/), [with the API](/chainguard/chainguard-images/features/ca-docs/custom-assembly-api-demo/), or via CI/CD.

This guide shows how to use Chainguard Custom Assembly as code via CI/CD, storing your configuration in Git and using automation to apply changes and trigger builds. The examples in this guide focus on GitHub Actions, as seen in [Chainguard's custom-assembly-as-code demo repository](https://github.com/chainguard-demo/custom-assembly-as-code). 

> **NOTE**: `chainctl` is an API client that handles common tasks like authentication and applying configuration files. You can manage Custom Assembly [interactively using `chainctl`](/chainguard/chainguard-images/features/ca-docs/custom-assembly-api-demo/). Running `chainctl` non-interactively is a common pattern for implementing GitOps workflows. 

## Prerequisites

Before getting started, you should have:
* A Chainguard organization with access to Custom Assembly
* Permission to manage Custom Assembly configuration for your organization/repository
* A CI/CD platform in place
    * In this guide, we use GitHub Actions as an example.
* A Git repository to host your apko configuration files
* A configured assumable identity for your CI workload
    * If you have not yet set up CI identities, see [Chainguard's tutorials for creating and assuming identities](/chainguard/administration/assumable-ids/identity-examples/).
* The full IDs for your [catalog_syncer and apko_builder identities](/chainguard/chainguard-images/how-to-use/verifying-chainguard-images-and-metadata-signatures-with-cosign/#chainguards-signing-identities/).

Also note that Chainguard's [demo workflow](/chainguard-demo/custom-assembly-as-code/) uses [octo-sts](https://www.chainguard.dev/unchained/the-end-of-github-pats-you-cant-leak-what-you-dont-have), a tool that generates short-lived GitHub tokens instead of using long-lived Personal Access Tokens (PATs). While octo-sts is optional for Custom Assembly builds, it's recommended for workflows that need GitHub API access alongside Chainguard operations.

### Understanding apko overlay files

Custom Assembly uses apko overlay YAML files to customize images. You can use them to define changes such as additional packages to install, environment variables, and annotations.

This example overlay file adds curl and jq to a base Python image:

```yaml
contents:
  packages:
    - curl
    - jq

environment:
  APP_ENV: production
  LOG_LEVEL: info

annotations:
  org.opencontainers.image.title: "Python App with Tools"
  org.opencontainers.image.description: "Custom Python image with curl and jq"
```

### Repository structure

We recommend organizing your configuration YAML files in a dedicated directory. For example:

```
your-repo/
├── .github/
│   └── workflows/
│       └── build-custom-images.yaml
├── ca-images-iac/
│   ├── python-app.yaml
│   ├── nginx-custom.yaml
│   └── node-api.yaml
└── README.md
```

In this example, the `ca-images-iac/` directory contains the apko overlay files, while the workflow file defines how and when builds are triggered.

## Step 1: Create an assumable identity

First, create an identity that your CI/CD platform can assume. The process varies by platform, but here's a GitHub Actions example:

```bash
chainctl iam identities create github-actions-identity \
  --description="GitHub Actions identity for Custom Assembly" \
  --claim=repository=your-org/your-repo \
  --claim=event_name=push
```

This creates an identity that GitHub Actions workflows in `your-org/your-repo` can assume when triggered by push events.


### Step 2: Grant permissions

The identity needs permission to build Custom Assembly images. You can create a [least-privilege custom role](/chainguard/chainguard-images/features/ca-docs/custom-assembly/#custom-assembly-permissions-requirements/) that contains the `repo.update` and `repo.create` permissions, then grant the necessary permission using `chainctl`:

```bash
# Get your identity ID
IDENTITY_ID=$(chainctl iam identities list -o json | jq -r '.items[] | select(.name=="github-actions-identity") | .id')

# Grant image build permissions
chainctl iam role-bindings create \
  --identity=$IDENTITY_ID \
  --role=custom-role \
  --group=your-group-id
```

### Step 3: Note Your identity ID

You'll need your identity ID for your CI/CD workflow configuration. Save it for use in the next section:

```bash
chainctl iam identities list -o table
```

## Trigger builds via chainctl in CI/CD workflows

Regardless of which CI/CD platform you use, Custom Assembly builds are triggered with the same chainctl command:
```bash
chainctl images repos build apply --file ca-images-iac/custom-jre.yaml \
  --parent your-parent-group \
  --repo your-repo \
  --yes
```
This command follows the example repo structure that appears earlier on this page, where `ca-images-iac` is the directory that contains the apko overlay files.

This command:
- Reads your apko overlay configuration from the YAML file
- Applies it to build a custom image
- Pushes the result to your Chainguard registry
- Skips the interactive confirmation via the `--yes` flag, making it suitable for automated workflows


### GitHub Actions example

This section provides a complete example for automating Custom Assembly builds with GitHub Actions.

Create `.github/workflows/build-custom-images.yaml` in your repository. This example is based on Chainguard's [custom-assembly-as-code demo](https://github.com/chainguard-demo/custom-assembly-as-code):

```yaml
# Trigger builds automatically when the specified file changes. Only runs on pushes to the main branch. Use a wildcard to trigger on any file in a specified directory.
name: build
on:
  push:
    branches: [main]
    paths:
      - 'ca-images-iac/custom-jre.yaml'
  workflow_dispatch:

env:
  CUSTOM_IMAGE: "cgr.dev/your-org/your-image"

# Top-level permissions set to principle of least privilege. Job-level permissions grant only what's needed.
permissions: {}

jobs:
  build-custom-image-as-code:
    runs-on: ubuntu-latest
    permissions:
      actions: read
      contents: read
      id-token: write
    steps:
      - name: Harden the runner (Audit all outbound calls)
        uses: step-security/harden-runner@20cf305ff2072d973412fa9b1e3a4f227bda3c76 # v2.14.0
        with:
          egress-policy: audit
      
      - name: Checkout repository
        uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
        with:
          ref: main
      
      - name: Setup Go environment
        uses: actions/setup-go@41dfa10bad2bb2ae585af6ee5bb4d7d973ad74ed # v5.1.0
        with:
          cache: false
      
      # Use octo-sts for GitHub authentication (no PAT needed)
      - uses: octo-sts/action@6177b4481c00308b3839969c3eca88c96a91775f # v1.0.0
        id: octo-sts
        with:
          scope: your-org/your-repo
          identity: build
      
      - name: Install Crane
        run: go install github.com/google/go-containerregistry/cmd/crane@latest
      
      - name: Install Cosign
        uses: sigstore/cosign-installer@dc72c7d5c4d10cd6bcb8cf6e3fd625a9e5e537da # v3.7.0
      
      # Authenticate to Chainguard using assumable identity
      - uses: chainguard-dev/setup-chainctl@8d93dcbef466d3cf3533f67084f52eb74ef9d262 # v0.2.4
        with:
          identity: "your-org-id/your-identity-id"
      
      - name: 'Auth to Registry'
        run: |
          chainctl auth configure-docker
          chainctl auth status
      
      # Verify existing image signature before rebuilding. Find these identity IDs in your organization's "Assumed Identities" settings.
      - name: Verify signature && pull existing image
        id: cosign-verify
        continue-on-error: false
        run: |
          # Images are signed by either CATALOG_SYNCER or APKO_BUILDER identity in your org.
          # Find these values in your organization settings under "Assumed Identities"
          CATALOG_SYNCER="your-org-id/catalog-syncer-id"
          APKO_BUILDER="your-org-id/apko-builder-id"
          cosign verify \
            --certificate-oidc-issuer=https://issuer.enforce.dev \
            --certificate-identity-regexp="https://issuer.enforce.dev/(${CATALOG_SYNCER}|${APKO_BUILDER})" \
            $CUSTOM_IMAGE:latest | jq
      
      # Extract and display packages from the SBOM attestation.
      - name: Print created time and list packages
        id: crane-config
        continue-on-error: false
        run: |
          echo "Created time: $(crane config $CUSTOM_IMAGE:latest | jq -r .created)"
          crane manifest $CUSTOM_IMAGE:latest | \
            jq -r '.manifests[] | \
            select (.platform.architecture=="amd64") | \
            .digest' | \
            xargs -I {} cosign verify-attestation --type=spdx \
            --certificate-oidc-issuer=https://issuer.enforce.dev \
            --certificate-identity-regexp="https://issuer.enforce.dev/(${CATALOG_SYNCER}|${APKO_BUILDER})" \
            $CUSTOM_IMAGE@{} 2> /dev/null | \
            jq -r .payload | base64 -d | jq '.predicate' | \
            jq '.packages[] | select(.externalRefs[]?.referenceCategory == "PACKAGE_MANAGER") | \
            .externalRefs[] | select(.referenceCategory == "PACKAGE_MANAGER") | .referenceLocator'
      
      # Apply the apko configuration file to trigger the build. The --yes flag skips the confirmation prompt.
      - name: Trigger custom build
        id: start-custom-build
        continue-on-error: false
        run: |
          chainctl image repo build apply -f ca-images-iac/custom-jre.yaml \
            --parent your-parent-group --repo your-repo --yes
```

## Testing your workflow

Before deploying your CI/CD workflow to production, test it thoroughly to ensure builds complete successfully and authentication works correctly. Start by triggering a manual build and reviewing the logs for each step. Verify that images are built with the expected packages and configurations, and confirm that signatures and attestations are properly generated. Testing in a non-production environment or with a dedicated test repository helps catch configuration issues early without impacting your production image builds.

### Testing the GitHub Action example

Before using the GitHub action in this guide, make sure to update the placeholders:
- `your-org/your-repo`: Your GitHub repository (e.g., `acme/infrastructure`)
- `your-org-id/your-identity-id`: Your full Chainguard identity ID
- `CUSTOM_IMAGE: "cgr.dev/your-org/your-image"`: Your image registry path
- `CATALOG_SYNCER="your-org-id/catalog-syncer-id"`: Your catalog syncer identity
- `APKO_BUILDER="your-org-id/apko-builder-id"`: Your APKO builder identity
- `--parent your-parent-group --repo your-repo`: Your Chainguard group and repo names
- `ca-images-iac/custom-jre.yaml`: Your repo's directory that holds the apko overlay files, and the overlay file name

To test your GitHub Action:

1. In GitHub, go to **Actions tab > Select workflow > Run workflow**.
2. View the detailed logs for each step.
3. Confirm that the images appear in your Chainguard registry.


## Additional resources

- [Custom Assembly Overview](/chainguard/chainguard-images/features/ca-docs/custom-assembly/)
- [apko Overview](/open-source/build-tools/apko/overview/)
- [Assumable Identity Documentation](/chainguard/administration/assumable-ids/assumable-ids/)
- [Demo Repository: custom-assembly-as-code](https://github.com/chainguard-demo/custom-assembly-as-code)
- [Chainguard Support](https://support.chainguard.dev)


