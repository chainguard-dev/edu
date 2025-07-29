---
title: "Overview of Chainguard Custom Assembly"
linktitle: "Overview"
identifier: "Custom Assembly Overview"
aliases:
- /chainguard/chainguard-images/features/custom-assembly/
type: "article"
description: "How to use Chainguard's Custom Assembly tool"
date: 2025-02-19T11:07:52+02:00
lastmod: 2025-07-15T11:07:52+02:00
draft: false
tags: ["Chainguard Containers", "Custom Assembly"]
images: []
menu:
  docs:
    parent: "features"
    identifier: "Custom Assembly Introduction"
weight: 001
toc: true
---

Chainguard has created Custom Assembly, a tool that allows users to create customized container images with extra packages added. This enables customers to reduce their risk exposure by creating container images that are tailored to their internal organization and application requirements while still having few-to-zero CVEs.

This overview of Custom Assembly outlines how it works, its limitations, and how you can use container images customized with Custom Assembly. For a more hands-on tutorial on using Custom Assembly, Chainguard Academy currently has documentation for the following methods of managing the tool:

* [Using the Chainguard console](/chainguard/chainguard-images/features/ca-docs/custom-assembly-console/)
* [Using `chainctl`, Chainguard's command-line interface tool](/chainguard/chainguard-images/features/ca-docs/custom-assembly-chainctl/)
* [Using Chainguard's API](/chainguard/chainguard-images/features/ca-docs/custom-assembly-api-demo/)


## About Custom Assembly

Custom Assembly is only available to customers that have access to Production Chainguard Containers.

In order to use the Custom Assembly tool, you will need to choose an appropriate source image from your organization's collection of Production Chainguard Containers to serve as the base for your customized container image. Say, for example, you want to build a custom base for a Python application. In this case, you would likely choose to use the [Python Chainguard Container](https://images.chainguard.dev/directory/image/python/versions) as the source for your customized image.

After selecting the packages for your customized container image, Chainguard will kick off a build on Chainguard's infrastructure. Once a customized image is built successfully (this normally takes less than 20 minutes), Chainguard will take care of its maintenance and rebuild it as necessary, such as when any of the packages in the image are updated.

### Limitations

Custom Assembly only allows you to add packages into a given container image; you cannot remove the packages included in the source application image by default. For example, Chainguard's Node.js container image comes with packages like `nodejs-23`, `npm`, and `glibc` by default. These packages can't be removed from a Node.js image using the Custom Assembly tool but you can add other packages into it, and you can remove these added packages in later builds.

The packages you can add to a container image are those that your organization already has access to based on the Chainguard Containers you have already purchased. Additionally, you can only add supported versions of packages to a customized image.

The changes you make to your customized container image may affect its functional behavior when deployed. Chainguard doesn’t test your final customized image and therefore doesn't guarantee its functional behavior. Please test your customized images extensively to ensure they meet your requirements.


## Custom Assembly Permissions Requirements

In order to build customized container images, you must have the appropriate permissions in relation to your Chainguard organization. Specifically, a Chainguard user must have a role with the `repo.update` capability. If you find yourself unable to customize container images with Custom Assembly, it may be that you don't have adequate permissions within your organization to do so.

As of this writing, only one of Chainguard's three main default roles (`viewer`, `editor`, and `owner`) has this capability: the `owner` role. 

This means that in order to use Custom Assembly, your account must be bound to the `owner` role, or to a custom role that also has the `repo.update` capability.

To create such a custom role, you can use the `chainctl iam roles create` command. The following example creates a custom role named `ca-role` with all the same capabilities as the `viewer` role, but with the added `repo.update` capability:

```shell
chainctl iam roles create ca-role --parent=$ORGANIZATION --capabilities=repo.update,account_associations.list,apk.list,group_invites.list,groups.list,identity.list,identity_providers.list,libraries.artifacts.list,libraries.entitlements.list,manifest.list,manifest.metadata.list,record_signatures.list,registry.entitlements.list,repo.list,roles.list,sboms.list,subscriptions.list,tag.list,version.list,vuln_report.list,vuln_reports.list
```

After creating this custom role, you would need to bind it to any identities in your organization that you want to be able to manage Custom Assembly resources. Check out our [Overview of Roles and Role-bindings in Chainguard](/chainguard/administration/iam-organizations/roles-role-bindings/roles-role-bindings/) to learn more.


## Using Customized Containers

You can use Docker to download the customized container image for testing or use, like this:

```shell
docker pull cgr.dev/$ORGANIZATION/$CUSTOMIZED-CONTAINER:latest
```

Be sure to change `$ORGANIZATION` to reflect the name used for your organization's private repository within the Chainguard registry and replace `$CUSTOMIZED-CONTAINER` with the actual name of your customized container image. 

Additionally, replace `latest` with your chosen tag, if different. You can find a list of all the available tags for your customized container in its **Tags** tab in the Console.

Note that you can also download specific builds of an container image by referencing the build's unique digest, as in this example:

```shell
docker pull cgr.dev/$ORGANIZATION/$CUSTOMIZED-CONTAINER@sha256:e24d3X4MPL338cb75b3X4MPL3674bd908681fca3X4MPL31e3d0321b892b9611d
```

Pulling container images by digest can [improve reproducibility](/chainguard/chainguard-images/how-to-use/container-image-digests/). 

> If you run into any issues with your customized container images or with using the Custom Assembly tool, please reach out to your account team for assistance.


### Installing packages from a Chainguard private APK repository

Chainguard offers [Private APK Repositories](/chainguard/chainguard-images/features/private-apk-repos/) which you can use to access the apk packages available to your organization. You can use your organization's private APK repository to further customize your Custom Assembly containers.

As an example, run a container with a Custom Assembly container image that has a shell and package manager, such as a `-dev` variant of a customized container image:

```shell
docker run -it --entrypoint /bin/sh --user root  \
-e "HTTP_AUTH=basic:apk.cgr.dev:user:$(chainctl auth token --audience apk.cgr.dev)" \
cgr.dev/$ORGANIZATION/$CUSTOMIZED-CONTAINER:latest-dev
```

Note that this command injects an `HTTP_AUTH` environment variable directly into the container by calling `chainctl` from the host machine to obtain an ephemeral token. This is necessary to authenticate to the private repository.

By default, your organization's private APK repository will be listed in the container's list of APK repositories:

```container
cat /etc/apk/repositories
```
```Output
https://apk.cgr.dev/45a0c3X4MPL3977f03X4MPL3ac06a63X4MPL3595
```

The repository address in this file (which includes a long unpronounceable string) will differ from the one shown in the Console (which reflects the organization name). The string shown in the `repositories` file is the ID number of the organization. You can confirm this by running the `chainctl iam organizations ls -o table` command.

To search for and install packages from the private APK repository, first the package index:

```container
apk update
```
```Output
fetch https://apk.cgr.dev/45a0c3X4MPL3977f03X4MPL3ac06a63X4MPL3595/x86_64/APKINDEX.tar.gz
 [https://apk.cgr.dev/45a0c3X4MPL3977f03X4MPL3ac06a63X4MPL3595]
OK: 1019 distinct packages available
```

Then you can search for packages available in your private repo. The following example searches for packages named "mongo":

```container
apk search mongo
```
```Output
mongo-5.0-5.0.31-r0
mongo-6.0-6.0.20-r0
mongo-7.0-7.0.16-r0
mongo-8.0-8.0.4-r1
mongod-5.0-5.0.31-r0
mongod-6.0-6.0.20-r0
mongod-7.0-7.0.16-r0
mongod-8.0-8.0.4-r1
```

Finally, you can install a package with `apk`:

```container
apk add mongo
```
```Output
(1/1) Installing mongo-8.0 (8.0.4-r1)
Executing busybox-1.37.0-r0.trigger
OK: 719 MiB in 78 packages
```

To learn more, refer to our [Private APK Repositories documentation](/chainguard/chainguard-images/features/private-apk-repos/).


## Troubleshooting

Build failures can occur for a number of reason, including the following:

* It's possible for users to select packages that conflict with each other. For example, if two packages install the same files, Custom Assembly may not be able to resolve the conflict and result in a failed build.
* Large images taking longer than 1 hour to build will fail with a timeout error.
* There is a known bug where container images will not be rebuilt if their source image was last built more than 48 hours ago.

In any case, you won't know whether a container image build fails until after it's complete. If you need assistance troubleshooting, please [reach out to our Customer Support team](https://www.chainguard.dev/contact?utm=docs).


## Learn More

Custom Assembly allows customers to leverage Chainguard’s build infrastructure to produce container images tailored to their requirements. That means customers no longer have to stand up and maintain their own builds, saving costs in the form of infrastructure, engineering overhead, and complexity.

This article provided a high-level overview of Custom Assembly. As a next step, we encourage you to checkout our guide on [managing Custom Assembly resources through the Chainguard Console](/chainguard/chainguard-images/features/ca-docs/custom-assembly-console/). You can also interact with Custom Assembly using [`chainctl`](/chainguard/chainguard-images/features/ca-docs/custom-assembly-chainctl/) as well as [the Chainguard API](/chainguard/chainguard-images/features/ca-docs/custom-assembly-api-demo/).

We encourage you to check out our resources on our other [Chainguard Containers features](/chainguard/chainguard-images/features/), including the following:

* [Unique Tags](/chainguard/chainguard-images/features/unique-tags/)
* [CVE Visualizations](/chainguard/chainguard-images/features/cve_visualizations/)
* [Custom Certificates](/chainguard/chainguard-images/features/incert-custom-certs/)

Additionally, for more information on working with Chainguard Containers, refer to our docs on [How to Use Chainguard Containers](/chainguard/chainguard-images/how-to-use/).
