---
title: "Set up Chainguard Checks and Chainguard Workspaces"
linktitle: "Set up Checks and Workspaces"
description: "How Chainguard Checks and Chainguard Workspaces work together, and how to sign up for both with chainctl develop init and give teammates access."
type: "article"
date: 2026-10-13T00:00:00+00:00
lastmod: 2026-10-20T15:35:02+00:00
draft: false
tags: ["Chainguard Checks", "Chainguard Workspaces", "Getting Started", "Procedural"]
images: []
weight: 10
toc: true
---

[Chainguard Checks](/chainguard/checks/overview/) runs your repository's CI on every GitHub pull request, with each check in its own microVM. [Chainguard Workspaces](/chainguard/workspaces/overview/) runs your development work, and the coding agents that do it, in a remote microVM session that holds none of your long-lived credentials. You can use either product on its own, but they're built to work together, and you set them up together: one command, `chainctl develop init`, turns on both. This page explains what the products share, then walks you through signing up and giving teammates access. For how the two products isolate your code, refer to [How Chainguard Checks and Chainguard Workspaces isolate your code](/get-started/checks-and-workspaces/how-it-works/).

{{< beta feature="Each product" >}}

## What the products share {#what-the-products-share}

| Shared piece | What it means |
| ------------ | ------------- |
| One sign-up | `chainctl develop init` turns on both products, each with its own free monthly allowance. Refer to [Sign up with chainctl develop init](#sign-up-with-chainctl-develop-init). |
| One GitHub App | The Chainguard App delivers pull request events to Chainguard Checks and, by default, fetches and pushes your repository for Workspaces sessions. A GitHub account can be linked to only one Chainguard organization. |
| One configuration file | Chainguard Checks runs the checks in your repository's `.chainguard/ci.yaml` file on every pull request. In a Workspaces session, `run-ci` runs the same checks against your working tree, and a session can use the file's environment. |
| One role | The `sandbox.user` role lets a member use both products. Refer to [Give teammates access](#give-teammates-access). |

## How they work together {#how-they-work-together}

A typical loop uses both products:

1. Open a Workspaces session on your repository, and let Claude Code make a change.
2. Run `run-ci` in the session to run your repository's checks against the change. Refer to [Run checks before you push](/chainguard/checks/run-checks/).
3. Push the change and open a pull request. Chainguard Checks runs the same checks and reports the result on the pull request.
4. If a check fails, read why from the session with `chainctl checks failures`, fix the change, and push again. Refer to [Inspect pull request runs](/chainguard/checks/inspect-and-run-checks/#inspect-pull-request-runs).

## Prerequisites {#prerequisites}

Before you begin, make sure you have the following:

- A GitHub account that can install GitHub Apps on the personal account or organization that owns your repository. To install the app on an organization and link it, you need the owner role on that organization.
- A local clone of a repository on github.com that you can push to.
- A work email address. A personal email address, such as a Gmail address, can't create a Chainguard organization.
- If you already belong to a Chainguard organization, the `owner` or `limited_owner` role in the organization where you turn on Chainguard Checks and Chainguard Workspaces.

## Install or update chainctl {#install-or-update-chainctl}

You sign up with `chainctl`, and you use it with both products: `chainctl checks` for Chainguard Checks and `chainctl develop` for Chainguard Workspaces. If you don't have it yet, follow the [chainctl installation guide](/platform/chainctl-usage/how-to-install-chainctl/).

Chainguard Checks and Chainguard Workspaces need `chainctl` 0.2.386 or later. Releases before 0.2.383 can't keep a detached session running while it's busy or use a Claude login that Chainguard holds, and releases before 0.2.382 can't sign you up as this page describes or run Claude Code in a session. Both products change often during the beta, so if you already have `chainctl`, update it to the latest release:

```shell
sudo chainctl update
```

If you installed `chainctl` with Homebrew, run `brew upgrade chainctl` instead. Refer to [Updating chainctl](/platform/chainctl-usage/how-to-install-chainctl/#updating-chainctl) for details.

Updating doesn't change the sessions you already have. A session created with `chainctl` 0.2.382 or earlier doesn't keep running while it's busy. Unless you keep it running, it parks about 10 minutes after you detach, as described in [Keep a session running while you're away](/chainguard/workspaces/manage-sessions/#keep-a-session-running-while-youre-away).

## Install the Chainguard App {#install-the-chainguard-app}

The Chainguard App is a GitHub App that connects your repositories to Chainguard. Chainguard Checks receives pull request events and reports results through it, and by default, Workspaces sessions fetch and push your repository through it. [Guardener](/chainguard/guardener/) uses the same app.

1. Go to the [Chainguard App installation page](https://github.com/apps/chainguard/installations/new).
2. Choose the personal account or organization that owns your repository.
3. Choose **All repositories**, or select the repositories you want to use with Chainguard Checks or Chainguard Workspaces.
4. Review the requested permissions and select **Install**.

Installing the app doesn't change your repositories. Chainguard Checks runs only on repositories that have a `.chainguard/ci.yaml` file, after you link the account in the next step.

## Sign up with chainctl develop init {#sign-up-with-chainctl-develop-init}

The `chainctl develop init` command signs you in, creates a free [Chainguard Starter](/chainguard/containers/reference/catalog-starter/) organization if you don't have one, and turns on Chainguard Checks and Chainguard Workspaces. Each product gets its own free monthly allowance, which resets on the first day of each month (UTC). For what each allowance includes, refer to Availability and limits for [Chainguard Checks](/chainguard/checks/overview/#availability-and-limits) and for [Chainguard Workspaces](/chainguard/workspaces/overview/#availability-and-limits).

Run the command in an interactive terminal, because it opens your browser and asks questions as it goes:

```shell
chainctl develop init
```

To create an organization, sign in with a work email address, using a password or a Google account. A personal email address, such as a Gmail address, can't create one, and neither can other sign-in methods, such as GitHub or GitLab.

The command does the following:

1. Signs you in through your browser, and registers a new Chainguard identity if you don't have one.
2. Picks the Chainguard organization to use:
    - If you don't belong to one, it asks your name, company, job title, and whether you want updates from Chainguard, then creates one, named after your email domain.
    - If you belong to exactly one organization on the Starter or Team plan, it uses that one, even if your role there, such as `viewer` or `sandbox.user`, can't turn on Chainguard Checks and Chainguard Workspaces. The command then stops with an error that says `missing: terms.accept`, as described in [`chainctl develop init` fails](/chainguard/workspaces/troubleshooting/#chainctl-develop-init-fails).
    - Otherwise, it stops and asks you to choose an organization with `--parent`.
3. Asks you to accept the terms that Chainguard Checks and Chainguard Workspaces are offered under, if your organization hasn't accepted them yet: the [Code Analysis Terms](https://www.chainguard.dev/legal/code-analysis-terms), the [Secured Platform Terms](https://www.chainguard.dev/legal/secure-platform-terms), the [Master Service and License Agreement](https://www.chainguard.dev/legal/master-service-and-license-agreement), and, for the GitHub link, the Guardener [Terms of Service](https://www.chainguard.dev/legal/guardener) and [Data Privacy Agreement](https://www.chainguard.dev/legal/supplemental-dpa).
4. If your organization isn't linked to a GitHub account yet, asks which one to link. Link the account that owns your repository: press `Enter` to link your own GitHub user, or enter the name of a GitHub organization where you have the owner role, such as `acme`, not a URL. The command opens your browser so you can authorize the link. If the Chainguard App isn't installed on the account, the command offers to open the installation page, then authorizes and links the account again.
5. Turns on Chainguard Checks and Chainguard Workspaces with their monthly allowances, and prints each product's limits. If Chainguard already granted your organization an allowance, the command keeps it.
6. Offers to connect your GitHub account, if you haven't yet and your organization allows it, so that the Workspaces sessions you create act on GitHub as you. The connection uses Chainguard Develop, a GitHub App separate from the Chainguard App. If you run the command in your repository's directory, it also offers to install Chainguard Develop on the GitHub accounts your repository needs. Chainguard Checks doesn't need this connection, so you can decline and connect later with `chainctl develop github login`, as described in [Let sessions act on GitHub as you](/chainguard/workspaces/github-as-you/).

When you authorize the link, GitHub might ask you to authorize single sign-on for your GitHub organizations. If you're linking your own GitHub user, select **Continue**. To link an organization that uses SAML single sign-on, authorize single sign-on for that organization.

A GitHub account can be linked to only one Chainguard organization at a time. If the account you choose is already linked to another Chainguard organization, `chainctl develop init` names the account and, in an interactive terminal, asks for a different one to link. To move the account to your organization instead, press `Ctrl+C` to stop the command, and then refer to [Moving a GitHub organization to a different Chainguard organization](/chainguard/guardener/github/app-connections/#moving-a-github-organization-to-a-different-chainguard-organization).

If `chainctl develop init` stops with an error, refer to [`chainctl develop init` fails](/chainguard/workspaces/troubleshooting/#chainctl-develop-init-fails).

### Answer questions ahead of time {#answer-questions-ahead-of-time}

You can answer some of the command's questions with flags:

| Flag | What it does |
| ---- | ------------ |
| `--github-org` | Links the named GitHub organization instead of your own GitHub user. |
| `--parent` | Turns on Chainguard Checks and Chainguard Workspaces in an organization you already belong to, including an Enterprise organization, instead of creating one. You need the `owner` or `limited_owner` role in it. |

For example, to link the `acme` GitHub organization:

```shell
chainctl develop init --github-org acme
```

For every flag, refer to the [`chainctl develop init` reference](/chainguard/workspaces/chainctl-develop-reference/#chainctl-develop-init).

### Use an organization your company already has {#use-an-organization-your-company-already-has}

If your company already has a Chainguard organization, `chainctl develop init` can't create a second one for your email domain. Ask one of its owners to add you, as described in [Give teammates access](#give-teammates-access). Someone with the `owner` or `limited_owner` role in the organization can then turn on both products, replacing `$ORGANIZATION` with the organization's name:

```shell
chainctl develop init --parent $ORGANIZATION
```

If the organization already has Chainguard Checks or Chainguard Workspaces through your Chainguard account team, the command keeps that allowance.

An organization that has a product through the account team must also accept that product's terms, which takes the `owner` or `limited_owner` role. Until someone accepts them, Chainguard Checks runs no checks for the organization, so the summary check on each pull request fails with **Run creation failed**, and no one can open a Workspaces session in it. To accept the terms for one product only, use its own command:

```shell
chainctl checks accept-terms --parent $ORGANIZATION
chainctl develop accept-terms --parent $ORGANIZATION
```

If your GitHub account isn't linked to the organization yet, link it as described in [Getting started with Guardener](/chainguard/guardener/github/getting-started/#step-2-link-your-chainguard-organization-to-github), which uses the same Chainguard App.

## Give teammates access {#give-teammates-access}

Your teammates don't need a Chainguard account to get checks on their pull requests or to read the results on GitHub. A teammate needs a role in your Chainguard organization to open the Chainguard Checks run page, to use `chainctl checks` commands such as `status` and `rerun`, or to open Workspaces sessions. Each teammate opens and manages their own sessions, which count toward your organization's [limits](/chainguard/workspaces/overview/#availability-and-limits).

| Role | In Chainguard Checks | In Chainguard Workspaces | Inside a session |
| ---- | -------------------- | ------------------------ | ---------------- |
| `sandbox.user` | Opens the run page, and reads, reruns, and cancels runs with `chainctl checks`. | Opens and manages the teammate's own sessions, and runs checks in them. | `chainctl checks` commands work as the teammate. The Chainguard MCP servers don't, because the role doesn't include the `mcp.tool.call` capability. |
| `limited_owner` | Starts runs with `chainctl checks run`, but can't open the run page or read runs. | Opens sessions. Also manages your organization's billing and invites or removes members. | Neither the Chainguard MCP servers nor the `chainctl checks` commands that look up a run, such as `status` and `logs`, work. |
| `mcp.tool_user` | Nothing. | Nothing. | Adds `mcp.tool.call`, so the Chainguard MCP servers work. |

Inside a session, a teammate's Chainguard identity can't do more than their role allows, as described in [Your Chainguard identity in a session](/chainguard/workspaces/credentials/#your-chainguard-identity-in-a-session). For more about roles, refer to [Overview of roles and role-bindings](/platform/administration/iam-organizations/roles-role-bindings/roles-role-bindings/).

### Add a teammate {#add-a-teammate}

In a Starter organization, the steps differ, as described in [Add a teammate to a Starter organization](#add-a-teammate-to-a-starter-organization). If you have the `owner` role in your organization, invite your teammate with the `sandbox.user` role as follows. Replace `$ORGANIZATION` with the name of your Chainguard organization:

1. Create an invite for your teammate with the `sandbox.user` role. Replace `$EMAIL` with your teammate's email address:

    ```shell
    chainctl iam invite create $ORGANIZATION --role sandbox.user --email $EMAIL
    ```

2. Send your teammate the invite code that the command prints. Your teammate accepts the invite by logging in with it, replacing `$INVITE_CODE` with the code:

    ```shell
    chainctl auth login --invite-code $INVITE_CODE
    ```

Accepting the invite grants the role. To let a teammate use the Chainguard MCP servers in sessions, also grant them `mcp.tool_user` with a role-binding, as described in [Overview of roles and role-bindings](/platform/administration/iam-organizations/roles-role-bindings/roles-role-bindings/).

Your teammate can then install `chainctl`, as described in [Install or update chainctl](#install-or-update-chainctl), and open a session, as described in [Get started with Chainguard Workspaces](/chainguard/workspaces/getting-started/#step-2-open-a-session).

### Add a teammate to a Starter organization {#add-a-teammate-to-a-starter-organization}

If you created your organization with `chainctl develop init`, it's a Starter organization, and you have the `limited_owner` role rather than `owner`. You can't create role-bindings for other users, so you can't grant the `sandbox.user` role, and members read Chainguard Checks results on GitHub instead of on the run page. An invite can give only a role whose permissions you also have, and of those roles, only `limited_owner` can open sessions.

To invite a teammate who can open sessions, follow [Add a teammate](#add-a-teammate), but use `--role limited_owner` instead of `--role sandbox.user` in step 1:

```shell
chainctl iam invite create $ORGANIZATION --role limited_owner --email $EMAIL
```

The `limited_owner` role also lets its holder manage your organization's billing and invite or remove members.

Each invite must name your teammate's email address with `--email`, and the address must be in your organization's domain or one of its subdomains.

A coworker whose email address is in your organization's domain can also ask to join by running `chainctl starter request-access`, which emails you the request. For details, refer to [Request access with chainctl](/chainguard/containers/reference/catalog-starter/#request-access-with-chainctl).

## Next steps {#next-steps}

- [Get started with Chainguard Checks](/chainguard/checks/getting-started/#step-2-add-a-configuration-file-to-your-repository): add a `.chainguard/ci.yaml` file and see your first checks run.
- [Get started with Chainguard Workspaces](/chainguard/workspaces/getting-started/#step-2-open-a-session): open your first session.
- [Use Claude Code in a session](/chainguard/workspaces/coding-agents/): work with a coding agent in a session.
