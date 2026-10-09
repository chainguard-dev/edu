---
title: "Get started with Chainguard Checks"
linktitle: "Getting started"
description: "Start a free trial of Chainguard Checks, add a .chainguard/ci.yaml file to a repository, and see your first checks run on a GitHub pull request."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-09T00:00:00+00:00
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

This guide walks you through starting a free trial of Chainguard Checks, adding checks to one of your GitHub repositories, and seeing them run on a pull request. It uses a Go repository as the example and takes about 15 minutes, plus about an hour while Chainguard finishes setting up a new organization.

{{< beta feature="Chainguard Checks" access="organizations that start a free trial with `chainctl develop init`, or that arrange access with their Chainguard account team" >}}

## Prerequisites

Before you begin, make sure you have the following:

- A GitHub account that can install GitHub Apps on the personal account or organization that owns your repository. To install the app on an organization and link it, you need the owner role on that organization.
- A repository on github.com that you can push to, and a local clone of it.

## Step 1: Install or update chainctl

You start the trial with `chainctl`. If you don't have it yet, follow the [chainctl installation guide](/platform/chainctl-usage/how-to-install-chainctl/).

If you already have `chainctl`, update it to the latest release, because Chainguard Checks changes often during the beta:

```shell
sudo chainctl update
```

If you installed `chainctl` with Homebrew, run `brew upgrade chainctl` instead. Refer to [Updating chainctl](/platform/chainctl-usage/how-to-install-chainctl/#updating-chainctl) for details.

## Step 2: Install the Chainguard App

Chainguard Checks receives pull request events and reports results through the Chainguard App, a GitHub App that also backs [Chainguard Workspaces](/chainguard/workspaces/overview/) and [Guardener](/chainguard/guardener/).

1. Go to the [Chainguard App installation page](https://github.com/apps/chainguard/installations/new).
2. Choose the personal account or organization that owns your repository.
3. Choose **All repositories**, or select the repositories you want to use with Chainguard Checks.
4. Review the requested permissions and select **Install**.

Installing the app doesn't change your repositories. Chainguard Checks runs only on repositories that have a `.chainguard/ci.yaml` file, after you link the account in the next step.

## Step 3: Start a free trial

The `chainctl develop init` command signs you up and starts a free 30-day trial of both Chainguard Checks and Chainguard Workspaces. Run it in an interactive terminal, because it opens your browser and asks questions as it goes:

```shell
chainctl develop init
```

The command does the following:

1. Signs you in through your browser, and registers a new Chainguard identity if you don't have one.
2. Creates a Chainguard organization for you if you don't belong to one. If you belong to several, it asks which one to use.
3. Asks you to accept the terms that Chainguard Checks and Chainguard Workspaces are offered under.
4. Asks for the GitHub organization or user to link, and opens your browser so you can authorize the link. Enter the account name only, such as `acme`, not a URL. This must be the account where you installed the Chainguard App.
5. Starts the trial and prints what it includes.

You can answer some of the questions ahead of time with flags. If you don't belong to a Chainguard organization yet, name the new one with `--name`. If you already belong to one or more, choose one with `--parent` instead. To name the GitHub account to link, pass `--github-org`. In this example, `acme-trial` is the new Chainguard organization and `acme` is the GitHub organization:

```shell
chainctl develop init --name acme-trial --github-org acme
```

Each organization can start one trial. After the trial starts, Chainguard finishes setting up a new organization within about an hour. Pull requests opened or updated before then get no checks, so wait before you open your first pull request in the next steps.

If your organization already has Chainguard Checks through your Chainguard account team, skip `chainctl develop init`. Instead, have an organization owner accept the terms once for the organization:

```shell
chainctl checks accept-terms --parent $ORGANIZATION
```

Replace `$ORGANIZATION` with the name of your Chainguard organization. If your GitHub account isn't linked to the organization yet, link it as described in [Getting started with Guardener](/chainguard/guardener/github/getting-started/#step-2-link-your-chainguard-organization-to-github), which uses the same Chainguard App.

## Step 4: Add a configuration file to your repository

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
  test:
    cmd: go test ./...
    network:
      egress: [proxy.golang.org, sum.golang.org]
EOF
```

This file tells Chainguard Checks to install the `go` package in each check's VM, then run `go vet` in one check and `go test` in another. The `test` check lists the Go module proxy and checksum database under `network.egress`, so it can download modules. The `vet` check has no network access. If your repository isn't a Go repository, replace the package and the commands with your own. Refer to the [configuration reference](/chainguard/checks/configuration/) for every option.

To find mistakes in the file before you push it, run `chainctl checks validate` with the repository's directory:

```shell
chainctl checks validate .
```

The command reads the file the same way Chainguard Checks does, without running anything. For this file, it prints `ok: the document lowers`. For a file with problems, it prints each problem with its line number.

## Step 5: Open a pull request

Commit the file, push the branch, and open a pull request. This example uses the GitHub CLI to open the pull request, but you can also open it on github.com:

```shell
git add .chainguard/ci.yaml
git commit -m "Add Chainguard Checks"
git push -u origin add-chainguard-checks
gh pr create --fill
```

Chainguard Checks reads the configuration file from the pull request itself, so the pull request that adds `.chainguard/ci.yaml` runs its checks.

## Step 6: Review the results

Open the pull request on GitHub and scroll to its checks. After a few seconds, you'll see the following:

- **Chainguard Checks (presubmit)**, the summary check for the whole run. It's pending while checks run, then passes only if every blocking check passed.
- **presubmit / ci / vet** and **presubmit / ci / test**, one GitHub check for each check in your file. Each appears when that check finishes.

To read a check's output, select the check. On GitHub, its output shows each step's outcome, exit code, and duration, followed by the end of its log and any errors it reported. The **Details** link opens the run's full log on a run page that Chainguard hosts, separate from the Chainguard Console.

If no checks appear, refer to [Troubleshoot Chainguard Checks](/chainguard/checks/troubleshooting/#a-pull-request-gets-no-checks).

## Step 7: Require checks before merging

To block merging until checks pass, add **Chainguard Checks (presubmit)** as a required status check in your branch protection rule or ruleset for the default branch.

Require only the summary check, not the per-check results. A check that a condition skips never reports a result, so GitHub would wait for it indefinitely. The summary check accounts for skipped checks.

## Next steps

- [Chainguard Checks configuration reference](/chainguard/checks/configuration/) covers packages, network access, conditions, and more.
- [Use Chainguard Checks on GitHub](/chainguard/checks/github/) explains reruns, checks that run on request, and checks that run after merging.
- [Run checks before you push](/chainguard/checks/run-checks/) shows how to run the same checks in a Chainguard Workspaces session.
- Ask questions in the #checks-questions channel in the [Chainguard community Slack](https://join.slack.com/t/chainguardcommunity/shared_invite/zt-3nttdr807-V9BJHayWvsB0KbHsfZO5Rw).
