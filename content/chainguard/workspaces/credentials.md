---
title: "Manage Chainguard Workspaces session credentials"
linktitle: "Session credentials"
description: "Learn how a Chainguard Workspaces session reaches GitHub, Claude, and Chainguard without holding credentials, and how to approve, review, and revoke what it can reach."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-08T00:00:00+00:00
draft: false
tags: ["Chainguard Workspaces", "Security", "Configuration"]
images: []
menu:
  docs:
    parent: "workspaces"
toc: true
weight: 50
---

A Chainguard Workspaces session holds no long-lived credentials: its VM stores no API keys, tokens, or registry logins. Instead, the session reaches each service through a local hostname, and the credential is added to the request outside the VM. This page explains what a session can reach by default and how to change it.

## How credentials reach a session

Each service a session can reach has a hostname inside the session, such as `http://github/` or `http://claude/`. Chainguard configures the session to use these hostnames. For example, `git` in the session rewrites `https://github.com/` URLs to `http://github/`, and Claude Code sends its requests to `http://claude/`.

When a request reaches one of these hostnames, `chainctl` on your laptop or Chainguard adds the credential outside the VM. Each credential has a *source*:

| Source | Where the credential comes from |
| ------ | ------------------------------- |
| `laptop` | Your laptop. `chainctl` reads the credential on your laptop and answers the request from there, so the credential never leaves your machine. This works only while your laptop serves the session. |
| `org` | Your Chainguard organization, such as the Chainguard App's access to your GitHub repositories. |
| `seat` | Your Chainguard identity, which your laptop delegates to the session when you attach. Only the `chainguard` service uses this source. |
| `off` | Nothing. The session can't use the service. |

Your laptop serves a session while you're attached to it. If your terminal served a laptop credential while you were attached, it keeps serving after you detach and keep the session running, until you press `Ctrl+C`. If nothing serves a session, requests that need your laptop fail with an error that says no laptop is attached.

## What a session can reach by default

A new session can reach the following services without asking you:

| Service | Default source | What it covers |
| ------- | -------------- | -------------- |
| `claude` | `laptop` | Your Claude Code login, for the Claude API's messages and models endpoints. |
| `github` | `org` | `git` fetch and push for the session's repository, and for your checkout's other github.com remotes where the Chainguard App is installed. |
| `cgr.dev` | `org` | Pulls from `cgr.dev` as the Chainguard platform, not as you, so it can't pull your organization's private images. |
| `chainguard` | `seat` | `chainctl` and the Chainguard Model Context Protocol (MCP) servers in the session act as you, limited to read and MCP capabilities in the session's organization. The delegation lasts while you're attached, and for up to an hour after you detach. |

The GitHub API isn't covered by default. The `gh` CLI is installed in every session, but it has no credential unless your organization has sessions act on GitHub as their owner, as described in [Let sessions act on GitHub as you](#let-sessions-act-on-github-as-you).

## Approve requests from a session

When a session asks for something beyond its defaults, such as fetching a private repository that isn't one of your checkout's remotes, `chainctl` shows a prompt on your attached terminal. The prompt says what the session wants and which credential it would use.

The keys you can press depend on the request:

| Request | Keys |
| ------- | ---- |
| Fetch a repository | `y` approves the request and remembers your approval for the next session on the same repository. `n` declines it. |
| Push to a repository | `p` approves the push for this session only. `n` declines it. |

Pressing `Enter` declines, and so does leaving the prompt unanswered for 60 seconds. To protect you from approving a request by accident, `chainctl` ignores keys for a moment after a prompt appears, and treats a paste as a decline.

If no terminal is attached, a session can't ask you, so it refuses the request. A terminal that keeps serving after you detach also refuses new requests. To allow access ahead of time, use `--with`.

## Allow access ahead of time

The `--with` flag adds access to a session when you create it or return to it. You can repeat the flag or separate entries with commas, and entries add to what the session already has. `chainctl` records each change on the session and remembers it on your laptop for the next session on the same organization and repository.

The `--with` flag accepts the following entries:

| Entry | What it does |
| ----- | ------------ |
| `github:<owner>/<repo>` | Allows fetching another repository. |
| `github:<owner>/<repo>+push` | Allows fetching and pushing to another repository. |
| `github:<owner>/*` | Allows fetching every repository of a GitHub account or organization. |
| `github:*` | Allows fetching any GitHub repository. |
| `claude`, `chainguard` | Turns a default service back on. |
| `cgr.dev` | Pulls from `cgr.dev` as you, with your laptop's `cgr.dev` login. |
| `all` | Restores the defaults and allows fetching any GitHub repository. |
| `none` | Allows only the session's own repository. It can't be combined with other entries. |

