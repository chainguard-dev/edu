---
title: "What Is a Build Horizon?"
linktitle: "Build Horizon"
description: "What a build horizon is and why enforcing maximum artifact age is a key practice for keeping software secure and up to date"
lead: "A guide to build horizons and enforcing artifact freshness"
type: "article"
date: 2026-03-16T00:00:00+00:00
lastmod: 2026-03-16T00:00:00+00:00
contributors: ["Chainguard"]
draft: false
tags: ["Conceptual"]
images: []
menu:
  docs:
    parent: "software-security"
weight: 15
toc: true
---

A _build horizon_ is the maximum amount of time a build artifact — such as a compiled binary or container image — is permitted to remain in use before it must be rebuilt. Once an artifact exceeds its build horizon, it is considered stale and must be regenerated from up-to-date sources.

The practice has been adopted broadly to maintain production hygiene, reduce technical debt, and limit exposure to vulnerabilities in aging dependencies.

## Why Build Horizons Matter

Software artifacts do not exist in isolation. They encode the state of their dependencies — base images, libraries, language runtimes, and operating system packages — at the time they were built. As time passes, new vulnerabilities are discovered in those dependencies, fixes are released, and the artifact falls behind the current security baseline.

Without a policy that enforces a maximum artifact age, old builds can quietly persist in production long after their dependencies have become insecure. This is especially common with infrastructure services and long-running background jobs, where the pressure to ship new features is lower and images are less likely to be rebuilt as a side effect of application changes.

Build horizons address this by making staleness a first-class concern. Rather than relying on developers to proactively update artifacts, a build horizon policy makes freshness a default requirement.

## What a Build Horizon Applies To

Build horizon practices apply across three broad categories of artifacts:

**Internal software** — services and tools your organization builds and owns. A continuous delivery philosophy encourages frequent delivery of small changes, which naturally limits artifact age. A build horizon formalizes this expectation and makes it enforceable.

**Off-the-shelf components** — third-party software such as Prometheus, Flux, the OpenTelemetry Collector, or Cilium that is deployed as-is inside your infrastructure. These components are often deployed and then forgotten, making them prime candidates for staleness.

**Compiled dependencies, including base images** — the foundational layers on which your software is built. A container image inherits all of the packages in its base image, which means an outdated base image can silently introduce hundreds of known vulnerabilities into an otherwise current application.

## The Principle of Ephemerality

Build horizons are most effective when paired with [the _Principle of Ephemerality_](https://www.chainguard.dev/unchained/the-principle-of-ephemerality): the idea that build artifacts should be treated as temporary by design, expected to be regularly discarded and regenerated rather than maintained indefinitely.

Under this principle, the goal is not to keep an artifact running as long as possible but to make the process of rebuilding it so reliable and automated that freshness becomes the default state. When rebuilding is routine, there is little cost to enforcing a short build horizon.

## Automating Dependency Updates

Enforcing a build horizon at scale requires automation. Manual processes are insufficient when an organization manages dozens or hundreds of services and dependencies. Common automation strategies include:

- **Dependency update bots** such as Dependabot, Renovate, or similar tools that open pull requests to upgrade library dependencies as new versions are released.
- **Base image update automation** — tools that monitor upstream base images and automatically trigger rebuilds or open pull requests when new image digests are published.
- **Scheduled rebuilds** — CI/CD pipelines configured to rebuild images on a regular cadence (for example, nightly or weekly), regardless of whether application code has changed.

These approaches reduce the manual burden of staying current and ensure that most artifacts are refreshed before they approach their horizon.

## Enforcing the Policy

Automation reduces drift, but it does not eliminate it entirely. Misconfigurations, forgotten services, and exceptions that outlive their justification can all result in artifacts exceeding their build horizon. Policy enforcement provides a backstop.

In Kubernetes environments, build horizon policies can be enforced using admission controllers. The [sigstore/policy-controller](https://docs.sigstore.dev/policy-controller/overview/) project, for example, exposes the `fetchConfigFile` function to inspect the `created` timestamp embedded in a container image's configuration. A policy written in [Rego](https://www.openpolicyagent.org/docs/latest/policy-language/) can then validate that the image was built within the permitted window:

```rego
isCompliant {
  created := time.parse_rfc3339_ns(input.config[_].created)
  time.now_ns() < created + maximum_age
}
```

This policy can be wrapped in a `ClusterImagePolicy` resource that scopes enforcement to specific namespaces or workload selectors. Policies can initially be configured in _warn_ mode, which surfaces violations as warnings without blocking deployments, giving teams time to remediate before strict enforcement is enabled.

## A Note on Reproducible Builds

Build horizon policies that rely on the `created` timestamp in a container image can fail for images produced with [reproducible build](https://reproducible-builds.org/) tooling. Some reproducible build tools set the `created` timestamp to the Unix epoch — January 1, 1970 — as a way to ensure that builds are deterministic regardless of when they are run. An image with a 1970 timestamp will always appear to exceed any reasonable build horizon.

The recommended solution is to use the `SOURCE_DATE_EPOCH` environment variable, which many reproducible build tools support. When set, this variable causes the build tool to derive timestamps from the date of the source commit rather than the current system clock. This preserves reproducibility while producing a meaningful, policy-compatible timestamp.

## Learn More

To learn more about related practices and tools, you can explore:

- [What is software supply chain security](/software-security/what-is-software-supply-chain-security/) — for background on the broader threat landscape that build horizons help address.
- [Selecting a base container image](/software-security/selecting-a-base-image/) — for guidance on choosing base images that are rebuilt frequently and carry few known vulnerabilities.
- [Strategies and Tooling for Updating Container Containers](/chainguard/chainguard-images/staying-secure/updating-images/strategies-tools-updating-images/) — which outlines different strategies and tools for keeping images up to date and avoiding the use of end-of-life software.
- [Reproducible Builds](https://reproducible-builds.org/) — for information on the reproducible builds initiative and the `SOURCE_DATE_EPOCH` convention.
