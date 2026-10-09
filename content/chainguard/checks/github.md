---
title: "Use Chainguard Checks on GitHub"
linktitle: "Checks on GitHub"
description: "Learn when Chainguard Checks runs on GitHub, and how to require checks before merging, rerun them, and run a check on request."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-09T00:00:00+00:00
draft: false
tags: ["Chainguard Checks", "GitHub", "Configuration"]
images: []
menu:
  docs:
    parent: "checks"
toc: true
weight: 40
---

Chainguard Checks runs on your GitHub repositories through the Chainguard App and reports its results as GitHub checks. This page explains when Chainguard Checks runs, how its results appear on GitHub, and how to use them to protect your branches.

## When Checks runs

Chainguard Checks runs on a repository when the Chainguard App is installed on the repository, its GitHub account is linked to a Chainguard organization with access to Chainguard Checks, and the repository has a `.chainguard/ci.yaml` file or a `.chainguard/ci/` directory. For a pull request, Chainguard Checks looks for the configuration on the pull request's branch and on its base branch.

| Event | What Chainguard Checks runs |
| ----- | --------------------------- |
| A pull request is opened, reopened, or updated | The repository's presubmit checks, which are checks without a `trigger` key or with `trigger: presubmit`. |
| A new commit arrives on the default branch | The repository's postsubmit checks, which are checks with `trigger: postsubmit`. |

Pushes to other branches, tags, and closed pull requests don't start runs.

For a pull request, Chainguard Checks runs against the commit GitHub would create by merging the pull request into its base branch, and reads the configuration from that commit. The result reflects the latest base branch as well as the change. If the pull request has merge conflicts, GitHub can't create that commit, and the summary check fails with **Merge conflict with the base branch**.

When you push a new commit to a pull request, Chainguard Checks cancels the run for the previous commit and starts a new one.

Pull requests from forks run without approval, the same way as pull requests from branches. They get workload identities only if the repository's trust policy allows the pull request's author. To skip a check on pull requests from forks, give it a condition on `context.github.pull_request.head_repository`, as described in [Conditions](/chainguard/checks/configuration/#conditions).

## How results appear

Each run reports a summary check and one GitHub check for each of your checks.

For a pull request, the summary check is named **Chainguard Checks (presubmit)**. It's pending while the run is in progress, and passes only when every blocking check passes. When the run finishes, its output lists each check's result, including advisory checks that failed and checks that run on request.

Each of your checks gets a GitHub check named `presubmit / <file> / <check>`, where `<file>` is `ci` in the single-file layout, or the file's name in the directory layout. For example, a `test` check in `.chainguard/ci.yaml` appears as **presubmit / ci / test**. Each one appears when its check finishes. A check that runs once for each of several variations, with `foreach`, appears as one GitHub check that counts how many variations passed.

To read a check's output, select it on the pull request's **Checks** tab. The output shows each step's outcome, exit code, and duration, then the end of the check's log and any errors and warnings it reported. JSON log lines, such as the output of `go test -json` or Terraform's `-json` option, appear as readable messages, with errors and warnings marked `ERROR:` and `WARNING:`. If a long log has an error-level line well before its end, the output also keeps the lines leading up to that error under `[Earlier error context]`, then shows the end of the log under `[Log tail]`. The **Details** link opens the run's full log on a run page that Chainguard hosts, separate from the Chainguard Console.

## Require checks before merging

To block merging until checks pass, add **Chainguard Checks (presubmit)** as a required status check in a branch protection rule or ruleset for your default branch.

Don't require the per-check results, such as **presubmit / ci / test**. A check that a condition skips, or that runs only on request, never reports a result for that pull request, so GitHub would wait for it indefinitely. The summary check already accounts for every check that should block the pull request.

The summary check doesn't fail because of an [advisory check](/chainguard/checks/configuration/#advisory-checks), so you can add a check as advisory first and make it blocking later.

## Change checks in a pull request

A pull request can add checks and change what they run. It can't weaken its own checks:

- If a pull request makes an existing check advisory, or changes it to run only on request, the change takes effect after the pull request merges. Until then, the check keeps blocking the pull request, and the summary check's output says so.
- If a pull request removes a check, or changes its conditions or trigger so that it no longer runs for that pull request, the summary check fails with **Run creation failed**. The base branch's configuration would have run that check, and a change can't remove itself from its own checks. The exception is a check limited by `when.changed` to files that no longer exist.

## Rerun checks

To rerun a pull request's checks, for example after a flaky failure, use **Re-run** on the summary check or on one of its per-check results on GitHub. Chainguard Checks reruns the whole run for the same commit, without reusing cached results. Pushing a new commit also starts a new run.

You can also rerun a pull request's checks with `chainctl` after its latest run finishes. Replace `$OWNER/$REPO#$NUMBER` with the pull request, such as `acme/app#123`, or with its URL. Replace `$ORGANIZATION` with the name of your Chainguard organization:

```shell
chainctl checks rerun "$OWNER/$REPO#$NUMBER" --parent $ORGANIZATION
```

The command reruns the pull request's latest run the same way as **Re-run** on GitHub. Nothing reruns if the pull request is closed, or if it has new commits since that run started. Follow the rerun on the pull request, because the `--watch` flag can't follow a pull request's rerun yet.

During the beta, you can't rerun checks that run after merging. Selecting **Re-run** on **Chainguard Checks (postsubmit)** or on one of its per-check results doesn't start a new run. To run those checks again, push or merge a new commit to your default branch.

## Run a check on request

A check with `when: {requested: true}` runs only when someone asks for it. Until then, it reports no result and doesn't block the pull request. When a run finishes, the summary check's output lists each check that can run on request, with the label that runs it.

To run a check on request, add the label `ci/run:<check>` to the pull request. For example, `ci/run:e2e-full` runs the `e2e-full` check. If two files in the directory layout have a check with the same name, include the file's name, such as `ci/run:go/e2e-full`. Adding labels requires the triage or write role on the repository.

A label also forces a check that `when.changed` would skip to run, but it doesn't override a `when.expr` condition.

GitHub only offers labels that already exist in the repository, so create each label once. This example uses the GitHub CLI. Replace `$OWNER/$REPO` with your repository:

```shell
gh label create ci/run:e2e-full --repo $OWNER/$REPO --description "Run the e2e-full check"
```

After you create the label, anyone with the triage or write role can add it to a pull request from GitHub's label picker.

What happens after you add the label depends on the current run:

| Current run | What happens |
| ----------- | ------------ |
| It passed. | The summary check goes back to pending, and the commit runs again with the requested check included. |
| It failed. | Nothing starts. The requested check runs on your next push or rerun. |
| It's still running. | Chainguard Checks waits for it to finish. If it passes, Chainguard Checks runs the commit again with the requested check included. |

Removing a label takes effect from the next push. A rerun keeps every check the run was asked to include.

## Run checks after merging

Checks with `trigger: postsubmit` run on each new commit on your default branch. Each new commit in the default branch's first-parent history gets its own run, so a merge commit gets one run, and a rebase merge of five commits gets five. The results appear on the commit as **Chainguard Checks (postsubmit)** and one GitHub check for each postsubmit check.

Use postsubmit checks for work that should run on merged code rather than on each pull request, such as a slow integration suite. A pull request can't fail because of a postsubmit check, so if a postsubmit check fails, fix it in a new pull request.
