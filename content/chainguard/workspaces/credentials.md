---
title: "Manage Chainguard Workspaces session credentials"
linktitle: "Session credentials"
description: "Learn how a Chainguard Workspaces session reaches GitHub, Claude, and Chainguard without holding credentials, and how to approve, review, and revoke what it can reach."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-13T13:59:25+00:00
draft: false
tags: ["Chainguard Workspaces", "Security", "Configuration"]
images: []
menu:
  docs:
    parent: "workspaces"
toc: true
weight: 50
---

A Chainguard Workspaces session holds no long-lived credentials: its VM stores no API keys, tokens, or registry logins. Instead, the session reaches each service through a local hostname, and the credential is added to the request outside the VM. This page explains what a session can reach by default, how to change it, and [which credentials a session can't supply](#credentials-a-session-cant-supply).

A check in Chainguard Checks can get short-lived credentials through a workload identity, which a session can't use. Refer to [Workload identities and trust](/chainguard/checks/identity-and-trust/).

## How credentials reach a session

Each service a session can reach has a hostname inside the session, such as `http://github/` or `http://claude/`. Chainguard configures the session to use these hostnames. For example, `git` in the session rewrites `https://github.com/` URLs to `http://github/`, and Claude Code sends its requests to `http://claude/`.

When a request reaches one of these hostnames, `chainctl` on your laptop or Chainguard adds the credential outside the VM. Each credential has a *source*:

| Source | Where the credential comes from |
| ------ | ------------------------------- |
| `laptop` | Your laptop. For `claude` and `gcp`, `chainctl` sends the credential to the session's host, outside the VM, when you attach. For `github` and `cgr.dev`, `chainctl` answers each request from your laptop, so the credential never leaves your machine. |
| `org` | Your Chainguard organization, such as the Chainguard App's access to your GitHub repositories. |
| `seat` | Your Chainguard identity, which your laptop delegates to the session when you attach. Only the `chainguard` service uses this source. |
| `off` | Nothing. The session can't use the service. |

A credential that `chainctl` sends to the session's host stays there until the session parks or the credential expires, so it keeps working after you close your terminal. Refer to [Use Claude Code in a session](/chainguard/workspaces/coding-agents/) for how long Claude's credential lasts, and to [Use your Google Cloud credentials in a session](#use-your-google-cloud-credentials-in-a-session) for Google Cloud's.

Requests that `chainctl` answers from your laptop work only while your laptop serves the session, which it does while you're attached. If your terminal served one of them while you were attached, it keeps serving after you detach and keep the session running, until you press `Ctrl+C`. If nothing serves a session, these requests fail with an error that says no laptop is attached.

## What a session can reach by default

A new session can reach the following services without asking you:

| Service | Default source | What it covers |
| ------- | -------------- | -------------- |
| `claude` | `laptop` | The credential Claude Code on your laptop uses, for the Claude API's messages and models endpoints. |
| `github` | `org` | `git` fetch and push for the session's repository, and for the repositories of your checkout's other github.com remotes where the Chainguard App is installed. To use the others, add them as remotes in the session, as described in [Choose the session's repository](/chainguard/workspaces/manage-sessions/#choose-the-sessions-repository). |
| `cgr.dev` | `org` | Pulls images and lists tags from `cgr.dev` as the Chainguard platform, not as you, so it can't pull or list your organization's private images. |
| `chainguard` | `seat` | `chainctl` and the Chainguard Model Context Protocol (MCP) servers in the session act as you, limited to read, Chainguard Checks, and MCP capabilities in the session's organization, within the permissions you hold. Refer to [Your Chainguard identity in a session](#your-chainguard-identity-in-a-session). |

The GitHub API isn't covered by default. The `gh` CLI is installed in every session, but it has no credential unless you connect your GitHub account before you create the session and your organization's policy allows it, as described in [Let sessions act on GitHub as you](/chainguard/workspaces/github-as-you/).

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
| `gcp` | Lets the session call Google Cloud APIs as you, with your laptop's Google Cloud application default credentials. You can add it to a new or existing session, `all` doesn't include it, and `chainctl` doesn't remember it for the next session. Refer to [Use your Google Cloud credentials in a session](#use-your-google-cloud-credentials-in-a-session). |
| `all` | Restores the defaults and allows fetching any GitHub repository. |
| `none` | Turns off `claude`, `cgr.dev`, `chainguard`, and `gcp`, and allows only the session's own repository. It can't be combined with other entries. |

For example, this command lets the session push to a second repository, `acme/docs`, in addition to its own:

```shell
chainctl develop --with github:acme/docs+push --parent $ORGANIZATION
```

Wildcard entries allow fetching only. To push to a repository, name it with `+push`. Under your organization's default GitHub policy, the Chainguard App doesn't serve wildcard entries, so they give access to public repositories only. To fetch a private repository, name it.

The `github` entries have no effect on a session that acts on GitHub as you, as described in [Controls that don't apply to a session that acts as you](/chainguard/workspaces/github-as-you/#controls-that-dont-apply-to-a-session-that-acts-as-you).

## Use your Google Cloud credentials in a session

To let `gcloud` and the Google Cloud client libraries in a session act as you, run `gcloud auth application-default login` on your laptop. Then add `--with gcp` when you create a session or return to one. For example, this command turns on `gcp` for an existing session:

```shell
chainctl develop app/quiet-harbor --with gcp --parent $ORGANIZATION
```

While you're attached, you can also turn `gcp` on or off from the session menu: press `Ctrl+]`, choose **Credentials**, choose `gcp`, and then choose **Set the source**. The change can take up to 30 seconds to reach the session. If `chainctl` says that the session's guest `was booted without the wiring that lets it use your Google credentials`, or the **Credentials** screen has no `gcp`, the session was created before it could use your Google credentials, so it can't use them. Delete it and create a new one with `chainctl develop --new --with gcp`.

The session's VM holds only a placeholder credential. Each time you attach, `chainctl` sends your Google Cloud credential to Chainguard, which keeps it outside the VM, adds it to the session's requests to Google APIs, and discards it when the session parks. Usually, `chainctl` sends a short-lived access token and renews it while you're attached. If you attach to a session you're already keeping running, however little of that time is left, `chainctl` sends your refresh token instead, and access lasts until the session parks. A session created with `--keep always` always gets the refresh token. If your application default credentials have no refresh token, such as a service account's, `chainctl` sends an access token either way. `chainctl` tells you which one it sent.

If you detach with one of the session menu's **Detach — keep running** options, whatever duration you choose, `chainctl` sends your refresh token before it detaches, so access lasts until the session parks. If you exit the shell instead, `chainctl` can't send the refresh token, and access ends within an hour. The message `chainctl` prints when you detach says which applies.

While the session has your credential, code in it can use your Google Cloud access, and anything it creates with that access, such as a service account key, outlives the session. If the session's environment has an `egress` list, include `sts.googleapis.com` and the Google APIs the session calls.

Every session sets `GOOGLE_APPLICATION_CREDENTIALS` and `CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE` to its placeholder credential, whether or not `gcp` is on. While `gcp` is off, `gcloud` and the Google Cloud client libraries fail with an error that says Google credentials are unavailable. To sign in to Google Cloud in the session another way, such as with `gcloud auth login`, unset both variables first.

## Credentials a session can't supply

A session gets credentials only for Claude, GitHub, Chainguard's `cgr.dev` and `apk.cgr.dev` registries, your Chainguard identity, and, when you turn on `gcp`, Google APIs on `*.googleapis.com`. The `--with` flag takes only the entries listed in [Allow access ahead of time](#allow-access-ahead-of-time), so you can't add another service. A session has no credential for services such as the following:

- Amazon Web Services (AWS) and Microsoft Azure
- Private npm, PyPI, and Maven registries
- Container registries other than `cgr.dev`, such as `ghcr.io` and Google Artifact Registry on `*.pkg.dev`
- Chainguard Libraries. A check in Chainguard Checks can download JavaScript and Python libraries through a [workload identity](/chainguard/checks/identity-and-trust/).

If you paste one of these credentials into a session, or sign in to a tool there, such as with `aws configure` or `npm login`, the credential stays on the session's disk or in its memory. When the session parks, Chainguard saves the credential in the session's snapshot with everything else, and keeps it until you delete the session or the session expires. Any program in the session, including a coding agent, can read the credential and send it anywhere the session can reach. Do work that needs these credentials on your laptop instead.

## Review and revoke a session's credentials

To see what a session can reach, run `chainctl develop creds` with the session's name or short ID:

```shell
chainctl develop creds app/quiet-harbor --parent $ORGANIZATION
```

The output lists each service with its source and any repositories bound to it, what your laptop remembers approving, whether a laptop is serving the session right now, and the most recent changes to the session's credentials.

To change a session's credentials, pass one or more of the following flags to `chainctl develop creds`:

| Flag | What it does |
| ---- | ------------ |
| `--revoke <entry>` | Takes access back from the session and from your laptop's remembered approvals. `<entry>` is `claude`, `cgr.dev`, `chainguard`, `github:<owner>/<repo>`, or `github:<owner>/<repo>+push`, which takes back only the push. |
| `--source <service>=<source>` | Changes where a credential comes from. `<source>` is `laptop`, `org`, or `off`. The `claude` and `gcp` services take only `laptop` or `off`, and `chainguard` takes only `off`. To turn `chainguard` back on, use `--with chainguard`. |
| `--forget` | Removes everything your laptop remembers for the session's repository, without changing the session. |

Changes to `github` have no effect on a session that acts on GitHub as you, as described in [Controls that don't apply to a session that acts as you](/chainguard/workspaces/github-as-you/#controls-that-dont-apply-to-a-session-that-acts-as-you).

For example, to let a session pull your organization's private images from `cgr.dev` as you, switch the `cgr.dev` credential to your laptop:

```shell
chainctl develop creds app/quiet-harbor --source cgr.dev=laptop --parent $ORGANIZATION
```

Your laptop must have a `cgr.dev` login in its Docker credential helper, which you can set up as described in [Configure a Docker credential helper](/platform/chainctl-usage/how-to-install-chainctl/#configure-a-docker-credential-helper). The session can pull with it, but not push.

Your laptop keeps remembered approvals in `develop/approvals.json` in the `chainctl` configuration directory, readable only by you. The file stores service names, sources, and scopes, never credentials, and Chainguard's servers can't write to it.

### Change credentials from the session menu

While you're attached, you can change a session's credentials without leaving it. Press `Ctrl+]` to open the session menu, choose **Credentials**, and then choose a credential. Its screen shows where the credential comes from, what it covers and what it doesn't, and what your laptop remembers for it. The screen offers the following actions:

| Action | What it does |
| ------ | ------------ |
| **Allow more…** | Adds access. It takes the same entries as `--with`, such as `github:<owner>/<repo>+push` or `cgr.dev`. |
| **Revoke…** | Takes access back from the session and from your laptop's remembered approvals, as `chainctl develop creds --revoke` does. For `github`, you choose a repository, or only its push. |
| **Set the source** | Changes where the credential comes from. For `claude` and `gcp`, you choose your laptop or no credential. For `github` and `cgr.dev`, you choose your laptop, your organization, or no credential. For `chainguard`, you choose your delegated Chainguard identity, which you then approve with `y`, or no credential. |
| **Widen…** | Asks for more capabilities or groups for `chainguard`. Type them as `CAP[,CAP...] [in GROUP[,GROUP...]]`, and then press `y` to approve the wider scope, or `d` to approve only the default scope. |

The `claude` screen also offers **Use Vertex AI…** or **Use Anthropic…**, as described in [Switch a session to another provider](/chainguard/workspaces/coding-agents/#switch-a-session-to-another-provider). For a session that acts on GitHub as you, the `github` screen shows your GitHub account and offers no actions. If the list has no `gcp`, the session can't use your Google Cloud credentials, as described in [Use your Google Cloud credentials in a session](#use-your-google-cloud-credentials-in-a-session).

When you attach, `chainctl` prints a line for each credential the session gets without asking you. A line that ends in `(turn off: ~. → Credentials)` or `(change: ~. → Credentials)` points to this screen, which you can open by pressing `Ctrl+]`, or by typing `~.` where it works, as described in [Detach from a session](/chainguard/workspaces/manage-sessions/#detach-from-a-session). If the attach has no session menu, the line names the `chainctl develop creds` command to run instead.

## Set your organization's GitHub policy

Your organization's policy controls which repositories the Chainguard App serves to sessions. Any session owner can read it:

```shell
chainctl develop policy describe --parent $ORGANIZATION
```

To change the policy, you need permission to list every user's sessions in the organization, which the `owner` role includes. A Starter organization has no role that includes it, so its policy stays at the defaults. Pass one or more of the following flags to `chainctl develop policy set`:

| Flag | Values | What it controls |
| ---- | ------ | ---------------- |
| `--org-github` | `bound` (default), `session`, or `off` | With `bound`, the app serves the session's repository and any other repository the session's owner approved, with a token scoped to that repository and operation. With `session`, the app serves only the session's repository, and other repositories go to the session owner's laptop. With `off`, the app serves nothing. |
| `--org-github-push-beyond-session` | `true` (default) or `false` | Whether the app can push to repositories other than the session's own, when the session's owner approved it. |
| `--user-github` | `true` (default) or `false` | Whether sessions can act on GitHub as their owner. A session acts as its owner only if the owner connected a GitHub account before creating it. With `false`, new sessions reach GitHub through their `github` source instead, and sessions that already act as their owner have their GitHub requests refused. |

Sessions pick up a policy change at their next request. The `--org-github` and `--org-github-push-beyond-session` settings don't apply to sessions that act on GitHub as their owner.

## Let sessions act on GitHub as you

If you connect your GitHub account, the sessions you create afterward act on GitHub as you through the Chainguard Develop GitHub App, instead of through their `github` source. Such a session doesn't ask you to approve GitHub requests, and the `github` entries and sources on this page don't apply to it. Refer to [Let sessions act on GitHub as you](/chainguard/workspaces/github-as-you/).

## Your Chainguard identity in a session

`chainctl` and the Chainguard MCP servers in a session act as you through a delegated Chainguard identity, so they work without a login in the session:

- The first time you attach to a session in an organization, `chainctl` creates an identity named `chainctl-develop` there. It acts for you only through grants that your laptop issues.
- While you're attached to the session's shell, `chainctl` on your laptop issues a grant that lasts about an hour, and renews it before it expires. After you detach, the identity keeps working until the last grant expires, for up to an hour. A terminal that keeps serving after you detach doesn't renew it.
- Your laptop needs a live `chainctl` login to issue grants. Don't run `chainctl auth login` in the session.
- By default, a grant carries MCP tool calls, the read-only capabilities you hold in the session's organization, and the capabilities to list, run, rerun, and cancel Chainguard Checks runs. It never carries a capability you don't hold. To ask for more capabilities or groups, open the session menu, choose **Credentials**, choose `chainguard`, and then choose **Widen…**.

The identity reaches the Chainguard API, `chainctl checks`, and the `cg-apk` and `cg-versions` MCP servers that every session includes. Whatever a grant carries, the session can't change anything through the Chainguard API except Chainguard Checks runs, and it can only list packages on `apk.cgr.dev`. Other MCP servers get no credential, and pulls from `cgr.dev` use the session's `cgr.dev` credential.

Most `chainctl checks` commands, such as `status`, `logs`, and `rerun`, work in the session as you, within your own permissions, and a pull request records a rerun as your request. In a Starter organization, the `limited_owner` role can't list Chainguard Checks runs, so `chainctl checks` commands that look up a run, including `status`, `logs`, and `rerun`, don't work for that role, in a session or on your laptop. The `chainctl checks top`, `chainctl checks trends`, and `chainctl checks accept-terms` commands work only on your laptop.

To turn off a session's Chainguard identity, run `chainctl develop creds` with `--revoke chainguard` or `--source chainguard=off`, pass `--with none`, or turn it off on the **Credentials** screen. To turn it back on, use `--with chainguard`. To stop it for every session at once, delete the `chainctl-develop` identity from your organization. Tokens that sessions already hold keep working until they expire.
