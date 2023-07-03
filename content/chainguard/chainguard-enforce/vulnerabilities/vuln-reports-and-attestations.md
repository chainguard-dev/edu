---
title: "Vulnerability reports and Attestations in Chainguard Enforce"
linktitle: "Vulnerability reports and Attestations"
aliases:
- /chainguard/chainguard-enforce/chainguard-enforce-kubernetes/vuln-reports-and-attestations/
- /chainguard/chainguard-enforce/concepts/vuln-reports-and-attestations/
type: "article"
description: "An overview of how Chainguard Enforce handles attestations of vulnerability reports"
date: 2023-03-19T15:56:52-07:00
lastmod: 2023-03-19T15:56:52-07:00
draft: false
tags: ["Enforce", "Cosign", "Vulnerability", "Conceptual"]
images: []
menu:
  docs:
    parent: "concepts"
weight: 030
toc: true
---

In order to fully leverage the capabilities offered by Chainguard Enforce, it's important to establish a process for generating quality vulnerability reports.
A vulnerability report lists all the discovered vulnerabilities contained in your software. Vulnerability scanning tools can use [SBOMs](/open-source/sbom/) to search for vulnerabilities that match the packages used to build your application.
Chainguard Enforce can ingest vulnerability reports and use their data to help you find vulnerabilities in  packages within your application's software ecosystem. It can also apply and enforce security policies for your runtime environments that take vulnerability data into account.
To get the best results from these features, vulnerability reports should be attached to the images in your registry as signed attestations. To create and attach reports to your images, you will need the following tools:

[Cosign](/open-source/sigstore/cosign/an-introduction-to-cosign/), which is a part of the Sigstore project, supports software artifact signing, verification, and storage in an [OCI (Open Container Initiative)](/open-source/oci/) registry.
The `cosign` command line tool offers the `cosign attest` subcommand, which you can use to attach a vulnerability report with a container image and then upload them to a registry.

* [Grype](https://github.com/anchore/grype), which is a vulnerability scanner for container images and filesystems.

This guide outlines how to use `cosign` and `grype` to generate, upload, and verify a cosign vulnerability attestation.

## Cosign Vulnerability Attestations

An *attestation* allows the end users or consumers of a software artifact (in the context of this guide, a vulnerability report) to verify that the contents of the artifact haven't been changed since it was produced. Importantly, this verification is done independently of the producer and requires software producers to provide verifiable proof of the quality of their software.

Put differently, an attestation is a written assurance of a software artifact's *provenance*, or the verifiable information about the artifact describing where, when, and how it was produced. You can think of an attestation as a proclamation that "software artifact X" was produced by "person Y" at "time Z".

The `cosign attest` command associates an artifact with an image and uploads it to a registry. It generates an [in-toto attestation](https://in-toto.io/), attaches it to the provided image, and uploads it to a registry as an OCI artifact with a `.att` extension.

In the following example, `grype` is used to generate a vulnerability scan report.

```sh
grype $IMAGE -o json > vuln-image-grype.json
```

* `vuln-image-grype.json` is a vulnerability report file that details the vulnerabilities discovered for `$IMAGE` in a custom Grype's JSON format.
* `$IMAGE` is the image that will be associated with the vulnerability report.

Following the vulnerability cosign attestation [specification](https://github.com/sigstore/cosign/blob/main/specs/COSIGN_VULN_ATTESTATION_SPEC.md), the results
from the scanner must be added to the predicate section `result: ` defined in the specification.
The following file, named as `vuln-image-grype.predicate`, contains an example of the content of a predicate for a vulnerability attestation.

```json
{
    "invocation": {
      "parameters": [],
      // [ "-o json" ]
      "uri": "",
      // https://github.com/chainguard-dev/actions/actions/runs/201231231
      "event_id": "",
      // 201231231
      "builder.id": ""
      // GitHub Actions
    },
    "scanner": {
      "uri": "",
      // pkg:github/anchore/grype@3865f4cc1dfcdcefbb7009400df153f24b18c772
      "version": "",
      // 0.62.3
      "result": {} // USE the content of `vuln-image-grype.json` here.
    },
    "metadata": {
      "scanStartedOn": "",
      // 2023-06-27T18:45:50.52Z
      "scanFinishedOn": ""
      // 2023-06-27T18:47:50.52Z
    }
}
```

Next use cosign to attest the predicate content with a vulnerability type using `cosign.key`, which is the signer's private key.

```sh
cosign attest --key cosign.key --type vuln --predicate vuln-image-grype.predicate $IMAGE
```

Note that after creating an attestation, you can verify it with cosign's `verify-attestation` subcommand.

```sh
cosign verify-attestation $IMAGE
```

This will upload the vulnerability attestation to the registry as an OCI artifact with a `.att` extension.
