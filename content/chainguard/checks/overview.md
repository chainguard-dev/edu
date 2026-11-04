---
title: "Chainguard Checks overview"
linktitle: "Overview"
description: "Learn how Chainguard Checks runs your repository's CI checks in isolated microVMs on every GitHub pull request, with no network access unless a check asks for it."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-11-04T17:00:59+00:00
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

Chainguard Checks runs your pull requests' checks, such as linting and tests, on Chainguard's infrastructure, and reports the results on the pull request's **Checks** tab on GitHub, beside any other checks the repository runs. You define the checks in a `.chainguard/ci.yaml` file in your repository, in Chainguard Checks' own format. Chainguard Checks doesn't run GitHub Actions workflows, so moving a workflow's jobs to it means writing that file, as described in [Migrate from GitHub Actions](/chainguard/checks/migrate-from-github-actions/).

A *check* is one command or script that you name in that file. On every pull request, Chainguard Checks runs each check in its own *microVM*: a small virtual machine, built on Chainguard OS, that starts fresh for that check.

Testing a pull request means running code that no one has reviewed yet, and that code might be malicious. So a check's VM holds no long-lived credentials, and it can't reach the network unless the check lists the hosts it needs.

{{< beta feature="Chainguard Checks" access="organizations that turn it on with `chainctl develop init`, which comes with a free monthly compute allowance, or that arrange access with their Chainguard account team" >}}

## How Checks works

You choose which repositories use Chainguard Checks: a repository uses it once it has a `.chainguard/ci.yaml` file or a `.chainguard/ci/` directory. Chainguard Checks reaches your repositories through the Chainguard App, a GitHub App that you install on your GitHub organization or personal account and link to your Chainguard organization, as described in [Set up Chainguard Checks and Chainguard Workspaces](/get-started/checks-and-workspaces/set-up/).

When someone opens or updates a pull request, the following happens:

1. Chainguard Checks merges the pull request into the latest commit on its base branch, in its own copy of the repository. This test merge exists only in the run and is never pushed to GitHub, so your branches don't change. That way, each run tests the change together with the latest base branch.
2. It reads the configuration from the test merge, so a pull request can add checks or change them.
3. It runs each check in its own microVM, with the packages that your configuration file declares.
4. It reports the results in the pull request's list of checks, as described in [How results appear](/chainguard/checks/github/#how-results-appear).

GitHub calls each result in that list a check too. Chainguard Checks reports one summary check, named **Chainguard Checks (presubmit)**, that covers all of your checks, plus one GitHub check, such as **presubmit / ci / test**, for each of your checks that doesn't pass or that reports something. A check that passes and reports nothing appears only in the summary check.

Each new push to the pull request cancels the run for the previous push and starts a new one. A check that you set to run after a change merges runs on each new commit on your default branch. Those runs report on the commit, as **Chainguard Checks (postsubmit)**, instead of on a pull request. Refer to [Use Chainguard Checks on GitHub](/chainguard/checks/github/) for details.

{{< note >}}Attestations for Checks runs are planned. With them, Chainguard Checks will verify an earlier passing run instead of running your checks again. Until then, Chainguard Checks runs your checks on every push to a pull request.{{< /note >}}

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

This file defines two checks, `vet` and `test`, and installs Go in each check's VM. Each check runs in a fresh VM with no network access unless it asks for some, so both list the Go module proxy and checksum database under `network.egress` to download the modules your code depends on. Refer to the [configuration reference](/chainguard/checks/configuration/) for every option.

On a pull request where both checks pass, the **Checks** tab shows one entry from Chainguard Checks, **Chainguard Checks (presubmit)**, titled **All 2 check(s) passed**. If `test` fails, it shows two: the summary check, titled **1 of 2 check(s) failed**, and **presubmit / ci / test**, whose title gives the exit code and whose output shows the end of the check's log.

## Isolation by default

Every check starts from the same minimal base and gets only what you declare:

