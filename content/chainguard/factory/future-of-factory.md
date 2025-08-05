---
title: "What is the future of the Chainguard Factory?"
linktitle: "Future of the Factory"
type: "article"
description: "Dustin Kirkland shares his vision for the future of the Chainguard Factory"
date: 2025-08-02T16:00:00+00:00
lastmod: 2025-08-02T16:00:00+00:00
draft: false
tags: ["Chainguard Factory", "Video", "Conceptual"]
images: []
menu:
  docs:
    parent: "chainguard-factory"
weight: 060
toc: true
---

{{< youtube eF9EYK6AKPA >}}

## Transcript

**Interviewer**: So what do you see as the future for the Factory?

**Dustin Kirkland**: Well, I'm not going to get into the super secret plans we have for next generation products, but I will tell you that we are constantly expanding the scope of the open source projects that we're building. So more and more packages—each of those show up as new packages that we're now able to add to our existing images or build new images around.

More and more images—there's a long list, a backlog of images that our customers have requested from us at Chainguard. We continue to expand that catalog from 1,300 to 1,400 to 1,500 images. We're growing by 50 to 100 images per month in that catalog. So even more packages, even more images, and more libraries too, for that matter.

We are adding Java packages that one would typically find and add using the Maven tool. More and more Python libraries that one would typically install using pip. We're building more and more of those from source and getting greater coverage. And it's not just the projects themselves, but more versions of those projects.

The fact that we can reproduce those builds means that we can apply patches. So we're fixing vulnerabilities and backporting fixes—CVEs that are fixed in latest versions—and now starting to backport some of those to older versions of those libraries.

And then in terms of the virtual machines form factor, super interesting that we can take any container image that we have and render that as a VM appliance, fully tested, fully qualified, running in various different environments. And we found some customers that just prefer to run some very specific workloads directly on the VM without a containerization layer.

So there's plenty of room to expand. The Factory gives us all of the power that we need to scale out the coverage across the open source ecosystem.

**Interviewer**: Excellent. And what about supply chain security in general? What do you see as the future there?

**Dustin Kirkland**: Yeah, so I mean, I think we've taken—very importantly, I think we've taken a key step in supply chain security by bootstrapping everything, building it from source, doing it well, doing it the right way, doing it all day every day, 24/7, 365, constantly. We don't snapshot the world and then attempt to backport patches to a version that just constantly drifts from where upstream is.

And that goes for compilers and toolchains, script interpreters, as well as the end applications, databases, and application frameworks. We're constantly rebuilding with exactly the same work that the upstream maintainers are using. And that fact, I think, is the important part. And what makes the rolling distro work for us is that we're matching the pace of upstream development here.