---
title: "Migrate from GitHub Actions to Chainguard Checks"
linktitle: "Migrate from GitHub Actions"
description: "Convert GitHub Actions pull request workflows to a Chainguard Checks .chainguard/ci.yaml file, with a mapping of common GitHub Actions keys."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-08T00:00:00+00:00
draft: false
tags: ["Chainguard Checks", "Migration", "GitHub"]
images: []
menu:
  docs:
    parent: "checks"
toc: true
weight: 60
---

If your repository runs its pull request checks with GitHub Actions, you can move them to Chainguard Checks one workflow at a time. Chainguard Checks and GitHub Actions can run on the same pull requests, so you can compare their results before you remove a workflow.

During the beta, convert workflows by hand. The `chainctl checks migrate` command drafts a configuration from your workflows, but in a format that pull requests don't accept yet.

## How the models differ

A GitHub Actions job starts on a general-purpose runner image, checks out your code, and installs its tools with setup actions before running its commands. In Chainguard Checks, a check starts in a minimal VM with your code already in `/work`, installs the packages you list, and runs its commands. The following table summarizes the differences:

| Area | GitHub Actions | Chainguard Checks |
| ---- | -------------- | ----------------- |
| Actions | Steps can use actions with `uses:`. | There are no actions. List each tool's package and run it directly. You don't need `actions/checkout`, because your code is already in the VM. |
| Preinstalled tools | The runner image includes many tools. | The VM includes BusyBox, GNU tar, and the packages you list. List every tool a check uses, including `git`, `bash`, and `make`. |
| Network | Jobs can reach the internet. | A check has no network access unless it lists hosts under `network.egress`, such as your package registry. |
| Secrets | Jobs read secrets from the `secrets` context. | There's no `secrets` context. Most checks don't need credentials. A check that must authenticate to Google Cloud or Chainguard can use a workload identity, as described in [Credentials](/chainguard/checks/configuration/#credentials). |

## Key mapping

The following table maps common GitHub Actions keys to their Chainguard Checks equivalents:

| GitHub Actions | Chainguard Checks |
| -------------- | ----------------- |
| `on: pull_request` | The default. A check runs on pull requests unless you set `trigger`. |
| `on: push` to the default branch | `trigger: postsubmit` |
| `on: pull_request: paths:` | `when: changed:` |
| `if:` | `when: expr:` with a CEL expression |
| `workflow_dispatch`, or a job that a label starts | `when: {requested: true}`, run with a `ci/run:<check>` label |
| `continue-on-error: true`, or a job that isn't required | `advisory: true` |
| `jobs.<job_id>` | `checks.<name>` |
| `runs-on` | `resources` |
| `steps[*].run` | `steps[*].cmd` or `steps[*].script` |
| `steps[*].uses` | Not supported. List the tool's package and run it. |
| `env` | `vars` |
| `needs` | `needs`, for checks in the same file |
| `timeout-minutes` | `timeout`, as a duration such as `15m` |
| `strategy.matrix` | `foreach` |
| `defaults.run.working-directory` | `workdir` |
| `on: schedule` | Not supported. |

Refer to the [configuration reference](/chainguard/checks/configuration/) for each Chainguard Checks key.

## Example

The following GitHub Actions workflow runs Go tests on pull requests that change Go files:

```yaml {title=".github/workflows/test.yaml"}
name: test
on:
  pull_request:
    paths: ["**/*.go", "go.mod", "go.sum"]
jobs:
  test:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-go@v5
        with:
          go-version: "1.24"
      - run: go test ./...
        env:
          CGO_ENABLED: "0"
```

The equivalent `.chainguard/ci.yaml` file installs Go 1.24 as a package instead of using `actions/setup-go` and drops `actions/checkout`:

```yaml {title=".chainguard/ci.yaml"}
version: 1
environment:
  packages: [go-1.24]
checks:
  test:
    cmd: go test ./...
    vars:
      CGO_ENABLED: "0"
    timeout: 15m
    when:
      changed: ["**/*.go", "go.mod", "go.sum"]
    network:
      egress: [proxy.golang.org, sum.golang.org]
```

The `network` key lets the check download modules, which the GitHub Actions runner could do without asking. To find the hosts a check needs, run it and look for connection errors in its log.

## Switch over

To move a workflow to Chainguard Checks without a gap in coverage, follow these steps:

1. Add the equivalent checks to `.chainguard/ci.yaml` in a pull request, and keep the GitHub Actions workflow.
2. Compare the results of both on that pull request and the ones after it.
3. When the results match, add **Chainguard Checks (presubmit)** as a required status check, as described in [Require checks before merging](/chainguard/checks/github/#require-checks-before-merging).
4. Remove the GitHub Actions workflow, and remove its jobs from your required status checks.
