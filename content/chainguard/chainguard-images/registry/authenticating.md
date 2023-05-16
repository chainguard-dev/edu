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
    parent: "registry"
weight: 500
toc: true
---

## Public Images

All public Chainguard Images are available for free.

However, logging in with a Chainguard account and authenticating when pulling from the registry provides a mechanism for Chainguard to contact you if there are any issues with images you are pulling.

This may enable Chainguard to notify you of upcoming deprecations, changes in behavior, critical vulnerabilities and remediations for images you have recently pulled.

## Signing Up

You can register a Chainguard account through our [sign up form](https://console.enforce.dev/auth/login?utm_source=docs). This will create your account and your organization's root [IAM group](/chainguard/chainguard-enforce/iam-groups/overview-of-enforce-iam-model/). If you already have an account, you can log in through the [login page]((https://console.enforce.dev/auth/login?utm_source=docs).

For more guidance on signing in, you can review our [sign in guidance](/chainguard/chainguard-enforce/authentication/log-in-chainguard-enforce/). If your organization is interested in (or already using) custom identity providers like Okta, you can read [how to authenticate to Chainguard with custom identity providers](/chainguard/chainguard-enforce/authentication/custom-idps/). 

## Authenticating with the `chainctl` Credential Helper

You can configure authentication by using the credential helper included with `chainctl`. This is the workflow recommended by Chainguard.

First [install `chainctl`](/chainguard/chainguard-enforce/how-to-install-chainctl/), and configure the credential helper:

```sh
chainctl auth configure-docker
```

This will update your Docker config file to call `chainctl` when an auth token is needed. A browser window will open when the token needs to be refreshed.

Pulls authenticated in this way are associated with your user.

## Authenticating with a Pull Token

You can also create a "pull token" using `chainctl`.

First [install `chainctl`](/chainguard/chainguard-enforce/how-to-install-chainctl/), then log in and configure a pull token:

```sh
chainctl auth configure-docker --pull-token
```

This will update your Docker config file with a long-lived username and password. This token expires in 30 days by default, which can be shortened using the `--ttl` flag (for example, `--ttl=24h`).

The token can be copied to other locations such as CI jobs, Kubernetes secrets, or even used for registry mirroring with tools like Artifactory.

Pulls authenticated in this way are associated with a Chainguard identity, which is associated with the group selected when the pull token was created.

### Note on Multiple Pull Tokens

Running the `chainctl auth configure-docker --pull-token` command multiple times will result in multiple pull tokens. However, the tokens are stored in your Docker config and subsquent token generation will overwrite old tokens.

Tokens cannot be retrieved once they have been overwritten so they must be extracted from the local Docker config and saved elsewhere if multiple are required.

### Revoking a Pull Token

Pull tokens are associated with Chainguard identities so they can be viewed with:

```sh
chainctl iam identities list
```

To revoke a token, delete the associated identity.

```sh
chainctl iam identity delete <identity UUID>
```

## Authenticating with GitHub Actions

You can configure authentication with OIDC-aware CI platforms like GitHub Actions.

First create an identity using `chainctl`, which can be limited to only allow OIDC federation from certain GitHub workflow runs:

```sh
chainctl iam identity create github [GITHUB-IDENTITY] \
  --github-repo=${GITHUB_ORG}/${GITHUB_REPO} \
  --github-ref=refs/heads/main \
  --role=registry.pull
```

This creates a Chainguard identity that can be assumed by a GitHub Actions workflow only for the specified GitHub repository, triggered on pushes to the specified branch (such as `refs/heads/main`), with permissions only to pull from the Chainguard Registry.

When this identity is created, its ID will be displayed. Using this ID, you can configure your GitHub Actions workflow to install `chainctl` and assume this identity when the workflow runs:

```yaml
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
      - run: docker pull cgr.dev/chainguard/node
```

Pulls authenticated in this way are associated with the Chainguard identity you created, which is associated with the group selected when the identity was created.

If the identity is configured to only work with GitHub Actions workflow runs from a given repo and branch, that identity will not be able to pull from other repos or branches, including pull requests targetting the specified branch.

## Authenticating with Kubernetes

You can also configure a Kubernetes cluster to use a pull token, as described above.

When you create a pull token, your Docker config file is updated to include that token and configure it to be used when pulling images from `cgr.dev`.

After that, you can create a Kubernetes secret based on those credentials, following [these instructions](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#registry-secret-existing-credentials):

```sh
kubectl create secret generic regcred \
    --from-file=.dockerconfigjson=<path/to/.docker/config.json> \
    --type=kubernetes.io/dockerconfigjson
```

**Important Note:** this will also make any other credentials you have configured in your Docker config available in the secret! Ensure only the necessary credentials are included.

Then you can create a Pod that uses that secret, following [these instructions](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#create-a-pod-that-uses-your-secret):

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: cgr-example
spec:
  containers:
  - name: nginx
    image: cgr.dev/chainguard/nginx:latest
  imagePullSecrets:
  - name: regcred
```

For this example, save the file as `cgr-example.yaml`. Then you can create and get the Pod:

```sh
kubectl apply -f cgr-example.yaml
kubectl get pod cgr-example
```
