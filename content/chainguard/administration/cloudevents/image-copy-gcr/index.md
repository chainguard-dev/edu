---
title: "Mirror new Images to Google Artifact Registry with Chainguard CloudEvents"
linktitle: "Mirror Images to Artifact Registry"
type: "article"
description: "Instructional guide outlining how one can set up an application that will listen for push events on a private Chainguard Registry and mirror any new Chainguard Images to a GCP Artifact Registry."
date: 2024-06-03T15:22:20+01:00
lastmod: 2024-06-03T15:22:20+01:00
draft: false
tags: ["Product", "CloudEvents", "Procedural"]
images: []
menu:
   docs:
    parent: "cloudevents"
weight: 15
toc: true
---

Certain interactions with Chainguard resources will emit [CloudEvents](/chainguard/administration/cloudevents/events-reference/) that you or an application can subscribe to. This allows you to do things like receive alerts when a user downloads one or more of your organization's private Images or when a new Image gets added to your organization's registry.

This tutorial is meant to serve as a companion to the [Image Copy GCP](https://github.com/chainguard-dev/platform-examples/tree/main/image-copy-gcp) example application. It will guide you through setting up infrastructure to listen for `push` events on an organization's private registry and mirror any new Chainguard Images in the registry to a repository in a GCP Artifact Registry repository.


## Prerequisites

To follow along with this guide, it is assumed that you have the following set up and ready to use.

* A [verified Chainguard organization](/chainguard/administration/iam-organizations/verified-orgs/) with a private [Registry](/chainguard/chainguard-registry/overview/) and access to [Production Images](/chainguard/chainguard-images/overview/#production-and-developer-images).
* `chainctl`, the Chainguard command-line interface. You can install this by following our guide on [How to Install `chainctl`](/chainguard/administration/how-to-install-chainctl/).
* [`terraform`](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) to configure a Google Cloud service account, IAM permissions, and deploy the Cloud Run service.
* A Google Cloud account with a project running. The example application assumes that your project has the following APIs enabled:
    * [Artifact Registry API](https://cloud.google.com/artifact-registry/docs/reference/rest)
    * [Cloud Run Admin API](https://cloud.google.com/run/docs/reference/rest)
* The [`gcloud` CLI](https://cloud.google.com/sdk/docs/install) installed on your local machine. You'll need this to authenticate to Google Cloud over the command line.


## Setting up the Terraform configuration

You can find all the code associated with this sample application in our [Platform Examples](https://github.com/chainguard-dev/platform-examples/tree/main/image-copy-gcp) repository on GitHub. 

To set up the sample application, you can create a Terraform configuration file and apply it to set up the necessary resources. To begin, create a new directory to hold the configuration and navigate into it.

```sh
mkdir ~/gcp-example && cd $_
```

After navigating into the new directory you can begin creating a Terraform configuration named `main.tf`.

This configuration will consist of a single module. For the purposes of this example, we will call it `image-copy`. This module's `source` value will be the `iac` folder from the application code in the examples repository.

```
module "image-copy" {
  source = "github.com/chainguard-dev/platform-examples//image-copy-gcp/iac"
```

The next five lines configure a few variables that you will need to update to reflect your own setup.

* First, the configuration defines a `name` value. This will be used to prefix resources created by this sample application where possible.
* Next, it specifies the GCP project ID where certain resources will reside, including the container image for this application (along with mirrored images), the Cloud Run service hosting the application, and the Service Account that authorizes pushes to the Google Artifact Registry.
* Following that, the configuration specifies the Chainguard IAM organization from which we expect to receive events. This is used to authenticate that the Chainguard events are intended for you, and not another user. Images pushed to repositories under this organization will be mirrored to Artifact Registry.
    * If you don't know your organization's UIDP, you can retrieve it by running `chainctl iam organizations list -o table`.
* The next line specifies the location of the Artifact Registry repository and the Cloud Run subscriber.
* The final line defines `dst_repo` value, which is used to create a name for the repository in the Artifact Registry where images will be mirrored.

As an example, if the `name` value you specify is `chainguard-dev` and the `dst_repo` value is `mirrored` (as shown in the following example) any pushes to `cgr.dev/<organization>/foo` will be mirrored to `<location>-docker.pkg.dev/<project_id>/chainguard-dev-mirrored`

Be sure to include to include a closing curly bracket after the final line.

```
  name = "chainguard-dev"

  project_id = "<project-id>"

  group = "<organization-id>"

  location = "us-central1" 

  dst_repo = "mirrored"
}
```

You can create this file with a command like the following.

```sh
cat > main.tf <<EOF
module "image-copy" {
  source = "github.com/chainguard-dev/platform-examples//image-copy-gcp/iac"

  name = "chainguard-dev"

  project_id = "<project-id>"

  group = "<organization-id>"

  location = "us-central1" 

  dst_repo = "mirrored"
}
EOF
```

Make sure to replace the placeholders with your own settings for `project_id` and `group`. In the next section, we'll see how to apply the configuration to get the application up and running.

## Applying the configuration

The Terraform configuration you created in the previous section will do all the work of setting up an events subscription for you. 

Specifically, it will build the mirroring application into an image using `ko_build` and deploy the app to a Cloud Run service with permission to push to the Google Artifact Registry. It also sets up a Chainguard Identity with permissions to pull from the private `cgr.dev` repository, allows the Cloud Run service's service account  to assume the puller identity, and sets up a subscription to notify the Cloud Run service when pushes happen to `cgr.dev`.

Before applying the configuration, you'll need to log in to both the Chainguard platform with `chainctl` and GCP with `gcloud`.

```sh
chainctl auth login
gcloud auth login
```

If you haven't already done so, you will also need to acquire new access credentials to use as [Application Default Credentials](https://cloud.google.com/docs/authentication/application-default-credentials). You can do so with this command.

```sh
gcloud auth application-default login
```

Following that, run `terraform init` to initialize Terraform’s working directory.

```sh
terraform init
```

> **Note**: If you have used the [Chainguard Terraform provider](/chainguard/administration/terraform-provider/) in the past but not recently, you may need to upgrade the provider by running `terraform init --upgrade` in order to avoid errors.

Then run `terraform plan`. This will produce a speculative execution plan that outlines what steps Terraform will take to create the resources defined in the file you set up in the last section.

```sh
terraform plan
```

If the plan worked successfully and you’re satisfied that it will produce the resources you expect, you can apply it.

```sh
terraform apply
```

Before going through with applying the Terraform configuration, this command will prompt you to confirm that you want it to do so. Enter `yes` to apply the configuration. 

```
. . .

Plan: 8 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

. . .

Apply complete! Resources: 8 added, 0 changed, 0 destroyed.
```

Assuming all the resources were created as expected, you can observe the application in action.


## Testing the application

If the `terraform apply` command you ran in the previous section was successful, the Terraform configuration will have set up a Cloud Run service to host the example application. 

As mentioned previously, this application listens for `registry.push` events that occur on your organization's repository; any time a new Image gets added to your organization's Registry the application will mirror it to your GCP project's Artifact Registry and into a repository named with the `name` and `dst_repo` values you set in your `main.tf` file. For example, if these values were `chainguard-dev` and `mirrored`, respectively, (as shown in the previous example) the mirror repository would be found at `<location>-docker.pkg.dev/<project_id>/chainguard-dev-mirrored`.

You can find the results of the application in your GCP Project's dashboard. Navigate to your GCP Project's **Artifact Registry**, then click on the mirror repository you set up with Terraform. There, you will find any Images that have been added to your organization's Registry since you deployed the application. This example shows a repository named `chainguard-dev-mirrored` with two Images (`node` and `python`) mirrored into it.

![Screenshot of a repository in a GCP Artifact Registry named "chainguard-dev-mirrored." This repository shows two Images stored within it. The first, `node`, was created and updated 36 minutes ago, while the second, `python`, was created and last updated 33 minutes ago.](gcp-events-1.png)

Be aware that just because the application is listening for `registry.push` events doesn't mean any will occur automatically. Chainguard Images are generally updated at least once every twenty four hours, so Images may not immediately appear in your mirror repository.


## Removing sample resources

If you'd like to remove the resources you created with Terraform, you can run the `terraform destroy` command.

```sh
terraform destroy
```

This will destroy everything created in your Terraform configuration, including the Artifact Registry repository, the Service Account, and the Cloud Run service.

You can then remove the working directory to clean up your system.

```sh
rm -r ~/gcp-example/
```

Following that, all of the example resources created in this guide will be removed from your system.


## Learn more

Chainguard emits more CloudEvents than just the `registry:push` events highlighted in this guide. We encourage you to check out our overview of [Chainguard Events](/chainguard/administration/cloudevents/events-reference/) to learn the full breadth of event types that Chainguard generates. In addition, you may find it useful to explore the rest of our [Administration](/chainguard/administration/) resources to better understand how you can work with Chainguard's products.
