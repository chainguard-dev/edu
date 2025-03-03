---
title: "Chainguard's Custom Assembly Images"
linktitle: "Custom Assembly"
type: "article"
description: "How to use Chainguard's Custom Image Assembly tool."
date: 2025-02-19T11:07:52+02:00
lastmod: 2025-02-19T11:07:52+02:00
draft: false
tags: ["CONCEPTUAL", "CHAINGUARD IMAGES", "PRODUCT", "REFERENCE"]
images: []
menu:
  docs:
    parent: "features"
weight: 001
toc: true
---

Chainguard has created a Custom Assembly tool that allows users to create customized images with extra packages added. This enables customers to reduce their risk exposure by creating container images that are tailored to their internal organization and application requirements while still having few-to-zero CVEs.

This guide outlines how to build customized Chainguard Images using Custom Assembly in the Chainguard Console. It includes a brief overview of how Custom Assembly works, as well as its limitations.

> **NOTE**: The Custom Assembly tool is currently in its beta phase and it is likely to go through changes before it becomes generally available.


## About Custom Assembly

Custom Assembly is only available to customers that have access to Production Chainguard Images. Additionally, your account team must enable Custom Assembly before you will be able to begin using it. Contact your account team directly to start the process.

When you enable the Custom Assembly tool for your organization, you must select at least one of Chainguard's application images to serve as the source for your customized image. For example, if you want to build a custom base for a Python application, you would likely elect to use the [Python Chainguard Image](https://images.chainguard.dev/directory/image/python/versions) as the source for your customized image.

After selecting the packages for your customized image, Chainguard will kick off a build on Chainguard's infrastructure. Once a customized image is built successfully, Chainguard will take care of its maintenance and rebuild it as necessary, such as when any of the packages in the image are updated.


### Limitations

Custom Assembly only allows you to add packages into a given image; you cannot remove the packages included in the source application image by default. For example, Chainguard's Node.js image comes with packages like `nodejs-23`, `npm`, and `glibc` by default. These packages can't be removed from a Node.js image using the Custom Assembly tool but you can add other packages into it, and you can remove these added packages in later builds.

The packages you can add to an image are those that your organization already has access to based on the Chainguard Images you have already purchased. Additionally, you can only add supported versions of packages to a customized image.

The changes you make to your customized image may affect its functional behavior when deployed. Chainguard doesn’t test your final customized image and therefore doesn't guarantee its functional behavior. Please test your customized images extensively to ensure they meet your requirements.

Lastly, while Custom Assembly is in its beta phase it can only be configured from the Chainguard Console.


## Accessing Customized Images in the Console

To provision a customized image, reach out to your account team who will configure one for you.

