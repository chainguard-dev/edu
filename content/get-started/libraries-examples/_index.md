---
title: "Libraries examples"
linktitle: "Libraries examples"
lead: ""
description: "Swap in your first secure dependency with Chainguard Libraries: a quickstart plus ecosystem overviews for Java, JavaScript, and Python."
type: "article"
date: 2026-06-26T00:00:00+00:00
lastmod: 2026-08-06T19:08:57+00:00
draft: false
images: []
weight: 025
crosslinks:
- title: "Quickstart: swap in a library"
  url: "/chainguard/libraries/quickstart/"
- title: "Java overview"
  url: "/chainguard/libraries/java/overview/"
- title: "JavaScript overview"
  url: "/chainguard/libraries/javascript/overview/"
- title: "Python overview"
  url: "/chainguard/libraries/python/overview/"
---

Point your package manager at Chainguard, reinstall, and ship — no breaking changes. Chainguard Libraries are rebuilt from verified source as drop-in replacements for the packages you already use.

These on-ramp guides link to the published Chainguard Libraries documentation. Libraries are currently available for **Java**, **Python**, and **JavaScript** — a reader on another ecosystem can still build with [Chainguard Containers](/get-started/containers-examples/).

## On-ramp guides

- **[Quickstart: swap in a library](/chainguard/libraries/quickstart/)** — point your package manager at Chainguard, reinstall, and ship.
- **[Java](/chainguard/libraries/java/overview/)** — which Maven Central artifacts Chainguard rebuilds, and how Maven and Gradle reach them.
- **[JavaScript](/chainguard/libraries/javascript/overview/)** — which npm packages Chainguard rebuilds, and how npm, pnpm, Yarn, and Bun reach them.
- **[Python](/chainguard/libraries/python/overview/)** — which PyPI packages Chainguard rebuilds, and how pip, uv, and Poetry reach them.

Moving an existing project rather than starting a new one? The [migration guides](/get-started/migration/) cover that path.

## Example projects

For hands-on testing, each ecosystem has a demo repository with example projects you can clone and run:

- **[Chainguard Libraries for Java](https://github.com/chainguard-demo/chainguard-libraries-java)** — Maven and Gradle projects, including a Spring Boot application and CVE remediation demos.
- **[Chainguard Libraries for JavaScript](https://github.com/chainguard-demo/chainguard-libraries-javascript)** — npm, pnpm, Yarn, and Bun examples, each with a `demo.sh` script.
- **[Chainguard Libraries for Python](https://github.com/chainguard-demo/chainguard-libraries-python)** — pip, uv, and Poetry examples, each with a `demo.sh` script.
