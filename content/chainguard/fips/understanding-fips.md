---
title: "Understanding FIPS"
linktitle: "Understanding FIPS"
type: "article"
description: "Learn about FIPS standards, who needs FIPS validation, and the cryptographic module validation process"
date: 2025-10-16T08:00:00+00:00
lastmod: 2025-10-16T08:00:00+00:00
draft: false
tags: ["FIPS", "Compliance", "Security"]
images: []
weight: 010
toc: true
---

## What is FIPS?

Federal Information Processing Standards (FIPS) are publicly announced standards developed by the [National Institute of Standards and Technology](https://www.nist.gov/itl/publications-0/federal-information-processing-standards-fips) (NIST) in accordance with the Federal Information Security Management Act (FISMA) and approved by the U.S. Secretary of Commerce.

FIPS is a **U.S. federal standard** that establishes requirements for cryptographic security in federal government systems. While FIPS originates from U.S. federal requirements, many organizations globally adopt FIPS validation as a recognized security benchmark, particularly when working with U.S. government agencies or operating in regulated industries.

FIPS compliance ensures that cryptographic security services within applications meet strict security and integrity standards, and are implemented and configured correctly. According to NIST guidance, "Non-validated cryptography is viewed as providing no protection… the data would be considered unprotected plaintext."

## Who Needs FIPS Validation?

### U.S. Federal and Government Requirements

**U.S. Federal agencies** are required to use FIPS-validated cryptography for protecting sensitive information under FISMA.

**U.S. Department of Defense (DoD)** systems at various Impact Levels (IL4, IL5, IL6) must use FIPS-validated cryptographic modules as part of their security authorization process.

**FedRAMP-authorized cloud services** must meet Federal Risk and Authorization Management Program requirements for operating in U.S. federal environments. FedRAMP Rev 5 specifically states that "any data in transit, whether from one container to another or to a sidecar inside the same host virtual machine" requires FIPS-validated encryption controls (SC-8).

**U.S. Government contractors** working with federal data often must demonstrate FIPS compliance as part of their contractual obligations.

### Global Organizations Working with U.S. Entities

Organizations outside the United States may need FIPS validation when:

- Providing cloud services to U.S. federal agencies or contractors
- Participating in U.S. defense supply chains
- Operating systems that handle U.S. federal data
- Seeking to demonstrate cryptographic security using a recognized standard

### Regulated Industries

Beyond government mandates, FIPS validation is recommended or required for:

- **Financial services**: Banks and payment processors handling sensitive financial data
- **Healthcare**: Organizations processing protected health information (PHI) under HIPAA
- **Critical infrastructure**: Energy, telecommunications, and transportation sectors
- **Defense contractors**: Companies in the defense industrial base

### Why Alternative Approaches Fall Short

Some organizations attempt to achieve compliance through alternative means, but these approaches have limitations:

**Service meshes** (Istio, Linkerd) cannot encrypt traffic between main containers and sidecars, or container-to-container calls within the same pod. Auditors will flag these gaps as non-compliant.

**VPN tunnels** only protect host-to-host traffic. They miss intra-host and intra-pod cryptographic operations that FedRAMP and DoD auditors require.

**FIPS-enabled host OS alone** doesn't force userspace applications to use FIPS modules. Applications must be explicitly configured, and this approach restricts you to older kernel versions.

## FIPS Standards Overview

### FIPS 140: Cryptographic Module Validation

FIPS 140 defines security requirements for cryptographic modules.

**FIPS 140-2** was the standard from 2001 until recently. As of September 2026, all FIPS 140-2 certificates will become historical, making migration to FIPS 140-3 essential.

**FIPS 140-3**, published in September 2019, delivers more robust security testing, clearer validation criteria, and updated standards that reflect advancements in cryptographic technology. Organizations adopting this version gain enhanced protection against emerging threats.

The transition from 140-2 to 140-3 represents a significant upgrade in:
- Security testing rigor
- Documentation requirements
- Conformance criteria clarity
- Alignment with international standards (ISO/IEC 19790)

### FIPS 186: Digital Signature Standard

**FIPS 186-5**, published by NIST in 2023, approved the EdDSA (Edwards-curve Digital Signature Algorithm) for digital signatures using Ed25519 and Ed448 schemes.

Ed25519 offers improved speed and smaller key sizes compared to RSA, making it attractive for modern cryptographic implementations. This standard enables more efficient digital signatures while maintaining security guarantees.

### SP 800-90B: Entropy Source Validation

SP 800-90B defines requirements for entropy sources used by random bit generators. Cryptographic operations require high-quality randomness that cannot be reasonably predicted.

Entropy Source Validation (ESV) certifies that a random number generator produces sufficient entropy to meet cryptographic requirements. This validation is separate from but complementary to CMVP (Cryptographic Module Validation Program) certification.

## The CMVP Validation Process

### What is CMVP?

The Cryptographic Module Validation Program (CMVP) is a joint effort between NIST and the Canadian Centre for Cyber Security to validate cryptographic modules according to FIPS 140 requirements.

A validated module receives a certificate number that organizations can reference for compliance purposes. Chainguard's OpenSSL FIPS provider, for example, holds CMVP Certificate [#4282](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4282).

### Validation Timeline

The CMVP process is lengthy and complex:

1. **Development and internal testing**: Implement cryptographic module with FIPS requirements
2. **Lab testing**: Submit to a NIST-approved testing lab for evaluation
3. **Patching and fixes**: Address findings from lab testing
4. **Formal submission**: Submit validated module to NIST
5. **NIST review process**: Module moves through pending review, coordination, and finalization states
6. **Certificate issuance**: If approved, NIST issues a validation certificate

**Current average timeline**: 590 days from submission to certificate issuance.

This extended timeline creates challenges for software vendors, as:
- Security vulnerabilities (CVEs) may be discovered during the validation process
- New features cannot be added without restarting validation
- Projects with rapid release cycles struggle to maintain current certifications

### Module in Process (MIP)

Modules awaiting validation appear on NIST's [Module in Process list](https://csrc.nist.gov/Projects/cryptographic-module-validation-program/modules-in-process/modules-in-process-list). This indicates formal submission but not yet completed validation.

## Cryptographic Boundaries

A cryptographic boundary defines what is inside the validated module versus what is outside. Understanding boundaries is essential for compliance.

**Inside the boundary**: The cryptographic algorithms, key management, and security functions that are validated.

**Outside the boundary**: Operating system services, entropy sources (validated separately under SP 800-90B), and application code that uses the module.

For example, Chainguard's kernel-independent FIPS design places:
- **Inside**: OpenSSL FIPS provider with approved algorithms
- **Outside**: Jitterentropy library (separately validated under SP 800-90B)
- **Outside**: Application code calling OpenSSL APIs

The entropy source validation satisfies the cryptographic module's entropy requirements without being part of the CMVP certificate itself.

## Approved vs. Non-Approved Algorithms

FIPS distinguishes between approved and non-approved cryptographic algorithms.

**Approved algorithms** have undergone NIST review and are permitted for protecting sensitive data. Examples include AES, SHA-2 and SHA-3 families, RSA (with constraints), and EdDSA.

**Non-approved algorithms** either haven't been evaluated or are explicitly prohibited for protecting sensitive information. Examples include MD5 (except for non-security purposes like checksums), SHA-1 for signatures, and protocols like WireGuard that require unapproved primitives.

**Approved-only mode** means the cryptographic module only permits approved algorithms. Chainguard FIPS images operate in approved-only mode and cannot be switched to allow non-approved algorithms. This design prevents accidental non-compliance.

## Security Policies

Each validated cryptographic module includes a security policy document describing:
- The module's cryptographic boundary
- Approved and non-approved modes of operation
- Required configuration for FIPS compliance
- Roles and services provided
- Physical and logical security mechanisms

Security policies are publicly available on the NIST website for each validated module. Review these policies to understand module capabilities and limitations.

## Maintaining Compliance

FIPS compliance is not set-and-forget:

**Ongoing updates**: As vulnerabilities are discovered, modules must be patched while maintaining validation. Chainguard addresses this by committing to zero-to-minimal CVEs under SLA.

**Certificate expiration**: Certificates must be renewed periodically. Organizations should track certificate status and plan for transitions.

**Configuration management**: Systems must maintain FIPS configuration throughout their lifecycle. A validated module running in non-FIPS mode provides no compliance benefit.

**Audit preparation**: Document which modules are in use, their certificate numbers, and configuration evidence for auditors.

## Next Steps

Now that you understand FIPS fundamentals, explore:

- [Kernel-Independent FIPS Architecture](/chainguard/fips/kernel-independent-architecture/) - Learn how Chainguard's approach simplifies FIPS deployment
- [Chainguard FIPS Containers](/chainguard/fips/fips-images/) - Overview of available FIPS images
- [FIPS Commitment](https://www.chainguard.dev/legal/fips-commitment) - Chainguard's warranties and certifications
- [NIST CMVP](https://csrc.nist.gov/projects/cryptographic-module-validation-program) - Official validation program information
