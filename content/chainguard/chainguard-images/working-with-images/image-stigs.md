---
title: "STIGs for Chainguard Images"
linktitle: "STIGs"
type: "article"
description: "A conceptual overview of STIGs, which are available for Chainguard Images."
date: 2024-06-13T15:56:52-07:00
lastmod: 2024-06-13T15:56:52-07:00
draft: false
tags: ["IMAGES", "PRODUCT", "CONCEPTUAL"]
images: []
menu:
  docs:
    parent: "concepts"
weight: 055
toc: true
---


The practice of using STIGs to secure various technologies originated with the United States Department of Defense (DoD). If an organization uses a certain kind of software, say MySQL 8.0, they must ensure that their implementation of it meets the requirements of the [associated STIG](https://public.cyber.mil/announcement/stig-update-disa-has-released-the-oracle-mysql-8-0-stig/) in order to qualify as a vendor for the DoD. More recently, other compliance frameworks have begun acknowledging the value of STIGS, with some going so far as to require the use of STIGs in their guidelines.

[Chainguard announced](https://www.chainguard.dev/unchained/stig-hardening-container-images) the release of a General Purpose Operating System STIG with the goal that it will help customers integrate Chainguard Images into their workflows with the confidence that they're doing so securely. This conceptual article aims to give a brief overview of what STIGs are and how they can be valuable in the context of container images.


## What are STIGs?

"STIG" is an acronym that stands for Secure Technical Implementation Guide. A STIG is akin to a checklist that a security administrator can go through to ensure that a given piece of software has been fully hardened against cybersecurity threats.

A STIG is typically written by the developer or vendor of the given piece of software against a published DOD Security Requirements Guide (SRG). STIGs are presented in the XCCDF (Extensible Configuration Checklist Description Format), allowing them to be ingested into a SCAP-validated tool to validate that a given target is in compliance with them.

After drafting the STIG, the vendor will submit it to the Defense Information Systems Agency (DISA), an agency within the DoD. One of DISA's responsibilities is publishing and maintaining STIGs on the [DoD Cyber Exchange website](https://public.cyber.mil/stigs/downloads/), and the process from a STIG being submitting to it being published by DISA can take years. As of this writing, DISA has published over 450 STIGs for a wide variety of software applications.


## How STIGs can be used to harden images

STIGs are typically published for hardware, firmware, and specific applications. However, in recent years containerization has grown in popularity and is now the modern way to deploy applications. Without STIGs to  presents a gap in terms of clear instructions on how to securely but there has historically been a gap when it comes to STIGs for 

Chainguard produces hardened, minimal container images with each one containing few to zero CVEs. Because of this, they adhere to many compliance standards where there's a control for vulnerability or risk management, including [FedRAMP](https://www.fedramp.gov/) and [PCI DSS v4.0](https://www.pcisecuritystandards.org/document_library/?category=pcidss). 

For many risk management frameworks, the system categorization will result in varying levels of hardening guidelines. Using FedRAMP as an example, FIPS-199 defines the security categorization which will result in a baseline set of controls (defined in NIST 800-53) that must be implemented.

Because the NIST 800-53 controls are technology-neutral, the STIGs published by DISA provide technology-specific configurations on how to satisfy the applicable NIST 800-53 control set. As stated in the CM-6 (a) Requirement 1 of the FedRAMP System Security Plan:

_“The service provider shall use the DoD STIGs to establish configuration settings; Center for Internet Security up to Level 2 (CIS Level 2) guidelines shall be used if STIGs are not available; Custom baselines shall be used if CIS is not available.”_

However, the requirements for how a STIG applies to a container image are rather unclear. For example, some controls apply to the host operating system instead of the image. Similarly, other controls apply to the Docker service instead of the container itself. Knowing what controls are relevant for containers and how to check for them in a STIG are key to achieving and maintaining FedRAMP compliance.

DISA understands that containers have different requirements than traditional operating systems. In an effort to highlight these differences, the DOD DevSecOps Initiative released the [Container Hardening Process Guide](https://dl.dod.cyber.mil/wp-content/uploads/devsecops/pdf/Final_DevSecOps_Enterprise_Container_Hardening_Guide_1.2.pdf) which describes the Initiative's approach to hardening images and how other agencies should handle applying STIGs to containers.

[Appendix C](https://dl.dod.cyber.mil/wp-content/uploads/devsecops/pdf/Final_DevSecOps_Enterprise_Container_Hardening_Guide_1.2.pdf#%5B%7B%22num%22%3A65%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22XYZ%22%7D%2C70%2C720%2C0%5D) of the Hardening Process Guide highlights an important point about STIG compliance for containers:

_"With a properly locked down hosting environment, containers inherit most of the security
controls and benefits from infrastructure to host OS-level remediation requirements."_

Deploying containers on a STIG hardened host provides many of the security features that are difficult or sometimes impossible to implement inside a container. What's left then is the application-level security configuration — in particular vulnerability remediation — which Chainguard provides through our guaranteed vulnerability remediation SLAs. 

Once a container has been deployed, you can use tools such as [OpenSCAP](http://www.open-scap.org/tools/) to validate that the container was appropriately hardened. Those scans will return [false positives](/chainguard/chainguard-images/recommended-practices/false-results/) any time they detect missing components inside the container which are inherited from the host where the container is running. As stated in [Appendix D](https://dl.dod.cyber.mil/wp-content/uploads/devsecops/pdf/Final_DevSecOps_Enterprise_Container_Hardening_Guide_1.2.pdf#%5B%7B%22num%22%3A67%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22XYZ%22%7D%2C70%2C720%2C0%5D) of the DSO Initiative's Container Hardening Process Guide:

_"If an OpenSCAP scan returns noncompliant result(s), always evaluate the validity of those findings. False positives are common within major host OS-based containers, as the security profiles normally account for all host-level controls potentially not applicable to a container build (e.g., GUI, CAC authentication, etc.). In addition to false positives, many of the base OS STIG requirements are not applicable in the containers either."_

To sum up, it can be difficult to determine exactly which results are false positives and which ones should be applied to a container. 


## False Positives and the General Purpose OS STIG

Here we've assembled several explanations for requirements from Chainguard's General Purpose Operating System STIG that are likely to cause false positives when scanning containers, as well as the rationale for those requirements. By disambiguating these false positives, the following sections should be helpful to any administrators deploying containers in environments where STIG hardening is necessary both as a means to understand where to expend effort performing hardening and for discussions with assessors and compliance personnel.

### Auditing

Auditing capabilities for Linux containers are implemented by the underlying host's audit configuration. In Linux, the auditing program `auditd` leverages multiple functions in the running kernel through the Linux Auditing System to capture runtime information such as starting and stopping processes, opening sockets, and accessing files.

Linux containers use their host's kernel, making it impossible to install and operate a separate auditing package inside the container itself. Instead, auditing information must be configured and collected through the auditing configuration of the host.

Once configured, logs of container actions are written to the host's audit log files and are readable only by the host superuser account. These logs must be collected from the host for incident response and reporting. Storage capacity limits, audit process monitoring, remote upload of logs, and associated alerts are the responsibility of the host where the containers are running.


### Isolation

Containers provide process isolation by executing their applications in a constrained environment using the Linux Namespace and cgroup subsystems. Inside the namespace, container processes are only permitted to access a limited set of system resources defined when the container is launched.

Processes are further restricted by limits imposed through the cgroup for access to system resources such as system memory or CPU use. Cgroups protect the host resources and other containers running on the host from being impacted by Denial of Service attacks on a targeted container.

Together, namespaces and cgroups isolate security functions of the host operating system from non-security functions of applications running inside the container. This separation makes it possible for container failures to not directly impact the operation of the host and its security functions when caused through processing of invalid inputs or other runtime errors. In the event of a container failure during initialization or shutdown, for example, the host operating system's security capabilities will continue to function as configured.


### Minimal images

Chainguard Images contain only the minimal software needed for the container to perform its intended function. Nonessential capabilities such as package managers, shell environments, executables, and process launching functions have been removed from the images and may not be installed once the container is running.

This limited implementation means that only the necessary software to operate can run on the container and restricts the installation of additional software on the image during operation. Be sure to have fixed permissions on libraries and executable files in place so that any software installed can't be modified.

The host's container execution environment further reduces the risk of unauthorized modification of software through Linux container isolation capabilities including namespaces and cgroups. These restrictions prevent unauthorized modification of the host operating system environment.


### Address Space Layout Randomization (ASLR)

ASLR configuration is the responsibility of the host operating system where containers run. Applications running within a container on a host that has ASLR enabled will automatically be protected by the configuration. No additional action is needed to ensure that container-based applications are protected.


### Host firmware

Linux containers inherit the firewall configuration of their host operating system which dictates which ports on the container can be accessed from the network. Selection of which ports to make accessible on the applications running on the container is the responsibility of the host firewall configuration — an additional application-level firewall inside the container is not necessary.


### Host filesystem

Linux containers use the host's filesystem for storage of their files and configuration. To protect data at rest inside containers from unauthorized access or modification, you must modify the host operating system's configuration. As an example, one might set up encrypted virtual filesystems. The host filesystem is also responsible for the size, utilization, and capacity of the physical disks that are used by containers running on that host. 


### Vulnerability scanning

The team deploying the container is also responsible for scanning it for vulnerabilities. This scanning can be executed from the host operating system or against the container image when it is stored in a registry. Continuous scanning can be used to detect vulnerabilities that have been identified / announced since the previous scan and determine when updated images should be built and deployed in the environment.


### Time

Linux containers inherit the system time from the underlying host; likewise, containers don't operate their own separate time services. The host owner is responsible for configuring the host's time service to generate the timestamp used by its auditing system, perform periodic synchronization, and ensure that only authorized time servers are used as the authoritative source. Time synchronization of the host clock is automatically reflected in the time used by the container.


### STIGs

These containers can be validated against the General Purpose Operating System STIG and other applicable STIGs using the [OpenSCAP toolset](http://www.open-scap.org/tools/). OpenSCAP can validate configuration of container images by reviewing the configuration of the image filesystem and can perform interactive checks by executing commands against running containers.


## Learn more

You can access Chainguard's General Purpose Operating STIG through the Early Access Program. If you’re interested in participating in the program, please fill out the [interest form](https://docs.google.com/forms/d/e/1FAIpQLSdKqtAziDyLpTtQw5v77orKup5jap0QP1T-VrAj4g32Y1pE6w/viewform?utm_source=blog&utm_medium=website&utm_campaign=FY25-EC-Blog_sourced) or email [compliance@chainguard.dev](mailto:compliance@chainguard.dev).

If you'd like to learn more about how Chainguard Images can help you meet FedRAMP compliance, we encourage you to refer to our overview of [Chainguard's FIPS-ready Images](/chainguard/chainguard-images/working-with-images/fips-images/).