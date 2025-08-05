---
title: "Can anybody build Chainguard Containers themselves?"
linktitle: "Can Anybody Build Containers"
type: "article"
description: "Dustin Kirkland discusses whether users can build Chainguard Containers on their own"
date: 2025-08-02T16:00:00+00:00
lastmod: 2025-08-02T16:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Video", "Procedural", "Overview"]
images: []
menu:
  docs:
    parent: "about"
weight: 050
toc: true
---

{{< youtube 5WGfroCpyn0 >}}

## Transcript

**Interviewer**: But everything is open source—can anybody build the images themselves?

**Dustin Kirkland**: Anyone certainly can. It does take quite a bit of expertise to get that to build the first time, and we've structured an entire engineering organization around building things the first time.

When we get new requests from either internal Chainguard or our existing customers or our new prospects, it goes through a process by which we analyze that source code. We grade it, we ensure that it's well-maintained, that it's actively maintained, that we can build it from source, that we can use it and distribute it according to its licenses.

Once that's all graded and approved, we then apply our build tools and our build expertise and get it to build. And sometimes that can take days to weeks or even months in the most complicated build system cases. But then once we do that, we then have the automation to do that constantly, every single time those open source projects tag a new release. That's not manual for us—that's the Factory and the Factory automation that's working on our behalf.

And what you'll find—we find often in the do-it-yourself approach—is that's actually a manual process where there's a human, a maintainer, a security engineer, or project maintainer who's responsible for doing that. And doing that at scale, you really hit the limits of what a human has time to do in a given day or a week.