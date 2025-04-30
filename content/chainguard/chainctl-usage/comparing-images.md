---
title: "How To Compare Chainguard Containers with chainctl"
linktitle: "Compare Images with chainctl"
aliases: 
- /chainguard/chainguard-images/comparing-images/
- /chainguard/chainguard-images/comparing-images/comparing-images/
- /chainguard/chainguard-images/using-the-image-diff-api
- /chainguard/chainguard-images/comparing-images/using-the-image-diff-api/
- /chainguard/chainguard-images/working-with-images/comparing-images/
- /chainguard/chainguard-images/how-to-use/comparing-images/
type: "article"
description: "An overview of how to use the chainctl images diff command to compare two Chainguard Containers."
date: 2023-08-30T11:07:52+02:00
lastmod: 2025-04-08T11:07:52+02:00
draft: false
tags: ["Chainguard Containers", "Product", ]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 080
toc: true
---

There may be times when you'd like to understand the difference between two Chainguard Containers. For example, you might want to know if there are any significant differences between yesterday's build and today's; or perhaps you want to know if any CVEs are present in a newer version of a custom container image.

[`chainctl`](/chainguard/chainctl/) — Chainguard's command line interface tool — allows you to directly compare two Chainguard Containers with its `images diff` feature. This guide outlines how to use the image diffing feature and highlights a few potential use cases for it.


## Prerequisites

In order to use the `chainctl images diff` subcommand, you'll need to have a few tools installed.

* You'll need `chainctl` installed on your local machine. Follow our guide on [How to Install chainctl](/chainguard/administration/how-to-install-chainctl/) to set this up. If you already have `chainctl` installed, be sure to update it to the latest version with `chainctl update`.
* Next, ensure you have Cosign installed. Our guide on [How to Install Cosign](/open-source/sigstore/cosign/how-to-install-cosign/) outlines several methods for installing Cosign.
* You'll also need Grype installed on your local machine, as `chainctl` uses this to scan the images when performing the diff. Follow the installation instructions for your operating system on the [Grype project GitHub repository](https://github.com/anchore/grype#installation).
* Lastly, an example command in this guide uses `jq` — a command-line JSON processor — to make the command's output more readable. You don't strictly need to have `jq` installed in order to use the `diff` subcommand, but if you'd like you can install it by following [the official documentation](https://jqlang.github.io/jq/download/).


## Using `chainctl images diff`

The `chainctl images diff` subcommand accepts the names of two Chainguard Containers as arguments and uses Grype to perform a vulnerability scan on each of them. It then retrieves both container images' SBOM information and outputs the difference between the two along with the previously obtained Grype data.

The `diff` subcommand follows this general syntax.

```sh
chainctl images diff $FROM_IMAGE $TO_IMAGE
```

As an example, try comparing the `latest` public `go` Chainguard Container with its `latest-dev` version.

```sh
chainctl images diff cgr.dev/chainguard/go:latest cgr.dev/chainguard/go:latest-dev | jq
```

This will return output like the following.

```
Fetching vulnerabilities for cgr.dev/chainguard/go@sha256:6fee3fff87854aa6e4762c7998c127436a68b09877f9c1010deca35e0f1e27bc
Fetching vulnerabilities for cgr.dev/chainguard/go@sha256:e62ce9fe5e62296186066e647d22cd8d16565d8eee9c2d18541094cec9ddd7a3
{
  "packages": {
    "added": [
      {
   	 "name": "sha256:e62ce9fe5e62296186066e647d22cd8d16565d8eee9c2d18541094cec9ddd7a3",
   	 "reference": "pkg:oci/index@sha256:e62ce9fe5e62296186066e647d22cd8d16565d8eee9c2d18541094cec9ddd7a3?mediaType=application%2Fvnd.oci.image.index.v1%2Bjson"
      },
      {
   	 "name": "sha256:a5910c192d3bd6e473cd98a0553d55dba1e9ddee240732a91bf4985116f893d0",
   	 "reference": "pkg:oci/image@sha256:a5910c192d3bd6e473cd98a0553d55dba1e9ddee240732a91bf4985116f893d0?arch=amd64&mediaType=application%2Fvnd.oci.image.manifest.v1%2Bjson&os=linux"
      },
      {
   	 "name": "sha256:35b2716760a4ec6652830a453d692cc7c55893eb8a6b4cc2afabc2bdfad2a10f",
   	 "reference": "pkg:oci/image@sha256:35b2716760a4ec6652830a453d692cc7c55893eb8a6b4cc2afabc2bdfad2a10f?arch=arm64&mediaType=application%2Fvnd.oci.image.manifest.v1%2Bjson&os=linux"
      }
    ],
    "removed": [
      {
   	 "name": "sha256:6fee3fff87854aa6e4762c7998c127436a68b09877f9c1010deca35e0f1e27bc",
   	 "reference": "pkg:oci/index@sha256:6fee3fff87854aa6e4762c7998c127436a68b09877f9c1010deca35e0f1e27bc?mediaType=application%2Fvnd.oci.image.index.v1%2Bjson"
      },
      {
   	 "name": "sha256:eaeb73fe40e46eabd28837f3b981791984fc40cac4833f872169f09c7c3cb4df",
   	 "reference": "pkg:oci/image@sha256:eaeb73fe40e46eabd28837f3b981791984fc40cac4833f872169f09c7c3cb4df?arch=arm64&mediaType=application%2Fvnd.oci.image.manifest.v1%2Bjson&os=linux"
      },
      {
   	 "name": "sha256:87d4c21ede568d79d4ca51271dda3bf46a4164be2bcd7405b6b85b49801d3504",
   	 "reference": "pkg:oci/image@sha256:87d4c21ede568d79d4ca51271dda3bf46a4164be2bcd7405b6b85b49801d3504?arch=amd64&mediaType=application%2Fvnd.oci.image.manifest.v1%2Bjson&os=linux"
      }
    ]
  },
  "vulnerabilities": {}
}
```

