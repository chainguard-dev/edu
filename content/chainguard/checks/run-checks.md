---
title: "Run checks before you push with Chainguard Workspaces"
linktitle: "Run checks before you push"
description: "Run your repository's checks against uncommitted changes in a Chainguard Workspaces session, and validate your Chainguard Checks configuration offline with chainctl."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-08T00:00:00+00:00
draft: false
tags: ["Chainguard Checks", "chainctl", "Procedural"]
images: []
menu:
  docs:
    parent: "checks"
toc: true
weight: 50
---

Waiting for a pull request's checks to find a mistake is slow, especially for a coding agent that has to push, wait, and read the results before it can try again. With [Chainguard Workspaces](/chainguard/workspaces/overview/), you can run your repository's checks against your working tree, uncommitted changes included, before you push. This page explains how, and how to find mistakes in your configuration without running anything.

## Run checks in a Workspaces session

Every Workspaces session has a `run-ci` command that runs the checks your repository defines against the working tree in `/work`. To run every check, run `run-ci` with no arguments in the session:

```shell
run-ci
```

The command prints each step's output as it runs, followed by a result line. For a repository with `vet` and `test` checks, the output looks similar to the following:

```
run-ci: checks vet, test (advisory: the gate runs the verdict on push)
── vet[0]: go vet ./...
── vet[0]: exit 0 (9.281s)
── test[0]: go test ./...
ok      github.com/acme/app    0.004s
── test[0]: exit 0 (3.843s)
PASS in 13.131s
```

Each `──` line names a check and the number of the step within it, counting from `0`, followed by the step's command or its exit code and duration. The first line is a reminder that the pull request's run, not `run-ci`, decides what GitHub shows. When a check declares a different environment from the session's, `run-ci` also prints a note about it.

To run a single check, pass its name:

```shell
run-ci test
```

The `run-ci` command exits with one of the following codes, so scripts and agents can act on the result:

| Exit code | Meaning |
| --------- | ------- |
| `0` | Every check passed. |
| `1` | A check failed. The last line names the check and the number of the step that failed. |
| `2` | The checks couldn't run. The last line says why. |

### How run-ci differs from a pull request run

The `run-ci` command reads your checks from the session's working tree, so it uses your latest edits to the configuration too. It differs from a pull request run in the following ways:

- It runs every check that has commands, in the order they appear in your configuration, and stops at the first check that fails, including an advisory check.
- It ignores `needs`, `when` conditions, `trigger`, and `timeout`, so it also runs checks that a pull request would skip.
- It runs each check in the session as it is, not in a fresh VM per check. Packages you installed in the session are available, and a check's own package list and network access don't apply.
- Sessions run on x86-64, while pull request checks usually run on arm64 unless their resource class pins the architecture.

Because of these differences, a pass from `run-ci` predicts that the pull request's checks will pass, but only the pull request's run in fresh VMs decides what GitHub shows.

The `run-ci` command works only while something is attached to the session, such as your terminal.

## Run checks in a session from your laptop

To run a session's checks without attaching to it, use `chainctl develop check` on your laptop with the session's name or short ID. If the session is parked, `chainctl` resumes it first. Replace `$SESSION` with the session's name or short ID, and `$ORGANIZATION` with the name of your Chainguard organization:

```shell
chainctl develop check $SESSION --parent $ORGANIZATION
```

To run a single check, add `--check` with its name:

```shell
chainctl develop check $SESSION --check test --parent $ORGANIZATION
```

The command uses the same runner as `run-ci` and streams each step's output. It exits with `0` when the checks pass, or `1` when a check fails or the checks can't run.

## Validate your configuration offline

To find mistakes in your configuration without running anything, run `chainctl checks validate` from your repository's directory:

```shell
chainctl checks validate .
```

Always pass the directory, `.` in this example. The command reads your configuration the same way Chainguard Checks reads it for a pull request. For a valid configuration, it prints each workflow it found:

```
workflow ci (.chainguard/ci.yaml)
ok: the document lowers
```

For a configuration with problems, it prints each problem with its file, line, and column, and exits with a non-zero status. For example, a string `cmd` with a pipe in it produces an error that suggests using a shell:

```
.chainguard/ci.yaml:6:10: check t: cmd "go test ./... | tee out": unquoted shell metacharacter '|': a string `cmd:` is safe-split with no shell behind it (no pipes, redirects, globs, or expansion) — quote the character, or write `cmd: [sh, -c, "..."]` to opt into a shell explicitly
```

Because `validate` needs no network access or Chainguard account, you can run it in a git pre-commit hook.

To see how Chainguard Checks interprets your configuration, run `chainctl checks explain`. It prints each check with its environment, trigger, and commands, plus its conditions, network access, and timeout when they're set:

```shell
chainctl checks explain
```

Run `explain` when a check doesn't behave as you expect, such as running when you thought a condition would skip it.

## Inspect pull request runs

During the beta, read a pull request's results on GitHub, as described in [How results appear](/chainguard/checks/github/#how-results-appear). The `chainctl checks` commands for inspecting runs, such as `chainctl checks status` and `chainctl checks logs`, don't show pull request runs yet.
