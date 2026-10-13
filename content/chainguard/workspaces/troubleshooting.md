---
title: "Troubleshoot Chainguard Workspaces"
linktitle: "Troubleshooting"
description: "Fix common problems with Chainguard Workspaces, including sign-up failures, permission errors, sessions that won't open, Claude Code errors, failed pushes, and usage limits."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-13T00:00:00+00:00
draft: false
tags: ["Chainguard Workspaces", "Troubleshooting"]
images: []
menu:
  docs:
    parent: "workspaces"
    identifier: "Workspaces Troubleshooting"
toc: true
weight: 70
---

This page describes common problems with Chainguard Workspaces sessions and how to fix them. If your problem isn't listed here, ask in the #workspaces-questions channel in the [Chainguard community Slack](https://join.slack.com/t/chainguardcommunity/shared_invite/zt-3nttdr807-V9BJHayWvsB0KbHsfZO5Rw).

## chainctl doesn't list the develop command

During the beta, `chainctl develop` doesn't appear in `chainctl --help` or in the [chainctl reference](/platform/chainctl/chainctl-docs/chainctl/). You can still run it, and `chainctl develop --help` shows its full help. For each subcommand and its flags, refer to the [`chainctl develop` reference](/chainguard/workspaces/chainctl-develop-reference/). The `chainctl checks` commands are hidden the same way, and the [`chainctl checks` reference](/chainguard/checks/chainctl-checks-reference/) describes them.

If `chainctl` reports that `develop` is an unknown command, or doesn't recognize a flag or subcommand on this site, your `chainctl` is out of date. Update it with `sudo chainctl update`, or with `brew upgrade chainctl` if you installed it with Homebrew.

## chainctl develop init fails

If `chainctl develop init` stops with an error, find its message in the following list. Replace `$ORGANIZATION` with the name of your Chainguard organization.

