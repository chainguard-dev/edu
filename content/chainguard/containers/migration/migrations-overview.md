---
title: "Overview of migrating to Chainguard Containers"
linktitle: "Migration overview"
aliases:
- /chainguard/migration/migrations-overview/
- /chainguard/migration-guides/migration-overview/
- /chainguard/migration/migration-overview/
- /get-started/migration/migrations-overview/
type: "article"
description: "Key differences, a recommended rollout strategy, and troubleshooting guidance for moving existing container workloads to Chainguard Containers."
date: 2024-07-22T12:56:52-00:00
lastmod: 2026-08-27T00:00:00+00:00
draft: false
tags: ["Chainguard Containers"]
images: []
menu:
  docs:
    parent: "migration"
weight: 010
toc: true
---

Chainguard Containers are minimal by design — most are [distroless](/chainguard/containers/getting-started-distroless/), with no shell or package manager. That keeps the attack surface small, but it also means moving an existing workload over usually requires adjusting how your image installs dependencies, which user it runs as, and what its entrypoint expects.

This guide covers the differences that matter during a migration, a recommended rollout strategy, and what to do when something breaks. For background on what Chainguard Containers are and how they are built, refer to the [Chainguard Containers overview](/chainguard/containers/overview/).

## Migration key points

* Most Chainguard Containers have no shell or package manager by default. This is great for security, but sometimes you need these things, especially in builder images. For those cases we have development container images (also known as `-dev` images, as in `cgr.dev/chainguard/python:latest-dev`) which do include a shell and package manager.
* The development variants and `wolfi-base` / `chainguard-base` use BusyBox by default, so any `groupadd` or `useradd` commands will need to be ported to `addgroup` and `adduser`.
* The free tier of Containers provides only the `:latest` and `:latest-dev` versions. Our paid Production Containers offer tags for major and minor versions.
* Chainguard Containers are [based on `glibc`](/chainguard/containers/concepts/glibc-vs-musl/) and our packages cannot be mixed with Alpine packages (which are instead based on musl).
* In some cases, the entrypoint in Chainguard Containers can be different from equivalent images based on other distros, which can lead to unexpected behavior. You should always check the image's specific documentation to understand how the entrypoint works.
* When needed, Chainguard recommends using a base image like `chainguard-base` or a development variant to install an application's OS-level dependencies.

Perhaps the best place for most users to get started with migrating to Chainguard Containers is by following our guide on [How to port a sample application to Chainguard Containers](/chainguard/containers/migration/porting-apps-to-chainguard/). This guide involves updating a sample application made up of three services to use Chainguard Containers. Although the application involved is fairly simple, the concepts outlined in the guide can also be useful for migrating more complex applications.

### Development containers

As mentioned previously, Chainguard's standard container images typically do not include a shell or package manager. This helps to minimize the size of containers and also reduces their potential attack surface, but many users find that they need images that include a shell or package manager to support their specific use case. For this reason, Chainguard offers development containers (also known as `-dev` variants, since their image tags are appended with `-dev`). These variants come with more tooling than our standard container images, including a shell and package manager.

Although development variants are still more secure than most popular container images based on other distros, for increased security on production environments we recommend combining them with a distroless variant in a multi-stage build.

