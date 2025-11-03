---
title: "How to Sync Images from Chainguard's Registry to Harbor"
linktitle: "Harbor"
type: "article"
description: "Tutorial outlining how to sync images from Chainguard's registry to Harbor."
date: 2025-08-19T12:00:00-00:00
lastmod: 2025-08-19T12:00:00-00:00
draft: false
tags: ["Chainguard Containers"]
images: []
menu:
  docs:
    parent: "pull-through-guides"
toc: true
weight: 015
contentType: "product-docs"
---

[Harbor](https://goharbor.io) is an open-source artifact registry. It's designed to securely store, manage, and distribute OCI artifacts, including container images and Helm charts by enforcing policies like vulnerability scanning, image signing, and role-based access control. Harbor delivers enterprise-grade compliance, performance, and interoperability across platforms like Kubernetes and Docker, all accessible via a web UI or RESTful API.

This tutorial outlines how to sync images from Chainguard's registry to a Harbor instance. It describes two approaches:

1. A [proxy cache](https://goharbor.io/docs/2.1.0/administration/configure-proxy-cache/), which configures a Harbor project as a pull through cache.
2. A [replication rule](https://goharbor.io/docs/2.1.0/administration/configuring-replication/create-replication-rules/), which copies images to a Harbor project.

## Prerequisites

You need the following in order to complete this tutorial:

* Administrative privileges over a Harbor instance. Refer to the [official Harbor documentation](https://goharbor.io/docs/2.13.0/) to learn how to set this up.
* `chainctl` — Chainguard's command-line interface — installed on your local machine. If you don't have `chainctl` installed, refer to our [How to Install `chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/) guide to set this up.
* Access to an account with permissions to pull Chainguard container images from your organization's repository within the Chainguard registry. This is necessary, as you will create a pull token for Harbor to use to access the registry, and you cannot generate a pull token that grants broader access than your own.


## Create a Registry Endpoint

Before configuring a proxy cache or replication rule, you must create a registry endpoint for the Chainguard registry.

If you don't already have one, generate a pull token in your organization:

```shell
chainctl auth configure-docker --parent <org-name> --pull-token
```

This returns username and password credentials:

```Output
To use this pull token in another environment, run this command:

    docker login "cgr.dev" --username "<pull-token-username>" --password "<pull-token-password>"
```

Take note of these values, as you'll need them shortly.

Next, open up the Harbor UI and perform the following steps:

1. Navigate to **Administration > Registries**
2. Click the **+ NEW ENDPOINT** button..
3. Configure the endpoint with these details:
    * **Provider** — There is no specific integration with the Chainguard registry, so here you must select the generic `Docker Registry` provider type.
    * **Name** — This is used to refer to your repository. You can choose whatever name you like here, but this guide's examples use the name `cgr.dev`.
    * **Endpoint URL** — This value **must** be `https://cgr.dev`.
    * **Access ID** — Enter the username value returned by the `chainctl auth` command you just ran.
    * **Access Secret** — Here, enter the password value returned by the `chainctl auth` command.
4. Click the **TEST CONNECTION** button to ensure that Harbor can reach `cgr.dev` successfully.
5. Click **OK** to create the endpoint.

After creating the endpoint, you can move on to creating a proxy cache.


## Create a Proxy Cache

A [*proxy* cache](https://goharbor.io/docs/2.1.0/administration/configure-proxy-cache/) allows Harbor to proxy and cache images from the Chainguard registry.

To configure a cache, perform the following steps in the Harbor UI:

1. Navigate to **Projects**.
2. Click the **+ NEW PROJECT** button.
3. Create the project with these details:
    * **Project Name** — This can be whatever you like. This guide uses the name `cgr—proxy`.
    * **Access Level** — Set this as required for your organization. Checking the **Public** box means `docker login` is not required.
    * **Project quota limits** — leave at `-1` for unlimited or set as required.
    * **Proxy Cache** — Toggle this on.
    * **Endpoint** — Choose the endpoint you created in the previous step.
    * **Bandwith — leave at `-1` for unlimited or set as required.
4. Click **OK**

Following that, you can pull images from the Harbor project like so:

```shell
docker pull $HARBOR_URL/cgr-proxy/$ORGANIZATION/$IMAGE:$TAG
```

Be sure to replace the placeholder values (`$HARBOR_URL`, `$ORGANIZATION`, `$IMAGE`, and `$TAG`) to reflect your own setup.


## Create a Replication Rule

A [*replication rule*](https://goharbor.io/docs/2.1.0/administration/configuring-replication/create-replication-rules/) is an alternative approach to a proxy cache. This section outlines how to configure a replication rule that copies images from the Chainguard registry to a Harbor project.

First, create a project:

1. Navigate to **Projects**.
2. Click the **+ NEW PROJECT** button.
3. Create the project with these details:
    * **Project Name** — This can be whatever you like. This guide uses the name `cgr—mirror`.
    * **Access Level** — Set this as required for your organization. Checking the **Public** box means `docker login` is not required.
    * **Project quota limits** — leave at `-1` for unlimited or set as required.
    * **Proxy Cache** — Leave this toggled off.
4. Click **OK**

Then, perform the following steps to create a new replication rule:

1. Navigate to **Administration > Replications**.
2. Click the **+ NEW REPLICATION RULE** button.
3. Create a new rule with these details:
    * **Name** — This can be whatever you like. This guide uses the name  `cgr-mirror`.
    * **Replication mode** — Must be `Pull-based`.
    * **Source registry** — Specify the `cgr.dev` endpoint.
    * **Source resource filter > Name** — (Optional) You can ensure you only select images in your organization by setting this to `<org-name>/*`.
    * **Destination > Namespace** — This should be the project you created before.
    * **Destination > Flattening** — Set to `Flatten All Levels`. This removes the organization name from the path.
    * **Trigger Mode** — Set to `Scheduled` to run the replication regularly or `Manual` to trigger on an ad hoc basis.
    * **Bandwidth** — leave at `-1` for unlimited or set as required.
    * **Override** — Ensure this is enabled so that tags in the destination project are replaced when they change.
4. Click the **Save** button.

To trigger the replication manually, select the `cgr-mirror` rule in the table and click the **REPLICATE** button. Then, navigate to **Projects > cgr-mirror** and observe images populating.

You should be able to pull images from the project like this:

```shell
docker pull $HARBOR_URL/cgr-mirror/$IMAGE:$TAG
```

Again, be sure to replace this command's placeholder values as necessary.



## Learn More

If you haven't already done so, you may find it useful to review our [Registry Overview](/chainguard/chainguard-registry/overview/) to learn more about Chainguard's registry. You can also learn more about Chainguard Containers by checking out our [Containers documentation](/chainguard/chainguard-images/overview/).

Additionally, if you'd like to learn more about Harbor, we encourage you to refer to the [official Harbor documentation](https://goharbor.io/docs).
