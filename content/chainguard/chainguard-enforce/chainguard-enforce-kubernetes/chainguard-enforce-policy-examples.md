---
title: "Example Policies for Chainguard Enforce"
type: "article"
description: "Chainguard Enforce for Kubernetes policy recipes"
date: 2022-15-07T15:22:20+01:00
lastmod: 2022-13-09T15:22:20+01:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-enforce-kubernetes"
weight: 100
toc: true
---

> _This provides user onboarding for Chainguard Enforce. In order to follow the onboarding, you will need access to Chainguard Enforce. You can request access through selecting **Chainguard Enforce for Kubernetes** on the [inquiry form](https://www.chainguard.dev/get-demo?utm_source=docs)._

Chainguard Enforce for Kubernetes allows users to create their own security policies that they can enforce in their clusters. Here are a few example policies to help you get started. You may also want to review the [Sigstore Policy Controller documentation](https://docs.sigstore.dev/policy-controller/overview).

## Policy enforcing signed containers from Chainguard Images

```
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: sample-policy
spec:
  images:
  - glob: "ghcr.io/chainguard-dev/*/*"
  - glob: "ghcr.io/chainguard-dev/*"
  - glob: "index.docker.io/*"
  - glob: "index.docker.io/*/*"
  authorities:
  - keyless:
      url: https://fulcio.sigstore.dev
```

An example using Docker Hub images:

```
...
  images:
  - glob: "index.docker.io/*"
  - glob: "index.docker.io/*/*"
...
```

## Policy enforcing signer identity through an OIDC provider and subject

```
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: policy-name
spec:
  images:
  - glob: "gcr.io/your-image-here/*"
  authorities:
  - keyless:
      identities: # <<<-- REPLACE the following with your OIDC provider & subject --> #
      - issuer: https://token.actions.githubusercontent.com
        subject: https://github.com/chainguard-dev/gke-demo/.github/workflows/release.yaml@refs/heads/main
```

An alternate issuer and subject:

```
...
      - issuer: https://accounts.google.com
        subject: your-gmail@gmail.com
```

## Policy enforcing that images have a signed SPDX SBOM attestation from a custom key

This policy asserts that all images must have a signed SPDX SBOM attestation from a custom key.

```
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: custom-key-attestation-sbom-spdxjson
spec:
  images:
  - glob: "**"
  authorities:
  - name: custom-key
    key:
      data: |
        -----BEGIN PUBLIC KEY-----
        ...
        -----END PUBLIC KEY-----
    attestations:
    - name: must-have-spdxjson
      predicateType: spdxjson
      policy:
        type: cue
        data: |
          predicateType: "https://spdx.dev/Document"
```

Set the `POLICY` and `IMAGES` environment variables appropriately, pointing to the sample policy and the image you would like to test.

```sh
POLICY="policies/custom-key-attestation-sbom-spdxjson.yaml"
```

Generate an SPDX SBOM, then attach the SBOM to your image:

```sh
cosign attest --type spdxjson
```

Next, sign it with a private key (for example, one located in a keys directory as in `keys/cosign.key`).

```sh
export COSIGN_PASSWORD=""

cosign attest --yes --type spdxjson \
  --predicate sboms/example.spdx.json \
  --key keys/cosign.key \
  "${IMAGE}"
```


## Policy enforcing that releases are signed by GitHub Actions

```
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: image-is-signed-by-github-actions
spec:
  images:
  # This is the release v0.3.0
  - glob: "gcr.io/projectsigstore/policy-webhook@sha256:d1e7af59381793687db4673277005276eb73a06cf555503138dd18eaa1ca47d6"
  authorities:
  - keyless:
      # Signed by Fulcio
      url: https://fulcio.sigstore.dev
      identities:
      # Matches the Github Actions OIDC issuer
      - issuer: https://token.actions.githubusercontent.com
        # Matches a specific GitHub workflow on main branch. Here we use the
        # Sigstore policy controller example testing workflow as an example.
        subject: "https://github.com/sigstore/policy-controller/.github/workflows/release.yaml@refs/tags/v0.3.0"
```