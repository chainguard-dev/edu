---
title: "Chainguard Checks overview"
linktitle: "Overview"
description: "Learn how Chainguard Checks runs your repository's CI checks in isolated microVMs on every GitHub pull request, with no network access unless a check asks for it."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-08T00:00:00+00:00
draft: false
tags: ["Chainguard Checks", "Overview", "GitHub"]
images: []
menu:
  docs:
    parent: "checks"
    identifier: "Checks Overview"
toc: true
weight: 10
---

Chainguard Checks runs your repository's CI on Chainguard's infrastructure instead of on GitHub Actions runners. You define your checks, such as linting and tests, in a `.chainguard/ci.yaml` file in your repository. On every pull request, Chainguard Checks runs each check in its own microVM, built on Chainguard OS, and reports the results on the pull request as GitHub checks.

CI runners usually hold long-lived secrets and can reach the whole internet while they run untrusted code, such as a pull request's changes or a compromised dependency. In Chainguard Checks, each check runs in a fresh VM that has no long-lived credentials, and no network access unless the check lists the hosts it needs.

{{< beta feature="Chainguard Checks" access="organizations that start a free trial with `chainctl develop init`, or that arrange access with their Chainguard account team" >}}

## How Checks works

Chainguard Checks reaches your repositories through the Chainguard App, a GitHub App that you install on your GitHub organization or personal account. When you link that account to your Chainguard organization, each repository that has a `.chainguard/ci.yaml` file, or a `.chainguard/ci/` directory, opts in to Chainguard Checks.

When someone opens or updates a pull request, the following happens:

1. Chainguard Checks plans a run against the commit GitHub would create by merging the pull request into its base branch, so each run tests the change together with the latest base branch.
2. It reads the configuration from that merged commit, so a pull request can add checks or change them.
3. Each check runs in its own microVM with the packages your configuration file declares.
4. It reports a summary check named **Chainguard Checks (presubmit)** on the pull request, plus one GitHub check for each of your checks.

Each new push to the pull request cancels the run for the previous push and starts a new one. Chainguard Checks can also run checks on each new commit on your default branch, for work that should run after a change merges. Refer to [Use Chainguard Checks on GitHub](/chainguard/checks/github/) for details.

Here's a minimal `.chainguard/ci.yaml` file for a Go repository:

```yaml {title=".chainguard/ci.yaml"}
version: 1
environment:
  packages: [go]
checks:
  vet:
    cmd: go vet ./...
  test:
    cmd: go test ./...
    network:
      egress: [proxy.golang.org, sum.golang.org]
```

This file installs Go in every check's VM and defines two checks. The `vet` check has no network access. The `test` check can reach only the Go module proxy and checksum database, so it can download its dependencies. Refer to the [configuration reference](/chainguard/checks/configuration/) for every option.

## Isolation by default

Every check starts from the same minimal base and gets only what you declare:

| Resource | What a check gets |
| -------- | ----------------- |
| Packages | BusyBox, GNU tar, and the packages your configuration file lists. A check has no `git`, package manager, or language toolchain unless you list it. |
| Network | No network access unless the check lists hosts under `network.egress`. Chainguard Checks always blocks cloud metadata endpoints, loopback addresses, and private IP ranges. |
| Credentials | No long-lived credentials. Your repository's code is already in the VM, so most checks need none. |

By default, Chainguard Checks refuses a connection to a host the check doesn't list, and the check keeps running. With `policy: destroy`, Chainguard Checks stops the check's VM instead, and the check fails.

## Use with Chainguard Workspaces

[Chainguard Workspaces](/chainguard/workspaces/overview/) reads the same `.chainguard/ci.yaml` file. In a Workspaces session, the `run-ci` command runs your checks against the session's working tree, uncommitted changes included, so you or a coding agent can find failures before pushing.

The `run-ci` command runs each check in the session's own environment, which can have different packages and network access than the check declares. Its result predicts the pull request's result, but only Chainguard Checks, which runs each check in a fresh VM, decides what GitHub shows. You can use Chainguard Checks without Chainguard Workspaces, and the other way around. Refer to [Run checks before you push](/chainguard/checks/run-checks/).

## Availability and limits

Chainguard Checks is offered as a Technology Preview, as described in the [Chainguard Master Service and License Agreement](https://www.chainguard.dev/legal/master-service-and-license-agreement). Technology Previews aren't recommended for production use. Don't use a Technology Preview to process personal data, or any data subject to legal or regulatory compliance requirements, unless Chainguard specifically authorizes it.

During the beta, Chainguard Checks has the following limits:

- It works with repositories on github.com only.
- A run can take up to 50 minutes from when it starts. Checks still running or waiting to start at that point fail.
- A free trial lasts 30 days and includes 500 vCPU-hours of Checks. Each organization can start one trial. During the trial, the following limits also apply:
    - Your organization can have 10 runs queued or running at a time, including runs after merging.
    - Each run can use up to 4 VMs and 16 vCPUs at once, so up to four of its checks run at the same time.
    - Each check's VM can have up to 4 vCPUs and 16 GB of memory.

## Next steps

- [Get started with Chainguard Checks](/chainguard/checks/getting-started/) to start a trial and run your first checks on a pull request.
- [Chainguard Checks configuration reference](/chainguard/checks/configuration/) to learn the `.chainguard/ci.yaml` format.
- [Use Chainguard Checks on GitHub](/chainguard/checks/github/) to require checks before merging.
