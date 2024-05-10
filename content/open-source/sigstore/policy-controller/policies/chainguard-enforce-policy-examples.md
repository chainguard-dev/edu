---
title: "Example Policies"
aliases: 
- /chainguard/chainguard-enforce/chainguard-enforce-kubernetes/chainguard-enforce-policy-examples/
type: "article"
description: "Policy recipes"
date: 2022-07-15T15:22:20+01:00
lastmod: 2024-05-10T15:22:20+01:00
draft: false
tags: ["Open Source", "Procedural", "Policy", "policy-controller" "Reference", "SBOM"]
images: []
menu:
  docs:
    parent: "policies"
weight: 075
toc: true
---

The [Sigstore Policy Controller](https://docs.sigstore.dev/policy-controller/overview/) allows users to create their own security policies that they can be enforced on Kuberenetes clusters. Here are a few example policies to help you get started. 

You may also review the [Sigstore Policy Controller documentation](https://docs.sigstore.dev/policy-controller/overview). In particular, we encourage you to review the Policy Controller documentation relating to the [Admission of images](https://docs.sigstore.dev/policy-controller/overview/#admission-of-images) to learn how to admit images through the cluster image policy.

## Policy enforcing signed containers

```
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: signed-keyless
spec:
  images:
    # All images
    - glob: "**"
  authorities:
    - keyless:
        url: https://fulcio.sigstore.dev
      ctlog:
        url: https://rekor.sigstore.dev
```

Examples using Chainguard Images from the Chainguard Registry or the GitHub Container Registry, respectively:

```
...
  images:
    - glob: cgr.dev/chainguard/**
    - glob: ghcr.io/chainguard-images/**
...
```

An example using Docker Hub images:

```
...
  images:
    - glob: "index.docker.io/*"
    - glob: "index.docker.io/*/*"
...
```

An example using Google Cloud Registry:

```
...
  images:
    - glob: gcr.io/your-image-here/*
...
```

## Policy enforcing signer identity through an OIDC provider and subject

```
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: enforce-signer-oidc
spec:
  images:
    - glob: "**"
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
    - glob: gcr.io/your-image-here/*
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

## Policy allowing trusted GKE images

```
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: gke-trusted
spec:
  images:
    - glob: gke.gcr.io/**
    - glob: gcr.io/gke-release/*
  authorities:
    - static:
        action: pass
```
## Enforce that cert-manager is signed

```
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: certmanager-signed
spec:
  images:
    - glob: quay.io/jetstack/cert-manager-*
  authorities:
    - key:
        data: |
          -----BEGIN PUBLIC KEY-----
          MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAsZZKaaIRjOpzbiWYIDKO
          yry9XGBqAfve1iOGmt5VO1jpjNoEseT6zewozHfWTM7osxayy2WjN8G+QV39MlT3
          Vxo91/31g+Zcq8KcvxG+iB8GRaD9pNgLmghorv+eYDiPYMO/+fhsLImyG5WEoPct
          MeCBD7umZ/A2t96U9DQxVDqQbTHlsNludno1p1wsgRnfUM3QHexNljDvJg5FcDMo
          dCpVLpRNvbw0lbJVfybJ4siJ5o/MmXzy0QCJpw+yMIqvqMc8qgKJ1yooJtuTVF4t
          4/luP+EG/oVIiSWCFeRMqYdbJ3R+CJi+4LN7vFNYQM1Q/NwOB52RteaR7wnqmcBz
          qSYK32MM8xdPCQ5tioWwnPTRbPZuzsZsRmJsKBO9JUrBYdDntZX1xY5g4QNSufxi
          QgJgJSU7E4VGMvagEzB1JzvOr6A/qNFCO1Z6JsA3jw3cJLV1rSHfxqfSXBACTLDf
          6bOPWRILRKydTJA6uLKNKmo1/nFm3jvd5tHKOjy4VAQLJ/Vx9wBsAAiLa+06veun
          Oz3AJ9sNh3wLp21RL11u9TuOKRBipE/TYsBYp8jpIyWPXDSV+JcD/TZqoT8y0Z6S
          0damfUmspuK9DTQFL2crpeaqJSG9RA+OuPZLxGD1IMURTsPJB7kXhPtmceeirBnw
          sVcRHHDitVt8oO/x4Wus1c0CAwEAAQ==
          -----END PUBLIC KEY-----
        hashAlgorithm: sha512
```

## Enforce that Chainguard agent is signed

```
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: chainguard-agent-is-signed
spec:
  images:
    - glob: us.gcr.io/prod-enforce-fabc/**
  authorities:
    - ctlog:
        url: https://rekor.sigstore.dev
      keyless:
        identities:
          - issuer: https://token.actions.githubusercontent.com
            subject: https://github.com/chainguard-dev/mono/.github/workflows/.release-drop.yaml@refs/heads/main
          - issuer: https://token.actions.githubusercontent.com
            subject: https://github.com/chainguard-dev/mono/.github/workflows/.build-drop.yaml@refs/heads/main
        url: https://fulcio.sigstore.dev
```

## Enforce that Google's distroless images are signed

```
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: google-distroless-signed
spec:
  images:
    - glob: gcr.io/distroless/static*
  authorities:
    - ctlog:
        url: https://rekor.sigstore.dev
      keyless:
        identities:
          - issuer: https://accounts.google.com
            subject: keyless@distroless.iam.gserviceaccount.com
        url: https://fulcio.sigstore.dev
```

## Enforce that Istio images are signed

```
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: istio-signed
spec:
  images:
    - glob: index.docker.io/istio/*
  authorities:
    - key:
        data: |
          -----BEGIN PUBLIC KEY-----
          MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEej5bv2n2vOecKineYGWwq1WaQa7C
          7HTEVN+BkNI4D1+66ufzn1eGTrbaC9dceJqCAkhp37vMxhWOrGufpBUokg==
          -----END PUBLIC KEY-----
```

