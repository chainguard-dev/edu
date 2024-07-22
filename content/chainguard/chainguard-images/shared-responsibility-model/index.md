---
title: "Chainguard's Shared Responsibility Model for Hardened Container Images"
linktitle: "Shared Responsibility Model"
Aliases:
- /chainguard/chainguard-images/shared-responsibility-model/
type: "article"
description: "Reference guide outlining Chainguard's Shared Responsibility model: a framework that clarifies security obligations for hardened container images."
date: 2024-07-18T15:22:20+01:00
lastmod: 2024-07-18T15:22:20+01:00
draft: false
tags: ["Product", "Images", "Reference"]
images: []
menu:
   docs:
    parent: "chainguard-images"
weight: 575
toc: true
---

Chainguard's Shared Responsibility Model is a comprehensive framework that delineates security responsibilities for hardened container images among Chainguard, upstream open-source projects, and customers. This model provides a clear understanding of who is responsible for what, ensuring a secure and compliant container environment. It addresses two primary categories: App Images (used as-is) and Base Images (used in multistage builds).

This reference guide outlines the Shared Responsibility Model, and includes a helpful diagram outlining the relevant responsiblities. It is intended to serve as a resource for customers who want to better understand their security responsibilities (as well as Chainguard's responsibilities) in regards to Chainguard Images. 


## Hardened Container Image Shared Responsibility Model (Diagram)

![Diagram representing Chainguard's shared responsibility model. On the left is a pyramid structure labeled "App Images" with 4 tiers: Apps, LangLibs (go mod, pom, …), Toolchains (go, java, php, …), and System (glibc, openssl). To the left of the pyramid there are two brackets showing that CVE management is performed by the Upstream Open Source project at the Apps level and by Chainguard at the Toolchains and System level. To the right of the pyramid are two smaller brackets showing that if bumping a dependency is breaking, the CVE management falls to the Upstream project; if it's successful, then CVE management falls to Chainguard. On the right is another pyramid labeled "Base images" with 3 tiers: Custom code, Toolchains (go, java, php, …), and System (glibc, openssl, …). To the left of this pyramid are two brackets, showing that CVE management is the responsibility of the customer a the Custom code level and it's the responsibility of Chainguard at the Toolchains and System levels.](shared-responsibility-model.png)

The next few sections dig deeper into the details about App Images, Base Images, and the responsibilities of Chainguard and its customers for both.


## App Images
Chainguard App Images are specialized container images designed to be used "as-is" in production environments.

### Key Characteristics
1. Minimal Attack Surface: Built using a [distroless](/chainguard/chainguard-images/getting-started-distroless/) approach, removing unnecessary components to reduce potential vulnerabilities.
2. Up-to-date Components: Continuously updated with the latest security patches and version updates from upstream projects.
3. Low to Zero CVEs: Rigorously scanned and maintained to minimize known vulnerabilities.
4. Layered Security Responsibility:
    * Top layers (Apps and Lang Libs) are managed by upstream open source projects
    * Lower layers (Toolchains and System) are secured and maintained by Chainguard
5. Compliance with CHP Levels: Adhere to Chainguard's Container Hardening Policy, typically at higher levels (CHP3-CHP5) for enhanced security.
6. SLSA Conformance: Built in accordance with [Supply-chain Levels for Software Artifacts](/open-source/slsa/what-is-slsa/) (SLSA) guidelines.
7. Immutable and Verified: Signed and verified to ensure integrity throughout the software supply chain.
8. SBOM Generation: Includes a build-time generated [Software Bill of Materials](/open-source/sbom/what-is-an-sbom/) for transparency and auditing.
9. FIPS Compliance: Versions available that meet Federal Information Processing Standards.
10. Rapid Patching: Covered by Chainguard's SLA for quick resolution of newly discovered vulnerabilities.

### Use Cases
* Ideal for organizations requiring secure, production-ready container images
* Suitable for environments with stringent security and compliance requirements
* Designed to integrate seamlessly into modern CI/CD pipelines and cloud-native architectures

### App Images Shared Responsibilities
* Apps Layer: Management of CVEs in the top-level application code.
* Lang Libs Layer: Handling vulnerabilities in language-specific libraries built into the image (e.g., `go mod`, `pom`).

Should a CVE be detected in any of these images we would likely bump a dependency to avoid in the next build. The outcome is two-fold: either bumping the dependency is successful or it breaks break the image. 

* **Bumping a dependency is successful**: In this case, the upgrade does not cause the application to break,\ and the CVE is considered independently fixable. This falls under the "Release or Rebuild" condition for a qualifying patch in our SLAs, where the remediation involves rebuilding the image with updated compilers or libraries. The CVE clock starts, and Chainguard aims to resolve the vulnerability within the SLA's time frame.
* **Bumping a dependency is breaking**: If the upgrade causes the application to break, the CVE is not considered independently fixable. Chainguard will file a "pending-upstream-fix" advisory, indicating that the vulnerability cannot be fixed without a fix from the upstream project. Chainguard cannot always service vulnerabilities from the "Lang Lib" (language libraries) layer, unfortunately. The CVE clock does not start in this case, as the vulnerability is not considered fixable under the SLA.

> **Note**: To learn more about Chainguard's Security Advisories, please refer to our [overview on the subject](/chainguard/chainguard-images/working-with-images/security-advisories/). We also encourage you to check out the [Security Advisories page](https://images.chainguard.dev/security) directly. 

### Chainguard's Responsibilities in App Images
* Toolchains Layer: CVE removal in development tools and runtimes (e.g., `go`, `java`, `php`).
* System Layer: Addressing vulnerabilities in base system libraries and utilities (e.g., `glibc`, `openssl`).

### Customer's Responsibilities in App Images
* Any added libraries or APK packages are the customer's responsibility.


## Base Images
Chainguard Base Images are foundational container images designed for use in multistage builds, providing a secure and minimal starting point for organizations to build their custom applications.

### Key Characteristics
1. Minimal Core: Built using a distroless approach, containing only essential components to minimize the attack surface.
2. Regularly Updated: Continuously maintained with the latest security patches and version updates.
3. Low to Zero CVEs: Rigorously scanned and maintained to minimize known vulnerabilities in the base layers.
4. Layered Security Responsibility:
    * Custom Code layer is the responsibility of the customer
    * Toolchains and System layers are secured and maintained by Chainguard
5. Toolchains Layer:
    * Definition: Includes development tools, compilers, and language runtimes necessary for building applications.
    * Examples: Go compiler, Java Development Kit (JDK), PHP interpreter
    * Responsibility: Chainguard manages CVE removal and updates
    * Importance: Provides secure, up-to-date tools for application compilation and runtime
6. Systems Layer:
    * Definition: Comprises base system libraries and core utilities essential for container functionality.
    * Examples: `glibc`, `openssl`, and other basic Unix utilities
    * Responsibility: Chainguard handles vulnerability management and updates
    * Importance: Ensures a secure foundation for all other layers of the container image
7. Compliance with CHP Levels: Adhere to Chainguard's Container Hardening Policy, typically at lower levels (CHP1-CHP2) to allow for customer customization.
8. SLSA Conformance: Built in accordance with Supply-chain Levels for Software Artifacts (SLSA) guidelines.
9. Verifiable Integrity: Signed and verified to ensure trustworthiness throughout the software supply chain.
10. SBOM Generation: Includes a comprehensive Software Bill of Materials for the base layers, aiding in transparency and auditing.
11. FIPS Compliance: Versions available that meet Federal Information Processing Standards for the base layers.
12. Rapid Patching: Covered by Chainguard's SLA for quick addressing of newly discovered vulnerabilities in the base layers.
13. Optimized for Customization: Designed to be easily extended with custom application code and additional dependencies.

### Use Cases
* Ideal for organizations building custom applications that require a secure foundation
* Suitable for DevOps teams implementing secure CI/CD pipelines
* Beneficial for projects requiring fine-grained control over the final image composition while maintaining a secure base

### Customer Responsibilities
* Custom Code Layer: Management of CVEs in customer-developed application code.

### Chainguard's Responsibilities
* Toolchains Layer: CVE removal in development tools and runtimes.
* System Layer: Addressing vulnerabilities in base system libraries and utilities.

## Types of Chainguard images based on Container Hardening Policy (CHP) Levels
Chainguard has developed Container Hardening Policy (CHP) Levels which are designed to complement [Supply-chain Levels for Software Artifacts](/open-source/slsa/what-is-slsa/) (SLSA). These offer practical guidance on what actually constitutes a hardened container image.

The following table highlights Chainguard's Container Hardening Policy Levels:

|    **CHP Level**       |                **RW**                |                       **SHELL**                       |                                     **SYS**                                     |                                     **NET**                                     |           **CVEs**          |
|-----------|:------------------------------------:|:-----------------------------------------------------:|:-------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|:---------------------------:|
|  | Read-write, mutuable root filesystem | Minimal, basic human interaction inside the container | Extended, general operating system level human interaction inside the container | Outbound network connection initiation capabilities as well as package managers | Unaddressed vulnerabilities |
|  **CHP5** |            🔒<br>read only            |                     🔒<br>no shell                     |                             🔒<br>no system utilities                            |                             🔒<br>limited networking                             |      🔒<br>low to 0 CVEs     |
|  **CHP4** |      Read-write local filesystem     |                     🔒<br>no shell                     |                             🔒<br>no system utilities                            |                             🔒<br>limited networking                             |      🔒<br>low to 0 CVEs     |
|  **CHP3** |      Read-write local filesystem     |                      Shell access                     |                             🔒<br>no system utilities                            |                             🔒<br>limited networking                             |      🔒<br>low to 0 CVEs     |
|  **CHP2** |      Read-write local filesystem     |                      Shell access                     |                              System level utilities                             |                             🔒<br>limited networking                             |      🔒<br>low to 0 CVEs     |
|  **CHP1** |      Read-write local filesystem     |                      Shell access                     |                              System level utilities                             |                 Outbound network (apk, git, wget, curl) allowed                 |      🔒<br>low to 0 CVEs     |
|  **CHP0** |      Read-write local filesystem     |                      Shell access                     |                              System level utilities                             |                 Outbound network (apk, git, wget, curl) allowed                 |      accumulating CVEs      |

Chainguard Images that meet CHP levels 0 or 1 can be used as base images to build on top of. Images meeting CHP levels 2, 3, and 4 are to be used as application-specific images. Images that align with the requirements for CHP level 5 are truly distroless application-specific images. 


## CVE Management Strategy
Chainguard follows these practices to minimize the number of CVEs that appear in our Images.
1. Continuous Monitoring: Using tools like [Grype](/chainguard/chainguard-images/working-with-images/scanners/grype-tutorial/) for ongoing vulnerability detection.
2. Rapid Patching: Implementing a stringent SLA for addressing identified vulnerabilities.
3. Minimal Images: Employing a distroless approach to reduce attack surface.
4. Regular Updates: Ensuring all components are current and patched.


## SLA Monitoring Process

### Key Definitions
* Guarded Images: Actively maintained images without end-of-life software.
* Qualifying Patches: The following criteria must be met in order to start the CVE remediation clock.
    * Identification of a CVE affecting a Guarded Image
    * Independent fixability of the CVE
    * Limited scale of required rebuilds (<25% of all guarded images)
    * Availability of an upstream fix or ability to remediate through rebuilding

### CVE Remediation Approaches
1. Upstream Release Version: Incorporating new versions of open-source projects with CVE fixes.
2. Rebuild with Updated Compilers/Libraries: Rebuilding affected packages and images when required.

### Pinned Language Libraries
Two options are provided:
* Option A (Recommended): Attempt to upgrade pinned libraries, with clear communication if upgrades cause build failures.
* Option B: Exclude pinned libraries from the SLA, continuing best-effort attempts to bump versions.

### Compliance Guardrails
To ensure high standards:
* New version detection within 2 hours
* Package updates and CVE triaging within 4-7 calendar days (severity-dependent)
* Rebuilding of critically affected images within 3 calendar days
* Syncing new images to customers within 12 hours


## Learn More
To learn more about best practices when working with Chainguard Images, you can refer to our [Recommended Practices resources](/chainguard/chainguard-images/recommended-practices/). We also encourage you to check out our resources on [Working with Chainguard Images](/chainguard/chainguard-images/working-with-images/). Our conceptual article on [How Chainguard Images are Tested](/chainguard/chainguard-images/images-testing/) may also be helpful for better understanding Chainguard's approach to keeping Images secure.
