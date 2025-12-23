---
title: "How to Use Octo STS with Kubernetes"
linktitle: "Kubernetes Integration"
type: "article"
lead: "Enable Kubernetes workloads to interact with GitHub repositories securely using OIDC-based workload identity federation without storing long-lived credentials"
description: "Learn about Octo STS for GitHub API access, enabling GitOps workflows and automated repository management from within clusters"
date: 2025-12-22T15:04:05+01:00
lastmod: 2025-12-22T15:04:05+01:00
tags: ["octo-sts", "Kubernetes", "OIDC", "Procedural"]
draft: false
images: []
menu:
  docs:
    parent: "octo-sts"
weight: 30
toc: true
---

Kubernetes workloads often need to interact with GitHub repositories for GitOps workflows, automated deployments, or repository management tasks. Traditionally, this requires storing GitHub Personal Access Tokens as Kubernetes secrets, creating security risks if the cluster or secrets are compromised.

This guide demonstrates how to use Kubernetes service account tokens with Chainguard's Octo STS to enable secure GitHub API access without storing long-lived credentials in your cluster.

## Prerequisites

Before you begin, ensure you have:

- A Kubernetes cluster (version 1.21 or later for OIDC token projection)
- `kubectl` configured to access your cluster
- Admin access to create service accounts and configure RBAC
- The octo-sts GitHub App installed on your target repository or organization
- A basic understanding of Kubernetes service accounts and OIDC

## Understanding Kubernetes OIDC Tokens

Kubernetes 1.21 introduced the ability to project service account tokens as OIDC-compliant tokens. These tokens:

- Are short-lived and automatically refreshed
- Can be bound to specific pods
- Include claims about the pod, namespace, and service account
- Can be configured with custom audiences

This makes them ideal for federation with external services like octo-sts.

## Step 1 — Configure the OIDC Issuer URL

Most Kubernetes distributions provide an OIDC issuer URL that Octo STS can validate. The issuer URL format varies by provider:

**Self-hosted clusters (using JWKS)**:
- Issuer: `https://kubernetes.default.svc.cluster.local`
- Public JWKS endpoint required

**Google Kubernetes Engine (GKE)**:
- Issuer: `https://container.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME`

**Amazon EKS**:
- Issuer: `https://oidc.eks.REGION.amazonaws.com/id/CLUSTER_ID`

**Azure AKS**:
- Issuer: `https://oidc.azure.com/TENANT_ID/`

For this guide, we'll use a generic self-hosted cluster example. Adjust the issuer URL based on your cluster provider.

To find your cluster's issuer URL:

```shell
kubectl get --raw /.well-known/openid-configuration | jq -r '.issuer'
```

## Step 2 — Create a Service Account

Create a dedicated Kubernetes service account for the workload that will access GitHub:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: github-automation
  namespace: default
```

Save this as `service-account.yaml` and apply it:

```shell
kubectl apply -f service-account.yaml
```

## Step 3 — Create the Trust Policy

Create a trust policy in your GitHub repository that allows your Kubernetes service account to obtain tokens.

Create `.github/chainguard/k8s-automation.sts.yaml`:

```yaml
issuer: https://kubernetes.default.svc.cluster.local
subject: system:serviceaccount:default:github-automation

permissions:
  contents: read
  issues: write
  pull_requests: write
```

This policy:
- Trusts tokens from your Kubernetes cluster's OIDC issuer
- Validates the subject matches the service account `github-automation` in the `default` namespace
- Grants permissions to read contents and manage issues and pull requests

The subject format for Kubernetes service accounts is:
```
system:serviceaccount:NAMESPACE:SERVICE_ACCOUNT_NAME
```

Commit and push the trust policy:

```shell
git add .github/chainguard/k8s-automation.sts.yaml
git commit -m "Add octo-sts trust policy for Kubernetes"
git push origin main
```

## Step 4 — Create a Pod with Token Projection

Create a pod that projects the service account token with the GitHub repository as the audience:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: github-automation
  namespace: default
spec:
  serviceAccountName: github-automation
  containers:
  - name: automation
    image: cgr.dev/chainguard/wolfi-base:latest
    command: ["/bin/sh"]
    args:
      - -c
      - |
        apk add curl jq gh

        # Read the projected service account token
        SA_TOKEN=$(cat /var/run/secrets/tokens/github-token)

        # Exchange with Octo STS
        RESPONSE=$(curl -s -H "Authorization: Bearer $SA_TOKEN" \
          "https://octo-sts.dev/sts/exchange?scope=${GITHUB_REPO}&identity=k8s-automation")

        # Extract GitHub token
        GITHUB_TOKEN=$(echo "$RESPONSE" | jq -r '.access_token')

        # Use the token to interact with GitHub
        export GITHUB_TOKEN
        gh repo view ${GITHUB_REPO}

        # Keep pod running for inspection
        sleep 3600
    env:
    - name: GITHUB_REPO
      value: "YOUR-ORG/YOUR-REPO"
    volumeMounts:
    - name: github-token
      mountPath: /var/run/secrets/tokens
      readOnly: true
  volumes:
  - name: github-token
    projected:
      sources:
      - serviceAccountToken:
          path: github-token
          expirationSeconds: 3600
          audience: https://github.com/YOUR-ORG/YOUR-REPO
```

