---
title: "SLSA at Chainguard"
linktitle: "SLSA"
description: "A brief overview of SLSA and Chainguard's compliance efforts."
type: "article"
date: 2025-07-22T14:05:09+00:00
lastmod: 2025-07-22T14:05:09+00:00
contributors: []
draft: false
tags: ["Compliance", "SLSA", "Standards"]
images: []
menu:
  docs:
    parent: "compliance"
weight: 035
toc: true
---

# SLSA Compliance at Chainguard

SLSA (pronounced “salsa”), or Supply chain Levels for Software Artifacts, is a security framework consisting of standards and controls that prevent tampering, improve integrity, and secure packages and infrastructure. It is described in depth in [What is SLSA?](/open-source/slsa/what-is-slsa/).

This page describes the work Chainguard has done to comply with the SLSA standard and why that matters.


## SLSA Levels and Requirements

One of the defining features of SLSA is its multi-level assurance model. SLSA currently specifies four primary levels (0 through 4) of compliance, with each level building on the previous and representing a milestone in securing the software supply chain. Higher levels correspond to stronger integrity guarantees and tamper-resistance.

Here we give a brief reminder of each level and then tie each level to Chainguard's internal work to meet the requirements.

### Level 0: “No Guarantees”

This is the starting point, representing the absence of SLSA practices. Software at Level 0 has no verifiable supply chain metadata. There are no particular requirements. Essentially, software at Level 0 still has an opaque build process and may be susceptible to tampering with little to no deterrence.

> **Note**
Level 0 is not an official part of the numbered levels but is a useful concept to denote non-compliance.


### Level 1: Provenance Exists

The first SLSA level requires that the build process is fully scripted or automated and that it produces provenance metadata describing how the artifact was built.

The provenance at Level 1 may be basic and even unsigned, but it still records the key details of the build. This gives developers and downstream users visibility into what source code and inputs went into a build. While Level 1 does not yet prevent tampering, it establishes a rudimentary “ingredient list” that can aid in debugging and trust decisions.



Example
 Imagine a team using GitHub Actions as their CI system. For every release build, their workflow automatically logs: (1) the Git repository URL, (2) the exact commit SHA, and (3) the build script or steps run during the process. It also outputs a build log and generates a Software Bill of Materials (SBOM) listing the included packages and dependencies. Even though this metadata isn’t cryptographically signed at this level, it’s a solid first step toward transparency. It would be like writing down your recipe so others can understand how your salsa was made, even if you haven’t locked your kitchen yet.


### Level 2: Hosted Build + Signed Provenance

SLSA Level 2 introduces requirements that significantly raise the bar on integrity. It mandates using version control for source and a trusted, hosted build service to perform the builds, which must generate authenticated (signed) provenance.

By relying on a dedicated build platform (rather than, say, a developer’s laptop) and signing the build metadata, Level 2 ensures that any tampering would require an active attack on the build service itself – deterring many attackers and insider threats.

The signature on the provenance means consumers can verify that the artifact truly came from the expected build system. Level 2 gives greater confidence in the origin of the software, and it also sets the stage for Level 3 by establishing a consistent, controlled build environment.

Example
A team upgrades their workflow to use GitHub Actions for all production builds. They have  integrated Sigstore’s Cosign into the pipeline to automatically sign the provenance after each successful build. For every container image they produce, the build system now: (1) pulls from a version-controlled Git repository, (2) runs on a hardened, hosted runner, and (3) emits signed provenance that includes the source repo, commit, build steps, and dependencies.

Thanks to the signature, anyone consuming the image can verify not just how it was built, but also that it was built on GitHub Actions, using a known and trusted pipeline. This gives consumers cryptographic assurance that the artifact wasn’t tampered with after the build and didn’t come from an unknown or rogue environment.

If Level 1 was like writing down your salsa recipe, Level 2 is like having that salsa made in a certified commercial kitchen, complete with security cameras and a signed delivery receipt. Not only do you know the ingredients and process, but you have proof it came from a trusted, controlled environment, not some random person’s garage with unlabeled jars and potentially questionable hygiene.


