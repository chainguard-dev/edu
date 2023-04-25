---
title: "Create GitHub Issues from Enforce CloudEvents"
type: "article"
description: "Creating GitHub Issues from Enforce CloudEvents"
date: 2023-04-11T15:22:20+01:00
lastmod: 2023-04-11T15:22:20+01:00
draft: false
tags: ["Enforce", "Product", "CloudEvents"]
images: []
menu:
  docs:
    parent: "cloudevents"
weight: 10
toc: true
---

> _This documentation is related to Chainguard Enforce. You can request access to the product by selecting **Chainguard Enforce** on the [inquiry form](https://www.chainguard.dev/contact?utm_source=docs)._

Chainguard Enforce for Kubernetes can send CloudEvents as webhook requests that you can subscribe to and use to do things like generate alerts, create GitHub issues, post messages to Slack channels, and more. This tutorial is meant to serve as a companion to the [Enforce Events github-issue-opener](https://github.com/chainguard-dev/enforce-events/tree/main/github-issue-opener) example application. It will guide you through creating and deploying a Google Cloud Run service that will open new GitHub issues for any Enforce policy violation event.

You can also opt to run the example application elsewhere. As long as it is publicly accessible to the [Enforce CIDR network ranges](/chainguard/chainguard-enforce/reference/network-requirements/#cidr-ranges), you will be able to receive CloudEvents and create GitHub issues with the example application. If you opt to deploy the demo outside of Cloud Run, you can skip to the [Subscribing to Chainguard Enforce CloudEvents](#subscribing-to-chainguard-enforce-cloudevents) section, provided you know the publicly accessible URL to your deployed instance of the demo.

## Prerequisites

To follow along with this guide, it is assumed that you have a Kubernetes cluster with Chainguard Enforce enabled. If you need to set this up, follow our [Getting Started](/chainguard/chainguard-enforce/chainguard-enforce-user-onboarding/#step-3--prepare-kubernetes-cluster) guide to create a local [kind](https://kind.sigs.k8s.io/) cluster that you can use for experimentation.

You will also need:

* The [`gcloud` CLI](https://cloud.google.com/sdk/docs/install) and a Google Cloud account if you choose to run the application using Cloud Run.
* `terraform` to configure a Google Cloud service account, IAM permissions, and deploy the Cloud Run service. If you are running the application elsewhere, you can ignore this requirement.
* A [fine-grained GitHub Personal Access Token](https://github.com/settings/tokens?type=beta) to ensure the token is limited to the specific repository where you want to file issues. Also make sure that it only has `Read-only` Metadata permissions, and `Read and write` Issues permissions.
* `chainctl` in order to create a subscription webhook endpoint.
* An [Enforce or Sigstore policy](/chainguard/chainguard-enforce/policies/chainguard-enforce-policy-examples/) and a Kubernetes namespace that is configured with the `policy.sigstore.dev/include=true` label to use Enforce for admission control.

## Steps Overview

Deploying the demo application consists of the following steps:

1. Cloning the example repository
2. Running `terraform` to provision resources in your Google Cloud account
3. Creating a secret in your Google Cloud account to store your GitHub Personal Access Token
4. Deploying a pod that will violate a policy
5. Subscribing to Enforce CloudEvents
6. Configuring an Enforce policy that generates GitHub issues

## Cloning the Demo Application

To clone the demo application, `git clone` the [`enforce-events`](https://github.com/chainguard-dev/enforce-events) repository and move into the newly created directory using the following commands:

```shell
cd ~
git clone https://github.com/chainguard-dev/enforce-events.git
cd enforce-events/github-issue-opener/iac
```

Next you will run Terraform to deploy the demo application.

## Running Terraform

Inside the `iac` directory you will find a Terraform module that builds the demo application and configures your Google Cloud project settings.

Run the `terraform init` command to download all the required providers:

```shell
terraform init
```

```
Initializing provider plugins...
- Finding latest version of ko-build/ko...
- Finding latest version of hashicorp/google...
- Installing ko-build/ko v0.0.7...
- Installed ko-build/ko v0.0.7 (self-signed, key ID 36A8C1D1056CC508)
- Installing hashicorp/google v4.61.0...
- Installed hashicorp/google v4.61.0 (signed by HashiCorp)
. . .
```

Now you can generate an execution plan. You will need a few pieces of information to input as variables:

1. `group`: your Chainguard group ID. Use `chainctl iam groups describe <your group> -o json |jq -r '.id'` to retrieve it.

2. `project_id`: your Google Cloud project ID. Use the human readable name for the project as opposed to the numeric identifier.

3. `github_org`: a GitHub organization or username that hosts the repository where you will create issues.

4. `github_repo`: the GitHub repository inside the organization or user's account where you will create issues.

5. `labels`: a comma separated list of labels that you would like to apply to the generated GitHub issues.

Once you have all the information gathered, run the `terraform plan` command:

```shell
terraform plan \
  -var "github_org=<user or org>" \
  -var "github_repo=<repo name>" \
  -var "group=<chainguard group ID>" \
  -var "project_id=<gcloud project ID>" \
  -var "name=enforce-events" \
  -var "labels=enforce-events" \
  -out enforce-events.plan
```

You will receive output like the following showing Terraform's execution plan:

```
. . .
# google_cloud_run_service.gh-iss will be created
  + resource "google_cloud_run_service" "gh-iss" {
      + autogenerate_revision_name = false
      + id                         = (known after apply)
      + location                   = "<google location>"
      + name                       = "enforce-events-issue-opener"
      + project                    = "<google project>"
      + status                     = (known after apply)
. . .
To perform exactly these actions, run the following command to apply:
    terraform apply "enforce-events.plan"
```

Inspect the plan to ensure that the resources that Terraform will create are in line with your Google Cloud project's settings and IAM permissions. Once you are satisfied with the plan, apply it:

```shell
terraform apply enforce-events.plan
```

Terraform will run the module and you will receive output like the following:

```
google_secret_manager_secret.gh-pat: Creating...
google_service_account.gh-iss-opener: Creating...
. . .
Outputs:

secret-command = "echo -n YOUR GITHUB PAT | gcloud --project <google project> secrets versions add enforce-events-github-pat --data-file=-"
url = "https://enforce-events-issue-opener-ntfj7ezpja-uc.a.run.app"
```

Note down the `url` and the `secret-command`.

## Configuring Google Cloud with your GitHub Token

With the output from the `terraform apply` step, you can now run the `echo` command to configure Google Cloud with your GitHub personal access token.

Substitute your GitHub personal access token in place of the `<your github PAT>` string and run the following command:

```shell
echo -n <your github PAT> | gcloud --project <google project> secrets versions add enforce-events-github-pat --data-file=-
```

This configures your Google Cloud project with your token so that it is available to the demo application when it is invoked on Cloud Run.

### Subscribing to Chainguard Enforce CloudEvents

Now that the demo application is deployed, the next step is to register it as a CloudEvents receiver for the Enforce webhook.

Run the following `chainctl` command to create an Enforce webhook subscription:

```shell
chainctl events subscriptions create \
  --group <your chainguard group> \
  https://<url from terraform>
```

You will receive output showing the ID of the subscription and the webhook endpoint, like the following:

```
                    ID                   |             SINK
 ----------------------------------------+-----------------------------
  <chainguard group ID>/0dfbc3c8b89e0147 | https://<url from terraform>
  ```

Enforce will now send events to the application that is running on Cloud Run at the specified URL.

## Deploying a Pod That Will Violate a Policy

In this step you will create a Kubernetes deployment that uses an unsigned image. Run the following to deploy `nginx` into your cluster:

```shell
kubectl create deployment nginx --image=nginx
```

Now that you have a workload running, you can can add an Enforce policy, and the deployment will trigger a policy violation event, which in turn will create a GitHub issue.

## Configuring an Enforce Policy

Before you can open GitHub issues for policy violations, you will need to ensure that you have Enforce configured with a policy that you can test. Make sure you have a cluster registered with Enforce using the `chainctl clusters ls` command. If you do not, visit our [Getting Started with Enforce Guide](/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/chainguard-enforce-user-onboarding/#step-3--prepare-kubernetes-cluster) to create and register a cluster.

Once you have a cluster enrolled with Enforce, create the following policy from the Getting Started guide:

```
cat > sample-policy.yaml <<EOF
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
  - glob: "cgr.dev/chainguard/**"
  authorities:
  - keyless:
      url: https://fulcio.sigstore.dev
      identities:
        - issuerRegExp: ".*"
          subjectRegExp: ".*"
EOF
```

Apply it using `chainctl`:

```
chainctl policies apply \
  -f sample-policy.yaml --group=<your chainguard group>
```

Depending on your Kubernetes cluster, applying the policy may generate multiple GitHub issues. For example, if you are using `kind`, the control plane images are not signed and should create issues.

Once the policy is created, check the logs of your [Cloud Run deployment](https://console.cloud.google.com/logs/query;query=resource.type%3D%22cloud_run_revision%22%0Aresource.labels.service_name%3D%22enforce-events-issue-opener%22%0AtextPayload:%20%22Opened%20issue%22;timeRange=PT4H). You may need to edit the `service_name` portion of the URL if your service is called something different from `enforce-events-issue-opener`.

You should see log entries corresponding to new GitHub issues that the demo application created for you:

![Screenshot of logs in Google Log Explorer showing Opened issue entries](google-cloud-logs.png)

Now visit your GitHub project's page and look for the issues. A new issue for the sample policy should look like the following:

![Screenshot of a GitHub issue created using the demo application](github-issue.png)

## Learn More

Now that you've deployed and tested creating issues with the demo application, you can continue to develop it to create issues for other Enforce event types. See our [Chainguard Enforce Events](/chainguard/chainguard-enforce/reference/events/) page for a complete reference of event types that Enforce emits.

To see how to extend the demo application to check for other event types, see the [Slack Issue Opener](https://github.com/chainguard-dev/enforce-events/blob/main/slack-webhook) demo in the repository that you cloned at the beginning of this tutorial.

You can edit the Go code in the repository and deploy new versions of it as you add functionality using the same `terraform plan` and `terraform apply` commands that you ran earlier in this tutorial.