Key configuration details:

- **serviceAccountName**: Uses the `github-automation` service account
- **volumes.projected.serviceAccountToken**: Projects a service account token
- **audience**: Set to the GitHub repository URL (important for validation)
- **expirationSeconds**: Token lifetime (3600 seconds = 1 hour)
- **volumeMounts**: Makes the token available at `/var/run/secrets/tokens/github-token`

Replace `YOUR-ORG/YOUR-REPO` with your actual organization and repository.

Save as `pod.yaml` and apply:

```shell
kubectl apply -f pod.yaml
```

## Step 5 — Verify the Integration

Check the pod logs to verify successful token exchange:

```shell
kubectl logs github-automation
```

You should see output from the `gh repo view` command, indicating the token was successfully exchanged and used.

To inspect the OIDC token contents (for debugging):

```shell
kubectl exec -it github-automation -- sh
cat /var/run/secrets/tokens/github-token | cut -d'.' -f2 | base64 -d | jq
```

This decodes the JWT token and shows the claims, including the issuer, subject, and audience.

## Use Case: GitOps Controller

A common use case is a controller that reads from a Git repository, applies changes to Kubernetes, and can write back status or updates.

### GitOps Trust Policy

Create `.github/chainguard/gitops.sts.yaml`:

```yaml
issuer: https://kubernetes.default.svc.cluster.local
subject: system:serviceaccount:gitops-system:controller

permissions:
  contents: write
  statuses: write
```

### GitOps Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: gitops-controller
  namespace: gitops-system
spec:
  replicas: 1
  selector:
    matchLabels:
      app: gitops-controller
  template:
    metadata:
      labels:
        app: gitops-controller
    spec:
      serviceAccountName: controller
      containers:
      - name: controller
        image: YOUR-GITOPS-CONTROLLER-IMAGE
        env:
        - name: GITHUB_REPO
          value: "YOUR-ORG/YOUR-REPO"
        - name: OCTO_STS_IDENTITY
          value: "gitops"
        volumeMounts:
        - name: github-token
          mountPath: /var/run/secrets/tokens
          readOnly: true
      volumes:
      - name: github-token
        projected:
          sources:
          - serviceAccountToken:
              path: github-token
              expirationSeconds: 3600
              audience: https://github.com/YOUR-ORG/YOUR-REPO
```

The controller application would:
1. Read the projected token from `/var/run/secrets/tokens/github-token`
2. Exchange it with Octo STS for a GitHub token
3. Use the GitHub token to clone repositories and push status updates
4. Automatically refresh tokens before expiration

## Use Case: CI/CD Pipeline Trigger

Use Kubernetes CronJobs to trigger CI/CD pipelines by creating pull requests or updating files:

### Pipeline Trust Policy

Create `.github/chainguard/pipeline.sts.yaml`:

```yaml
issuer: https://kubernetes.default.svc.cluster.local
subject: system:serviceaccount:pipeline:trigger

permissions:
  contents: write
  pull_requests: write
