---
title: "Troubleshoot Chainguard Checks"
linktitle: "Troubleshooting"
description: "Fix common problems with Chainguard Checks, including pull requests that get no checks, refused configurations, failed runs, network errors, and missing tools."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-08T00:00:00+00:00
draft: false
tags: ["Chainguard Checks", "Troubleshooting"]
images: []
menu:
  docs:
    parent: "checks"
    identifier: "Checks Troubleshooting"
toc: true
weight: 70
---

This page describes common problems with Chainguard Checks and how to fix them. If your problem isn't listed here, contact your Chainguard account team or email [support@chainguard.dev](mailto:support@chainguard.dev).

## A pull request gets no checks

If a pull request shows no **Chainguard Checks (presubmit)** check at all, Chainguard Checks didn't start a run for it. Confirm the following:

- The Chainguard App is installed on the GitHub account that owns the repository, with access to the repository, and that account is linked to your Chainguard organization. Running `chainctl develop init` links the account when you start a trial.
- The repository has a `.chainguard/ci.yaml` file or a `.chainguard/ci/` directory at its root, on the pull request's branch or its base branch. A file named `ci.yml` doesn't count.
- The configuration has presubmit checks. Checks with only `trigger: postsubmit` run after merging, not on pull requests.
- Your organization finished setting up. After a trial starts, Chainguard takes about an hour to finish setting up a new organization, and pull requests opened or updated before then get no checks. After an hour, push a new commit to the pull request to start a run.
- Your organization isn't at its run limit. During a free trial, your organization can have 10 runs queued or running at a time, including runs after merging. At the limit, Chainguard Checks doesn't start a run for a new commit, and the pull request shows no summary check until a place frees up. Pushing again doesn't free a place.
- Your organization still has access. When a trial ends, Chainguard Checks stops starting runs. Contact your Chainguard account team to continue.

## The summary check says the configuration is invalid

If **Chainguard Checks (presubmit)** fails with a title that starts with **Invalid config**, Chainguard Checks refused the pull request's configuration and ran nothing. The summary check's output lists each problem with its file and line.

To find the same problems before you push, run `chainctl checks validate .` from your repository's directory. These are the most common causes:

- A configuration file doesn't have `version: 1`.
- A configuration file uses GitHub Actions keys, such as `jobs`, `on`, `runs-on`, or `env`, which aren't part of the format. Refer to [Migrate from GitHub Actions](/chainguard/checks/migrate-from-github-actions/) for their equivalents. A file drafted by `chainctl checks migrate` uses a `jobs` key that pull requests don't accept yet.
- A string `cmd` contains shell syntax. A string `cmd` runs without a shell, so Chainguard Checks refuses pipes, redirection, `&&`, variables, and glob characters in it. Use `script` instead.
- A check has a `network` key with no hosts under `egress`. To keep a check off the network, leave out `network` entirely.
- A check with `when: {requested: true}` has no `description`.
- A check's `shell` isn't the exact name of a package in the check's environment, such as `python-3.13`.
- The `.chainguard/` directory holds a file that isn't a configuration file, such as `README.md`, or a file with the `.yml` extension.

## The summary check says the run couldn't be created or failed

If **Chainguard Checks (presubmit)** fails with **Run creation failed** or **Run failed**, Chainguard Checks read your configuration but didn't run it. The summary check's output gives the reason. These are the most common causes:

- The pull request removes a check, or changes a check's conditions or trigger so that it no longer runs for this pull request. A change can't remove itself from its own checks. Refer to [Change checks in a pull request](/chainguard/checks/github/#change-checks-in-a-pull-request).
- A check `needs` another check that doesn't run under the same trigger. For example, a presubmit check can't need a check with only `trigger: postsubmit`.
- A check asks for a larger resource class than your organization allows. The output says that a job asks for more CPUs and memory than your organization's largest resource class. During a free trial, the largest class is `medium`, which has 4 vCPUs and 16 GB of memory. Choose a smaller class with `resources`.
- Your organization used up its compute budget. The output says that the compute budget is used up and that work already running finishes. Contact your Chainguard account team to continue.

## The summary check reports a merge conflict

Chainguard Checks runs each pull request against the commit GitHub would create by merging it. If the pull request has merge conflicts with its base branch, GitHub can't create that commit, and the summary check fails with **Merge conflict with the base branch**. Resolve the conflicts and push.

## A check can't find a command

A check's VM starts with BusyBox, GNU tar, and only the packages you list, so commands such as `git`, `bash`, `make`, and `curl` aren't available unless you list their packages. Add the package to `environment.packages` in your configuration file.

If a script file fails with `not found`, its first line, such as `#!/bin/bash`, may name an interpreter that isn't installed. List the interpreter's package. If a `script` uses Bash syntax, also set `shell: bash` and list the `bash` package.

## A check can't reach a host

A check has no network access unless it lists hosts under `network.egress`, so downloads and API calls fail, often with errors that a host couldn't be resolved or a connection was refused. Add each host the check needs to its `egress` list, such as `proxy.golang.org` for Go modules or `registry.npmjs.org` for npm packages. List bare hostnames, without a scheme or port. Refer to [Network access](/chainguard/checks/configuration/#network-access).

Some hosts redirect to others. For example, a package registry might serve files from a separate content delivery host. If a download still fails after you add the registry, look in the check's log for the host it was redirected to, and add that host too.

## A check fails on pull requests but passes in run-ci

The `run-ci` command in a Workspaces session runs each check in the session's environment, which can differ from the pull request's:

- The session might have packages or network access that the check's own environment doesn't list.
- Sessions run on x86-64, while pull request checks usually run on arm64. If a check downloads or runs an x86-64 binary, set its resource class to an `-amd64` variant, such as `medium-amd64`.

Refer to [How run-ci differs from a pull request run](/chainguard/checks/run-checks/#how-run-ci-differs-from-a-pull-request-run).

## A check stops after 50 minutes

A whole run can take up to 50 minutes from when it starts, and checks still running or waiting to start at that point fail. Split long checks into smaller ones, which run in parallel, up to four at a time during a free trial. You can also move slow work to a [postsubmit check](/chainguard/checks/github/#run-checks-after-merging).

## A required check never reports

If GitHub waits indefinitely for a required check, you probably required a per-check result, such as **presubmit / ci / test**, instead of the summary check. A check that a condition skips, or that runs only on request, never reports a result. Require only **Chainguard Checks (presubmit)**, as described in [Require checks before merging](/chainguard/checks/github/#require-checks-before-merging).

## chainctl doesn't list the checks command

During the beta, `chainctl checks` doesn't appear in `chainctl --help`. You can still run it, and `chainctl checks --help` shows its full help.

If `chainctl checks validate .` reports that validating a directory isn't supported, or `chainctl` doesn't recognize a command on this site, your `chainctl` is out of date. Update it with `sudo chainctl update`, or with `brew upgrade chainctl` if you installed it with Homebrew.

## chainctl checks status reports no platform verdict

During the beta, `chainctl checks status`, `chainctl checks logs`, and the other commands that inspect runs don't show pull request runs. For a pull request, they report that the platform created no run for it, even when its checks ran. Read the results on GitHub instead, as described in [How results appear](/chainguard/checks/github/#how-results-appear).
