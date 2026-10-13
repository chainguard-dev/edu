---
title: "Chainguard Checks overview"
linktitle: "Overview"
description: "Learn how Chainguard Checks runs your repository's CI checks in isolated microVMs on every GitHub pull request, with no network access unless a check asks for it."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-13T00:00:00+00:00
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

{{< beta feature="Chainguard Checks" access="organizations that turn it on with `chainctl develop init`, which comes with a free monthly compute allowance, or that arrange access with their Chainguard account team" >}}

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
    network:
      egress: [proxy.golang.org, sum.golang.org]
  test:
    cmd: go test ./...
    network:
      egress: [proxy.golang.org, sum.golang.org]
```

This file installs Go in every check's VM and defines two checks, `vet` and `test`. Each check runs in a fresh VM with no network access unless it asks for some, so both list the Go module proxy and checksum database under `network.egress` to download the modules your code depends on. Refer to the [configuration reference](/chainguard/checks/configuration/) for every option.

## Isolation by default

Every check starts from the same minimal base and gets only what you declare:

| Resource | What a check gets |
| -------- | ----------------- |
| Packages | BusyBox, GNU tar, and the packages your configuration file lists. A check has no `git`, package manager, or language toolchain unless you list it. |
| Network | No network access unless the check lists hosts under `network.egress`. Chainguard Checks always blocks cloud metadata endpoints, loopback addresses, and private IP ranges. |
| Credentials | No long-lived credentials. Your repository's code is already in the VM, so most checks need none. A check that must authenticate to Google Cloud or to Chainguard can request a [workload identity](/chainguard/checks/identity-and-trust/) for short-lived access. |
| Caches | None unless the check declares one. During the beta, a Go check can reuse build output from earlier runs through cache pools that your default branch defines. Refer to [Caches](/chainguard/checks/variations-services-caches/#caches). |

By default, Chainguard Checks refuses a connection to a host the check doesn't list, and the check keeps running. With `policy: destroy`, Chainguard Checks stops the check's VM instead, and the check fails.

## Use with Chainguard Workspaces

[Chainguard Workspaces](/chainguard/workspaces/overview/) reads the same `.chainguard/ci.yaml` file. In a Workspaces session, the `run-ci` command runs your checks against the session's working tree, uncommitted changes included, so you or a coding agent can find failures before pushing.

The `run-ci` command runs each check in the session's own environment, which can have different packages and network access than the check declares. Its result predicts the pull request's result, but only Chainguard Checks, which runs each check in a fresh VM, decides what GitHub shows. You can use Chainguard Checks without Chainguard Workspaces, and the other way around. Refer to [Run checks before you push](/chainguard/checks/run-checks/).

## Availability and limits

Chainguard Checks is offered as a Technology Preview, as described in the [Chainguard Master Service and License Agreement](https://www.chainguard.dev/legal/master-service-and-license-agreement). Technology Previews aren't recommended for production use. Don't use a Technology Preview to process personal data, or any data subject to legal or regulatory compliance requirements, unless Chainguard specifically authorizes it. If you turn on the [requested checks agent](/chainguard/checks/github/#what-the-agent-reads), Chainguard Checks sends pull request content to a model, so don't turn it on for a repository whose pull requests contain such data.

During the beta, Chainguard Checks has the following limits:

- It works with repositories on github.com only.
- It doesn't run on GitHub merge queues, so don't require **Chainguard Checks (presubmit)** on a branch that uses one. Refer to [Require checks before merging](/chainguard/checks/github/#require-checks-before-merging).
- It doesn't run checks on a pull request, or on a commit to your default branch, that changes 3,000 or more files. The summary check fails with **Run creation failed** instead, so split a change that large into smaller pull requests. Refer to [Troubleshoot Chainguard Checks](/chainguard/checks/troubleshooting/#the-summary-check-says-the-run-couldnt-be-created-or-failed).
- A run can take up to 50 minutes from when it starts. Checks still running or waiting to start at that point fail.

`chainctl develop init` turns on the *Starter allowance*: 500 vCPU-hours of Checks each month, separate from the Workspaces allowance. The allowance resets on the first day of each month (UTC) and comes with the following limits:

- Your organization can have 10 runs queued or running at a time, including runs after merging.
- Each run can use up to 4 VMs and 16 vCPUs at once, so up to four of its checks run at the same time.
- Each check's VM can have up to 4 vCPUs and 16 GB of memory.

Chainguard counts each check's vCPUs for as long as its VM runs. A check with the [default resources](/chainguard/checks/configuration/#resources) uses 2 vCPU-hours for each hour it runs, and a `medium` check uses 4. Chainguard doesn't show your usage during the beta. When the allowance is used up, Chainguard Checks doesn't start new runs until it resets, and runs already in progress finish. Refer to [Troubleshoot Chainguard Checks](/chainguard/checks/troubleshooting/#the-summary-check-says-the-run-couldnt-be-created-or-failed) for what a pull request shows then.

If your organization arranged access with its Chainguard account team, its allowance and limits can differ.

## Get help

To ask questions or get support, use the #checks-questions channel in the [Chainguard community Slack](https://join.slack.com/t/chainguardcommunity/shared_invite/zt-3nttdr807-V9BJHayWvsB0KbHsfZO5Rw). If you aren't a member yet, the link invites you to join.

## Next steps

- [Get started with Chainguard Checks](/chainguard/checks/getting-started/) to sign up and run your first checks on a pull request.
- [Chainguard Checks configuration reference](/chainguard/checks/configuration/) to learn the `.chainguard/ci.yaml` format.
- [Use Chainguard Checks on GitHub](/chainguard/checks/github/) to require checks before merging.
- [Workload identities and trust](/chainguard/checks/identity-and-trust/) to give a check short-lived Google Cloud or Chainguard credentials.
- [chainctl checks command reference](/chainguard/checks/chainctl-checks-reference/) for every `chainctl checks` command and flag.
