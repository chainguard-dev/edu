---
title: "Authenticating to Chainguard Registry"
type: "article"
description: "A guide on authenticating to the Chainguard Registry to get images"
date: 2023-03-21T15:10:16+00:00
lastmod: 2023-03-21T15:10:16+00:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 500
toc: true
---

### Public Images

All public Chainguard Images are available for free.

However, logging in with a Chainguard account and authenticating when pulling from the registry can provide a mechanism for Chainguard to contact you if there are any issues with images you are pulling.

This may include upcoming deprecations or changes in behavior, or critical vulnerabilities found and remediations applied to images being pulled.

### Authenticating with the credential helper

The easiest way to configure authentication is to use the credential helper included with `chainctl`.

First install `chainctl`, then log in and configure the credential helper:

```
chainctl auth login
chainctl auth configure-docker
```

This will update your Docker config file to call `chainctl` when an auth token is needed. A browser window will open when the token needs to be refreshed.

Pulls authenticated in this way are associated with your user.

### Authenticating with a Pull Token

You can also create a "pull token" using `chainctl`.

First install `chainctl`, then log in and configure a pull token:

```
chainctl auth login
chainctl auth configure-docker --pull-token
```

This will update your Docker config file with a long-lived username and password. This token expires in 30 days by default, but it can be copied to other locations such as CI jobs or Kubernetes secrets.

Pulls authenticated in this way are associated with a Chainguard identity, which is associated with the group selected when the pull token was created.

### Authenticating with GitHub Actions

You can configure authentication with OIDC-aware CI platforms like GitHub Actions.

First create an identity using `chainctl`, which can be limited to only allow OIDC federation from certain GitHub workflow runs:

```
chainctl auth identity create github [GITHUB-IDENTITY] \
  --github-repo=${GITHUB_ORG}/${GITHUB_REPO} \
  --github-ref=refs/heads/main \
  --role=registry.pull
```

This creates a Chainguard identity that can be assumed by a GitHub Actions workflow only for the specified GitHub repository, triggered on pushes to the specified branch (e.g., `refs/heads/main`), with permissions only to pull from the Chainguard Registry.

When this identity is created, its ID will be displayed. Using this ID, you can configure your GitHub Actions workflow to install `chainctl` and assume this identity when the workflow runs:

```
name: Chainguard Registry Example

on:
  push:
    branches: ['main']

permissions:
  contents: read
  id-token: write  # This is needed for OIDC federation.

jobs:
  example:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: chainguard-dev/actions/setup-chainctl@main
        with:
          identity: [[ The Chainguard Identity ID you created above ]]
      - runs: docker pull cgr.dev/chainguard/node
```

Pulls authenticated in this way are associated with the Chainguard identity you created, which is associated with the group selected when the identity was created.

If the identity is configured to only work with GitHub Actions workflow runs from a given repo and branch, that identity will not be able to pull from other repos or branches.
