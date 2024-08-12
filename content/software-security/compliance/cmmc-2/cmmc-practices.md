---
title: "Overview of CMMC 2.0 Practices/Control Groups "
description: "Overview of CMMC 2.0 Practices/Control Groups "
lead: "Learn about the 14 differenct domains of practices required for CMMC 2.0."
type: "article"
date: 2024-08-09T19:10:09+00:00
lastmod: 2024-08-09T19:10:09+00:00
contributors: []
draft: false
tags: ["compliance", "CMMC 2.0", "standards"]
images: []
menu:
  docs:
    parent: "cmmc-2"
weight: 003
toc: true
---

Cybersecurity Maturity Model Certification (CMMC) 2.0 requires a progressive set of practices. Level 1 has 17 practices. Level 2 includes Level 1 practices plus an additional 110 practices. Level 3 practices include Level 2 practices, plus additional practices that are still being determined. These practices are divided into 14 domains, each of which covers a different aspect of cybersecurity.

Wait, you may be wondering. Are “practices” the same as “controls” or “requirements?” This can be a point of confusion, as CMMC 2.0 refers to its requirements as “practices”, yet the majority are taken from NIST SP 800-171 and NIST SP 800-172 standards or requirements.

## Naming Conventions for CMMC 2.0 Practices/Controls

CMMC 2.0 practices are labeled using the format “DD.L#-REQ”, where:
- DD is the two-letter domain abbreviation
- L# is the level number
- REQ is the NIST SP 800-171 Rev 2 or NIST SP 800-172 security requirement number

## CMMC 2.0 Practice/Control Domains

Below is a table overview of the domains:

| Domain                          | Description                                                                                                   | Example Practice/Control                                     |
|---------------------------------|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| **Access Control (AC)**          | Manage and restrict access to information systems to ensure that only authorized users and processes can interact with the system, protecting sensitive data from unauthorized access. | AC.L1-3.1.22 - Control information posted or processed on publicly accessible information systems. |
| **Awareness and Training (AT)**  | Ensure that personnel are educated on cybersecurity practices and aware of their roles in maintaining security, improving overall organizational resilience against cyber threats. | AT.L2-3.2.3 - Provide security awareness training on recognizing and reporting potential indicators of insider threat. |
| **Audit and Accountability (AU)**| Involve the logging and monitoring of system activities to track and review actions, ensuring accountability and providing a means to detect and respond to potential security incidents. | AU.L2-3.3.2 - Ensure that the actions of individual system users can be uniquely traced to those users so they can be held accountable for their actions. |
| **Configuration Management (CM)**| Establish and maintain secure configurations for information systems to prevent vulnerabilities, ensuring that systems are set up and managed in a consistent and secure manner. | CM.L2-3.4.2 - Establish and enforce security configuration settings for information technology products employed in organizational systems. |
| **Identification and Authentication (IA)** | Focus on verifying the identity of users and devices to ensure that only authorized individuals and systems can access or interact with the organization’s information assets. | IA.L2-3.5.5 - Prevent reuse of identifiers for a defined period. |
| **Incident Response (IR)**       | Prepare for and respond to cybersecurity incidents through structured plans and regular testing, ensuring that the organization can effectively manage and mitigate the impact of incidents. | IR.L2-3.6.2 - Track, document, and report incidents to designated officials and/or authorities both internal and external to the organization. |
| **Maintenance (MA)**             | Maintain and update systems, ensuring that maintenance activities are performed securely. | MA.L2-3.7.1 - Perform maintenance on organizational systems. |
| **Media Protection (MP)**        | Protect information stored on physical and digital media through encryption and other security measures to safeguard data from unauthorized access and exposure. | MP.L2-3.8.2 - Limit access to Controlled Unclassified Information (CUI) on system media to authorized users. |
| **Personnel Security (PS)**      | Manage security risks related to personnel by ensuring thorough background checks and security clearances, addressing potential vulnerabilities from insider threats. | PS.L2-3.9.1 - Screen individuals prior to authorizing access to organizational systems containing CUI. |
| **Physical Protection (PE)**     | Protect physical locations and systems through access controls, surveillance, and other security measures to prevent unauthorized physical access and potential tampering. | PE.L1-3.10.3 - Escort visitors and monitor visitor activity. |
| **Risk Assessment (RA)**        | Assess and remediat risks and vulnerabilities in organizational operations, assets, and systems.   | RA.L2-3.11.2 - Scan for vulnerabilities in organizational systems and applications periodically |
| **Security Assessment (CA)**     | Evaluate the effectiveness of security controls through assessments and address any identified vulnerabilities to continuously improve the security posture. | CA.L2-3.12.1 - Periodically assess the security controls in organizational systems to determine if the controls are effective in their application. |
| **System and Communications Protection (SC)** | Secure communications and data transmitted across networks to protect information from interception and unauthorized access. | SC.L2-3.13.3 - Separate user functionality from system management functionality. |
| **System and Information Integrity (SI)** | Ensure the integrity of systems and information by monitoring for unauthorized changes, protecting against malicious code, and applying updates to maintain system security. | SI.L2-3.14.7 - Identify unauthorized use of organizational systems. |

For a list of all required practices, see pages 9 to 18 in the [Cybersecurity Maturity Model Certification - Model Overview](https://dodcio.defense.gov/Portals/0/Documents/CMMC/ModelOverview_V2.0_FINAL2_20211202_508.pdf) published by Carnegie Mellon University and The Johns Hopkins University Applied
Physics Laboratory LLC and funded by the Department of Defense (DoD).

To learn more about requirements for tracking compliance, continue to the next article in our guide, [CMMC 2.0 Documentation Requirements](./cmmc-documentation.md)

## Browse all CMMC 2.0 articles:
- [Introduction to CMMC 2.0](./intro-cmmc-2.md)
- [CMMC 2.0 Maturity Levels](./cmmc-2-levels.md)
- (Current article) Overview of CMMC 2.0 Practice/Control Groups
- [How Chainguard Can Help With CMMC 2.0](./cmmc-chainguard.md)

**[Get started with Chainguard FIPS Images today!](https://images.chainguard.dev/?category=fips)**