After logging in to the [Chainguard Console](https://console.chainguard.dev/auth/login), you will be greeted with your account overview page. If you belong to more than one organization, be sure to select the organization which has Custom Assembly enabled from the drop-down menu in the top-left corner.

Click on **Organization Images** and scroll or search for the customized image that was set up by your account team. This will typically have a name that specifies the source image while also highlighting that it is a customized image, such as `python-custom` or `node-custom`. Once you've found it, click on the image.


## Selecting Packages and Building a Customized Image

Clicking on the Custom Assembly image will take you to its entry in the Console. In the upper right corner of this page, you'll find a button that says **Customize Image**: 

<center><img src="custom-assembly-1.png" alt="Screenshot of a Custom Assembly image (named 'custom-node') page with the 'Customize Image' button highlighted in a yellow box." style="width:1100px;"></center>
<br /> 

Click on this button to open a window displaying a list of all of the packages available to be added or removed from your selected image. This list of packages includes all the packages your organization is entitled to. If there's a package you'd like to include in your image but it isn't available in this list, reach out to your account team for access.

You can scroll through the list and select or deselect packages to tailor the image to your needs by checking their respective boxes. Alternatively, you can use the search box to filter for the packages you're looking for.

After selecting your chosen packages, click the **Preview Changes** button to view all the packages you've selected for the customized image:

<center><img src="custom-assembly-2.png" alt="Screenshot of the custom-node image's customization preview. It shows three packages selected: bash, curl, and wget." style="width:650px;"></center>
<br /> 

If you'd like to make further changes, click the **Back** button to return to the package selection.

If you're satisfied with the selection of packages, click the **Apply Changes** button to build the new customized image. You will receive a confirmation message at the top of the Customize Image display letting you know that the image was successfully customized.

If a build fails, you'll need to make the appropriate changes before attempting another build. You can check their logs for information about what went wrong and what to fix.


## Listing Builds and Viewing Logs

You can view a list of all the available builds of your customized image by clicking the customized image's **Builds** tab in the Console:

<center><img src="custom-assembly-3.png" alt="Screenshot of a Custom Assembly image's Builds tab, with the Builds tab highlighted in a yellow box." style="width:1100px;"></center>
<br /> 

The table in the Builds tab has six columns:

* **ID**: A unique identifier representing a specific customized image build.
* **Version**: The image version the build represents.
* **Status**: The status of the given build. When a build is successful, this column will show a green check inside of a circle. When a build has failed, this column will display a red exclamation mark in a triangle.
* **Digest**: A unique, content-based hash representing the given image build. 
* **Duration**: The amount of time it took to build the image.
* **Created**: How long it's been since the build was created. 

Note that if you only recently customized the image it may take a few minutes for the latest builds to populate.

Additionally, builds will only stay listed in the Console for 24 hours. This is because Chainguard Images, including Custom Assembly images, are rebuilt frequently and would quickly congest the user interface.

You can click on the row of any build listed in the Builds tab to access its logs. This will cause a window to appear from the right where you can get more details about the build, including build failures:

<center><img src="custom-assembly-4.png" alt="Screenshot of a customized image build's logs, showing a successful build." style="width:650px;"></center>
<br /> 


## Using Customized Images

You can use Docker to download the customized image for testing or use, like this:

```shell
docker pull cgr.dev/$ORGANIZATION/$CUSTOMIZED-IMAGE:latest
```

Be sure to change `$ORGANIZATION` to reflect the name used for your organization's private repository within the Chainguard registry and replace `$CUSTOMIZED-IMAGE` with the actual name of your image. 

Additionally, replace `latest` with your chosen tag, if different. You can find a list of all the available tags for your customized image in its **Versions** tab in the Console.

Note that you can also download specific builds of an image by referencing the build's unique digest, as in this example:

```shell
docker pull cgr.dev/$ORGANIZATION/$CUSTOMIZED-IMAGE@sha256:e24d3X4MPL338cb75b3X4MPL3674bd908681fca3X4MPL31e3d0321b892b9611d
```

Pulling images by digest can [improve reproducibility](/chainguard/chainguard-images/how-to-use/container-image-digests/). 

> If you run into any issues with your customized images or with using the Custom Assembly tool, please reach out to your account team for assistance.


### Installing packages from a Chainguard private APK repository

Chainguard offers [Private APK Repositories](/chainguard/chainguard-images/features/private-apk-repos/) which you can use to access that apk packages that your organization has access to. You can use your organization's private APK repository to further customize your Custom Assembly images.

As an example, run a container with a Custom Assembly image that has a shell and package manager, such as a `-dev` variant of a customized image:

```shell
docker run -it --entrypoint /bin/sh --user root  \
-e "HTTP_AUTH=basic:apk.cgr.dev:user:$(chainctl auth token --audience apk.cgr.dev)" \
cgr.dev/$ORGANIZATION/$CUSTOMIZED-IMAGE:latest-dev
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


### Installing packges from Chainguard's package repositories

You can use `apk` to install additional packages from Chainguard's package repositories (`apk.cgr.dev/extra-packages` and `packages.wolfi.dev/os`) into your customized image.

To illustrate, run the following command to create a Dockerfile:

```shell
cat > Dockerfile <<EOF
FROM cgr.dev/$ORGANIZATION/custom-assembly:latest-dev
USER root
RUN mv /etc/apk/repositories /etc/apk/repositories.disabled
RUN echo 'https://apk.cgr.dev/extra-packages' >> /etc/apk/repositories
RUN echo 'https://packages.wolfi.dev/os' >> /etc/apk/repositories
EOF
```

This Dockerfile uses the `latest-dev` version of a Custom Assembly image named `custom-assembly`. You will need to change the name of the image (along with the name of your organization's repository within the Chainguard Registry) to reflect your own setup.

Note that this Dockerfile renames the image's default `/etc/apk/repositories` file and adds the two repositories to the new `repositories` file. This isn't necessary, but will disable the private APK repository listed in the file by default. This will allow us to use only the `extra-packages` and `wolfi` repositories.

Using this Dockerfile, build a new image:

```shell
docker build -t custom-apk .
```

Then run a container with the newly-built image. This command will run the image in an interactive container and changes the entrypoint to open up the Bash shell:

```shell
docker run -it --entrypoint /bin/sh --user root custom-apk
```

From the customized image's shell, add the `packages.wolfi.dev/os` repository keys. Note that this command includes the `--allow-untrusted` flag; by adding the keys with this command, you won't need to include this flag with this repository moving forward:

```container
apk add wolfi-keys --allow-untrusted
```

Following that, install the `apko` package. You will use this package to install the keys for the `apk.cgr.dev/extra-packages` repository shortly:

```container
apk add apko
```

Finally, run `apko install-keys` to add the keys for the `apk.cgr.dev/extra-packages` repository. This command uses key discovery based on the repositories present in `/etc/apk/repositories`:

```container
apko install-keys
```

With that, you can any packages available from these repositories:

```container
apk add curl
```
```Output
OK: 676 MiB in 79 packages
```


## Troubleshooting

Build failures can occur for a number of reason, including the following:

* It's possible for users to select packages that conflict with each other. For example, if two packages install the same files, Custom Assembly may not be able to resolve the conflict and result in a failed build.
* There is a known bug where images will not be rebuilt if their source image is more than 48 hours old. 

In any case, you won't know whether an image build fails until after it's complete. If you need assistance troubleshooting, please [reach out to our Customer Support team](https://www.chainguard.dev/contact?utm=docs).


## Conclusion

Custom Assembly allows customers to leverage Chainguard’s build infrastructure to produce container images tailored to their requirements. That means customers no longer have to stand up and maintain their own builds, saving costs in the form of infrastructure, engineering overhead, and complexity.

We encourage you to check out our resources on our other [Chainguard Images features](/chainguard/chainguard-images/features/), including the following:

* [Unique Tags](/chainguard/chainguard-images/features/unique-tags/)
* [CVE Visualizations](/chainguard/chainguard-images/features/cve_visualizations/)
* [Custom Certificates](/chainguard/chainguard-images/features/incert-custom-certs/)

Additionally, for more information on working with Chainguard images, refer to our docs on [How to Use Chainguard Images](/chainguard/chainguard-images/how-to-use/).
