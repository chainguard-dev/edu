---
title: "Chainguard Actions overview"
linktitle: "Overview"
description: "Learn how Chainguard Actions provides hardened drop-in replacements for popular GitHub Actions to protect your CI/CD pipelines from supply chain attacks."
type: "article"
date: 2026-06-18T00:00:00+00:00
lastmod: 2026-06-18T00:00:00+00:00
draft: false
tags: ["Chainguard Actions", "Overview"]
menu:
  docs:
    parent: "actions"
weight: 001
toc: true
---

Chainguard Actions are a set of hardened drop-in replacements for popular GitHub Actions. Each action preserves the same inputs and outputs as the upstream version, but has been examined and revised to better protect your CI/CD pipelines from supply chain attacks. The only change in your workflow configuration is the name of the action in the `uses:` line.

Coverage spans GitHub first-party (`actions/*`), cloud-provider (`aws-actions/*`, `azure/*`, `google-github-actions/*`), Docker, HashiCorp, and security tools actions (Trivy, Grype, CodeQL, Semgrep), as well as a growing catalog of community actions.

Each hardened action:

- Is built from source and evaluated through a rule-based and AI-powered hardening pipeline
- Has every internal `uses:` and container image reference pinned to an immutable SHA digest
- Ships with a `HARDENING.md` report documenting exactly what was checked and fixed
- Is re-reviewed and re-hardened whenever upstream publishes a new version or Chainguard adds a new rule

Chainguard Actions protect against common threats including tag hijacking, dependency confusion, `pull_request_target` abuse, and secret exfiltration.

