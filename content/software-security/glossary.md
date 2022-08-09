---
title: "Chainguard Glossary"
lead: "Software supply chain security vocabulary"
type: "article"
date: 2022-08-01T15:21:01+02:00
lastmod: 2022-08-01T15:21:01+02:00
draft: false
images: []
menu:
  docs:
    parent: "software-security"
weight: 10
toc: true
---

### Software supply chain

Like in material good supply chains, a software supply chain is composed of activities that an organization undertakes to deliver an end product or service to a consumer. Software supply chain activities involve the transformation of dependencies, packages, components, binaries, build and packaging scripts, code and other software artifacts, and infrastructure into a finished software deliverable that is deployed into production. Participants in the supply chain include actors like developers, reviewers, testers, and maintainers who are working on the product at hand, but also includes those who maintain and contribute to packages and package managers, and other software that may be incorporated into a given product. Software supply chains also include information relevant to the software, such as versioning, signatures, and hashes.

---

### Software development life cycle

The methodology and process for planning, designing, creating, testing, deploying, and maintaining software.

---

### Software supply chain attacks

An intentional act of inserting malicious functionality into — or taking advantage of a known vulnerability within — the build, source, components or deployment software or infrastructure with the goal of propagating that harmful functionality through current distribution methods.

---

### Software artifact

An artifact is an immutable blob of data. Examples of artifacts include a file, a git commit, a container image, a firmware image.

---

### Attestation

An attestation allows consumers of a software artifact to verify the quality of that artifact independently from the producer of the software.
This thing was produced by this person at this time.
It also requires software producers to provide verifiable proof of the quality of their software.

---

### Provenance

It’s the verifiable information about software artifacts describing where, when and how something was produced

---

### SBOM

software bill of materials, it’s like an electronic packaging slip or receipt.  “a formal record containing the details and supply chain relationships of various components used in building software.”
