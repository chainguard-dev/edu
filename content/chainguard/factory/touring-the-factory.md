---
title: "Touring the Chainguard Factory"
linktitle: "Factory Tour"
type: "article"
description: "Take a guided tour through the Chainguard Factory with Dustin Kirkland to see how secure software is built"
date: 2025-08-02T16:00:00+00:00
lastmod: 2025-08-02T16:00:00+00:00
draft: false
tags: ["Chainguard Factory", "Video", "Overview"]
images: []
menu:
  docs:
    parent: "chainguard-factory"
weight: 030
toc: true
---

{{< youtube gg_EdCrhzL4 >}}

## Transcript

**Interviewer**: So Dustin, can you give us a quick tour of the Chainguard Factory?

**Dustin Kirkland**: Yeah, so the Chainguard Factory is the automation that we have inside of Chainguard itself that is able to reproducibly build thousands of open-source projects. 

We start from a fully bootstrapped-from-source version of the source code. We pull the source code down, we apply our build rules, build that code, test that code, sign that code, and publish that code—first as packages.

And then we take those packages and put them into various different form factors. In the nominal case, we put them into container images that typically run inside of a Docker or Kubernetes. But we also can take those same packages and build virtual machine appliances, fully booting with a Linux kernel. And then we also twist some of these into libraries, also built entirely from source.