This command first uses Grype to scan each container image's vulnerability data and then retrieves both images' [SBOMs](/open-source/sbom/what-is-an-sbom/). It then outputs the differences that it finds between the two. This sample output indicates that compared to the `go:latest` container image, the `go:latest-dev` image has three packages added, three removed, and no unique vulnerabilities.

`chainctl`compares the images like this because of the order they appear in the command. If you reversed the order of the images in the example command, the packages shown as `added` and `removed` would also be flipped:

```
Fetching vulnerabilities for cgr.dev/chainguard/go@sha256:e62ce9fe5e62296186066e647d22cd8d16565d8eee9c2d18541094cec9ddd7a3
Fetching vulnerabilities for cgr.dev/chainguard/go@sha256:6fee3fff87854aa6e4762c7998c127436a68b09877f9c1010deca35e0f1e27bc
{
  "packages": {
    "added": [
      {
   	 "name": "sha256:6fee3fff87854aa6e4762c7998c127436a68b09877f9c1010deca35e0f1e27bc",
   	 "reference": "pkg:oci/index@sha256:6fee3fff87854aa6e4762c7998c127436a68b09877f9c1010deca35e0f1e27bc?mediaType=application%2Fvnd.oci.image.index.v1%2Bjson"
      },
      {
   	 "name": "sha256:eaeb73fe40e46eabd28837f3b981791984fc40cac4833f872169f09c7c3cb4df",
   	 "reference": "pkg:oci/image@sha256:eaeb73fe40e46eabd28837f3b981791984fc40cac4833f872169f09c7c3cb4df?arch=arm64&mediaType=application%2Fvnd.oci.image.manifest.v1%2Bjson&os=linux"
      },
      {
   	 "name": "sha256:87d4c21ede568d79d4ca51271dda3bf46a4164be2bcd7405b6b85b49801d3504",
   	 "reference": "pkg:oci/image@sha256:87d4c21ede568d79d4ca51271dda3bf46a4164be2bcd7405b6b85b49801d3504?arch=amd64&mediaType=application%2Fvnd.oci.image.manifest.v1%2Bjson&os=linux"
      }
    ],
    "removed": [
      {
   	 "name": "sha256:e62ce9fe5e62296186066e647d22cd8d16565d8eee9c2d18541094cec9ddd7a3",
   	 "reference": "pkg:oci/index@sha256:e62ce9fe5e62296186066e647d22cd8d16565d8eee9c2d18541094cec9ddd7a3?mediaType=application%2Fvnd.oci.image.index.v1%2Bjson"
      },
      {
   	 "name": "sha256:a5910c192d3bd6e473cd98a0553d55dba1e9ddee240732a91bf4985116f893d0",
   	 "reference": "pkg:oci/image@sha256:a5910c192d3bd6e473cd98a0553d55dba1e9ddee240732a91bf4985116f893d0?arch=amd64&mediaType=application%2Fvnd.oci.image.manifest.v1%2Bjson&os=linux"
      },
      {
   	 "name": "sha256:35b2716760a4ec6652830a453d692cc7c55893eb8a6b4cc2afabc2bdfad2a10f",
   	 "reference": "pkg:oci/image@sha256:35b2716760a4ec6652830a453d692cc7c55893eb8a6b4cc2afabc2bdfad2a10f?arch=arm64&mediaType=application%2Fvnd.oci.image.manifest.v1%2Bjson&os=linux"
      }
    ]
  },
  "vulnerabilities": {}
}
```

Be aware that because this is a relatively new feature, the format of the `diff` subcommand's output is subject to change.


## Potential use cases

Being able to find the exact difference between two Chainguard Containers with a single command allows users to make more informed decisions about what container images they use in their applications. This section goes over a couple scenarios where you may want to use the `chainctl images diff` command.

One potential use case for why you would want to find the differences between two Chainguard Containers is that you're curious about the differences between available release versions. Say you're using Custom Chainguard Containers and your application is pinned to a specific version of `go`. By diffing the two container images, you could check what vulnerabilities you could remove by updating to the next patch or minor version.

Another potential use could be in cases where you're interested in knowing the difference between a Chainguard Container's daily builds. For example, say you'd like to keep your images updated but only when there are significant changes between daily builds. You could diff between the running versions and the latest builds, only updating if there’s a meaningful difference.


## Learn more

To learn more about the `chainctl image` subcommands, we encourage you to check out our
[`chainctl` command resources](/chainguard/chainctl/chainctl-docs/chainctl_images/). You can also explore the rest of our [Chainguard Containers resources](/chainguard/chainguard-images/) to learn more about how images can help you keep your software secure by default.
