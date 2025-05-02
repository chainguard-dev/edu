---
title: "An Introduction to Rekor"
linktitle: "Introduction"
type: "article"
lead: "The Rekor transparency log"
description: "Understanding Rekor, the transparency log of Rekor"
date: 2022-08-20T08:49:31+00:00
lastmod: 2022-08-20T08:49:31+00:00
draft: false
tags: ["Rekor", "Overview"]
images: []
menu:
  docs:
    parent: "rekor"
weight: 001
toc: true
---

_An earlier version of this material was published in the [Rekor chapter](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/block-v1:LinuxFoundationX+LFS182x+2T2022+type@sequential+block@e785fae1be184e2c929db62dbe7444fa/block-v1:LinuxFoundationX+LFS182x+2T2022+type@vertical+block@a48c33126e2c4ee6ad3bfa6b7bc9c957) of the Linux Foundation [Sigstore course](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/home)._

Rekor stores records of artifact metadata, providing transparency for signatures and therefore helping the open source software community monitor and detect any tampering of the software supply chain. On a technical level, it is an append-only (sometimes called “immutable”) data log that stores signed metadata about a software artifact, allowing software consumers to verify that a software artifact is what it claims to be. You could think of Rekor as a bulletin board where anyone can post and the posts cannot be removed, but it’s up to the viewer to make informed judgements about what to believe.

## Transparency log

Rekor’s role as a _transparency log_ is the source of its security benefits for the software supply chain. Because the Rekor log is tamper-evident — meaning that any tampering can be detected — malicious parties will be less likely to tamper with the software artifacts protected by sigstore.

In order to detect tampering, we can use _monitors_ — software that examines the Rekor log and searches for anomalies — to verify that nothing has been manipulated outside of standard practices. Additionally, downstream users can search Rekor for signatures associated with signed artifact metadata, can verify the signature, and can make an informed judgment about what security guarantees to trust about a signed artifact.

The Fulcio certificate authority enables a downstream user to trust that a public key associated with a particular artifact metadata entry from Rekor is associated with a particular identity, and Cosign performs this verification with a single convenient command.

## Public instance of Rekor

A public instance of Rekor is run as a non-profit, public good transparency service that the open source software community can use. The service lives at [https://rekor.sigstore.dev/](https://rekor.sigstore.dev/). Those who are interested in helping to operate or maintain the Rekor public instance, or those who would like to discuss a production use case of the public instance can reach out via the [mailing list](https://docs.sigstore.dev/about/contributing/#mailing-list).

The latest Signed Tree hashes of Rekor are published on Google Cloud Storage. These are stored in both unverified raw and verified decoded formats; the signatures can be verified by users against Rekor’s public key. Entries include a short representation of the state of Rekor, which is posted to GCS, and can be verified by users against Rekor's public key. These representations can be used to check that a given entry was in the log at a given time.

## Rekor usage

Rekor provides a restful API based server for validation and a transparency log for storage, accessible via a command-line interface (CLI) application: `rekor-cli`. You can install `rekor-cli` with Go, which we will discuss in the lab section below. Alternatively, you can navigate to the [Rekor release page](https://github.com/sigstore/rekor/releases) to grab the most recent release, or you can build the [Rekor CLI manually](https://docs.sigstore.dev/logging/installation/#build-rekor-cli-manually).

Through the CLI, you can make and verify entries, query the transparency log to prove the inclusion of an artifact, verify the integrity of the transparency log, or retrieve entries by either public key or artifact.

To access the data stored in Rekor, the `rekor-cli` requires either the log index of an entry or the universally unique identifier (UUID) of an artifact.

The log index of an entry identifies the order in which the entry was entered into the log. Someone who wants to collect all the log entries or perhaps a large subset of the entries might use the log index, and receive an object as below, in their standard output.

```
LogID: c0d23d6ad406973f9559f3ba2d1ca01f84147d8ffc5b8445c224f98b9591801d
Index: 100
IntegratedTime: 2021-01-19T19:38:52Z
UUID: 2343d145e62b1051b6a2a54582b69a821b13f31054539660a020963bac0b33dc
Body: {
  "RekordObj": {
    "data": {
      "hash": {
        "algorithm": "sha256",
        "value": "bf9f7899c65cc4decf96658762c84015878e5e2e41171bdb39e6ac39b4d6b797"
      }
    },
    "signature": {
      "content": "LS0tL…S0=",
      "format": "pgp",
      "publicKey": {
        "content": "LS…0tLS0="
      }
    }
  }
}
```

The `RekordObj` is indicated inside the body field, and is one of the standard formats used by Rekor to indicate a digital signature of an object. The signature in this entry was generated via PGP, a traditional method of creating digital signatures, sometimes also used to sign code artifacts. Many other digital signature types are accepted. The signature block contains content fields that are base64-encoded, a form of encoding that enables reliably sending binary data over networks.

There are a number of different formats stored in the Rekor log, each associated with a particular type of artifact and use case.

Users of Rekor also have an offline method for determining whether a particular entry exists in a Rekor log by leveraging inclusion proofs, which are enabled through Merkle trees. Merkle trees are a data structure that enable a party to use cryptographic hash functions — a way of mapping potentially large values to relatively short digests — to prove that a piece of data is contained within a much larger data structure. This proof is accomplished by providing a series of hashes to the user, hashes that if recombined prove to the user that an entry is indeed in the Rekor log. Sigstore users can “staple” such an inclusion proof to an artifact, attaching the inclusion proof next to an artifact in a repository, and therefore proving that the artifact is indeed included in Rekor. For a detailed description of Merkle trees and inclusion proofs, refer to the “helpful resources” section at the end of this chapter.

## Setting up an internal Rekor instance

Your organization can also set up its own instance of Rekor, or you can individually set up a Rekor server to more fully understand it. You can deploy the Rekor server through Project Sigstore’s [Docker Compose file](https://github.com/sigstore/rekor/blob/main/docker-compose.yml), through a [Kubernetes operator](https://github.com/sigstore/rekor-operator), with a [Helm chart](https://github.com/sigstore/helm-charts), or you can build a Rekor server yourself.

In order to build a Rekor server, you will need Go, a MySQL-compatible database, and you will need to build Trillian, an append-only log. In the lab section, we will walk through how to set up a Rekor server locally.
