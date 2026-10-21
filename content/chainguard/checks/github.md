---
title: "Use Chainguard Checks on GitHub"
linktitle: "Checks on GitHub"
description: "Learn when Chainguard Checks runs on GitHub, how to read its results, and how to require checks before merging, rerun them, and run checks on request."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-20T14:50:35+00:00
draft: false
tags: ["Chainguard Checks", "GitHub", "Configuration"]
images: []
menu:
  docs:
    parent: "checks"
toc: true
weight: 40
---

Chainguard Checks runs on your GitHub repositories through the Chainguard App and reports its results as GitHub checks. This page explains when Chainguard Checks runs, how its results appear on GitHub, how to read them with the GitHub API, and how to use them to protect your branches.

## When Checks runs {#when-checks-runs}

Chainguard Checks runs on a repository when the Chainguard App is installed on the repository, its GitHub account is linked to a Chainguard organization with access to Chainguard Checks, and the repository has a `.chainguard/ci.yaml` file or a `.chainguard/ci/` directory. For a pull request, Chainguard Checks looks for the configuration on the pull request's branch and on its base branch.

| Event | What Chainguard Checks runs |
| ----- | --------------------------- |
| A pull request is opened, reopened, or updated | The repository's presubmit checks, which are checks without a `trigger` key or with `trigger: presubmit`. |
| A new commit arrives on the default branch | The repository's postsubmit checks, which are checks with `trigger: postsubmit`. |

Pushes to other branches, tags, and closed pull requests don't start runs.

For a pull request, Chainguard Checks runs against the commit GitHub would create by merging the pull request into its base branch, and reads the configuration from that commit. The result reflects the latest base branch as well as the change. If the pull request has merge conflicts, GitHub can't create that commit, and the summary check fails with **Merge conflict with the base branch**.