For example, this command lets the session push to a second repository, `acme/docs`, in addition to its own:

```shell
chainctl develop --with github:acme/docs+push --parent $ORGANIZATION
```

Wildcard entries allow fetching only. To push to a repository, name it with `+push`. Under your organization's default GitHub policy, the Chainguard App doesn't serve wildcard entries, so they give access to public repositories only. To fetch a private repository, name it.

## Review and revoke a session's credentials

To see what a session can reach, run `chainctl develop creds` with the session's name or short ID:

```shell
chainctl develop creds app/quiet-harbor --parent $ORGANIZATION
```

The output lists each service with its source and any repositories bound to it, what your laptop remembers approving, whether a laptop is serving the session right now, and the most recent changes to the session's credentials. You can see the same list by choosing **Credentials** in the session menu.

To change a session's credentials, pass one or more of the following flags to `chainctl develop creds`:

| Flag | What it does |
| ---- | ------------ |
| `--revoke <entry>` | Takes access back from the session and from your laptop's remembered approvals. `<entry>` is `claude`, `cgr.dev`, `chainguard`, `github:<owner>/<repo>`, or `github:<owner>/<repo>+push`, which takes back only the push. |
| `--source <service>=<source>` | Changes where a credential comes from. `<source>` is `laptop`, `org`, or `off`. The `claude` service takes only `laptop` or `off`, and `chainguard` takes only `off`. To turn `chainguard` back on, use `--with chainguard`. |
| `--forget` | Removes everything your laptop remembers for the session's repository, without changing the session. |

For example, to let a session pull your organization's private images from `cgr.dev` as you, switch the `cgr.dev` credential to your laptop:

```shell
chainctl develop creds app/quiet-harbor --source cgr.dev=laptop --parent $ORGANIZATION
```

Your laptop must have a `cgr.dev` login in its Docker credential helper, which you can set up as described in [Configure a Docker credential helper](/platform/chainctl-usage/how-to-install-chainctl/#configure-a-docker-credential-helper). The session can pull with it, but not push.

Your laptop keeps remembered approvals in `develop/approvals.json` in the `chainctl` configuration directory, readable only by you. The file stores service names, sources, and scopes, never credentials, and Chainguard's servers can't write to it.

## Set your organization's GitHub policy

Your organization's policy controls which repositories the Chainguard App serves to sessions. Any session owner can read it:

```shell
chainctl develop policy describe --parent $ORGANIZATION
```

To change the policy, you need permission to list every user's sessions in the organization, which organization owners have. Pass one or more of the following flags to `chainctl develop policy set`:

| Flag | Values | What it controls |
| ---- | ------ | ---------------- |
| `--org-github` | `bound` (default), `session`, or `off` | With `bound`, the app serves the session's repository and any other repository the session's owner approved, with a token scoped to that repository and operation. With `session`, the app serves only the session's repository, and other repositories go to the session owner's laptop. With `off`, the app serves nothing. |
| `--org-github-push-beyond-session` | `true` (default) or `false` | Whether the app can push to repositories other than the session's own, when the session's owner approved it. |
| `--user-github` | `true` or `false` (default) | Whether sessions act on GitHub as their owner. |

Sessions pick up a policy change at their next request.

## Let sessions act on GitHub as you

By default, a session reaches GitHub through the Chainguard App with access to specific repositories. If your organization turns on the `user_github` policy, sessions in the organization act on GitHub as their owner instead, through the Chainguard App:

- `git` fetch and push work for any repository you can access where the app is installed.
- The `gh` CLI and the GitHub API work, within the app's permissions and your own access.
- Check runs and commit statuses are read-only, and a person must approve and merge pull requests.

To turn on the policy for an organization, run the following command with the permissions described in the previous section:

```shell
chainctl develop policy set --user-github=true --parent $ORGANIZATION
```

Next, connect your GitHub account once. `chainctl` opens your browser so you can authorize the connection:

```shell
chainctl develop github login
```

The connection serves your sessions in every organization whose policy turns it on, and renews itself until you disconnect it. No GitHub token is written to your laptop. When the policy is on and you haven't connected an account, `chainctl develop` offers to connect it, and refuses to create a session until you do. To check the connection, run `chainctl develop github status`. To disconnect, run `chainctl develop github logout`.
