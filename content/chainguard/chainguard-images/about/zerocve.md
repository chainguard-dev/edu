---
title: "How Chainguard Creates Container Images with Low-to-No CVEs"
linktitle: "Video: Why Our Images Have Low-to-No CVEs"
aliases:
- /chainguard/chainguard-images/videos/zerocve/
- /chainguard/chainguard-images/about/zerocve/
lead: ""
description: "This video explains how Chainguard is able to create container images with low-to-no
CVEs."
type: "article"
date: 2024-05-31T12:21:01+00:00
lastmod: 2024-05-31T12:21:01+00:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 035
toc: true
---

{{< youtube Fuw9lYX6Ne8 >}}

## Tools and resources used in this video

* [Grype](https://github.com/anchore/grype)
* [Wolfi Secuirty Advisories](https://github.com/wolfi-dev/advisories)

{{< blurb/free-tier-message >}}

## Transcript

I sometimes get asked how Chainguard manages to create images with zero CVEs.

Sometimes people claim it's a trick or that we're cheating in some way.

It's absolutely not a trick and I'm going to explain in this video how we do it.

Now the first thing to be aware of is that our images work with majority of scanners and they will flag CVEs if they're present in our images.

So just to prove this I'm going to scan an old image.

So this is the flux Chainguard image and it's from I think around three months ago.

So in that time since it's been published it's accumulated CVEs and Grype will tell us that.

So in, I think it's around three months, it's accumulated three medium and 75 unknown CVEs.

So some of you are probably aware that there's issues at the NVD with classification at the minute which is why there's so many unknown CVEs which is a bit unfortunate.

It is telling me that they're fixed or 71 of them are fixed, meaning that if we update these APKs they will go away.

But yeah so that's an old image with CVEs.

If I compare it to the current image, "latest", I am hoping, yes, there's zero CVEs.

So hopefully this proves that scanners or Grype at least will report CVEs in Chainguard Images.

There are basically three things we do to address CVEs.

One we keep our images as small as possible.

By reducing the amount of software in an image to the absolute minimum required we reduce the amount of software there is to have a CVE in the first place.

Less packages means less vulnerabilities.

And we take this seriously.

Our production images don't even have a shell or package manager by default.

Two: we're really aggressive about keeping our software up-to-date.

So when an upstream project does a release we'll grab that immediately and typically have a new Wolfi package ready in four hours and a new container image shortly after.

And if there's one piece of advice I would give teams to avoid issues it's keep your software and dependencies up-to-date.

It really is the best way to avoid getting hit by known vulnerabilities.

It is a lot of work as things tend to break when you update things but it really is necessary work.

Between them those two points handle most cases.

But there is a third thing we do and it's a bit more specific to us and that is we issue security advisories.

Now a security advisory is basically a YAML file that gets picked up by scanners and provides them with more information on specific vulnerabilities.

So if we go back and look at some of the CVEs reported by Grype we see some specific to flux up here.

For example CVE-2024-24783 through to CVE-2024-24786.

So what we can do is we can go to the advisory website on Wolfi for flux and see what it says about those CVEs.

Okay so I'm on the advisories github project for wolfi-dev and we're looking at the flux advisories.

And what we see here is we've got an advisory for CVE-2023-39325 and what we're saying is we fixed that CVE and it's been fixed since package 2.1.2-r1.

So we might have pulled in a patch or we might have updated a release etc.

Got a very similar one here.

I think this was Rapid Reset by the way.

Here's another interesting one.

This time we're saying this CVE-2023-45283 is a false positive because this vulnerability only affects windows and this is a Linux package.

Same with this one and if we scroll down a bit we should get to, yeah, these are the CVEs that we saw in the output earlier and you can see when they've been fixed and which version they've been fixed in.

Aliases, so the CVE also goes by the github security advisory with this code.

And here we got an example of us picking up so we became aware that Grype had detected a vulnerability in one of our images on the 14th of March and we fixed it on the 16th of March and this is the version that it was fixed in.

This information is picked up by scanners and used to filter out the results so they're more accurate.

Okay so that's about it.

To recap the three things we do are one keep our images small, two keep our packages up-to-date and three when we have to we issue security advisories.

Hope that was helpful please let me know if you have any questions.