### Level 3: Hardened Builds

At Level 3, the requirements extend to the build and source platforms themselves. The source code repository and build infrastructure must meet specific security standards to guarantee the auditability of source and the integrity of the build process.

This may involve independent audits or certifications of the CI/CD platform and enforcing strict controls like isolated builds (to prevent one build from influencing another) and non-falsifiable provenance (provenance that even build administrators cannot alter).

Achieving Level 3 typically means the build system is resistant to most known supply-chain attacks – for example, it can prevent an attacker who has compromised one build from inserting code into another project’s build. It also often entails strong access controls, monitoring, and security policies on the pipeline. Level 3 provides a high level of assurance: even sophisticated adversaries would need to find novel vulnerabilities in the hardened build environment to compromise the software.
Example
A company upgrades to a centrally managed build farm with hardened security. Their build environment includes (1) strict isolation between build jobs, enforced at the VM or container level, (2) a mandatory two-factor authentication for anyone accessing the build infrastructure, (3) auditing and logging of all build actions and changes, and (4) access restrictions that prevent developers—or even most admins—from directly modifying the build output.

The result is that every artifact is built in a clean, locked-down environment, and the signed provenance can be cryptographically tied to that secure setup. Insider tampering, cross-project contamination, or stealthy post-build modifications become extremely difficult, if not impossible.

If Level 2 is like a certified commercial kitchen, Level 3 is a high-security food processing facility with clean rooms, employee badge scans, separate prep zones for each product line, and tamper-evident packaging. Even if someone sneaks into the building, they can’t just toss mystery ingredients into the salsa without triggering alarms. Plus, you got camera footage, logs, and seals to prove it.

💡 Note
As of SLSA v1.1, Level 3 is the highest level in the Build track that has formal requirements defined.


### Level 4: Highest Trust (proposed)

Level 4 represents the ideal end state of supply chain security in the SLSA framework: full traceability, high assurance, and minimal room for human error or malicious interference. While still aspirational and not yet finalized in SLSA v1.1, the original drafts outlined several key practices for this level:
Two-person review for all source code changes
Hermetic builds that use only pre-declared, verified inputs
Reproducible builds that produce the exact same output, bit-for-bit, every time

By requiring review and restricting the build environment, Level 4 closes many of the remaining gaps left at earlier levels. No one person can slip in a dangerous change unnoticed, and the build process can’t reach out to the internet for untracked dependencies. Every input is locked, checksummed, and declared up front. The resulting provenance provides complete, verifiable documentation of the entire process and all its ingredients.

Requiring two-person code review means no single individual can inject a malicious change undetected, which deters insider threats and mistakes

Hermetic, reproducible builds ensure that given the same inputs, the build output is always identical – and that the build process isn’t pulling in undeclared or unverified dependencies from the internet.

All dependencies would be explicitly declared and locked (pinned), and the provenance would list them completely.

Achieving Level 4 would give consumers very high confidence that the software hasn’t been tampered with and that its entire dependency chain is accounted for and verified.
Example
An organization working toward Level 4 would enforce (1) mandatory two-person code review for every commit before it can be merged, (2) a hermetic build environment that pre-fetches all inputs, checksums them, and blocks undeclared network access, (3) reproducible builds that generate identical artifacts when repeated with the same inputs, and (4) provenance that includes a full, verified list of dependencies, versions, and build instructions.

These practices give the company extremely high confidence that the code in production reflects only approved, verified changes—and that the artifact can be rebuilt independently and validated down to the byte.

Taking our ongoing food analogy to its most extreme, here, we’d be running a pharmaceutical-grade salsa production line. Every ingredient would be batch-tested, stored in clean-room containers, and handled by two employees under camera surveillance. The entire process is documented, repeatable, and sealed with tamper-proof labels. If someone would ever question the product’s quality, you could re-run the exact process with the same inputs and get the same jar of salsa—absolutely every time. Our food analogy has now run its course, and we clearly need to leave it behind.

> **Note**
As of the current SLSA specification, Level 4 is a future direction – many of these controls are being explored for upcoming SLSA versions.


