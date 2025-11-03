---
title: "How does Chainguard Libraries help developers?"
linktitle: "How Libraries Help"
type: "article"
description: "Interview with Dustin Kirkland about the benefits Chainguard Libraries provide to developers"
date: 2025-08-02T16:00:00+00:00
lastmod: 2025-08-02T16:00:00+00:00
draft: false
tags: ["Chainguard Libraries", "Video", "Overview", "Recommended Practices"]
images: []
menu:
  docs:
    parent: "chainguard-libraries"
weight: 070
toc: true
contentType: "product-docs"
---

{{< youtube yvo2SyUeaJM >}}

## Transcript

**Interviewer**: So how does Chainguard Libraries help developers?

**Dustin Kirkland**: Yeah, so building off of that Chainguard Factory, we've actually repurposed all of that automation to not just build packages and containers, but actually fetch libraries directly from their upstream source and recompile those Java binaries—JARs—and those Python binaries—wheels—in a new format, or in the same format rather, but totally bootstrapped from source. The fact that we can rebuild those libraries means that we can actually patch them if necessary.

Now, in doing so, we've created an entire repository of Python wheels and Java JARs that we can publish and hydrate into a customer's environment, so that their developers can retrieve their libraries from a secure source, from a trusted source, and avoid malicious packages—deliberately modified or intentionally compromised packages—which, you know, we find in PyPI.org or in Maven Central from time to time. But Chainguard building those from source ensures that that entire open source ecosystem is secured in the same way that we're securing the packages and the container ecosystems.
