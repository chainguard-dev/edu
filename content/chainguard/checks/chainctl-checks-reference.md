---
title: "chainctl checks command reference"
linktitle: "chainctl checks reference"
description: "Reference for the chainctl checks commands that inspect pull request runs, start and rerun checks, summarize check history, and validate your Chainguard Checks configuration."
type: "article"
date: 2026-10-12T00:00:00+00:00
lastmod: 2026-10-20T15:35:02+00:00
draft: false
tags: ["Chainguard Checks", "chainctl", "Reference"]
images: []
menu:
  docs:
    parent: "checks"
toc: true
weight: 65
---

The `chainctl checks` commands read your pull requests' results from your terminal, start and rerun checks, summarize your checks' history, and validate your configuration. This page lists each command's arguments, flags, exit codes, and JSON output. For examples of the commands in use, refer to [Inspect and run checks with chainctl](/chainguard/checks/inspect-and-run-checks/).

{{% blurb/hidden-chainctl-commands %}}

For example, run `chainctl checks status --help`. You can also type `chainctl ci` instead of `chainctl checks`. If `chainctl` doesn't recognize a command or flag on this page, [update chainctl](/platform/chainctl-usage/how-to-install-chainctl/#updating-chainctl).

The examples on this page use `acme/app#123` for a pull request. Replace `$ORGANIZATION` with the name of your Chainguard organization.

## Commands {#commands}

