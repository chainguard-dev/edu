---
title: "What are OCI Artifacts?"
type: "article"
description: "OCI Artifacts are a way of using OCI registries, or container registries that are compliant with specifications set by the Open Container Initiative, to store arbitrary files."
date: 2022-06-09T15:22:20+01:00
lastmod: 2022-06-09T15:22:20+01:00
draft: false
images: []
menu:
  docs:
    parent: "oci"
weight: 150
toc: true
---

[OCI artifacts](http://github.com/opencontainers/artifacts) are a way of using OCI registries, or container registries that are compliant with specifications set by the [Open Container Initiative](https://edu.chainguard.dev/open-source/oci/what-is-the-oci/), to store arbitrary files. While container registries were originally designed to store and distribute images, container engineers are increasingly using them to store non-container files such as Helm charts, Tekton bundles, and policy modules. By storing associated objects in the same infrastructure as containers, container engineers can consolidate their security and management efforts. Another benefit of using OCI registries is that provide a [content-addressable API](https://edu.chainguard.dev/open-source/oci/what-is-the-oci/#image-manifest), a way of referring to files that assures their authenticity and integrity.  

OCI artifacts are sometimes misunderstood as a new specification or format but they are in fact just a way of using the OCI Image Specification to store something other than an image in a container registry. The Image Specification requires a particular format for the [Image Manifest](https://edu.chainguard.dev/open-source/oci/what-is-the-oci/#image-manifest), and the inclusion of the specified OCI `mediaTypes` values `application/vnd.oci.image.config.v1+json` and `application/vnd.oci.image.layer.v1.tar+gzip` in the `config` and `layers` fields. To store an artifact using the Image Specification, you need to change the `mediaTypes` values in the `config` and `layers` fields as in the example manifest below.  

```json
{
  "schemaVersion": 2,
  // no top-level mediaType to indicate OCI
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


## OCI Artifacts and Software Supply Chain Security 
For software supply chain security, OCI artifacts offer a useful way to store [SBOMs](​​https://edu.chainguard.dev/open-source/sbom/what-is-an-sbom/) and signatures inside a container registry. 

An **SBOM**, or software bill of materials, is a formally structured list of libraries, modules, licensing, and version information that make up any given piece of software. When a vulnerability security advisory is issued, SBOMs enable software operators to quickly see whether their codebase contains any components associated with the vulnerability. A [**signature**](https://edu.chainguard.dev/open-source/sigstore/cosign/an-introduction-to-cosign/) is a way of verifying that you are the author of your software, and that it has not been tampered with by a third party. 

The open source tool [Cosign](https://github.com/sigstore/cosign), part of the [Sigstore](https://www.sigstore.dev/) project, enables container engineers to sign their images and artifacts and store them as an artifact in an OCI registry. You can also use Cosign to store SBOMs as artifacts in an OCI registry. To learn more about storing signatures as artifacts, visit the [section on counter signing](
https://github.com/sigstore/cosign#counter-signing) in the Cosign repo. To learn more about storing SBOMs as artifacts, visit the [section on signing SBOMs](https://docs.sigstore.dev/cosign/other_types/#sboms-software-bill-of-materials) in Sigstore’s documentation.  

 ## Considerations 
Community usage and guidance of OCI artifacts is actively evolving and there are a few things to keep in mind when using them. First, not all registries support artifacts, and the [OCI Image Specification](https://github.com/opencontainers/image-spec) recommends avoiding the use of artifacts if you are concerned about portability. Best practices are still also under debate, giving rise to the [OCI Reference Types Working Group](https://github.com/opencontainers/wg-reference-types), which is considering different ways of describing and handling objects stored in an OCI registry. You can read a more about the proposals the group is currently considering by visiting the [Intro to OCI Reference Types](https://www.chainguard.dev/unchained/intro-to-oci-reference-types) post on Chainguard’s blog. 
