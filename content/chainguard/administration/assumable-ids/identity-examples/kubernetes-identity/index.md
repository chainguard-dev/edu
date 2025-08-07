---
title : "Create an Assumable Identity for a Kubernetes Pod"
linktitle: "Kubernetes"
aliases: []
lead: ""
description: "Procedural tutorial outlining how to create a Chainguard identity that can be assumed by a Kubernetes pod."
type: "article"
date: 2025-08-07T13:00:00+00:00
lastmod: 2025-08-07T13:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Procedural"]
images: []
weight: 012
---

Chainguard's [*assumable identities*](/chainguard/administration/iam-organizations/assumable-ids/)
are identities that can be assumed by external applications or workflows in
order to perform certain tasks that would otherwise have to be done by a human.

This procedural tutorial outlines how to create an identity that can be assumed
by a Kubernetes pod and then used to interact with the Chainguard API.

## Prerequisites

To complete this guide, you will need the following.

* `chainctl` — the Chainguard command line interface tool — installed on your
  local machine. Follow our guide on
  [How to Install `chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/)
  to set this up.
* `kubectl` - the command line interface tool for Kubernetes.
* Access to a Kubernetes cluster.

## Finding the Issuer URL of the Kubernetes Cluster

A Kubernetes cluster operates as an OIDC issuer. How you find the URL for that
issuer depends on where the cluster is running.

### GKE  (Google Kubernetes Engine)

The issuer URL for a GKE cluster will follow this format.

```
https://container.googleapis.com/v1/projects/<project>/locations/<location>/clusters/<cluster-name>
```

### EKS (Amazon Elastic Kubernetes Service)

```shell
aws eks describe-cluster \
  --name <cluster-name> \
  --query "cluster.identity.oidc.issuer" \
  --output text
```

### AKS (Azure Kubernetes Service)

```shell
az aks show \
  --name <cluster-name> \
  --resource-group <resource-group> \
  --query "oidcIssuerProfile.issuerUrl" \
  --output tsv
```

### Generic

You can issue a token with `kubectl` and find the issuer URL in the `iss`
claim with [`jwt`](https://github.com/mike-engel/jwt-cli).

```shell
kubectl create token default | jwt decode -
```

## Creating an Assumable Identity

Run this `chainctl` command to create an identity for the `default` service
account in the `default` namespace and assign it the `registry.pull` role.

Provide the issuer URL you identified in the previous step.

```shell
chainctl iam id create example-identity \
    --identity-issuer="<issuer-url>" \
    --subject-pattern="system:serviceaccount:default:default" \
    --role=registry.pull
```

This will return the ID of the identity which we will use in the next section.

If your cluster's issuer URL is not available over the internet then you can
create an identity by exporting the JWKS (JSON Web Key Set) from the cluster
with `kubectl` and provide it with the `--issuer-keys` flag.

```shell
chainctl iam identities create example-identity \
  --issuer-keys="$(kubectl get --raw /openid/v1/jwks)" \
  --identity-issuer=<issuer-url> \
  --subject=system:serviceaccount:default:default \
  --role=registry.pull
```

Many Kubernetes clusters will rotate the keys in the JWKS, so this command
creates a static identity that expires after a period of time. The default
duration is 30 days. In this scenario you should regularly recreate the
identity with the latest JWKS.

## Assume the Identity in a Pod

Create `pod.yaml` with this content. Replace `<identity-id>` in the
list of environment variables with the ID of the identity you created in the
previous step.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: assumable-id-demo
  namespace: default
spec:
  serviceAccountName: default
  restartPolicy: Never
  containers:
    - name: curl
      image: cgr.dev/chainguard/curl:latest-dev
      command:
        - sh
        - -c
        - |
          # Exchange the service account token for a Chainguard
          # API token
          IDENTITY_TOKEN=$(cat /var/run/chainguard/oidc/oidc-token)
          API_TOKEN=$(curl \
            -sSf \
            -H "Authorization: Bearer $IDENTITY_TOKEN" \
            "https://issuer.enforce.dev/sts/exchange?aud=https://console-api.enforce.dev&identity=$IDENTITY" \
            | jq -r .token
          )

          # List repos in the Chainguard registry
          curl -sSf -H "Authorization: Bearer $API_TOKEN" https://console-api.enforce.dev/registry/v1/repos | jq -r .items[].name
      env:
        - name: IDENTITY
          value: "<identity-id>"
      volumeMounts:
        - name: oidc-token
          mountPath: /var/run/chainguard/oidc
          readOnly: true
  volumes:
    - name: oidc-token
      projected:
        sources:
          - serviceAccountToken:
              path: oidc-token
              expirationSeconds: 600
              audience: issuer.enforce.dev
```

Then create the pod.

```shell
kubectl create -n default -f pod.yaml
```

Wait for the pod to complete and then view the logs. It should return a list of
the repositories in your organization.

```shell
kubectl -n default logs assumable-id-demo
```

## Clean Up

Delete the pod.

```shell
kubectl -n default delete pod assumable-id-demo
```

Delete the identity.

```shell
chainctl iam id delete <identity-id>
```

## Learn more

For more information about how assumable identities work in Chainguard, check
out our [conceptual overview of assumable identities](/chainguard/administration/iam-organizations/assumable-ids/).