| Command | What it does |
| ------- | ------------ |
| [`chainctl checks status`](#chainctl-checks-status) | Shows a run and whether each of its checks passed. |
| [`chainctl checks failures`](#chainctl-checks-failures) | Shows why a run's checks failed. |
| [`chainctl checks logs`](#chainctl-checks-logs) | Prints a run's check logs, or part of one. |
| [`chainctl checks trace`](#chainctl-checks-trace) | Shows the programs that each step of a check started. |
| [`chainctl checks attempts`](#chainctl-checks-attempts) | Lists each attempt at a check. |
| [`chainctl checks events`](#chainctl-checks-events) | Prints the events that one attempt at a check recorded. |
| [`chainctl checks describe`](#chainctl-checks-describe) | Shows where a run came from, its status, and each of its checks. |
| [`chainctl checks list`](#chainctl-checks-list) | Lists the runs you started with `chainctl checks run`. |
| [`chainctl checks run`](#chainctl-checks-run) | Runs a pushed commit's checks without a pull request. |
| [`chainctl checks rerun`](#chainctl-checks-rerun) | Reruns a pull request's latest run. |
| [`chainctl checks cancel`](#chainctl-checks-cancel) | Cancels a run that hasn't finished. |
| [`chainctl checks stats`](#chainctl-checks-stats) | Counts the outcomes of your organization's newest runs. |
| [`chainctl checks top`](#chainctl-checks-top) | Ranks your organization's checks over a window of time. |
| [`chainctl checks trends`](#chainctl-checks-trends) | Shows how long checks take, hour by hour. |
| [`chainctl checks validate`](#chainctl-checks-validate) | Finds problems in your configuration without running anything. |
| [`chainctl checks explain`](#chainctl-checks-explain) | Prints each check as Chainguard Checks reads it. |
| [`chainctl checks migrate`](#chainctl-checks-migrate) | Drafts a configuration from your GitHub Actions workflows. |
| [`chainctl checks accept-terms`](#chainctl-checks-accept-terms) | Accepts the terms that Chainguard Checks is offered under. |

## Access and organization {#access-and-organization}

Every command on this page except `validate`, `explain`, `migrate --dry`, and `accept-terms` needs the `owner` or `sandbox.user` role in the Chainguard organization linked to the repository's GitHub account. Without one of these roles, the commands fail with `permission denied`. To get a role, refer to [Give teammates access](/get-started/checks-and-workspaces/set-up/#give-teammates-access).

If you created a Starter organization with `chainctl develop init`, you have the `limited_owner` role instead. That role can start runs, with `chainctl checks run` or with `chainctl checks migrate` without `--dry`, but it can't read any run. Those runs use your allowance without showing you their results, so don't use either command in a Starter organization. Read the results on GitHub instead, as described in [The Details link or a chainctl checks command says you don't have access](/chainguard/checks/troubleshooting/#the-details-link-or-a-chainctl-checks-command-says-you-dont-have-access).

The `validate`, `explain`, and `migrate --dry` commands read only your local checkout, so they don't need a Chainguard account or network access.

The commands that need a role take `--parent` with the name or ID of your Chainguard organization. Without `--parent`, `chainctl` uses the `CHAINCTL_SANDBOX_GROUP` environment variable, then the `default.group` value in your `chainctl` configuration. If neither is set, it asks you to choose an organization.

## Name a run {#name-a-run}

Most commands that read runs take a `REF` argument that names the run. During the beta, use one of the following forms:

| `REF` | Example | What it names |
| ----- | ------- | ------------- |
| A pull request | `acme/app#123`, or `https://github.com/acme/app/pull/123` | The pull request's newest run. Capitalize the owner and repository the same way GitHub does. |
| A run ID | `$RUN_ID` | One run. For a run after merging, use the whole ID after `/runs/` in the **Details** link of **Chainguard Checks (postsubmit)**. For a run you started with `chainctl checks run`, you can use the start of its ID. |

The `chainctl checks status -o json` command prints the run's full name in its `run` field. Pass that name to the other commands to keep reading the same run after someone pushes to the pull request.

The commands also accept a directory, which stands for the commit checked out there, or a full commit SHA. During the beta, these never find your repositories' runs, so the commands report that the platform created no run, even when checks ran. Without a `REF`, the commands use the current directory, so pass a pull request or a run ID instead. Refer to [chainctl checks status reports no platform verdict](/chainguard/checks/troubleshooting/#chainctl-checks-status-reports-no-platform-verdict).

## Output and exit codes {#output-and-exit-codes}

To print JSON for a script or a coding agent, add `-o json`, which is short for `--output json`. Each command's section describes its JSON.

On a terminal, commands that print your repository's output remove escape sequences and other control characters from it. To keep them, add `--raw` to a command that takes it. When the output isn't a terminal, such as when you pipe it to a file, the commands always print it as it is.

Unless a command's section says otherwise, it exits with `0` when it succeeds and `1` when it fails.

## Inspect runs {#inspect-runs}

### chainctl checks status {#chainctl-checks-status}

Shows a run and whether each of its checks passed.

```
chainctl checks status REF [--watch]
```

| Flag | Description |
| ---- | ----------- |
| `--watch` | Waits until the run finishes, and prints the checks again each time they change. |

For example, to wait for a pull request's checks to finish:

```shell
chainctl checks status acme/app#123 --watch --parent $ORGANIZATION
```

The output marks a failed advisory check as `(advisory)`, and shows the label that runs each check that runs only on request. The command exits with one of the following codes:

| Exit code | Meaning |
| --------- | ------- |
| `0` | The run passed, or it's still running and you didn't add `--watch`. |
| `1` | The run finished and a blocking check didn't pass, or the command failed. |
| `2` | Chainguard Checks created no run for the `REF`. |

With `-o json`, the command prints one object, the final one with `--watch`. It has the run's `run`, `repository`, `revision`, `pull_request`, `phase`, and `outcome`, and `failed`, which is `true` when the command exits with `1`. Its `checks` list has each check's `workflow`, `check`, `phase`, and `outcome`, plus `exit_code`, `advisory`, and `request_label` when they apply. When there's no run, the object's `status` is `no platform verdict`.

### chainctl checks failures {#chainctl-checks-failures}

Shows why a run's checks failed. For each failed check, the command shows the step that failed, with its exit code and command, and the end of the failing output, quoted from the check's log. For Go tests that a step runs with `go test -json`, it quotes the failing tests. Otherwise, it quotes the programs that exited with an error, or the end of the step's output, with a note that says which one it quoted and why. For a check with no record of why it failed, such as one that couldn't be executed, the command shows the check's error and a `chainctl checks logs` command that reads the end of its log.

```
chainctl checks failures REF [--check CHECK [--workflow WORKFLOW]] [--budget BYTES] [--not-run] [--raw]
```

| Flag | Description |
| ---- | ----------- |
| `--check` | Shows only this check. |
| `--workflow` | Names the file of the check, when two files have a check with that name. |
| `--budget` | Limits the output to this many bytes, 8 KiB by default. If the failures don't fit, the command shows as many checks in full as fit, then one line for each of the next ones, then the names of the rest. Without `--check`, it quotes at most 4 KiB of each check's output. |
| `--not-run` | Also lists the checks that didn't run or haven't finished, with the reason. The list doesn't count toward `--budget`. |
| `--raw` | Prints check names, commands, and quoted output as they are, including escape sequences, even on a terminal. |

For example, to see why a pull request's checks failed:

```shell
chainctl checks failures acme/app#123 --parent $ORGANIZATION
```

The output starts with the run's name, then its status and how many of its checks failed, passed, and didn't run. The command exits with `0` when it shows failures, so use `chainctl checks status` to test whether a run passed.

With `-o json`, the command prints one object with the run's name in `target`, its `phase` and `outcome`, the `counts` of checks that `passed`, `failed`, haven't finished (`running`), or didn't run (`not_run`), a `failed` list, and `truncated`, which is `true` when the command shortened or left out part of the output to fit `--budget`. Each failed check has its `check`, `outcome`, `exit_code`, the `step` that failed, and `quotes` from its log. Each quote has its `text` and the `log_ranges` it came from. When the log has output before the quote, the quote's `more` field is the `chainctl checks logs` command that reads that output. A check with no record of why it failed has no quotes, and its own `more` field is the command that reads the end of its log. With `--not-run`, the object also has a `not_run` list.

### chainctl checks logs {#chainctl-checks-logs}

Prints the combined standard output and standard error of a run's checks, followed by the errors, warnings, and notices each check reported, as described in [Report errors and annotations](/chainguard/checks/configuration/#report-errors-and-annotations). Without `--check`, the command prints every check's log, each after a line that names the check.

```
chainctl checks logs REF [--check CHECK [--workflow WORKFLOW]] [--follow] [--attempt N] [--raw]
chainctl checks logs REF --check CHECK (--errors | --grep RE) [-C N] [--max N] [--offset BYTES]
chainctl checks logs REF --check CHECK --tail N
chainctl checks logs REF --check CHECK --offset BYTES [--limit-bytes N]
```

| Flag | Description |
| ---- | ----------- |
| `--check` | Prints only this check's log. |
| `--workflow` | Names the file of the check, when two files have a check with that name. |
| `-f`, `--follow` | Keeps reading a running check's output until it finishes, and waits for a check that hasn't started. Without `--check`, it keeps reading until every check in the run finishes. |
| `--attempt` | Reads this attempt of a check that ran more than once, such as `1` for the first. Needs `--check`. To list a check's attempts, run [`chainctl checks attempts`](#chainctl-checks-attempts). |
| `--errors` | Shows only error lines, such as `::error` lines and error-level JSON or logfmt lines. If the log has none, the command shows its last 30 lines. |
| `--grep` | Shows only the lines that match this RE2 regular expression, reading at most 64 MiB of the log. |
| `-C`, `--context` | With `--errors` or `--grep`, shows this many lines before and after each line. |
| `--max` | With `--errors` or `--grep`, shows at most this many lines, 10 error lines or 20 matching lines by default. |
| `--tail` | Shows the log's last lines, up to this number or 16 KiB. |
| `--offset` | Starts `--errors` or `--grep` at this byte of the log, or reads the log from this byte. |
| `--limit-bytes` | With `--offset`, reads this many bytes, 64 KiB by default. |
| `--raw` | Prints the log as it is, including escape sequences, even on a terminal. |

The `--errors`, `--grep`, `--tail`, `--offset`, and `--limit-bytes` flags read part of one check's log, so they need `--check`, and you can't combine them with `--follow`. Use only one of `--errors`, `--grep`, and `--tail` at a time. Each excerpt starts with the byte range it covers. If the command leaves lines out, it says so, and gives the `--offset` to continue from.

For example, to show a failed check's error lines with three lines around each one:

```shell
chainctl checks logs acme/app#123 --check test --errors -C 3 --parent $ORGANIZATION
```

The `-o json` flag works only with `--errors`, `--grep`, `--tail`, `--offset`, or `--limit-bytes`. The command then prints one JSON object per line: one with `type` set to `excerpt` for each excerpt, with its `check`, `attempt`, `offset`, `end_offset`, and `text`, followed by one with `type` set to `summary`. The summary says how much the command showed, whether it left anything out, and the `next_offset` to continue from.

### chainctl checks trace {#chainctl-checks-trace}

Shows the programs that each step of a check started, with each program's name, how long it ran, and how it exited. Chainguard Checks records program names, never their arguments. For a failed step, the output names the program that most likely failed it. This guess comes from the recorded programs, so it can be wrong, such as when a shell or build tool ignores a program's exit code.

```
chainctl checks trace REF [--check CHECK [--workflow WORKFLOW]] [--failed]
```

| Flag | Description |
| ---- | ----------- |
| `--check` | Shows only this check's steps. Without it, the command shows every check that has recorded programs. |
| `--workflow` | Names the file of the check, when two files have a check with that name. |
| `--failed` | Shows only failed steps, each as the path from the step's command to the program that most likely failed it. |

For example:

```shell
chainctl checks trace acme/app#123 --check test --failed --parent $ORGANIZATION
```

A trace marked `INCOMPLETE` lost some of its records, or `chainctl` cut it to fit, so parts of it might be missing. With `-o json`, the command prints one JSON object per line for each step, with the step's `workflow`, `check`, `step` number, and its tree of programs in `document`.

### chainctl checks attempts {#chainctl-checks-attempts}

Lists each attempt at a check, oldest first. For each attempt, the command shows why it ran, such as an [automatic retry](/chainguard/checks/github/#automatic-retries) or a rerun, how it ended, when it started, and how long it took. It also marks each attempt whose result Chainguard Checks reused from an earlier run, and names that run. After the list, the command shows each attempt's error, if it had one, and how long the attempt spent queued, waiting for a free slot, booting its VM, setting up, and running its steps.

```
chainctl checks attempts REF --check CHECK [--workflow WORKFLOW]
```

| Flag | Description |
| ---- | ----------- |
| `--check` | The check to list attempts for. Required. |
| `--workflow` | Names the file of the check, when two files have a check with that name. |

For example:

```shell
chainctl checks attempts acme/app#123 --check test --parent $ORGANIZATION
```

To read one attempt's log or events, pass its number to `--attempt` in `chainctl checks logs` or `chainctl checks events`. With `-o json`, the command prints one object with the check's `workflow_run`, `workflow`, and `check`, and its `attempts` as the API returns them.

### chainctl checks events {#chainctl-checks-events}

Prints the events that one attempt at a check recorded, in order: when its setup, each of its steps, and each program that a step started began and ended, and any diagnostics attached to them.

```
chainctl checks events REF --check CHECK [--workflow WORKFLOW] [--attempt N]
```

| Flag | Description |
| ---- | ----------- |
| `--check` | The check to print events for. Required. |
| `--workflow` | Names the file of the check, when two files have a check with that name. |
| `--attempt` | Reads this attempt instead of the latest one. |

For example:

```shell
chainctl checks events acme/app#123 --check test --parent $ORGANIZATION
```

With `-o json`, the command prints the events as the API returns them.

### chainctl checks describe {#chainctl-checks-describe}

Shows where a run came from, its status, and each of its checks.

```
chainctl checks describe RUN [--steps] [--events]
```

`RUN` is a run ID, as described in [Name a run](#name-a-run). The command doesn't take a pull request, so to describe a pull request's run, pass the `run` field that `chainctl checks status -o json` prints.

| Flag | Description |
| ---- | ----------- |
| `--steps` | Adds each check's steps. |
| `--events` | Adds the run's events, and how long each attempt spent queued, waiting for a free slot, booting its VM, setting up, and running its steps. |

For example:

```shell
chainctl checks describe $RUN_ID --events --parent $ORGANIZATION
```

With `-o json`, the command prints one object with the `run`, its `workflow_runs`, and with `--events`, its `events`, as the API returns them.

### chainctl checks list {#chainctl-checks-list}

Lists the runs you started with `chainctl checks run`, newest first. During the beta, it doesn't list pull request runs or runs after merging.

```
chainctl checks list [--repo REPO] [--outcome OUTCOME] [--limit N]
```

| Flag | Description |
| ---- | ----------- |
| `--repo` | Lists only runs of this repository, such as `acme/app`. |
| `--outcome` | Lists only finished runs with this outcome: `passed`, `failed`, `errored`, `dependency_failed`, or `cancelled`. It searches the 500 newest runs. |
| `--limit` | Lists at most this many runs, 20 by default. |

For example:

```shell
chainctl checks list --repo acme/app --outcome failed --parent $ORGANIZATION
```

With `-o json`, the command prints a list with one object for each run, with its `run`, `create_time`, `repository`, `revision`, `phase`, and `outcome`.

## Start and stop runs {#start-and-stop-runs}

### chainctl checks run {#chainctl-checks-run}

Runs a commit's checks in Chainguard Checks without a pull request. The commit must be pushed to GitHub, because Chainguard Checks reads its configuration from there through your organization's link to the repository's GitHub account. To run checks against uncommitted changes, use `chainctl develop check` instead, as described in [Run checks in a session from your laptop](/chainguard/checks/run-checks/#run-checks-in-a-session-from-your-laptop).

```
chainctl checks run [DIR] [--check CHECK [--workflow WORKFLOW]] [--request CHECK]... [--git-remote NAME] [--base REV] [--watch]
```

`DIR` is a local checkout, the current directory by default. The command runs the commit checked out there, in the github.com repository of its `origin` remote.

| Flag | Description |
| ---- | ----------- |
| `--check` | Runs only this check and the checks it `needs`, including a check that runs only on request. |
| `--workflow` | Names the file of the check, when two files have a check with that name. |
| `--request` | Runs this check if it runs only on request, as a `ci/run:` label does on a pull request. Repeat the flag for more checks. |
| `--git-remote` | Uses the github.com repository of this remote instead of `origin`, such as `upstream` in a checkout of a fork. |
| `--base` | The commit that `when.changed` conditions compare against. By default, it's where the commit branched from the remote's default branch, or the commit's parent if the commit is on that branch. |
| `--watch` | Waits until the run finishes, and prints the checks again each time they change. |

For example, to run the `test` check and wait for its result:

```shell
chainctl checks run . --check test --watch --parent $ORGANIZATION
```

The run doesn't report to GitHub, and it never counts as a pull request's or commit's result. It uses your organization's Checks allowance like any other run. Because the run has no pull request, the command refuses a check whose `when.expr` condition reads the trigger, the pull request, or its labels.

The command prints the run's name, followed by its checks. The run's ID is the part of the name after `/runs/`. Pass the ID to `chainctl checks status`, `cancel`, or the other commands that read runs. With `--watch`, the command exits with `1` when a blocking check doesn't pass. With `-o json`, it prints the run as the API returns it, or with `--watch`, the run's final status in the same form as `chainctl checks status -o json`.

### chainctl checks rerun {#chainctl-checks-rerun}

Reruns a pull request's latest run after it finishes, the same way as **Re-run** on GitHub. Refer to [Rerun checks](/chainguard/checks/github/#rerun-checks) for what reruns and how to follow the new run.

```
chainctl checks rerun REF
```

During the beta, `REF` must be a pull request. The command can't rerun runs after merging or runs you started with `chainctl checks run`. To run checks after merging again, push or merge a new commit to your default branch. To repeat a run you started with `chainctl checks run`, run that command again.

For example:

```shell
chainctl checks rerun acme/app#123 --parent $ORGANIZATION
```

With `-o json`, the command prints the run whose checks it reruns, as the API returns it.

### chainctl checks cancel {#chainctl-checks-cancel}

Cancels a run that hasn't finished, stopping its checks that are queued or running. Checks that already finished keep their results. The command returns once Chainguard Checks accepts the request, before the checks stop. Canceling a run again changes nothing.

```
chainctl checks cancel RUN [--force]
```

`RUN` is a run ID, as described in [Name a run](#name-a-run), or the run's full name. The command doesn't take a pull request, so to cancel a pull request's run, pass the `run` field that `chainctl checks status -o json` prints.

| Flag | Description |
| ---- | ----------- |
| `--force` | Cancels a run that GitHub started, for a pull request or after merging. Without it, the command refuses these runs. |

Anyone with the `owner` or `sandbox.user` role in your organization can cancel any of its runs, including runs that someone else started. The `--force` flag doesn't change who can cancel a run. It only confirms that you mean to stop a run that GitHub started.

For example, to cancel a pull request's run:

```shell
RUN=$(chainctl checks status acme/app#123 -o json --parent $ORGANIZATION | jq -r .run)
chainctl checks cancel "$RUN" --force --parent $ORGANIZATION
```

When you cancel a run that GitHub started, its summary check on GitHub ends with **Run cancelled** and doesn't pass. To run the checks again, push a new commit, or rerun them as described in [Rerun checks](/chainguard/checks/github/#rerun-checks). Adding a `ci/run:` label or editing the pull request doesn't start a new run.

To find out when Chainguard Checks cancels a pull request's run on its own, refer to [When Checks runs](/chainguard/checks/github/#when-checks-runs).

With `-o json`, the command prints the run as the API returns it.

## Summarize check history {#summarize-check-history}

The `stats`, `top`, and `trends` commands summarize your organization's checks across runs. For examples, refer to [See check history](/chainguard/checks/inspect-and-run-checks/#see-check-history).

The `top` and `trends` output starts with the window it read and how current its data is, because the newest attempts can take time to appear. The first time you run either command, `chainctl` might ask you to sign in again. Without a terminal to sign in at, such as in a script, the command fails and prints the `chainctl auth login` command to run first.

### chainctl checks stats {#chainctl-checks-stats}

Counts the outcomes of your organization's newest runs, by repository and by check.

```
chainctl checks stats [--limit N]
```

| Flag | Description |
| ---- | ----------- |
| `--limit` | Counts at most this many runs, 500 by default and 2,000 at most. |

In the output, `OPEN` counts runs or checks that haven't finished, and `RUNNING` is the part of `OPEN` that's running. `FAIL%` is the share of failed results among the results that passed or failed, so checks that are still running, were canceled or skipped, or couldn't finish don't change it. `CONFIGS` counts the different configurations a repository's runs used.

With `-o json`, the command prints one object with the number of `runs` it read and a `repositories` list. Each repository has its `name`, `counts`, `configs`, and a `checks` list with each check's `name`, `counts`, and `median_seconds`. Each `counts` object has `total`, `passed`, `failed`, `errored`, `dependency_failed`, `not_instantiated`, `cancelled`, `open`, and `running`.

### chainctl checks top {#chainctl-checks-top}

Ranks your organization's checks over a window of time.

```
chainctl checks top [--repo REPO] [--since DURATION | --from TIME --to TIME] [--by count|runtime|failures] [--limit N]
```

| Flag | Description |
| ---- | ----------- |
| `--by` | Ranks checks by their number of attempts (`count`), their total runtime (`runtime`), or their failure rate (`failures`). The default is `runtime`. Only a check with at least 100 attempts in the window has a failure rate. |
| `--repo` | Ranks only checks of this repository, such as `acme/app`. |
| `--since` | Reads the window that ends now and lasts this long, such as `7d` or `36h`. The default is `14d`, and the longest is `31d`. |
| `--from`, `--to` | Reads the window between these RFC 3339 times, such as `2026-10-01T00:00:00Z`. Use both together, for a window of up to 31 days. |
| `--limit` | Shows at most this many checks, up to 20, which is the default. |

A check's failure rate is the share of its attempts that failed or couldn't finish, such as by timing out. Attempts include retries, but not attempts whose result Chainguard Checks reused from an earlier run.

With `-o json`, the command prints one object with the `window`, when the data was generated (`generatedAt`), the ranking (`by`), and a `checks` list. Each check has its `job_ref`, `name`, `attempts`, `failed`, `errored`, `runtime_seconds`, and `failure_rate`, which is `null` for a check with fewer than 100 attempts.

### chainctl checks trends {#chainctl-checks-trends}

Shows the median, 95th percentile, and 99th percentile durations of checks for each hour of a window, for the 10 checks with the most total runtime in that window. Hours with no attempts don't appear.

```
chainctl checks trends [--repo REPO] [--since DURATION | --from TIME --to TIME] [--check CHECK]
```

| Flag | Description |
| ---- | ----------- |
| `--check` | Shows only this check. A check outside the 10 has no trend. |
| `--repo` | Shows only checks of this repository, such as `acme/app`. |
| `--since` | Reads the window that ends now and lasts this long, such as `7d` or `36h`. The default is `14d`, and the longest is `31d`. |
| `--from`, `--to` | Reads the window between these RFC 3339 times. Use both together, for a window of up to 31 days. |

With `-o json`, the command prints one object with the `window`, `generatedAt`, and a `trends` list with one object for each check and hour. Each object has the check's `job_ref`, the `hour`, the number of attempts it measured in `samples`, and the `median_seconds`, `p95_seconds`, and `p99_seconds` durations.

## Set up checks {#set-up-checks}

### chainctl checks validate {#chainctl-checks-validate}

Finds problems in your configuration without running anything, the way Chainguard Checks reads it for a pull request, with the differences described in [Validate your configuration offline](/chainguard/checks/run-checks/#validate-your-configuration-offline). That section also shows the command's output.

```
chainctl checks validate [PATH]
```

`PATH` is a repository's root directory, a configuration file under its `.chainguard/` directory, or a standalone configuration file. For a file under `.chainguard/`, the command validates its repository's whole configuration. Without `PATH`, the command validates the repository that the current directory is in.

For example, to validate another repository's configuration:

```shell
chainctl checks validate ../app
```

The command exits with `1` when the configuration has a problem that Chainguard Checks would refuse. Warnings, such as for a key that Chainguard Checks ignores, don't change the exit code. With `-o json`, the command prints one object with the repository's `root`, the problems that kept it from reading the configuration in `diagnostics`, and a `workflows` list. Each workflow has its `workflow` name, its `path`, its `refusals` and `warnings`, problems with `needs` in `graph`, and `ok`. The object's own `ok` is `true` when the whole configuration is valid.

### chainctl checks explain {#chainctl-checks-explain}

Prints each check as Chainguard Checks reads it for a pull request, with its environment, trigger, steps, and resource class, without running anything.

```
chainctl checks explain [DIR] [--raw]
```

`DIR` is the repository's root directory. Without it, the command reads the repository that the current directory is in.

| Flag | Description |
| ---- | ----------- |
| `--raw` | Prints check names, commands, and other text from your repository as they are, including escape sequences, even on a terminal. |

If Chainguard Checks would refuse the configuration, the command prints each problem with its file and position, and exits with `1`. With `-o json`, it prints the resolved configuration, or the problems when it's refused.

### chainctl checks migrate {#chainctl-checks-migrate}

Drafts a `.chainguard/ci/migrated.yaml` file from your repository's GitHub Actions workflows that run on `pull_request`. Refer to [Migrate from GitHub Actions to Chainguard Checks](/chainguard/checks/migrate-from-github-actions/) for how to review the draft.

```
chainctl checks migrate [PATH] [--dry]
```

`PATH` is a local clone whose `origin` remote is on github.com, the current directory by default. The `--dry` flag drafts the file and prints it, followed by a list of what the draft carried over, flagged, and ignored, without running anything.

Without `--dry`, the command also tests the draft by running its checks in your organization, up to six times. These runs need a role, as described in [Access and organization](#access-and-organization), and use your organization's Checks allowance like any other run. In the first run, each check that has no `egress` list can reach any host by name, so that the command can draft its list. Chainguard Checks still refuses connections to IP addresses, private ranges, and metadata endpoints. During the beta, use `--dry` to avoid these runs.

For example, to write the draft to its file:

```shell
mkdir -p .chainguard/ci
chainctl checks migrate --dry -o json | jq -r .document > .chainguard/ci/migrated.yaml
```

With `-o json`, the command prints one object with the `repository`, `revision`, the draft's `path`, the number of `jobs` it drafted, the draft itself in `document`, and the `ledger` of what it carried over, flagged, and ignored.

### chainctl checks accept-terms {#chainctl-checks-accept-terms}

Accepts the terms that Chainguard Checks is offered under for your organization: the [Code Analysis Terms](https://www.chainguard.dev/legal/code-analysis-terms) and the [Master Service and License Agreement](https://www.chainguard.dev/legal/master-service-and-license-agreement). Someone with the `owner` or `limited_owner` role runs it once. The `chainctl develop init` command also asks you to accept these terms, as described in [Sign up with chainctl develop init](/get-started/checks-and-workspaces/set-up/#sign-up-with-chainctl-develop-init).

```
chainctl checks accept-terms [--parent ORGANIZATION] [--yes]
```

| Flag | Description |
| ---- | ----------- |
| `--parent` | The organization to accept the terms for. Without it, the command uses the `default.group` value in your `chainctl` configuration, or asks you to choose. |
| `--yes` | Accepts the terms without asking, for use without an interactive terminal. By adding it, you agree to the statement in the command's help, which it also prints. |

For example:

```shell
chainctl checks accept-terms --parent $ORGANIZATION
```

Running the command again after the organization accepts the terms changes nothing.
