---
title: "How to Use Octo STS with Cloud Providers"
linktitle: "Cloud Provider Integration"
type: "article"
lead: "Connect workloads running in AWS, Google Cloud, and Azure to GitHub repositories using native cloud identity and OIDC federation"
description: "Learn about Octo STS for GitHub API access, enabling secure cloud-to-GitHub integrations without storing credentials"
date: 2025-12-22T15:04:05+01:00
lastmod: 2025-12-22T15:04:05+01:00
tags: ["octo-sts", "AWS", "GCP", "Azure", "Cloud", "Procedural"]
draft: false
images: []
menu:
  docs:
    parent: "octo-sts"
weight: 40
toc: true
---

Cloud workloads often need to interact with GitHub repositories for deployment automation, infrastructure updates, or operational tasks. Instead of storing GitHub Personal Access Tokens in cloud secret managers, you can use each cloud provider's native OIDC identity with Chainguard's Octo STS to obtain short-lived GitHub tokens.

This guide demonstrates how to configure workloads in AWS, Google Cloud Platform (GCP), and Microsoft Azure to use octo-sts.

## Prerequisites

Before you begin, ensure you have:

- The octo-sts GitHub App installed on your target repository or organization
- Access to create and configure workloads in your cloud provider
- Basic understanding of your cloud provider's identity and access management
- Familiarity with OIDC concepts

## AWS Integration

AWS services can obtain OIDC tokens through AWS IAM roles and the Security Token Service (STS). Common use cases include Lambda functions, ECS tasks, and EC2 instances accessing GitHub.

### Step 1 — Configure IAM for OIDC

AWS doesn't directly provide OIDC tokens in the same way as GCP. However, you can use AWS IAM to assume roles that include OIDC claims, or use AWS services that support OIDC directly.

For this example, we'll configure an AWS Lambda function to use octo-sts.

### Step 2 — Create IAM Role with OIDC Provider

First, set up an OIDC identity provider in AWS IAM:

1. Go to **IAM** → **Identity providers** → **Add provider**
2. Select **OpenID Connect**
3. Provider URL: Use a public OIDC endpoint (if using GitHub Actions from AWS, you might already have `https://token.actions.githubusercontent.com`)
4. Audience: `sts.amazonaws.com`

Create an IAM role that can be assumed with OIDC tokens:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::ACCOUNT_ID:oidc-provider/token.actions.githubusercontent.com"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "token.actions.githubusercontent.com:sub": "repo:YOUR-ORG/YOUR-REPO:ref:refs/heads/main",
          "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
        }
      }
    }
  ]
}
```

### Step 3 — Using Google OIDC Tokens from AWS

A more practical approach is to use Google's OIDC tokens (which are well-supported) from workloads running in AWS:

Create a trust policy in GitHub at `.github/chainguard/aws-lambda.sts.yaml`:

```yaml
issuer: https://accounts.google.com
subject_pattern: "[0-9]+"
claim_pattern:
  email: ".*@YOUR-DOMAIN.com"

permissions:
  contents: read
  issues: write
```

From an AWS Lambda function with Google service account credentials:

```python
import json
import requests
import google.auth
from google.auth.transport.requests import Request

def lambda_handler(event, context):
    # Get Google OIDC token
    credentials, project = google.auth.default()
    credentials.refresh(Request())

    # Request OIDC token with GitHub audience
    oidc_token = credentials.id_token

    # Exchange with Octo STS
    response = requests.get(
        "https://octo-sts.dev/sts/exchange",
        params={
            "scope": "YOUR-ORG/YOUR-REPO",
            "identity": "aws-lambda"
        },
        headers={"Authorization": f"Bearer {oidc_token}"}
    )

    github_token = response.json()["access_token"]

    # Use GitHub token
    repo_response = requests.get(
        "https://api.github.com/repos/YOUR-ORG/YOUR-REPO",
        headers={"Authorization": f"Bearer {github_token}"}
    )

    return {
        "statusCode": 200,
        "body": json.dumps(repo_response.json())
    }
```

### AWS-Specific Use Case: ECS Task

For ECS tasks, configure the task definition to use a service account with OIDC:

```json
{
  "family": "github-automation",
  "taskRoleArn": "arn:aws:iam::ACCOUNT_ID:role/github-automation-role",
  "containerDefinitions": [
    {
      "name": "automation",
      "image": "YOUR-IMAGE",
      "environment": [
        {
          "name": "GITHUB_REPO",
          "value": "YOUR-ORG/YOUR-REPO"
        }
      ]
    }
  ]
}
```

The container can then use the AWS SDK to obtain credentials and exchange them appropriately.

## Google Cloud Platform (GCP) Integration

GCP provides robust OIDC support through service accounts. Workloads in Cloud Run, Cloud Functions, GCE, and GKE can easily obtain OIDC tokens.

### Step 1 — Create a Service Account

Create a dedicated GCP service account for GitHub automation:

```shell
gcloud iam service-accounts create github-automation \
  --display-name="GitHub Automation" \
  --description="Service account for GitHub API access via octo-sts"
