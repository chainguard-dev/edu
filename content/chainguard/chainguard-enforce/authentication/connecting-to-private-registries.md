---
title: "Connect Enforce to Private Container Registries"
linktitle: "Connect to Private Registries"
aliases:
- /chainguard/chainguard-enforce/chainguard-enforce-kubernetes/connecting-to-private-registries/
type: "article"
lead: ""
description: "How to connect Chainguard Enforce to a private container registry"
date: 2022-09-02T15:56:52-07:00
lastmod: 2022-11-18T15:56:52-07:00
draft: false
tags: ["Enforce", "Product", "Procedural"]
images: []
menu:
  docs:
    parent: "authentication"
weight: 020
toc: true
---

Chainguard Enforce supports two methods of authenticating to private registries:

- Using image pull secrets in your tenant clusters
- Using cloud account associations to the cloud provider running your registry

Depending on your organization’s setup, you may leverage one or both of the supported authentication strategies.

## Image Pull Secrets

To support the widest set of private registries, you can authenticate using a Kubernetes image pull secret. This is configured on a per-policy basis, and applies to all the images scoped to that policy. 

### Configuring your image pull secret

To verify policies using attestation and signatures for images in a private registry, create an image pull secret in the `cosign-system` namespace of your cluster. The following example creates a secret named `regcreds`, but you could provide a different name if you like. Additionally, the `docker-registry` subcommand creates a secret that is specifically for use with a Docker registry.

In the next lines, fill in your own details for the private registry, username, password, and email, substituting those values for the variables.


```sh
kubectl create secret docker-registry regcreds \
    -n cosign-system \
    --docker-server=$privateregistry \
    --docker-username=$username \
    --docker-password=$password \
    --docker-email=$email
```

> **Note**: It is important to ensure the secret is created in the `cosign-system` namespace, as this ensures the Chainguard Enforce agent can use this secret to authenticate images from all namespaces in the cluster.

The same image pull secret must be added to the `cosign-system` namespace of every cluster that you’d like to enforce policies in.

### Using your image pull secret in a policy

Once you’ve created your image pull secret, you can reference it in a cluster image policy using the authority’s source specification. This example requires all containers from a private registry with hostname `registry.example.com` to be signed by the public Fulcio instance:

```yaml
apiVersion: policy.sigstore.dev/v1alpha1
kind: ClusterImagePolicy
metadata:
  name: images-from-private-registry-are-signed
spec:
  images:
  - glob: "registry.example.com/*"
  authorities:
  - keyless:
      url: https://fulcio.sigstore.dev
      identities:
        - issuerRegExp: ".*"
          subjectRegExp: ".*"
    source:
    - oci: "registry.example.com"
      signaturePullSecrets:
      - name: regcreds
```

In this example, add the name of your private registry directory in `glob` and include the name of the private registry in `oci`. Note that the value you pass to the `oci` key cannot be a glob pattern and must be a valid repository name. Also, be aware that you will have set up `regcreds` in the previous `kubectl create secret` command; be sure to change this value if you gave your secret a different name.


### Scoping image pull secret credentials to a registry namespace

Some registries, like Docker Hub, can issue credentials that are scoped to a particular private namespace in the registry. To use these namespace scoped credentials in a cluster image policy, modify the authority’s source specification to include the namespace. This example uses credentials scoped to the Docker hub namespace `"privatenamespace"`:

```yaml
apiVersion: policy.sigstore.dev/v1alpha1
kind: ClusterImagePolicy
metadata:
  name: images-from-private-namespace-are-signed
spec:
  images:
  - glob: "privatenamespace/*"
  authorities:
  - keyless:
      url: https://fulcio.sigstore.dev
      identities:
        - issuerRegExp: ".*"
          subjectRegExp: ".*"
    source:
    - oci: "index.docker.io/privatenamespace/$image"
      signaturePullSecrets:
      - name: regcreds
```

Replace the variables pointing to your private Docker namespace next to `glob` and `oci`. 

> **Note**: For legacy Docker Hub reasons that have propagated to how container runtimes identify images, `privatenamespace/*` is equivalent to `index.docker.io/privatenamespace/*` — both will work!

## Cloud account associations

If your private registry is either AWS’s Elastic Container Registry (ECR) or Google Cloud’s Google Container Registry (GCR), you can leverage Enforce for Kubernetes’ cloud account association feature to allow Enforce to authenticate to your registry. While support is limited to ECR and GCR, cloud account associations remove the need to maintain image pull secrets in all clusters and no long term access credentials are stored by our platform.

### Configuring your cloud account association

Detailed instructions can be found in our dedicated article on [How to Set Up Chainguard Enforce Cloud Account Associations](/chainguard/chainguard-enforce/cloud-account-associations/). Once you have a cloud account association configured at a specified group level, policies at or below that group can be verified against private registries in the associated cloud account. 

### Using Google Container Registry images in policies

In GCP, you can verify that an account association is correctly configured by running:

```
chainctl iam groups check-gcp $group_name
```

If successful, you will receive a message similar to the following:

```
2022/09/01 11:26:47 GCP role impersonation was successful!
```

You can now write policies under `$group_name` that refer to images in your associated GCP project:

```yaml
apiVersion: policy.sigstore.dev/v1alpha1
kind: ClusterImagePolicy
metadata:
  name: gcr-is-signed
spec:
  images:
  - glob: "gcr.io/$your-gcp-project/*"
  authorities:
  - keyless:
      url: https://fulcio.sigstore.dev
      identities:
        - issuerRegExp: ".*"
          subjectRegExp: ".*"
```

Be sure to replace `$your-gcp-project` with your relevant project name. 

### Using AWS Elastic Container Registry Images in Policies

In AWS, you can verify that an account association is correctly configured by running the following.

```sh
chainctl iam groups check-aws $group_name
```

If successful, you will receive a message back that’s similar to this output:

```
2022/09/01 11:26:47 AWS role impersonation was successful!
```

You can now write policies under `$group_name` that refer to images in your associated AWS Account:

```yaml
apiVersion: policy.sigstore.dev/v1alpha1
kind: ClusterImagePolicy
metadata:
  name: ecr-is-signed
spec:
  images:
  - glob: "$aws_account_id.dkr.ecr.us-west-2.amazonaws.com/*"
  authorities:
  - keyless:
      url: https://fulcio.sigstore.dev
      identities:
        - issuerRegExp: ".*"
          subjectRegExp: ".*"
```

Be sure to replace the variable next to glob with your relevant account information, within the double quotes.
