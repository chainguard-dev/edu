---
title: "Inspect and run checks with chainctl"
linktitle: "Inspect and run checks"
description: "Read a pull request's Chainguard Checks results and logs from your terminal, run checks on a pushed commit without a pull request, and find the checks that take the most time or fail most often."
type: "article"
date: 2026-10-12T00:00:00+00:00
lastmod: 2026-10-13T18:50:45+00:00
draft: false
tags: ["Chainguard Checks", "chainctl", "Procedural"]
images: []
menu:
  docs:
    parent: "checks"
toc: true
weight: 55
---

The `chainctl checks` commands read your checks' results from your terminal, so you or a coding agent can find out why a check failed without opening GitHub. This page explains how to inspect a pull request's runs, how to run checks on a pushed commit without opening a pull request, and how to find the checks that take the most time or fail most often. For every command and flag, refer to the [`chainctl checks` command reference](/chainguard/checks/chainctl-checks-reference/).

These commands need a role in your Chainguard organization, as described in [The Details link or a chainctl checks command says you don't have access](/chainguard/checks/troubleshooting/#the-details-link-or-a-chainctl-checks-command-says-you-dont-have-access). To pass your organization's name to `--parent`, rather than its ID, you also need a role that can see the organization, such as `viewer`.

## Inspect pull request runs {#inspect-pull-request-runs}

To check a pull request's latest run, pass the pull request to `chainctl checks status`. Replace `$OWNER/$REPO#$NUMBER` with the pull request, such as `acme/app#123`, or with its URL, and capitalize the owner and repository the same way GitHub does. Replace `$ORGANIZATION` with the name of your Chainguard organization:

```shell
chainctl checks status "$OWNER/$REPO#$NUMBER" --parent $ORGANIZATION
```

The command shows the pull request's newest run and each check's result. It exits with `0` while the run is in progress, so to wait until the run finishes, add `--watch`. After you push a commit or start a rerun, the command shows the previous run until Chainguard Checks creates the new one. For its exit codes and JSON output, refer to [chainctl checks status](/chainguard/checks/chainctl-checks-reference/#chainctl-checks-status).

To see why a pull request's checks failed, run `chainctl checks failures`:

```shell
chainctl checks failures "$OWNER/$REPO#$NUMBER" --parent $ORGANIZATION
```

For each failed check, the command shows the step that failed, with its exit code and command, and the end of the failing output, quoted from the check's log. To show one check, add `--check` with its name. To also list the checks that didn't run, and why, add `--not-run`. The output stays within a size limit that `--budget` sets in bytes: the command shows as many failed checks in full as fit, then one line for each of the rest.

To print a check's log, pass the pull request and the check's name to `chainctl checks logs`:

```shell
chainctl checks logs "$OWNER/$REPO#$NUMBER" --check test --parent $ORGANIZATION
```

To keep reading a running check's output until it finishes, add `--follow`. To show only a long log's error lines, with three lines around each, add `--errors -C 3`. For other ways to read part of a log, refer to [chainctl checks logs](/chainguard/checks/chainctl-checks-reference/#chainctl-checks-logs).

To see the programs that each step of a failed check started, and which one most likely failed, run `chainctl checks trace` with `--failed`:

```shell
chainctl checks trace "$OWNER/$REPO#$NUMBER" --check test --failed --parent $ORGANIZATION
```

These commands also work in a Workspaces session, where `chainctl` acts as you. During the beta, they can't find a run by its commit, so pass the pull request, as described in [Name a run](/chainguard/checks/chainctl-checks-reference/#name-a-run).

For a run after merging, pass the run's ID instead, such as `chainctl checks status $RUN_ID --parent $ORGANIZATION`. The ID is the part after `/runs/` in the **Details** link of the **Chainguard Checks (postsubmit)** summary check.

## Run checks on a pushed commit

To run your checks in fresh VMs without opening a pull request, push your commit and run `chainctl checks run` in your checkout. Unlike `run-ci` in a [Workspaces session](/chainguard/checks/run-checks/), it runs only what you pushed, not uncommitted changes. Replace `$ORGANIZATION` with the name of your Chainguard organization:

```shell
chainctl checks run . --watch --parent $ORGANIZATION
```

The command runs the commit checked out in the current directory. Chainguard Checks reads the commit from GitHub, in the repository of the checkout's `origin` remote, so push the commit first. In a checkout of a fork, add `--git-remote upstream` to read it from the repository you forked instead. The repository's GitHub account must be linked to your Chainguard organization, as described in [Getting started](/get-started/checks-and-workspaces/#sign-up-with-chainctl-develop-init).

The command prints the run's name, followed by its checks. With `--watch`, it waits until the run finishes, and exits with `1` if a blocking check doesn't pass. To run only one check and the checks it `needs`, add `--check` with its name. To include a check that runs only on request, name it with `--check`, or add `--request` with its name, as a `ci/run:` label does on a pull request. For every flag, refer to the [`chainctl checks run` reference](/chainguard/checks/chainctl-checks-reference/#chainctl-checks-run).

A run you start this way differs from a pull request run in the following ways:

- It's for your information only. It doesn't appear on GitHub and never counts as a pull request's or commit's result, but it uses your organization's Checks allowance like any other run.
- It runs only checks that run on pull requests, so it skips checks whose `trigger` is only `postsubmit`.
- Its `when.changed` conditions compare the commit with where it branched from the remote's default branch, or with its parent if the commit is on that branch. To compare it with another commit, add `--base` with that commit.
- It has no pull request, trigger, or labels. If a check's `when` expression reads any `context` field, the command names the check and doesn't start a run. To run other checks, select one with `--check`.
- A check with a workload `identity` fails, because only pull request runs and runs after merging get identities.

In a Starter organization, don't use `chainctl checks run`. Your role can start runs, which use your allowance, but can't read their results, so open a pull request instead.

### Read a run you started

To read a run you started, pass its ID, or the start of it, to `chainctl checks status` or the other commands that read runs. The ID is the part after `/runs/` in the run's name. Replace `$RUN_ID` with the ID:

```shell
chainctl checks status $RUN_ID --watch --parent $ORGANIZATION
```

Don't pass `.` or the commit's SHA instead. Because the run never counts as the commit's result, `status` reports that the platform created no run for the commit.

To find the ID of a run you started earlier, run `chainctl checks list --parent $ORGANIZATION`. To stop a run before it finishes, pass its ID to `chainctl checks cancel`.

## See check history {#see-check-history}

To find the checks that take the most time or fail most often, use `chainctl checks top`, `chainctl checks trends`, and `chainctl checks stats`.

To rank a repository's checks by their total runtime over the past week, run `chainctl checks top`. Replace `$OWNER/$REPO` with the repository, such as `acme/app`, and `$ORGANIZATION` with the name of your Chainguard organization:

```shell
chainctl checks top --repo $OWNER/$REPO --since 7d --parent $ORGANIZATION
```

To rank the checks by failure rate instead, add `--by failures`. For the other rankings, the time windows you can read, and how the command counts failures, refer to [chainctl checks top](/chainguard/checks/chainctl-checks-reference/#chainctl-checks-top).

To see how long a check takes, hour by hour, pass its name to `chainctl checks trends`:

```shell
chainctl checks trends --repo $OWNER/$REPO --check test --parent $ORGANIZATION
```

For each hour, the command shows the check's median, 95th percentile, and 99th percentile durations. Only the 10 checks with the most total runtime in the window have trends. For more, refer to [chainctl checks trends](/chainguard/checks/chainctl-checks-reference/#chainctl-checks-trends).

To count the outcomes of your organization's recent runs, run `chainctl checks stats`:

```shell
chainctl checks stats --parent $ORGANIZATION
```

The command prints a table of each repository's runs by outcome, and a table of each check's results by outcome, with the check's failure percentage and median duration. For what each column counts, refer to [chainctl checks stats](/chainguard/checks/chainctl-checks-reference/#chainctl-checks-stats).
