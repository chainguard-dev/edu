---
title: "Troubleshoot Chainguard Checks"
linktitle: "Troubleshooting"
description: "Fix common problems with Chainguard Checks, including pull requests that get no checks, refused configurations, failed runs, checks that couldn't run, network errors, missing tools, and unused caches."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-15T12:09:53+00:00
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

This page describes common problems with Chainguard Checks and how to fix them. If your problem isn't listed here, ask in the #checks-questions channel in the [Chainguard community Slack](https://join.slack.com/t/chainguardcommunity/shared_invite/zt-3nttdr807-V9BJHayWvsB0KbHsfZO5Rw).

## A pull request gets no checks {#a-pull-request-gets-no-checks}

If a pull request shows no **Chainguard Checks (presubmit)** check at all, Chainguard Checks didn't start a run for it. Confirm the following:

- The Chainguard App is installed on the GitHub account that owns the repository, with access to the repository, and that account is linked to your Chainguard organization. Running `chainctl develop init` links the account when you sign up. A GitHub account can be linked to only one Chainguard organization at a time.
- The repository has a `.chainguard/ci.yaml` file or a `.chainguard/ci/` directory at its root, on the pull request's branch or its base branch. A file named `ci.yml` doesn't count.
- The configuration has presubmit checks. Checks with only `trigger: postsubmit` run after merging, not on pull requests. A pull request that changes every check to `trigger: postsubmit` still gets a summary check, which fails with **Run creation failed**, as described in [Change checks in a pull request](/chainguard/checks/github/#change-checks-in-a-pull-request). It gets no checks only if each of the base branch's presubmit checks is limited by `when.changed` to files that no longer exist.
- Chainguard Checks is turned on for your organization, either with `chainctl develop init` or by your Chainguard account team. Pull requests opened or updated before then get no checks, so push a new commit to the pull request to start a run. If `chainctl develop init` failed, refer to [chainctl develop init fails](/chainguard/workspaces/troubleshooting/#chainctl-develop-init-fails).
- Your organization isn't at its run limit. With the [Starter allowance](/chainguard/checks/overview/#availability-and-limits), your organization can have 10 runs queued or running at a time, including runs after merging. At the limit, Chainguard Checks retries a new run for a few minutes, then gives up, and the pull request shows no summary check. The run doesn't start on its own when a place frees up, so once earlier runs finish, push a new commit, reopen the pull request, or use **Re-run**.
- If your organization started a free trial with `chainctl` 0.2.379 or earlier, the trial hasn't ended. That trial lasts 30 days, plus a 7-day grace period, and includes 500 vCPU-hours of Checks. When the grace period ends, Chainguard Checks stops starting runs. To continue, [contact Chainguard](https://www.chainguard.dev/contact?utm=docs).

## The summary check says the configuration is invalid {#the-summary-check-says-the-configuration-is-invalid}

If **Chainguard Checks (presubmit)** fails with a title that starts with **Invalid config**, Chainguard Checks refused the pull request's configuration and ran nothing. The summary check's output lists each problem with its file and line. To find the same problems before you push, run `chainctl checks validate .` from your repository's directory.

The following table lists the most common causes, grouped by the key or file they involve:

| Cause | What to do |
| ----- | ---------- |
| A configuration file doesn't have `version: 1`. | Add `version: 1` to the file. |
| A configuration file uses GitHub Actions keys, such as `jobs`, `on`, `runs-on`, or `env`. | Replace them with their equivalents, as described in [Migrate from GitHub Actions](/chainguard/checks/migrate-from-github-actions/). |
| A string `cmd` contains unquoted shell syntax, such as a pipe, redirection, `&&`, a variable, or a glob character. | A string `cmd` runs without a shell. Quote those characters to pass them to the command as they are, or use `script` to run them with a shell. Inside double quotes, `$` and backticks are refused too, so put them in single quotes. Refer to [The cmd key](/chainguard/checks/configuration/#the-cmd-key). |
| A check's `shell` isn't the exact name of a package in the check's environment. | Set `shell` to a package that the environment lists, such as `python-3.13`. |
| A check has a `network` key with no hosts under `egress`. | List the hosts the check needs. To keep a check off the network, leave out `network` entirely. |
| A `when` key is empty. | To run the check every time, leave out `when`. Refer to [Conditions](/chainguard/checks/configuration/#conditions). |
| `when.changed` lists no patterns. | List at least one pattern, or leave out `changed`. |
| `when.requested` is set to something other than `true`. | Set it to `true`, or leave it out. |
| A `foreach` entry sets `when: {requested: true}`. | Set `when: {requested: true}` on the check instead. |
| A check with `when: {requested: true}` has no `description`. | Add a `description` that says what the check covers and when it's worth running. Refer to [Run on request](/chainguard/checks/configuration/#run-on-request). |
| A check with `when: {requested: true}` also sets `changed` or `expr` under `when`. | To run a check when its files change and also on request, use `when.changed` alone. Refer to [Run a check on request](/chainguard/checks/github/#run-a-check-on-request). |
| A check with `when: {requested: true}` has a name longer than 43 characters. | Shorten the name. Refer to [Run on request](/chainguard/checks/configuration/#run-on-request). |
| A blocking check needs an advisory check, either with `needs` or by taking an input from it with `from`. | Make both checks advisory, or both blocking. Refer to [Advisory checks](/chainguard/checks/configuration/#advisory-checks). |
| A check that doesn't run on request needs one that does, with `needs` or `from`. | Make both checks run on request, or neither. Refer to [Run on request](/chainguard/checks/configuration/#run-on-request). |
| A check's name has a character that isn't allowed, or doesn't start and end with a letter or digit. | Rename the check. Unless the character is `.` or `/`, the error for a character that isn't allowed says only that the name must fit the 128-character limit, even when the name is short. Refer to [Check names](/chainguard/checks/configuration/#check-names). |
| Two checks in the same file have names that differ only in case, such as `Test` and `test`. | Rename one of them. |
| A check's full name, such as `ci/test`, is longer than 128 characters. | Shorten the check's name, or the file's. |
| A check's environment names a cache under `caches`, but the check doesn't set `user: build`. | Set `user: build` on the check, or give it an environment without the cache. Refer to [Build caches](/chainguard/checks/variations-services-caches/#build-caches). |
| A check sets a variable that its cache sets, such as `GOCACHE`. | Remove the variable from the check's `vars`. |
| A check's `docs` names a Markdown file that doesn't exist beside the check's file in `.chainguard/ci/`, or that's larger than 1 MiB. | Add or shorten the file. The single-file layout doesn't support `docs`. Refer to [Describe a check](/chainguard/checks/configuration/#describe-a-check). |
| `.chainguard/ci/resources.yaml` doesn't define a class named `default`. | Add a `default` class. Refer to [Define your own resource classes](/chainguard/checks/configuration/#define-your-own-resource-classes). |
| `resources.yaml` gives a `memory` or `disk` size in a unit other than `Mi` or `Gi`, such as `16GB`. | Write the size in `Mi` or `Gi`, such as `16Gi`. |
| A check names a resource class that `resources.yaml` doesn't define. | The file replaces the built-in classes, so a check can't name `medium` or `large-amd64` unless the file defines it. Define the class, or name one that the file defines. |
| `.chainguard/` or `.chainguard/ci/` holds a file that the repository's layout doesn't allow, such as a `.yml` file. | Remove or rename the file. Refer to [File layouts](/chainguard/checks/configuration/#file-layouts) for the files each layout allows. |
| The repository has a `.chainguard/ci.yaml` file and also has files in `.chainguard/ci/` other than `identities.yaml`. | A repository can't use both layouts. Move the checks from `.chainguard/ci.yaml` into a file in `.chainguard/ci/`, and its environment to `.chainguard/ci/env/default.yaml`. |

## The summary check says the run couldn't be created or failed {#the-summary-check-says-the-run-couldnt-be-created-or-failed}

If **Chainguard Checks (presubmit)** fails with **Run creation failed** or **Run failed**, Chainguard Checks read your configuration but didn't run it. The summary check's output gives the reason. The following table lists the most common causes:

| Cause | What to do |
| ----- | ---------- |
| The pull request removes a check, changes a check's conditions or trigger so that it no longer runs for this pull request, or leaves no presubmit checks while the base branch's configuration still has one, even one that wouldn't have run for this pull request. The exception is a check limited by `when.changed` to files that no longer exist. | A change can't remove itself from its own checks. Refer to [Change checks in a pull request](/chainguard/checks/github/#change-checks-in-a-pull-request). |
| The pull request changes 3,000 or more files, and the output says so. | Split the change into smaller pull requests, because **Re-run** fails the same way. A commit on your default branch that changes 3,000 or more files also fails in **Chainguard Checks (postsubmit)**. Refer to [Availability and limits](/chainguard/checks/overview/#availability-and-limits). |
| A check `needs` another check that doesn't run under the same trigger, such as a presubmit check that needs a check with only `trigger: postsubmit`. | Give both checks the same `trigger`. |
| A check's `git` input names a private repository, or a `ref` that doesn't exist in the repository. | Chainguard Checks resolves each `git` input to a commit when it creates the run, without credentials, so it can check out only public GitHub repositories. Refer to [Check out another repository](/chainguard/checks/variations-services-caches/#check-out-another-repository). |
| A check's `user` is the name of an account that the VM already has, such as `daemon`, `mail`, or `nobody`, and the output says that the user collides with an existing account. | `chainctl checks validate` accepts these names, but the run fails. Choose another name, such as `build`, as described in [Run as another user](/chainguard/checks/variations-services-caches/#run-as-another-user). |
| A check binds `context.github.pull_request.body` to `CHAINGUARD_BASE_REVISION`, `GOOGLE_APPLICATION_CREDENTIALS`, `GITHUB_TOKEN`, or `GOFLAGS`. | Bind the description to a variable with another name. Refer to [Environment variables](/chainguard/checks/configuration/#environment-variables). |
| A check binds the pull request's description, and the description is over 65,536 bytes or contains a NUL character. The output says how many bytes the description is, or that it contains NUL. | Shorten the description, then use **Re-run** on the summary check, or push a new commit. Characters outside ASCII take more than one byte each. |
| A check asks for a larger resource class than your organization allows. The output says that a job asks for more CPUs and memory, or more scratch disk, than your organization's largest resource class. | Choose a smaller class with `resources`, or lower your class's `cpus`, `memory`, or `disk`. With the Starter allowance, the largest class is `medium`, which has 4 vCPUs and 16 GB of memory. Unless your organization's allowance sets a different limit, a check's VM can have at most 16 vCPUs, 64 GB of memory, and 100 GB of disk. The built-in classes are within these limits, but a class you [define in `resources.yaml`](/chainguard/checks/configuration/#define-your-own-resource-classes) can exceed them. |
| Your organization used up this month's compute allowance. The output says that your organization can't start work until the allowance resets on the first day of the month (UTC), and that work already running finishes. | After the reset, use **Re-run** on the summary check, or push a new commit. To continue sooner, [contact Chainguard](https://www.chainguard.dev/contact?utm=docs). Refer to [Availability and limits](/chainguard/checks/overview/#availability-and-limits) for how checks use the allowance. |
| Your organization hasn't accepted the terms that Chainguard Checks is offered under. The output names the terms and the command that accepts them. | Have an organization owner run `chainctl checks accept-terms --parent $ORGANIZATION`, replacing `$ORGANIZATION` with the name of your Chainguard organization. After about 30 seconds, use **Re-run** on the summary check, or push a new commit. |

## The summary check says checks could not be executed {#the-summary-check-says-checks-could-not-be-executed}

If **Chainguard Checks (presubmit)** says that checks could not be executed, or a check's title starts with **Could not be executed**, those checks stopped for a reason other than a command that failed. The summary check's output lists each one's reason under **Errors:**, as described in [Read the summary check](/chainguard/checks/github/#read-the-summary-check). These are the most common reasons:

| Reason | What to do |
| ------ | ---------- |
| `task timed out after`, followed by the check's `timeout` | The check ran longer than its own [timeout](/chainguard/checks/configuration/#timeouts). Raise `timeout`, or split the check into smaller ones. |
| `workflow run exceeded the 50-minute limit` | The run reached its time limit before the check finished. Refer to [A check stops after 50 minutes](#a-check-stops-after-50-minutes). |
| Includes `workflow identity rejected` | The check didn't get its workload identity, for example because the pull request doesn't reach the identity's ring. Refer to [When a pull request doesn't get an identity](/chainguard/checks/identity-and-trust/#when-a-pull-request-doesnt-get-an-identity). |
| `the package set does not resolve`, or `two packages in the set install the same file` | Chainguard Checks couldn't install the check's packages. Fix the names and version constraints in `environment.packages`, or remove one of the two packages that install the same file. |
| Any other reason | The check's VM kept failing for a reason outside the check, even after [automatic retries](/chainguard/checks/github/#automatic-retries). Use **Re-run** on the summary check, or push a new commit. |

## The summary check reports a merge conflict {#the-summary-check-reports-a-merge-conflict}

Chainguard Checks runs each pull request against the commit GitHub would create by merging it. If the pull request has merge conflicts with its base branch, GitHub can't create that commit, and the summary check fails with **Merge conflict with the base branch**. Resolve the conflicts and push.

## A check can't find a command {#a-check-cant-find-a-command}

A check's VM starts with BusyBox, GNU tar, and only the packages you list, so commands such as `git`, `bash`, `make`, and `curl` aren't available unless you list their packages. Add the package to `environment.packages` in your configuration file.

If a script file fails with `not found`, its first line, such as `#!/bin/bash`, may name an interpreter that isn't installed. List the interpreter's package. If a `script` uses Bash syntax, also set `shell: bash` and list the `bash` package.

## A check can't reach a host {#a-check-cant-reach-a-host}

A check has no network access unless it lists hosts under `network.egress`, so downloads and API calls fail, often with errors that a host couldn't be resolved or a connection was refused. Add each host the check needs to its `egress` list, such as `proxy.golang.org` for Go modules or `registry.npmjs.org` for npm packages. List bare hostnames, without a scheme or port. Refer to [Network access](/chainguard/checks/configuration/#network-access).

Some hosts redirect to others. For example, a package registry might serve files from a separate content delivery host. To see every host a check tried to reach, follow these steps:

1. Open the check's **Details** link on the pull request, and sign in with your Chainguard account.
2. In the run page's sidebar, under the check's name, select **Details**.
3. Expand **Network activity**. It's already open if Chainguard Checks refused a connection.
4. Add each host whose **Decision** is `deny` or `destroy` to the check's `egress` list.

The table has a row for each hostname the check looked up and each address it connected to. A connection's row shows the IP address and port, followed by the hostnames the check looked up for that address. With `policy: destroy`, the page also names the host that stopped the check. To open the run page, you need a role in your Chainguard organization, as described in [The Details link or a chainctl checks command says you don't have access](#the-details-link-or-a-chainctl-checks-command-says-you-dont-have-access).

## A check can't find submodules, Git LFS files, or private repositories {#a-check-cant-find-submodules-git-lfs-files-or-private-repositories}

A check's `/work` directory holds your repository's tracked files and history, but not submodules or Git LFS content. Submodule directories are empty, and files that Git LFS tracks hold their pointer files. During the beta, a check also has no GitHub credential, so commands that fetch from a private GitHub repository, such as a download of a private Go module, fail to authenticate. Refer to [Credentials](/chainguard/checks/configuration/#credentials).

To add files from another public repository, use a [`git` input](/chainguard/checks/variations-services-caches/#check-out-another-repository).

## A check fails on pull requests but passes in run-ci {#a-check-fails-on-pull-requests-but-passes-in-run-ci}

The `run-ci` command in a Workspaces session runs each check in the session's environment, which can differ from the pull request's:

- The session might have packages or network access that the check's own environment doesn't list.
- Sessions run on x86-64 unless their resource class pins arm64, while pull request checks usually run on arm64 unless their resource class pins x86-64. If a check downloads or runs an x86-64 binary, set its resource class to an `-amd64` variant of a built-in class, such as `medium-amd64`. If you [define your own resource classes](/chainguard/checks/configuration/#define-your-own-resource-classes), set `platform` on the check's class instead, because only `platform` pins the architecture.

Refer to [How run-ci differs from a pull request run](/chainguard/checks/run-checks/#how-run-ci-differs-from-a-pull-request-run).

To see what failed on the pull request, print the error lines of the check's log from your terminal, with three lines around each. Replace `$OWNER/$REPO#$NUMBER` with the pull request, such as `acme/app#123`, `test` with the check's name, and `$ORGANIZATION` with the name of your Chainguard organization:

```shell
chainctl checks logs "$OWNER/$REPO#$NUMBER" --check test --errors -C 3 --parent $ORGANIZATION
```

For other ways to read part of a long log, and the role these commands need, refer to [Inspect pull request runs](/chainguard/checks/inspect-and-run-checks/#inspect-pull-request-runs).

## A check stops after 50 minutes {#a-check-stops-after-50-minutes}

A whole run can take up to 50 minutes from when it starts, and checks still running or waiting to start at that point fail. Split long checks into smaller ones, which run in parallel, up to four at a time with the Starter allowance. You can also move slow work to a [postsubmit check](/chainguard/checks/github/#run-checks-after-merging).

## A check runs out of space in /tmp {#a-check-runs-out-of-space-in-tmp}

A check's `/tmp` directory is held in memory and can hold up to a quarter of the VM's memory: about 2 GB with the default class, or 4 GB with `medium`. When it's full, commands that write there fail with `No space left on device`, even though the VM's disk has room.

Put large files, such as build output, downloaded archives, or a Python virtual environment, under `/var/tmp` or `/work`, which are on the VM's disk. Many tools write temporary files to the directory that `TMPDIR` names, so you can also set `TMPDIR` to `/var/tmp` in the check's `vars`. To give `/tmp` more room instead, choose a resource class with more memory. Refer to [Resources](/chainguard/checks/configuration/#resources).

## A check doesn't use its cache {#a-check-doesnt-use-its-cache}

A check whose environment names a cache under `caches` runs without one, and without an error, in the following cases:

- Your default branch doesn't define cache pools yet. This includes the pull request that adds them, because Chainguard Checks reads pools only from your default branch. Refer to [Set up cache pools](/chainguard/checks/variations-services-caches/#set-up-cache-pools).
- No pool lists the run's ring, such as ring `0` for a pull request opened by someone outside your subrings.
- The cache isn't `gobuild`. During the beta, the other cache types cache nothing.
- The run is a rerun from **Re-run** on GitHub or from `chainctl checks rerun`.
- The check uses a workload identity, and a ring in its pool can't get the same identity.
- The pool is still filling, as described in [How caches fill](/chainguard/checks/variations-services-caches/#how-caches-fill).

To see what each check gets, run `chainctl checks explain` and read its `cache selection` section. For each check that names a cache, it shows what the check mounts in each pool, or why it mounts nothing. It can't tell which pool a pull request's author reaches, and it lists the cache types other than `gobuild` as `read-write`, though they cache nothing during the beta.

## A required check never reports {#a-required-check-never-reports}

If GitHub waits indefinitely for a required check, you probably required a per-check result, such as **presubmit / ci / test**, instead of the summary check. A check that a condition skips, or that runs only on request, never reports a result. Require only **Chainguard Checks (presubmit)**, as described in [Require checks before merging](/chainguard/checks/github/#require-checks-before-merging).

A GitHub merge queue that requires **Chainguard Checks (presubmit)** never gets a result either, because Chainguard Checks doesn't run on merge queues during the beta. The queue waits until its timeout expires, then removes the pull request. Don't require the summary check on a branch that uses a merge queue.

## The requested checks agent doesn't comment on a pull request {#the-requested-checks-agent-doesnt-comment-on-a-pull-request}

The [requested checks agent](/chainguard/checks/github/#let-an-agent-request-checks) doesn't add a comment for each push. It keeps one **Requested checks** comment on the pull request, edits it, and names the commit that it answers for. If the comment doesn't appear at all, or names an earlier commit, check the following:

- `requested_checks_agent` is set to `comment` or `agent` on the pull request's base branch. The agent reads the setting from the latest commit on the base branch, so the pull request that sets it gets no answer. After it merges, pull requests that are already open get an answer at their next push or edit.
- The pull request is open and isn't a draft. Marking a draft ready for review starts the agent.
- If the pull request changes files in `.chainguard/`, its configuration is valid. To check, run `chainctl checks validate`.
- The pull request has a check that the agent could request: a presubmit check with `when: {requested: true}`, or with `when.changed` patterns that the pull request's changes don't match. The agent skips checks whose `when.expr` is false and checks that already run, and when none are left, it doesn't comment.
- The pull request changes fewer than 3,000 files.

The agent answers once for each pushed commit and base branch. Editing the pull request's title or description doesn't make it choose again, but pushing a commit or changing the base branch does. When it finds no check worth running, it still comments to say so.

## chainctl doesn't list the checks command {#chainctl-doesnt-list-the-checks-command}

{{% blurb/hidden-chainctl-commands %}}

For every subcommand and flag, refer to the [`chainctl checks` reference](/chainguard/checks/chainctl-checks-reference/) and the [`chainctl develop` reference](/chainguard/workspaces/chainctl-develop-reference/).

If `chainctl checks validate .` reports that validating a directory isn't supported, or `chainctl` doesn't recognize a command on this site, your `chainctl` is out of date. Update it with `sudo chainctl update`, or with `brew upgrade chainctl` if you installed it with Homebrew.

## chainctl checks status reports no platform verdict {#chainctl-checks-status-reports-no-platform-verdict}

During the beta, `chainctl checks status`, `chainctl checks logs`, and the other commands that inspect runs can't find a run by its commit. When you pass a commit SHA or a directory, or run one of these commands with no argument, which uses the commit checked out in the current directory, they report that the platform created no run for it, even when its checks ran. The `chainctl checks list` command doesn't list pull request runs or runs after merging either.

To inspect a pull request's latest run, pass the pull request instead. Replace `$OWNER/$REPO#$NUMBER` with the pull request, such as `acme/app#123`, or with its URL. Replace `$ORGANIZATION` with the name of the Chainguard organization linked to the repository's GitHub account:

```shell
chainctl checks status "$OWNER/$REPO#$NUMBER" --parent $ORGANIZATION
```

If the command still reports no platform verdict for a pull request whose checks appear on GitHub, check that you typed the owner and repository exactly as GitHub shows them, including capital letters. With a `chainctl` release older than the [minimum version](/get-started/checks-and-workspaces/set-up/#install-or-update-chainctl), pull requests also report no platform verdict. Update it with `sudo chainctl update`, or with `brew upgrade chainctl` if you installed it with Homebrew.

For a run after merging, pass the run's ID instead of a commit. The ID is the part after `/runs/` in the **Details** link of **Chainguard Checks (postsubmit)**. You can also read the results on GitHub, as described in [Run checks after merging](/chainguard/checks/github/#run-checks-after-merging).

For a run you started with [`chainctl checks run`](/chainguard/checks/chainctl-checks-reference/#chainctl-checks-run), pass the ID that the command printed, or the start of it, instead of `.` or a commit. To find the ID later, run `chainctl checks list`. These runs never appear on GitHub.

## The Details link or a chainctl checks command says you don't have access {#the-details-link-or-a-chainctl-checks-command-says-you-dont-have-access}

The **Details** link on a check opens the run on a page that Chainguard hosts, where you sign in with your Chainguard account. To open the run page, or to read or rerun runs with `chainctl checks` commands such as `status`, `logs`, and `rerun`, you need the `owner` or `sandbox.user` role in the Chainguard organization linked to the repository's GitHub account. Without one of these roles, `chainctl checks` fails with `permission denied`.

To pass your organization's name to `--parent`, you also need a role that can see the organization, such as `viewer`. With `sandbox.user` alone, `chainctl` can't find your organization by its name, so pass the organization's ID instead.

To get these roles, ask an owner of your organization, as described in [Give teammates access](/get-started/checks-and-workspaces/set-up/#give-teammates-access).

During the beta, if you created a Starter organization with `chainctl develop init`, you have the `limited_owner` role instead, which can't open the run page or read runs, and you can't grant the `sandbox.user` role. In that case, do the following:

- Read the results on the pull request, as described in [How results appear](/chainguard/checks/github/#how-results-appear), and rerun checks with **Re-run** on GitHub.
- Don't use `chainctl checks run`. Your role can start runs, which use your allowance, but can't read their results.
- To run checks before you push, use a Workspaces session with `chainctl develop check`, as described in [Run checks in a session from your laptop](/chainguard/checks/run-checks/#run-checks-in-a-session-from-your-laptop).
