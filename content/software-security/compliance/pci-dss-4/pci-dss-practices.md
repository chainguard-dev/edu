---
title: "Overview of PCI DSS 4.0 Practices/Requirements"
description: "Learn about the practices required for PCI DSS 4.0"
lead: "Learn about the practices required for PCI DSS 4.0"
type: "article"
date: 2024-08-09T19:10:09+00:00
lastmod: 2024-08-15T19:10:09+00:00
contributors: []
draft: false
tags: ["compliance", "PCI DSS 4.0", "standards"]
images: []
menu:
  docs:
    parent: "pci-dss-4"
weight: 003
toc: true
---

PCI DSS 4.0, or PCI Data Security Standard is intended for all entities that store, process, or transmit cardholder data and/or authentication data that could impact the security of the cardholder data environment. This includes all entities interacting with information such as the following:

| Cardholder Data | Authentication Data |
|------------------------|-------------------------------------------------------|
| Primary account number | Full track data, such as on a magnetic stripe or chip |
| Cardholder name | Card verification code (the number on the back) |
| Expiration data | PINs |

PCI DSS 4.0 requires compliance with a set of requirements, each related to an information security practice or goal. All of these are intended to protect cardholder data from theft and fraud.


## PCI DSS 4.0 Goals and Requirements

Below is a table overview with a high-level description of the goals and requirements, summarized from the PCI DSS v4.0 Quick Reference Guide from the PCI Security Standards Council, available from their [Document Library](https://east.pcisecuritystandards.org/document_library):

| Goals | Requirements |
|------------------------|-------------------------------------------------------|
| **Build and maintain a secure network and systems** | Install and maintain network security controls and apply secure configurations to all system components |
| **Protect account data** | Protect stored account data as well as during transmission over open, public networks |
| **Maintain a vulnerability management program** | Protect all systems and networks from malicious software, develop and maintain secure systems and software |
| **Implement strong access control measures** | Restrict access to system components and cardholder data y business need to know, identify users and authenticate access to system components, restrict physical access to cardholder data |
| **Regularly monitor and test networks** | Log and monitor all access to system components and cardholder data, test security of all systems regularly |
| **Maintain an information security policy** | Support information security with organizational policies and programs |

For a list of all required practices, see the PCI DSS documentation available in the [PCI Security Standards Council's Document Library](https://east.pcisecuritystandards.org/document_library).


## Browse all PCI DSS 4.0 Articles

- [Introduction to PCI DSS 4.0](/software-security/compliance/pci-dss-4/intro-pci-dss-4/)
- (Current article) Overview of PCI DSS 4.0 Practices/Requirements
- [How Chainguard Can Help With PCI DSS 4.0](/software-security/compliance/pci-dss-4/pci-dss-chainguard/)

**[Get started with Chainguard FIPS Images today!](https://images.chainguard.dev/?category=fips?utm_source=docs)**
