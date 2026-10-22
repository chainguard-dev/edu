---
title: "How Chainguard Checks and Chainguard Workspaces isolate your code"
date: 2026-10-15T12:09:53+00:00
lastmod: 2026-10-22T14:48:15+00:00
linktitle: "How it works"
description: "The security model of Chainguard Checks and Chainguard Workspaces in one place: microVM isolation, credentials kept outside the VM, network allowlists, trust rings, and the run and session lifecycles."
type: "article"
draft: false
tags: ["Chainguard Checks", "Chainguard Workspaces", "Security", "Overview"]
images: []
weight: 20
toc: true
---

Chainguard Checks runs your pull request checks, and Chainguard Workspaces runs your development sessions and coding agents, in microVMs that hold none of your long-lived credentials. This page collects the security model of both products in one place, for security reviewers who need to decide whether to allow them and for coding agents that need the rules. It describes how each product isolates code, where credentials come from, what code can reach on the network, who decides what a pull request gets, and how runs and sessions move through their lifecycles. A [glossary](#glossary) at the end defines the terms both products use.

For sign-up and roles, refer to [Set up Chainguard Checks and Chainguard Workspaces](/get-started/checks-and-workspaces/set-up/).

{{< beta feature="Each product" >}}

## Isolation {#isolation}

Each check, and each session, runs in its own microVM built on Chainguard OS:

| | Chainguard Checks | Chainguard Workspaces |
| -- | -- | -- |
| What gets a VM | Each check on each run. A check that runs once for each of several [variations](#glossary) gets one VM for each variation. | Each session. You can open several sessions on one repository, and each is its own VM. |
| How long the VM lasts | One check. The next run, and every retry, starts a fresh VM. | The life of the session. The VM stops when the session parks, and resumes from a snapshot. |
| What starts in the VM | BusyBox, GNU tar, and the packages the configuration declares. Your repository's code is already in the VM. | Your synced directory at `/work`, the packages the configuration declares, and by default `git`, `gh`, Claude Code, and `chainctl`. By default, you work as `root`. |

Chainguard treats the code in every VM as hostile, so the VM is the boundary that holds it:

- Chainguard puts no credential in the VM in a form its code could spend elsewhere. Credentials are added outside the VM, as described in [Credentials](#credentials).
- No host directory is mounted in the VM. Chainguard streams your repository, or the directory you sync to a session, into it.
- A session's snapshot is sealed and bound to its owner, so a copy of it can't restore anyone else's session.

A check starts with nothing from earlier runs unless it declares a cache. Even then, a run gets a cache only from a cache pool that your default branch defines for the run's [ring](#rings).

In a session, `run-ci` runs your checks inside the session's own VM, not in fresh VMs, so its environment can differ from a pull request run. Only Chainguard Checks, which runs each check in a fresh VM, decides what GitHub shows. Refer to [How run-ci differs from a pull request run](/chainguard/checks/run-checks/#how-run-ci-differs-from-a-pull-request-run).

## Credentials {#credentials}

Neither product puts a long-lived credential in the VM. Where a check or session needs access, the credential is added to its requests outside the VM.

| | Chainguard Checks | Chainguard Workspaces |
| -- | -- | -- |
| How code authenticates | A check can request a [workload identity](/chainguard/checks/identity-and-trust/). Chainguard Checks issues the check an OpenID Connect (OIDC) token that lasts five minutes, and renews it while the check runs. | The session reaches each service through a local hostname, such as `http://github/` or `http://claude/`. `chainctl` on your laptop, or Chainguard, adds the credential to each request. |
| What the VM holds | For Google Cloud, a credential configuration and sealed stand-in tokens. Chainguard Checks swaps in the real tokens only on requests to `sts.googleapis.com` and other `googleapis.com` subdomains. For Chainguard, nothing. | A placeholder at most. For `github` and `cgr.dev` from your laptop, the credential never leaves your machine. For `claude` and `gcp`, `chainctl` sends it to the session's host, outside the VM, and the host discards it when the session parks. For a session that uses a Claude login Chainguard holds for you, Chainguard sends the host short-lived access tokens from it instead, attached or not, and sends them again when the session resumes. |
| Who decides | `identities.yaml` on the pull request's base branch, and the `trust` section on your default branch. | Your organization's policy and the session's credential settings. A request beyond the defaults needs your approval on your terminal. |

Code in the VM can't read the real credentials, but it can use them. Each request it sends carries the credential's access, and anything it creates with that access, such as a Google Cloud service account key, outlives the check or session. Grant each workload identity only the access its checks need, and review a session's credentials before you let an agent work in it unattended. Refer to [Manage session credentials](/chainguard/workspaces/credentials/).

For a check's workload identity, and for your Google Cloud credential in a session, a proxy outside the VM swaps in the real credential only on requests that it has verified over TLS as going to an allowed host. For a check's Chainguard identity, the proxy also refuses opaque TLS tunnels to Chainguard hosts, and sends each request only to the host whose TLS name it verified.

Sessions can't use workload identities, so `run-ci` skips checks that use one.

Two credentials sit outside these controls:

- A credential that you paste into a session, or that a tool there stores, such as with `aws configure` or `npm login`, stays on the session's disk or in its memory, and in its snapshot when it parks. Any program in the session can read it. Do that work on your laptop instead.
- If you connected your GitHub account, sessions you create afterward act on GitHub as you, through the Chainguard Develop GitHub App. They can push, approve pull requests, and merge as you, and neither an `egress` list nor `chainctl develop creds` limits them. Refer to [Protect your branches](/chainguard/workspaces/github-as-you/#protect-your-branches).

## Network {#network}

Both products use the same `network.egress` allowlist, but they read a missing `network` key in opposite ways:

| The check's configuration | In a check | In a session |
| -- | -- | -- |
| No `network` key | No network access | The open internet |
| `network.egress` lists hosts | Only those hosts | Only those hosts, when you open the session on that check |
| `network.egress: ["*"]` | Any public host | Any public host |
| `policy: destroy` | A connection to an unlisted host stops the VM, and the check fails | Treated as `deny`: the connection is refused, and the session keeps running |

A session that uses the default environment, a `.chainguard/develop.yaml` file, or a file's top-level `environment` reaches the open internet, because none of these can set `network`. To restrict a session, open it on a check that has an `egress` list. Refer to [Network access](/chainguard/workspaces/session-environment/#network-access).

Whatever a check or session allows, it never reaches cloud metadata endpoints, loopback addresses, or private IP ranges. Chainguard Checks also intercepts most HTTPS connections from a check, using a certificate authority that it creates for that check's VM alone, as described in [Network access](/chainguard/checks/configuration/#network-access).

The `egress` list doesn't apply to a session's credential hostnames, such as `http://github/` and `http://claude/`, so a session with a narrow list can still push to GitHub and use Claude Code. Google Cloud is different, because its requests go to Google's own hosts: a check that uses a Google Cloud workload identity, and a session that uses your Google Cloud credentials with an `egress` list, must list `sts.googleapis.com` and the Google APIs they call.

To see which hosts a check tried to reach, and whether Chainguard Checks allowed each one, open the check's run page from its **Details** link on GitHub. Refer to [A check can't reach a host](/chainguard/checks/troubleshooting/#a-check-cant-reach-a-host).

## Trust {#trust}

Chainguard Checks reads the rules that limit a pull request, such as which checks gate it, which identities it can get, and how far it's trusted, from branches the pull request can't change. The pull request controls only what its checks run:

| What a run gets | Where Chainguard Checks reads it |
| -- | -- |
| Which checks must run, and which of them block | The pull request's base branch |
| An identity's definition: which checks, branches, and audiences get it | `identities.yaml` on the pull request's base branch |
| The `trust` section: groups, subrings, rings, and cache pools | Your default branch's latest commit |
| Each check's commands, its `identity` key, and its `network.egress` | The commit being tested, which includes the pull request's changes |

A pull request can add checks and change what they run, but it can't weaken its own gate:

- A change that makes a check advisory, or makes it run only on request, takes effect after the pull request merges. Until then, the check keeps blocking.
- A change that removes a check, or stops it from running for this pull request, fails the summary check with **Run creation failed**.
- A change that leaves no presubmit checks fails the same way when the base branch has any.

Refer to [Change checks in a pull request](/chainguard/checks/github/#change-checks-in-a-pull-request).

### Rings {#rings}

Chainguard Checks places each run in a *ring*, based on the `trust` section on your default branch:

| Ring | Runs in the ring |
| -- | -- |
| `2` | Runs after merging, on your default branch |
| `1.<subring>` | Pull requests opened by an account in one of the subring's `authors` groups |
| `0` | Every other pull request, including pull requests from forks by anyone outside your subrings |

An identity's `ring` is the lowest ring that gets the identity. Only the account that opened the pull request counts: who pushed its commits, who reviewed it, and whether it comes from a fork don't change the ring. Without a `trust` section, every open pull request whose base branch an identity allows gets that identity, including pull requests from forks, which run without approval. Refer to [Limit which pull requests get an identity](/chainguard/checks/identity-and-trust/#limit-which-pull-requests-get-an-identity).

## Run lifecycle {#run-lifecycle}

A *run* is one pass of a repository's checks for one commit. The following table follows a pull request run from start to finish:

| Stage | What happens | What can end the run here |
| -- | -- | -- |
| 1. Event | GitHub tells Chainguard Checks, through the Chainguard App, that a pull request was opened, reopened, or updated. | Pushes to other branches, tags, and closed pull requests start no run. |
| 2. Test merge | Chainguard Checks merges the pull request into the latest commit on its base branch. The merge commit exists only in the run, never on GitHub. | Conflicts, which Chainguard Checks can find where GitHub finds none, fail the summary check with **Merge conflict with the base branch**. A pull request past the merge's size limits fails with **Too large to merge**. Refer to [The summary check reports a merge conflict](/chainguard/checks/troubleshooting/#the-summary-check-reports-a-merge-conflict). |
| 3. Plan | Chainguard Checks reads the configuration from the merge commit, applies the base branch's rules, and selects the checks that this change runs. | An invalid configuration fails with **Invalid config**. A change that weakens its own gate, or that changes 3,000 or more files, fails with **Run creation failed**. |
| 4. Admission | Chainguard Checks admits the run only if Chainguard Checks is turned on for the organization and the organization is within its limits. | Chainguard Checks isn't turned on for the organization, or the organization is at its run limit, such as 10 runs queued or running with the Starter allowance. Either way, no summary check appears. The summary check fails with **Run creation failed** when the organization has used up its monthly compute allowance or hasn't accepted the terms. |
| 5. Checks | Each selected check runs in its own fresh VM, after the checks it `needs`. Before a check gets a workload identity, Chainguard Checks verifies again, against GitHub, that the pull request is still open at the head and base this run tests, and that the base branch allows the identity for this check. A check that can't finish for a reason outside the check, such as a VM that doesn't start, runs again in a new VM, up to three attempts in all. | A check fails, times out, is stopped by `policy: destroy`, or doesn't get the workload identity it requests. |
| 6. Summary | A check that doesn't pass, or that reports errors, warnings, notices, or a summary, gets a GitHub check named `presubmit / <file> / <check>` when it finishes. The summary check, **Chainguard Checks (presubmit)**, lists every check and passes only when every blocking check passes. | |

A new push to the pull request cancels the current run and starts a new one at stage 1. After a change merges, each new commit on your default branch gets its own run in ring `2`, which reports **Chainguard Checks (postsubmit)**. Refer to [Use Chainguard Checks on GitHub](/chainguard/checks/github/).

## Session lifecycle {#session-lifecycle}

A session moves through the following states:

| State | What it means | What moves it on |
| -- | -- | -- |
| Creating | `chainctl develop` creates the VM, syncs your directory into `/work`, and installs the session's packages. | When it's ready, your terminal attaches. |
| Attached | Your terminal is connected to the session's shell. `chainctl` answers the requests that use your laptop's credentials, and sends your Claude and Google Cloud credentials to the session's host. For a session that uses a Claude login Chainguard holds for you, `chainctl` sends nothing for Claude. | When you detach, the session keeps running. **Park now** in the session menu parks it right away. |
| Running, detached | The session keeps running, and an agent in it can keep working. It still uses compute. | The session keeps running while it's busy, such as during a build, a Claude Code turn, a `run-ci` run, or a `busy` command, and parks after it's been idle for 10 minutes, no later than 24 hours after you last detach. A time you chose with **Detach — keep running** or `--keep` keeps it running until then, and then while it's busy. A `--keep park` session parks about 10 minutes after you detach, busy or not, and a `--keep always` session parks 7 days after you last detach. Attaching again returns it to attached. |
| Parked | Chainguard saves the session's memory and disk to a snapshot and stops the VM, so it uses no compute. The host discards the credentials `chainctl` sent it. | Attaching resumes it from the snapshot in seconds, with processes, files, and shell as you left them. When the session resumes, Chainguard sends the host fresh access tokens from a Claude login it holds for you, without waiting for you to attach. Five days after parking, it expires. |
| Expired | Chainguard discards the VM and the snapshot. The session can't be resumed, but it stays in `chainctl develop list --expired`, and its name stays in use. | `chainctl develop delete` removes it. |

A session's VM runs for up to 6 days without parking. Then Chainguard parks the session and resumes it on a new host, the same way the session menu's **Restart the host** option does, so a session in long use isn't cut off. If you're attached, the park waits until you detach, and if your organization's monthly allowance is used up, the session stays parked.

You can delete a session in any state. Anything you didn't push is lost. A parked session counts toward your session limit until it expires or you delete it. Refer to [Manage Chainguard Workspaces sessions](/chainguard/workspaces/manage-sessions/).

## Glossary {#glossary}

**Chainguard App**
: The GitHub App that you install on your GitHub organization or personal account. It delivers pull request events to Chainguard Checks, and by default it fetches and pushes a session's repository.

**Chainguard Develop**
: A separate GitHub App, `chainguard-develop`. After you connect your GitHub account with `chainctl develop github login`, the sessions you create act on GitHub as you through this app instead of through the Chainguard App.

**Check**
: One named entry under `checks` in a configuration file, such as `.chainguard/ci.yaml` or a file in `.chainguard/ci/`. Refer to [How results appear](/chainguard/checks/github/#how-results-appear) for how it reports on GitHub.

**Park**
: To save a session's memory and disk to a snapshot and stop its VM. A parked session resumes where it left off.

**Ring**
: The trust level of a run: `2` for runs after merging, `1.<subring>` for pull requests from accounts you trust, and `0` for every other pull request. Rings decide which runs get workload identities and caches.

**Run**
: One pass of a repository's checks for one commit: a pull request's test merge commit, or a new commit on your default branch. Each run reports one summary check. The word also appears in messages such as **Run creation failed** and in capability names such as `sandbox.run.list`.

**Session**
: A Linux microVM in Chainguard's cloud that `chainctl develop` opens, with your repository at `/work`.

**Variation**
: One entry in a check's `foreach` list. Each variation runs in its own VM, and all of a check's variations report as one GitHub check.

**Workload identity**
: Short-lived credentials that Chainguard Checks gives a check while it runs, for Google Cloud, AWS, Azure, or Chainguard. Sessions don't get them.

Several names in `chainctl` and in the configuration don't match the product names:

| Name | What it is |
| -- | -- |
| `sandbox.user` | The IAM role that lets a member use both Chainguard Checks and Chainguard Workspaces. |
| `CHAINCTL_SANDBOX_GROUP` | An environment variable that sets the default organization or folder for `chainctl develop --parent`. |
| `::sandbox-summary::` | A line that a check prints to start a Markdown summary on its GitHub check. `::end-sandbox-summary::` ends it. |