When you push a new commit to a pull request, Chainguard Checks cancels the run for the previous commit and starts a new one. Closing or merging a pull request doesn't cancel its run. The run finishes, reports its results on the pull request, and uses your organization's [Checks allowance](/chainguard/checks/overview/#availability-and-limits) until it ends. To stop the run, use [`chainctl checks cancel --force`](/chainguard/checks/chainctl-checks-reference/#chainctl-checks-cancel).

Pull requests from forks run without approval, the same way as pull requests from branches. To skip a check on pull requests from forks, give it a condition on `context.github.pull_request.head_repository`, as described in [Conditions](/chainguard/checks/configuration/#conditions). The condition also skips pull requests that your own team opens from forks.

Without a `trust` section in `.chainguard/ci/identities.yaml` on your default branch, any open pull request, including one from a fork, can get a [workload identity](/chainguard/checks/identity-and-trust/). Refer to [Limit which pull requests get an identity](/chainguard/checks/identity-and-trust/#limit-which-pull-requests-get-an-identity).

## How results appear {#how-results-appear}

Each run reports a summary check, plus a GitHub check for each of your checks that doesn't pass or that [reports errors, warnings, notices, or a summary](/chainguard/checks/configuration/#report-errors-and-annotations).

For a pull request, the summary check is named **Chainguard Checks (presubmit)**. It's pending while the run is in progress, and passes only when every blocking check passes. When the run finishes, its output lists each check's result, as described in [Read the summary check](#read-the-summary-check).

Each of these GitHub checks is named `presubmit / <file> / <check>`, where `<file>` is the name of the file that defines the check, without `.yaml`. For example, a `test` check in `.chainguard/ci.yaml` appears as **presubmit / ci / test**. Each one appears when its check finishes. A check that passes without reporting anything gets no GitHub check of its own, unless an earlier run for the same commit left one under its name. The summary check's output still lists it. When a check that runs once for each of several variations, with `foreach`, gets a GitHub check, it appears as one GitHub check that counts how many variations passed.

If a pull request changes `.chainguard/develop.yaml`, or a file it takes its environment from, Chainguard Checks also reports a check named **Chainguard Checks / develop-environment**. This check reads the file the way a [Chainguard Workspaces](/chainguard/workspaces/session-environment/) session would, without starting a session or installing packages, and marks each problem on its file and line. It isn't part of the run: the summary check doesn't count it, and **Re-run** on it does nothing. If it finds a problem, it fails, but it doesn't block merging. To clear a problem, push a commit that fixes it.

To read a check's output, select it on the pull request's **Checks** tab. The output shows each step's outcome, exit code, and duration, then the end of the check's log and any errors and warnings it reported. JSON log lines, such as the output of `go test -json` or Terraform's `-json` option, appear as readable messages, with errors and warnings marked `ERROR:` and `WARNING:`. If a long log has an error-level line well before its end, the output also keeps the lines leading up to that error under `[Earlier error context]`, then shows the end of the log under `[Log tail]`.

The **Details** link opens the check on a run page that Chainguard hosts, separate from the Chainguard Console. To open it, sign in with your Chainguard account. You also need a role in your Chainguard organization, as described in [The Details link or a chainctl checks command says you don't have access](/chainguard/checks/troubleshooting/#the-details-link-or-a-chainctl-checks-command-says-you-dont-have-access). Without one, read the check's output on GitHub. Besides the full log, the run page shows a timeline of the run and the programs that each step started, with how long each program ran and how it exited. Chainguard keeps these program records for 30 days, and never records the programs' arguments.

On the run page, the check's **Details** view lists each host and address that the check tried to reach under **Network activity**, with whether Chainguard Checks allowed the connection, and suggests an `egress` list to start from. To use it to fix a blocked connection, refer to [A check can't reach a host](/chainguard/checks/troubleshooting/#a-check-cant-reach-a-host).

### Read the summary check {#read-the-summary-check}

The summary check's title says how the run ended:

| Title | What it means |
| ----- | ------------- |
| **All N check(s) passed** | Every check passed or didn't need to run for this change. |
| **All N blocking check(s) passed; M advisory check(s) did not** | Every blocking check passed, and at least one [advisory check](/chainguard/checks/configuration/#advisory-checks) didn't. |
| **N of M blocking check(s) failed** | At least one blocking check failed. N also counts blocking checks that couldn't be executed. If no check is advisory, the title leaves out "blocking". |
| **N check(s) could not be executed** | No blocking check failed, but at least one couldn't run to the end. |

The output starts with the merge commit the run tested and how many checks passed. It then lists how many checks weren't instantiated, which means their conditions or `foreach` selected nothing for this change. A check that isn't instantiated counts as passing. The output also lists the checks that can run on request, with the label for each, any advisory checks that didn't pass, and any checks that labels requested.

Then a table lists each check with its outcome, a class for a check that failed or couldn't be executed, and the exit code of a check that failed. A check with `foreach` has one row, plus a row for each variation that didn't pass. The table shows up to 50 rows, and an advisory check's outcome ends with `(advisory)`.

| Outcome | Class | What it means |
| ------- | ----- | ------------- |
| `PASSED` | | The check passed. |
| `FAILED` | `CHECK` | A command exited with a nonzero code, shown under **Exit code**. |
| `FAILED` | `POLICY` | The check has `policy: destroy` and tried to reach a host it doesn't list, so Chainguard Checks stopped its VM. The check fails even if its commands would have succeeded. |
| `ERRORED` | `TIMEOUT` | The check ran longer than its `timeout`. |
| `ERRORED` | `INFRA` | Something else kept the check from finishing, such as packages that can't be installed together, a workload identity that the pull request doesn't get, or a VM that kept failing after [automatic retries](#automatic-retries). |
| `DEPENDENCY_FAILED` | | A check that it `needs` didn't pass, so it didn't run. |
| `NOT_INSTANTIATED` | | The check didn't need to run for this change, because of its conditions or because it runs only on request. It counts as passing. |

For each check that couldn't be executed, the reason appears under **Errors:** after the table, and the check's own GitHub check is titled **Could not be executed**, followed by the reason. For how to fix the common reasons, refer to [Troubleshoot Chainguard Checks](/chainguard/checks/troubleshooting/).

## Read results with the GitHub API {#read-results-with-the-github-api}

A merge bot, a dashboard, or an agent can read results through GitHub's REST API, which calls each GitHub check a *check run*. The API needs only GitHub access that can read the repository's pull requests and checks. It doesn't need a Chainguard role that can read runs, so it also works if you have the `limited_owner` role in a Starter organization. For example, a GitHub App needs read access to **Checks** and **Pull requests**, and a personal access token (classic) needs the `repo` scope for a private repository. Fine-grained personal access tokens don't have a **Checks** permission.

Results appear on the pull request's head commit, not on the merge commit that Chainguard Checks tests. List the head commit's check runs by name. Filtering by app alone isn't enough, because the Chainguard App also reports checks for other Chainguard products, such as Guardener. These commands use the GitHub CLI. Replace `$OWNER/$REPO` with your repository and `$NUMBER` with the pull request's number:

```shell
SHA=$(gh api "repos/$OWNER/$REPO/pulls/$NUMBER" --jq .head.sha)
gh api --method GET "repos/$OWNER/$REPO/commits/$SHA/check-runs" \
  -f check_name="Chainguard Checks (presubmit)" \
  --jq '.check_runs[0] | {status, conclusion, title: .output.title}'
```

By default, the API returns only the newest check run with that name. The summary check is finished when its `status` is `completed`. Its `conclusion` is then `success` only if every blocking check passed or didn't need to run, so treat any other conclusion as not passing. Act on `conclusion`, not on the title, which is written for people. If every field stays `null`, the commit has no summary check, so refer to [A pull request gets no checks](/chainguard/checks/troubleshooting/#a-pull-request-gets-no-checks). For a commit on your default branch, use the commit's SHA and set `check_name` to `Chainguard Checks (postsubmit)`.

A result can go out of date, so get the head commit's SHA and read the summary check again just before you act on it:

- A rerun, a `ci/run:` label, or a [change to the pull request](#reruns-when-a-pull-request-changes) can start a new run on the same commit, and the summary check goes back to `queued` or `in_progress`.
- A push moves the pull request to a new head commit. Chainguard Checks cancels the earlier commit's run, and that commit's summary check can stay `queued` or `in_progress` indefinitely.

To see which of your checks failed, read their own check runs. Each check gets one when it finishes:

| Outcome | Check run's conclusion |
| ------- | ---------------------- |
| `PASSED` | `success` |
| `FAILED` | `failure` |
| `ERRORED` | `failure` |
| `DEPENDENCY_FAILED` | `skipped` |
| `NOT_INSTANTIATED` | No check run |

An advisory check gets the same conclusion as a blocking check with the same outcome. A check with `foreach` gets one check run, with the conclusion `failure` if any variation failed or couldn't be executed. Each planner, described in [Compute variations during a run](/chainguard/checks/variations-services-caches/#compute-variations-during-a-run), also gets a check run when it finishes. A check run can also end `cancelled` or `neutral`, so treat any conclusion other than `success` as not passing.

Decide whether a pull request passes from the summary check alone, not from the per-check results:

- Some checks have no check run: checks that weren't instantiated, checks that haven't finished, and checks that never will because the run ended early, such as when the summary check fails with **Run failed**. A run that can't start, such as when the summary check fails with **Run creation failed**, reports no per-check results at all.
- A failed advisory check shows `failure` while the summary check passes.
- A check run from an earlier run on the same commit can remain. The API returns it until the new run reports that check, and keeps returning it if the new run never does, such as when the check isn't instantiated this time or the new run can't start.

Only the summary check always reflects the latest run, but its table shows up to 50 rows. With a role in your Chainguard organization, `chainctl checks status` shows every check's result, as described in [Inspect pull request runs](/chainguard/checks/inspect-and-run-checks/#inspect-pull-request-runs). For the API's parameters and fields, refer to GitHub's [REST API endpoints for check runs](https://docs.github.com/en/rest/checks/runs).

## Require checks before merging {#require-checks-before-merging}

To block merging until checks pass, add **Chainguard Checks (presubmit)** as a required status check in a branch protection rule or ruleset for your default branch.

Don't require the per-check results, such as **presubmit / ci / test**, or **Chainguard Checks / develop-environment**. A check that passes without reporting anything, that a condition skips, or that runs only on request never reports a result of its own for that pull request, and the develop-environment check appears only on pull requests that change its files, so GitHub would wait for them indefinitely. The summary check already accounts for every check that should block the pull request.

During the beta, Chainguard Checks doesn't run on GitHub merge queues. If a branch uses a merge queue and requires **Chainguard Checks (presubmit)**, the queue waits for a result that never arrives, and removes the pull request when its timeout expires. Don't require the summary check on a branch that uses a merge queue.

The summary check doesn't fail because of an [advisory check](/chainguard/checks/configuration/#advisory-checks), so you can add a check as advisory first and make it blocking later.

## Change checks in a pull request {#change-checks-in-a-pull-request}

A pull request can add checks and change what they run. It can't weaken its own checks:

- If a pull request makes an existing check advisory, or changes it to run only on request, the change takes effect after the pull request merges. Until then, the check keeps the base branch's setting, so a blocking check keeps blocking the pull request, and the summary check's output says so. A change that makes a check stricter, such as making an advisory check blocking, takes effect on the same pull request.
- If a pull request removes a check, or changes its conditions or trigger so that it no longer runs for that pull request, the summary check fails with **Run creation failed**. The base branch's configuration would have run that check, and a change can't remove itself from its own checks. The exception is a check limited by `when.changed` to files that no longer exist.
- If a pull request leaves no presubmit checks, such as by changing every check to `trigger: postsubmit`, it fails the same way when the base branch's configuration has any presubmit check, even one that wouldn't have run for this pull request. A check limited by `when.changed` to files that no longer exist doesn't count. The pull request also fails this way if the base branch's configuration is invalid. Otherwise, it gets no Chainguard Checks run or summary check at all.

Chainguard Checks applies these rules to the pull request as it is now, including whether it's a draft and which labels it has. Conditions and labels can change which checks the base branch's configuration would run, so a change that passed as a draft can fail with **Run creation failed** when it [runs again](#reruns-when-a-pull-request-changes) after you mark it ready for review.

## Rerun checks {#rerun-checks}

To rerun a pull request's checks, for example after a flaky failure, use **Re-run** on the summary check or on one of its per-check results on GitHub. Chainguard Checks reruns the whole run for the same commit, without reusing earlier results or caches. Pushing a new commit also starts a new run. If the base branch has removed its Chainguard Checks configuration, or all of its presubmit checks, since the pull request's last run, a rerun or a `ci/run:` label starts nothing. The summary check shows that run's result again, notes that nothing can run, and lists any checks that labels requested under **Requested but not run**.

You can also rerun a pull request's checks with `chainctl` after its latest run finishes. Like the run page, this needs a role in your Chainguard organization, as described in [The Details link or a chainctl checks command says you don't have access](/chainguard/checks/troubleshooting/#the-details-link-or-a-chainctl-checks-command-says-you-dont-have-access). Without one, use **Re-run** on GitHub. Replace `$OWNER/$REPO#$NUMBER` with the pull request, such as `acme/app#123`, or with its URL. Replace `$ORGANIZATION` with the name of your Chainguard organization:

```shell
chainctl checks rerun "$OWNER/$REPO#$NUMBER" --parent $ORGANIZATION
```

The command reruns the pull request's latest run the same way as **Re-run** on GitHub. Nothing reruns if the pull request is closed, or if it has new commits since that run started. Until the new run starts, `chainctl checks status` shows the previous run, and the summary check shows **Re-run requested by *IDENTITY_ID* via chainctl**, where *IDENTITY_ID* is your Chainguard identity ID. After the summary check shows the new run's progress, follow the rerun:

```shell
chainctl checks status "$OWNER/$REPO#$NUMBER" --parent $ORGANIZATION --watch
```

For more ways to inspect a pull request's run from your terminal, refer to [Inspect pull request runs](/chainguard/checks/inspect-and-run-checks/#inspect-pull-request-runs). To find the checks that fail most often across runs, refer to [See check history](/chainguard/checks/inspect-and-run-checks/#see-check-history).

During the beta, you can't rerun checks that run after merging. Selecting **Re-run** on **Chainguard Checks (postsubmit)** or on one of its per-check results doesn't start a new run. To run those checks again, push or merge a new commit to your default branch.

### Reruns when a pull request changes {#reruns-when-a-pull-request-changes}

After a run passes, Chainguard Checks runs the same commit again when you edit the pull request's title, add or remove a label, mark it ready for review, or convert it to a draft, if either of the following is true:

- A [`when.expr` condition](/chainguard/checks/configuration/#run-when-an-expression-is-true) skipped one of the run's checks.
- The pull request changes your Chainguard Checks configuration, such as `.chainguard/ci.yaml` or a file in `.chainguard/ci/`.

The summary check goes back to pending with **Pull request changed; running again**, and every check runs again with the pull request as it is now. For a change to your configuration, Chainguard Checks applies the rules in [Change checks in a pull request](#change-checks-in-a-pull-request) again, so the summary check can fail with **Run creation failed**. Editing the pull request's description doesn't start a new run, and neither does a change to a pull request whose run failed.

### Automatic retries {#automatic-retries}

If a check can't finish for a reason outside the check, such as a VM that doesn't start or loses its connection, Chainguard Checks runs the check again in a new VM, up to three attempts in all. It doesn't retry a check that fails, times out, or is stopped by `policy: destroy`, or one with a problem that a retry can't fix, such as packages that can't be installed together, or a workload identity that the pull request doesn't get.

A retry runs every step again from the first, so make steps with side effects, such as an upload, safe to repeat. The check's `timeout` keeps counting across attempts, except for the time spent starting each VM, and every attempt counts toward the run's [two-hour limit](/chainguard/checks/configuration/#timeouts).

## Run a check on request {#run-a-check-on-request}

A check with `when: {requested: true}` runs only when someone asks for it. Until then, it reports no result and doesn't block the pull request. When a run finishes, the summary check's output lists each check that can run on request, with the label that runs it.

To run a check on request, add the label `ci/run:<check>` to the pull request. For example, `ci/run:e2e-full` runs the `e2e-full` check. If two files have a check with the same name, include the file's name, such as `ci/run:go/e2e-full`. Labels match check names regardless of case, so `ci/run:E2E-Full` also runs `e2e-full`. Adding labels requires the triage or write role on the repository.

A check that runs on request has limits on its name and its other conditions, as described in [Run on request](/chainguard/checks/configuration/#run-on-request). To run a check when its files change and also on request, use `when.changed` alone, because a label also forces a check that `when.changed` would skip to run. A label doesn't override a `when.expr` condition.

GitHub only offers labels that already exist in the repository, so create each label once. This example uses the GitHub CLI. Replace `$OWNER/$REPO` with your repository:

```shell
gh label create ci/run:e2e-full --repo $OWNER/$REPO --description "Run the e2e-full check"
```

After you create the label, anyone with the triage or write role can add it to a pull request from GitHub's label picker.

What happens after you add the label depends on the current run:

| Current run | What happens |
| ----------- | ------------ |
| It passed. | The summary check goes back to pending, and the commit runs again with the requested check included. |
| It failed. | Nothing starts. The summary check's output lists the check under **Requested after this run did not pass, so not run**, and it runs on your next push or rerun. |
| It's still running. | Chainguard Checks waits for it to finish. If it passes, Chainguard Checks runs the commit again with the requested check included. |

The summary check's output lists the checks that labels requested under **Requested by label**. Removing a label takes effect from the next push. A rerun keeps every check the run was asked to include.

## Let an agent request checks {#let-an-agent-request-checks}

Instead of adding labels yourself, you can have an agent pick which checks each pull request should run. The agent chooses from *requestable checks*: presubmit checks with `when: {requested: true}`, and `when.changed` checks that the pull request's changes didn't select. It never picks a check that's already running, or one whose `when.expr` condition is false.

To turn on the agent, set [`requested_checks_agent`](/chainguard/checks/configuration/#top-level-keys) at the top level of `.chainguard/ci.yaml`, or of `.chainguard/ci/env/default.yaml` in the directory layout:

```yaml {title=".chainguard/ci.yaml"}
version: 1
requested_checks_agent: comment
environment:
  packages: [go]
checks:
  # ...
```

| Value | What the agent does |
| ----- | ------------------- |
| `off` (default) | Nothing. |
| `comment` | Comments with the checks it would request and the label for each. To run one, a person adds its label. |
| `agent` | Adds a `ci/run:<check>` label for each check it picks, and comments with its reasons. |

Start with `comment` to see what the agent picks before you let it add labels. Chainguard Checks reads the setting from the tip of the pull request's base branch, so it takes effect after the pull request that sets it merges.

The agent runs when a pull request is opened or reopened, gets new commits, is marked ready for review, or changes its base branch. It skips drafts and closed pull requests, and answers once for each commit and base branch.

The agent picks checks by their `description` and their [`docs`](/chainguard/checks/configuration/#describe-a-check) file. For a check that already exists on the base branch, it reads both from the base branch, so a pull request can't rewrite them to get a check picked. Write each description to say what the check covers and when it's worth running. The agent rarely picks a check without a description, so give `when.changed` checks a `description` too.

### What the agent shows on the pull request

The Chainguard App keeps one **Requested checks** comment on the pull request and edits it after each push. The comment lists each check that the agent picked, with its label and a one-sentence reason, then a collapsed list of the requestable checks it didn't pick. The agent doesn't comment when every requestable check already runs.

Labels that the agent adds work the same way as labels a person adds, as described in [Run a check on request](#run-a-check-on-request). The agent never removes a label, and doesn't add back a label that someone removed. To stop a check that the agent requested from running, remove its label. The change takes effect from the next push. The agent only adds checks, so it can't make a failing summary check pass.

### What the agent reads {#what-the-agent-reads}

The agent is off unless your base branch sets `requested_checks_agent` to `comment` or `agent`. When it's on, each time the agent runs, Chainguard Checks sends the following to an Anthropic Claude model that Chainguard runs on Google Cloud Vertex AI:

- The repository's name.
- The pull request's title and description.
- The changed files, with the number of lines added and removed in each.
- Each requestable check's name, `when.changed` patterns, `description`, and `docs` file.

The model can also read a changed file's diff and any file at the pull request's head commit, up to 15 reads each time. Chainguard Checks marks the pull request's title, description, and files as untrusted input for the model, and accepts only picks from the requestable checks. The agent's GitHub access is limited to reading the repository's contents and writing labels and comments on pull requests. It runs on pull requests from forks as well as on pull requests from branches.

Before you turn on the agent, review the terms that Chainguard Checks is offered under, including the [Code Analysis Terms](https://www.chainguard.dev/legal/code-analysis-terms). Don't turn it on for a repository whose pull requests contain personal data, or any data subject to legal or regulatory compliance requirements.

## Run checks after merging {#run-checks-after-merging}

Checks with `trigger: postsubmit` run on each new commit on your default branch. Each new commit in the default branch's first-parent history gets its own run, so a merge commit gets one run, and a rebase merge of five commits gets five. The results appear on the commit as **Chainguard Checks (postsubmit)**, with per-check results named `postsubmit / <file> / <check>`, as described in [How results appear](#how-results-appear).

For a run after merging, `when.changed` compares the new commit with its first parent. A merge commit or a squash merge selects checks by the whole pull request's changes, and each commit of a rebase merge selects them by its own changes only. A commit has no labels, so a check with `when: {requested: true}` never runs after merging, and one that also has only `trigger: postsubmit` never runs at all. To run that work on merged code, define a separate postsubmit check without `requested`.

Use postsubmit checks for work that should run on merged code rather than on each pull request, such as a slow integration suite. A pull request can't fail because of a postsubmit check, so if a postsubmit check fails, fix it in a new pull request.