- `this identity is not eligible for a self-serve Starter organization`: run `chainctl develop init` again and, in your browser, sign in with an email address and password or with Google. Other sign-in methods, such as GitHub, can't create a Starter organization. If you already signed in one of those ways, [contact Chainguard](https://www.chainguard.dev/contact?utm=docs).
- `unable to create self-serve organization`: most often, your email domain already has a Chainguard organization. Ask one of its owners to invite you. If that organization is on the Starter or Team plan, you can also run `chainctl starter request-access` to send its owners a request.
- `you belong to several organizations, or none on the Starter or Team plan`, or `you already belong to an organization`: run the command again with `--parent $ORGANIZATION`, and without `--name`, to choose the organization where you turn on Checks and Workspaces.
- `missing: terms.accept`: only the `owner` and `limited_owner` roles can turn on Checks and Workspaces. Ask someone with one of those roles to run `chainctl develop init --parent $ORGANIZATION`.
- `creating a Starter organization asks a few questions about you`, or `accepting the required legal agreements needs an interactive terminal`: run the command in an interactive terminal, without `--non-interactive`.
- `This organization can't use self-serve Checks and Workspaces`, or `Checks and Workspaces were turned off for this organization`: [contact Chainguard](https://www.chainguard.dev/contact?utm=docs).
- `you must own the GitHub account (organization or user)`: link your own GitHub user, or a GitHub organization where you're an owner.

### The GitHub account is linked to another organization

If `chainctl develop init` fails with a message that says the GitHub account or organization you chose is `already linked` to another Chainguard organization, you can't link it until that link is removed, because a GitHub account can be linked to only one Chainguard organization at a time. In `chainctl` 0.2.381 or later, `chainctl develop init` names the account and, in an interactive terminal, asks for a different one to link instead of stopping. Otherwise, do one of the following:

- Run `chainctl develop init` again and link a different GitHub account. The command uses the organization it already created.
- Use the organization that holds the link instead. Have one of its owners run `chainctl develop init --parent $ORGANIZATION`, replacing `$ORGANIZATION` with that organization's name.
- If you own the GitHub account, unlink it from the other organization with `chainctl guardener github unlink --github-org $GITHUB_ACCOUNT`, replacing `$GITHUB_ACCOUNT` with the account's name, and then run `chainctl develop init` again. Unlinking stops Guardener for that account in the other organization.

For more about links, refer to [Managing Chainguard App connections](/chainguard/guardener/github/app-connections/#moving-a-github-organization-to-a-different-chainguard-organization).

## You don't have permission

If a `chainctl develop` command fails with a `PermissionDenied` error that says only `permission denied`, the account you're logged in with doesn't have a role in the organization that allows the command, as described in [Roles](/chainguard/workspaces/chainctl-develop-reference/#roles). Membership alone isn't enough, because the `viewer` and `editor` roles don't include Workspaces. Ask an organization owner to give you access, as described in [Give teammates access](/chainguard/workspaces/getting-started/#give-teammates-access). If you have more than one Chainguard account, run `chainctl auth status` to check which one you're logged in with.

The `chainctl develop list --all` and `chainctl develop policy set` commands need the `owner` role. Without it, `chainctl develop policy set` fails with the same error, and `chainctl develop list --all` fails with an error that says `listing another owner's sessions requires the list capability on the instance`.

## Your organization isn't entitled to Chainguard Workspaces

If `chainctl develop` fails with a `PermissionDenied` error that says `this organization is not entitled to Chainguard Workspaces`, Checks and Workspaces aren't turned on for the organization. Have someone with the `owner` or `limited_owner` role turn them on with the following command, replacing `$ORGANIZATION` with the name of your Chainguard organization:

```shell
chainctl develop init --parent $ORGANIZATION
```

If an owner turned them on a moment ago, wait a minute and try again.

## Your organization hasn't accepted the terms

If `chainctl develop` fails with a `FailedPrecondition` error that says your organization hasn't accepted the terms Chainguard Workspaces is offered under, Chainguard refuses to create sessions in the organization until someone with the `owner` or `limited_owner` role accepts them. The error names the terms. Have someone with one of those roles run the following command, replacing `$ORGANIZATION` with the name of your Chainguard organization:

```shell
chainctl develop accept-terms --parent $ORGANIZATION
```

The acceptance can take up to 30 seconds to take effect, so wait briefly before you try again. Sessions that are already running or parked keep working.

## A session won't open on a directory

If `chainctl develop` refuses to open a directory, the error says why. The following sections describe the most common causes.

### Several sessions match the directory

If a directory has more than one session, `chainctl` asks which one you want, or lists them and fails when it can't ask. Pass the session's name or short ID instead of the directory.

### The repository has no environment

With `--non-interactive`, a repository that has neither a `.chainguard/develop.yaml` file nor a `.chainguard/ci.yaml` file is an error. Pass `--env default` to use the default environment.

### The directory is too large to generate an environment

If `chainctl develop --env generate` fails with an error that says the directory is `larger than the 33554432-byte generation limit`, the files that `chainctl` uploads to generate the environment add up to more than 32 MiB. An error that says the upload `holds more than 50000 files` means that it has too many files. Either way, pass `--env default` or an [environment file of your own](/chainguard/workspaces/session-environment/#use-a-separate-environment-file) instead. To learn which files the upload includes, refer to [Generate an environment](/chainguard/workspaces/session-environment/#generate-an-environment).

### The directory is the top of a linked worktree or submodule

If `chainctl develop` fails with an error that says `the checkout's .git is a pointer to a git directory elsewhere`, the directory is the top of a linked worktree, which `git worktree add` creates, or of a submodule. Its history is stored outside the directory, so `chainctl` can't sync it. Run `chainctl develop` from the main checkout instead. A session opened there gets each submodule as an empty directory.

From a subdirectory of a linked worktree or submodule, `chainctl` syncs only that subdirectory, without the repository's history.

## You reached the session limit

With the free monthly allowance, each user can have one session at a time, including a parked one, and the organization can have three. A parked session counts toward both limits until you delete it or it expires. At a limit, `chainctl develop` fails with a `ResourceExhausted` error:

- If the error says `you are at your limit of 1 active sessions in this organization`, delete a session you no longer need with `chainctl develop delete`, or return to the one you have.
- If the error says `this organization is at its active-session capacity (3)`, other users hold the organization's sessions. Only the user who created a session can delete it with `chainctl develop delete`, so ask your teammates to delete the sessions they no longer need. If you have the `owner` role, `chainctl develop list --all` shows every user's sessions with an `OWNER` column. In a Starter organization, no one can list other users' sessions, as described in [Roles](/chainguard/workspaces/chainctl-develop-reference/#roles).

## A session fails to start because of a package

If a session fails to start with an error about a package, such as `nothing provides` followed by a package name, the session's environment lists a package that doesn't exist or that your organization can't access. Check the package names in the file the environment comes from, such as `.chainguard/develop.yaml`, `.chainguard/ci.yaml`, or your `--env` file. Package names often include a version, such as `go-1.24` or `python-3.13`.

## A session asks for more resources than your organization allows

If a session fails with an error that says the environment's guest is `larger than this organization's largest resource class`, the session's environment asks for more vCPUs, memory, or disk than your organization allows. The error names what the environment asks for and your organization's limit. Choose a smaller size in the environment's `resources`, as described in [Resources](/chainguard/workspaces/session-environment/#resources), or [contact Chainguard](https://www.chainguard.dev/contact?utm=docs).

## Changes on your laptop don't appear in the session

This is expected. Your directory syncs into a session only the first time you attach. After that, changes on your laptop don't reach the session, and changes in the session don't reach your laptop. Commit and push from the session, then pull on your laptop, or the other way around.

To start a session from your laptop's current tree, open a new one with `chainctl develop --new`.

## Claude Code reports an error in the session

Most errors mean that the session doesn't have a current Claude credential. For how long a session keeps the credential that `chainctl` sends, refer to [Keep Claude Code working while you're away](/chainguard/workspaces/coding-agents/#keep-claude-code-working-while-youre-away). Claude Code shows the error in the session, and `chainctl` prints messages about the credential on your laptop. To review those messages later, press `Ctrl+]` to open the session menu and choose **Logs**.

The following sections describe the most common causes.

### No credential has arrived

If the error says that `none has arrived`, the session has no Claude credential. Claude Code might show only a `503` error. Update `chainctl` to version 0.2.380 or later, run `claude` on your laptop and log in, and then attach to the session with `chainctl develop`. If you use Claude through Vertex AI, run `gcloud auth application-default login` on your laptop instead of logging in to Claude.

### The session's host is too old

If the error says that the session's host `predates laptop credential push`, or `chainctl` says that the session's host was started before it could send model credentials, the host can't take a credential. Attach to the session with a current `chainctl`, press `Ctrl+]`, and choose **Restart the host**. You can also detach, let the session park, and attach again.

### The credential sent to the session expired

If the error says that `the owner's Claude login token sent to this session expired`, the short-lived access token from your stored Claude login ran out. `chainctl` renews it while you're attached, and while a terminal that you detached from with a **Detach — keep running** option stays open. Attach again to send a fresh one.

To keep a long unattended task from stopping, use a token from `claude setup-token`, as described in [Keep Claude Code working while you're away](/chainguard/workspaces/coding-agents/#keep-claude-code-working-while-youre-away).

If you use Claude through Vertex AI, the error says instead that your Google credential or access token sent to the session for Vertex AI no longer works or expired. Attach again to send a fresh one.

### Claude Code uses a different provider

If the error says that `claude in this session now uses` Vertex AI or the Anthropic API, the session's Claude provider changed while Claude Code was running. Exit Claude Code and run `claude --continue` to resume the conversation.

### Claude is turned off for the session

If the error says that `claude is turned off for this session`, the session's `claude` credential is turned off. Turn it back on with the command that the error names. Replace `$SESSION` with the session's short ID, which the error includes:

```shell
chainctl develop creds $SESSION --source claude=laptop
```

### Your Claude login expired

If `chainctl` says that `your Claude login on this laptop` expires soon or has expired, run `claude` on your laptop once to refresh it. `chainctl` sends the refreshed login while you're attached. If you're detached, attach to the session again.

### You aren't logged in to Claude

If `chainctl` says `claude: nothing to send` when you attach, it found no Claude login or Google credentials on your laptop. Run `claude` on your laptop and log in, or run `gcloud auth application-default login` if you use Claude through Vertex AI. `chainctl` tries again while you're attached.

### Claude Code isn't installed in the session

If `claude` isn't found in the session, the session's environment doesn't list it. Add `claude` to your environment's packages and open a new session, or open one on the default environment with `--env default`.

## A push or fetch fails in the session

If `git push` or `git fetch` fails with a message that the org GitHub App can't serve the repository because it's not installed or not linked, the Chainguard App isn't installed on the GitHub account that owns the repository, or that account isn't linked to your organization. Install the app from the [Chainguard App installation page](https://github.com/apps/chainguard/installations/new), selecting every account you work in. Then allow the repository, replacing `$OWNER` and `$REPO` with its owner and name:

```shell
chainctl develop --with github:$OWNER/$REPO --parent $ORGANIZATION
```

If the message says the request isn't allowed for the session yet, that the session owner declined it, or that nobody answered within 60 seconds, the session asked for access beyond its defaults and nobody approved it. Approve it on your attached terminal when the prompt appears, or allow it ahead of time with `--with`. Refer to [Manage session credentials](/chainguard/workspaces/credentials/).

Pushing from the session over SSH doesn't work. The session rewrites only `https://github.com/` URLs, so keep your remotes on HTTPS.

### The branch requires signed commits

Commits that you make in a session aren't signed. If a GitHub rule requires signed commits on the branch that you push to, GitHub rejects the push. To get the commits onto that branch, push them to a branch that the rule doesn't cover, sign them on your laptop, and then merge them as you usually do:

1. In the session, create a branch and push it, replacing `$BRANCH` with a name that the rule doesn't cover:

   ```shell
   git switch -c $BRANCH
   git push origin $BRANCH
   ```

2. On your laptop, check out the branch, sign each of its commits, and push it again. If the session started from a branch other than `main`, replace `main` with that branch's name:

   ```shell
   git fetch origin
   git switch $BRANCH
   git rebase --exec 'git commit --amend --no-edit -S' origin/main
   git push --force-with-lease
   ```

If a rule requires signed commits on every branch, you can't push commits from a session to the repository.

### Find the details in the forwarding log

`chainctl` writes every GitHub and `cgr.dev` request that it serves from your laptop, and every failure, to `develop-forward.log` in its configuration directory on your laptop. On macOS, that's `~/Library/Application Support/chainctl/`. On Linux, it's `$XDG_CONFIG_HOME/chainctl/`, or `~/.config/chainctl/` if `XDG_CONFIG_HOME` isn't set. The log doesn't record Claude requests, because the session's host sends them itself.

## A session that acts as you can't reach a repository

If you connected your GitHub account with `chainctl develop github login`, the sessions you create act on GitHub as you through the Chainguard Develop GitHub App, `chainguard-develop`. This app is separate from the Chainguard App. To fetch a private repository or push to any repository, a session needs Chainguard Develop installed on the account that owns the repository. For how to install it, refer to [Install the Chainguard Develop app](/chainguard/workspaces/github-as-you/#install-the-chainguard-develop-app).

When you open a session from a repository URL, Chainguard checks that your account can reach the repository. If it can't, `chainctl develop` fails with a `FailedPrecondition` error that names one of the following causes and where to fix it:

- Chainguard Develop isn't installed on the account that owns the repository. An owner of that account installs it, and a member can request it, on the [Chainguard Develop installation page](https://github.com/apps/chainguard-develop/installations/new).
- The app's installation hasn't granted it read access to repository contents. An owner of the account accepts the app's requested permissions.
- The organization requires SAML single sign-on. Sign in at the page that the error names, and then run `chainctl develop github login` again.
- Your account can't see the repository through the app. If the app is installed only on selected repositories, an owner of the account adds this one. Otherwise, ask an owner for access.

On a terminal, `chainctl` offers to open the page where you make the fix, waits for you to press `Enter`, and then tries to create the session again.

A session that you open on a directory isn't checked when you create it. Instead, `git fetch` or `git push` fails in the session with a message that begins `GitHub refused the push` or `GitHub refused the fetch` and names the cause and the fix. The fix takes effect at once, so retry the command after you make it. You don't need a new session. To check from inside a session whether your account reaches a repository, run the following command, replacing `$OWNER` and `$REPO` with the repository's owner and name:

```shell
curl -s "http://github/.chainguard/access?repo=$OWNER/$REPO"
```

On your laptop, `chainctl develop github status` shows which accounts the checkout in your current directory still needs the app installed on.

## A session runs out of space or memory

The `/tmp` directory in a session is held in memory and limited to a quarter of the session's memory, which is 4 GB with the default 16 GB. Writing large files there uses memory that your processes need. Put large files under `/var/tmp` or `/work`, which are on the session's disk, 50 GB by default. To change a session's memory or disk, refer to [Resources](/chainguard/workspaces/session-environment/#resources).

## A session started fresh instead of resuming

Rarely, Chainguard can't restore a parked session's snapshot. The session then starts fresh, and `chainctl` says that the parked snapshot couldn't be restored and that uncommitted work was lost. Push your work regularly so that a lost snapshot doesn't cost you much.

## A session has expired

A parked session expires 5 days after it parks, and an expired session can't be resumed. `chainctl develop list --expired` shows your expired sessions. An expired session keeps its name until you delete it, so to reuse the name, delete the expired session with `chainctl develop delete`. Then open a new session with `chainctl develop`.

## Your organization's monthly compute allowance is used up

If `chainctl develop` fails with a `FailedPrecondition` error that says `this month's compute allowance is used up`, your organization has used its monthly vCPU-hours of Workspaces. Until the allowance resets on the first day of the month (UTC), you can't create a session or resume a parked one, and a session created with `--keep always` parks after you detach instead of staying up. Sessions that are already running aren't stopped.

A parked session still expires 5 days after it parks, even if the allowance hasn't reset yet, so push your work regularly. To learn how sessions use the allowance, refer to [Availability and limits](/chainguard/workspaces/overview/#availability-and-limits). To continue before the allowance resets, [contact Chainguard](https://www.chainguard.dev/contact?utm=docs).

## Your organization's access to Chainguard Workspaces ended

If `chainctl develop` fails with a `PermissionDenied` error that says `this organization's access to Chainguard Workspaces has ended`, you can't create sessions, attach to them, or keep them running. You can still list, rename, and delete sessions, and use `chainctl develop creds`, `chainctl develop policy`, and `chainctl develop github`, so you can clean up. To continue, [contact Chainguard](https://www.chainguard.dev/contact?utm=docs).

This happens, for example, when a free trial that your organization started with `chainctl` 0.2.379 or earlier ends. Such a trial includes 500 vCPU-hours of Workspaces over 30 days, followed by a 7-day grace period during which `chainctl` warns you each time you create a session. Its compute budget doesn't reset each month, and when the budget is used up, `chainctl develop` fails with a message that says `compute budget used up`.

## chainctl can't find your session

`chainctl develop list` shows only your own sessions, unless you have the `owner` role and pass `--all`. If you're logged in to `chainctl` with a different account than the one that created a session, `chainctl` reports that no session matches. In some cases, it says instead that you're logged in as one identity but the session belongs to another. Only a session's owner can attach to it. Run `chainctl auth login` and choose the account that owns the session.
