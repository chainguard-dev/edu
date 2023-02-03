---
title: "Chainguard Images Version Policy"
type: "article"
description: "Maintenance policy for Chainguard Images Versions"
date: 2023-02-03T08:49:31+00:00
lastmod: 2023-02-03T08:49:31+00:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 420
toc: true
---

Our mission with Chainguard Images is to improve the security of the industry through a set of freely available container images that set the standard for provenance, minimalism, and low CVE counts.

As part of this mission we need to limit the maintenance cost of providing these images. For that reason, we limit the images available to anonymous and free-plan users. By requiring user registration, we can notify users of changes to images e.g. if a new version has been released which fixes a critical security vulnerability or when pulling an old version of an image that is leaving support imminently.  This allows us to safely concentrate our efforts on the latest versions of all our freely available images, and keep users from unknowingly depending on out of date, vulnerable dependencies.
Image versions available to anonymous users

Users who do not register will only be able to pull the `latest` tag and by digest.

## Image versions available to registered users

Users who register will have access to a greater range of tags. This will typically cover the last two minor versions of an image e.g. if the last two minor versions are `1.2.3` and `1.1.9`, the tags available would be:

- `latest`, `1.2.3`, `1.2`, `1` (all pointing to the same image)
- `1.1.9`, `1.1` (both pointing to the same image)

Often images will also provide an “edge” tag, representing release candidates or similar.

The exact tags available for an image should be made clear in the documentation for that image.

## What happens when an image tag leaves registered user availability?

When a new image version is released, old patch and minor versions will be deprecated. This will start a 30 day grace period, after which the image tag will be deleted. The image will remain pullable by SHA digest.

By registering, you can choose to receive notifications prior to deletion.

## Images available to subscribed users
Users can pay for a subscription providing access to older versions of images amongst other benefits. These images will be continuously rebuilt, so any software dependencies that aren’t part of the core package (such as OS components) will be kept up-to-date and vulnerability free. Please contact us regarding exact versions that are supported.

## When will this be enforced?
We will start requiring authentication to pull image tags on 24th April 2023.

## What about non-semver projects?

These will be documented on a case-by-case basis but should try to follow the same spirit i.e. supporting at least 2 versions.

## Why 2 minor versions?

For most packages we expect 2 minor versions to provide users with a reasonable window of time to upgrade to the latest supported version. This is not a hard rule. For example, in some instances we might support two major versions over a prolonged period to support a community through a long migration cycle. We will make these support decisions on an image by image basis.