```

### CronJob Configuration

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: pipeline-trigger
  namespace: pipeline
spec:
  schedule: "0 2 * * *"  # Run at 2 AM daily
  jobTemplate:
    spec:
      template:
        spec:
          serviceAccountName: trigger
          restartPolicy: OnFailure
          containers:
          - name: trigger
            image: cgr.dev/chainguard/wolfi-base:latest
            command:
            - /bin/sh
            - -c
            - |
              apk add curl jq gh git

              # Get Kubernetes token
              SA_TOKEN=$(cat /var/run/secrets/tokens/github-token)

              # Exchange for GitHub token
              RESPONSE=$(curl -s -H "Authorization: Bearer $SA_TOKEN" \
                "https://octo-sts.dev/sts/exchange?scope=${GITHUB_REPO}&identity=pipeline")
              GITHUB_TOKEN=$(echo "$RESPONSE" | jq -r '.access_token')

              # Clone repo and create update
              export GITHUB_TOKEN
              gh repo clone ${GITHUB_REPO} repo
              cd repo

              # Make changes
              echo "Updated at $(date)" >> pipeline-status.txt

              # Commit and create PR
              git checkout -b update-$(date +%Y%m%d)
              git add pipeline-status.txt
              git commit -m "Automated pipeline update"
              git push origin update-$(date +%Y%m%d)

              gh pr create --title "Automated Update" \
                --body "Automated update from Kubernetes pipeline"
            env:
            - name: GITHUB_REPO
              value: "YOUR-ORG/YOUR-REPO"
            volumeMounts:
            - name: github-token
              mountPath: /var/run/secrets/tokens
          volumes:
          - name: github-token
            projected:
              sources:
              - serviceAccountToken:
                  path: github-token
                  expirationSeconds: 3600
                  audience: https://github.com/YOUR-ORG/YOUR-REPO
```

## Pattern: Using Pattern Matching for Multiple Namespaces

To allow service accounts across multiple namespaces to use the same trust policy:

```yaml
issuer: https://kubernetes.default.svc.cluster.local
subject_pattern: "system:serviceaccount:.*:github-automation"

permissions:
  contents: read
```

This allows any service account named `github-automation` in any namespace to obtain tokens.

## Pattern: Custom Claims for Advanced Validation

Some Kubernetes distributions support custom claims in service account tokens. You can validate these in trust policies:

```yaml
issuer: https://kubernetes.default.svc.cluster.local
subject: system:serviceaccount:default:github-automation
claim_pattern:
  kubernetes.io/namespace: "production-.*"

permissions:
  contents: write
```

This would only grant tokens to pods running in namespaces starting with `production-`.

## Security Best Practices

**Use dedicated service accounts**: Create separate service accounts for different workloads, each with its own trust policy.

**Set appropriate token expiration**: Balance security (shorter is better) with operational needs (avoid frequent refreshes causing API rate limits).

**Implement RBAC in Kubernetes**: Restrict which users and workloads can create pods with specific service accounts.

**Monitor token usage**: Log token exchanges and GitHub API calls to detect anomalous behavior.

**Use namespace isolation**: Run sensitive workloads in dedicated namespaces with network policies.

**Rotate on compromise**: If a service account is compromised, delete the trust policy immediately to revoke access.

## Cloud-Specific Configurations

### Google Kubernetes Engine (GKE)

GKE workload identity provides OIDC tokens automatically. Configure the trust policy:

```yaml
issuer: https://container.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME
subject: system:serviceaccount:NAMESPACE:SERVICE_ACCOUNT_NAME

permissions:
  contents: read
```

### Amazon EKS

EKS provides an OIDC identity provider. Find your issuer:

```shell
aws eks describe-cluster --name CLUSTER_NAME --query "cluster.identity.oidc.issuer" --output text
```

Trust policy:

```yaml
issuer: https://oidc.eks.REGION.amazonaws.com/id/CLUSTER_ID
subject: system:serviceaccount:NAMESPACE:SERVICE_ACCOUNT_NAME

permissions:
  contents: read
```

### Azure AKS

AKS provides Azure AD-based workload identity. Configure federation first, then use:

```yaml
issuer: https://oidc.azure.com/TENANT_ID/
subject: system:serviceaccount:NAMESPACE:SERVICE_ACCOUNT_NAME

permissions:
  contents: read
```

## Troubleshooting

### Token exchange fails with invalid_token

Check that:
- The service account token is being projected correctly (`kubectl exec` into pod and verify token exists)
- The audience in the projected token matches the GitHub repository
- The token hasn't expired

### Trust policy validation fails

Verify:
- The issuer in the trust policy matches your cluster's OIDC issuer exactly
- The subject format is correct: `system:serviceaccount:NAMESPACE:SA_NAME`
- The trust policy file is committed to the correct path in the repository

### Cannot access OIDC issuer endpoint

If octo-sts cannot reach your cluster's OIDC endpoint:
- Ensure the OIDC endpoint is publicly accessible (required for octo-sts to validate tokens)
- Check firewall rules and network policies
- For private clusters, consider using a public OIDC discovery URL

## Next Steps

- [Using Octo STS with Cloud Providers](/open-source/octo-sts/how-to-use-octo-sts-with-cloud-providers/) - Integrate with AWS, GCP, and Azure workloads
- [Trust Policy Reference](/open-source/octo-sts/trust-policy-reference/) - Advanced trust policy patterns
- [FAQ](/open-source/octo-sts/faq/) - Common questions and solutions
