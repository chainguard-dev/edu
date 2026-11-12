---
title: "Tutorial: Fix a failing check with Claude Code in a Chainguard Workspaces session"
date: 2026-11-12T15:30:50+00:00
lastmod: 2026-11-12T16:11:13+00:00
linktitle: "Tutorial: Fix a failing check"
description: "Walk the whole loop of Chainguard Checks and Chainguard Workspaces: let Claude Code change a small Go project in a session, run the checks with run-ci, open a pull request, read a failing check with chainctl checks failures, and have Claude Code fix it."
type: "article"
draft: false
tags: ["Chainguard Checks", "Chainguard Workspaces", "Getting Started", "Procedural"]
images: []
weight: 15
toc: true
---

Chainguard Checks and Chainguard Workspaces are built to work together: a coding agent changes your code in a Workspaces session, `run-ci` runs your checks against the change before you push, and Chainguard Checks runs the same checks on the pull request. When a check fails, the agent reads why from the session and fixes it.

In this tutorial, you walk that loop once with a small Go project. You open a session, let Claude Code add a function, check the change with `run-ci`, and open a pull request whose checks pass. Then you break a test on purpose, push without running `run-ci`, read the failure from the session with `chainctl checks failures`, and let Claude Code fix it.

{{< beta feature="Each product" >}}

## Before you begin {#before-you-begin}

You need the following:

- A Chainguard organization with Chainguard Checks and Chainguard Workspaces turned on, `chainctl` 0.2.391 or later, and the Chainguard App installed on the GitHub account that owns your repository. Refer to [Set up Chainguard Checks and Chainguard Workspaces](/get-started/checks-and-workspaces/set-up/).
- A new, empty repository on github.com that you can push to, such as `acme/hello`, and a clone of it on your laptop. If you installed the Chainguard App on selected repositories only, add this one.
- A Claude account for Claude Code. If Chainguard doesn't hold a Claude login for you, `chainctl` offers to set one up when you open the session, as described in [Get started with Chainguard Workspaces](/chainguard/workspaces/getting-started/#step-2-open-a-session).

You don't need Go on your laptop. The checks and the session install it.

In the commands on this page, replace `$ORGANIZATION` with the name of your Chainguard organization. If you belong to only one organization, you can omit `--parent`.

## Step 1: Create the project {#step-1-create-the-project}

In your clone, create a Go module with one function and its test. Create a `go.mod` file:

```text {title="go.mod"}
module github.com/acme/hello

go 1.24
```

Create a `hello.go` file:

```go {title="hello.go"}
// Package hello builds greetings.
package hello

// Greeting returns a greeting for name.
func Greeting(name string) string {
    return "Hello, " + name + "!"
}
```

Create a `hello_test.go` file:

```go {title="hello_test.go"}
package hello

import "testing"

func TestGreeting(t *testing.T) {
    if got := Greeting("Ada"); got != "Hello, Ada!" {
        t.Errorf("Greeting(\"Ada\") = %q, want %q", got, "Hello, Ada!")
    }
}
```

Then create the file that defines your checks:

```yaml {title=".chainguard/ci.yaml"}
version: 1
environment:
  packages: [go, git, claude]
checks:
  vet:
    cmd: go vet ./...
  test:
    cmd: go test ./...
```

The file defines two checks, `vet` and `test`, which Chainguard Checks runs on every pull request. A Workspaces session uses the same `environment`, so its `packages` give the session Go, Git, and Claude Code. The project has no dependencies, so neither check needs network access.

Commit the files and push them to your repository's default branch:

```shell
git add .
git commit -m "Add the hello project"
git push origin main
```

## Step 2: Open a session {#step-2-open-a-session}

Create a branch for your change, then open a session from your clone:

```shell
git switch -c add-farewell
chainctl develop --parent $ORGANIZATION
```

`chainctl` creates a session, uploads your branch, and opens a shell in the session. Its output includes lines similar to the following:

```output
Creating a session for . (checkout of https://github.com/acme/hello at 1efc76b9f6c4) from its own .chainguard/ci.yaml, as Ada Lovelace <ada@example.com> …
Created acme/hello/quiet-harbor (fa101f50)
  claude: served from your Claude login held by Chainguard (ada@example.com), attached or not
Syncing . as a delta over https://github.com/acme/hello@ceab2476db62 …
Attached to acme/hello/quiet-harbor [running] · github, claude, cgr.dev · Ctrl+] detach  ~? help
```

The session's environment comes from your `.chainguard/ci.yaml` file, and the `claude:` line names the Claude login that Claude Code uses in the session. Your files are in `/work`, on your `add-farewell` branch.

## Step 3: Ask Claude Code for a change {#step-3-ask-claude-code-for-a-change}

In the session, start Claude Code:

```shell
claude
```

Ask it for a small change, such as the following:

```
Add a Farewell function to hello.go that returns "Goodbye, <name>!", and a test for it in hello_test.go, in the same style as Greeting and its test.
```

