---
title: "Rekor"
lead: ""
type: "article"
date: 2020-10-06T08:49:15+00:00
lastmod: 2026-10-02T13:51:55+00:00
draft: false
menu:
  docs:
    parent: "sigstore"
images: []
---

Rekor is Sigstore's transparency log: a tamper-resistant, append-only ledger of signing metadata from software supply chains. You can query it with the `rekor-cli` command-line tool to verify that an artifact's signature was recorded.

To learn how Rekor works and why a transparency log matters, read [What is Rekor?](https://www.chainguard.dev/supply-chain-security-101/what-is-sigstore-rekor) in Supply Chain Security 101. The pages in this section show you how to install Rekor, query it, upload signed metadata, and run your own Rekor instance.
