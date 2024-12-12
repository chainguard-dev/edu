---
title: "Considerations for Keeping Images Up to Date"
linktitle: "Image Update Considerations"
aliases:
- /chainguard/chainguard-images/considerations-for-images-updates
type: "article"
description: "A conceptual article on best practices for keeping images up to date."
date: 2023-10-05T11:07:52+02:00
lastmod: 2023-10-11T11:07:52+02:00
draft: false
tags: ["CONCEPTUAL", "CHAINGUARD IMAGES", "PRODUCT"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 005
toc: true
---

It is essential to keep container images up-to-date in order to receive critical security updates and leverage new features. However, updates come with a risk: any time new code is introduced, there is a chance for breaking changes or other impacts on dependent systems.

Due to the complexity involved in modern containerized applications, there is no one-size-fits-all approach to keeping your container images up to date. With these conflicting approaches in mind, this article will explore how best to keep container images up-to-date.


## Understanding image versioning and naming conventions

Before discussing  image updates, it's helpful to have a baseline understanding of how images are typically versioned and named.

[*Semantic versioning*](https://semver.org/) — also known as "semver" — is a system for determining how version numbers are assigned to a given piece of software. Software using semver has versions numbered in the format of `X.Y.Z`. `X` is reserved for major versions that are backwards incompatible, `Y` is used for minor versions that are backward compatible, and `Z` is used for patches and bug fixes. As an example, for a piece of software with the version number `3.5.2`, `3` is the major version, `5` is the minor version, and `2` is the patch number.

Semantic versioning is intended to improve problems associated with having a large number of dependencies. Although semver has become a common practice throughout the software industry, it isn't used universally.

When referencing an image, it's important to know exactly what image you are working with. Docker uses the following format for image names.

```image
[host]/[repository][image_name][:tag]
```

For example, the full name for the [Chainguard Go Image](https://images.chainguard.dev/directory/image/go/versions?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-recommended-practices-considerations-for-image-updates), is `cgr.dev/chainguard/go:latest`.

Certain elements of this name format are optional in many cases. For instance, if you omit the hostname portion of an image name in either Docker or Kubernetes, both will default to using the public Docker registry.


## Automating updates

One solution to avoiding out-of-date container images would be to automate the process of updating images. This may be a system that scans a container registry for new versions of a given image and updates the application any time a new version of an image is released.

However, you will need to consider a few specific details around your particular software and organization's situation prior to fully automating container image updates, as you may run into issues with breaking changes upstream. You’ll want to think through the following:

* What is your risk appetite: is your software part of critical infrastructure or is its function of less urgent importance?
* What tests do you have in place? If you have confidence in your test suite, you may have a higher risk tolerance as you’ll trust that tests will fail and prevent broken images from going live.

You’ll also want to consider what exact version of an image you are updating, whether you are pinning to a digest to guarantee reproducibility, defaulting to a tag, or automating minor or patch version updates.

Even with safeguards in place, there is still a risk that at some point your application will use a version of an image it’s no longer fully compatible with, and you’ll need to have a plan in place to remedy this.

There are some tools that can automate some or all of the process of updating your images. One such example is [watchtower](https://github.com/containrrr/watchtower), which will update the running version of your app when an appropriately tagged image is pushed to a relevant registry. Additionally, there are [FluxCD](https://fluxcd.io/flux/guides/image-update/) and [Argo CD's Image Update tool](https://argocd-image-updater.readthedocs.io/en/stable/).

If you're going to use tools like these to automate image updates, it is a recommended that you have testing and monitoring in place. Monitoring, alerting, and logging support you and your organization in making the information you need for debugging, security-related analysis, and compliance requirements available while also keeping a history of relevant data.


## Be mindful about tagging practices

Developers will often create multiple variations of the same image. Sometimes these different images may represent distinct numbered versions of the image, or they may contain unique sets of packages. Typically, these different images in the same series will share a name and be stored in the same repository, but the developer will differentiate them by giving them different *tags*.

In the context of containers, a tag is a human-readable identifier associated with an image. These make it easier to distinguish between different versions of images within the same repository. Oftentimes, developers will pin their project to a specific tag. As an example, imagine a project that uses an image named `example_image` and it is pinned to version `1.9`, as in `cgr.dev/chainguard/example_image:1.9`. One day, version `2.0` is released, but the project developers choose not to upgrade, as doing so would introduce breaking changes.

There may be situations where different tags point to the same image. For example, the first version of an image named `sample_image` is released with the tag `1`. Later on, a minor version is released with the tag `1.2`, and then even later  patch is released with the tag `1.2.3`. In this case, the images tagged `1` and `1.2` would point to the same image as the one tagged `1.2.3`, since `1.2.3` is the latest patch of both these major and minor versions. Conversely, if the developer later decides to patch version `1.1` of the `sample_image` and tags it as `1.1.4`, the image tagged `1` will still point to `1.2.3`, as that's the latest iteration of the most recent minor version.

Many systems will default to using the `latest` tag in certain cases if you don't specify one. For example, if you use Docker to build an image but don't specify a tag, it will always default to tagging it with `latest`. There's a misconception that the `latest` tag always represents the most recent stable version of a given image. The normal convention is for the latest tag to point to the most up-to-date stable version of the image, but it is only a convention and not an enforced rule.

One of the most important features of container builds is their *reproducibility* as you would like to ensure that you are using the same image each time. However, container tags are mutable, meaning that they can change over time. If you pin your application to a specific image tag and then the image associated with that tag gets updated and you redeploy or pull the image again, your application will be using a different image than it was before. Eventually, the image could change to the point that it no longer works with your application.

When it comes to container versions, pinning an application to a major version is usually an acceptable practice since minor version increases typically won't break things. That being said, the potential for "jumping” across minor or major versions without warning means that pinning an application to a major or minor tag isn't suitable for many production workflows. To avoid this problem, it's recommended to [pin projects to an *image digest*](/chainguard/chainguard-images/how-to-use-chainguard-images/#pulling-by-digest). A digest is a content-based hash of the image contents and is guaranteed to be immutable. Because a digest will always point to the same image, its reproducibility is guaranteed. To find the digest for an image, users can run a command like the following.

```sh
docker images --digests cgr.dev/chainguard/wolfi-base
```
```
REPOSITORY                  	TAG   	DIGEST                                                                	IMAGE ID   	CREATED  	SIZE
cgr.dev/chainguard/wolfi-base   latest	sha256:490977f0fd3d8596d173839dbb314153797312553b43f6a24b0e341cf2e8d473   2606ed78c658   9 days ago   10.9MB
```

To clarify, using tags to keep your images may work for you and your organization. However, if you're concerned about ensuring reproducibility — or you just want more control over what images you're running — using digests can be a better approach for your situation.


## Recommendations

As mentioned in the previous section, image digests guarantee full reproducibility. For that reason, it's generally recommended that projects update their container images by digest whenever possible.

Of course, digests do come with their own drawbacks. Image digests are not human readable; unlike tags, you can't always tell the difference between two image digests with a quick visual scan. Digests also don't make it clear whether a digest represents an older version, or whether one digest is older than another. Combined, these factors mean that digests can make it more difficult to know whether an image is up to date.

[Chainguard Images](/chainguard/chainguard-images/) are rebuilt daily in order to ensure that they're kept up to date and include all the latest available security patches. We recommend adopting a development pattern where digests are used to identify Chainguard Images and are regularly updated by a bot, ensuring that the project and its downstream users benefit from reduced vulnerability counts, bug fixes, and new features. We do this ourselves with our [digestabot tool](https://github.com/chainguard-dev/digestabot).

As with the recommendation stated previously, Chainguard requires a human to approve the digestabot's update before it's deployed. Technically, we could set up an automatic approval for the bot's updates, but requiring a human approval combines the stability and reproducibility of using a digest with the good security hygiene of keeping images regularly updated.

There are many factors to consider when developing a process for keeping your images up to date, so you're unlikely to find useful advice on the subject beyond the general strategies outlined in this guide. Of course, different update strategies will work for different circumstances. Ultimately, whatever process you or your organization land on for keeping images up to date should suit the needs of your users without becoming a burden to you or your organization.


## Learn more

To reiterate, there's no one-size-fits-all approach to keeping one's images up to date. Our goal for this article is to introduce some of the important factors one should consider when developing a container image update plan for their application. If you'd like to learn more about the subjects touched on in this guide, we encourage you to check out the following resources.

* [How to Use Chainguard Images](/chainguard/chainguard-images/how-to-use-chainguard-images/)
* [How to Use Container Image Digests to Improve Reproducibility](/chainguard/chainguard-images/videos/container-image-digests/)
* [How To Compare Chainguard Images with chainctl](/chainguard/chainguard-images/comparing-images/)
