---
title: "Get started with Chainguard Checks"
linktitle: "Getting started"
description: "Sign up for Chainguard Checks, add checks to one of your GitHub repositories, and see them run on a pull request."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-11-02T16:29:06+00:00
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

Get a first check passing with the [quick start](#quick-start), or learn each part in the [step-by-step guide](#step-by-step-guide).

{{% quickstart %}}

## Quick start {#quick-start}

1. **Install chainctl**

    To install `chainctl` with Homebrew, run the following command:

    ```shell
    brew install chainguard-dev/tap/chainctl
    ```

    Or, to install it with curl on macOS or Linux, run the following commands:

    ```shell
    curl -fL -o chainctl "https://dl.enforce.dev/chainctl/latest/chainctl_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m | sed 's/aarch64/arm64/')"
    sudo install -o $UID -g $(id -g) -m 0755 chainctl /usr/local/bin/
    ```

    If you already have `chainctl`, you need 0.2.386 or later. Update it with `sudo chainctl update`, or with `brew upgrade chainctl` if you installed it with Homebrew.

1. **Sign up**

    In the root of a local clone of a GitHub repository that you can push to, run the following command:

    ```shell
    chainctl develop init
    ```

    The command creates your Chainguard organization, if you don't have one, and turns on Chainguard Checks. When it asks which GitHub account to link, choose the one that owns your repository: press `Enter` for your own user, or enter the organization's name. If the Chainguard App isn't installed on that account, the command offers to open its installation page. Give the App access to your repository. If you installed it earlier and GitHub shows that it's asking for more permissions, accept them. To sign in with an email address and password, first run `chainctl config set default.social-login email`.

1. **Add a first check**

    Create a branch and a `.chainguard/ci.yaml` file with one check:

    ```shell
    git checkout -b add-chainguard-checks
    mkdir -p .chainguard
    cat > .chainguard/ci.yaml <<'EOF'
    version: 1
    environment: {}
    checks:
      hello:
        cmd: ls -la
    EOF
    ```

    The check lists the files in its working directory and needs no packages or network access, so it passes on any repository.

1. **Open a pull request**

    Commit the file and push the branch:

    ```shell
    git add .chainguard/ci.yaml
    git commit -m "Add Chainguard Checks"
    git push -u origin add-chainguard-checks
    ```

    Then open a pull request, from the link that `git push` prints or on github.com.

1. **Read the result**

    On the pull request, wait for the **Chainguard Checks (presubmit)** check to pass, which can take a minute, and then select it to read the `hello` check's output. If no check appears, refer to [A pull request gets no checks](/chainguard/checks/troubleshooting/#a-pull-request-gets-no-checks).

To replace the first check with your own, refer to [Replace the first check with your own](#replace-the-first-check-with-your-own). To draft checks from your GitHub Actions workflows, refer to [Draft checks from your workflows](#draft-checks-from-your-workflows).
{.quick-start-done}
{{% /quickstart %}}

{{< beta feature="Chainguard Checks" access="organizations that turn it on with `chainctl develop init`, which comes with a free monthly compute allowance, or that arrange access with their Chainguard account team" >}}

## Draft checks from your workflows {#draft-checks-from-your-workflows}

If your repository runs GitHub Actions workflows on pull requests, `chainctl checks migrate` can draft checks from them. A repository can't have both `.chainguard/ci.yaml` and `.chainguard/ci/migrated.yaml`, so if you added the quick start's first check, delete `.chainguard/ci.yaml` first.

In the root of your local clone, run the following commands. The first creates the directory for the draft, and the second drafts the checks without running anything and saves them as `.chainguard/ci/migrated.yaml`. The second command needs [jq](https://jqlang.org/download/).

```shell
mkdir -p .chainguard/ci
chainctl checks migrate --dry -o json | jq -r .document > .chainguard/ci/migrated.yaml
```

The command drafts checks only from jobs that run on `pull_request`. If none of your workflows does, the draft has no checks and the command reports `Nothing to migrate`, so keep the quick start's first check instead.

The draft gives every check no network access, so most drafted checks fail until you add the hosts and packages that each one needs, as described in [Migrate from GitHub Actions](/chainguard/checks/migrate-from-github-actions/#draft-a-configuration-with-chainctl). Then commit the file on a new branch and open a pull request with it, as in the quick start, and Chainguard Checks runs the drafted checks on that pull request.

## Step-by-step guide {#step-by-step-guide}

The following steps add the same first check as the quick start and explain each part. If you followed the quick start, skip to [Step 4](#step-4-review-the-results).

### Step 1: Sign up {#step-1-sign-up}

<span id="step-1-install-or-update-chainctl"></span><span id="step-2-install-the-chainguard-app"></span><span id="step-3-sign-up-and-turn-on-chainguard-checks"></span>

Sign up as described in [Set up Chainguard Checks and Chainguard Workspaces](/get-started/checks-and-workspaces/set-up/). You install or update `chainctl`, install the Chainguard App on the account that owns your repository, and run `chainctl develop init`, which turns on Chainguard Checks and Chainguard Workspaces together. You also need a local clone of a repository on github.com that you can push to.

### Step 2: Add a configuration file to your repository

In your local clone, create a branch for the change. Replace `$REPO_DIR` with the path to your local clone:

```shell
cd $REPO_DIR
git checkout -b add-chainguard-checks
```

Next, create a `.chainguard/ci.yaml` configuration file that defines one check:

```shell
mkdir -p .chainguard
cat > .chainguard/ci.yaml <<'EOF'
version: 1
environment: {}
checks:
  hello:
    cmd: ls -la
EOF
```

This file defines one environment and one check, named `hello`. Every file that has checks needs an `environment` key, and `environment: {}` is the smallest one: a bare root filesystem with no packages added. Each check runs in a fresh VM with no network access unless it asks for some, and `hello` doesn't need any. It runs `ls -la`, which lists the files in its working directory, so it passes on any repository. A string `cmd` runs without a shell, so it can't use pipes, redirects, or variables. To run a command through a shell, write it as a list, such as `cmd: [sh, -c, "ls -la | head"]`. Refer to the [configuration reference](/chainguard/checks/configuration/) for every option.

To find mistakes in the file before you push it, run `chainctl checks validate` with the repository's directory:

```shell
chainctl checks validate .
```

The command reads the file the same way Chainguard Checks does, without running anything. For this file, it prints `workflow ci (.chainguard/ci.yaml)` followed by `ok: the document lowers`. For a file with problems, it prints each problem with its line number.

### Step 3: Open a pull request

Commit the file and push the branch:

```shell
git add .chainguard/ci.yaml
git commit -m "Add Chainguard Checks"
git push -u origin add-chainguard-checks
```

Then open a pull request, from the link that `git push` prints or on github.com. If you use the GitHub CLI, `gh pr create --fill` also opens one.

Chainguard Checks reads the configuration file from the pull request itself, so the pull request that adds `.chainguard/ci.yaml` runs its checks.

### Step 4: Review the results

Open the pull request on GitHub and scroll to its checks. Within about a minute, you'll see the following:

- **Chainguard Checks (presubmit)**, the summary check for the whole run. It's pending while checks run, then passes only if every blocking check passed.
- **presubmit / ci / hello**, for a check that doesn't pass or that reports errors, warnings, notices, or a summary. A check that passes without reporting anything appears only in the summary check's output.

To read a check's output, select the check. On GitHub, its output shows each step's outcome, exit code, and duration, followed by the end of its log and any errors it reported. The **Details** link opens the check's full log on a run page that Chainguard hosts. To open the run page, you need a role in your Chainguard organization, as described in [The Details link or a chainctl checks command says you don't have access](/chainguard/checks/troubleshooting/#the-details-link-or-a-chainctl-checks-command-says-you-dont-have-access). If you created your organization with `chainctl develop init`, you don't have that role, so read the output on GitHub.

If no checks appear, refer to [Troubleshoot Chainguard Checks](/chainguard/checks/troubleshooting/#a-pull-request-gets-no-checks).

### Step 5: Require checks before merging

To block merging until checks pass, add **Chainguard Checks (presubmit)** as a required status check in your branch protection rule or ruleset for the default branch. GitHub lists the check there only after it has run in the repository within the past week. For where to find these settings on GitHub, refer to GitHub's [Managing a branch protection rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule) or [Creating rulesets for a repository](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository).

Require only the summary check, not the per-check results. A check that passes without reporting anything, or that a condition skips, never reports a result of its own, so GitHub would wait for it indefinitely. The summary check accounts for skipped checks.

## Replace the first check with your own {#replace-the-first-check-with-your-own}

Once the first check passes, replace it with the checks your repository needs. For example, if your repository is a Go module, with a `go.mod` file at its root, the following `.chainguard/ci.yaml` file runs `go vet` and `go test` as two checks:

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

This file tells Chainguard Checks to install the `go` package in each check's VM, then run `go vet` in one check and `go test` in another. Both checks list the Go module proxy and checksum database under `network.egress` to download the modules your code depends on. In a repository that isn't a Go module, both commands fail, so use your own packages and commands instead.

Run `chainctl checks validate .` again, then commit and push the change. Chainguard Checks runs the new checks on the pull request when it's updated.

## Give teammates access {#give-teammates-access}

<span id="add-a-teammate"></span><span id="add-a-teammate-to-a-starter-organization"></span>

Your teammates don't need a Chainguard account to get checks on their pull requests or to read the results on GitHub. A teammate needs a role in your Chainguard organization only to open the run page, to use `chainctl checks` commands such as `status` and `rerun`, or to run checks in a Workspaces session. To give them one, refer to [Give teammates access](/get-started/checks-and-workspaces/set-up/#give-teammates-access).

## Next steps

- [Chainguard Checks configuration reference](/chainguard/checks/configuration/) covers packages, network access, conditions, and more.
- [Use Chainguard Checks on GitHub](/chainguard/checks/github/) explains reruns, checks that run on request, and checks that run after merging.
- [Run checks before you push](/chainguard/checks/run-checks/) shows how to run the same checks in a Chainguard Workspaces session.
- [Workload identities and trust](/chainguard/checks/identity-and-trust/) explains how to give a check short-lived Google Cloud, AWS, Azure, or Chainguard credentials.
- [chainctl checks command reference](/chainguard/checks/chainctl-checks-reference/) lists every `chainctl checks` command and flag.
- Ask questions in the #checks-questions channel in the [Chainguard community Slack](https://join.slack.com/t/chainguardcommunity/shared_invite/zt-3nttdr807-V9BJHayWvsB0KbHsfZO5Rw).