Claude Code asks before it runs commands or edits files, depending on its [permission mode](/chainguard/workspaces/coding-agents/#choose-a-permission-mode). Its edits vary from run to run, but the change looks similar to the following:

```go
// Farewell returns a farewell for name.
func Farewell(name string) string {
    return "Goodbye, " + name + "!"
}
```

```go
func TestFarewell(t *testing.T) {
    if got := Farewell("Ada"); got != "Goodbye, Ada!" {
        t.Errorf("Farewell(\"Ada\") = %q, want %q", got, "Goodbye, Ada!")
    }
}
```

When Claude Code finishes, exit it with `/exit`.

## Step 4: Check the change and open a pull request {#step-4-check-the-change-and-open-a-pull-request}

Run your checks against the change in the session:

```shell
run-ci
```

The `run-ci` command runs each check in `.chainguard/ci.yaml` against the files in `/work`, including changes you haven't committed. The output looks similar to the following:

```output
run-ci: checks vet, test (advisory: the gate runs the verdict on push)
── vet[0]: go vet ./...
── vet[0]: exit 0 (180ms)
── test[0]: go test ./...
ok      github.com/acme/hello    (cached)
── test[0]: exit 0 (177ms)
PASS in 521ms
```

Commit the change and push your branch:

```shell
git add hello.go hello_test.go
git commit -m "Add Farewell"
git push origin add-farewell
```

The Chainguard App adds the credential for the push, so you don't sign in to GitHub in the session. The push prints a link for creating a pull request on GitHub. Open the link in your browser, and create the pull request.

Chainguard Checks runs `vet` and `test` on the pull request, each in a fresh VM. When they finish, the **Chainguard Checks (presubmit)** check on the pull request reads **All 2 check(s) passed**. For what else the pull request shows, refer to [How results appear](/chainguard/checks/github/#how-results-appear).

## Step 5: Make a check fail {#step-5-make-a-check-fail}

To see what happens when a check fails, change `Greeting` so that its test fails, and push the change without running `run-ci`. In the session, change the `!` in `Greeting` to a period:

```shell
sed -i 's/"Hello, " + name + "!"/"Hello, " + name + "."/' hello.go
git commit -am "Change the greeting punctuation"
git push origin add-farewell
```

The `sed` command matches only `Greeting`'s string, not `Farewell`'s. The push updates the pull request, and Chainguard Checks runs the checks again. This time, **Chainguard Checks (presubmit)** reads **1 of 2 check(s) failed**, and names `ci / test` as the check that failed.

## Step 6: Read the failure and fix it {#step-6-read-the-failure-and-fix-it}

In the session, read why the check failed:

```shell
chainctl checks failures
```

The command finds the pull request's latest run for the commit you're on, and prints each failed check with the end of its output:

```output
Run: instances/<organization-id>/runs/<run-id>
Status: failed; 1 failed, 1 passed, 0 did not run

=== check "test" in workflow "ci": failed (exit 1), attempt 1 ===
step 0 "step 0": failed (exit 1)
  command: go test ./...
  working directory: /work
  process go: exit 1 (guest-attested; the last 148 B of its output, log bytes 390-538)
  > --- FAIL: TestGreeting (0.00s)
  >     hello_test.go:7: Greeting("Ada") = "Hello, Ada.", want "Hello, Ada!"
  > FAIL
  > FAIL    github.com/acme/hello    0.001s
  > FAIL
```

The command works while you're attached to the session, because the session gets its Chainguard credential from your attached terminal. For its options, refer to [Inspect pull request runs](/chainguard/checks/inspect-and-run-checks/#inspect-pull-request-runs).

Claude Code can read the same output. Start it again with `claude`, and ask it to fix the failure:

```
The checks on my pull request failed. Run chainctl checks failures to see why, then fix the code so the checks pass. Do not change the tests.
```

Claude Code runs `chainctl checks failures`, finds the test that failed, and changes the period in `Greeting` back to `!`. It may run `run-ci` to confirm the fix, and point out that the fix undoes your last commit.

## Step 7: Push the fix {#step-7-push-the-fix}

Run the checks in the session, then commit and push the fix:

```shell
run-ci
git commit -am "Restore the greeting punctuation"
git push origin add-farewell
```

Chainguard Checks runs the checks again, and **Chainguard Checks (presubmit)** reads **All 2 check(s) passed**.

## Step 8: Clean up {#step-8-clean-up}

To leave the session, press `Ctrl+]` to open the session menu, then press `Enter` or `d` to detach. On your laptop, find the session's name, and delete the session:

```shell
chainctl develop list --parent $ORGANIZATION
chainctl develop delete acme/hello/quiet-harbor --parent $ORGANIZATION
```

The `delete` command asks you to confirm, then destroys the session's VM and its snapshot. Anything you didn't push is gone. Then close the pull request on GitHub, or merge it, and delete the repository if you don't need it.

## Next steps {#next-steps}

- [Run checks before you push](/chainguard/checks/run-checks/): what `run-ci` covers, and how it differs from a pull request run.
- [Inspect and run checks with chainctl](/chainguard/checks/inspect-and-run-checks/): read runs, logs, and history from your terminal or an agent.
- [Use Claude Code in a Chainguard Workspaces session](/chainguard/workspaces/coding-agents/): permission modes, keeping Claude Code working while you're away, and running agents in parallel.
- [Chainguard Checks configuration reference](/chainguard/checks/configuration/): write checks for your own project.
