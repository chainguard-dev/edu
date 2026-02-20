---
title: "Chainguard Containers Product Release Lifecycle"
linktitle: "Product Release Lifecycle"
aliases:
- /chainguard/chainguard-images/versions/
- /chainguard/chainguard-images/features/eol-notifications/
type: "article"
description: "Understanding Chainguard's approach to container image versions."
date: 2024-01-08T08:49:31+00:00
lastmod: 2025-11-28T06:30:00+00:00
draft: false
tags: ["Chainguard Containers"]
images: []
menu:
  docs:
    parent: "about"
weight: 025
toc: true
---

[Chainguard
Containers](https://images.chainguard.dev/?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement)
are able to offer few-to-zero known vulnerabilities because they are updated
frequently. Because of this continuous release cycle, the best way to mitigate
vulnerabilities is to use the newest build of each Chainguard Container
available. Chainguard keeps Containers up to date by doing one or more of the
following:

* Applying new releases from upstream projects
* Rapidly applying upstream patches to current releases — you can read more
  about this in our blog post, “[How Chainguard fixes vulnerabilities before
  they're
  detected](https://www.chainguard.dev/unchained/how-chainguard-fixes-vulnerabilities?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement)”
* Applying Chainguard patches to OSS software

Upstream projects are updated frequently for many reasons, including to combat
CVEs, and Chainguard ensures that the most up-to-date software is available in
all Chainguard Containers. Additionally, Chainguard often identifies CVEs and
other issues before scanners can detect them, so Chainguard may offer a patch to
a vulnerable dependency to support Chainguard Containers with few-to-zero
vulnerabilities.

The best way to mitigate vulnerabilities is to continually update to the latest
patched releases of software, but testing and updating can take time and effort.
To support flexibility and user choice, Chainguard aims to offer multiple
versions of a Chainguard Container that provide the lowest number of
vulnerabilities realistically possible.

This document provides an overview of Chainguard’s approach to updates,
releases, and versions within Chainguard Containers. For more specific guidance,
please [contact
us](https://www.chainguard.dev/contact?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement).

## How versions are maintained

Chainguard Containers are built on open source software, so understanding how
Chainguard manages releases starts with understanding how open source projects
version and release software. Generally, projects follow one of two approaches:

- **Multiple release track**: Popular open source
projects often provide maintenance for a number of release tracks concurrently.
For example, Java, Go, Postgres, and Kubernetes patch multiple release versions,
each on their own defined maintenance schedule. 
    - For these types of projects, Chainguard will maintain every version track of the
upstream software that receives updates from the project.
- **Single release track**: Many open source projects support only a single stream of releases that are
continuously incremented; often, this is simply the latest release. In the case
of a single release track, any security fix that is published will only be
applied to the most recent release of the project, and the project release tags
will be updated to indicate a new version is available. 
    - For this type of project, Chainguard only warrants that the latest release of
the software and its corresponding version tags have the most up-to-date patches
available.

In rare cases, a project may not follow a defined release pattern at all.

### Examples of what Chainguard supports and maintains for Chainguard Containers

There are several scenarios that define what Chainguard agrees to maintain
regarding software versions in the [Chainguard Containers
Directory](/chainguard/chainguard-images/how-to-use/images-directory/). All
container images that Chainguard currently supports are those with upstream
software that is still supported and maintained, and Chainguard patches and
rebuilds these Containers daily. If you have purchased a container image during
its lifecycle that is no longer being supported upstream, you will still be able
to access this Container, _but_ Chainguard will not be patching or rebuilding
this Container and it will start to accrue CVEs. It is recommended to upgrade to
an actively maintained version.

The table provides some example scenarios to help illustrate our approach.

| **Category**	| **Example** | **Maintained Upstream Releases** | **Chainguard Patches** | **Chainguard No Longer Patches** |
|---------------|-------------|----------------------------------|------------------------|----------------------------------|
| **Multiple Release Tracks** | [Go](https://images.chainguard.dev/directory/image/go/versions?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement)       | 1.23, 1.22                 | `:latest`, 1, 1.23, 1.22 | 1.23.old, 1.22.old, 1.21 and below |
|                             | [Python](https://images.chainguard.dev/directory/image/python/versions?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement)   | 3.13, 3.12, 3.11, 3.10, 3.9 | `:latest`, 3, 3.9 and above | 3.8 and below, 3.8.old, 3.9.old, 3.10.old, 3.11.old, 3.12.old |
|                             | [Postgres](https://images.chainguard.dev/directory/image/postgres/version?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement) | 17, 16, 15, 14, 13         | `:latest`, 17, 16, 15, 14, 13 | 12 (EOL November 21, 2024) and below |
| **Single Release Track**    | [Cosign](https://images.chainguard.dev/directory/image/cosign/versions?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement)   | 2                          | `:latest`, 2, 2.4 | 2.3, 2.2, 2.1, 2.0, 1.x, 0.x |
|                             | [Bank-Vaults](https://images.chainguard.dev/directory/image/bank-vaults/versions?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement) | 1 | `:latest`, 1 | Any previous version tag
| **No Release Track**        | [envoyproxy/ratelimit](https://images.chainguard.dev/directory/image/envoy-ratelimit/versions?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement) | No versioned releases | `:latest` | Any previous version tag |

> **Note**: The "Maintained Upstream Releases" column is current as of December 2024.

### Daily rebuilds and proactive patching

[Actively maintained](#list-active-tags) Chainguard Containers are rebuilt on a daily 
cadence, so you can be sure the container image you are using is up to date. 

In some 
cases, Chainguard will fix vulnerabilities in tools without waiting for the external 
project to release patches. Learn more about this under [Epoch tags](#epoch-tags).

## Versions available by tier

If you use [Chainguard Free
Containers](/chainguard/chainguard-images/about/images-categories/#starter-containers),
you will have access to the `:latest` version of any Container available to the
public. In some cases, you will also have access to the `:latest-dev` version,
which includes a shell and package manager. For example, the Python container
image has both `cgr.dev/chainguard/python:latest` and
`cgr.dev/chainguard/python:latest-dev`. Many of the programming languages have
these options available, including the Java JDK and JRE containers, PHP, Go,
Node, Ruby, and Rust.

If you use enterprise Chainguard Production Containers, you will have access to
more versions. The Chainguard approach is as follows:

* For **multiple-release track projects**, you will have access to major and
  minor versions that are actively maintained.
* For **single-release track projects**, you will receive the `:latest` tag as
  well as every versioned tag that is released over time.

### Floating tags and epoch tags

Chainguard Containers use *floating tags*. This means that a container image's
tag always points to the most recent build or version within a version stream,
rather than a fixed, immutable image. For example, `python:3.19` will always
point to the latest version of that version stream (`3.13.9`, as of this
writing), even if older tags like `3.13.8` and `3.13.7` are available.

### Epoch tags

Epoch tags provide a clear, human-readable way to track incremental updates to a
specific version of a container image, especially when changes are made to the
main package or for security fixes.

When upstream projects are slow to release fixes, Chainguard will sometimes
patch vulnerabilities directly rather than wait. For example, say there's a CVE
in Go 1.21.3 and the Go team is uncharacteristically slow releasing a fix.
Chainguard could patch 1.21.3 directly and release it as 1.21.3-r2, while
continuing to make the original available as 1.21.3-r1. Any further patches to
that version would increment the suffix to -r3, -r4, and so on. This suffix is
called the epoch number.

Chainguard may do this to patch vulnerabilities, remove unnecessary bloat,
rebuild the same source with newer tools, or address bugs in our build configs
and tooling. Epoch tags make it easy to track these incremental updates in a
clear, human-readable way — particularly useful when changes affect the main
package or involve security fixes.

**How epoch tags work**

Once a newer epoch tag is available, the previous one stops being updated. For
example, the tag `1.14.5-r3` will no longer be updated once `1.14.5-r4` is
available. Because Chainguard Containers are rebuilt frequently, this may not
always be apparent; a container image with these tags may show both as being
updated on the same day, when in fact `-r3` was updated only to be replaced
later in the day by `-r4`.

As mentioned previously, Chainguard Containers use floating tags. In the context
of epoch tags, this means that the minor version and patch will both always
point to the latest available epoch tag. For example, if the latest epoch tag
for Chainguard's `python` container image is `python:3.14.0-r6`, then
`python:3`, `python:3.14`, `python:3.14.0`, and `python3.14.0-r6` will all point
to the same container image. However, you could still specify `python:3.14.0-r5`
should you need.

**How epoch tags affect other packages**

Bear in mind that Chainguard's Containers, although minimal, will almost always
contain more than one package. At the time of writing this, the Go image has
more than 60 distinct packages in it, such as bash, busybox, git, glibc, make,
and zlib. When we fix a vulnerability in bash for example, we likewise ensure
that fix gets rolled out to every container image that includes bash, including
the `go:1.21.3` image. The image tagged `1.21.3-r2` will pull in that bash fix,
and fixes for any of the other packages in the image.

Put simply, when you opt in to pulling `go:1.21.3-r2`, you're opting in to a
consistent version of Go, and potentially floating versions of all the other
packages. This means you get CVE fixes as well as patch, and minor, and even
major version releases of bash, and every other package the image contains.

It's important to note that using epoch tags to "lock" to specific images is
discouraged, as even specific epoch tags can change over time and may introduce
breaking or functional changes. For true immutability, use [image
digests](/chainguard/chainguard-images/how-to-use/container-image-digests/)
instead.

You can learn more about our approach by reviewing our [blog on Chainguard's
container image tagging
philosophy](https://www.chainguard.dev/unchained/chainguards-image-tagging-philosophy-enabling-high-velocity-updates-pt-1-of-3?utm=docs).


## Wolfi Packages in Chainguard Containers

Chainguard Containers only contain packages that are either built and maintained
internally by Chainguard or packages from the [Wolfi
Project](https://github.com/wolfi-dev). These packages follow the same
conventions of minimalism and rapid updates as Chainguard Containers.

Starting in March of 2024, Chainguard will maintain one version of each Wolfi
package at a time. These will track the latest version of the upstream software
in the package. Chainguard will end patch support for previous versions of
packages in Wolfi. Existing packages will not be removed from Wolfi and you may
continue to use them, but be aware that older packages will no longer be updated
and will accrue vulnerabilities over time. The tools we use to build packages
and container images remain freely available and open source in Wolfi.

This change ensures that Chainguard can provide the most up-to-date patches to
all packages for our Containers customers. Note that specific package versions
can be made available in Production Containers. If you have a request for a
specific package version, please [contact
support](https://support.chainguard.dev?utm=docs).

## SLAs

A vulnerability and patch service-level agreement (SLA) is available for
Chainguard Production Containers. There are no SLAs available for Chainguard's
free tier of container images, but you will have access to frequently updated
and patched container images with low-to-zero CVEs.

If you are a Chainguard Production Containers user, Chainguard vulnerability and
patch SLAs apply only to supported and maintained versions of upstream projects
as clearly published by the upstream projects or published container images that
can be rebuilt using updated compilers and/or libraries. In the case of
single-release track projects, this means that the Chainguard vulnerability and
patch SLAs apply only to the latest version and corresponding version tags of
the upstream projects. Containers that use open source applications that have
reached their end of life are no longer patched.

## End of Life and End of Support software

When an open source application version is no longer maintained by the upstream
project or has otherwise met its end of life (EOL), Chainguard will generally no
longer provide patches to that software. While the Chainguard Production
Containers organization directory will continue to have previously purchased
container images available, new builds will no longer be published and
vulnerabilities are expected to accumulate in those Containers over time. It is
recommended to move to an up-to-date, actively maintained version.

For software applications that maintain multiple concurrent release tracks,
Chainguard will endeavor to provide [reasonable
notice](/chainguard/chainguard-images/features/eol-notifications/) when a
particular software release version is expected to reach EOL status, thus no
longer updated.

No EOL notice will be provided for single-release applications where the only
supported release is the `:latest` or corresponding version tag.


### EOL grace period

There are cases where an organization may want to continue using a container
image after it has reached end-of-life. This could be because an image reaches
EOL before the organization's release schedule, or perhaps later image versions
have one or more issues that prevent the organization from upgrading.

To help in situations like this, Chainguard offers an end-of-life grace period
for eligible Containers, allowing customers access to new builds of container
images whose primary package has entered its end-of-life phase for up to six
months after they have reached EOL. Refer to our [overview of the EOL Grace
Period](/chainguard/chainguard-images/features/eol-gp-overview/) for more
information.

## Inspecting the product release lifecycle

There are a number of ways that you can inspect and understand the version
lifecycle of your Chainguard Containers.

### List Active Tags

**Active tags in the Chainguard Console**

If you use Chainguard Production Containers, you can opt in to a feature that
allows you to view tag statuses in the Chainguard Console. In the Console under
**Images > Organization**, any images with active tags display `Active` in the
"Status" column. If you are not entitled to an image, its status is `Expired`.

Click into an image to see which of its tags are active. If a tag is no longer
being actively maintained, a "pause" icon will appear next to its name.

>**Note**: Use active tags to stay on a supported, continuously patched version,
>and use unique tags or digests when you need to pin deployments to an exact
>build for stability or compliance. Learn more in [Unique
>tags](/chainguard/chainguard-images/features/unique-tags/).

**List active tags with chainctl**

You can also use `chainctl` to retrieve the list of tags that are being actively
maintained for a Chainguard cointainer image by running:
```shell
chainctl image repo list
```

For instance, the following command lists the tags that are currently active for
`python`:

```sh
chainctl image repo list --repo=python -o json | jq -r '.items[].activeTags'
```
```output
[
  "3",
  "3-dev",
  "3.10",
  "3.10-dev",
  "3.10.19",
  "3.10.19-dev",
  "3.10.19-r2",
  "3.10.19-r2-dev",
  "3.11",
  "3.11-dev",
  "3.11.14",
  "3.11.14-dev",
  "3.11.14-r2",
  "3.11.14-r2-dev",
  "3.12",
  "3.12-dev",
  "3.12.12",
  "3.12.12-dev",
  "3.12.12-r2",
  "3.12.12-r2-dev",
  "3.13",
  "3.13-dev",
  "3.13.9",
  "3.13.9-dev",
  "3.13.9-r2",
  "3.13.9-r2-dev",
  "3.14",
  "3.14-dev",
  "3.14.0",
  "3.14.0-dev",
  "3.14.0-r8",
  "3.14.0-r8-dev",
  "3.9",
  "3.9-dev",
  "3.9.25",
  "3.9.25-dev",
  "3.9.25-r0",
  "3.9.25-r0-dev",
  "latest",
  "latest-dev"
]
```

### List Package Version Information

You can list the version information for packages that have multiple release
tracks with `chainctl package versions list`, which uses the [List Repos
API](/chainguard/api/spec/#/operations/Registry_ListRepos/).

The following `chainctl` command lists the active release tracks for the `python`
package:

```sh
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

This output also includes the date when the version will become EOL, as
well as the date after which it will no longer be covered by the EOL grace
period.

Refer to the [`chainctl`
documentation](/chainguard/chainctl/chainctl-docs/chainctl_packages_versions_list/)
for the full list of options that can be passed to the command.

### EOL Grace Period API

The [EOL Grace Period
API](/chainguard/chainguard-images/features/eol-gp-overview/#using-the-eol-grace-period-api)
provides lifecycle information about a Chainguard container image's tags.

For instance, the following snippet retrieves EOL data for the `python` image:

```sh
REPO_ID=$(chainctl images repos list --repo=python --parent=${ORGANIZATION} -o json | jq -r '.items[0].id')

curl -H "Authorization: Bearer $(chainctl auth token)" \
    "https://console-api.enforce.dev/registry/v1/eoltags?uidp.childrenOf=${REPO_ID}" \
    | jq '.'
```

This command will return output like the following:

```output
{
  "items": [
    ...
    {
      "id": "326bcde5903252f3ae2fe01c691b5a50f7046b5d/256c7780003faa0a/f37adb295422587a",
      "name": "3.10.16-r4-dev",
      "mainPackageName": "python",
      "tagStatus": "TAG_INACTIVE",
      "mainPackageVersion": {
        "eolDate": "2026-10-31",
        "exists": true,
        "fips": false,
        "legacyLts": "",
        "lts": false,
        "releaseDate": "2021-10-04",
        "version": "3.10",
        "eolBroken": false,
        "latestVersion": "",
        "versionSource": null
      },
      "graceStatus": "GRACE_ELIGIBLE",
      "gracePeriodExpiryDate": null
    },
    ...
  ]
}
```

This output tells you whether a tag is active, inactive (no longer being rebuilt
by Chainguard) whether it is eligible for an EOL grace period, and whether it is
currently within its grace period.

For full instructions on how to use the API and interpret its output, refer to
[our overview of the EOL grace
period](/chainguard/chainguard-images/features/eol-gp-overview/#using-the-eol-grace-period-api).

### Refer to endoflife.date

The [endoflife.date](https://endoflife.date) website lists the release tracks
and product lifecycles of many Open Source projects. Generally the information
on this site will align with the lifecycle of the corresponding Chainguard
image.
