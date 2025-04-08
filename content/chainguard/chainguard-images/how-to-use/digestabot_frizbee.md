---
title: "Reproducible Dockerfiles with Frizbee and Digestabot"
linktitle: "Reproducible Dockerfiles"
aliases:
- /chainguard/chainguard-images/videos/digestabot_frizbee/
- /chainguard/chainguard-images/how-to-use/digestabot_frizbee/
lead: ""
description: "How to avoid issues with flaky Dockerfiles by using Frizbee and Digestabot to pin images to digests."
type: "article"
date: 2024-06-07T12:21:01+00:00
lastmod: 2024-06-07T12:21:01+00:00
draft: false
tags: ["Chainguard Containers", "Product", "Video"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 040
toc: true
---

{{< youtube FfZZVZ-V5ho >}}

## Tools

* [Frizbee](https://github.com/stacklok/frizbee)
* [Digestabot](https://github.com/chainguard-dev/digestabot)

## Transcript

I'd like to talk about a problem I faced with container builds in the past and a potential solution.

So basically, the problem is you rerun your Docker build, or you reapply your Kubernetes YAML, and it no longer works, even though it was perfectly fine the last time.

And it's because the images your configuration is pointing to have changed, i.e. you're now pulling different versions of the images.

Now, I hit this most when I come back to a project after a few months, but it can really happen at any point.

Now, let's take a look at an example so we can really understand what I'm talking about.

OK, so I have a Dockerfile here, and at the moment, it's broken.

It does build, but if I run it, we get an error.

And the reason is that the version of Python has changed since it was first built.

So if we look at the Dockerfile, we can see it's a multi-stage build, where the build step is using this `latest-dev` tag.

So that's a completely up-to-date image with build tool inside it.

But the runtime part uses this Python tag, Python `latest` at a specific digest, which in this case refers to an image from a few months ago.

Now, if we change this to use the current `latest`, rebuild it, and run it, it does work.

But because both images are the latest versions, they can change at any point and break again.

And if someone else runs this build, there's no guarantee that it's going to work.

What we should really do is pin both images to digests that we know will work together.

And to demonstrate that, I'm going to use this frizbee tool from StackLock.

So if I run frizbee on an image, it will go to the registry and ask for the current digest for a tag and update the Dockerfile with the new tag.

So if I run `frizbee image -n` to say dry run, and then `Dockerfile`, which is the file we're interested in, we can see what it's done here.

And our `latest-dev` now has this SHA hash, which is the current SHA hash of the `latest-dev` image.

And our Python latest has changed to this SHA hash.

So that's perfect.

You know these two images will work together.

And we can output this and build it again.

And this should run.

Let's just call it the same thing.

Yes.

OK.

So now I have a Dockerfile with exact image versions that I know will work.

But even better, the Python dependencies are specified in this `requirements.txt` file.

And they have exact versions.

So I'm actually pretty confident that if I come back to this build in, say, a year's time, it's still going to work, with the assumption that the images and the packages are still available to be downloaded.

Now, you don't want to be running versions of software that are a year out of date in production, obviously, as you're going to find you're missing important security updates, and your scanners, and maybe even your security team are going to start shouting at you.

So you need to update and test your Dockerfile periodically.

Now, you can script a solution with Frizbee, but there's also Digestabot from Chainguard.

So Digestabot is a GitHub action that will run regularly and open a PR to update your image references if it finds they're out of date.

What both of these options give you is a high level of reproducibility, along with a simple update mechanism that gives you control over how and when changes are applied.

So please take a look at Frizbee and at Digestabot, and let me know how you get on.
