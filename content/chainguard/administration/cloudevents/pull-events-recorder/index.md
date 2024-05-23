---
title: "Listen for Chainguard Pull Events and Store them in BigQuery"
type: "article"
description: "Instructional guide outlining how one can set up an application that will listen for pull events in a given Chainguard Registry and store the data in Google BigQuery."
date: 2024-05-21T15:22:20+01:00
lastmod: 2024-05-21T15:22:20+01:00
draft: false
tags: ["Product", "CloudEvents", "Procedural"]
images: []
menu:
  docs:
    parent: "cloudevents"
weight: 10
toc: true
---

When you interact with certain Chainguard resources, it will emit [CloudEvents](/chainguard/administration/cloudevents/events-reference/) that you or an application can subscribe to. This allows you to do things like receive alerts when a new repository is created in your organization's registry or learn when your organization's private Images are being downloaded. 

This tutorial is meant to serve as a companion to the [CloudEvents recorder](https://github.com/chainguard-dev/platform-examples/tree/main/event-recorder) example application. It will guide you through setting up infrastructure to listen to Chainguard Image pull events and store them in BigQuery for later analysis.


## Prerequisites

To follow along with this guide, it is assumed that you have the following tools and programs set up and ready to use.

* `chainctl`, the Chainguard command-line interface. You can install this by following our guide on [How to Install `chainctl`](/chainguard/administration/how-to-install-chainctl/).
* `terraform` to configure a Google Cloud service account, IAM permissions, and deploy the Cloud Run service.
* A Google Cloud account with a project running. The example application assumes that your project has the following APIs enabled:
    * [Cloud DNS API](https://cloud.google.com/dns/docs/overview/)
    * [BigQuery API](https://cloud.google.com/bigquery/docs/reference/rest)
    * [BigQuery Data Transfer API](https://cloud.google.com/bigquery/docs/reference/datatransfer/rest)
    * [Compute Engine API](https://cloud.google.com/compute/docs/reference/rest/v1)
    * [Artifact Registry API](https://cloud.google.com/artifact-registry/docs/reference/rest)
    * [Cloud Run Admin API](https://cloud.google.com/run/docs/reference/rest)
* The [`gcloud` CLI](https://cloud.google.com/sdk/docs/install) installed on your local machine. You'll need this to authenticate to Google Cloud over the command line.


## How the sample application works

As mentioned in the introduction, this guide is meant to serve as a companion to the [`events-recorder` application](https://github.com/chainguard-dev/platform-examples/tree/main/event-recorder) in our public [Platform Examples repository](https://github.com/chainguard-dev/platform-examples/). 

This application will record data  whenever an Image gets pulled from a specified organization's private [Chainguard Registry](/chainguard/chainguard-registry/overview/). It does this by leveraging GCP Cloud Run, Cloud Pub/Sub and Cloud Storage to efficiently buffer events before loading into BigQuery.

![i think this is alt text?](https://mermaid.ink/img/pako:eNpNkTFPwzAQhf-K5SkRrRBCLB2QSNIiJAZoyxQzOPElserY0dluVVX979hJoHg6nd_77vl8obURQFe0UeZUdxwd2RdMk3BekiTJOy516zmKNE3JckngCNrZUD2TrGQ0V8YLsvWa7JH3g1FSA2M6GXylZE2-tu8po98TL4v-I1dScAeC3JFGKgcYykjLyxsrQ3MAJG-6RbB2tltftciHjgwoj4FANLiTwcN0m0f4ONV2I68o_-J9-Op-56uYq_JNE0fGVDO3iM4AtzXKCkbv-l-WLdQGBeCsXkf1CaUDG3eBZ_LYj57N7Nk5g7yFWb6JcmW4-FU_PE3y1zLJZPvpQy-dtaAFXdAesOdShB-5xDajroMeGF2FUvDwXMr0Nei4d2Z31jVdOfSwoH6Iay0kD0vqp-b1B1XEmCs?type=png)]

![diagram](mermaid-diagram-2024-05-22-232315.png)

This means that records may not be published immediately, with a delay of up to 18 minutes end-to-end. With that said, the application should be able to handle bursts of requests gracefully without dropping events. When no events are being received, the Cloud Run services will scale to zero and incur no cost. During bursts of events, services will scale up as needed.

The Terraform configuration you'll use in this guide will do all the work of setting up the example application's infrastructure and resources. Importantly, it creates a BigQuery dataset named `cloudevents_pull_event_recorder`, with a table named `dev_chainguard_registry_pull_v1`.

The [`pull.schema.json` file](https://github.com/chainguard-dev/platform-examples/blob/main/event-recorder/iac/pull.schema.json) describes this dataset's schema, which contains fields describing the user who pulled the image, the image that was pulled, the time of the pull, and information about errors that occurred during the pull. This schema matches the description for the `registry:pul `event type described in the [Chainguard Events overview documentation](/chainguard/administration/cloudevents/events-reference/#service-registry---pull).

> **Note**: The purpose of the example application and this tutorial is to show how Chainguard CloudEvents can be ingested and used. It is not meant to serve as a long-term solution. Any solution you implement should be configured specifically to align with your organization's policies and support its needs. 


## Setting up the Terraform configuration

You can find all the code associated with this sample application in our [Platform Examples](https://github.com/chainguard-dev/platform-examples/tree/main/event-recorder) repository on GitHub. 

To set up the sample application, you can create a Terraform configuration file that points to the application code in the Platform Examples repository and then apply it to set up the necessary resources. To begin, create a new directory to hold the configuration file and navigate into it.

```sh
mkdir ~/gcr-pull-data && cd $_
```

After navigating into the new directory you can begin creating a Terraform configuration named `main.tf`. We'll go through each line of this file one by one.

This configuration will consist of a single module. For the purposes of this example, we will call it `event-recorder`. This module's `source` value will be the [`iac` folder](https://github.com/chainguard-dev/platform-examples/tree/main/event-recorder/iac) from the application code in the examples repository.

```
module "event recorder" {
  source = "github.com/chainguard-dev/platform-examples//event-recorder/iac"
```

The next section specifies the GCP project ID where the application resources will reside.

```
  project_id = "<GCP project ID>"
```

Following that, the configuration specifies the region where the application's subnetwork will be created.

```
  region 	= "us-central1"
```

Lastly, it specifies the UIDP of the Chainguard IAM organization associated with the private Reigstry from which we expect to receive events.

```
  group = "<organization-id>"
}
```

If you don't know your organization's UIDP, you can retrieve it the following command.

```sh
chainctl iam organizations list -o table
```

You can create this file with a command like the following.

```sh
cat > main.tf <<EOF
module "event-recorder" {
  source = "github.com/chainguard-dev/platform-examples//event-recorder/iac"

  project_id = "<GCP project ID>"
  region 	= "us-central1"
  group  	= "<Chainguard organization ID>"
}
EOF
```

Following that you can apply the configuration to get the application working.


## Applying the configuration

Before applying the configuration, you'll need to log in to both the Chainguard platform with `chainctl` and GCP with `gcloud`.

```sh
chainctl auth login
gcloud auth login
```

Following that, run `terraform init` to initialize Terraform’s working directory.

```sh
terraform init
```

Then run `terraform plan`. This will produce a speculative execution plan that outlines what steps Terraform will take to create the resources defined in the files you set up in the last section.

```sh
terraform plan
```

If the plan worked successfully and you’re satisfied that it will produce the resources you expect, you can apply it.

```sh
terraform apply
```

Before going through with applying the Terraform configuration, this command will prompt you to confirm that you want it to do so. Enter `yes` to apply the configuration. 

Assuming all the resources were created as expected, you can now observe the application in action.


## Testing the application

After running the commands in the previous section, Terraform will have created all the resources the example application needs to function correctly.

You can now test that the application is working correctly by pulling one or more images from your organization's repository and waiting for the event data from these pulls to appear in your BigQuery dashboard. 

As an example, if your organization has access to the `python` Image, you could pull it with a command like the following.

```sh
docker pull cgr.dev/<chainguard.organization>/python:latest
```

After you or someone else with access to the organization repo pulls an Image from the repository, data relating to that pull will appear in the specified GCP project's BigQuery dashboard. The Terraform configuration creates a BigQuery dataset named `cloudevents_pull_event_recorder` with a table named `dev_chainguard_registry_pull_v1`. 

You can find this table in the Google Cloud Platform from the BigQuery explorer. In the Explorer's left-hand navigation, click on the name of your project in the drop-down menu, then click `cloudevents_pull_event_recorder` dataset to find the `dev_chainguard_registry_pull_v1` table.


![Screenshot of the BigQuery Explorer interface for a project named "cg-academy-example". It shows the "dev_chainguard_registry_pull_v1" table open to the "Preview" tab with three rows visible. The top row shows a "repository" value of "chainguard.edu/python" and a "tag" value of "3.11.9," indicating that this pull data relates to someone pulling version 3.11.9 of the python image.](gcp-bigquery-example.png)

As mentioned previously, be aware that records may not be published immediately, with a delay of up to 18 minutes end-to-end. With that said, the application should be able to handle bursts of requests gracefully without dropping events.


## Removing sample resources

If you'd like to remove the resources you created with Terraform, you can run the `terraform destroy` command.

```sh
terraform destroy
```

This will destroy all the resources Terraform created when you ran the `terraform apply` command earlier in this tutorial.

You can then remove the working directory to clean up your system.

```sh
rm -r ~/gcr-pull-data/
```

Following that, all of the example resources created in this guide will be removed from your system.

## Learn more

Chainguard emits more CloudEvents than just the `registry:pull` events highlighted in this guide. We encourage you to check out our overview of [Chainguard Events](/chainguard/administration/cloudevents/events-reference/) to learn the full breadth of event types that Chainguard generates. In addition, you may find it useful to explore the rest of our [Chainguard Administration](/chainguard/administration/) resources to better understand how you can work with Chainguard's products.