---
title: "Minimum Attestation References"
type: "wide"
date: 2023-05-10T15:21:01+02:00
lastmod: 2023-05-10T15:21:01+02:00
draft: false
tags: ["Reference"]
images: []
menu:
  docs:
    parent: "secure-software-development"
weight: 20
toc: true
---
The minimum requirements within the Secure Software Attestation Form address requirements
put forth in EO 14028 subsection (4)(e) and specific SSDF practices and tasks. For reference,
please review the chart below.

| Attestation Requirements | Related EO 14028 Subsection | Related SSDF Practices and Tasks |
| -- | -- | -- |
| 1) The software was developed and built in secure environments. Those environments were secured by the following actions, at a minimum: | 4e(i) | [See rows below]| 
| a) Separating and protecting each environment involved in developing and building software; | 4e(i)(A) | [PO.5.1](/software-security/secure-software-development/ssdf/#PO.5.1) |
| b) Regularly logging, monitoring, and auditing trust relationships used for authorization and access: i) to any software development and build environments; and ii) among components within each environment; | 4e(i)(B) | [PO.5.1](/software-security/secure-software-development/ssdf/#PO.5.1) |
| c) Enforcing multi-factor authentication and conditional access across the environments relevant to developing and building software in a manner that minimizes security risk; | 4e(i)(C) | [PO.5.1](/software-security/secure-software-development/ssdf/#PO.5.1), [PO.5.2](/software-security/secure-software-development/ssdf/#PO.5.2) |
| d) Taking consistent and reasonable steps to document, as well as minimize use or inclusion of software products that create undue risk, within the environments used to develop and build software; | 4e(i)(D) | [PO.5.1](/software-security/secure-software-development/ssdf/#PO.5.1) |
| e) Encrypting sensitive data, such as credentials, to the extent practicable and based on risk; | 4e(i)(E) | [PO.5.2](/software-security/secure-software-development/ssdf/#PO.5.2)
| f) Implementing defensive cyber security practices, including continuous monitoring of operations and alerts and, as necessary, responding to suspected and confirmed cyber incidents; | 4e(i)(F) | [PO.3.2](/software-security/secure-software-development/ssdf/#PO.3.2), [PO.3.3](/software-security/secure-software-development/ssdf/#PO.3.3), [PO.5.1](/software-security/secure-software-development/ssdf/#PO.5.1), [PO.5.2](/software-security/secure-software-development/ssdf/#PO.5.2)
| 2) The software producer has made a good-faith effort to maintain trusted source code supply chains by:
| a) Employing automated tools or comparable processes; and b) Establishing a process that includes reasonable steps to address the security of third-party components and manage related vulnerabilities; | 4e(iii) | PO 1.1, [PO.3.1](/software-security/secure-software-development/ssdf/#PO.3.1), [PO.3.2](/software-security/secure-software-development/ssdf/#PO.3.2), [PO.5.1](/software-security/secure-software-development/ssdf/#PO.5.1), [PO.5.2](/software-security/secure-software-development/ssdf/#PO.5.2), [PS.1.1](/software-security/secure-software-development/ssdf/#PS.1.1), [PS.2.1](/software-security/secure-software-development/ssdf/#PS.2.1), [PS.3.1](/software-security/secure-software-development/ssdf/#PS.3.1), [PW.4.1](/software-security/secure-software-development/ssdf/#PW.4.1), [PW.4.4](/software-security/secure-software-development/ssdf/#PW.4.4), PW 7.1, PW 8.1, RV 1.1 |
| 3) The software producer maintains provenance data for internal and third-party code incorporated into the software; | 4e(vi) | [PO.1.3](/software-security/secure-software-development/ssdf/#PO.1.3), [PO.3.2](/software-security/secure-software-development/ssdf/#PO.3.2), [PO.5.1](/software-security/secure-software-development/ssdf/#PO.5.1), [PO.5.2](/software-security/secure-software-development/ssdf/#PO.5.2), [PS.3.1](/software-security/secure-software-development/ssdf/#PS.3.1), [PS.3.2](/software-security/secure-software-development/ssdf/#PS.3.2), [PW.4.1](/software-security/secure-software-development/ssdf/#PW.4.1), [PW.4.4](/software-security/secure-software-development/ssdf/#PW.4.4), [RV.1.1](/software-security/secure-software-development/ssdf/#RV.1.1), [RV.1.2](/software-security/secure-software-development/ssdf/#RV.1.2) |
| 4) The software producer employed automated tools or comparable processes that check for security vulnerabilities. In addition: a) The software producer ensured these processes operate on an ongoing basis and, at a minimum, prior to product, version, or update releases and b) The software producer has a policy or process to address discovered security vulnerabilities prior to product release; and c) The software producer operates a vulnerability disclosure program and accepts, reviews, and addresses disclosed software vulnerabilities in a timely fashion. | 4e(iv) | [PO.4.1](/software-security/secure-software-development/ssdf/#PO.4.1), [PO.4.2](/software-security/secure-software-development/ssdf/#PO.4.2), [PS.1.1](/software-security/secure-software-development/ssdf/#PS.1.1), [PW.2.1](/software-security/secure-software-development/ssdf/#PW.2.1), [PW.4.4](/software-security/secure-software-development/ssdf/#PW.4.4), [PW.5.1](/software-security/secure-software-development/ssdf/#PW.5.1), [PW.6.1](/software-security/secure-software-development/ssdf/#PW.6.1), [PW.6.2](/software-security/secure-software-development/ssdf/#PW.6.2), [PW.7.1](/software-security/secure-software-development/ssdf/#PW.7.1), [PW.7.2](/software-security/secure-software-development/ssdf/#PW.7.2), [PW.8.2](/software-security/secure-software-development/ssdf/#PW.8.2), [PW.9.1](/software-security/secure-software-development/ssdf/#PW.9.1), [PW.9.2](/software-security/secure-software-development/ssdf/#PW.9.2).

## References

Table of the references comes from the top of the [original RFC PDF](https://www.cisa.gov/secure-software-attestation-form).

_Reprinted courtesy of the National Institute of Standards and Technology, U.S. Department of Commerce. Not copyrightable in the United States._