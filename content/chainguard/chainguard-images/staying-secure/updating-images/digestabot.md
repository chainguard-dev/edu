---
title: "Keep your Chainguard Images Up to Date with digestabot"
linktitle: "Video: Up-to-date Images with Digestabot"
aliases:
- /chainguard/chainguard-images/videos/digestabot/
- /chainguard/chainguard-images/troubleshooting/digestabot/
lead: ""
description: "This video explains how to use digestabot, a free GitHub action we created to make it easier for public users to keep their Chainguard Images fresh."
type: "article"
date: 2024-02-07T15:21:01+00:00
lastmod: 2024-12-12T15:21:01+00:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 025
toc: true
---

{{< youtube 7WvzkwS9yms >}}

## Tools used in this video

* [digestabot](https://github.com/marketplace/actions/update-the-image-digest)

## Transcript

Today, I'd like to talk about a common question I get asked.

How can you keep images up to date while avoiding breaking changes?

The basic issue is that we'd like to make sure we're getting the latest security updates and features for our software.

But we really don't want our applications and infrastructure to break unexpectedly.

So there's a tension between updating all the time, which gives you the latest code and limits unexpected breakages.

In this example, we have a multi-stage Python build using Chainguard Images which are pinned to Digest.

Now, Digests are content-based hashes of images.

So if you reference an image by Digest, you will always get exactly the same image every time.

Now, this is fantastic for reproducibility.

As I know, if anybody uses this Dockerfile, they will get exactly the same images that I was using.

And this is especially important in Python, where if the version changes, so we go from Python 3.12 to Python 3.13, you might find that various libraries don't work until they're updated.

Now, how do you do updates then?

Well, you could manually go in and change, bump this Digest yourself.

But we've got a better solution for you that I want to talk about briefly today, and it's called Digestabot.

Digestabot is a GitHub action that can be set to run on a cron job and will open a PR when it detects there's a newer version of the image available.

You can then test the image to make sure it works with your application before merging the PR.

So for my example, it would check the Chainguard registry for the current digest of the latest tag and open a PR if it doesn't match the digest in the file.

We use Digestabot internally at Chainguard, and this pattern nicely balances the tension between keeping images up to date and vulnerability-free with the need to test and verify changes before shipping to production.

So please try it out and let me know if you have any questions.

## Relevant Resources
- [Reproducible Dockerfiles with Frizbee and Digestabot](https://edu.chainguard.dev/chainguard/chainguard-images/videos/digestabot_frizbee/) (Video)
- [Reproducibility and Chainguard Images](https://edu.chainguard.dev/chainguard/chainguard-images/videos/repro/) (Video)
- [Considerations for Keeping Images Up to Date](https://edu.chainguard.dev/chainguard/chainguard-images/recommended-practices/considerations-for-image-updates/) (Article)
- [Strategies and Tooling for Updating Container Images](https://edu.chainguard.dev/chainguard/chainguard-images/recommended-practices/strategies-tools-updating-images/) (Article)
