---
title: "How does Chainguard Libraries plug into a developer's workflow?"
linktitle: "Libraries Developer Workflow"
type: "article"
description: "Interview with Dustin Kirkland explaining how Chainguard Libraries integrate seamlessly into existing developer workflows"
date: 2025-08-02T16:00:00+00:00
lastmod: 2025-08-02T16:00:00+00:00
draft: false
tags: ["Chainguard Libraries", "Video", "Integration"]
images: []
menu:
  docs:
    parent: "chainguard-libraries"
weight: 070
toc: true
contentType: "product-docs"
---

{{< youtube SBisxaL855k >}}

## Transcript

**Interviewer**: So Dustin, how does Libraries actually plug into a developer workflow?

**Dustin Kirkland**: Yeah, so I used the word "hydrate" earlier. We hydrate typically a JFrog Artifactory or a Cloudsmith—we hydrate that registry of artifacts with Chainguard securely built artifacts. And we produce this constant flow of tens of thousands of those library version tuples into that environment. And our customers can come to us and get a license for our entire Java ecosystem or our entire Python ecosystem.

So from that sense, we're certainly not an artifact registry. You use the artifact registry that's typically used inside of your organization. We help populate that with secure artifacts. This is fairly similar to our approach with containers, where we're not a scanner, but what we're trying to do is complement the scanners that you have with better containers that have fewer CVEs, and you end up with cleaner scan results. So in this artifact sense, we're not an artifact registry, but we're putting better binaries into that artifact destination.

**Interviewer**: So once the artifact registry is set up, is there any changes to actual developers' workflow, or will it just work?

**Dustin Kirkland**: Typically not. I mean, if inside of your organization you already have an artifact registry and your developers are pip installing or maybe even importing those classes and libraries from that artifact repository, we're just replacing the artifacts that may have additional vulnerabilities or potentially malicious code with artifacts that have fewer vulnerabilities and are immune to that malicious code.
