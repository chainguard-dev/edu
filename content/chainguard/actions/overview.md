---
title: "Chainguard Actions overview"
linktitle: "Actions overview"
description: "Learn how Chainguard Actions provides hardened drop-in replacements for popular GitHub Actions to protect your CI/CD pipelines from supply chain attacks."
type: "article"
date: 2026-06-18T00:00:00+00:00
lastmod: 2026-09-25T14:39:07+00:00
draft: false
tags: ["Chainguard Actions", "Overview"]
menu:
  docs:
    parent: "actions"
weight: 001
toc: true
---

Chainguard Actions are a set of hardened drop-in replacements for popular GitHub Actions. Each action preserves the same inputs and outputs as the upstream version, but has been examined and revised to better protect your CI/CD pipelines from supply chain attacks. The only change in your workflow configuration is the name of the action in the `uses:` line.

The catalog holds more than 1,000 hardened actions. Coverage spans GitHub first-party (`actions/*`), cloud-provider (`aws-actions/*`, `azure/*`, `google-github-actions/*`), Docker, HashiCorp, and security tools actions (Trivy, Grype, CodeQL, Semgrep), as well as a growing catalog of community actions.

Each hardened action:

- Is rebuilt from the upstream source at a pinned commit, then reviewed by a static ruleset and an AI-powered analysis pass
- Has every internal `uses:` and container image reference pinned to an immutable SHA digest
- Ships with a `HARDENING.md` report documenting exactly what was checked and fixed
- Ships with a signed SLSA provenance attestation recording the upstream source and the ruleset version applied (releases published before signing began don't carry one)
- Is re-reviewed and re-hardened whenever upstream publishes a new version or Chainguard adds a new rule

Chainguard Actions protect against common threats including tag hijacking, dependency confusion, `pull_request_target` abuse, and secret exfiltration.

This page provides enough to get you started. Refer to the [Chainguard Actions README](https://github.com/chainguard-actions) in GitHub for deeper technical details and some example migrations.

## What hardening checks and fixes

Every action in the catalog goes through the same two-stage review. A deterministic static pre-pass runs first and catches patterns mechanically. An AI-powered analysis pass then evaluates the action against the policy ruleset. Findings from either stage carry an ID that appears in the action's `HARDENING.md` report, so you can trace any change back to the check that produced it.

### Policy checks

| Check | Finding IDs | Severity | What it catches |
| ----- | ----------- | -------- | --------------- |
| Unpinned uses | `unpinned-uses` | High | A `uses:` reference or a `runs.image:` container reference pointing at a mutable tag or branch instead of an immutable commit SHA or image digest. The `docker://` prefix is optional, so `image: ghcr.io/example/tool:latest` is a finding too. |
| Script injection | `script-injection` | High | Expressions such as `${{ inputs.name }}` interpolated directly into a `run:` block, where the shell can parse attacker-controlled text as commands. |
| Unsafe shell | `unsafe-shell` | High | Remote content piped straight into an interpreter, such as `curl ... \| bash`. |
| Hardcoded credentials | `hardcoded-credentials` | High | Literal secrets assigned to names containing `password`, `secret`, `token`, `api_key`, or `aws_secret`. |
| GitHub environment injection | `github-env-injection` | High | Untrusted values written to `$GITHUB_ENV`, `$GITHUB_PATH`, or `$GITHUB_OUTPUT` without newline sanitization, which lets an attacker inject variables into later steps. |
| Suspicious run content | `suspicious-run-content` | High | Malicious patterns in `run:` blocks, including obfuscated execution, process memory access, dynamic evaluation, credential file access, outbound exfiltration, reverse shells, persistence, and environment secret scraping. |
| Permissions | `permissions`, `missing-permissions`, `broad-permissions` | Medium | Workflows that leave `GITHUB_TOKEN` at its default permissions, or that set `read-all` or `write-all` instead of specific scopes. |

### Static pre-pass checks

The static pre-pass complements the analysis pass by catching patterns the analysis may miss. It reports one finding per occurrence, so a report can list the same ID many times, each with its own location. `static-inline-injection` is the most common finding in the catalog for that reason.

| Finding ID | Severity | What it catches |
| ---------- | -------- | --------------- |
| `static-inline-injection` | High | A single expression interpolated directly into a `run:` block. The finding names the expression and the step it appears in, and the fix moves the value into an `env:` map. |
| `static-unsanitized-env-write` | Medium | An unsanitized write to a GitHub environment file. |
| `invalid-yaml` | High | An action or workflow file that could not be parsed. |

Both stages read the action definition (`action.yml` or `action.yaml`) and every workflow under `.github/workflows/` in the action's own repository. Neither inspects built or vendored output: `dist/`, `vendor/`, and `node_modules/` are out of scope, as are the action's test fixtures.

Findings are fixed in place and the pipeline re-evaluates its own work, so a single hardening run can take several iterations before an action passes. Both the findings and the per-iteration notes are recorded in `HARDENING.md`.

## Transitive dependencies

Actions rarely run alone. A composite action can call other actions, and an action can fetch container images, language packages, or binaries while it runs. Chainguard hardens the references it can see in the action's source:

- **Nested action and image references are pinned.** Every `uses:` reference and container image reference inside a hardened action resolves to an immutable commit SHA or image digest, with the original tag preserved as a comment. A moved upstream tag can't change what a hardened action runs.
- **The action's own workflows are reviewed too.** Both stages of the review cover the workflows under `.github/workflows/` in the action's repository, not only the action definition.
- **Missing dependencies can be onboarded.** When a hardened action depends on an action that isn't in the catalog yet, [request that action](https://github.com/chainguard-actions/.github/issues/new?template=new-action.yml) and Chainguard hardens and publishes it.

### Rewriting nested references to hardened equivalents

Pinning a nested reference to an upstream commit SHA freezes what runs, but the code it freezes is still the upstream project's. Chainguard is rolling out a dependency graph that replaces those references with the Chainguard hardened counterpart instead, also pinned by commit SHA. When a dependency is hardened and published, every action that depends on it returns to the hardening queue so its `uses:` reference can be rewritten.

The graph is enabled in production and rewriting is rolling out across the catalog, so a given action may not have been rewritten yet. Three limits apply where it does:

- It covers composite actions only. Node and Docker actions have no `uses:` steps to rewrite.
- It fires only when a hardened counterpart exists for that exact upstream commit.
- It never rewrites a reference when the correct counterpart is ambiguous.

To see what a particular action references today, read its `action.yml` on the version branch you plan to use.

### Dependencies an action installs when it runs

Dependency vulnerability management is not part of hardening today. When Chainguard rebuilds a JavaScript action's bundle, the builder installs exactly what the upstream lockfile pins, so the hardened action ships the same dependency versions the upstream release shipped. The rebuild reproduces the bundle rather than refreshing it: if an upstream release bundled a vulnerable package, so does the hardened release. Language packages and binaries that an action downloads while it runs are likewise outside what the review inspects.

Dependency handling is an area Chainguard is actively building out, and the nested-reference rewriting described earlier is the first piece of it.

To see the full dependency graph for your own repository, including actions reached through other actions, use the `--recursive` flag described in [View the actions you are currently using](#view-the-actions-you-are-currently-using-in-a-repository).

## Prerequisites

To follow this guide, you need:

- `chainctl` **v0.2.261** or later, installed and authenticated. Refer to [How to install `chainctl`](/platform/chainctl-usage/how-to-install-chainctl/) if you don't have it yet.
- An active Chainguard organization.
- Owner access on the organization.

## Set up Chainguard Actions

Setting up has two parts: entitle your organization, then choose how you migrate your workflows.

### Step 1: Create the Actions entitlement

Authenticate using `chainctl`:

```shell
chainctl auth login
```

Create the Chainguard Actions entitlement to enable access to the hardened actions hosted at `github.com/chainguard-actions`:

```shell
chainctl actions entitlements create
```

The output confirms the entitlement:

```output
Enabled Actions product for org chainguard.edu ($ENTITLEMENT_ID) [entitlement id: $ENTITLEMENT_ID]
```

Confirm your entitlement:

```shell
chainctl actions entitlements list
```

```output
                    ID                    |         CREATED
------------------------------------------|-------------------------
 $ENTITLEMENT_ID                          | 2026-06-18 17:33:24 UTC
```

#### What the entitlement controls

The entitlement records your organization's access to Chainguard Actions. It does not gate consumption of the actions themselves, and it can't: the hardened action repositories are public, and GitHub provides no mechanism to require authentication to consume a public action.

Each hardened action runs a `runs.pre` hook that records a usage event to `https://actions.enforce.dev/actions/v1/record`. The hook returns no authorization decision, so there is nothing for the action to act on. It times out after 2 seconds and discards every error, which means Chainguard being slow or unreachable cannot fail your workflow. If your runners use an egress allowlist, add that host so the hook doesn't spend its timeout on every step.

Refer to [Chainguard Actions telemetry and privacy](/chainguard/actions/telemetry/) for what the hook records and how to limit it.

### Step 2: Install the Guardener GitHub App

The [Chainguard Guardener](/chainguard/guardener/github/getting-started/) GitHub App is the recommended way to adopt Chainguard Actions across more than a repository or two. Once you install it and link it to your Chainguard organization, the Guardener:

- Inventories the actions your workflows use across every repository it can access
- Comments on pull requests that introduce unhardened actions, so your workflows don't drift back
- Opens and maintains a pull request that swaps in Chainguard hardened equivalents, once you enable migration

To set it up:

1. Install the [Guardener GitHub App](https://github.com/apps/chainguard-guardener) on your GitHub organization.
2. Link your Chainguard organization to your GitHub organization with `chainctl guardener github link`.
3. Add a `.chainguard/actions.yaml` file to the root of each repository you want the Guardener to work on.

Both of the last two steps matter. Installing the app changes no repository on its own, and the Actions feature stays inert until `.chainguard/actions.yaml` exists in the repository. Once it does, pull request recommendations are on by default, but automated migration pull requests need `migrate.enabled: true` set explicitly:

```yaml
enabled: true
migrate:
  enabled: true
```

If installing an app in your organization needs an administrator's approval, they will be asked to approve a specific set of GitHub permissions. [Permissions the Guardener requests](/chainguard/guardener/github/getting-started/#permissions-the-guardener-requests) lists each one and why it's needed, so you can take that to them before you start.

Refer to [Getting started with Chainguard Guardener](/chainguard/guardener/github/getting-started/) for the installation and linking steps, and to [Hardened Actions](/chainguard/guardener/github/actions-security/) for the configuration reference, the migration options, and the on-demand migration command.

The Guardener GitHub App is in beta. It runs in production and is supported, but its features and configuration may still change.

If you'd rather not install a GitHub App, you can migrate with the [cg-actions](https://github.com/chainguard-dev/cg-skills/tree/main/skills/cg-actions) skill or by hand. Both approaches are covered in [Configure your workflows to use Chainguard Actions](#configure-your-workflows-to-use-chainguard-actions).

## Basic usage (quick start)

To use a Chainguard hardened action, edit your workflow's YAML configuration file and change the `uses:` line to match the location in `chainguard-actions`:

```yaml
- uses: chainguard-actions/<action-name>@<version-tag>
```

Repository names are prefixed with the upstream organization, so `tj-actions/changed-files` becomes `tj-actions-changed-files`. This keeps two different sources of a `changed-files` action from clashing in the Chainguard Actions organization.

Search the Chainguard Actions repository, find the action you want to use, and then use the name you find there.

> **Note:** Don't reference a hardened action with `@main`. The main branch of each repository holds only metadata (`README.md`, `LICENSE_CHAINGUARD`, and `source.json`). The hardened action itself lives on the version branches, so a reference to `@main` fails to resolve.

This example uses a version tag to show the mechanic, which is all that changes in your workflow. For any workflow you intend to keep, pin to a commit SHA instead, as described in [Choose how to reference an action](#choose-how-to-reference-an-action).

## Choose how to reference an action

Pin to a commit SHA, and pair the pin with Dependabot or Renovate:

```yaml
- uses: chainguard-actions/actions-checkout@<sha> # v4
```

A commit SHA is the only immutable reference in the catalog. Tags are mutable by design, and not just the floating major version. Chainguard re-hardens published versions in place and moves the tag when it does, including fully qualified patch tags, so a single upstream release can be re-hardened several times with the same tag pointing somewhere new each time. Both `@v4` and `@v4.3.1` resolve to whatever was published most recently.

Pinning on its own isn't enough, though. A pin with no tooling behind it is the one configuration that strands you: you stay on that build, and stop receiving re-hardening, until someone updates the SHA by hand. Dependabot and Renovate both track a pinned SHA against its tag and open a pull request when the tag moves, so you receive every re-hardening as a change your own CI validates before it reaches a live workflow. That gives you more control than a mutable tag does, and costs you nothing in freshness.

Pinning is also the standard Chainguard applies to the actions it hardens. The `unpinned-uses` check fails any `uses:` reference on a tag, so if you run an actions linter against your own repository, referencing a hardened action by tag will register a finding.

Use the canonical repository name in the reference. Some catalog repositories answer to an older name through a GitHub rename redirect — `chainguard-actions/checkout` reaches `chainguard-actions/actions-checkout`, for example — but a redirect isn't something to depend on in a pinned workflow.

## Configure your workflows to use Chainguard Actions

You can save some time by using the optional [cg-actions](https://github.com/chainguard-dev/cg-skills/tree/main/skills/cg-actions) skill, a Claude Code skill for auditing GitHub Actions usage and migrating to Chainguard hardened actions.

Following the steps in this section will achieve a similar result.

### Inventory the actions you currently use.

Run this from the root of your repository to get a deduplicated list of every `uses:` line across every workflow:

```shell
grep -rhE "uses:\s*[^@]+@" .github/workflows/ | sort -u
```

For a more thorough inventory that also follows composite actions, use [`chainctl actions discover`](#view-the-actions-you-are-currently-using-in-a-repository).

### Check the Chainguard Actions catalog for each action.

Browse [the Chainguard Actions repository](https://github.com/chainguard-actions) or use the GitHub search UI. Match by organization and action name — for example, if you use `tj-actions/changed-files`, search for `org:chainguard-actions tj-actions-changed-files`.

If the action isn't in the catalog, [open an issue](https://github.com/chainguard-actions/.github/issues/new?template=new-action.yml) to request it.

### Replace the `uses:` line in each workflow.

Change the `uses:` line to match the location in `chainguard-actions`. To pin by SHA digest, preserve the original tag as a comment so Dependabot, Renovate, and human reviewers can track upgrades:

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
- uses: chainguard-actions/tj-actions-changed-files@25a1eb5aa40568ec6f8c0e58f2e809ef4270ebfa # v47
```

### Update your allowed-actions list.

If your GitHub organization or repository restricts which actions can run (**Settings > Actions > General > Allow select actions**), add `chainguard-actions/*` to the allowed patterns. Without this, workflows fail with a policy error on first run.

> **Note:** It's a good idea to remove allowed actions that are no longer being used.

### Commit, open a PR, and verify that CI passes.

The action's inputs, outputs, and behavior are almost always identical to the upstream version, so no other workflow changes are typically needed.

However, read the `HARDENING.md` file for each hardened action before migrating. In rare cases, the hardening process requires a change to inputs, outputs, or behavior — those changes are documented in this file.

If something breaks, [file an issue](https://github.com/chainguard-actions/.github/issues/new?template=action-issue.yml) with a reproducer.

## View the actions you are currently using in a repository

Use `chainctl` to scan every workflow and composite action in a repository and list the actions and container images they reference:

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

The command needs a GitHub token, which it reads from `$GITHUB_TOKEN` or from `gh auth token`. The target can be a local directory (the current directory by default), an `owner/repo` pair, or a single action reference such as `actions/checkout@v4`.

By default, `discover` lists only the actions your workflows reference directly. Add `--recursive` to follow each referenced action into its own definition and resolve the full transitive dependency graph:

```shell
chainctl actions discover $GIT_ORGANIZATION/$REPO --recursive
```

A recursive scan makes many GitHub API calls, so it caches responses and stops after `--timeout` (five minutes by default). Refer to [`chainctl actions discover`](/platform/chainctl/chainctl-docs/chainctl_actions_discover/) for the full set of flags.

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

To list the catalog entries available to a specific organization rather than the whole public catalog, use [`chainctl actions list`](/platform/chainctl/chainctl-docs/chainctl_actions_list/):

```shell
chainctl actions list --parent $ORGANIZATION
```

## What ships in each hardened action

Each hardened action's repository has a main branch and one branch per hardened version. The hardened action lives on the version branches; the main branch holds only metadata.

The main branch of each repository contains:

- `README.md` — a pointer to the action and its upstream source
- `LICENSE_CHAINGUARD` — the Chainguard license for the hardened variant
- `source.json` — a manifest naming the upstream owner, repository, version, and commit, along with the policy SHAs applied

Each version branch contains:

- `HARDENING.md` — the authoritative, per-action record of what was checked, what was fixed, and how, including the policy SHA that pins the exact ruleset applied
- `action.yml` or `action.yaml` — the hardened action definition, preserving upstream inputs and outputs with fixes applied
- `attestations/provenance.intoto.jsonl` — a signed [SLSA provenance](https://slsa.dev/provenance/v1) attestation naming the upstream repository and commit, the ruleset version, the build times, and a SHA-256 digest for every file in the hardened action
- `LICENSE_CHAINGUARD` — the Chainguard license for the hardened variant
- The upstream action's own files, including its license and any documentation you can adapt for the hardened version

Because `HARDENING.md` and the attestation are per-version, read them on the version branch you plan to use rather than on the main branch.

Nearly every version branch in the catalog carries an attestation. A small number of older releases were published before Chainguard began signing them, so if a version branch has no `attestations/` directory, treat that release as unverifiable rather than as verified.

Chainguard doesn't publish a customer-facing verification procedure yet. Verification requires the signing key's fingerprint, which isn't published, so there is no complete recipe to follow today. Tooling for this is planned. In the meantime the attestation is still useful as a record: it names the upstream commit the release was built from and the ruleset version that was applied.

## The continuous re-hardening process

Chainguard Actions are continuously re-hardened:

- When upstream publishes a new version, the pipeline re-runs and publishes a new hardened version
- When the hardening ruleset is updated, every action in the catalog is re-evaluated against the new ruleset and re-hardened as needed
- The `HARDENING.md` report is regenerated on every hardening run, with its own policy SHA pinning the exact set of rules that were applied

Because the policy SHA is computed over the ruleset itself, any change to a rule produces a new SHA, which is what triggers the catalog-wide re-evaluation.

## Request a new action or report an issue

To request an action that isn't in the catalog, [open a new action issue](https://github.com/chainguard-actions/.github/issues/new?template=new-action.yml).

If an action isn't working as expected, [open an action issue](https://github.com/chainguard-actions/.github/issues/new?template=action-issue.yml) with the action reference, a description of the problem, and steps to reproduce.

## Learn more

- [Chainguard Actions telemetry and privacy](/chainguard/actions/telemetry/)
- [Hardened Actions with Chainguard Guardener](/chainguard/guardener/github/actions-security/)
- [Chainguard Actions product page](https://www.chainguard.dev/actions)
- For other questions, [contact Chainguard](https://www.chainguard.dev/contact?utm=docs).
