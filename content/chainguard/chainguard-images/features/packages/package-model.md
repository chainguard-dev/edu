---
title: "Overview of Chainguard's Package Repositories"
linktitle: "Package Repositories"
lead: "Overview of Chainguard's package repositories, highlighting the different repositories and how to access them."
description: "Overview of Chainguard's package repositories, highlighting the different repositories and how to access them."
type: "article"
date: 2025-09-12T00:00:00Z
lastmod: 2025-09-12T00:00:00Z
draft: false
tags: ["Chainguard Containers", "Overview", "Product"]
images: []
weight: 001
---

Chainguard offers curated package repositories to support containerized workloads and simplify dependency management. These repositories ensure you can access trusted packages — whether building custom container images, working with Chainguard OS, or using Chainguard Containers in production.

This article provides an overview of Chainguard's package model, highlighting the different Chainguard package repositories available to customers.


## Repository Types

Chainguard Customers have access to three distinct package repositories maintained by Chainguard:

* Wolfi
* Extra
* A Private APK Repository specific to their organization

> **Note**: Be aware that the packages maintained by Chainguard are not covered by an SLA.

Chainguard Containers are built to run `apk` (Alpine Package Keeper) packages, a package format developed for [Alpine Linux](https://www.alpinelinux.org/). Accordingly, Chainguard's package repositories contain apk packages, the package format developed for apk, and you can interact with them using the standard [`apk` commands](https://docs.alpinelinux.org/user-handbook/0.1a/Working/apk.html). Chainguard maintains the packages within all of these package repositories. 

The following table presents a high-level overview of these package repositories:

| Repository Type | Access Level | Package Scope | Authentication Required | Typical Use Case |
|-----------------|:----------------:|:----------------------:|:-----------------------:|:------------------------:|
| Wolfi | Public | Wolfi ecosystem | No | Starter images |
| Extra | Public | Supplemental utilities | No | Additional dependencies |
| Private | Private/Organization-specific | Packages in org-entitled container images | Yes | Customizing Chainguard Containers with [Custom Assembly](/chainguard/chainguard-images/features/ca-docs/custom-assembly/) |


## Public Repositories

Chainguard has two public package repositories: the Wolfi and Extra package repositories. These repos typically include the latest stable versions and explicitly exclude FIPS-validated packages or version streams. 

### Wolfi packages repository

The [Wolfi packages repository](https://github.com/wolfi-dev/os) is the public package source for [Wolfi, Chainguard's open-source Linux "undistro."](/open-source/wolfi/overview/) It contains all the open-source packages used in Chainguard's Starter tier of free container images. As a public repository, the Wolfi APK repo doesn't require authentication. 

By default, Chainguard's Starter container images use a generic address for this repository (`https://apk.cgr.dev/chainguard`) in their `/etc/apk/repositories` files:

```shell
docker run -it --rm --entrypoint cat cgr.dev/chainguard/python:latest-dev /etc/apk/repositories
```
```output
https://apk.cgr.dev/chainguard
```

Chainguard customers can access it with a URL that's unique to their organization:

```url
https://virtualapk.cgr.dev/$ORGANIZATION_ID/chainguard
```

If you need packages outside Wolfi's open-source scope, or under less permissive licenses, Chainguard offers a supplemental Extra packages repository

### Extra packages repository

Chainguard's Extra Packages repository is a public-facing APK repository that includes utilities and compatibility packages that aren't fully open-source, but can still be redistributed by Chainguard. The repository’s primary role is to provide supplemental packages needed to support containerized applications, especially when those utilities fall outside the scope of the official base images or are under less permissive licenses than those in the Wolfi repository.

The Extra packages repository follows similar rules to the Wolfi repo, but explicitly allows packages under more restrictive licenses as long as redistribution is permitted.

The Extra package repository isn't specified in the `/etc/apk/repositories` file of Chainguard's Starter images by default. Like the Wolfi repository, though, customers can access it with a URL that's unique to their organization:

```url
https://virtualapk.cgr.dev/$ORGANIZATION_ID/extra-packages
```


### Working with public repositories

As mentioned previously, both the Wolfi and Extra Packages repositories are public and don't require authentication. Chainguard customers can access both with a URL that's unique to their organization:

* Wolfi: `https://virtualapk.cgr.dev/$ORGANIZATION_ID/chainguard`
* Extra: `https://virtualapk.cgr.dev/$ORGANIZATION_ID/extra-packages`

You must replace `$ORGANIZATION_ID` with your organization's unique identifier (UID). You can find this with `chainctl` if [you've installed it](/chainguard/chainctl-usage/how-to-install-chainctl/): 

```shell
chainctl iam orgs ls -o table
```
```output
                    ID                    |      NAME       |          DESCRIPTION                          
------------------------------------------|-----------------|--------------------------------------
 0a************************************c8 | example.com     | This is an example organization
```

You can also find this in the [Chainguard Console](https://console.chainguard.dev/). After logging in, open the **Settings** tab. There, you'll find your organization's identifier under **Organization UID**. Be aware that these repository URLs **will not** resolve properly if you include the name of your organization instead of the UID. 

For any of your organization's Chainguard Containers that include the APK package manager, these repositories are included by default. You can also add them to the `/etc/apk/repositories` file of any container that uses APK. Our guide on [How to Pull Packages from Chainguard Package Repositories through Artifactory](/chainguard/chainguard-images/chainguard-registry/pull-through-guides/artifactory/artifactory-packages-pull-through/#configuring-pull-through-caches-for-chainguards-public-repositories) includes directions for setting up pull-through caches for these repositories on Artifactory.


## Private APK Repositories

Chainguard customers have access to a private APK repository that is only accessible to members of their organization, allowing them to pull apk packages maintained by Chainguard. The packages in a private APK repository include any Chainguard packages not available in the Wolfi or Extra repositories. These include the main packages found in Chainguard container images, as well as any packages relating to FIPS support.

However, a given organization's private APK repository will only contain a subset of the packages not included in the Wolfi or Extra repositories. The list of packages available in an organization’s private repository is based on the packages available in the Chainguard Containers that the organization already has access to.

For example, say your organization has access to the Chainguard MySQL container image. Along with the container's main package (`mysql`), this image comes with other apk packages, including `bash`, `glibc`, and `pwgen`. This means that you’ll have access to these apk packages through your organization’s private APK repository, along with any others that appear in Chainguard container images that your organization has access to.

Chainguard's private APK repositories have URLs that follow this form:

```url
https://apk.cgr.dev/$ORGANIZATION
```

Because Chainguard's private APK repos are only accessible to members of a specific organization, you must authenticate in order to access them. Refer to our overview of [Chainguard's Private APK Repositories](/chainguard/chainguard-images/features/private-apk-repos/) for more information. Additionally, note that if you customize a Chainguard Container using the [Custom Assembly tool](/chainguard/chainguard-images/features/ca-docs/custom-assembly/), the list of packages available for you to add to your container image is taken from your organization's private APK repository.


## Learn More

Chainguard’s package repositories provide trusted apk packages to support both standard and advanced containerized workloads. With the public Wolfi and Extra repositories alongside organization-specific private repositories, customers can reliably source the dependencies they need for production environments.

We encourage you to learn more about Chainguard's private APK repositories by referring to our [documentation on the subject](/chainguard/chainguard-images/features/packages/private-apk-repos/). Additionally, if you're interested in customizing your Chainguard Containers by adding packages, we encourage you to check out our Chainguard's [Custom Assembly tool](/chainguard/chainguard-images/features/ca-docs/custom-assembly/).