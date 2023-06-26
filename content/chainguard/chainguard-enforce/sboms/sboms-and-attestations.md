---
title: "SBOMs and Attestations in Chainguard Enforce"
linktitle: "SBOMs and Attestations"
aliases:
- /chainguard/chainguard-enforce/chainguard-enforce-kubernetes/sboms-and-attestations/
- /chainguard/chainguard-enforce/concepts/sboms-and-attestations/
type: "article"
description: "An overview of how Chainguard Enforce handles attestations and SBOMs"
date: 2023-03-19T15:56:52-07:00
lastmod: 2023-03-19T15:56:52-07:00
draft: false
tags: ["ENFORCE", "COSIGN", "SBOM", "CONCEPTUAL"]
images: []
menu:
  docs:
    parent: "concepts"
weight: 030
toc: true
---

In order to fully leverage the capabilities offered by Chainguard Enforce, it's important to establish a process for creating quality *Software Bills of Materials* (SBOMs). An [SBOM](/open-source/sbom/) is a formal record that contains the details and supply chain relationships (such as dependencies) of the components used in building software. Chainguard Enforce can capture SBOM data and use it to help you find images and packages in your ecosystem, as well as apply and enforce security policies to your runtime environments. To get the best results from these features, SBOMs should be attached to the images in your registry as signed attestations. 

[Cosign](/open-source/sigstore/cosign/an-introduction-to-cosign/)  — a part of the Sigstore project — supports software artifact signing, verification, and storage in an [OCI (Open Container Initiative)](/open-source/oci/) registry. The `cosign` command line tool offers two subcommands that you can use to associate an SBOM with a container image and then upload them to a registry: `cosign attach` and `cosign attest`. 

However, these commands don't work the same way, and Chainguard Enforce treats SBOMs that have been attached differently from those that have been attested. This guide outlines the differences between these two subcommands and provides guidance for when you might want to use one over the other.


## Comparison of attaching and attesting

The following table presents a high-level comparison of the `cosign attach` and `cosign attest` commands.

|   | `cosign attach` | `cosign attest` |
|----------|----------|----------|
| Produces an in-toto attestation (a "signed SBOM") | no  | yes  |
| SBOM can be ingested immediately | yes  | no  |
| SBOM requires policy for ingestion | no | yes  |
| Policies can be applied to SBOM | no | yes |
| Uploads OCI artifact to registry | yes | yes |
| OCI artifact extension | `.sbom` | `.att` |

The remaining sections of this guide elaborate further on the similarities and differences between these two commands.


## SBOMs vs. Attestations

An SBOM is essentially an electronic packing slip: it's a list of all the components that went into making a given piece of software. But unless you have some indication of when the software was produced, who produced it, and how it was produced, then you can't say with any certainty that the components listed in the SBOM are actually part of the software you're running.

An *attestation* allows the end users or consumers of a software artifact (in the context of this guide, an SBOM) to verify — independently of the producer — that the contents of the artifact haven't been changed since it was produced. It also requires software producers to provide verifiable proof of the quality of their software.

Put differently, an attestation is a written assurance of a software artifact's *provenance*, or the verifiable information about the artifact describing where, when, and how it was produced. You can think of an attestation as a proclamation that "software artifact X" was produced by "person Y" at "time Z".

Both `cosign attest` and `cosign attach` associate an artifact with an image and upload it to a registry. However, `cosign attest` generates an [in-toto attestation](https://in-toto.io/) while `cosign attach` does not. `cosign attest` then attaches it to the provided image and uploads it to a registry as an OCI artifact with a `.att` extension.

In the following example, `image.sbom` is an SBOM file that was previously created, `$IMAGE` is the image that will be attached to the SBOM, and `cosign.key` is the signer's private key.

```sh
cosign attest --key cosign.key --predicate image.sbom $IMAGE
```

Note that after creating an attestation, you can verify it with Cosign's `verify-attestation` subcommand.

```sh
cosign verify-attestation $IMAGE
```

`cosign attach`, on the other hand, only attaches an SBOM to an image and uploads it to a registry. In this case the SBOM isn't signed, meaning that Chainguard Enforce won't have any way to verify its authenticity.

```sh
cosign attach sbom --sbom image.sbom $IMAGE
```

This will upload the SBOM to the registry as an OCI artifact with a `.sbom` extension.

Be aware that there is also the `cosign sign` command. After running `cosign attach` to attach an SBOM and upload it to a registry, you can then run `cosign sign` to sign the SBOM, and upload the signature to the registry as a separate OCI artifact, this time with the `.sig` extension.


## Should I attest or attach?

Attestations are generally seen as being more trustworthy than unsigned SBOMs, because you can identify who signed them and when. However, Chainguard Enforce will not import the attestation data and begin using it (in other words, ingest the attestation) unless there is an active policy covering it. 

The reason for this is that if Enforce detects that an image has an attached attestation, then it will attempt to verify its signature by checking it against a policy. If it didn't do this, then Enforce would essentially be ingesting attestations without validating them, which defeats their purpose. Although the policy requirement for attestations generated by a `cosign attest` command is an extra step, this added security layer is often worth the peace of mind it brings.

Conversely, Chainguard Enforce will ingest attached SBOMs out of the box, but cannot apply policies against them. With that said, if you can trust with absolute certainty that an unsigned SBOM is accurate (say, if you yourself created and attached it to the image) or if you don't care about policy enforcement, then attaching SBOMs may suit your needs. 

Say you ran a `cosign attach` command to attach a `.sbom` artifact to an image and upload it to a registry. Then you ran `cosign sign` to sign the SBOM, generate a `.sig` artifact, and upload that to the registry. In this scenario, Chainguard Enforce would still see the SBOM as a `.sbom` artifact and not as an attestation (`.att`). Even though you've signed the SBOM, the signature is a separate artifact so Enforce cannot treat it as an attestation, and thus still won't be able to apply policies against it.


## A note on generating SBOMs

There are many tools available today — both proprietary and open source — that allow you to generate SBOMs. However, these tools do not generate SBOMs in the same way or at the same point in the development process. As with signed versus unsigned SBOMs, an organization may find SBOMs generated by one tool as more trustworthy than those from others. 

For example, SBOMs generated from source code can be valuable. But ultimately, you have no way of knowing whether the image has been tampered with between the time the SBOM was generated and the time you actually run the image. 

[apko](/open-source/apko/overview/) is a command-line tool that allows users to build container images using a declarative language based on YAML. When building a container image, apko will generate an SBOM outlining each of the apks it uses to build it. When combined with [melange](/open-source/melange/overview/), an apk builder tool that uses declarative pipelines to create apk packages, these tools can serve as a good starting point for a secure container image factory. Checkout ["Secure Your Software Factory with melange and apko"](https://www.chainguard.dev/unchained/secure-your-software-factory-with-melange-and-apko) to learn more.