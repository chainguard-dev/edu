---
title: "Get started with Chainguard Checks"
linktitle: "Getting started"
description: "Sign up for Chainguard Checks, add a .chainguard/ci.yaml file to a repository, and see your first checks run on a GitHub pull request."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-13T14:50:35+00:00
draft: false
tags: ["Chainguard Checks", "Getting Started", "GitHub", "Procedural"]
images: []
menu:
  docs:
    parent: "checks"
    identifier: "Checks Getting Started"
toc: true
weight: 20
---

This guide walks you through signing up for Chainguard Checks, adding checks to one of your GitHub repositories, and seeing them run on a pull request. It uses a Go repository as the example and takes about 15 minutes.

{{< beta feature="Chainguard Checks" access="organizations that turn it on with `chainctl develop init`, which comes with a free monthly compute allowance, or that arrange access with their Chainguard account team" >}}

## Prerequisites

Before you begin, make sure you have the following:

- A GitHub account that can install GitHub Apps on the personal account or organization that owns your repository. To install the app on an organization and link it, you need the owner role on that organization.
- A repository on github.com that you can push to, and a local clone of it.

## Step 1: Install or update chainctl {#step-1-install-or-update-chainctl}

You sign up with `chainctl`. If you don't have it yet, follow the [chainctl installation guide](/platform/chainctl-usage/how-to-install-chainctl/).

This guide needs `chainctl` 0.2.382 or later. Earlier releases can't sign you up as this guide describes. If you already have `chainctl`, update it to the latest release, because Chainguard Checks changes often during the beta:

```shell
sudo chainctl update
```

