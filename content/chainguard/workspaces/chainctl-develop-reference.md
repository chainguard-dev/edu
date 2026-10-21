---
title: "chainctl develop command reference"
linktitle: "chainctl develop reference"
description: "Reference for the chainctl develop commands that open and manage Chainguard Workspaces sessions, with their flags, output formats, exit codes, and the roles they need."
type: "article"
date: 2026-10-12T00:00:00+00:00
lastmod: 2026-10-20T15:35:02+00:00
draft: false
tags: ["Chainguard Workspaces", "chainctl", "Reference"]
images: []
menu:
  docs:
    parent: "workspaces"
toc: true
weight: 65
---

The `chainctl develop` command opens and manages Chainguard Workspaces sessions. This page lists each `chainctl develop` command, with its flags, output formats, exit codes, and the roles it needs. For how the commands fit together, refer to [Manage sessions](/chainguard/workspaces/manage-sessions/).

{{% blurb/hidden-chainctl-commands %}}

To read the help for the version you have installed, run `chainctl develop --help`, or add `--help` to any command on this page. You can shorten `chainctl develop` to `chainctl dev`. If `chainctl` doesn't recognize a command or flag on this page, [update chainctl](/platform/chainctl-usage/how-to-install-chainctl/#updating-chainctl).

The examples on this page use `$ORGANIZATION` for the name of your Chainguard organization. If you belong to only one organization, you can omit `--parent`.

## Commands

