---
title: "Troubleshoot container and version availability"
linktitle: "Availability troubleshooting"
type: "article"
description: "When a container or version isn't available to you: how to identify which situation you're in, what to do about each, and when to open a support request."
date: 2026-09-02T00:00:00+00:00
lastmod: 2026-09-02T16:33:19+00:00
draft: false
tags: ["Chainguard Containers"]
images: []
menu:
  docs:
    parent: "about"
weight: 026
toc: true
---

You need a container image, or a particular version of one, and you can't pull it. The right next step depends on why it's missing, and there are four distinct reasons. This guide helps you tell them apart and resolve each one.

First, distinguish between the public container registry and your organization's registry:

* The [Chainguard Containers Directory](https://images.chainguard.dev/) at `images.chainguard.dev` is public. It lists every container image Chainguard builds, along with the tags, sizes, and metadata for each. Anyone can browse it.
* Your organization's registry at `cgr.dev/$ORGANIZATION/` holds only the images your organization has access to. This is what your teams pull from.

Browsing an image in the Directory doesn't mean your organization can pull it. For a fuller explanation of that distinction and how it relates to your subscription, see [Onboard your teams](/get-started/onboard-your-teams/).

## Find your situation

Look up the image in the Directory, then match what you see to the following table:

| What you find | Go to |
| --- | --- |
| The image is in the Directory, but the Console shows **Unavailable to organization**, **Add to organization for access**, or **Request image for access** | [The container isn't in your organization's catalog](#the-container-isnt-in-your-organizations-catalog) |
| The image isn't in the Directory at all | [Chainguard doesn't build the container](#chainguard-doesnt-build-the-container) |
| The image is in the Directory, but not the version you need | [The version you need isn't listed](#the-version-you-need-isnt-listed) |
| The version is listed with a pause icon, an **Expired** status, or an end-of-life date that has passed | [The version has reached end of life](#the-version-has-reached-end-of-life) |

## The container isn't in your organization's catalog

Chainguard builds the image, but your organization hasn't added it yet. What you do next depends on your subscription.

**Catalog customers.** A Catalog subscription covers the whole catalog, but only a subset of images is loaded into your organization's registry at any time. Administrators add more as teams need them. If you have the `owner` role, you can add the image yourself from the Console: go to **Images**, then click **Add image** on the **Organization** tab, or **Add to org** on the **Chainguard catalog** tab. The image appears in your catalog after a few minutes.

Self-serve adds require a role with the `repo (create, list, update)` capabilities, and the `registry.entitlement (list)` capability is useful for understanding what your organization is entitled to. The `owner` role is the only built-in role that carries all of them. For the full walkthrough and the role details, see [Chainguard container catalog pricing](/chainguard/containers/about/pricing/) and [Overview of roles and role-bindings](/platform/administration/iam-organizations/roles-role-bindings/roles-role-bindings/).

If you don't have the `owner` role, ask an administrator in your organization to add the image.

**Per-image customers.** A per-image subscription covers a specific licensed set of images rather than the whole catalog. You can browse everything in the Directory, but only your licensed images are permitted for builds, deployments, and production workloads. Ask your administrators to start a request; once they approve it, they add the image to your organization's registry.

Questions about what your organization is licensed for go to your account team, meaning the customer success manager or solutions architect assigned to your organization.

## Chainguard doesn't build the container

If the image doesn't appear in the Directory, Chainguard doesn't build it yet, and you can ask for it. Submit the request from the **Requests** section of the Chainguard Console, where you can also see what Chainguard is already building and upvote requests from other customers. Chainguard prioritizes requests by demand, so upvoting an existing request helps more than filing a duplicate.

Submitting requests requires membership in a [verified organization](/platform/administration/iam-organizations/verified-orgs/). The form asks for the resource type, the resource's existing public name, and a link to the upstream open source repository.

Some requests can't be fulfilled. Chainguard won't build resources from proprietary code, won't build projects that no longer receive upstream updates, and can't always produce a FIPS variant. For the full process and the current limitations, see [Requesting new Chainguard resources](/chainguard/containers/features/request-resources/).

## The version you need isn't listed

This is the most common case, and often the version you're asking for isn't the one you need. Before you request anything, it's worth understanding how Chainguard versions its container images, because that determines what's available.

### How Chainguard maintains versions

Chainguard actively maintains the latest patch release of each supported upstream version stream, not every patch that stream has ever released. If Python maintains 3.11, 3.12, and 3.13 upstream, Chainguard maintains all three streams; within each one, only the current patch is rebuilt. So `python:3.13` tracks the newest patch of the 3.13 stream, which was `3.13.9` when this was written.

Chainguard Containers also use *floating tags*. A tag points at the most recent build within its version stream rather than at a fixed image, so a tag's contents change as Chainguard rebuilds it. No tag stays pinned to one specific upstream patch release.

That combination explains most missing-version reports. If you need `7.79.2` and the stream has moved on to `7.80.1`, the supported path is the stream tag, which gives you that stream's latest patch with current security fixes applied. Requesting the older patch tag gets you an image that is no longer rebuilt and will accumulate CVEs.

Two related points follow from how tags float:

* A newer epoch tag supersedes the previous one. Once `1.14.5-r4` exists, `1.14.5-r3` stops being updated. Epoch tags aren't a locking mechanism.
* To list what's actually maintained for an image, run `chainctl image repo list --repo=$IMAGE -o json | jq -r '.items[].activeTags'`. See [Chainguard Containers product release lifecycle](/chainguard/containers/about/versions/) for more on tags, epochs, and how to inspect them.

### Pin to a specific build with a digest

If your reason for wanting a specific patch version is reproducibility, use a digest instead of a tag. A digest is a content-addressed reference to one exact build, and it never changes:

```shell
docker pull cgr.dev/$ORGANIZATION/node@sha256:ede7ef4ca485553f5313f7a02ad3537db1fe337079fc7cfb879f44cf709326db
```

Retrieve the digest for a tag with `crane`:

```shell
crane digest --full-ref cgr.dev/$ORGANIZATION/node:latest
```

A digest identifies one build and keeps identifying that same build even after the tag that pointed to it has moved on. Note the tradeoff: a pinned digest also stops receiving patches, so pair digest pinning with a process for updating the pin. See [Container image digests](/chainguard/containers/how-to-use/container-image-digests/) for the full workflow.

### If an actively maintained tag is missing from your organization

When the Directory shows a tag as actively maintained but that tag isn't available in your organization's registry, that's worth reporting. [Open a support request](#open-a-support-request) with the image name and the exact tag.

The Console makes the same point from the image's **Versions** tab. Below the tag table is a link labeled **Looking for older tags?**, which explains that only actively supported tags are available when an image is added to your organization, and asks you to try a supported tag before opening a request.

## The version has reached end of life

When an upstream project stops maintaining a version, Chainguard generally stops patching it. New builds are no longer published, and vulnerabilities accumulate in that version over time. Chainguard doesn't build or maintain end-of-life versions, so requesting one isn't a path forward. Move to an actively maintained version instead.

Chainguard also doesn't retroactively build versions that had already reached end of life before Chainguard began maintaining an image. If an upstream project released a version years before the image entered the catalog, that version was never built and can't be added.

### Check the end-of-life date

Use `chainctl` to see the end-of-life date and grace period end date for each release track:

```shell
chainctl package versions list python --show-active
```

```output
 VERSION |  EOL DATE  | EOL GRACE PERIOD END DATE
---------|------------|---------------------------
 3.10    | 2026-10-31 | 2027-05-01
 3.11    | 2027-10-31 | 2028-05-01
 3.12    | 2028-10-31 | 2029-05-01
 3.13    | 2029-10-31 | 2030-05-01
 3.14    | 2030-10-31 | 2031-05-01
```

The [endoflife.date](https://endoflife.date) website lists the release tracks and product lifecycles of many open source projects, and its information generally aligns with the lifecycle of the corresponding Chainguard container image. If the date you see from Chainguard differs from the one on the upstream project's own site, the two are probably using different definitions of a support tier.

Several signals tell you a version is no longer being rebuilt:

* In the Console, an inactive tag appears in gray text with a pause icon beside its name. Hovering the icon shows the message `This tag is no longer considered active.` [Open a support request](#open-a-support-request) if you want to request an inactive tag. Specify all the tags you need in a single request if requesting more than one to save time.
* On the **Organization** tab under **Images**, the **Status** column shows **Expired** for images your organization no longer has access to.
* The **Vulnerabilities** tab reports that a tag is no longer being scanned. Scanning stops because the image contents have stopped changing.

None of these mean the image was deleted. They mean the version has been superseded, and you should move to the current version of that stream.

### Continue past end of life with the EOL Grace Period

Sometimes you can't upgrade on Chainguard's schedule, whether because a version reaches end of life ahead of your release cycle or because a later version has a problem that blocks you.

For these cases, the End-of-Life Grace Period gives eligible containers up to six more months of new builds after the primary package reaches end of life. Eligibility depends on several requirements, and you can query grace period status through the Chainguard API. See the [EOL Grace Period overview](/chainguard/containers/features/eol-gp-overview/) for the requirements and the API.

## Open a support request

Open a support request when:

* An actively maintained tag appears in the Directory but is missing from your organization.
* A version isn't end of life upstream but doesn't appear in the Directory. Chainguard may not have it in the build matrix yet, or it may be a recent upstream release still moving through the build pipeline. Support can confirm whether a build is planned.
* A tag that used to be available in your organization has disappeared unexpectedly.

Include the image name, the exact tag you need, and the date you need it by. For the full list of what to include and the portal's prerequisites, see [Get support](/get-started/get-support/).

Questions about your subscription or entitlements, including whether a particular image is covered, go to your account team rather than the support portal.
