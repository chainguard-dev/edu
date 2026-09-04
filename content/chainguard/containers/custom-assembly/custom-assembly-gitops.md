---
title: "Using GitOps to manage Custom Assembly resources"
linktitle: "Manage with GitOps"
type: "article"
description: "How to use GitOps to manage Custom Assembly resources."
date: 2026-01-29T11:07:52+02:00
lastmod: 2026-09-01T16:34:19+00:00
draft: false
tags: ["Chainguard Containers", "Procedural", "Custom Assembly"]
images: []
menu:
  docs:
    parent: "features"
weight: 040
toc: true
aliases:
- /chainguard/chainguard-images/features/ca-docs/custom-assembly-gitops/
- /chainguard/containers/features/ca-docs/custom-assembly-gitops/
---

Chainguard's [Custom Assembly](/chainguard/containers/custom-assembly/overview/) is a tool that lets customers create customized container images with extra packages and annotations added. This enables customers to reduce their risk exposure by creating container images that are tailored to their internal organization and application requirements while still having few-to-zero CVEs. It can be managed in the [Chainguard Console](/chainguard/containers/custom-assembly/custom-assembly-console/), [with `chainctl`](/chainguard/containers/custom-assembly/custom-assembly-chainctl/), [with the API](/chainguard/containers/custom-assembly/custom-assembly-api-demo/), or from a CI/CD pipeline.