| Command | What it does |
| ------- | ------------ |
| [`chainctl develop`](#chainctl-develop) | Opens a session, or returns to one. |
| [`chainctl develop list`](#chainctl-develop-list) | Lists your sessions. |
| [`chainctl develop rename`](#chainctl-develop-rename) | Renames a session. |
| [`chainctl develop delete`](#chainctl-develop-delete) | Deletes a session. |
| [`chainctl develop check`](#chainctl-develop-check) | Runs your repository's checks in a session. |
| [`chainctl develop creds`](#chainctl-develop-creds) | Shows or changes what a session can reach. |
| [`chainctl develop github`](#chainctl-develop-github) | Connects your GitHub account to the sessions you create. |
| [`chainctl develop claude`](#chainctl-develop-claude) | Lets Chainguard hold a Claude login for your sessions. |
| [`chainctl develop policy`](#chainctl-develop-policy) | Shows or changes your organization's GitHub policy for sessions. |
| [`chainctl develop init`](#chainctl-develop-init) | Signs you up and turns on Chainguard Checks and Chainguard Workspaces. |
| [`chainctl develop accept-terms`](#chainctl-develop-accept-terms) | Accepts the terms that Chainguard Workspaces is offered under. |

## Flags for every command

Every `chainctl develop` command accepts the following flags:

| Flag | Description |
| ---- | ----------- |
| `--parent` | The organization or folder, by name or ID, that holds the sessions. Defaults to the `CHAINCTL_SANDBOX_GROUP` environment variable, then to the `default.group` value in your `chainctl` configuration. If none of these is set and you belong to one organization, `chainctl` uses it. If you belong to several, it asks which one, or lists them and fails when it can't ask. `chainctl develop init` handles `--parent` differently, as described in [`chainctl develop init`](#chainctl-develop-init). |
| `--non-interactive` | Never prompts. Where `chainctl` would ask a question, such as which of several matching sessions you mean, it fails and lists the choices instead. |
| `-o`, `--output` | The output format, for the commands listed in [Output formats](#output-formats). |

## Session arguments

Commands that take a `SESSION` argument accept any of the following:

- The session's name, such as `app/quiet-harbor`, or the name with the repository's GitHub owner in front, such as `acme/app/quiet-harbor`, as `chainctl develop list` shows it.
- The session's short ID, such as `3f9a2c1e`.
- A directory or a repository URL, if exactly one of your sessions matches it.

If several of your sessions match, `chainctl` asks which one you mean, or lists them and fails when it can't ask. Commands find only your own sessions.

## chainctl develop

Opens a session and attaches your terminal to its shell. If one of your sessions already matches the argument, `chainctl develop` returns to it instead, resuming it first if it's parked.

```
chainctl develop [DIR|REPO|SESSION] [flags]
```

The argument is a directory, a repository URL, or a session. Without one, `chainctl develop` uses the current directory. Refer to [How chainctl develop chooses a session](/chainguard/workspaces/manage-sessions/#how-chainctl-develop-chooses-a-session) for what each one opens.

| Flag | Description |
| ---- | ----------- |
| `--new` | Opens a new session even if one already matches the directory or repository. |
| `--name` | Sets the second part of a new session's name, such as `scratch` in `app/scratch`. Without it, `chainctl` generates one. |
| `--env` | Sets a new session's environment: the path to a file, `default`, or `generate`. Refer to [How a session chooses its environment](/chainguard/workspaces/session-environment/#how-a-session-chooses-its-environment). |
| `--check` | Gives a new session the environment and network access of a check. From a local directory, the check must be in `.chainguard/ci.yaml`. From a repository URL, it can also be in the `.chainguard/ci/` directory. Refer to [How a session chooses its environment](/chainguard/workspaces/session-environment/#how-a-session-chooses-its-environment). |
| `--cache` | For a session opened from a repository URL, mounts the Go build cache that your checks keep for your default branch. Refer to [Start with a warm Go build cache](/chainguard/workspaces/session-environment/#start-with-a-warm-go-build-cache). |
| `--with` | Gives a new or existing session access beyond its defaults. Repeat the flag or separate entries with commas. Refer to [Allow access ahead of time](/chainguard/workspaces/credentials/#allow-access-ahead-of-time) for the entries. |
| `--keep` | Sets how the session keeps running when you detach. Without it, a new session keeps running while it's busy and parks after it's been idle for 10 minutes, no later than 24 hours after you last detach. A duration of up to `24h`, such as `8h`, keeps the session running for that long when you detach. With `always`, creates a session that keeps running instead of parking. With `park`, creates a session that parks about 10 minutes after you detach, busy or not. Refer to [Keep a session running while you're away](/chainguard/workspaces/manage-sessions/#keep-a-session-running-while-youre-away). |
| `--git-remote` | For a directory, the git remote whose GitHub repository a new session is on, or `-` for no repository. Refer to [Choose the session's repository](/chainguard/workspaces/manage-sessions/#choose-the-sessions-repository). |
| `-o json` | Prints the session as JSON instead of attaching to it, and creates the session first if none matches. Refer to [Use sessions from scripts](/chainguard/workspaces/manage-sessions/#use-sessions-from-scripts). |

The `--name`, `--env`, `--check`, `--cache`, `--keep always`, and `--keep park` flags each open a new session, so you don't need `--new` with them, and you can't combine them with a session name.

In a checkout of a repository named `app`, this example opens a new session named `app/scratch` with the default environment:

```shell
chainctl develop --env default --name scratch --parent $ORGANIZATION
```

## chainctl develop list

Lists your sessions that haven't expired, most recently used first, with each session's branch, state, and when you last used it. Alias: `ls`.

```
chainctl develop list [--all] [--expired] [-o json|table|wide]
```

| Flag | Description |
| ---- | ----------- |
| `-a`, `--all` | Lists every user's sessions in the organization, with an `OWNER` column. Needs the `owner` role, as described in [Roles](#roles). |
| `--expired` | Also lists your expired sessions. |
| `-o wide` | Adds each session's commit, environment, and directory, in the `HEAD`, `ENV`, and `DIRECTORY` columns. |

For example output, refer to [List sessions](/chainguard/workspaces/manage-sessions/#list-sessions).

## chainctl develop rename

Replaces the second part of a session's name. The repository part stays the same. Alias: `mv`.

```
chainctl develop rename SESSION NAME [-o json]
```

This example renames `app/quiet-harbor` to `app/tests`:

```shell
chainctl develop rename app/quiet-harbor tests --parent $ORGANIZATION
```

## chainctl develop delete

Destroys a session's VM and its snapshot, after asking you to confirm. Anything in the session that you didn't push is lost. For an expired session, the command removes it from `chainctl develop list --expired` and frees its name. Alias: `rm`.

```
chainctl develop delete SESSION [--yes] [-o json]
```

| Flag | Description |
| ---- | ----------- |
| `-y`, `--yes` | Deletes the session without asking you to confirm. |

This example deletes `app/scratch` without asking:

```shell
chainctl develop delete app/scratch --yes --parent $ORGANIZATION
```

## chainctl develop check

Runs the checks in a session's working tree, in the session's own environment, and streams each step's output to your terminal. If the session is parked, `chainctl` resumes it first. The command uses the same runner as the `run-ci` command in a session.

```
chainctl develop check SESSION [--check CHECK] [-o json]
```

| Flag | Description |
| ---- | ----------- |
| `--check` | Runs only the named check. Without it, `chainctl` runs every check that has a command, in the order your configuration lists them, and stops at the first failure. |
| `-o json` | Prints the result as JSON on standard output, and sends the steps' output to standard error. |

This example runs the `test` check in `app/quiet-harbor`:

```shell
chainctl develop check app/quiet-harbor --check test --parent $ORGANIZATION
```

For which checks the command skips, and how its result compares with a pull request's, refer to [Run checks in a session from your laptop](/chainguard/checks/run-checks/#run-checks-in-a-session-from-your-laptop).

## chainctl develop creds

Shows what a session can reach, or changes it.

```
chainctl develop creds SESSION [--revoke ENTRY]... [--source SERVICE=SOURCE]... [--forget] [-o json|table]
```

Without flags, the command lists each service's source and bindings, what your laptop remembers approving, what serves the session's laptop credentials right now, and the latest changes to the session's credentials.

| Flag | Description |
| ---- | ----------- |
| `--revoke` | Takes an entry back from the session and from your laptop's remembered approvals. Repeatable. |
| `--source` | Sets where a service's credential comes from: `laptop`, `org`, `owner`, or `off`. Repeatable. |
| `--forget` | Removes everything your laptop remembers for the session's repository, without changing the session. |

To add access, run `chainctl develop SESSION --with ENTRY` instead. Refer to [Review and revoke a session's credentials](/chainguard/workspaces/credentials/#review-and-revoke-a-sessions-credentials) for the entries and sources that each service takes.

This example takes back a session's access to `cgr.dev`:

```shell
chainctl develop creds app/quiet-harbor --revoke cgr.dev --parent $ORGANIZATION
```

## chainctl develop github

Connects your GitHub account so that the sessions you create act on GitHub as you, through the Chainguard Develop GitHub App. Refer to [Let sessions act on GitHub as you](/chainguard/workspaces/github-as-you/).

```
chainctl develop github login [--port PORT] [-o json]
chainctl develop github logout
chainctl develop github status [-o json|table]
```

| Command | What it does |
| ------- | ------------ |
| `login` | Opens your browser to connect your GitHub account, replacing any earlier connection. The `--port` flag sets the local port that your browser returns to after you authorize the connection. |
| `logout` | Disconnects your GitHub account. Sessions that act on GitHub as you refuse `git` and `gh` requests until you connect again. |
| `status` | Shows your connected GitHub account, the app it's connected through, whether the connection works, whether your organization's policy allows sessions to act as you, and which accounts the checkout in your current directory still needs the app installed on. |

## chainctl develop claude {#chainctl-develop-claude}

Lets Chainguard hold a Claude login for your sessions, so that Claude Code in them works whether or not you're attached. One login serves your sessions in every organization, except sessions that use Vertex AI. Refer to [Let Chainguard hold your Claude login](/chainguard/workspaces/coding-agents/#let-chainguard-hold-your-claude-login).

```
chainctl develop claude login [-o json]
chainctl develop claude status [-o json|table]
chainctl develop claude logout
```

| Command | What it does |
| ------- | ------------ |
| `login` | Opens your browser to log in to Claude, and asks you to paste the code that the page shows. Chainguard then holds the login for about 4 weeks. A new login replaces the earlier one and revokes it. |
| `status` | Shows the login's Claude account, its Claude organization, whether it still works, and when it ends, in the `CLAUDE ACCOUNT`, `ORGANIZATION`, `STATE`, and `EXPIRES` columns. |
| `logout` | Revokes the login at Anthropic, which ends it in every session at once, and has Chainguard forget it. Sessions that use it refuse Claude Code's requests until you log in again. If Chainguard can't reach Anthropic, it keeps the login, and `logout` says so. In that case, run `chainctl develop claude logout` again. |

## chainctl develop policy

Shows or changes your organization's GitHub policy for sessions. Alias: `policies`.

```
chainctl develop policy describe [-o json|table]
chainctl develop policy set [--org-github bound|session|off] [--org-github-push-beyond-session=true|false] [--user-github=true|false] [-o json|table]
```

The `describe` command, with the aliases `desc` and `get`, shows the policy, its revision, and who last changed it. The `set` command changes only the settings you pass, and needs the `owner` role. Refer to [Set your organization's GitHub policy](/chainguard/workspaces/credentials/#set-your-organizations-github-policy) for what each setting controls.

This example limits the Chainguard App to each session's own repository:

```shell
chainctl develop policy set --org-github session --parent $ORGANIZATION
```

## chainctl develop init {#chainctl-develop-init}

Signs you in, creates a Chainguard Starter organization or picks one you belong to, and turns on Chainguard Checks and Chainguard Workspaces with a free monthly allowance. Run it in an interactive terminal.

```
chainctl develop init [--parent ORGANIZATION] [--github-org ACCOUNT] [--name NAME] [--port PORT]
```

| Flag | Description |
| ---- | ----------- |
| `--github-org` | The GitHub organization to link, instead of your own GitHub user. |
| `--parent` | An existing organization, such as an Enterprise organization, to turn on Checks and Workspaces for. You need the `owner` or `limited_owner` role in it. |
| `--name` | Has no effect, because an organization you create is named after your work email domain. You can't combine it with `--parent`. |
| `--port` | The local port that your browser returns to after you authorize the GitHub link. |

Without `--parent`, the command creates a Starter organization if you don't belong to any organization, and uses your organization on the Starter or Team plan if you have exactly one. Otherwise, it fails and asks you to pass `--parent`. Unlike the other commands, it doesn't fall back to the `default.group` value in your `chainctl` configuration.

For what the command asks as it runs, refer to [Sign up with chainctl develop init](/get-started/checks-and-workspaces/set-up/#sign-up-with-chainctl-develop-init).

## chainctl develop accept-terms {#chainctl-develop-accept-terms}

Accepts the Secured Platform Terms and the Master Service and License Agreement (MSLA) for an organization. Chainguard Workspaces refuses to open sessions in an organization until it accepts them. Someone with the `owner` or `limited_owner` role runs the command once, and running it again changes nothing.

```
chainctl develop accept-terms [--parent ORGANIZATION] [--yes]
```

| Flag | Description |
| ---- | ----------- |
| `--yes` | Accepts the terms without asking, such as where no interactive terminal is available. Passing it means you agree to the statement in `chainctl develop accept-terms --help`, which the command also prints. |

An organization that already has Workspaces through your Chainguard account team must accept the terms before anyone can open new sessions in it. Running `chainctl develop init --parent $ORGANIZATION` accepts them, turns on Checks, and keeps the allowance your account team arranged. To accept only the Workspaces terms, run `chainctl develop accept-terms` instead:

```shell
chainctl develop accept-terms --parent $ORGANIZATION
```

If you accept only the Workspaces terms and your GitHub account isn't linked to the organization yet, link it as described in [Getting started with Guardener](/chainguard/guardener/github/getting-started/#step-2-link-your-chainguard-organization-to-github), which uses the same Chainguard App.

## Output formats

Each command accepts only the following output formats:

| Command | Formats | JSON output |
| ------- | ------- | ----------- |
| `chainctl develop` | `json` | The session. `chainctl` doesn't attach. |
| `list` | `table` (default), `wide`, `json` | An array of sessions. |
| `rename` | `json` | The renamed session. |
| `delete` | `json` | The deleted session, with `"deleted": true`. |
| `check` | `json` | The result: `passed`, `jobs` (the checks that ran), `failed_job` and `failed_step` for a failure, `skipped`, and `elapsed`. |
| `creds` | `table` (default), `json` | `sources`, with each service's `source` and `bindings`; `serving`, what serves the session's laptop credentials; and `trail`, the latest changes. |
| `github login` | `json` | The connected account, in the same form as `github status`. |
| `github status` | `table` (default), `json` | `login`, `valid`, `user_github`, `installed_accounts`, and `app_slug`. |
| `claude login` | `json` | The login, in the same form as `claude status`. |
| `claude status` | `table` (default), `json` | `supported`, `enrolled`, `email`, `organization`, `organization_uuid`, `valid`, and `expires`. |
| `policy describe`, `policy set` | `table` (default), `json` | The policy. |

A session in JSON output includes its `name`, such as `app/quiet-harbor`; its `label`, the name with the repository's GitHub owner in front; its `id` and `short_id`; its `state`, `repository`, `branch`, `head`, and `directory`; how it keeps running after you detach, in `idle` (`auto_hold` or `keep_running`), `keep_running_until`, `held_until`, and `last_busy`; and timestamps such as `create_time` and `expire_time`. Fields without a value are left out.

## Exit codes

| Command | Exit code |
| ------- | --------- |
| `chainctl develop` | When you exit the session's shell, such as with `exit`, the shell's exit status. Otherwise, `0` when you detach and `1` when the command fails. |
| `chainctl develop check` | `0` when every check passes, and `1` when a check fails or the checks can't run. |
| Every other command | `0` when the command succeeds, and `1` when it fails. |

## Roles {#roles}

What you can do with `chainctl develop` depends on your role in the session's organization:

| Commands | Roles |
| -------- | ----- |
| `chainctl develop`, `list`, `rename`, `delete`, `check`, `creds`, `github`, `claude`, and `policy describe` | `owner`, `limited_owner`, or `sandbox.user` |
| `accept-terms` | `owner` or `limited_owner` |
| `list --all` and `policy set` | `owner` |

The `limited_owner` role is the one that `chainctl develop init` gives the person who creates a Starter organization. No one in a Starter organization has the `owner` role, so no one there can run `list --all` or `policy set`. On their own, other roles, such as `editor` and `viewer`, can't open or manage sessions. To run `chainctl develop init --parent` on an organization you already belong to, you need the `owner` or `limited_owner` role in it. An organization owner can grant the `sandbox.user` role with an invite, as described in [Give teammates access](/get-started/checks-and-workspaces/set-up/#give-teammates-access).

In a session, your role also limits what your Chainguard identity can do. The `limited_owner` role doesn't include `mcp.tool.call` or `sandbox.run.list`, so the Chainguard MCP servers and the `chainctl checks` commands that look up a run don't work for it. Refer to [MCP servers in a session](/chainguard/workspaces/coding-agents/#mcp-servers-in-a-session) and [Your Chainguard identity in a session](/chainguard/workspaces/credentials/#your-chainguard-identity-in-a-session).

## Environment variables and configuration

| Name | What it sets |
| ---- | ------------ |
| `CHAINCTL_SANDBOX_GROUP` | The default for `--parent`. |
| `CHAINCTL_DEVELOP_CACHE` | With `true`, new sessions ask for the Go build cache, as `--cache` does. Unlike `--cache`, it doesn't make `chainctl develop` open a new session. Refer to [Start with a warm Go build cache](/chainguard/workspaces/session-environment/#start-with-a-warm-go-build-cache). |
| `default.group` | The `chainctl` configuration value that `--parent` falls back to when `CHAINCTL_SANDBOX_GROUP` isn't set. The `CHAINGUARD_DEFAULT_GROUP` environment variable also sets it. |
| `develop.vertex.project`, `develop.vertex.region` | The Google Cloud project and region that new sessions use for Claude through Vertex AI. Refer to [Use Claude through Vertex AI](/chainguard/workspaces/coding-agents/#use-claude-through-vertex-ai). |
