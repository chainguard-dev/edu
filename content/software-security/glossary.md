---
title: "Chainguard Glossary"
lead: "Software supply chain security vocabulary"
description: "Software supply chain security vocabulary"
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

## General terms

### Software supply chain

Like in material good supply chains, a software supply chain is composed of activities that an organization undertakes to deliver an end product or service to a consumer. Software supply chain activities involve the transformation of dependencies, packages, components, binaries, build and packaging scripts, code and other software artifacts, and infrastructure into a finished software deliverable that is deployed into production. Participants in the supply chain include actors like developers, reviewers, testers, and maintainers who are working on the product at hand, but also includes those who maintain and contribute to packages and package managers, and other software that may be incorporated into a given product. Software supply chains also include information relevant to the software, such as versioning, signatures, and hashes.

---

### Software supply chain attacks

An intentional act of inserting malicious functionality into — or taking advantage of a known vulnerability within — the build, source, components or deployment software or infrastructure with the goal of propagating that harmful functionality through current distribution methods.

---

### Software development life cycle

The methodology and process for planning, designing, creating, testing, deploying, and maintaining software.

---

### Software artifact

An artifact is an immutable blob of data. Examples of artifacts include a file, a git commit, a container image, a firmware image.

---

### Attestation

An attestation allows consumers of a software artifact to verify the quality of that artifact independently from the producer of the software. It also requires software producers to provide verifiable proof of the quality of their software. You can think of an attestation as a **proclamation** that _software artifact X was produced by Y person at Z time._

---

### Provenance

Provenance is the verifiable information about software artifacts describing _where_, _when_ and _how_ something was produced.

---

## Security tools and frameworks

### Certificate authority

Often abbreviated as **CA**, a certificate or certification authority is a governing body that stores, signs, and issues digital certificates that can verify claims about the ownership of a given public key. Software consumers can use a CA to verify the assertions made about the private key that corresponds with the certified public key. A trusted third party, CAs use the X.509 or EMV standard to format certificates. 

---

### Code signing

The process of digitally signing software artifacts to verify the author of the software as well as guarantee that the code has not been altered in any way since it was signed. Cryptographic hashes are used to sign software in order to validate authenticity and integrity. Code signing results in a signature. 

---

### OCI

OCI stands for the **O**pen **C**ontainer **I**nitiative, which is an open governance structure that was set up to create and foster open industry standards around software container formats and runtimes.

---

### OIDC

OIDC is short for **O**pen**ID** **C**onnect, an identity layer that is built on top of the OAuth 2.0 protocol, and is governed by the OpenID Foundation. The tool allows for identity authentication and identity verification based on the authentication performed by a provider such as Apple, Google, GitLab, Microsoft, and others. 

---

### PKI

Standing for **p**ublic **k**ey **i**nfrastructure, PKI arranges the necessary elements of infrastructure to manage public-key encryption, binding public keys with respective identities of entities (including individuals and organizations).

---

### Red teaming

Conducting a red team assessment consists of a goal-based adversarial activity to demonstrate how attackers can combine exploits to compromise the integrity of software or otehr technology. 

---

### SBOM

An acronym, SBOM stands for a **s**oftware **b**ill **o**f **m**aterials (plural: SBOMs or software bill_s_ of materials). An SBOM is like an electronic packaging slip or receipt, it is a formal record that contains the details and supply chain relationships (such as dependencies) of the components used in building given software.

---

### Sigstore

A suite of tools to sign, verify, and monitor software artifacts. Within the umbrella of Sigstore are Cosign for artifact signing and verification, the certificate authority Fulcio, and the transparency log Rekor. All of this tooling can be used independently of each other.

---

### SLSA

Standing for **s**upply chain **l**evels for **s**oftware **a**rtifacts, SLSA (pronounced like "SLSA") is a security framework that offers a check-list of standards and controls in order to prevent tampering, improve integrity, and secure packages and infrastructure. SLSA has four levels of increasing security. 

---

### SSDF

A project of the United States Department of Commerce's National Institute of Standards and Technology (NIST), the Secure Software Development Framework (SSDF) is a set of guidance and recommendations to establish a secure software development practice.

---

### Tekton

Tekton provides a cloud-native solution for building CI/CD systems with a focus on software supply chain security through offering artifact signatures and attestations through Tekton Chains. 

---

### TUF

**T**he **U**pdate **F**ramework, known as TUF, offers a framework for securing software update systems.

---

## Attacks and vulnerabilities

### Log4Shell

An internet vulnerability involving a nearly ubiquitous piece of software, Log4j. The vulnerability received attention in December 2021 and much work was done to mitigate the vulnerability, which can be exploited by a remote code execution attack.

---

### SolarWinds Hack

The commonly used term to refer to the software supply chain breach that involved the SolarWinds Orion system, which occurred in 2020. Hackers gained access to networks, systems, and data of thousands of SolarWinds customers, and compromised the systems of over 30,000 organizations who relied on Orion software. This was one of the largest software supply chain attacks of its kind recorded to date. 

---

### Typosquatting

Typosquatting is a cyber attack that is done by adversaries who try to pass a string (such as a URL) that they own as something that is official. For example, instead of the official chainguard.dev an adversary may register chain-guard.dev, cha1nguard.dev, or chainguar.dev in order to pretend to be the official site.
