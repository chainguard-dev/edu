---
title: "Excess Enforce"
type: "article"
lead: "Setup of Chainguard Enforce with Google Cloud Shell and Kind"
description: "Set up Chainguard Enforce with Google Cloud Shell and Kind"
date: 2022-15-07T15:22:20+01:00
lastmod: 2022-15-07T15:22:20+01:00
draft: false
unlisted: true
images: []
menu:
  docs:
    parent: "chainguard-enforce-kubernetes"
weight: 620
toc: true
---

## Customization options on the policy

### Enforce the identity of the signer

The following is an example of a policy that enforces signer identity.

```sh
cat > demo-policy.yaml <<EOF
apiVersion: policy.sigstore.dev/v1alpha1
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
EOF
```

Another example of OIDC issuer and subject.

```sh
      - issuer: https://accounts.google.com
        subject: your-gmail@gmail.com
```

## How to use private registries

Chainguard Enforce supports several methods of authenticating to private registries. Depending on your organization’s setup, you may leverage one or multiple of the supported authentication strategies.

### Generic private registries

To support the widest set of private registries, authentication via an `imagePullSecret` can be used. This is configured on a per-policy basis, and applies to all the images scoped to that policy.

#### From a private registry

If your images come from a completely private registry, first create an `imagePullSecret` in the **cosign-system** namespace:

```sh
kubectl create secret docker-registry regcreds -n cosign-system --docker-server=$privateregistry --docker-username=$username --docker-password=$password --docker-email=$email
```

> **NOTE**: It is important to ensure the secret is created in the cosign-system namespace, as this ensures the Chainguard Enforce agent can use this secret to authenticate images from all namespaces in the cluster.


From there, any policy defined that references images from `$privateregistry` can be linked to the appropriate `imagePullSecret` which is regcreds in this example.

```sh
cat > demo-policy-private-dockerhub.yaml <<EOF
apiVersion: policy.sigstore.dev/v1alpha1
kind: ClusterImagePolicy
metadata:
  name: policy-name
spec:
  images:
  - glob: "$privateregistry/*"
  authorities:
  - keyless:
      url: https://fulcio.sigstore.dev
    source:
      - oci: "$privateregistry"
        signaturePullSecrets:
          - name: regcreds
EOF
```

#### From Docker Hub

For images that come from a private namespace within Docker Hub (or any private registry), the credentials can be scoped to that specific namespace, rather than the whole registry.

Assuming the same regcreds secret as above, use the registry namespace to scope the credentials in each policy as follows:

```sh
cat > demo-policy-private-dockerhub.yaml <<EOF
apiVersion: policy.sigstore.dev/v1alpha1
kind: ClusterImagePolicy
metadata:
  name: policy-name
spec:
  images:
  - glob: "privatedockernamespace/*"
  authorities:
  - keyless:
      url: https://fulcio.sigstore.dev
    source:
      - oci: "index.docker.io/privatedockernamespace/image"
        signaturePullSecrets:
          - name: regcreds
EOF
```

> **NOTE**: For legacy Docker Hub reasons that have propagated to how container runtimes identify images, `privatedockernamespace/*` is equivalent to `index.docker.io/privatedockernamespace/*` —  both will work!

### Generic private registry using a pull secret

Associate GCR with an IAM group
Associate ECR with an IAM group