This page provides enough to get you started. See the [Chainguard Actions README](https://github.com/chainguard-actions) in GitHub for deeper technical details and some example migrations.

## Prerequisites

To follow this guide, you need:

- `chainctl` **v0.2.261** or later, installed and authenticated. See [How to Install `chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/) if you don't have it yet.
- An active Chainguard organization.
- Owner access on the organization.

The examples in this guide use an `$ORGANIZATION` environment variable to refer to your organization. Set it to the name of your organization before you begin:

```shell
export ORGANIZATION=<your-organization>
```

## Preliminary steps

Before using Chainguard Actions, log in to Chainguard and enable the Chainguard Actions entitlement for your organization.

Authenticate using `chainctl`:

```shell
chainctl auth login
```

Create the Chainguard Actions entitlement to enable access to the hardened actions hosted at `github.com/chainguard-actions`:

```shell
chainctl actions entitlements create --parent $ORGANIZATION
```

The output confirms the entitlement:

```output
Enabled Actions product for org chainguard.edu ($ENTITLEMENT_ID) [entitlement id: $ENTITLEMENT_ID]
```

Confirm your entitlement:

```shell
chainctl actions entitlements list --parent $ORGANIZATION
```

```output
                    ID                    |         CREATED
------------------------------------------|-------------------------
 $ENTITLEMENT_ID                          | 2026-06-18 17:33:24 UTC
```

## Basic usage (quick start)

To use a Chainguard hardened action, edit your workflow's YAML configuration file and change the `uses:` line to match the location in `chainguard-actions`:

```yaml
- uses: chainguard-actions/<action-name>@main
```

Action names often have the upstream organization appended to the action name for clarity, for example, `tj-actions/changed-actions` becomes `tj-actions-changed-actions`. This prevents two different sources of a `changed-actions` action from clashing in the Chainguard Actions repository.

Search the Chainguard Actions repository, find the action you want to use, and then use the name you find there.

> **Note:** This example uses `@main`, a mutable reference, to illustrate the mechanics of switching organizations. For production workflows, pin to an immutable SHA digest instead. The [Configure your workflows](#configure-your-workflows-to-use-chainguard-actions) section covers the full migration, including how to [find the correct SHA digest](#find-the-sha-for-a-specific-release).

The rest of this page goes a bit deeper into how to use Chainguard Actions.

## Configure your workflows to use Chainguard Actions

You can save some time by using the optional [cg-actions](https://github.com/chainguard-dev/cg-skills/tree/main/skills/cg-actions), which is a Claude Code skill for auditing GitHub Actions usage and migrating to Chainguard hardened actions. See the link for details.

Following the steps in this section will achieve a similar result.

### Inventory the actions you currently use.

Run this from the root of your repository to get a deduplicated list of every `uses:` line across every workflow:

```shell
grep -rhE "uses:\s*[^@]+@" .github/workflows/ | sort -u
```

### Check the Chainguard Actions catalog for each action.

Browse [the Chainguard Actions repository](https://github.com/chainguard-actions) or use the GitHub search UI. Match by organization and action name — for example, if you use `tj-actions/changed-files`, search for `org:chainguard-actions tj-actions-changed-files`.

If the action isn't in the catalog, [open an issue](https://github.com/chainguard-actions/.github/issues/new?template=new-action.yml) to request it.

### Replace the `uses:` line in each workflow.

Change the `uses:` line to match the location in `chainguard-actions`. Find and pin to the commit SHA digest and preserve the original tag as a comment so Dependabot, Renovate, and human reviewers can track upgrades:

```yaml
# Before
- uses: tj-actions/changed-files@v47
```

```yaml
# After
- uses: chainguard-actions/tj-actions-changed-files@<SHA> # v47
# originally - uses: tj-actions/changed-files@v47
```

To find the SHA digest for a specific release, use the `gh` CLI:

```shell
gh api repos/chainguard-actions/tj-actions-changed-files/commits/v47 --jq '.sha'
```

```output
25a1eb5aa40568ec6f8c0e58f2e809ef4270ebfa
```

For the short SHA digest:

```shell
gh api repos/chainguard-actions/tj-actions-changed-files/commits/v47 --jq '.sha[:7]'
```

```output
25a1eb5
```

The resulting `uses:` line with the full SHA digest:

```yaml
- uses: chainguard-actions/changed-files@25a1eb5aa40568ec6f8c0e58f2e809ef4270ebfa # v47
```

### Update your allowed-actions list.

If your GitHub organization or repository restricts which actions can run (**Settings > Actions > General > Allow select actions**), add `chainguard-actions/*` to the allowed patterns. Without this, workflows fail with a policy error on first run.

> **Note:** It's a good idea to remove allowed actions that are no longer being used.

### Commit, open a PR, and verify that CI passes.

The action's inputs, outputs, and behavior are almost always identical to the upstream version, so no other workflow changes are typically needed.

However, read the `HARDENING.md` file for each Chainguard Action before migrating. In rare cases, the hardening process requires a change to inputs, outputs, or behavior — those changes are documented in this file.

If something breaks, [file an issue](https://github.com/chainguard-actions/.github/issues/new?template=action-issue.yml) with a reproducer.


## View the actions you are currently using in a repository

Use `chainctl` to scan every workflow and composite action in a repository and list all dependencies transitively:

```shell
chainctl actions discover $GIT_ORGANIZATION/$REPO
```

```output
    scanning $GIT_ORGANIZATION/$REPO for workflows and actions
               ACTION                    | REQUESTED | USED BY
    -------------------------------------|-----------|---------
     actions/checkout                    | v4        | 1
     chainguard-actions/actions-checkout | v6.0.2    | 1

    2 actions, 0 container images

```

## View the actions currently available

While you can search the [Chainguard Actions repository](https://github.com/chainguard-actions) directly in GitHub, you can also use `chainctl` to find an action.

```shell
chainctl actions catalog list --upstream-owner=$OWNER
```

For example, to list all the actions from the `tj-actions` source:

```shell
chainctl actions catalog list --upstream-owner=tj-actions
```

This example returns a list of all actions in the Chainguard Actions repository that originate from the `tj-actions` upstream source.


## Hardened action repository contents

The main branch of each hardened action repository contains:

- `HARDENING.md` — the authoritative, per-action record of what was checked, what was fixed, and how
- `action.yml` or `action.yaml` — the hardened action definition, preserving upstream inputs and outputs with fixes applied
- `LICENSE_CHAINGUARD` — the Chainguard license for the hardened variant
- `source.json` and `published.json` — manifests pointing at the upstream source and the upstream version being tracked (not yet present in all repos; some older repos don't include them)
- Some actions also include documentation from upstream that you can adapt to use with the Chainguard hardened version

Then, the version branches in the hardened action repos contain the hardened actions.

## The continuous re-hardening process

Chainguard Actions are continuously re-hardened:

- When upstream publishes a new version, the pipeline re-runs and publishes a new hardened version
- When the hardening ruleset is updated, affected actions are re-reviewed against the new rules
- The `HARDENING.md` report is regenerated on every hardening run, with its own policy SHA pinning the exact set of rules that were applied

## Request a new action or report an issue

To request a new action, [open an issue](https://github.com/chainguard-actions/.github/issues/new?template=new-action.yml).

## Report an issue

If an action isn't working as expected, [open an issue](https://github.com/chainguard-actions/.github/issues/new?template=action-issue.yml) with the action reference, a description of the problem, and steps to reproduce.

## Learn more

- [Chainguard Actions product page](https://www.chainguard.dev/actions)
- For other questions, [contact Chainguard](https://www.chainguard.dev/contact?utm=docs).
