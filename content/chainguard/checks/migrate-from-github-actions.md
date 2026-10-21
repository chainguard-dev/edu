---
title: "Migrate from GitHub Actions to Chainguard Checks"
linktitle: "Migrate from GitHub Actions"
description: "Draft a Chainguard Checks configuration from GitHub Actions pull request workflows with chainctl, or convert workflows by hand with a mapping of common GitHub Actions keys."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-20T14:50:35+00:00
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

You can convert workflows by hand, or start from a draft that the `chainctl checks migrate` command writes for you.

If you'd rather keep your workflows on GitHub Actions, [Chainguard Actions](/chainguard/actions/overview/) replaces the actions they use with hardened equivalents, and Guardener's [Hardened Actions](/chainguard/guardener/github/actions-security/) feature can migrate them for you.

## Draft a configuration with chainctl

The `chainctl checks migrate --dry` command drafts a configuration from your GitHub Actions workflows without running anything. Run it from the root of a local clone of your repository whose `origin` remote is on github.com:

```shell
chainctl checks migrate --dry
```

The command reads each workflow that runs on `pull_request` and prints a draft `.chainguard/ci/migrated.yaml` file, followed by a list of what it carried over, flagged, and ignored. To write the draft to its file, run the following commands:

```shell
mkdir -p .chainguard/ci
chainctl checks migrate --dry -o json | jq -r .document > .chainguard/ci/migrated.yaml
```

The draft has one check for each job it can carry over, and a separate check for each combination of a static matrix of up to 8 combinations. A job whose matrix uses `include` or an expression, or has more than 8 combinations, isn't carried over. The list after the draft flags it, so convert it by hand. The draft's checks appear on GitHub as `presubmit / migrated / <check>`.