This guide shows how to use Chainguard Custom Assembly as code from a CI/CD pipeline, storing your configuration in Git and using automation to apply changes and trigger builds. The examples in this guide focus on GitHub Actions, and are adapted from [Chainguard's custom-assembly-as-code demo repository](https://github.com/chainguard-demo/custom-assembly-as-code).

> **NOTE**: `chainctl` is an API client that handles common tasks like authentication and applying configuration files. You can manage Custom Assembly [interactively using `chainctl`](/chainguard/containers/custom-assembly/custom-assembly-api-demo/). Running `chainctl` non-interactively is a common pattern for implementing GitOps workflows.

## Prerequisites

Before getting started, you need the following:

* A Chainguard organization with access to Custom Assembly, as well as permission to manage Custom Assembly for your organization
* A CI/CD platform in place. This guide uses GitHub Actions as an example
    * Custom Assembly builds need no GitHub credentials beyond the token `actions/checkout` uses by default, so the example workflow in this guide does not authenticate to the GitHub API.
* A Git repository to host your apko configuration files
* A configured assumable identity for your CI workload
    * If you have not yet set up CI identities, refer to [Chainguard's tutorials for creating and assuming identities](/chainguard/administration/assumable-ids/identity-examples/).
* The full IDs for your [image-syncer and custom-image-builder identities](/chainguard/containers/security-and-compliance/verifying-chainguard-images-and-metadata-signatures-with-cosign/#chainguards-signing-identities), named `catalog_syncer` and `apko_builder` in older organizations

### Understanding apko overlay files

Custom Assembly uses apko overlay YAML files to customize images. You can use them to define changes such as additional packages to install, environment variables, and annotations.

This example overlay file shows the configuration options available for customizing Chainguard images:

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

accounts:
   run-as: "appuser"
   users:
     - username: "appuser"
       uid: 65532
       gid: 65532
       homedir: "/home/appuser"
   groups:
     - groupname: "appgroup"
       gid: 65532
       members:
         - "appuser"

certificates:
   additional:
     - name: "certificate name"
       content: |
          -----BEGIN CERTIFICATE-----
         ...
         -----END CERTIFICATE-----
```

### Repository structure

Chainguard recommends organizing your configuration YAML files in a dedicated directory, as in the following example repository structure:

```
<github-repository>/
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

First, create an identity that your CI/CD platform can assume. The process varies by platform; the following example uses GitHub Actions.

```bash
chainctl iam identities create github-actions-identity \
  --description="GitHub Actions identity for Custom Assembly" \
  --identity-issuer=https://token.actions.githubusercontent.com \
  --subject-pattern=".*" \
  --claim-pattern=repository:<github-organization>/<github-repository> \
  --claim-pattern='event_name:^(push|workflow_dispatch)$'
```

Replace `<github-organization>/<github-repository>` with the repository that holds your workflow. This creates an identity that GitHub Actions workflows in that repository can assume, whether triggered by a push or started manually from the Actions tab.

Claim values are patterns, not literal strings, so `^(push|workflow_dispatch)$` matches either event. Match both: the workflow later in this guide triggers on `push` and `workflow_dispatch`, and the testing steps start a run manually. An identity pinned to `event_name:push` alone rejects manual runs with `token has invalid "event_name": workflow_dispatch`. Be sure to quote the pattern so your shell does not interpret the `|` as a pipe.

Repeat `--claim-pattern` once per claim, as shown in this example. Passing several `claim:pattern` pairs as a single comma-separated value does not create separate claims — `chainctl` treats the entire string as one pattern, matching a `repository` claim whose literal value is `<github-organization>/<github-repository>,event_name:push`. This fails silently, producing an identity that no workflow can assume.

This example matches on the `repository` and `event_name` claims rather than the `sub` claim, so it is unaffected by GitHub's [immutable subject claims](/platform/administration/assumable-ids/identity-examples/github-identity/#finding-your-repositorys-numeric-identifiers), which change only the `sub` claim. The `repository` claim carries the repository name, and names can be reassigned. For stronger protection against namespace reuse, pin the identity to the repository's numeric ID by adding `--claim-pattern=repository_id:<github-repository-id>`.

## Step 2: Grant permissions

The identity needs permission to build Custom Assembly images. You can create a [least-privilege custom role](/chainguard/containers/custom-assembly/overview/#custom-assembly-permissions-requirements) that contains the `repo.update` and `repo.create` permissions, then grant the necessary permission using `chainctl`.

After creating the custom role, set an environment variable named `IDENTITY_ID` to the UIDP of the `github-actions-identity` identity you just created:

```shell
IDENTITY_ID=$(chainctl iam identities list -o json | jq -r '.items[] | select(.name=="github-actions-identity") | .id')
```

Then use this variable to create a role binding that grants the custom role to the identity:

```shell
chainctl iam role-bindings create \
  --identity=$IDENTITY_ID \
  --role=<custom-role> \
  --parent=<chainguard-org>
```

Be sure to replace `<custom-role>` with the name of the custom role you created and `<chainguard-org>` with the name of your Chainguard organization.

## Step 3: Note your identity ID

You'll need your identity ID for your CI/CD workflow configuration. Save it for use in the next section:

```bash
chainctl iam identities list -o table
```

## Trigger builds with `chainctl` in CI/CD workflows

Regardless of which CI/CD platform you use, you trigger Custom Assembly builds with the same `chainctl images repos build apply` command:

```bash
chainctl images repos build apply --file ca-images-iac/custom-jre.yaml \
  --parent <chainguard-org> \
  --repo <image-name> \
  --yes
```

This command follows the example repo structure that appears earlier on this page, where `ca-images-iac` is the directory that contains the apko overlay files.

This command:

* Reads your apko overlay configuration from the YAML file
* Applies it to build a custom image
* Pushes the result to your Chainguard registry
* Skips the interactive confirmation when you pass `--yes`, making it suitable for automated workflows

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

# Images are signed by either the image-syncer or custom-image-builder identity in
# your organization. Find these values under "Assumed Identities" in your
# organization settings. They are defined here, at workflow level, so every step can
# read them.
env:
  CUSTOM_IMAGE: "cgr.dev/<chainguard-org>/<image-name>"
  IMAGE_SYNCER: "<chainguard-org-id>/<image-syncer-id>"
  CUSTOM_IMAGE_BUILDER: "<chainguard-org-id>/<custom-image-builder-id>"

# Top-level permissions follow the principle of least privilege. Job-level permissions grant only what's needed.
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

      # Nothing after this step uses git or the GitHub API, so there is no reason to
      # leave the checkout token behind in .git/config.
      - name: Checkout repository
        uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
        with:
          ref: main
          persist-credentials: false

      - name: Setup Go environment
        uses: actions/setup-go@41dfa10bad2bb2ae585af6ee5bb4d7d973ad74ed # v5.1.0
        with:
          cache: false

      # Pin Crane to a release rather than @latest so a run cannot pick up an
      # unreviewed version. Check for newer releases periodically.
      - name: Install Crane
        run: go install github.com/google/go-containerregistry/cmd/crane@v0.21.9

      - name: Install Cosign
        uses: sigstore/cosign-installer@dc72c7d5c4d10cd6bcb8cf6e3fd625a9e5e537da # v3.7.0

      # Authenticate to Chainguard using assumable identity
      - uses: chainguard-dev/setup-chainctl@8d93dcbef466d3cf3533f67084f52eb74ef9d262 # v0.2.4
        with:
          identity: "<chainguard-org-id>/<chainguard-identity-id>"

      - name: 'Auth to Registry'
        run: |
          chainctl auth configure-docker
          chainctl auth status

      # Verify existing image signature before rebuilding.
      - name: Verify signature && pull existing image
        id: cosign-verify
        continue-on-error: false
        run: |
          cosign verify \
            --certificate-oidc-issuer=https://issuer.enforce.dev \
            --certificate-identity-regexp="https://issuer.enforce.dev/(${IMAGE_SYNCER}|${CUSTOM_IMAGE_BUILDER})" \
            "$CUSTOM_IMAGE:latest" | jq

      # Extract and display packages from the SBOM attestation.
      - name: Print created time and list packages
        id: crane-config
        continue-on-error: false
        run: |
          echo "Created time: $(crane config "$CUSTOM_IMAGE:latest" | jq -r .created)"
          crane manifest "$CUSTOM_IMAGE:latest" |
            jq -r '.manifests[]
              | select(.platform.architecture=="amd64")
              | .digest' |
            xargs -I {} cosign verify-attestation --type=spdx \
              --certificate-oidc-issuer=https://issuer.enforce.dev \
              --certificate-identity-regexp="https://issuer.enforce.dev/(${IMAGE_SYNCER}|${CUSTOM_IMAGE_BUILDER})" \
              "$CUSTOM_IMAGE@{}" 2> /dev/null |
            jq -r .payload | base64 -d | jq '.predicate' |
            jq '.packages[]
              | select(.externalRefs[]?.referenceCategory == "PACKAGE_MANAGER")
              | .externalRefs[]
              | select(.referenceCategory == "PACKAGE_MANAGER")
              | .referenceLocator'

      # Apply the apko configuration file to trigger the build. The --yes flag skips the confirmation prompt.
      - name: Trigger custom build
        id: start-custom-build
        continue-on-error: false
        run: |
          chainctl images repos build apply -f ca-images-iac/custom-jre.yaml \
            --parent <chainguard-org> --repo <image-name> --yes
```

#### Extending the workflow with GitHub API access

Some extensions to this workflow do need GitHub credentials, such as committing an updated overlay file, opening a pull request that reports which CVEs a rebuild fixed, or commenting build results on an existing pull request.

Rather than storing a long-lived Personal Access Token, add an [Octo STS](https://github.com/apps/octo-sts) step. Octo STS exchanges the workflow's OIDC token for a GitHub token that is scoped to the permissions you declare and expires with the run:

```yaml
      - uses: octo-sts/action@6177b4481c00308b3839969c3eca88c96a91775f # v1.0.0
        id: octo-sts
        with:
          scope: <github-organization>/<github-repository>
          identity: build
```

Pass the result to whichever step needs it as `${{ steps.octo-sts.outputs.token }}`. Using Octo STS also requires installing its GitHub App on your organization and committing a trust policy to `.github/chainguard/build.sts.yaml`, where `build` matches the `identity` input. Refer to the [Octo STS overview](/open-source/octo-sts/overview/) for more information.

## Testing your workflow

Before deploying your CI/CD workflow to production, test it thoroughly to ensure builds complete successfully and authentication works correctly. Start by triggering a manual build and reviewing the logs for each step. Verify that images are built with the expected packages and configurations, and confirm that signatures and attestations are properly generated. Testing in a non-production environment or with a dedicated test repository helps catch configuration issues early without impacting your production image builds.

### Testing the GitHub Action example

Before using the GitHub action in this guide, make sure to update the placeholders:

* `<chainguard-org-id>/<chainguard-identity-id>`: The full ID of the identity you created in Step 1
* `CUSTOM_IMAGE: "cgr.dev/<chainguard-org>/<image-name>"`: Your image registry path
* `IMAGE_SYNCER: "<chainguard-org-id>/<image-syncer-id>"`: Your `image-syncer` identity
* `CUSTOM_IMAGE_BUILDER: "<chainguard-org-id>/<custom-image-builder-id>"`: Your `custom-image-builder` identity
* `--parent <chainguard-org> --repo <image-name>`: Your Chainguard organization and image repository names
* `ca-images-iac/custom-jre.yaml`: The directory in your GitHub repository that holds the apko overlay files, and the overlay file name

{{< note >}}
Older Chainguard organizations name the `image-syncer` and `custom-image-builder` identities `catalog_syncer` and `apko_builder` instead. The names are interchangeable: each pair points at the same account association, so the signatures verify the same way. The workflow's environment variable names are arbitrary — only the identity IDs they hold matter.
{{< /note >}}

To test your GitHub Action:

1. In GitHub, go to the **Actions** tab, select your workflow, then click **Run workflow**.
2. Check the detailed logs for each step.
3. Confirm that the images appear in your Chainguard registry.

## Additional resources

* [Custom Assembly overview](/chainguard/containers/custom-assembly/overview/)
* [apko overview](/open-source/build-tools/apko/overview/)
* [Assumable identity documentation](/chainguard/administration/assumable-ids/assumable-ids/)
* [Demo Repository: custom-assembly-as-code](https://github.com/chainguard-demo/custom-assembly-as-code)
* [Get support](/get-started/get-support/)
