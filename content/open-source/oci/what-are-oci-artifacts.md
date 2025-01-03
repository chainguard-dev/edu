---
title: "What are OCI Artifacts?"
type: "article"
description: "OCI artifacts are a way of using OCI registries, or container registries that are compliant with specifications set by the Open Container Initiative, to store arbitrary files."
date: 2022-06-09T15:22:20+01:00
lastmod: 2022-06-09T15:22:20+01:00
draft: false
tags: ["OCI", "Conceptual"]
images: []
menu:
  docs:
    parent: "oci"
weight: 150
toc: true
---

OCI artifacts are a way of using OCI registries, or container registries that are compliant with specifications set by the [Open Container Initiative](/open-source/oci/what-is-the-oci/), to store arbitrary files. They are useful to understand given their growing importance for software supply chain security and their general utility for container engineering. However, community usage of OCI artifacts is still actively evolving and differing opinions and understandings of their purpose can lead to confusion. In this guide, you will learn the difference between OCI "artifacts" and "Artifacts," their utility for software supply chain security, and some important considerations when using them.

## OCI "artifacts" versus "Artifacts"
The term "OCI artifact" is a general purpose way of referring to any object stored within a container registry, but is most often used to refer to objects stored in registries that are not images. Container registries were originally designed to store and distribute images, but software engineers soon saw their utility for storing non-image objects such as Helm charts, Tekton bundles, and policy modules. By storing these objects in the same infrastructure as their containers, software engineers are able to consolidate their security and management efforts. Another benefit of using OCI registries for artifacts is that registries provide a [content-addressable API](/open-source/oci/what-is-the-oci/#image-manifest), or a way of referring to files (like images and artifacts) that assures their authenticity and integrity.

OCI artifacts are sometimes misunderstood as a new OCI specification or format but they are in fact a way of using the [OCI Image Specification](https://github.com/opencontainers/image-spec) to store something other than an image in a container registry. Some software projects use OCI registries to store non-images without making any formal changes to the object's manifest. However, the OCI does provide guidance for formally specifiying an object as an "OCI Artifact" (note the capital "A") by modifying its manifest in a particular way.

According to the OCI Image Specification, an [image manifest](/open-source/oci/what-is-the-oci/#image-manifest) needs to include the  OCI `mediaTypes` values `application/vnd.oci.image.config.v1+json` and `application/vnd.oci.image.layer.v1.tar+gzip` in the `config` and `layers` fields. When creating a manifest for an OCI **A**rtifact, however, you switch out both of these values with custom `mediaTypes` values as in the example below.

```json
{
  "schemaVersion": 2,
  "config": {
    "mediaType": "application/vnd.yourcustomartifact+json",
    "size": 233,
    "digest": "sha245:..."
  },
  "layers": [{
    "mediaType": "application/vnd.yourcustomartifact.tar.gzip",
    "size": 680,
    "digest": "sha245:..."
  }]
}
```

In the example manifest above, the  `config` field contains the custom `mediaType` value `application/vnd.yourcustomartifact+json` and the `layers` fields contains the custom `mediaType` value `application/vnd.yourcustomartifact.tar.gzip`.

Some container tools make use of the OCI Artifacts format guidelines (such as Helm and Tekton), but using these guidelines comes with a serious drawback. Not all registries support OCI Artifacts (or manifests with a custom `mediaType`), and the [OCI Image Specification](https://github.com/opencontainers/image-spec) recommends avoiding the use of Artifacts if you are concerned about portability. As you will read about in the section below, this lack of portability is a reason why some software projects choose to store artifacts in an OCI registry without adding a custom `mediaType` to the manifest.

## OCI artifacts and software supply chain security
For software supply chain security, OCI artifacts offer a useful way to store [SBOMs](/open-source/sbom/what-is-an-sbom/) and signatures inside a container registry.

An **SBOM**, or software bill of materials, is a formally structured list of libraries, modules, licensing, and version information that make up any given piece of software. When a security advisory is issued, SBOMs enable software operators to quickly understand whether their codebase contains any components associated with the vulnerability described in the advisory. A [**signature**](/open-source/sigstore/cosign/an-introduction-to-cosign/) is a way of attesting to the fact that you are the author of your software, and enables the consumer to verify that the signature and software have not been tampered with by a third party.

The open source tool [Cosign](https://github.com/sigstore/cosign), part of the [Sigstore](https://www.sigstore.dev/) project, enables software engineers to store their SBOMs and signatures as artifacts in the same container registry where they store their associated images. However, given the lack of support for OCI Artifacts across registries, Cosign ships all SBOM and signature artifacts as OCI Images and not as OCI Artifacts. In this way, software engineers can take advantage of Cosign regardless of whether their container registry supports the OCI Artifact manifest format or not.

To learn more about storing signatures as artifacts, visit the [section on counter signing](
https://github.com/sigstore/cosign#counter-signing) in the Cosign repo. To learn more about storing SBOMs as artifacts, visit the [Cosign SBOM Specification](https://github.com/sigstore/cosign/blob/b6aaddc05cbf04819221f9c7084399d4615b9d27/specs/SBOM_SPEC.md) page on Github or the [section on signing SBOMs](https://docs.sigstore.dev/cosign/signing/other_types/#sboms-software-bill-of-materials) in Sigstore’s documentation.

## Considerations
Community usage and guidance of OCI artifacts and Artifacts are actively evolving and there are a few considerations to keep in mind when you are planning on using them. As noted earlier, not all registries support OCI Artifacts, and the [OCI Image Specification](https://github.com/opencontainers/image-spec) recommends avoiding the use of them if you are concerned about portability. Recommended practices are still also under debate, giving rise to the [OCI Reference Types Working Group](https://github.com/opencontainers/wg-reference-types), which is considering different ways of describing and handling objects stored in an OCI registry. You can read a more about the proposals the group is currently considering by visiting the [Intro to OCI Reference Types](https://www.chainguard.dev/unchained/intro-to-oci-reference-types) post on Chainguard’s blog.