```

### Step 2 — Create Trust Policy

Create `.github/chainguard/gcp-automation.sts.yaml`:

```yaml
issuer: https://accounts.google.com
subject: "SERVICE_ACCOUNT_UNIQUE_ID"

permissions:
  contents: read
  issues: write
  pull_requests: write
```

To find your service account's unique ID (numeric subject):

```shell
gcloud iam service-accounts describe github-automation@PROJECT_ID.iam.gserviceaccount.com \
  --format="value(uniqueId)"
```

Alternatively, use pattern matching for the email:

```yaml
issuer: https://accounts.google.com
claim_pattern:
  email: "github-automation@PROJECT_ID.iam.gserviceaccount.com"

permissions:
  contents: read
  issues: write
  pull_requests: write
```

Commit and push the trust policy.

### Step 3 — Use from Cloud Run

Deploy a Cloud Run service that exchanges tokens with Octo STS:

```python
# main.py
import os
import requests
from google.auth.transport import requests as google_requests
from google.oauth2 import id_token
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/github-status')
def github_status():
    # Get OIDC token for the current service account
    target_audience = "https://github.com/YOUR-ORG/YOUR-REPO"
    oidc_token = id_token.fetch_id_token(google_requests.Request(), target_audience)

    # Exchange with Octo STS
    response = requests.get(
        "https://octo-sts.dev/sts/exchange",
        params={
            "scope": "YOUR-ORG/YOUR-REPO",
            "identity": "gcp-automation"
        },
        headers={"Authorization": f"Bearer {oidc_token}"}
    )

    github_token = response.json()["access_token"]

    # Use GitHub token
    repo_response = requests.get(
        "https://api.github.com/repos/YOUR-ORG/YOUR-REPO",
        headers={"Authorization": f"Bearer {github_token}"}
    )

    return jsonify(repo_response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
```

Deploy to Cloud Run:

```shell
gcloud run deploy github-automation \
  --source . \
  --service-account=github-automation@PROJECT_ID.iam.gserviceaccount.com \
  --allow-unauthenticated \
  --region=us-central1
```

### Step 4 — Use from Cloud Functions

For Cloud Functions (2nd gen):

```python
# main.py
import functions_framework
import requests
from google.auth.transport import requests as google_requests
from google.oauth2 import id_token

@functions_framework.http
def github_webhook(request):
    # Get OIDC token
    target_audience = "https://github.com/YOUR-ORG/YOUR-REPO"
    oidc_token = id_token.fetch_id_token(google_requests.Request(), target_audience)

    # Exchange with Octo STS
    sts_response = requests.get(
        "https://octo-sts.dev/sts/exchange",
        params={
            "scope": "YOUR-ORG/YOUR-REPO",
            "identity": "gcp-automation"
        },
        headers={"Authorization": f"Bearer {oidc_token}"}
    )

    github_token = sts_response.json()["access_token"]

    # Create an issue based on webhook payload
    issue_data = {
        "title": "Automated Issue from GCP",
        "body": f"Function triggered at {request.get_json()}"
    }

    issue_response = requests.post(
        "https://api.github.com/repos/YOUR-ORG/YOUR-REPO/issues",
        json=issue_data,
        headers={"Authorization": f"Bearer {github_token}"}
    )

    return {"status": "created", "issue": issue_response.json()}, 201
```

Deploy:

```shell
gcloud functions deploy github-webhook \
  --gen2 \
  --runtime=python311 \
  --trigger-http \
  --service-account=github-automation@PROJECT_ID.iam.gserviceaccount.com \
  --allow-unauthenticated \
  --region=us-central1
```

### GCP Use Case: Cloud Scheduler + Cloud Functions

Automate periodic GitHub operations:

```shell
# Create a scheduled job that triggers a Cloud Function
gcloud scheduler jobs create http github-daily-sync \
  --schedule="0 2 * * *" \
  --uri="https://REGION-PROJECT_ID.cloudfunctions.net/github-webhook" \
  --http-method=POST \
  --oidc-service-account-email=github-automation@PROJECT_ID.iam.gserviceaccount.com
```

## Microsoft Azure Integration

Azure provides managed identities that can be used to obtain OIDC tokens for federation with Octo STS.

### Step 1 — Create Managed Identity

Create a user-assigned managed identity:

```shell
az identity create \
  --name github-automation \
  --resource-group YOUR-RESOURCE-GROUP
```

Note the `clientId` and `principalId` from the output.

### Step 2 — Create Trust Policy

Azure managed identities use Azure AD as the OIDC issuer. Create `.github/chainguard/azure-automation.sts.yaml`:

```yaml
issuer: https://login.microsoftonline.com/TENANT_ID/v2.0
subject: PRINCIPAL_ID

permissions:
  contents: read
  issues: write
```

Replace `TENANT_ID` with your Azure AD tenant ID and `PRINCIPAL_ID` with the managed identity's principal ID.

Commit and push the trust policy.

### Step 3 — Use from Azure Function

Create an Azure Function that uses the managed identity:

```python
# __init__.py
import os
import logging
import requests
import azure.functions as func
from azure.identity import ManagedIdentityCredential

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('GitHub automation function triggered')

    # Get OIDC token using managed identity
    credential = ManagedIdentityCredential()
    token = credential.get_token("https://github.com/YOUR-ORG/YOUR-REPO")
    oidc_token = token.token

    # Exchange with Octo STS
    response = requests.get(
        "https://octo-sts.dev/sts/exchange",
        params={
            "scope": "YOUR-ORG/YOUR-REPO",
            "identity": "azure-automation"
        },
        headers={"Authorization": f"Bearer {oidc_token}"}
    )

    github_token = response.json()["access_token"]

    # Use GitHub token
    repo_response = requests.get(
        "https://api.github.com/repos/YOUR-ORG/YOUR-REPO",
        headers={"Authorization": f"Bearer {github_token}"}
    )

    return func.HttpResponse(
        repo_response.text,
        status_code=200
    )
```

Deploy the function with the managed identity:

```shell
az functionapp identity assign \
  --name YOUR-FUNCTION-APP \
  --resource-group YOUR-RESOURCE-GROUP \
  --identities /subscriptions/SUBSCRIPTION_ID/resourcegroups/YOUR-RESOURCE-GROUP/providers/Microsoft.ManagedIdentity/userAssignedIdentities/github-automation
```

### Step 4 — Use from Azure Container Instances

Deploy a container with managed identity:

```shell
az container create \
  --name github-automation \
  --resource-group YOUR-RESOURCE-GROUP \
  --image YOUR-IMAGE \
  --assign-identity /subscriptions/SUBSCRIPTION_ID/resourcegroups/YOUR-RESOURCE-GROUP/providers/Microsoft.ManagedIdentity/userAssignedIdentities/github-automation \
  --environment-variables GITHUB_REPO=YOUR-ORG/YOUR-REPO
```

The container can use the Azure SDK to obtain OIDC tokens and exchange them with Octo STS.

### Azure Use Case: Logic Apps

Use Azure Logic Apps to trigger GitHub operations based on events:

1. Create a Logic App with managed identity
2. Add a custom HTTP action that:
   - Obtains an OIDC token using the managed identity
   - Exchanges it with Octo STS
   - Calls GitHub API with the resulting token

This enables event-driven GitHub automation from Azure services.

## Cross-Cloud Pattern: Using Google OIDC Everywhere

A practical pattern for multi-cloud environments is to use Google service accounts across all clouds, since Google provides excellent OIDC support:

1. Create a Google service account
2. Export service account keys
3. Store keys in AWS Secrets Manager, Azure Key Vault, etc.
4. Use Google's OIDC tokens from any cloud

Trust policy:

```yaml
issuer: https://accounts.google.com
claim_pattern:
  email: "automation@PROJECT_ID.iam.gserviceaccount.com"

permissions:
  contents: read
  issues: write
```

This provides consistent OIDC token handling across AWS, Azure, and on-premises environments.

## Security Best Practices

**Use cloud-native identity**: Prefer each cloud's native identity solution over exporting credentials when possible.

**Scope managed identities narrowly**: In Azure, assign managed identities only to the specific resources that need them.

**Monitor token exchanges**: Enable cloud logging to track when workloads obtain OIDC tokens and exchange them with Octo STS.

**Rotate on compromise**: If a cloud identity is compromised, delete the trust policy immediately and investigate.

**Use private endpoints**: Where possible, use private networking to ensure OIDC token requests don't traverse the public internet.

**Implement least privilege**: Grant only the minimum GitHub permissions required for each workload's specific task.

## Troubleshooting

### Token exchange fails with invalid_issuer

Verify:
- The issuer in your trust policy exactly matches the OIDC issuer from your cloud provider
- For GCP: Use `https://accounts.google.com`
- For Azure: Use `https://login.microsoftonline.com/TENANT_ID/v2.0`
- For AWS: Depends on your OIDC provider configuration

### Cannot obtain OIDC token from cloud service

Check that:
- The service account or managed identity exists and is correctly configured
- The workload has permission to impersonate the identity
- The cloud service supports OIDC token generation

### Subject mismatch errors

Ensure:
- For GCP: Use the numeric `uniqueId` as the subject, not the email
- For Azure: Use the managed identity's `principalId`
- For AWS: Subject format depends on your OIDC provider configuration

## Next Steps

- [Trust Policy Reference](/open-source/octo-sts/trust-policy-reference/) - Advanced trust policy patterns and claim validation
- [FAQ](/open-source/octo-sts/faq/) - Common questions and solutions
- [Using Octo STS with Kubernetes](/open-source/octo-sts/how-to-use-octo-sts-with-kubernetes/) - Integrate with Kubernetes workloads
