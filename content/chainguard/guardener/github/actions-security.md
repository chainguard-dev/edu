---
title: "Guardener Hardened Actions"
linktitle: "Hardened Actions"
description: "Configure Guardener to recommend and migrate your GitHub Actions to Chainguard's hardened, SHA-pinned equivalents."
type: "article"
date: 2026-07-08T00:00:00+00:00
lastmod: 2026-11-12T13:56:30+00:00
draft: false
aliases:
- /chainguard/guardener/actions-security/
tags: ["GitHub", "Automation"]
images: []
menu:
  docs:
    parent: "guardener-github"
weight: 40
toc: true
---

The Hardened Actions feature recommends and migrates your GitHub Actions to Chainguard's hardened, SHA-pinned equivalents. Pinning actions to a specific commit SHA — rather than a mutable tag or branch — protects your workflows from supply chain attacks in which an upstream tag is moved to point at malicious code.

{{< note >}}Hardened Actions is in Early Access. It's available to organizations that have installed and linked the Chainguard App.{{< /note >}}

Hardened Actions operates in two independent modes:

- **Pull request recommendations** — non-blocking review comments that suggest hardened action alternatives, with one-click suggestion blocks.
- **Automated migration pull requests** — a periodically maintained pull request that updates workflows across your repository. You can also [trigger this migration on demand](#run-an-on-demand-migration) with `chainctl` instead of waiting for the next scheduled run. If you opt in, the same pull request also [upgrades the Chainguard Actions pins you already use](#keep-chainguard-actions-pins-up-to-date).

You can enable either mode on its own or both together.

Hardened Actions keeps your workflows on GitHub Actions. To move a repository's pull request checks off GitHub Actions runners instead, refer to [Migrate from GitHub Actions to Chainguard Checks](/chainguard/checks/migrate-from-github-actions/).

## Enable Hardened Actions

Add a `.chainguard/actions.yaml` file to your repository:

```yaml
enabled: true
```

With just `enabled: true`, Guardener posts non-blocking recommendation comments on pull requests that touch your workflows. It does not open pull requests of its own.

## Enable automated migration pull requests

To have Guardener periodically open and maintain a pull request that migrates your workflows, enable the `migrate` block:

```yaml
enabled: true
migrate:
  enabled: true
  period: "168h"
```

Guardener opens (and keeps updated) a single migration pull request on the cadence you set with `period`.

When a later run finds nothing left to migrate or upgrade, for example after a new `migrate.ignore` entry excludes the remaining changes, Guardener closes the migration pull request with a comment that says why. Guardener leaves the pull request open if it has an assignee or the `skip:guardener` label, or if a lookup in the Chainguard Actions catalog failed during the run. Setting `migrate.enabled: false` doesn't close the pull request.

## Run an on-demand migration

Instead of waiting for the next scheduled run — for example, right after enabling migration, or after Chainguard publishes a hardened equivalent for an action you use — you can trigger the migration immediately with `chainctl`.

An on-demand run performs exactly the same migration as the scheduled flow: it opens (or updates) the repository's single migration pull request and honors the same `.chainguard/actions.yaml` configuration, including `migrate.ignore`. Because it shares the opt-in gate, the repository (or its organization, through the [org-level `.github` configuration](/chainguard/guardener/github/configuration/)) must have `migrate.enabled: true`; if migration is not enabled, the run completes as a no-op without opening a pull request. Triggering an on-demand run does not change the periodic schedule.

Before you start, make sure that:

- The Chainguard App is installed and your Chainguard organization is linked to your GitHub organization, as described in [Getting started](/chainguard/guardener/github/getting-started/). The migration must be requested through the Chainguard organization that owns the Chainguard App installation.
- You hold the `guardener.actions.migrate` capability on that Chainguard organization. The built-in `viewer`, `editor`, and `owner` roles include it, as do `guardener.user` and `guardener.admin`. Each built-in role that includes either migration capability includes both. Refer to the [Built-in roles and capabilities reference](/platform/administration/iam-organizations/roles-role-bindings/capabilities-reference/) for more information on roles.

Run `chainctl guardener github migrate create` with the repository to migrate:

```shell
chainctl guardener github migrate create <owner>/<repo>
```

The repository can be given as `owner/repo` shorthand or as a full URL (`https://github.com/owner/repo`); only github.com repositories are supported today. The migration runs under the Chainguard organization that owns the Chainguard App installation. `chainctl` selects that organization automatically when only one is available and prompts you when there are several; pass `--parent <group-name>` to name it explicitly.

With `chainctl` 0.2.375 or later, the command runs every migration that the repository opts in to, so it also opens or updates the [Container Image Migration](/chainguard/guardener/github/image-migration/) pull request when `.chainguard/images.yaml` enables it. Earlier versions of `chainctl` run only the Hardened Actions migration.

Each migration checks its own capability. If you hold `guardener.actions.migrate` but not `guardener.images.migrate`, the `Images:` line reports a permission error and the command exits with an error, even when the repository doesn't use image migration.

By default, the command waits for the migrations to finish (up to 10 minutes, adjustable with `--timeout`) and prints one result for each:

```
Repository: https://github.com/<owner>/<repo>
Triggered by: you@example.com (user)
Actions: https://github.com/<owner>/<repo>/pull/42
Images: migration is not enabled here or in repository configuration
Status: completed
```

In this example, the repository opts in to Hardened Actions migration only. When there's nothing to migrate — every action is already on a Chainguard equivalent, or the ignore rules exclude everything — the `Actions:` line reads `no changes needed` instead of a pull request URL. When the repository hasn't enabled Hardened Actions migration, it reads `migration is not enabled here or in repository configuration`. If a migration fails, its line reads `failed` with the reason, the last line reads `Status: completed with failures`, and the command exits with an error.

If the migration fails because the Chainguard App installation does not cover the repository (for example, the app was installed on **selected repositories** and this one isn't included), the error says so; grant the app access to the repository in your GitHub organization settings and trigger the migration again.

## Check a migration operation

Pass `--wait=false` to return immediately instead of waiting. The command prints an operation name of the form `operations/migrate/<group>/<id>`, which you can check later with `chainctl guardener github migrate get`:

```shell
chainctl guardener github migrate get operations/migrate/<group>/<id>
```

The owning organization is derived from the operation name, so no `--parent` is needed. Add `--wait` to poll until the operation completes (bounded by `--timeout`, 10 minutes by default). Interrupting a waiting `migrate create` is also safe — the migration keeps running server-side, and the command prints the operation name so you can check it later.

For the complete set of flags and options, refer to the `chainctl` reference:

- [`chainctl guardener github migrate`](/platform/chainctl/chainctl-docs/chainctl_guardener_github_migrate/)
- [`chainctl guardener github migrate create`](/platform/chainctl/chainctl-docs/chainctl_guardener_github_migrate_create/)
- [`chainctl guardener github migrate get`](/platform/chainctl/chainctl-docs/chainctl_guardener_github_migrate_get/)

## Exclude files and actions

Use the `migrate.ignore` block to exclude specific workflow files or upstream actions from automated migration. Both fields accept glob patterns:

```yaml
enabled: true
migrate:
  enabled: true
  period: "168h"
  ignore:
    files:
      - "release.yml"
      - "*.deprecated.yml"
    actions:
      - "actions/checkout"
      - "actions/*"
```

- `ignore.files` — workflow files (under `.github/workflows/`) to skip.
- `ignore.actions` — upstream actions to leave untouched.

## Keep Chainguard Actions pins up to date

After Guardener migrates a step to a hardened action, it doesn't change that step again, so the pin gets older as Chainguard publishes new versions. To have Guardener move your existing Chainguard Actions pins to newer versions, turn on upgrades in the `migrate` block:

```yaml
enabled: true
migrate:
  enabled: true
  period: "168h"
  upgrade:
    enabled: true
```

Upgrades are off by default, and they run only when `migrate.enabled` is also `true`. They run on the `migrate.period` schedule and with each [on-demand migration](#run-an-on-demand-migration), and they skip anything that `migrate.ignore` excludes. With only `upgrade.enabled: true`, Guardener allows every update type and waits three days before it uses a new version.

### How Guardener picks a new version

Guardener reads versions from the Chainguard Actions catalog rather than from upstream tags. For each pin, it picks the newest version that meets all of these conditions:

- It's later than the version the pin uses now, and it isn't a prerelease.
- No [ignore rule](#skip-upgrades-with-ignore-rules) skips it.
- Its [cooldown](#set-the-cooldown) has ended.

The newest version can be a new major version, as with Dependabot's default behavior. If no version meets the conditions, Guardener leaves the line unchanged.

Each pin keeps its form. A SHA pin gets a new SHA, and a tag pin gets a new tag:

| Pin form | Before | After |
| -------- | ------ | ----- |
| SHA pin | `chainguard-actions/actions-checkout@<sha> # v4.2.2` | `chainguard-actions/actions-checkout@<new-sha> # v7.0.1` |
| Tag pin | `chainguard-actions/actions-checkout@v4.2.2` | `chainguard-actions/actions-checkout@v7.0.1` |
| Floating tag pin | `chainguard-actions/actions-checkout@v4` | `chainguard-actions/actions-checkout@v6` |

A floating tag, such as `v4`, moves to each new release in its major version. A pin on a floating tag stays on a floating tag and never becomes a pin on a single release. A SHA pin with a `# v4` comment moves to the newest build of `v4`, or to a later floating tag such as `# v6`. A tag pin on `@v4` already gets each new build of `v4` through the tag, so it moves only to a later major version's tag.

Guardener doesn't check whether an upgrade changes an action's inputs or behavior. Major versions can include breaking changes, so read the release notes for each major upgrade before you merge the pull request.

### Review upgrades in the migration pull request

Upgrades go into the same pull request as migrations, in a table that lists each action's current version, new version, and update type. The update type follows Dependabot's rules. For a pin on `4.2.2`:

| New version | Update type |
| ----------- | ----------- |
| `4.2.3` | Patch |
| `4.3.0` | Minor |
| `5.0.0` or later | Major |

A newer build of the same version counts as a patch, except for a SHA pin on a floating tag. There, a newer build counts as the largest change the tag allows: a minor for `# v4` and a patch for `# v4.3`. A rule that skips minor updates therefore also skips new builds of `v4`.

When a later version passes its cooldown, Guardener updates the pull request instead of opening another one. A pull request that only upgrades pins is titled "Upgrade Chainguard GitHub Actions".

### Set the cooldown

A new version waits out a cooldown before Guardener uses it, which gives time for a bad release to be found and withdrawn. The default cooldown is three days, the same as Dependabot's. To change it, set `cooldown.default-days` to a whole number of days from 0 to 365:

```yaml
enabled: true
migrate:
  enabled: true
  upgrade:
    enabled: true
    cooldown:
      default-days: 7
```

A value of `0` turns off the cooldown. Guardener counts whole days in UTC. With a three-day cooldown, a version first listed on October 16 can be used from October 20.

The cooldown starts at the later of two dates: the date the Chainguard Actions catalog first listed the version, and the date of the upstream commit it was built from. If upstream moves a tag to a newer commit, the cooldown starts again. A Chainguard rebuild of the same upstream code doesn't restart it.

### Skip upgrades with ignore rules

The `upgrade.ignore` list uses the same format as Dependabot's `ignore` option, so you can copy rules from your `dependabot.yml` file. This example skips major upgrades for every action and skips all upgrades for `chainguard-actions/actions-cache`:

```yaml
enabled: true
migrate:
  enabled: true
  upgrade:
    enabled: true
    ignore:
      - dependency-name: "*"
        update-types: ["version-update:semver-major"]
      - dependency-name: "chainguard-actions/actions-cache"
```

Each rule has these fields:

- `dependency-name` — the actions that the rule covers, such as `chainguard-actions/actions-checkout`. A `*` matches any characters, including `/`, and matching ignores case. A rule for an action also covers its sub-path actions, so `chainguard-actions/actions-cache` also covers `chainguard-actions/actions-cache/restore`.
- `update-types` — the update types to skip: `version-update:semver-major`, `version-update:semver-minor`, or `version-update:semver-patch`. A rule without `update-types` skips every upgrade for the actions it covers.

Guardener doesn't support Dependabot's `versions` field in ignore rules.

### Fix invalid upgrade settings

A mistake in `migrate.upgrade` turns off upgrades for the repository, but nothing else. Migrations and pull request recommendations keep running, and the migration pull request names the setting that turned off upgrades. If the mistake leaves nothing to migrate or upgrade, Guardener [closes the migration pull request](#enable-automated-migration-pull-requests) and names the setting in its closing comment. If the repository has no migration pull request, Guardener doesn't report the mistake, so check `.chainguard/actions.yaml` when expected upgrades don't appear.

These count as mistakes:

- A value of the wrong type, such as `0.5` for `default-days`
- A number of days outside the range from 0 to 365
- An ignore rule without a `dependency-name`
- An update type other than the three listed in [Skip upgrades with ignore rules](#skip-upgrades-with-ignore-rules)
- A `versions` field in an ignore rule
- Any other key under `migrate.upgrade` or `migrate.upgrade.cooldown`, such as a misspelled `default-days` or Dependabot's `semver-major-days`

Guardener ignores Dependabot's cooldown `include` and `exclude` lists. Without them, the cooldown applies to every action.

### Use upgrades alongside Dependabot or Renovate

If Dependabot or Renovate already updates GitHub Actions in the repository, both tools open pull requests for the same upgrades. To prevent this, have the other tool skip Chainguard Actions. For Dependabot, add an ignore rule to the `github-actions` entry in your `dependabot.yml` file:

```yaml
version: 2
updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
    ignore:
      - dependency-name: "chainguard-actions/*"
```

For Renovate, add a `packageRules` entry that turns off updates for packages under `chainguard-actions/`.

### Upgrade limitations

Guardener doesn't upgrade these pins:

- A SHA pin that Guardener can't match to a version, because the catalog no longer lists its SHA and it has no version comment.
- Pins in a repository that has a GitHub workflow lockfile (`.github/workflows/actions.lock`). Migrations in these repositories work as before.

## Configuration reference

| Field                    | Default | Purpose                                                                             |
| ------------------------ | ------- | ----------------------------------------------------------------------------------- |
| `enabled`                | `true`  | Enables inline pull request recommendation comments.                                |
| `migrate.enabled`        | `false` | Opts into automated migration pull requests.                                        |
| `migrate.period`         | `24h`   | How often the migration pull request is refreshed. Clamped to a minimum of one day. |
| `migrate.version-strategy` | `exact` | Version selection when no exact equivalent exists. Set to `smallest-major-bump` to migrate older pins to the closest Chainguard-supplied major version. |
| `migrate.ignore.files`   | —       | Glob patterns for workflow files to skip during migration.                          |
| `migrate.ignore.actions` | —       | Glob patterns for upstream actions to skip during migration.                        |
| `migrate.upgrade.enabled` | `false` | Opts into upgrades of existing Chainguard Actions pins. Requires `migrate.enabled: true`. |
| `migrate.upgrade.cooldown.default-days` | `3` | Whole days a new version waits before Guardener uses it, from 0 to 365. `0` turns off the cooldown. |
| `migrate.upgrade.ignore` | — | Dependabot-style rules that skip upgrades by action name and update type. |

The `period` value is a Go-style duration string (for example, `24h`, `168h` for one week).

## Full example

A complete `.chainguard/actions.yaml` enabling both recommendations and weekly automated migration, while leaving the `actions/*` family and a release workflow untouched:

```yaml
enabled: true
migrate:
  enabled: true
  period: "168h"
  ignore:
    files:
      - "release.yml"
    actions:
      - "actions/*"
```

## Next steps

- **[Commit Verification](/chainguard/guardener/github/commit-verification/)** — Require cryptographically signed commits in pull requests.
- **[Configuration](/chainguard/guardener/github/configuration/)** — Review the shared `.chainguard/` configuration model.
