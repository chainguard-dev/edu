---
title: "How to Query Rekor"
type: "article"
description: "Access the data stored in Sigstore's transparency log, Rekor"
date: 2022-20-087T08:49:31+00:00
lastmod: 2022-24-08T08:49:31+00:00
draft: false
tags: ["REKOR", "PROCEDURAL"]
images: []
menu:
  docs:
    parent: "rekor"
terminalImage: academy/rekor:latest
weight: 003
toc: true
---

_An earlier version of this material was published in the [Rekor chapter](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/block-v1:LinuxFoundationX+LFS182x+2T2022+type@sequential+block@e785fae1be184e2c929db62dbe7444fa/block-v1:LinuxFoundationX+LFS182x+2T2022+type@vertical+block@a48c33126e2c4ee6ad3bfa6b7bc9c957) of the Linux Foundation [Sigstore course](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS182x+2T2022/home)._

Rekor is the transparency log of Sigstore, which stores records of artifact metadata. Before querying Rekor, you should have the `rekor-cli` installed, which you can achieve by following the "[How to Install the Rekor CLI](../how-to-install-rekor)" tutorial.

In order to access the data stored in Rekor, the `rekor-cli` requires either the log index of an entry or the UUID of a software artifact.

For instance, to retrieve entry number 100 from the public log, use this command:

```sh
rekor-cli get --rekor_server https://rekor.sigstore.dev --log-index 100
```

An abridged version of the output is below:

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

The next command will produce the same output but uses the UUID to retrieve the artifact:

```sh
rekor-cli get --uuid 2343d145e62b1051b6a2a54582b69a821b13f31054539660a020963bac0b33dc
```

It is also possible to use a web API to return results that are similar to those above. For instance, we can use curl to fetch the same artifact by its UUID with the following query: 

```sh
curl -X GET "https://rekor.sigstore.dev/api/v1/log/entries/2343d145e62b1051b6a2a54582b69a821b13f31054539660a020963bac0b33dc"
```

By appending the UUID value returned by the `rekor-cli` get command that we ran before, we can obtain detailed information about a specific artifact that has been previously registered within the Rekor public instance.