If you installed `chainctl` with Homebrew, run `brew upgrade chainctl` instead. Refer to [Updating chainctl](/platform/chainctl-usage/how-to-install-chainctl/#updating-chainctl) for details.

## Step 2: Install the Chainguard App

Chainguard Checks receives pull request events and reports results through the Chainguard App, a GitHub App that also backs [Chainguard Workspaces](/chainguard/workspaces/overview/) and [Guardener](/chainguard/guardener/).

1. Go to the [Chainguard App installation page](https://github.com/apps/chainguard/installations/new).
2. Choose the personal account or organization that owns your repository.
3. Choose **All repositories**, or select the repositories you want to use with Chainguard Checks.
4. Review the requested permissions and select **Install**.

Installing the app doesn't change your repositories. Chainguard Checks runs only on repositories that have a `.chainguard/ci.yaml` file, after you link the account in the next step.

## Step 3: Sign up and turn on Chainguard Checks {#step-3-sign-up-and-turn-on-chainguard-checks}

The `chainctl develop init` command signs you in, creates a free [Chainguard Starter](/chainguard/containers/reference/catalog-starter/) organization if you don't have one, and turns on Chainguard Checks and Chainguard Workspaces with a monthly compute allowance that resets on the first day of each month (UTC). [Availability and limits](/chainguard/checks/overview/#availability-and-limits) describes what the allowance includes. Run the command in an interactive terminal, because it opens your browser and asks questions as it goes:

```shell
chainctl develop init
```

To create an organization, sign in with an email address and password or with a Google account, not with GitHub or GitLab.

The command does the following:

1. Signs you in through your browser, and registers a new Chainguard identity if you don't have one.
2. Picks the Chainguard organization to use:
    - If you don't belong to one, it asks your name, company, job title, and whether you want updates from Chainguard, then creates one. With a work email address, the organization is named after your email domain. With a personal email address, you name it.
    - If you belong to exactly one organization on the Starter or Team plan, it uses that one.
    - Otherwise, it stops and asks you to choose an organization with `--parent`.
3. Asks you to accept the terms that Chainguard Checks and Chainguard Workspaces are offered under, if your organization hasn't accepted them yet: the [Code Analysis Terms](https://www.chainguard.dev/legal/code-analysis-terms), the [Secured Platform Terms](https://www.chainguard.dev/legal/secure-platform-terms), the [Master Service and License Agreement](https://www.chainguard.dev/legal/master-service-and-license-agreement), and, for the GitHub link, the Guardener [Terms of Service](https://www.chainguard.dev/legal/guardener) and [Data Privacy Agreement](https://www.chainguard.dev/legal/supplemental-dpa).
4. Asks which GitHub account to link. Link the account that owns your repository: press Enter to link your own GitHub user, or enter the name of a GitHub organization where you have the owner role, such as `acme`, not a URL. The command opens your browser so you can authorize the link. If the Chainguard App isn't installed on the account, the command offers to open the installation page, then authorizes and links the account again.
5. Turns on Chainguard Checks and Chainguard Workspaces with the monthly allowance, and prints each product's limits. If Chainguard already granted your organization an allowance, the command keeps it.
6. Offers to connect your GitHub account to Chainguard Workspaces sessions, unless it's connected already or your organization doesn't allow it. Sessions then act on GitHub as you, through a separate GitHub App named Chainguard Develop. Chainguard Checks doesn't need this, so you can decline, and connect later as described in [Let sessions act on GitHub as you](/chainguard/workspaces/credentials/#let-sessions-act-on-github-as-you).

When you authorize the link, GitHub might ask you to authorize single sign-on for your GitHub organizations. If you're linking your own GitHub user, select **Continue**. To link an organization that uses SAML single sign-on, authorize single sign-on for that organization.

A GitHub account can be linked to only one Chainguard organization at a time. If the account you choose is already linked to another Chainguard organization, `chainctl develop init` says so and asks for a different GitHub user or organization to link. To move the account to your organization instead, press `Ctrl+C` to stop the command, and then refer to [Moving a GitHub organization to a different Chainguard organization](/chainguard/guardener/github/app-connections/#moving-a-github-organization-to-a-different-chainguard-organization).

You can answer some of the questions ahead of time with flags:

| Flag | What it does |
| ---- | ------------ |
| `--github-org` | Links the named GitHub organization instead of your own GitHub user. |
| `--parent` | Turns on Chainguard Checks and Chainguard Workspaces in an organization you already belong to, including an Enterprise organization, instead of creating one. You must be an owner of the organization. |
| `--name` | Names the new organization when you sign up with a personal email address. The name can't look like a domain name. The command ignores `--name` for a work email address, and fails if you already belong to an organization. |

For example, to link the `acme` GitHub organization:

```shell
chainctl develop init --github-org acme
```

To turn on Chainguard Checks in an organization you already belong to, replace `$ORGANIZATION` with the organization's name:

```shell
chainctl develop init --parent $ORGANIZATION
```

If `chainctl develop init` fails, refer to [Troubleshoot Chainguard Workspaces](/chainguard/workspaces/troubleshooting/#chainctl-develop-init-fails).

If your company already has a Chainguard organization, `chainctl develop init` can't create a second one for your work email domain. Ask one of its owners to add you, as described in [Give teammates access](#give-teammates-access). An owner can then turn on Chainguard Checks in it with `chainctl develop init --parent $ORGANIZATION`. If the organization already has Chainguard Checks through your Chainguard account team, the command keeps that allowance.

An owner of an organization that has Chainguard Checks through the account team can instead accept only the Chainguard Checks terms, with the following command:

```shell
chainctl checks accept-terms --parent $ORGANIZATION
```

Until an owner accepts the terms, Chainguard Checks runs no checks for the organization, and the summary check on each pull request fails with **Run creation failed**. If your GitHub account isn't linked to the organization yet, link it as described in [Getting started with Guardener](/chainguard/guardener/github/getting-started/#step-2-link-your-chainguard-organization-to-github), which uses the same Chainguard App.

## Step 4: Add a configuration file to your repository

In your local clone, create a branch for the change. Replace `$REPO_DIR` with the path to your local clone:

```shell
cd $REPO_DIR
git checkout -b add-chainguard-checks
```

Next, create a `.chainguard/ci.yaml` configuration file that defines two checks:

```shell
mkdir -p .chainguard
cat > .chainguard/ci.yaml <<EOF
version: 1
environment:
  packages: [go]
checks:
  vet:
    cmd: go vet ./...
    network:
      egress: [proxy.golang.org, sum.golang.org]
  test:
    cmd: go test ./...
    network:
      egress: [proxy.golang.org, sum.golang.org]
EOF
```

This file tells Chainguard Checks to install the `go` package in each check's VM, then run `go vet` in one check and `go test` in another. Each check runs in a fresh VM with no network access unless it asks for some, so both checks list the Go module proxy and checksum database under `network.egress` to download the modules your code depends on. If your repository isn't a Go repository, replace the package and the commands with your own. Refer to the [configuration reference](/chainguard/checks/configuration/) for every option.

To find mistakes in the file before you push it, run `chainctl checks validate` with the repository's directory:

```shell
chainctl checks validate .
```

The command reads the file the same way Chainguard Checks does, without running anything. For this file, it prints `workflow ci (.chainguard/ci.yaml)` followed by `ok: the document lowers`. For a file with problems, it prints each problem with its line number.

## Step 5: Open a pull request

Commit the file, push the branch, and open a pull request. This example uses the GitHub CLI to open the pull request, but you can also open it on github.com:

```shell
git add .chainguard/ci.yaml
git commit -m "Add Chainguard Checks"
git push -u origin add-chainguard-checks
gh pr create --fill
```

Chainguard Checks reads the configuration file from the pull request itself, so the pull request that adds `.chainguard/ci.yaml` runs its checks.

## Step 6: Review the results

Open the pull request on GitHub and scroll to its checks. After a few seconds, you'll see the following:

- **Chainguard Checks (presubmit)**, the summary check for the whole run. It's pending while checks run, then passes only if every blocking check passed.
- **presubmit / ci / vet** and **presubmit / ci / test**, one GitHub check for each check in your file. Each appears when that check finishes.

To read a check's output, select the check. On GitHub, its output shows each step's outcome, exit code, and duration, followed by the end of its log and any errors it reported. The **Details** link opens the check's full log on a run page that Chainguard hosts. To open the run page, you need a role in your Chainguard organization, as described in [The Details link or a chainctl checks command says you don't have access](/chainguard/checks/troubleshooting/#the-details-link-or-a-chainctl-checks-command-says-you-dont-have-access). If you created your organization with `chainctl develop init`, you don't have that role, so read the output on GitHub.

If no checks appear, refer to [Troubleshoot Chainguard Checks](/chainguard/checks/troubleshooting/#a-pull-request-gets-no-checks).

## Step 7: Require checks before merging

To block merging until checks pass, add **Chainguard Checks (presubmit)** as a required status check in your branch protection rule or ruleset for the default branch.

Require only the summary check, not the per-check results. A check that a condition skips never reports a result, so GitHub would wait for it indefinitely. The summary check accounts for skipped checks.

## Give teammates access {#give-teammates-access}

Your teammates don't need a Chainguard account to get checks on their pull requests or to read the results on GitHub. A teammate needs a role in your Chainguard organization only to open the run page, to use `chainctl checks` commands such as `status` and `rerun`, or to run checks in a Workspaces session:

| Role | What it lets your teammate do |
| ---- | ----------------------------- |
| `viewer` | Find your organization by name, which `chainctl` commands need for `--parent $ORGANIZATION`. |
| `sandbox.user` | Open the run page; read, rerun, and cancel runs with `chainctl checks`; and run checks in their own Workspaces sessions. |

### Add a teammate

In a Starter organization, the steps differ, as described in [Add a teammate to a Starter organization](#add-a-teammate-to-a-starter-organization). If you have the `owner` role in your organization, invite your teammate and grant them the `sandbox.user` role as follows. Replace `$ORGANIZATION` with the name of your Chainguard organization:

1. Create an invite for your teammate with the `viewer` role. Your teammate needs it as well as `sandbox.user`, because `sandbox.user` alone doesn't let `chainctl` find your organization. Replace `$EMAIL` with your teammate's email address:

    ```shell
    chainctl iam invite create $ORGANIZATION --role viewer --email $EMAIL
    ```

2. Send your teammate the invite code that the command prints. Your teammate accepts the invite by logging in with it, replacing `$INVITE_CODE` with the code:

    ```shell
    chainctl auth login --invite-code $INVITE_CODE
    ```

3. After your teammate accepts, list your organization's role-bindings. The output shows each member's identity ID next to their email address:

    ```shell
    chainctl iam role-bindings list --parent $ORGANIZATION
    ```

4. Grant your teammate the `sandbox.user` role, replacing `$IDENTITY_ID` with their identity ID:

    ```shell
    chainctl iam role-bindings create --identity $IDENTITY_ID --role sandbox.user --parent $ORGANIZATION
    ```

Your teammate can then install `chainctl`, as described in [Step 1](#step-1-install-or-update-chainctl). For more about roles, refer to [Overview of roles and role-bindings](/platform/administration/iam-organizations/roles-role-bindings/roles-role-bindings/).

### Add a teammate to a Starter organization

If you created your organization with `chainctl develop init`, it's a Starter organization, and you have the `limited_owner` role rather than `owner`. You can invite a teammate with steps 1 and 2 of [Add a teammate](#add-a-teammate), within these limits:

- Each invite must name your teammate's email address with `--email`, and the address must be in your organization's domain or one of its subdomains.
- If you signed up with a personal email address, you can't invite anyone.
- You can't create role-bindings for other users, so you can't grant the `sandbox.user` role, and members read results on GitHub instead of on the run page.
- An invite can give only a role whose permissions you also have. Of those roles, only `limited_owner` can open sessions, and it also lets its holder manage your organization's billing and invite or remove members.

A coworker whose email address is in your organization's domain can also ask to join by running `chainctl starter request-access`, which emails you the request. For details, refer to [Request access with chainctl](/chainguard/containers/reference/catalog-starter/#request-access-with-chainctl).

## Next steps

- [Chainguard Checks configuration reference](/chainguard/checks/configuration/) covers packages, network access, conditions, and more.
- [Use Chainguard Checks on GitHub](/chainguard/checks/github/) explains reruns, checks that run on request, and checks that run after merging.
- [Run checks before you push](/chainguard/checks/run-checks/) shows how to run the same checks in a Chainguard Workspaces session.
- [Workload identities and trust](/chainguard/checks/identity-and-trust/) explains how to give a check short-lived Google Cloud or Chainguard credentials.
- [chainctl checks command reference](/chainguard/checks/chainctl-checks-reference/) lists every `chainctl checks` command and flag.
- Ask questions in the #checks-questions channel in the [Chainguard community Slack](https://join.slack.com/t/chainguardcommunity/shared_invite/zt-3nttdr807-V9BJHayWvsB0KbHsfZO5Rw).