The draft uses the [directory layout](/chainguard/checks/configuration/#file-layouts), and a repository can't use both layouts. If your repository already has a `.chainguard/ci.yaml` file, move its checks into a file in `.chainguard/ci/`, and its environment to `.chainguard/ci/env/default.yaml`, before you add the draft.

Review the draft before you commit it:

- Add the packages each check needs. The draft lists packages for setup actions, such as `actions/setup-go`, but not for tools that the GitHub Actions runner image includes, such as `git` and `make`.
- Add the hosts each check needs under `network.egress`. The draft gives checks no network access. To find the hosts, refer to [Find the hosts a check needs](#find-the-hosts-a-check-needs).
- For each check that needs x86-64, set `resources` to a class that pins it, such as the built-in `medium-amd64`. The draft ignores `runs-on`, so its checks usually run on arm64.
- Read each `# migrator:` comment. Each one marks something the draft couldn't carry over, such as a step that uses a third-party action, a step with a `${{ }}` expression, a service container, or a `paths` filter. Convert each one by hand.

Then run `chainctl checks validate` to check the result. The rest of this page explains how to convert what the draft leaves out, including workflows that run on other events, such as `push`.

## How the models differ

A GitHub Actions job starts on a general-purpose runner image, checks out your code, and installs its tools with setup actions before running its commands. In Chainguard Checks, a check starts in a minimal VM with your code already in `/work`, installs the packages you list, and runs its commands. The following table summarizes the differences:

| Area | GitHub Actions | Chainguard Checks |
| ---- | -------------- | ----------------- |
| Actions | Steps can use actions with `uses:`. | There are no actions. List each tool's package and run it directly. You don't need `actions/checkout`, because `/work` already holds your repository's tracked files and history at the commit under test, but not its submodules or Git LFS content. |
| Preinstalled tools | The runner image includes many tools. | The VM includes BusyBox, GNU tar, and the packages you list. List every tool a check uses, including `git`, `bash`, and `make`. |
| Network | Jobs can reach the internet. | A check has no network access unless it lists hosts under `network.egress`, such as your package registry. |
| Shell | A `run` step uses `bash -e`, or `bash -eo pipefail` with `shell: bash`. | A `script` runs with BusyBox `sh -e`, or with `bash -e` if you list the `bash` package and set `shell: bash`. Neither sets `pipefail`, so for a step that had `shell: bash`, start its script with `set -o pipefail`. The draft keeps `pipefail` for these steps. Refer to [The script key](/chainguard/checks/configuration/#the-script-key). |
| Caches | Jobs save and restore caches with actions, such as `actions/cache`. | A check starts with no cache. If the `trust` section of `.chainguard/ci/identities.yaml` on your default branch defines a cache pool, a Go check can reuse build output from earlier runs. |
| Run length | A job can run for up to 6 hours. | A whole run can take up to two hours, and checks still running at that point fail. Split long jobs into several checks, which run in parallel. |
| Background processes | A process that a step starts in the background keeps running in the job's later steps. | When a step ends, Chainguard Checks stops every process that the step left running in the background. To keep a process, such as a database, running for a check's commands, use a [service](/chainguard/checks/variations-services-caches/#services). Refer to [How commands run](/chainguard/checks/configuration/#how-commands-run). |
| Secrets | Jobs read secrets from the `secrets` context, and get a `GITHUB_TOKEN`. | There's no `secrets` context. During the beta, a check gets no GitHub token, so it can't fetch your private GitHub repositories, such as private Go modules. A check that must authenticate to Google Cloud or Chainguard can use a workload identity, as described in [Credentials](/chainguard/checks/configuration/#credentials). |

## Key mapping

The following table maps common GitHub Actions keys and actions to their Chainguard Checks equivalents:

| GitHub Actions | Chainguard Checks |
| -------------- | ----------------- |
| `on: pull_request` | The default. A check runs on pull requests unless you set `trigger`. |
| `on: push` to the default branch | `trigger: postsubmit` |
| `on: pull_request: paths:` | `when: changed:`. A `**` matches any number of directories only as a whole path segment, so write `**.go` as `**/*.go`. A pattern that starts with `!` has no equivalent. Refer to [Run when files change](/chainguard/checks/configuration/#run-when-files-change). |
| `on: pull_request: paths-ignore:` | No equivalent. List the paths that should run the check under `when: changed:` instead. |
| `if:` | `when: expr:` with a CEL expression |
| `workflow_dispatch`, or a job that a label starts | `when: {requested: true}`, run with a `ci/run:<check>` label |
| `continue-on-error: true`, or a job that isn't required | `advisory: true` |
| `jobs.<job_id>` | `checks.<name>` |
| `runs-on` | `resources`. A built-in class without a suffix usually runs on arm64, while `ubuntu-latest` is x86-64, so use an `-amd64` class, such as `medium-amd64`, for a job that needs x86-64. If your repository defines its own classes in `.chainguard/ci/resources.yaml`, the built-in classes aren't available, and only a class with a `platform` pins the architecture. Refer to [Resources](/chainguard/checks/configuration/#resources). |
| `steps[*].run` | `steps[*].cmd` or `steps[*].script`. A step takes only `id`, `name`, `cmd`, `script`, and `shell`, so step-level `env`, `if`, and `working-directory` are refused. |
| `steps[*].uses` | Not supported. List the tool's package and run it. |
| `actions/checkout` with `repository` | `inputs` with `git`, for a public repository on github.com. Refer to [Check out another repository](/chainguard/checks/variations-services-caches/#check-out-another-repository). |
| `actions/checkout` with `submodules` or `lfs` | No equivalent. Submodule directories are empty, and Git LFS files hold their pointer files. |
| `actions/upload-artifact` and `actions/download-artifact` | `outputs` on the check that writes the files, and `inputs` with `from` on a check in the same file that reads them. Refer to [Pass files between checks](/chainguard/checks/variations-services-caches/#pass-files-between-checks). A run keeps no files that you can download. |
| `actions/cache`, or the caching in `actions/setup-go` | For the Go build cache, `environment.caches: {gobuild: {}}`, with a cache pool in the `trust` section of `.chainguard/ci/identities.yaml` on your default branch. The check runs as `root` or as `build`, as described in [Build caches](/chainguard/checks/variations-services-caches/#build-caches). Other cache types have no effect during the beta. |
| `jobs.<job_id>.services` | `environment.services`. A service runs in the check's VM from packages that you list, not in a container. Refer to [Services](/chainguard/checks/variations-services-caches/#services). To run a container image instead, run Docker as a service, as described in [Run Docker](/chainguard/checks/variations-services-caches/#run-docker). |
| `env` | `vars` |
| `needs` | `needs`, for checks in the same file |
| `timeout-minutes` | `timeout`, as a duration such as `15m` |
| `strategy.matrix` | `foreach`. Chainguard Checks doesn't expand a matrix, so write one entry for each combination, and replace each `${{ matrix.<key> }}` with a variable that the entry sets in `vars`, such as `$GOARCH` in a `script`. An entry can't change the check's packages, so for a matrix of tool versions, write a separate check with its own environment for each version, as the draft does. Refer to [Run a check once per variation](/chainguard/checks/variations-services-caches/#run-a-check-once-per-variation). |
| `strategy.max-parallel` | `parallelism` |
| `defaults.run.working-directory` | `workdir` |
| `$GITHUB_STEP_SUMMARY` | Not set, so a command that writes to it fails. Instead, print Markdown between a `::sandbox-summary::` line and an `::end-sandbox-summary::` line, and the check's output on GitHub shows it before the log. Refer to [Add a Markdown summary](/chainguard/checks/configuration/#add-a-markdown-summary). |
| `on: schedule` | Not supported. |
| `on: merge_group` | Not supported. Chainguard Checks doesn't run on merge queues, so don't require **Chainguard Checks (presubmit)** on a branch that uses one. Refer to [Require checks before merging](/chainguard/checks/github/#require-checks-before-merging). |

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

The `network` key lets the check download modules. The workflow doesn't list these hosts, because a GitHub Actions job can reach any host. To find the hosts a check needs, refer to [Find the hosts a check needs](#find-the-hosts-a-check-needs).

By default, `actions/setup-go` caches downloaded modules and build output between runs. This file uses no cache, so each run downloads its modules and builds from scratch. To reuse Go build output between runs, add the `gobuild` cache, as described in [Caches](/chainguard/checks/variations-services-caches/#caches). During the beta, Chainguard Checks doesn't cache modules, so keep the `network` hosts. With the cache, `go test` still runs every test instead of reusing earlier results.

## Find the hosts a check needs {#find-the-hosts-a-check-needs}

The run page that a check's **Details** link opens lists each host the check tried to reach, and suggests an `egress` list built from the hosts it connected to. The suggestion includes only connections that the check's `egress` allowed, so to see every host a check uses, let it reach any host for one run:

1. In a pull request whose code you trust, set the check's `network.egress` to `["*"]`. With `*`, the check's commands can reach any public host.
2. When the check finishes, open its **Network activity** on the run page, as described in [A check can't reach a host](/chainguard/checks/troubleshooting/#a-check-cant-reach-a-host).
3. Review the hosts listed after **Suggested allowlist (review before applying)**, replace `*` with them, and push the change.

The suggestion covers only that run. It leaves out connections to an IP address that the check didn't look up by name, and hosts that the check reaches only on other paths, such as retries, fallback mirrors, or code that the run didn't exercise.

To open the run page, you need a role in your Chainguard organization, as described in [The Details link or a chainctl checks command says you don't have access](/chainguard/checks/troubleshooting/#the-details-link-or-a-chainctl-checks-command-says-you-dont-have-access). Without one, list the hosts you expect, run the check, and look in its log for connection errors.

## Switch over

To move a workflow to Chainguard Checks without a gap in coverage, follow these steps:

1. In a pull request, add the equivalent checks to `.chainguard/ci.yaml`, or add the `.chainguard/ci/migrated.yaml` file that you drafted, and keep the GitHub Actions workflow.
2. Compare the results of both on that pull request and the ones after it.
3. When the results match, add **Chainguard Checks (presubmit)** as a required status check, as described in [Require checks before merging](/chainguard/checks/github/#require-checks-before-merging).
4. Remove the GitHub Actions workflow, and remove its jobs from your required status checks.
