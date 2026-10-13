---
title: "Run checks before you push with Chainguard Workspaces"
linktitle: "Run checks before you push"
description: "Run your repository's checks against uncommitted changes in a Chainguard Workspaces session, and validate your Chainguard Checks configuration offline before you push."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-13T00:00:00+00:00
draft: false
tags: ["Chainguard Checks", "chainctl", "Procedural"]
images: []
menu:
  docs:
    parent: "checks"
toc: true
weight: 50
---

Waiting for a pull request's checks to find a mistake is slow, especially for a coding agent that has to push, wait, and read the results before it can try again. With [Chainguard Workspaces](/chainguard/workspaces/overview/), you can run your repository's checks against your working tree, uncommitted changes included, before you push. This page explains how, and how to find mistakes in your configuration without running anything. To run checks on a pushed commit without a pull request, or to read results and your checks' history from your terminal, refer to [Inspect and run checks with chainctl](/chainguard/checks/inspect-and-run-checks/).

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

- It runs the checks that have commands, in the order they appear in your configuration, and stops at the first check that fails, including an advisory check.
- It skips checks that need something only a pull request run provides: a [workload identity](/chainguard/checks/configuration/#credentials), `services` in the check's environment, or `inputs`. It prints a line for each, such as `run-ci: skipped deploy: declares identity gcp-prod, which only CI provides`. Those checks run only on the pull request, so a pass from `run-ci` doesn't cover them. If you name a skipped check, as in `run-ci deploy`, or if it skips every check, `run-ci` exits with `2`.
- It runs checks as the session's user, not as each check's `user`. Sessions run as `root` unless their environment comes from a check with a different `user`, such as a session you open with `chainctl develop --check`. In a `root` session, every check runs as `root`. A session that runs as another user runs only the checks with that `user`, and skips the rest the same way.
- It ignores `needs`, `when` conditions, `trigger`, and `timeout`, so it also runs checks that a pull request would skip. A check with `foreach` runs once for each variation, and each one appears in the output as `<check>/<variation>`, such as `test/api`.
- It runs each check in the session as it is, not in a fresh VM per check. Packages you installed in the session are available, and a check's own package list and network access don't apply.
- It uses the session's size and CPU architecture, not each check's `resources`. A session runs on x86-64 unless its resource class ends in `-arm64`, as described in [Resources](/chainguard/workspaces/session-environment/#resources). On pull requests, a class without a suffix usually runs on arm64.

Because of these differences, a pass from `run-ci` predicts that the pull request's checks will pass, but only the pull request's run in fresh VMs decides what GitHub shows.

The `run-ci` command works while something is attached to the session, such as your terminal. It also works after you detach, if you keep the session running with a **Detach — keep running** option or `--keep`, as described in [Keep a session running while you're away](/chainguard/workspaces/manage-sessions/#keep-a-session-running-while-youre-away). Running checks doesn't keep a session from parking, so if the session parks while `run-ci` runs, the run stops and `run-ci` exits with `2`.

## Run checks in a session from your laptop

To run a session's checks without attaching to it, use `chainctl develop check` on your laptop with the session's name or short ID. If the session is parked, `chainctl` resumes it first. Replace `$SESSION` with the session's name or short ID, and `$ORGANIZATION` with the name of your Chainguard organization:

```shell
chainctl develop check $SESSION --parent $ORGANIZATION
```

To run a single check, add `--check` with its name:

```shell
chainctl develop check $SESSION --check test --parent $ORGANIZATION
```

The command uses the same runner as `run-ci` and streams each step's output. It skips the same checks as `run-ci`, and prints a line for each, such as `Skipped deploy: declares identity gcp-prod, which only CI provides`. It exits with `0` when the checks pass, or `1` when a check fails or the checks can't run, including when you name a skipped check with `--check`. To print the result as JSON, add `--output json`. The JSON lists the checks it skipped under `skipped`.

If you detached from the session and kept it running, `chainctl develop check` might fail with a message that says `the guest is held by another controller`. Run the command again, or attach to the session and run `run-ci` in it.

## Validate your configuration offline

To find mistakes in your configuration without running anything, run `chainctl checks validate` anywhere in your repository's checkout:

```shell
chainctl checks validate
```

With no argument, the command finds your repository's root. You can also pass the path of a repository or of a configuration file. With `chainctl` 0.2.379 or earlier, pass the repository's directory instead, such as `.` from the repository's root. For a valid configuration, the command prints each workflow it found:

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

For a pull request, Chainguard Checks reads only the files directly in your repository's root `.chainguard/` directory and the files under `.chainguard/ci/`. In the directory layout, `validate` and `explain` read the same files. In the single-file layout, they also read `.chainguard/` directories below the root, such as `testdata/.chainguard/`, and folders inside `.chainguard/`. As a result, they can list a workflow that pull requests never run, or fail on a file that pull requests ignore. To avoid this, move those files out of `.chainguard/` directories, or use the [directory layout](/chainguard/checks/configuration/#file-layouts).
