---
title: "Chainguard VMs FAQ"
linktitle: "FAQ"
description: "Frequently asked questions about Chainguard VMs, including availability, supported ecosystems, compliance, and more"
type: "article"
date: 2025-10-21T08:04:00+00:00
lastmod: 2025-10-21T15:09:59+00:00
draft: false
tags: ["Chainguard VMs", "FAQ"]
menu:
  docs:
    parent: "vms"
weight: 010
toc: true
---

## Which platforms and hypervisors are Chainguard VMs available for?

Chainguard VMs are available for AWS ([EC2](https://aws.amazon.com/ec2/) and [ECS](https://aws.amazon.com/ecs/)/[EKS](https://aws.amazon.com/eks/)), [GCP](https://cloud.google.com/?hl=en) (Compute Engine), and [Azure Compute](https://azure.microsoft.com/en-us/products/category/compute) cloud environments, and also for on-prem solutions based on KVM such as [QEmu](https://www.qemu.org/), [VMWare](https://www.vmware.com/products/cloud-infrastructure/vsphere), [Nutanix](https://www.nutanix.com/), among others.

## What kinds of VMs are currently available?

As part of our initial offering, we’re providing Container Host VMs, Base VMs, and Application VMs. This list should expand as we fine tune the product based on customer feedback.

## What are Container Host VMs and which versions are available?

Container Host VMs allow you to run containerized workloads on a hardened VM runtime. We currently offer container host VMs for AWS Container Services ECS and EKS, and also for native compute instances on AWS EC2, Google Compute Engine, and Azure Compute.

## What are Base VMs and which versions are available?

Base VMs are general purpose VMs that can be customized to suit your application needs. Current offerings include Chainguard Base, Java Base, and Python Base VM images available for native compute instances on AWS EC2, Google Compute Engine, and Azure Compute.

## What are Application VMs and which versions are available?

Application VMs come pre-packaged with popular backend applications running as systemd services. We currently offer Nginx, Jenkins, and Squid Proxy Application VMs available for native compute instances on AWS EC2, Google Compute Engine, and Azure Compute.

## Which operating system is used by Chainguard VMs?

Chainguard VMs are based on [Chainguard OS](https://get.chainguard.dev/chainguard-your-os-whitepaper-0), our minimal Linux distribution initially designed to run on containers and now extended to include a kernel and other components.

## Which Linux kernel is used in Chainguard VMs?

The [Chainguard Factory](/chainguard/factory/overview/) tracks both the stable upstream and the latest LTS (for FIPS) versions of the kernel, building from source to provide the most up-to-date and patched versions.

## Do Chainguard VMs support in-place upgrades?

No, Chainguard VMs do not support in-place upgrades (e.g. via package upgrade). The upgrade strategy is based on node replacement.

## How does FIPS work on VMs?

In Virtual Machines, FIPS is traditionally dependent on the Linux kernel, which requires engineers to provision dedicated hardware and virtual machines (VMs) with the host kernel configured in FIPS mode in order to be compliant. Using a FIPS validated Linux kernel allows VMs to provide FIPS graded cryptography for use cases like Disk Encryption, IPSec, KMSV, dm-verity, dm-integrity, among others.

This design, which requires maintenance of FIPS cryptographic boundaries at the kernel-level, drives significant friction for vendors delivering FIPS compliant workloads for modern cloud-native applications, since it forces a dependence on a limited set of FIPS-enabled kernels. With kernel FIPS you often need separate, kernel-pinned images (and careful reboots) to keep the validated stack intact.

Making the cryptographic module user-space or [kernel independent](https://www.chainguard.dev/unchained/kernel-independent-fips-images) breaks that coupling, so the same validated module can serve many VMs and kernels with less toil and fewer surprises.

## Do Chainguard VMs support FIPS?

Yes, Chainguard VMs support **kernel independent FIPS**. This means that application workloads use a FIPS validated entropy source independent of the kernel. The advantage to this approach is that the certification of the entropy source does not need to be performed against a specific kernel, so customers can take advantage of new kernel features while remaining FIPS compliant. It also means that VMs no longer need to be booted in FIPS mode.

Note that with kernel independent FIPS, some low level operating system functions such as disk encryption, IPSEC, KMSV, among others do not use FIPS validated entropy. This is less relevant on cloud platforms, since disk volumes are encrypted with FIPS validated entropy, as is network and filesystem encryption. On the cloud, kernel independent FIPS is a more efficient way of servicing FIPS workloads in VMs.
