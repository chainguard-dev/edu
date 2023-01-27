---
title: "How to Set Up Chainguard Enforce Cloud Account Associations"
type: "article"
description: "How to bind Chainguard Enforce to your cloud provider"
date: 2022-09-02T15:56:52-07:00
lastmod: 2023-01-19T15:56:52-07:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-enforce-kubernetes"
weight: 670
toc: true
---

> _This documentation is related to Chainguard Enforce. You can request access to the product by selecting **Chainguard Enforce for Kubernetes** on the [inquiry form](https://www.chainguard.dev/get-demo?utm_source=docs)._


Chainguard Enforce for Kubernetes allows you to associate a cloud provider
account with an Enforce IAM group. Cloud account association allows the
Chainguard Enforce platform to access cloud resources on your behalf to enable
several features, including:

- Verifying policies against containers hosted in private cloud container registries
- Verifying signatures created by cloud key management systems (KMS)
- Connecting cloud managed Kubernetes clusters without the need to run the Enforce agent (agentless)

Support for cloud account associations is currently limited to Google Cloud
Platform (GCP) and Amazon Web Services (AWS), but support for more platforms is
planned.

## How Cloud Account Associations Work

Cloud account associations do not require you to provide the Chainguard Enforce
platform with any long-lived access credentials to your cloud provider.
Instead, cloud account association leverages the Enforce identity provider
(https://issuer.enforce.dev) to allow Enforce services to role-bind to your
cloud provider’s IAM system.

## Setting up a Cloud Account Association for AWS

To configure (or upgrade) a cloud account association with AWS, start by setting up the
association in Chainguard Enforce using `chainctl`. First, associate the ID of
the relevant Enforce group and the AWS account ID to variables for later use.
You can find the IAM group ID by running `chainctl iam groups ls -o table`:

```sh
export ENFORCE_GROUP_ID="<<uidp of target Enforce IAM group>>"
export AWS_ACCOUNT_ID="12 digit AWS account ID to connect to"

chainctl iam group set-aws $ENFORCE_GROUP_ID --account $AWS_ACCOUNT_ID
```

Next, configure your AWS account to allow access from Enforce to specific AWS
IAM roles. We provide a Terraform module to automate this setup. Using the same
group and AWS account, for instance, our Terraform file will be written like
this:

```sh
cat  <<EOF > main.tf
provider "aws" {}

module "aws-impersonation" {
  source  = "chainguard-dev/chainguard-account-association/aws"

  enforce_group_ids = ["$ENFORCE_GROUP_ID"]
}

# While the above configures global IAM bindings, this module contains
# regional resources that let Chainguard Enforce monitor audit logs that
# let us discover infrastructure changes immediately.
#
# This module must be applied to each region containing resources you would like
# Chainguard Enforce to monitor in near real time.
module "aws-auditlogs" {
  # Note the // is semantic and tells terraform that auditlogs is a directory.
  source = "chainguard-dev/chainguard-account-association/aws//auditlogs"
}
EOF
```

Then, initiate and apply the module:

```sh
terraform init -upgrade
terraform plan
terraform apply
```

More documentation and examples are available in the [module source repository](https://github.com/chainguard-dev/terraform-aws-chainguard-account-association).

Once your AWS account is configured, you can check that the account association
is configured correctly:

```sh
chainctl iam groups check-aws $ENFORCE_GROUP_ID
```

You’ll receive output that the configuration was successful.

```sh
2022/09/01 11:26:47 AWS role impersonation was successful!
```

## Setting up a Cloud Account Association for GCP

To configure (or upgrade) a cloud account association with GCP, start by setting up the
association in Chainguard Enforce using `chainctl`. First, store the ID of the
relevant Enforce group, the GCP account ID, and the GCP project number into
variables for later use. You can find the IAM group ID by running `chainctl iam
groups ls -o table`:

```
export ENFORCE_GROUP_ID="UIDP of target Enforce IAM group"
export PROJECT_ID="GCP project ID"
export PROJECT_NUMBER="GCP project number"

chainctl iam group set-gcp $ENFORCE_GROUP_ID \
  --project-id $PROJECT_ID \
  --project-number $PROJECT_NUMBER
```

Next, configure your GCP project to allow access from Enforce to specific IAM roles. We provide a Terraform module to automate this setup. Using the same group and GCP project details, for instance, our Terraform file will be written like this:

```sh
cat  <<EOF > main.tf
provider "google" {
  project = "$PROJECT_ID"
}

provider "google-beta" {
  project = "$PROJECT_ID"
}

module "gcp-impersonation" {
  source  = "chainguard-dev/chainguard-account-association/google"

  enforce_group_ids  = ["$ENFORCE_GROUP_ID"]
  google_project_id = "$PROJECT_ID"
}
EOF
```

Then, initiate and apply the module:

```sh
terraform init -upgrade
terraform plan
terraform apply
```

More documentation and examples are available in the [module source repository](https://github.com/chainguard-dev/terraform-google-chainguard-account-association).

It may take a few minutes for changes to propagate.
Once your GCP project is configured you can check that the account association
is configured correctly:

```sh
chainctl iam groups check-gcp $ENFORCE_GROUP_ID
```

You’ll receive output that the configuration was successful.

```sh
2022/09/01 11:26:47 GCP role impersonation was successful!
```