| Resource | What a check gets |
| -------- | ----------------- |
| Packages | BusyBox, GNU tar, and the packages your configuration file lists. A check has no `git`, package manager, or language toolchain unless you list it. |
| Network | No network access unless the check lists hosts under `network.egress`. Chainguard Checks always blocks cloud metadata endpoints, loopback addresses, and private IP ranges. |
| Credentials | No long-lived credentials. Your repository's code is already in the VM, so most checks need none. A check that must authenticate to Google Cloud, AWS, Azure, or Chainguard can request a [workload identity](/chainguard/checks/identity-and-trust/) for short-lived access. |
| Caches | None unless the check declares one. During the beta, a check can reuse Go build output, downloaded Go modules, and the packages that Python, Maven, and Gradle download in earlier runs, through cache pools that your default branch defines. Refer to [Caches](/chainguard/checks/variations-services-caches/#caches). |

By default, Chainguard Checks refuses a connection to a host the check doesn't list, and the check keeps running. With `policy: destroy`, Chainguard Checks stops the check's VM instead, and the check fails.

Chainguard Checks intercepts most HTTPS connections from a check, so that it can verify each host's certificate itself and add a [workload identity's](/chainguard/checks/identity-and-trust/) credentials outside the VM. It presents the check with certificates from a certificate authority that it creates for that check's VM alone. It records which hosts and addresses a check connects to, which the check's run page shows, but not what the check sends or receives. A tool that keeps its own list of trusted certificates can reject the intercepted connections. Refer to [Network access](/chainguard/checks/configuration/#network-access) and [A check fails with a certificate error](/chainguard/checks/troubleshooting/#a-check-fails-with-a-certificate-error).

For the security model of Chainguard Checks and Chainguard Workspaces side by side, including trust rings and the run lifecycle, refer to [How Chainguard Checks and Chainguard Workspaces isolate your code](/get-started/checks-and-workspaces/how-it-works/).

## Use with Chainguard Workspaces

[Chainguard Workspaces](/chainguard/workspaces/overview/) reads the same `.chainguard/ci.yaml` file. In a Workspaces session, the `run-ci` command runs your checks against the session's working tree, uncommitted changes included, so you or a coding agent can find failures before pushing.

The `run-ci` command runs each check in the session's own environment, which can have different packages and network access than the check declares. Its result predicts the pull request's result, but only Chainguard Checks, which runs each check in a fresh VM, decides what GitHub shows. You can use Chainguard Checks without Chainguard Workspaces, and the other way around. Refer to [Run checks before you push](/chainguard/checks/run-checks/).

## Availability and limits {#availability-and-limits}

{{% blurb/technology-preview product="Chainguard Checks" %}}

If you turn on the [requested checks agent](/chainguard/checks/github/#what-the-agent-reads), Chainguard Checks sends pull request content to a model, so don't turn it on for a repository whose pull requests contain such data.

During the beta, Chainguard Checks has the following limits:

- It works with repositories on github.com only.
- It doesn't run on GitHub merge queues, so don't require **Chainguard Checks (presubmit)** on a branch that uses one. Refer to [Require checks before merging](/chainguard/checks/github/#require-checks-before-merging).
- It doesn't run checks on a pull request, or on a commit to your default branch, that changes 3,000 or more files. The summary check fails with **Run creation failed** instead, so split a change that large into smaller pull requests. Refer to [Troubleshoot Chainguard Checks](/chainguard/checks/troubleshooting/#the-summary-check-says-the-run-couldnt-be-created-or-failed).
- A run can take up to two hours from when it starts. Checks still running or waiting to start at that point fail.

`chainctl develop init` turns on the *Starter allowance*: 500 vCPU-hours of Checks each month, separate from the Workspaces allowance. The allowance resets on the first day of each month (UTC) and comes with the following limits:

- Your organization can have 10 runs queued or running at a time, including runs after merging.
- Each run can use up to 4 VMs and 16 vCPUs at once, so up to four of its checks run at the same time.
- Each check's VM can have up to 4 vCPUs and 16 GB of memory.

Chainguard counts each check's vCPUs for as long as its VM runs. A check with the [default resources](/chainguard/checks/configuration/#resources) uses 2 vCPU-hours for each hour it runs, and a `medium` check uses 4. Chainguard doesn't show your usage during the beta. When the allowance is used up, Chainguard Checks doesn't start new runs until it resets, and runs already in progress finish. Refer to [Troubleshoot Chainguard Checks](/chainguard/checks/troubleshooting/#the-summary-check-says-the-run-couldnt-be-created-or-failed) for what a pull request shows then.

If your organization arranged access with its Chainguard account team, its allowance and limits can differ.

## Get help

{{% blurb/checks-workspaces-help channel="checks-questions" %}}

## Next steps

- [Get started with Chainguard Checks](/chainguard/checks/getting-started/) to sign up and run your first checks on a pull request.
- [Chainguard Checks configuration reference](/chainguard/checks/configuration/) to learn the `.chainguard/ci.yaml` format.
- [Use Chainguard Checks on GitHub](/chainguard/checks/github/) to require checks before merging.
- [Workload identities and trust](/chainguard/checks/identity-and-trust/) to give a check short-lived Google Cloud, AWS, Azure, or Chainguard credentials.
- [chainctl checks command reference](/chainguard/checks/chainctl-checks-reference/) for every `chainctl checks` command and flag.
