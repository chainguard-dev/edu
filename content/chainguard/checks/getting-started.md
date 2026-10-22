---
title: "Get started with Chainguard Checks"
linktitle: "Getting started"
description: "Sign up for Chainguard Checks, add checks to one of your GitHub repositories, and see them run on a pull request."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-22T12:41:37+00:00
draft: false
tags: ["Chainguard Checks", "Getting Started", "GitHub", "Procedural"]
images: []
menu:
  docs:
    parent: "checks"
    identifier: "Checks Getting Started"
toc: true
weight: 20
---

This guide shows you how to run Chainguard Checks on pull requests in one of your GitHub repositories. If the repository already runs GitHub Actions workflows on pull requests, use the [quick start](#quick-start) to draft checks from those workflows. To learn how each part of the setup works, follow the [step-by-step guide](#step-by-step-guide), which uses a Go repository and a configuration file you write yourself, and takes about 15 minutes.

{{< beta feature="Chainguard Checks" access="organizations that turn it on with `chainctl develop init`, which comes with a free monthly compute allowance, or that arrange access with their Chainguard account team" >}}

{{% quickstart %}}

## Quick start {#quick-start}

You need `chainctl` 0.2.386 or later and a local clone of a GitHub repository that runs GitHub Actions workflows on pull requests. To install or update `chainctl`, refer to [Install or update chainctl](/get-started/checks-and-workspaces/set-up/#install-or-update-chainctl).

1. **Sign up**

    ```shell
    chainctl develop init
    ```

    The command creates your Chainguard organization, if you don't have one, and turns on Chainguard Checks. When it asks which GitHub account to link, choose the one that owns your repository: press `Enter` for your own user, or enter the organization's name.

1. **Install the Chainguard App**

    If the app isn't on that account yet, `chainctl develop init` offers to open its installation page, and finishes linking the account after you install it. You can also [install the app](https://github.com/apps/chainguard/installations/new) before you sign up.

1. **Draft checks from your workflows**

    In the root of your local clone, run the following commands. The second one needs [jq](https://jqlang.org/download/).

    ```shell
    mkdir -p .chainguard/ci
    chainctl checks migrate --dry -o json | jq -r .document > .chainguard/ci/migrated.yaml
    ```

    The draft gives checks no network access. Add the hosts and packages each check needs, as described in [Migrate from GitHub Actions](/chainguard/checks/migrate-from-github-actions/#draft-a-configuration-with-chainctl), then open a pull request with the file.

Chainguard Checks runs your checks on the pull request. To read the results and require checks before merging, go to [Step 4: Review the results](#step-4-review-the-results).
{.quick-start-done}
{{% /quickstart %}}

## Step-by-step guide {#step-by-step-guide}

The following steps set up Chainguard Checks with a `.chainguard/ci.yaml` file you write yourself, instead of a draft from your workflows. Follow them if your repository doesn't run GitHub Actions workflows, or to see how a configuration file works before you add one. A repository can't have both `.chainguard/ci.yaml` and `.chainguard/ci/migrated.yaml`, so if you followed the quick start, skip to Step 4.

### Step 1: Sign up {#step-1-sign-up}

<span id="step-1-install-or-update-chainctl"></span><span id="step-2-install-the-chainguard-app"></span><span id="step-3-sign-up-and-turn-on-chainguard-checks"></span>

Sign up as described in [Set up Chainguard Checks and Chainguard Workspaces](/get-started/checks-and-workspaces/set-up/). You install or update `chainctl`, install the Chainguard App on the account that owns your repository, and run `chainctl develop init`, which turns on Chainguard Checks and Chainguard Workspaces together. You also need a local clone of a repository on github.com that you can push to.

### Step 2: Add a configuration file to your repository

In your local clone, create a branch for the change. Replace `$REPO_DIR` with the path to your local clone:

```shell
cd $REPO_DIR
git checkout -b add-chainguard-checks
```

Next, create a `.chainguard/ci.yaml` configuration file that defines two checks:

```shell
mkdir -p .chainguard
cat > .chainguard/ci.yaml <<EOF
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
EOF
```

This file tells Chainguard Checks to install the `go` package in each check's VM, then run `go vet` in one check and `go test` in another. Each check runs in a fresh VM with no network access unless it asks for some, so both checks list the Go module proxy and checksum database under `network.egress` to download the modules your code depends on. If your repository isn't a Go repository, replace the package and the commands with your own. Refer to the [configuration reference](/chainguard/checks/configuration/) for every option.

To find mistakes in the file before you push it, run `chainctl checks validate` with the repository's directory:

```shell
chainctl checks validate .
```

The command reads the file the same way Chainguard Checks does, without running anything. For this file, it prints `workflow ci (.chainguard/ci.yaml)` followed by `ok: the document lowers`. For a file with problems, it prints each problem with its line number.

### Step 3: Open a pull request

Commit the file, push the branch, and open a pull request. This example uses the GitHub CLI to open the pull request, but you can also open it on github.com:

```shell
git add .chainguard/ci.yaml
git commit -m "Add Chainguard Checks"
git push -u origin add-chainguard-checks
gh pr create --fill
```

Chainguard Checks reads the configuration file from the pull request itself, so the pull request that adds `.chainguard/ci.yaml` runs its checks.

### Step 4: Review the results

Open the pull request on GitHub and scroll to its checks. After a few seconds, you'll see the following:

- **Chainguard Checks (presubmit)**, the summary check for the whole run. It's pending while checks run, then passes only if every blocking check passed.
- **presubmit / ci / vet** or **presubmit / ci / test**, for a check that doesn't pass or that reports errors, warnings, notices, or a summary. A check that passes without reporting anything appears only in the summary check's output.

To read a check's output, select the check. On GitHub, its output shows each step's outcome, exit code, and duration, followed by the end of its log and any errors it reported. The **Details** link opens the check's full log on a run page that Chainguard hosts. To open the run page, you need a role in your Chainguard organization, as described in [The Details link or a chainctl checks command says you don't have access](/chainguard/checks/troubleshooting/#the-details-link-or-a-chainctl-checks-command-says-you-dont-have-access). If you created your organization with `chainctl develop init`, you don't have that role, so read the output on GitHub.

If no checks appear, refer to [Troubleshoot Chainguard Checks](/chainguard/checks/troubleshooting/#a-pull-request-gets-no-checks).

### Step 5: Require checks before merging

To block merging until checks pass, add **Chainguard Checks (presubmit)** as a required status check in your branch protection rule or ruleset for the default branch.

Require only the summary check, not the per-check results. A check that passes without reporting anything, or that a condition skips, never reports a result of its own, so GitHub would wait for it indefinitely. The summary check accounts for skipped checks.

## Give teammates access {#give-teammates-access}

<span id="add-a-teammate"></span><span id="add-a-teammate-to-a-starter-organization"></span>

Your teammates don't need a Chainguard account to get checks on their pull requests or to read the results on GitHub. A teammate needs a role in your Chainguard organization only to open the run page, to use `chainctl checks` commands such as `status` and `rerun`, or to run checks in a Workspaces session. To give them one, refer to [Give teammates access](/get-started/checks-and-workspaces/set-up/#give-teammates-access).

## Next steps

- [Chainguard Checks configuration reference](/chainguard/checks/configuration/) covers packages, network access, conditions, and more.
- [Use Chainguard Checks on GitHub](/chainguard/checks/github/) explains reruns, checks that run on request, and checks that run after merging.
- [Run checks before you push](/chainguard/checks/run-checks/) shows how to run the same checks in a Chainguard Workspaces session.
- [Workload identities and trust](/chainguard/checks/identity-and-trust/) explains how to give a check short-lived Google Cloud or Chainguard credentials.
- [chainctl checks command reference](/chainguard/checks/chainctl-checks-reference/) lists every `chainctl checks` command and flag.
- Ask questions in the #checks-questions channel in the [Chainguard community Slack](https://join.slack.com/t/chainguardcommunity/shared_invite/zt-3nttdr807-V9BJHayWvsB0KbHsfZO5Rw).
