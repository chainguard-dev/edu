---
title: "What is the Chainguard Factory?"
linktitle: "What is the Factory"
type: "article"
description: "Dustin Kirkland explains the concept and purpose of the Chainguard Factory"
date: 2025-08-02T16:00:00+00:00
lastmod: 2025-08-02T16:00:00+00:00
draft: false
tags: ["Chainguard Factory", "Overview", "Video", "Security"]
images: []
menu:
  docs:
    parent: "chainguard-factory"
weight: 001
toc: true
contentType: "product-docs"
---

{{< youtube KyO4ppSR9Lo >}}

## Transcript

**Interviewer**: So Dustin, can you explain what the Chainguard Factory is?

**Dustin Kirkland**: Yeah, so the Chainguard Factory is the automation that's at the heart of what we do here at Chainguard. Essentially, we have this build system that's constantly monitoring over 10,000 open source projects, and the moment that any upstream maintainer tags a new release, our automation springs into action—fetching that source code, checking the checksums, applying our build rules, rebuilding and recompiling that software, retesting that software at the package and unit level.

And then, if all of that works, publishing a new package with signatures of that package that's been rebuilt from source, bootstrapped from source with our toolchain and our testing. 

Once we have that package, we're then able to assemble that package into multiple different image formats. We can do container images, we can do virtual machine images, and we're now building libraries—Java, Python, and Node libraries—from source.
