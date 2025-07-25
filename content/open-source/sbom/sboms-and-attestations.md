---
title: "The Differences between SBOMs and Attestations"
linktitle: "SBOMs and Attestations"
aliases:
- /chainguard/chainguard-enforce/chainguard-enforce-kubernetes/sboms-and-attestations/
- /chainguard/chainguard-enforce/concepts/sboms-and-attestations/
- /chainguard/chainguard-enforce/sboms/sboms-and-attestations/
type: "article"
description: "An overview of the differences between attestations and SBOMs"
date: 2023-03-19T15:56:52-07:00
lastmod: 2023-03-19T15:56:52-07:00
draft: false
tags: ["Cosign", "SBOM", "Conceptual"]
images: []
menu:
  docs:
    parent: "sbom"
weight: 030
toc: true
---

One of the first steps to improving your software supply chain security is to establish a process for creating quality *Software Bills of Materials* (SBOMs). An [SBOM](/open-source/sbom/) is a formal record that contains the details and supply chain relationships (such as dependencies) of the components used in building software.

[Cosign](/open-source/sigstore/cosign/an-introduction-to-cosign/) — a part of the Sigstore project — supports software artifact signing, verification, and storage in an [OCI (Open Container Initiative)](/open-source/oci/) registry. The `cosign` command line tool offers two subcommands that you can use to associate an SBOM with a container image and then upload them to a registry: `cosign attach` and `cosign attest`.

However, these commands don't work the same way. This guide outlines the differences between these two subcommands and provides guidance for when you might want to use one over the other.


## SBOMs vs. Attestations

An SBOM is essentially an electronic packing slip: it's a list of all the components that went into making a given piece of software. But unless you have some indication of when the software was produced, who produced it, and how it was produced, then you can't say with any certainty that the components listed in the SBOM are actually part of the software you're running.

An *attestation* allows the end users or consumers of a software artifact (in the context of this guide, an SBOM) to verify — independently of the producer — that the contents of the artifact haven't been changed since it was produced. It also requires software producers to provide verifiable proof of the quality of their software.

Put differently, an attestation is a written assurance of a software artifact's *provenance*, or the verifiable information about the artifact describing where, when, and how it was produced. You can think of an attestation as a proclamation that "software artifact X" was produced by "person Y" at "time Z". Because of this extra provenance information, attestations are generally seen as being more trustworthy than SBOMs since you can identify who signed them and when.

Both `cosign attest` and `cosign attach` associate an artifact with an image and upload it to a registry. However, `cosign attest` generates an [in-toto attestation](https://in-toto.io/) while `cosign attach` does not. `cosign attest` then attaches it to the provided image and uploads it to a registry as an OCI artifact with a `.att` extension.

In the following example, `image.sbom` is an SBOM file that was previously created, `$IMAGE` is the image that will be attached to the SBOM, and `cosign.key` is the signer's private key.

```sh
cosign attest --key cosign.key --predicate image.sbom $IMAGE
```

Note that after creating an attestation, you can verify it with Cosign's `verify-attestation` subcommand.

```sh
cosign verify-attestation $IMAGE
```

`cosign attach`, on the other hand, only attaches an SBOM to an image and uploads it to a registry. In this case the SBOM isn't signed, meaning that there's no way to confidently verify its authenticity.

```sh
cosign attach sbom --sbom image.sbom $IMAGE
```

This will upload the SBOM to the registry as an OCI artifact with a `.sbom` extension.

Be aware that there is also the `cosign sign` command. After running `cosign attach` to attach an SBOM and upload it to a registry, you can then run `cosign sign` to sign the SBOM, and upload the signature to the registry as a separate OCI artifact, this time with the `.sig` extension.

If you'd like to learn more about working with SBOMs and Cosign, we encourage you to checkout our tutorial on [How to Sign an SBOM with Cosign](/open-source/sigstore/cosign/how-to-sign-an-sbom-with-cosign/).


## A note on generating SBOMs

There are many tools available today — both proprietary and open source — that allow you to generate SBOMs. However, these tools do not generate SBOMs in the same way or at the same point in the development process. As with signed versus unsigned SBOMs, an organization may find SBOMs generated by one tool as more trustworthy than those from others.

For example, SBOMs generated from source code can be valuable. But ultimately, you have no way of knowing whether the image has been tampered with between the time the SBOM was generated and the time you actually run the image.

[apko](/open-source/apko/overview/) is a command-line tool that allows users to build container images using a declarative language based on YAML. When building a container image, apko will generate an SBOM outlining each of the apks it uses to build it. When combined with [melange](/open-source/melange/overview/), an apk builder tool that uses declarative pipelines to create apk packages, these tools can serve as a good starting point for a secure container image factory. Checkout ["Secure Your Software Factory with melange and apko"](https://www.chainguard.dev/unchained/secure-your-software-factory-with-melange-and-apko) to learn more.
