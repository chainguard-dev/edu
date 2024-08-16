---
title: "CMMC 2.0 Maturity Levels"
description: "Learn about the differences between CMMC 2.0's maturity levels"
lead: "Learn about the differences between CMMC 2.0's maturity levels"
type: "article"
date: 2024-08-09T19:10:09+00:00
lastmod: 2024-08-15T19:10:09+00:00
contributors: []
draft: false
tags: ["compliance", "CMMC 2.0", "standards"]
images: []
menu:
  docs:
    parent: "cmmc-2"
weight: 002
toc: true
---

The  **Cybersecurity Maturity Model Certification (CMMC) 2.0** integrates various cybersecurity standards and best practices into a unified model that encompasses three maturity levels. Each level builds upon the previous one, with increasing rigor in cybersecurity practices and processes. In this article, we’ll provide an overview of the three levels of maturity and example practices that are representative of their requirements.

![Overview of CMMC Model 2.0 showing three levels: Level 3 (Expert) with over 110 practices based on NIST SP 800-172 and triennial government-led assessments, Level 2 (Advanced) with 110 practices aligned with NIST SP 800-171 and a mix of triennial third-party assessments and annual self-assessments, and Level 1 (Foundational) with 17 practices and annual self-assessment.](CMMC-level.jpg)

## Level 1: Foundational

Contractors and subcontractors who handle only [Federal Contract Information](https://isoo.blogs.archives.gov/2020/06/19/%E2%80%8Bfci-and-cui-what-is-the-difference/) (FCI) typically need this level of certification. This is particularly relevant for small businesses that provide basic products or services without dealing with sensitive information. For example, a company supplying standard office supplies to a government agency would fall under this category. The focus at this level is on maintaining basic safeguards by implementing 17 fundamental cybersecurity practices. These practices are primarily derived from the Federal Acquisition Regulation (FAR) 52.204-21, a set of rules for government procurement in the United States. They are designed to protect FCI by ensuring that essential, straightforward protections are in place.

### Documentation Requirements

At Level 1, the documentation requirements are minimal, focusing on basic cyber hygiene through the implementation of 17 foundational cybersecurity practices. The purpose is to establish essential protections without the need for extensive documentation.

For example, organizations may maintain basic policies and procedures for access control, media protection, and physical security, along with records of security awareness training. The emphasis at this level is on demonstrating that these fundamental practices are in place, rather than producing detailed documentation, as required in higher levels.

### Example Level 1 Practices
- Limiting information system access to authorized users.
- Conducting background checks on employees.
- Implementing basic measures such as antivirus and firewalls.

## Level 2: Advanced

Contractors and subcontractors who handle [Controlled Unclassified Information](https://www.ftc.gov/policy-notices/controlled-unclassified-information) (CUI) but are not involved in critical defense programs typically need Level 2 certification. This is relevant for companies involved in more complex projects that deal with sensitive, though not highly classified, data. For instance, a contractor providing technical support for military communication systems, where sensitive but not classified information is exchanged, would require this level.

Level two consists of implementing a subset of the security requirements specified in NIST SP 800-171, totaling 110 practices. This level is designed as a transitional step for organizations aiming to achieve Level 3, building upon the foundational practices established in Level 1.

### Documentation Requirements

At Level 2, the documentation requirements are moderate, reflecting the need for intermediate cyber hygiene and addressing a subset of the NIST SP 800-171 requirements. Organizations must maintain a System Security Plan (SSP) that outlines security strategies and vulnerability assessment and remediation plans. They must also create a Plan of Action and Milestones (POA&M) addressing any aspects of the organization which are note yet implemented.

Other Level 2 documentation requirements may include audit logs, incident response reports, inventory of the organization’s systems, location of [Controlled Unclassified Information](https://www.ftc.gov/policy-notices/controlled-unclassified-information) (CUI) in the organization’s environment, and other documents related to the implementation and management of cybersecurity practices.

### Example Level 2 Practices
- Implementing multifactor authentication.
- Conducting regular vulnerability assessments.
- Establishing and maintaining an operational incident-handling capability for organizational
systems.

## Level 3: Expert

Contractors handling highly sensitive CUI and involved in critical defense programs typically require this level of certification. This applies to large defense contractors developing advanced military technologies, such as a company designing next-generation fighter jets for the DoD. The focus at this level is on advanced and proactive cyber hygiene, requiring organizations to implement all 110 practices from NIST SP 800-171, along with additional practices from a subset of NIST SP 800-172.

This level demands advanced security measures to protect CUI against advanced persistent threats (APTs), such as cyber-espionage campaigns, zero-day exploits, and coordinated attacks targeting vulnerabilities in critical infrastructure. It requires three government-led assessments a year to maintain compliance.

### Documentation Requirements

Level 3 requires the same documentation requirements as Level 2, including the [System Security Plan](https://csrc.nist.gov/glossary/term/system_security_plan) (SSP) and [Plan of Action and Milestones](https://csrc.nist.gov/glossary/term/poaandm) (POA&M). Further documentation requirements will be clear once the DoD determines which additional practices from NIST SP 800-172 will also be required.

### Example Level 3 Practices
At the time of publication, specific Level 3 practices are still being determined. However, the Department of Defense has indicated that they will be pulled from a subset of NIST SP 800-172, Enhanced Security Requirements for Protecting Controlled Unclassified Information.

Each CMMC level builds upon the previous one, ensuring that as organizations progress through the levels, their cybersecurity posture becomes more robust and capable of addressing increasingly sophisticated threats. This tiered approach allows organizations of varying sizes and capabilities to incrementally improve their cybersecurity measures while meeting the specific requirements necessary to handle sensitive information.

To learn more about the specific required practices of CMMC 2.0, continue to the [Overview of CMMC 2.0 Practice/Control Groups](/software-security/compliance/cmmc-2/cmmc-practices/).

## Browse all CMMC 2.0 Articles

- [Introduction to CMMC 2.0](/software-security/compliance/cmmc-2/intro-cmmc-2/)
- (Current article) CMMC 2.0 Maturity Levels
- [Overview of CMMC 2.0 Practice/Control Groups](/software-security/compliance/cmmc-2/cmmc-practices/)
- [How Chainguard Can Help With CMMC 2.0](/software-security/compliance/cmmc-2/cmmc-chainguard/)

**[Get started with Chainguard FIPS Images today!](https://images.chainguard.dev/?category=fips?utm_source=docs)**