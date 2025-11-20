---
title: "Chainguard VMs Overview"
linktitle: "VMs Overview"
description: "Chainguard VMs are designed for minimalism, security, and operational clarity."
type: "article"
date: 2025-10-21T08:04:00+00:00
lastmod: 2025-10-21T15:09:59+00:00
draft: false
tags: ["Chainguard VMs", "Overview"]
menu:
  docs:
    parent: "vms"
weight: 001
toc: true
---

Chainguard VMs offer a minimal and verifiable foundation for running ephemeral workloads in cloud and on-prem hypervisor deployments, designed to complement and extend the same secure-by-default philosophy found in [Chainguard Containers](https://edu.chainguard.dev/chainguard/chainguard-images/overview/). With a strong focus on rapid CVE remediation and a small attack surface, Chainguard VMs are purpose-built to service the target workload and include only the packages that are essential for its operation.

Built in the Chainguard Factory, Chainguard VMs benefit from a highly automated, secure-by-design build pipeline that ensures consistent, reproducible artifacts. This streamlined process enables the delivery of VM images that are continuously updated to eliminate known vulnerabilities.

## Why Chainguard VMs

Unlike traditional virtual machines, which are often burdened with legacy components, unnecessary packages, and opaque dependency chains, Chainguard VMs are designed for minimalism, security, and operational clarity. Based on Chainguard OS, Chainguard VMs include a kernel that closely tracks the upstream Linux stable tree, ensuring timely updates and compatibility, along with a minimal `systemd` for service management. Consistent with the principle of minimalism, only the essential systemd units required to support the VM’s intended workload are included. Every component is fully traceable, with SLSA guarantees and SBOMs generated at every step, providing end-to-end transparency and helping prevent CVEs from ever entering your environment.

For platform engineers and DevOps teams, this means:

* **Reduce Engineering Toil**: With no unnecessary software to maintain, you reduce noise from non-actionable CVEs and focus only on what matters.
* **Improved boot and runtime security**: Minimal, hardened images reduce the chances of privilege escalation, kernel exploits, and lateral movement.
* **Operational consistency**: The same secure-by-default toolchain that powers Chainguard Containers now extends to your VMs, making it easier to manage and audit infrastructure uniformly across environments.

## VMs and Containers Compared

To understand the applicability of Chainguard VMs to your organization, it might be helpful to compare the features of Chainguard VMs to Chainguard Containers. In a nutshell, the main differences come from the fact that Chainguard VMs boot from and run with their own hardened kernel as part of Chainguard OS, while Chainguard Containers rely on the host system's kernel.

| Feature | Chainguard Container                                   | Chainguard VM                                                                               |
| :---- |:-------------------------------------------------------|:--------------------------------------------------------------------------------------------|
| Includes Kernel? | **No** – uses host’s kernel                            | **Yes** – ships and boots with its own hardened kernel                                      |
| Environment | Userspace only, isolated via namespaces & cgroups      | Full OS, boots in VM with kernel, init, userspace                                           |
| Boot Process | Starts from container entrypoint, no bootloader/kernel | Full bootloader → kernel → init system                                                      |
| Security Boundaries | Dependent on host kernel isolation                     | Stronger isolation via hypervisor and custom kernel controls, secure boot, SELinux policies |
| Use Case Focus | Microservices, CI/CD, ephemeral workloads              | Secure cloud workloads, edge VMs, kernel-level policy control, high performance             |

## Chainguard VM Types

We currently offer 3 distinct types of virtual machine images:

* **Container Host:** a versatile option to run containerized workloads, protecting how you deploy containers on underlying hosts
* **Base:** general purpose VM base images that can be customized to suit your application needs. Current offerings include Chainguard Base, Java Base, and Python Base.
* **Application:** pre-packaged with popular backend applications running as systemd services. We currently offer Nginx, Jenkins, and Squid Proxy Application VMs.

## Availability

Chainguard VMs are currently available for the following platforms / hypervisors:

* Google Cloud Platform (Compute Engine)
* AWS (EC2, ECS, and EKS)
* Microsoft Azure (Azure Compute)
* QEMU/KVM (qcow2/raw)
* VMware vSphere (VMDK)
* Nutanix (qcow2/raw)

Offering broad compatibility, Chainguard VMs allow for deployment in any environment, from public clouds to self-managed infrastructure. This flexibility facilitates one-click deployment across environments and helps prevent vendor lock-in.

[Join the waitlist](https://get.chainguard.dev/vmearlyaccesswaitlist?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement) today to get started.

## Compliance and SLAs

Chainguard VMs (running Chainguard OS) are intentionally designed to minimize risk, maximize transparency, and satisfy security standards such as [CIS Benchmarks](https://edu.chainguard.dev/compliance/cis-benchmarks/), [FedRAMP](https://edu.chainguard.dev/chainguard/chainguard-images/staying-secure/fedramp-considerations/), SOC 2, and others.

* CVE remediation backed by an [industry-leading SLA](https://www.chainguard.dev/legal/cve-policy): 7 days for critical, 14 days for all others
* Consistent, reproducible builds
* Enterprise-grade support for multi-cloud and on-prem
* Verifiable provenance for all included components

## Resources

- [Chainguard VMs](https://www.chainguard.dev/vms)
- [Unchained Blog: Announcing Chainguard VMs: Minimal, Zero-CVE Container Host Images](https://www.chainguard.dev/unchained/announcing-chainguard-vms-minimal-zero-cve-container-host-images)
- [Unchained Blog: Expanding Chainguard VMs: Zero-CVE Application & Base Virtual Machine Images](https://www.chainguard.dev/unchained/expanding-chainguard-vms-zero-cve-application-base-virtual-machine-images-for-cloud-and-on-prem)

## Learn More and Get Started

Chainguard VMs are available through a subscription. To learn more and get started, [join the waitlist](https://get.chainguard.dev/vmearlyaccesswaitlist?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement).