Refer to our guide on [Chainguard's Container variants](/chainguard/containers/concepts/container-variants/) for more information on development containers.

### Full variants

For a number of our most popular Containers, Chainguard also offers *full* variants, whose tags are appended with `-full`. Unlike standard or development variants, full variants are designed to map to their upstream equivalent — typically the Debian-based image on Docker Hub — including the packages, environment variables, and entrypoint scripts that our minimal images omit. They exist primarily to ease migration: if your build or test pipelines depend on components from your previous image, starting with a full variant lets you adopt Chainguard Containers without untangling those dependencies first. Once you've migrated, we recommend moving to a slimmer variant that includes only what your workload needs.

Refer to our guide on [Chainguard's Container variants](/chainguard/containers/concepts/container-variants/#full-container-variants) for more information on full variants.

## Before migrating

Before you begin actively migrating to Chainguard Containers, review the images that your organization has access to and determine which teams and applications will be using each image. Notify the teams involved in the migration process so they can begin preparing. For teams that are new to Chainguard Containers, we recommend taking the online self-paced course, [Linky’s Guide to Chainguard Containers](https://courses.chainguard.dev/path/linkys-guide-to-chainguard-images).

Next, determine which users and/or systems are going to need access to your Chainguard registry in order to begin preparing access. Most customers will need to copy images from their Chainguard registry into their organization's registry. An easy way to do this is by configuring the organization's registry as a pull-through mirror of the Chainguard registry. We have a guide on [how to configure Artifactory](/chainguard/chainguard-registry/pull-through-guides/artifactory/artifactory-images-pull-through/) for this use case.

## Recommended rollout approach

When the goal is to migrate multiple deployments to Chainguard Containers, a major consideration is the strategy in which these container images are rolled out and deployed throughout your environment. The recommended rollout strategy for most customers is as follows:

* Start with less complex and non-critical applications to build confidence before migrating mission-critical workloads.
* Employ a gradual approach where you choose a small subset of container images and deploy those first to a non-production environment for testing and validation, and then to a small percentage of production instances and then gradually scale up.
* Use strategies like blue-green deployments or canary releases to introduce the updated container images gradually into production.

We understand that customers may have urgent timelines and need to accelerate Chainguard Container deployment by rolling out many images to a larger percentage of production simultaneously. For customers to be successful in this accelerated approach, we recommend the following:

* Have internal Chainguard Container champions identified and ready to lead and assist cross-functionally across teams.
* Your teams participating in the Chainguard Container migration should have the following technical skillset:
    * Familiarity with tools used to build images and run containers such as Docker CLI, Dockerfiles (including multi-stage builds), and orchestration platforms (Kubernetes, ECS, etc).
    * Experience using appropriate deployment security standards (such as the [Kubernetes Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)).
    * Experience debugging containers that have no shell.
* Review and understand concepts in the [Shared responsibility model](/chainguard/containers/concepts/shared-responsibility-model/).
* Your organization should already have a mature container strategy in place, including:
    * Mature and Established UAT and regression testing processes.
    * Automated CI/CD with permissions restrictions and auditing.
    * Monitoring, logging and runtime security.

Finally, as you plan for the migration to Chainguard Containers you should ensure there’s a clear rollback plan in case of unforeseen issues during migration. Keep the previous container image tagged and accessible for quick redeployment if necessary.

### Adding certificates

A common requirement for many customers is to add a company specific certificate or other security related content. The three most common ways to accomplish this are:

1. [Incert](/chainguard/containers/custom-assembly/incert-custom-certs/)
2. Dockerfile and `update-ca-certificates` utility
3. Dockerfile and java keytool

The process of adding or updating certificates, configuring APK repositories, and implementing other organization-specific customizations into an image is commonly known as creating a “Golden Image”. This approach enables these standard modifications to be applied once and then distributed across all teams, thereby reducing the risk of errors and minimizing friction during the migration process.

### Image type considerations

Many Chainguard customers use both application and base container images, but it often takes more time to migrate your applications to a base image in comparison to an application image due to the complexity of coordinating multiple teams, testing, and release schedules. We recommend starting with and migrating to application images first while your teams get trained and onboarded with base images.

#### Application images

When migrating to a [Chainguard Application Container](/chainguard/containers/concepts/container-categories/#application-containers) you should first check the image’s overview page on the [Containers  Directory](https://images.chainguard.dev) for usage details and any compatibility notes. There may be user, permissions, or volume path differences with the Chainguard Image that you should be aware of.

It is a best practice to use the same version of the Chainguard Application Image as what is currently running in your environment, if that version is available from Chainguard. Post-migration you should thoroughly test and monitor your application.

#### Base images

When migrating to a [Chainguard Base Container](/chainguard/containers/concepts/container-categories/#base-containers) you should first check the images’s overview page on the [Containers Directory](https://images.chainguard.dev) for usage details and any compatibility remarks. You should understand the libraries, runtime requirements, and operating system dependencies of the applications you plan to have running on the base image.

It is a best practice to use the same versions of any languages or applications that will be running on the Chainguard Base Container as what is currently running in your environment. Do not upgrade language or application versions at the same time that you migrate. Post-migration you should test and monitor your application as outlined below in Section 6.

If you need a package to use with your Chainguard Base Container, ChainguardOS packages are available using `apk`. Ensure you only use ChainguardOS packages, as Alpine APKs are not compatible with ChainguardOS. Additionally, it is important to note that vendor provided packages need to be [glibc](/chainguard/containers/concepts/glibc-vs-musl/) based and their functionality should be fully tested along with the application.

### Extending Chainguard Containers

You can take advantage of Chainguard's [Custom Assembly](/chainguard/containers/custom-assembly/overview/) and [Private APK repositories](/chainguard/containers/building-and-modifying/packages/private-apk-repos/) features to extend your container images

Custom Assembly allows users to create customers container images with extra packages added. This reduces their risk exposure by creating container images that are tailored to their internal organization and application requirements while still having few-to-zero CVEs.

Private APK Repositories, meanwhile, allow customers to pull secure apk packages from Chainguard. The list of packages available in an organization’s private repository is based on the apk repositories that the organization already has access to. For example, say your organization has access to the [Chainguard MySQL container image](https://images.chainguard.dev/directory/image/mysql/versions). Along with `mysql`, this image comes with other apk packages, including `bash`, `openssl`, and `pwgen`. This means that you'll have access to these apk packages through your organization's private APK repository, along with any others that appear in Chainguard container images that your organization has access to.

## Tips for migrating to Chainguard Containers

Although not fully comprehensive, it can be helpful to keep the following list of tips and strategies in mind when migrating to Chainguard Containers.

* Use development variants when you need a shell
* If necessary, install a different shell
* Use `apk search` to find the utilities needed by your application
* Beware of entrypoint differences between Chainguard Containers and their upstream counterparts
* Be aware that Chainguard Containers typically do not run as root by default
* If packages you need are missing, install them into a base image, preferably as part of a multi-stage build

Each of these tips and strategies are explained in greater detail in our guide on [Container migration tips](/chainguard/containers/migration/migration-tips/).

## Troubleshooting

The move to a distroless workflow can be confusing for both individual developers and larger teams. We recommend taking the following steps when you encounter issues as you begin using Chainguard Containers:

* **Debugging Distroless Container Images**: Debugging distroless images can be challenging due to the absence of a shell and package manager.
    * **Temporary Rebuild with `-dev` Tag**: Temporarily rebuild your image using the development variant to get a shell and other debugging tools. This is useful for local troubleshooting or in developer clusters.
        * Remember to remove the `-dev` tag before merging.
    * **Ephemeral Debug Containers**: In Kubernetes, use `kubectl debug` to launch an ephemeral container attached to the existing Pod for troubleshooting.
    * **Docker Debug**: While `docker debug` is available, it requires a Docker Desktop Pro license.
    * **`cdebug` and `kubectl debug`**: These tools allow you to enter a running container for debugging and can access the target container's file system.
    * **`chainctl images diff`**: This command allows you to compare two container images and identify differences between them.
* **General Troubleshooting Tips**:
    * Check the image's overview page in the [Containers Directory](https://images.chainguard.dev/) for specific usage details.
    * If you encounter issues, use a development image as a starting point.
    * Ensure you've replaced `apt install` or equivalent commands with `apk add`.
    * If elevated privileges are needed, use `USER root` before commands that require administrative access, then switch back to a non-root user before finalizing the image build.
    * Always check the image documentation for entrypoint details, as they may vary from other distributions. You can find entrypoint details in the [Specifications tab](https://images.chainguard.dev/directory/image/python/specifications) on any image's entry in the [Containers Directory](https://images.chainguard.dev/).

### Troubleshooting resources

To help with troubleshooting issues that can occur, Chainguard Academy has a guide on [Debugging distroless containers](/chainguard/containers/troubleshooting/debugging-distroless-images/).

Lastly, you might also find help in the [Chainguard Containers FAQs](/chainguard/containers/faq/).

## Migration resources

Once you have worked through the [sample application port](/chainguard/containers/migration/porting-apps-to-chainguard/#porting-key-points), the [Migration best practices and checklist](/chainguard/containers/migration/migration-checklist/) collects the steps worth running through before and during a rollout.

To automate Dockerfile migration, [The Guardener](/chainguard/guardener/dockerfile-migration/) is an AI-powered agent that iteratively converts, builds, and validates your Dockerfiles for use with Chainguard Containers.

Chainguard Academy groups the rest of its migration material into three sets:

* **[Migration guides](/chainguard/containers/migration/migration-guides/)** — language- and platform-specific guidance for Python, Node, PHP, .NET, Go, and Java.
* **[Compatibility guides](/chainguard/containers/migration/compatibility/)** — what changes when moving from Alpine, Debian, Red Hat, or Ubuntu.
* **[Getting started guides](/chainguard/containers/getting-started/)** — how to work with a specific Container, several with a sample application.

### Courses

Chainguard also offers a number of courses aimed to help teams understand and use Chainguard Containers.

#### Quickstart

* [Chainguard Containers Crash Course](https://courses.chainguard.dev/linkys-crash-course-on-chainguard-images): A quick overview of everything you need to know to get started ASAP.

#### Getting started (developer-focused)

* [Getting Started With Chainguard Containers](https://courses.chainguard.dev/path/linkys-guide-to-chainguard-images/getting-started-with-chainguard-images): Intro to everything you need to know - from basic setup to security scanning.
* [Foundations of Supply Chain Security](https://courses.chainguard.dev/path/linkys-guide-to-chainguard-images/foundations-of-software-supply-chain-security): The what, why, and how of keeping your software supply chain secure.
* [Migration guidance](https://courses.chainguard.dev/path/linkys-guide-to-chainguard-images/migration-guidance): Your friendly guide to moving to Chainguard Containers without the headaches.

#### Level up (next level courses)

* [Foundations of Supply Chain Security](https://courses.chainguard.dev/path/linkys-guide-to-chainguard-images/foundations-of-software-supply-chain-security): The what, why, and how of keeping your software supply chain secure.
* [Images! Images! Images!](https://courses.chainguard.dev/path/linkys-guide-to-chainguard-images/images-images-images): Become an image expert - from FIPS to SBOMs and everything in between.
* [Crush Your CVEs](https://courses.chainguard.dev/path/linkys-guide-to-chainguard-images/crush-your-cves): Master vulnerability management and keep your systems secure.

#### Running the show (admin courses)

* [Registry Rockstar](https://courses.chainguard.dev/path/linkys-guide-to-chainguard-images/registry-rockstar): Everything you need to know about managing access, identity, and registry setup.
* [Chainguard's Superstar Support](https://courses.chainguard.dev/path/linkys-guide-to-chainguard-images/chainguards-superstar-support): Get the most out of Chainguard's support resources and tools.

## Further reading

* [Overview of Chainguard Containers](/chainguard/containers/overview/)
* [How to use Chainguard Containers](/chainguard/containers/using-and-deploying/using-containers/)
* [How to transition to secure container images with new migration guides (Blog)](https://www.chainguard.dev/unchained/how-to-transition-to-secure-container-images-with-new-migration-guides)
* [Getting started with distroless containers](/chainguard/containers/getting-started-distroless/)
