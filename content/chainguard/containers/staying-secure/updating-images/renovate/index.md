---
title: "Using Renovate with Chainguard Containers"
linktitle: "Using Renovate"
aliases:
- /chainguard/chainguard-images/working-with-images/renovate/
- /chainguard/chainguard-images/staying-secure/updating-images/renovate/
- /chainguard/containers/working-with-images/renovate/
- /chainguard/containers/staying-secure/updating-images/renovate/
type: "article"
description: "How to use Renovate to automatically keep Chainguard Containers updated"
date: 2023-09-05T11:07:52+02:00
lastmod: 2026-08-03T18:16:45+00:00
draft: false
tags: ["Chainguard Containers"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 020
toc: true
---

[Renovate](https://github.com/renovatebot/renovate) can be used to alert on updates to Chainguard Containers. This can be an effective way to keep your images up-to-date and free of CVEs. This article explains how to configure Renovate to support Chainguard Containers.

> **NOTE**: This article describes using Renovate to alert on new versions of Chainguard Containers. It is not about alerts for Wolfi packages (which is unsupported at the time of writing).

## Prerequisites

This guide assumes you have successfully installed and configured Renovate. If you haven't already set this up, please refer to the [installation instructions](https://docs.renovatebot.com/getting-started/installing-onboarding/).

Additionally, several examples in this guide assume you have `chainctl` — Chainguard's command-line interface — installed on your local machine. Follow our guide on [How to install `chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/) to set this up.

## Setting up credentials for Renovate

In order to support versioned images from a private repository, you must provide Renovate with credentials to access the [Chainguard registry](/chainguard/containers/chainguard-registry/overview/) at `cgr.dev`. You can do this by creating a token with `chainctl`, as in this example:

```shell
chainctl auth configure-docker --pull-token
```

This command responds with output such as:

```shell
To use this pull token in another environment, run this command:

    docker login "cgr.dev" --username "<USERNAME>" --password "<PASSWORD>"
```

By default, this credential is good for 30 days.

You can now configure `hostRules` in Renovate to support the Chainguard registry. Depending on how Renovate was set up, you can add this to your Renovate configuration with a setting such as:

```json
{
...
   "hostRules": [
    {
      "hostType": "docker",
      "matchHost": "cgr.dev",
      "username": "<USERNAME>",
      "password": "<PASSWORD>"
     }]
}
```

Be aware that you **SHOULD NOT** check this file into source control with the exposed secret. Instead, you can use environment variables which you pass in at runtime if you use a `config.js` file:

```json
module.exports = {
...
   "hostRules": [
    {
      "hostType": "docker",
      "matchHost": "cgr.dev",
      "username": process.env.CGR_USERNAME,
      "password": process.env.CGR_PASSWORD,
     }]
};
```

But an even more secure solution would be to create a script which automatically updates the configuration with the correct values by calling `chainctl`. If you do this, you should also set the credential lifetime to a much shorter period with the `--ttl` flag:

```shell
chainctl auth configure-docker --pull-token --ttl 10m
```

This sets the pull token's lifetime to 10 minutes, which limits the risk posed if the token should leak. You can also set the lifetime to a longer period for more manual configurations.

## Updating versioned container images

By default, Renovate will now open PRs for any out-of-date versions of images it finds. For example, you can run Renovate by pushing the following Dockerfile to a repository overseen by Renovate:

```dockerfile
FROM cgr.dev/chainguard.edu/python:3.11-dev AS builder
...

FROM cgr.dev/chainguard.edu/python:3.11
...
```

At the time of writing, version 3.12 was the current version of the Python image, so the following PR was opened by Renovate:

![Screenshot showing GitHub PR from Renovate updating python version](python_update.png)

Not all images use semantic versioning. Refer to the [Renovate documentation](https://docs.renovatebot.com/) for details on how to support different schemes.

Ideally, image references should also be pinned to a digest, as shown in the following section.

## Updating `:latest` container images

Renovate also supports updating image references that are pinned to digests. This allows you to keep floating tags such as `:latest` in sync with the most up-to-date version.

As an example, the following Dockerfile prompts Renovate to open two similar pull requests:

```dockerfile
FROM cgr.dev/chainguard/go:latest-dev@sha256:ff187ecd4bb5b45b65d680550eed302545e69ec4ed45f276f385e1b4ff0c6231 AS builder

WORKDIR /work

COPY go.mod /work/
COPY cmd /work/cmd
COPY internal /work/internal

RUN CGO_ENABLED=0 go build -o hello ./cmd/server

FROM cgr.dev/chainguard/static:latest@sha256:5e9c88174a28c259c349f308dd661a6ec61ed5f8c72ecfaefb46cceb811b55a1
COPY --from=builder /work/hello /hello

ENTRYPOINT ["/hello"]
```

The following screenshot shows the PR to update the static image:

![Screenshot showing Renovate PR to update static image digest](static_update.png)

## Pinning digests

The `pinDigests` option configures Renovate to add digests to image references that don't contain them.

The following example Renovate configuration includes this option:

```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": [
    "config:recommended"
  ],
  "packageRules": [
    {
      "matchDatasources": ["docker"],
      "pinDigests": true
    }
  ]
}
```

This configures Renovate to open PRs that will pin a reference like `cgr.dev/chainguard/python:3.12` to a digest like the following:

```
cgr.dev/chainguard/python:3.12@sha256:e3b524a97c37c32ba590aae0ebcebe3a983c1f69a5093b670fdba980f97a09b3
```

You can also use the `matchUpdateTypes` option to disable updates for any types other than `digest`.

Here is an example Renovate configuration that does this:

```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": [
    "config:recommended"
  ],
  "packageRules": [
    {
      "matchDatasources": ["docker"],
      "matchUpdateTypes": [
        "major",
        "minor",
        "patch"
      ],
      "enabled": false
    }
  ]
}
```

This configures Renovate to update the digest for a reference but not the tag.

The benefit of this approach is that it allows you to define your update strategy for each image reference by the use of a mutable tag, rather than having separate rules for different images in your Renovate configuration, similar to Chainguard's [Digestabot](https://github.com/chainguard-dev/digestabot) Github Action.

## Updating Chainguard Helm charts in Helmfiles

Renovate supports updating [Helmfile](https://helmfile.readthedocs.io/) releases with its [built-in `helmfile` manager](https://docs.renovatebot.com/modules/manager/helmfile/). However, it doesn't presently support updating [digest references](/chainguard/containers/how-to-use/container-image-digests/) for OCI chart URLs, which is a [recommended practice when deploying Chainguard Helm charts](/chainguard/containers/how-to-use/use-chainguard-helm-charts/#pin-to-digest). See [renovatebot/renovate#45054](https://github.com/renovatebot/renovate/discussions/45054) for more details.

To pin Chainguard Helm charts to digests and update them with Renovate, you can use a [custom `jsonata` manager](https://docs.renovatebot.com/modules/manager/jsonata/) as a workaround.

Given a `helmfile.yaml` such as:

```yaml
releases:
  - name: kube-prometheus-stack
    chart: oci://cgr.dev/<org>/charts/kube-prometheus-stack@sha256:833bd55297054df0afdbe47750013b8e2eff930059c63c0746447fa8d0b729d3
    version: 87.4.0
    namespace: monitoring
  - name: nginx
    chart: oci://cgr.dev/<org>/iamguarded-charts/nginx@sha256:7b88d44da254fc764171da809471d10c6cf15b9ab0ddcb4b475b9a8f380aeb79
    version: 22.1.0
    namespace: nginx
```

Configure Renovate with the example below, replacing every instance of `cgr.dev/<org>` with your Chainguard organization or internal mirror/proxy.

```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "packageRules": [
    {
      "matchManagers": ["helmfile"],
      "matchPackagePatterns": [
        "^cgr\\.dev/<org>/(charts|iamguarded-charts)/"
      ],
      "enabled": false
    }
  ],
  "customManagers": [
    {
      "customType": "jsonata",
      "fileFormat": "yaml",
      "fileMatch": ["(^|/)helmfile\\.ya?ml$"],
      "matchStrings": [
        "releases[$contains(chart, 'cgr.dev/<org>/charts/')].($n := $substringAfter($substringBefore(chart & '@', '@'), 'charts/'); $exists(version) ? { 'depName': $n, 'packageName': 'cgr.dev/<org>/charts/' & $n, 'currentValue': version, 'currentDigest': $substringAfter(chart, '@') } : { 'depName': $n, 'packageName': 'cgr.dev/<org>/charts/' & $n, 'currentDigest': $substringAfter(chart, '@') })"
      ],
      "datasourceTemplate": "docker"
    },
    {
      "customType": "jsonata",
      "fileFormat": "yaml",
      "fileMatch": ["(^|/)helmfile\\.ya?ml$"],
      "matchStrings": [
        "releases[$contains(chart, 'cgr.dev/<org>/iamguarded-charts/')].($n := $substringAfter($substringBefore(chart & '@', '@'), 'iamguarded-charts/'); $exists(version) ? { 'depName': $n, 'packageName': 'cgr.dev/<org>/iamguarded-charts/' & $n, 'currentValue': version, 'currentDigest': $substringAfter(chart, '@') } : { 'depName': $n, 'packageName': 'cgr.dev/<org>/iamguarded-charts/' & $n, 'currentDigest': $substringAfter(chart, '@') })"
      ],
      "datasourceTemplate": "docker"
    }
  ]
}
```

## Updating Chainguard Helm charts in ArgoCD applications

Renovate supports updating [ArgoCD](https://argo-cd.readthedocs.io/) `Application` manifests with its [built-in `argocd` manager](https://docs.renovatebot.com/modules/manager/argocd/). However, it doesn't presently support updating [digest references](/chainguard/containers/how-to-use/container-image-digests/) for OCI chart URLs, which is a [recommended practice when deploying Chainguard Helm charts](/chainguard/containers/how-to-use/use-chainguard-helm-charts/#pin-to-digest). See [renovatebot/renovate#45055](https://github.com/renovatebot/renovate/discussions/45055) for more details.

To pin Chainguard Helm charts to digests and update them with Renovate, you can use a [custom `jsonata` manager](https://docs.renovatebot.com/modules/manager/custom.jsonata/) as a workaround.

Given `Application` manifests such as:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: kube-prometheus-stack
spec:
  source:
    repoURL: oci://cgr.dev/<org>/charts
    chart: kube-prometheus-stack
    targetRevision: 87.4.0@sha256:833bd55297054df0afdbe47750013b8e2eff930059c63c0746447fa8d0b729d3
---
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: nginx
spec:
  source:
    repoURL: oci://cgr.dev/<org>/iamguarded-charts
    chart: nginx
    targetRevision: 22.1.0@sha256:7b88d44da254fc764171da809471d10c6cf15b9ab0ddcb4b475b9a8f380aeb79
```

Configure Renovate as in the example below, replacing every instance of `cgr.dev/<org>` with your Chainguard organization or internal mirror/proxy.

```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "packageRules": [
    {
      "matchManagers": ["argocd"],
      "matchPackagePatterns": [
        "^cgr\\.dev/<org>/(charts|iamguarded-charts)/"
      ],
      "enabled": false
    }
  ],
  "customManagers": [
    {
      "customType": "jsonata",
      "fileFormat": "yaml",
      "fileMatch": ["\\.ya?ml$"],
      "matchStrings": [
        "spec.source[$contains(repoURL, 'cgr.dev/<org>/charts')].($tr := targetRevision; $substring($tr, 0, 7) = 'sha256:' ? { 'depName': chart, 'packageName': 'cgr.dev/<org>/charts/' & chart, 'currentDigest': $tr } : { 'depName': chart, 'packageName': 'cgr.dev/<org>/charts/' & chart, 'currentValue': $substringBefore($tr & '@', '@'), 'currentDigest': $substringAfter($tr, '@') })"
      ],
      "datasourceTemplate": "docker"
    },
    {
      "customType": "jsonata",
      "fileFormat": "yaml",
      "fileMatch": ["\\.ya?ml$"],
      "matchStrings": [
        "spec.source[$contains(repoURL, 'cgr.dev/<org>/iamguarded-charts')].($tr := targetRevision; $substring($tr, 0, 7) = 'sha256:' ? { 'depName': chart, 'packageName': 'cgr.dev/<org>/iamguarded-charts/' & chart, 'currentDigest': $tr } : { 'depName': chart, 'packageName': 'cgr.dev/<org>/iamguarded-charts/' & chart, 'currentValue': $substringBefore($tr & '@', '@'), 'currentDigest': $substringAfter($tr, '@') })"
      ],
      "datasourceTemplate": "docker"
    }
  ]
}
```

## Updating Chainguard Helm charts in Flux

Renovate natively supports updating [Flux](https://fluxcd.io/) `OCIRepository` resources with its [built-in `flux` manager](https://docs.renovatebot.com/modules/manager/flux/).

Given a Flux manifest such as:

```yaml
---
apiVersion: source.toolkit.fluxcd.io/v1
kind: OCIRepository
metadata:
  name: kube-prometheus-stack
  namespace: monitoring
spec:
  interval: 5m
  url: oci://cgr.dev/<org>/charts/kube-prometheus-stack
  ref:
    tag: 87.4.0
    digest: sha256:833bd55297054df0afdbe47750013b8e2eff930059c63c0746447fa8d0b729d3
---
apiVersion: helm.toolkit.fluxcd.io/v2
kind: HelmRelease
metadata:
  name: kube-prometheus-stack
  namespace: monitoring
spec:
  interval: 5m
  chartRef:
    kind: OCIRepository
    name: kube-prometheus-stack
```

Configure Renovate with the example below, adjusting the `flux.fileMatch` patterns to cover your repository layout. The `pinDigests` rule enforces the [recommended practice of pinning charts to a digest](/chainguard/containers/how-to-use/use-chainguard-helm-charts/#pin-to-digest): if an `OCIRepository` has a `tag` but no `digest`, Renovate opens a PR to add one.

```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "flux": {
    "fileMatch": [
      "(^|/)flux\\.ya?ml$",
      "(^|/)gotk-components\\.ya?ml$"
    ]
  },
  "packageRules": [
    {
      "matchManagers": ["flux"],
      "matchDatasources": ["docker"],
      "matchPackagePatterns": [
        "^cgr\\.dev/<org>/(charts|iamguarded-charts)/"
      ],
      "pinDigests": true
    }
  ]
}
```

## Running Renovate in GitHub Actions

You can use [`renovatebot/github-action`](https://github.com/renovatebot/github-action) to run Renovate from a GitHub Actions workflow. This can be combined with an [assumable identity](/chainguard/administration/assumable-ids/assumable-ids/) to authenticate to `cgr.dev` and update references to Chainguard container images in your repository.

> **Note**: This section assumes you have permissions to create identities in your Chainguard organization.

First, create a Renovate configuration file at the root of your GitHub repository. Refer to the [official documentation](https://docs.renovatebot.com/configuration-options/) for all the supported options.

This is an example of a minimal configuration:

```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json"
}
```

Push this file to the `main` branch of your repository.

Next, create an assumable identity for your GitHub repository. The `--github-repo` value embeds GitHub's immutable numeric owner and repository IDs; refer to [Finding your repository's numeric identifiers](/platform/administration/assumable-ids/identity-examples/github-identity/#finding-your-repositorys-numeric-identifiers) for how to retrieve them and when the format applies.

```shell
chainctl iam identities create github <identity-name> \
  --github-repo=<github-org>@<owner-id>/<github-repo-name>@<repo-id> \
  --github-ref=refs/heads/main \
  --role=registry.pull
```

Create a workflow file named `.github/workflows/renovate.yaml` with the following content. Replace `<identity-id>` with the ID returned by the previous command.

```yaml
name: Renovate

on:
  workflow_dispatch:
  schedule:
    - cron: "0 3 * * *"

permissions:
  contents: read

jobs:
  renovate:
    name: Renovate
    runs-on: ubuntu-latest

    permissions:
      contents: write
      pull-requests: write
      issues: write
      id-token: write

    steps:
    - uses: chainguard-dev/setup-chainctl@be0acd273acf04bfdf91f51198327e719f6af978 # v0.4.0
      with:
        identity: "<identity-id>"

    - shell: bash
      run: |
        RENOVATE_DOCKER_CGR_DEV_PASSWORD=$(chainctl auth token --audience=cgr.dev)
        echo "::add-mask::$RENOVATE_DOCKER_CGR_DEV_PASSWORD"
        echo "RENOVATE_DOCKER_CGR_DEV_PASSWORD=$RENOVATE_DOCKER_CGR_DEV_PASSWORD" >> $GITHUB_ENV

    - name: Run Renovate
      uses: renovatebot/github-action@6927a58a017ee9ac468a34a5b0d2a9a9bd45cac3 # v43.0.11
      env:
        RENOVATE_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        RENOVATE_REPOSITORIES: ${{ github.repository }}
        RENOVATE_DETECT_HOST_RULES_FROM_ENV: "true"
        RENOVATE_DOCKER_CGR_DEV_USERNAME: "_token"
```

This workflow performs the following steps:

* Installs chainctl and logs in as the assumable identity you created.
* Exports a short lived token for cgr.dev as `RENOVATE_DOCKER_CGR_DEV_PASSWORD`.
* Runs renovate with `RENOVATE_DETECT_HOST_RULES_FROM_ENV=true` so that it uses the password exported by the previous step.

Push this file to your repository's `main` branch.

This workflow is scheduled to run at 3:00 a.m. every morning. You can trigger it manually by navigating to **Actions > Renovate** and selecting **Run workflow**.

Once the workflow has ran successfully, you will find pull requests in your repository for any image references that need to be updated.

## Running Renovate with Docker

Chainguard provide [an image for Renovate](https://images.chainguard.dev/directory/image/renovate/overview). This is an example of how you can run this image to keep references to Chainguard images up to date in a GitHub repository.

> **Note**: To follow along with this section, you must have access to Chainguard's `renovate` container image.

To begin, generate a Personal Access Token for your GitHub user as described in Renovate's [official documentation](https://docs.renovatebot.com/modules/platform/github/#authentication).

Export the token as an environment variable named `RENOVATE_TOKEN`:

```shell
export RENOVATE_TOKEN=ghp_XXXXXXXXXXXXXXXXXX
```

Next, create a Renovate configuration file at the root of any GitHub repositories you want to target with Renovate. Refer to the [official documentation](https://docs.renovatebot.com/configuration-options/) for all the supported options.

This is an example of the most minimal configuration:

```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json"
}
```

Then, log in with `chainctl`:

```shell
chainctl auth login
```

Finally, run Renovate. Substitute `<org-name>` with the name of your Chainguard organization and provide any GitHub repositories that you want to target as arguments in the form `<github-org>/<github-repo-name>`:

```shell
docker run \
  -it \
  --rm \
  -e RENOVATE_TOKEN="${RENOVATE_TOKEN}" \
  -e RENOVATE_DETECT_HOST_RULES_FROM_ENV=true \
  -e RENOVATE_DOCKER_CGR_DEV_USERNAME=_token \
  -e RENOVATE_DOCKER_CGR_DEV_PASSWORD=$(chainctl auth token --audience cgr.dev) \
  cgr.dev/<org-name>/renovate \
  <github-org>/<github-repo-name>
```

This example passes a short-lived token for `cgr.dev` using the `RENOVATE_DOCKER_CGR_DEV_PASSWORD` environment variable.

## Troubleshooting

### Validate Renovate configuration

If Renovate isn't working as expected, try running it in debug mode and/or dumping the resolved configuration.

For example:

```
LOG_LEVEL=debug renovate --print-config
...
       "hostRules": [
         {
           "hostType": "docker",
           "matchHost": "cgr.dev",
           "username": "<Organizations ID>/<pull token ID>",
           "password": "***********",
           "resolvedHost": "cgr.dev"
         },
         {"matchHost": null, "hostType": "local"}
       ]
...
DEBUG: hostRules: basic auth for https://cgr.dev (repository=local)
DEBUG: getLabels(https://cgr.dev, ORGANIZATION/static, latest) (repository=local)
DEBUG: getManifestResponse(https://cgr.dev, ORGANIZATION/static, latest, get) (repository=local)
DEBUG: getManifestResponse(https://cgr.dev, ORGANIZATION/static, sha256:76d71eb53b1b44ec955529ece91c6da222a54fed660ca6b25124935bdd96e133, get) (repository=local)
DEBUG: found labels in manifest (repository=local)
       "labels": {
         "dev.chainguard.package.main": "static",
         "org.opencontainers.image.authors": "Chainguard Team https://www.chainguard.dev/",
         "org.opencontainers.image.created": "2024-12-04T19:55:37Z",
         "org.opencontainers.image.source": "https://github.com/chainguard-images/images-private/tree/main/images/static",
         "org.opencontainers.image.url": "https://images.chainguard.dev/directory/image/static/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-working-with-images-renovate",
         "org.opencontainers.image.vendor": "Chainguard"
       }
```

### Connection errors

If you have problems getting Renovate to monitor `cgr.dev`, please double check the connection details. Make sure the token is still valid (you can verify with `chainctl iam identities list`) and it has access to the repository you are referring to. You can test these credentials by running a `docker login` and `docker pull` in a clean environment.

### getReleaseList error

You may encounter errors such as the following:

```
DEBUG: getReleaseList error (repository=chainguard-images/images-private, branch=renovate/cgr.dev-chainguard.edu-python-3.x)
       "type": "github",
       "apiBaseUrl": "https://api.github.com/",
       "err": {
         "message": "`chainguard-images` forbids access via a personal access token (classic). Please use a GitHub App, OAuth App, or a personal access token with fine-grained permissions.",
         "stack": "Error: `chainguard-images` forbids access via a personal access token (classic). Please use a GitHub App, OAuth App, or a personal access token with fine-grained permissions.\n    at
…
```

These can be safely ignored. They are caused by Renovate using the `org.opencontainers.image.source` label on our images to look for a changelog. As this source is set to the private `images-private` GitHub repository, this request fails.
