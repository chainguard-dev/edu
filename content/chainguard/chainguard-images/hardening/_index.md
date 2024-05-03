---
title: "Chainguard Images Hardening"
linktitle: "Hardening"
description: "Conceptual articles outlining how Chainguard Images are hardened and tested"
type: "article"
date: 2024-04-23T08:49:15+00:00
lastmod: 2024-03-23T08:49:15+00:00
draft: false
images: []
weight: 250
---

Chainguard's approach to hardening is consistent with high-reliability practices across the tech ecosystem. As the NSA put it in its [AI System Security guidance](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/3741371/nsa-publishes-guidance-for-strengthening-ai-system-security/): "Adopt a [zero trust] mindset, which assumes a breach is inevitable or has already occurred." 

Individual security controls are fallible, and [zero-days](/software-security/glossary/#zero-day) do happen. For this reason, we embrace a defense-in-depth model where we apply complementary and overlapping security controls. This way, when a single layer fails, the other layers provide a measure of redundant protection. 

This conceptual article provides a high-level snapshot of the layers of defense Chainguard currently has in place, and how they allow for the production and delivery of hardened Chainguard Images.

## Process segmentation overview

Chainguard owns every step of its image production pipeline end-to-end.

![Diagram outlining Chainguard's Image production pipeline. At the left is an object labeled "Source". To the right, an arrow from this points to another object labeled "APK". Another arrow points from the right of the APK object to yet another object labeled "OCI". Lastly, four arrows extend from the right of the OCI object to four more stacked objects. These are also labeled "OCI" to represent the images distributed to customers.](hardening-guide-1.png)

First, we fetch source code from upstream Git repositories and turn it into [Alpine Package Keeper (APK)](https://wiki.alpinelinux.org/wiki/Apk_spec) packages. We then assemble those APK packages into [Open Container Initiative (OCI)](https://opencontainers.org/) images before distributing them to our customers.

To ensure integrity across these states, Chainguard's systems rely on cryptographic hashing and signatures:

 * Our packaging pipelines always start with [a source fetch based on an immutable reference](https://slsa.dev/spec/v0.1/requirements#hermetic), which ranges from SHA1 to SHA512. The resulting APKs are signed with a strong signing key in a trusted control plane.
* Our image builds verify these APK signatures when assembling those APKs into OCI-compliant container images. The resulting OCI images are signed and attested using the [Sigstore project](https://www.sigstore.dev/).
* Our signed OCI images are then distributed to our customers’ private repositories in accordance with what they have access to. Upon delivery, Chainguard can optionally send a [CloudEvents](/chainguard/administration/cloudevents/) webhook to customer subscription endpoints. The CloudEvent webhook carries an [Open ID Connect (OIDC)](https://openid.net/developers/how-connect-works/) token authorizing the event as from Chainguard, for that particular customer, and including a cryptographic hash of the event payload in a custom OIDC claim.

As an aside, you may have noticed that the **only** checksum in this flow that isn’t signed is the source code. We noticed this too, which is why Chainguard created (and subsequently donated to Sigstore) the [Gitsign](https://docs.sigstore.dev/signing/gitsign/) project to help close this gap.

Put briefly: we at Chainguard take cryptographic verification of artifacts traversing our supply chain seriously. Let’s go over each of these steps in greater detail to better understand how we layer defenses into the process wherever possible.

### Source

![Portion of the previous diagram, showing just the "Source" object and the arrow pointing from its right.](hardening-guide-2.png)

The Chainguard software engineer who creates the initial package definition determines the initial source code checksum. That developer also generally configures a small declarative block which tells our automation how to identify when new versions of the upstream software package become available. This allows our automation to both confirm that the original source checksum matches expectations and to update the checksums for new versions as they are released.

To track software updates, our automation ties into several systems including the GitHub API, [Release Monitoring](https://release-monitoring.org/), and [End-of-Life](https://endoflife.date/).

Regardless of the source of the changes, package updates all flow through our Pull Request process. Any package definition changes are reviewed by a Wolfi maintainer, a dry-run of the package build is performed, and a battery of checks are performed that surface additional signal to the reviewer. We'll go over these checks in greater detail in the following sections.

### Source to Package

![Portion of the first diagram, this one showing the "Source" object with an arrow pointing to the "APK" object.](hardening-guide-3.png)

Chainguard defines the process of turning an “immutable reference” to an upstream project into a set of APK packages in one of our [melange configurations](/open-source/melange/). Melange allows the package’s author to run an upstream project’s build process and then carve up the resulting build artifacts into a number of sub-packages.
 
In order to support minimal packages, we generally divide up the resulting APK packages in accordance with the granularity with which the constituent pieces might be independently consumed. As an example, a project may have a CLI, a shared library, man pages, and headers. This fine slicing ensures that when it is time to assemble an image from a set of our packages, we only pull in what is necessary for a truly minimal image.

As part of our hardening process, we pass a number of flags to various toolchains to increase security. One example of how Chainguard goes beyond what most other Linux distributions do for security is that we pass `-D_FORTIFY_SOURCE=3` to our C++ toolchains. Additionally, we use immediate symbol binding at runtime (-Wl,-z,now) and read-only relocations (-Wl,-z,relro).

In order to shift quality control to the “left” our package definitions also carry a place where package authors can define tests. These tests must pass before a new version of the package is merged and released. We are also investing in [memory-safe alternatives for certain packages](https://www.chainguard.dev/unchained/building-the-first-memory-safe-distro-wolfi), to which we assign a higher priority so that the APK solver prefers them to less safe variants.

Finally, as part of living our values of _treating our development platform like a production system_, we “[eat our own dogfood](https://en.wikipedia.org/wiki/Eating_your_own_dog_food)”, a practice also known as "dogfooding." Package builds happen within [ephemeral](https://www.chainguard.dev/unchained/the-principle-of-ephemerality) containers that are defined as the build-time dependencies of the final package in the [melange configurations](/open-source/melange/). 

By dogfooding, we enable ourselves to tap into Chainguard's own value proposition in ways that give us a high-level view of ephemeral build environment hardening:

* Our ability to produce [minimal](https://www.chainguard.dev/unchained/the-principle-of-minimalism) containers means these build environments have a smaller surface than virtually any other build environment.
* The few packages that do get included benefit from our Low/No CVE SLA.

In addition to this, we have a disciplined separation of our build’s “trusted supervisor” orchestration layer from the “untrusted guest” execution layer. This ensures a strong separation between privileges or credentials and the execution of any untrusted or unreviewed code.

### Package

![Another portion of the first diagram, showing the "APK" object with an arrow pointing to its left side and another arrow pointing from its right side.](hardening-guide-4.png)

There are two main states that a package exists in that merit discussion: a throwaway build performed pre-submit, and a release build that is produced and signed post-submit.

We run a battery of checks across packages in both of these states. The throw-away package builds are analyzed as part of the pull-request workflow and any results are surfaced to the author and reviewer (given the context, these are often presented as a diff against a previous release build of the package).

The release builds are continuously analyzed to ensure that we can flag any issues we missed as our tooling improves. The set of checks performed generally have a good deal of overlap to avoid only discovering things after a package has merged. The main purpose of the tooling checks is to catch issues that only come to light after things have been built; for example, a previously unknown CVE.

One of the key analyses we perform is to run CVE scans over our packages. This ensures that new package builds and updates to existing packages satisfy our SLA before they're merged. We continuously monitor our release package builds to measure our SLA and trigger CVE remediation as new vulnerabilities come up.

In addition to CVEs, a common request we get from our users is around scanning for malware. To fill this gap, Chainguard has a tool called [`bincapz`](https://www.chainguard.dev/unchained/the-principle-of-minimalism) that includes over 12k [YARA](https://github.com/VirusTotal/yara) rules for both detecting malware and attempting to classify the syscalls performed by applications.

As package updates come in, we use `bincapz` to analyze the binaries included in the package and enable the code reviewer to assess whether the upstream software potentially includes changes in capabilities. For instance, [in this pull request](https://github.com/wolfi-dev/os/pull/16172), it flagged an update to Qt that introduced the symbol `interceptor_vfork` to detect when it is running under asan/msan:

![Screenshot from the linked pull request showing what bincapz flagged in the Qt updates. This guide specifically calls attention to a medium risk issue found in a change to qt6-qtbase/usr/lib/libQt6Core.so.6.7.0.](hardening-guide-5.png)

Here, bincapz reports the introduction of this symbol in the upstream source diff:

![Screenshot of a GitHub diff, as reported by bincapz.](hardening-guide-6.png)

Once a Wolfi maintainer has reviewed package changes and the assorted signals extracted by our automation, it is merged and a new release build of the package is performed (as outlined in the Source to Package section) and then the final package is signed and added to our APK repository. If a maintainer is required to make any manual changes to the package update — such as fixing a broken build or patching CVEs — then a different reviewer must approve those edits before it can be merged.

### Package to Image

![The next portion of the first diagram in this article, showing the "APK" object, with an arrow pointing from its right to the "OCI" object.](hardening-guide-7.png)

To help ensure that our images are up to date, we rebuild our full image directory nightly. We trigger builds immediately on image definition changes, and frequently throughout the day to pick up any package changes (see previous sections).

Our image build process is driven by [apko](https://github.com/chainguard-dev/apko), a highly differentiated tool purpose-built by Chainguard to produce OCI images from a declarative configuration. apko is designed to include the minimum transitive closure of dependencies from some core list of packages. This is a key facet of why finely slicing packages is important, as outlined in the previous Source to Package section.

Most Chainguard images are defined  in such a way that this "core list of packages" is a single application. This means that everything included in the final image is either a result of a dependency the application has or that we've inadequately sliced a package; we can fix the latter cases as we become aware of them. In addition to minimizing the number of packages, the vast majority of Chainguard images default to a **nonroot** user.

Chainguard’s tooling for producing minimal images is able to produce an enormous breadth of minimized application and base images while also remaining functional and fully compatible with SCA tooling. Due to this minimalism, our images [accumulate CVEs more slowly than alternatives](https://www.chainguard.dev/unchained/enforce-against-vulnerability-sprawl-with-up-to-date-images), and are less susceptible to “living off the land" attacks.

Once we have assembled an image, we publish it by digest to our registry. We then sign the image so that our customers can verify an image came from our release process. We also attest to several important properties, including our images' [SBOMs](/chainguard/chainguard-images/images-features/retrieve-image-sboms/), their [SLSA provenance](https://www.chainguard.dev/unchained/scaling-chainguard-images-with-a-growing-catalog-and-proactive-security-updates), and the ["locked" image configuration used to produce each image](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Image

The Image stage is similar to the Package stage in that we run a number of analyses on our images to ensure we are satisfying our SLAs and that our images are of high quality.

First, we verify that we can reproduce a bitwise-equivalent image from the locked configuration using a parallel toolchain. This reproducibility enables our users to be able to audit our image provenance. Since we confirm this reproducibility with a separate `apko` toolchain, it would require an attacker to compromise both form factors of our `apko` toolchains to evade detection.

From there, we move on to more testing to qualify that the produced images work as intended. For complex containerized applications, which consist of several distinct containers, we test them as a single unit (in the case of kyverno, cert-manager, etc).

We will generally test things in form factors consistent with how our customers are consuming them. As an example, images that run on Kubernetes are deployed with their accepted Helm chart on ephemeral clusters and functionally validated. Likewise, for images representing applications with well known conformance benchmarks, [we ensure these benchmarks are run and validated](/chainguard/chainguard-images/images-testing/) periodically.

We have users in a variety of regulated industries (including Federal, Finance, Health Care, Transportation, Critical Infrastructure), which impose assorted hardening requirements on the software they deploy. To satisfy our customers’ compliance requirements, the produced images are then benchmarked against popular compliance frameworks, with our current focus being on 
[STIGs](https://en.wikipedia.org/wiki/Security_Technical_Implementation_Guide) and [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks). This added benchmark validation is yet another security layer that's especially relevant for compliance auditors and organizations looking to pass audits.

The availability of benchmarks varies by image. As a baseline, all images are benchmarked against the General Purpose Operating System (GPOS) [Security Requirements Guide (SRG)](https://www.stigviewer.com/stig/general_purpose_operating_system_security_requirements_guide/), using the underlying “OS” as the system in question. This ensures general evidence is available for comment requirements such as [FIPS](/chainguard/chainguard-images/images-features/fips-images/#what-is-fips). For images where a dedicated SRG is present (such as PostgreSQL), an additional SRG is implemented alongside the GPOS SRG. 

Only after the image is published, signed, attested, and has passed all of these qualifications, will we tag them. For our [Developer Images](/chainguard/chainguard-images/overview/#production-and-developer-images), this makes them available immediately. 

### Image to Customer

![The final portion of the diagram, showing the single "OCI" image with several arrows extending from its right pointing to several other "OCI" objects, representing OCI images being delivered to customers.](hardening-guide-8.png)

As images are published to our private image directory `cgr.dev/chainguard-private`, our “catalog syncer” looks up customers that have access to each new image and the new image is distributed to users' private repositories; for example, `cgr.dev/example-user.org`.

As mentioned previously, users can configure real-time CloudEvent notifications so that as their images are copied into their Chainguard repositories, they can take action. We have samples demonstrating how to mirror these images to [ECR](https://github.com/chainguard-dev/platform-examples/tree/main/image-copy-ecr) or [GCR](https://github.com/chainguard-dev/platform-examples/tree/main/image-copy-gcr) based on these events. Also, note that this is how our [integration with DockerHub](https://www.chainguard.dev/unchained/chainguard-images-now-available-on-docker-hub) works. 

## Underlying Production Infrastructure

We take our production practices extremely seriously, and we treat our development platform with the same level of production rigor. This includes practices discussed previously, such as ephemerality, minimalism, immutability, and more.

Chainguard created its own Security Token Service for Github called [Octo STS](https://github.com/apps/octo-sts) to allow us to leverage short-lived credentials brokered with trust relationships, a much more secure solution than long-lived credentials which are prone to leaks.

We've also implemented a "zero trust" architecture, meaning that our image production structure doesn't grant any implicit trust to assets or user accounts. 

As an example, suppose the cloud platform where Chainguard is running was fully compromised by malicious actors. If our users are verifying whether the signatures of the images they receive from us were indeed produced by our release automation, they will get an alert when those signatures don’t match. In this case, the only feasible attack one could mount without immediate detection would be a replay attack, and even this could be mitigated with “build horizon” policies around the age of images.

This is one of the reasons why we're such big fans of cryptographic content-addressing and signing: your blob storage could be fully compromised and the worst case scenarios are Denial-of-Service or Replay attacks.

## Putting it all together

With our end-to-end ownership of this delivery pipeline (including a great deal of its tooling), we are able to gain considerable visibility into the software supply chain. 

While we are deeply committed to making it incredibly difficult for any bad packages to make it through our gauntlet of security layers, we are also committed to building the tools we need to recall anything that inevitably makes it through.

## Learn more

Chainguard offers FIPS-enabled versions of a number of its images which, in addition to the hardening features outlined here, use FIPS-validated cryptography. Refer to our overview of [FIPS-enabled Chainguard Images](/chainguard/chainguard-images/images-features/fips-images/) to learn more.

You may also be interested in our article on [How Chainguard Images are Tested](/chainguard/chainguard-images/images-testing/). If you have other questions about Chainguard Images, you may find our [Frequently Asked Questions](/chainguard/chainguard-images/faq/) to be helpful. 
