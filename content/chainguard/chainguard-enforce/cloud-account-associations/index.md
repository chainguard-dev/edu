---
title: "How to Set Up Chainguard Enforce Cloud Account Associations"
linkTitle: "Cloud Account Associations"
aliases:
- /chainguard/chainguard-enforce/chainguard-enforce-kubernetes/cloud-account-associations/
type: "article"
description: "How to bind Chainguard Enforce to your cloud provider"
date: 2022-09-02T15:56:52-07:00
lastmod: 2023-11-29T15:22:20+01:00
draft: false
tags: ["Enforce", "Product", "Procedural"]
images: []
menu:
  docs:
    parent: "chainguard-enforce"
weight: 030
toc: true
---

> _This documentation is related to Chainguard Enforce. You can request access to the product by selecting **Chainguard Enforce** on the [inquiry form](https://www.chainguard.dev/contact?utm_source=docs)._


Chainguard Enforce for Kubernetes allows you to associate a cloud provider account with an Enforce IAM group. Cloud account association allows the Chainguard Enforce platform to access cloud resources on your behalf to enable several features, including:

- Verifying policies against containers hosted in private cloud container registries
- Verifying signatures created by cloud key management systems (KMS)

Support for cloud account associations is currently limited to Google Cloud Platform (GCP) and Amazon Web Services (AWS), but support for more platforms is planned.


## How Cloud Account Associations Work

Cloud account associations do not require you to provide the Chainguard Enforce platform with any long-lived access credentials to your cloud provider. Instead, cloud account association leverages the Enforce identity provider (https://issuer.enforce.dev) to allow Enforce services to role-bind to your cloud provider’s IAM system.

When you set up a cloud account association with Chainguard Enforce, it creates a number of IAM resources within your cloud account. On AWS, these are known as "Roles", while GCP refers to them as "Service Accounts."

Although the exact permissions between these profiles differ slightly between both cloud providers, they perform generally the same functions on GCP and AWS.

* `chainguard-canary` — used to test whether the cloud account association is working correctly. This profile has no permissions, as it only functions as an endpoint for testing
* `chainguard-discovery` — allows Enforce to find and list resources running within your cloud account, thereby enabling [Chainguard Enforce's Discovery feature](/chainguard/chainguard-enforce/chainguard-enforce-discovery-onboarding/)
* `chainguard-ingester` — has read-only access to SBOMs, allowing Enforce to download and ingest them as necessary
* `chainguard-enforce-signer` — allows Chainguard to perform [Enforce Signing](/chainguard/chainguard-enforce/chainguard-enforce-signing/chainguard-enforce-signing-faqs/)
* `chainguard-cosigned` — provides access to the open source SigStore policy controller, allowing Enforce to verify container attestations and signatures

A complete table of the IAM resources that Enforce creates is listed at the end of this page in the [Additional IAM Resources section](#additional-iam-resources).

## Setting up a Cloud Account Association for AWS

To configure (or upgrade) a cloud account association with AWS, start by setting up the association in Chainguard Enforce using `chainctl`.

First, associate the ID of the relevant Enforce group and the AWS account ID to variables for later use. You can find the IAM group ID by running `chainctl iam groups ls -o table`.

```sh
export ENFORCE_GROUP_ID="<<uidp of target Enforce IAM group>>"
export AWS_ACCOUNT_ID="12 digit AWS account ID to connect to"
```

Then, run the `chainctl` command to begin setting up the AWS account with the Enforce group.

```sh
chainctl iam account-associations set aws $ENFORCE_GROUP_ID --account $AWS_ACCOUNT_ID
```

Next, configure your AWS account to allow access from Enforce to specific AWS IAM roles. We provide a Terraform module to automate this setup. Using the same group and AWS account, for instance, our Terraform file will be written like this:

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

Once your AWS account is configured, you can check that the account association is configured correctly:

```sh
chainctl iam groups check-aws $ENFORCE_GROUP_ID
```

You’ll receive output that the configuration was successful.

```sh
2023/01/24 20:17:09 AWS role impersonation was successful!
```

More documentation and examples are available in the [module source repository](https://github.com/chainguard-dev/terraform-aws-chainguard-account-association).

## Setting up a Cloud Account Association for GCP

To configure (or upgrade) a cloud account association with GCP, first store the ID of the relevant Enforce group, the GCP account ID, and the GCP project number into variables for later use.

You can find the IAM group ID (UIDP) by running `chainctl iam groups ls -o table`. To find your GCP project ID and project number, open a web browser window and navigate to [https://console.cloud.google.com/welcome](https://console.cloud.google.com/welcome). Ensure you are in your preferred project from the dropdown in the nav bar, and note your **Project ID** (which should be a string of characters), and your **Project number** (which should be a string of numbers only).

```
export ENFORCE_GROUP_ID="UIDP of target Enforce IAM group"
export PROJECT_ID="GCP project ID"
export PROJECT_NUMBER="GCP project number"
```

Next, set up the association in Chainguard Enforce using `chainctl`.

```sh
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

You will be asked for confirmation during this process. If you are satisfied with the description you receive in the output, type `yes` to confirm.

It may take a few minutes for changes to propagate.

If you experience an error message when running the Terraform commands above, you may need to authenticate from the terminal to GCP with the following `gcloud` command.

```sh
gcloud auth application-default login
```

Once your GCP project is configured you can check that the account association is configured correctly:

```sh
chainctl iam groups check-gcp $ENFORCE_GROUP_ID
```

You’ll receive output that the configuration was successful.

```sh
2023/01/24 20:17:09 GCP role impersonation was successful!
```

More documentation and examples are available in the [module source repository](https://github.com/chainguard-dev/terraform-google-chainguard-account-association).


## Setting up Cloud Account Associations through the Enforce Console

You can also set up cloud account associations through the Chainguard Enforce Console.

After logging into the Console, navigate to the **Settings** tab. There, you will find a table listing  of all your Chainguard Enforce IAM groups. The rightmost columns are named **GCP** and **AWS**. If you haven't associated one of the listed groups with a GCP or AWS account, an "edit" icon will appear in these columns for the given row.

![Screenshot showing an example "Settings" tab, including a table with four groups. No group has yet been associated with a cloud account.](settings-grp-selection.png)

To associate a group with a cloud account, find the group you want to associate and click on the pencil-shaped edit icon for the cloud of your choice. A modal window will appear from the right with next steps, which differ depending on the cloud provider you selected.


### Setting up an AWS Cloud Account Association through the Console

If you clicked the edit icon for AWS, the modal window will contain a **Launch Stack** button.

![Screenshot of the AWS cloud account association modal window. It shows the window's helper text followed by the "Launch Stack" button. Below the button is the "Account ID" field with "your_account_id_here" entered as an example. At the bottom are the "Configure" and "Back" buttons.](aws.png)

Click this button, which will open an OpenID Connect login flow.

After completing this login flow, navigate back to the modal window in the Chainguard Enforce Console. Below the **Launch Stack** button is an empty field labeled **Account ID**. Within that field, enter the twelve-digit identification number of the AWS account you want to associate with Enforce.

After entering the account number, click the **Configure** button to finish associating your AWS account with Chainguard Enforce.


### Setting up a GCP Cloud Account Association through the Console

If you clicked the edit icon for GCP, the modal window will outline a four-step process to set up a cloud account association.

#### Authentication

First, the Console will ask you to authenticate to GCP. Click the **Authenticate** button, which will open an OpenID Connect login flow. Select the GCP account you want to associate with your Chainguard Enforce IAM group. Following that, Chainguard will be able to create Cloud resources on your behalf.


#### Select a Project

In the second step, a dropdown menu will appear with all the projects available for you to choose. Select the project you want to associate with your Chainguard Enforce group and click **Continue**.

![Screenshot showing Step 2 of the GCP cloud account association process. There is a dropdown menu labeled "Project" with no items selected yet.](gcp_step2.png)

#### Configure Workload Identity Federation

After selecting a project, the next step is to configure workload identity federation. Rather than supplying a service account key — which would provide Chainguard Enforce with unnecessarily broad permissions — workload identity federation allows Enforce to impersonate service accounts living in your Cloud environment.

If this is your first time setting up a cloud account association for this project you will need to explicitly authorize the creation of three resources:

* IAM Service Account Credentials API
* Workload Identity
* Workload Identity Provider

![Screenshot showing Step 3 of the GCP cloud account association process. This picture shows the three workload identity federation resources in a "Not Ready" state. There is a large "Incomplete" warning along with a "Configure" button above the table.](gcp_step3.png)

Click the **Configure** button to set up these resources. Once all of them show a **Ready** status, click the **Continue** button.

#### Configure Service Accounts

Lastly, you need to configure a set of service accounts which will connect with Chainguard, allowing Enforce to perform certain limited functions on your project's resources.

Again, if you haven't already set up the required service accounts on your chosen project then you must click the **Configure** button to do so.

![Screenshot showing Step 4 of the GCP cloud account association process. This picture shows all six service account profiles are in a "Not Ready" state. There is a large "Incomplete" warning along with a "Configure" button above the table.](gcp_step4.png)

Once each of the service accounts are in a **Ready** state, click the **Done** button to finish setting up your cloud account association.


## Removing Cloud Account Associations

`chainctl` comes with a few handy subcommands you can use to remove an account association that you've already created. To remove a GCP account association, run the `remove-gcp` subcommand, as in the following example.

```sh
chainctl iam groups remove-gcp
```

To remove an AWS account association, run the `remove-aws` subcommand instead.

```sh
chainctl iam groups remove-aws
```

After running either of these examples, `chainctl` will prompt you to select the Chainguard Enforce group whose association you'd like to remove. After selecting the group, `chainctl` will immediately remove the association.

> Note: As of this writing, it is not possible to remove cloud account associations through the Chainguard Enforce Console. Also note that using `chainctl` to remove account associations will not remove any AWS IAM roles, GCP service accounts, or workload identity federation settings from your cloud provider.


## Learn More

After setting up a cloud account association, you can use Chainguard Enforce's [Discovery feature](/chainguard/chainguard-enforce/chainguard-enforce-discovery-onboarding/) to discover various containerized workloads within your project.

## Additional IAM Resources

In addition to the IAM roles or service accounts that Enforce creates for account associations, it also enables and requires the following resources:

|Provider|Resource Type|Display Name|
|--------|-------------|------------|
|Google  |serviceusage.Service|storage-component.googleapis.com|
|Google  |iam.Role     |Custom Role Chainguard Signer CA |
|AWS     |AWS::IAM::OIDCProvider | ChainguardIDP |

You can examine the resources that Enforce creates using the `gcloud` or `aws` command line tools depending on your cloud provider.

### Google IAM Role

Enforce creates an additional IAM role that allows listing certificates from a CA. You can examine the role with the following command:

```
gcloud iam roles list --project <your project name>
```
```
---
description: Chainguard signer role to list certificates from a CA
etag: BwX4lw5KpDY=
name: projects/<your project name>/roles/chainguardSignerCA
title: Custom Role Chainguard Signer CA
```

### Google Workload Identity Pool

Since Enforce uses OIDC for authentication, it relies on Workload Identity Federation to generate short-lived tokens. You can examine the identity pool, and the provider that Enforce creates with the following commands:

```
 gcloud iam workload-identity-pools list \
    --location=global --project <your project name>
 ```

 You'll receive the following output:

 ```
---
description: Identity pool for Chainguard impersonation.
displayName: Chainguard Pool
name: projects/<your project number>/locations/global/workloadIdentityPools/chainguard-pool
state: ACTIVE
```

### Google Workload Identity Pool Provider

To inspect the Workload Identity Pool Provider that Enforce creates, use the following command:

```
gcloud iam workload-identity-pools providers list \
    --location=global --project <your project name> \
    --workload-identity-pool=projects/<your project number>/locations/global/workloadIdentityPools/chainguard-pool
```

You will receive output like the following:

```
---
attributeMapping:
  attribute.sub: assertion.sub
  google.subject: assertion.sub
description: This is the provider for impersonation by the https://issuer.enforce.dev
  Chainguard environment's issuer for https://issuer.enforce.dev.
displayName: chainguard-provider
name: projects/<your project number>/locations/global/workloadIdentityPools/chainguard-pool/providers/chainguard-provider
oidc:
  allowedAudiences:
  - google
  issuerUri: https://issuer.enforce.dev
state: ACTIVE
```

### Google Service Accounts

As noted in the beginning of this guide, Enforce creates a number of service accounts in your Google project. You can list the accounts with the following command:

```
gcloud iam service-accounts list --project <your project name>
```

```
DISPLAY NAME  EMAIL                                                                     DISABLED
. . .
              chainguard-canary@<your project name>.iam.gserviceaccount.com          False
              chainguard-ingester@<your project name>.iam.gserviceaccount.com        False
              chainguard-cosigned@<your project name>.iam.gserviceaccount.com        False
              chainguard-discovery@<your project name>.iam.gserviceaccount.com       False
              chainguard-enforce-signer@<your project name>.iam.gserviceaccount.com  False
. . .
```

### AWS IAM Roles

You can list the IAM roles that Enforce creates using the following command:

```
aws iam list-roles | \
  jq -r '.Roles [] | select(.RoleName |test("chainguard")) | .RoleName'
```

You will receive output like the following:

```
chainguard-canary
chainguard-cosigned
chainguard-discovery
chainguard-enforce-signer
chainguard-ingester
```

You can then inspect each of the rules using the `aws iam get-role` command.
