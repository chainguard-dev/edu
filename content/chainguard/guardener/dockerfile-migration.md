---
title: "Chainguard Guardener Dockerfile Migration"
linktitle: "Dockerfile Migration"
description: "Use Chainguard Guardener to migrate, optimize, upgrade, and validate your Dockerfiles against Chainguard Containers with AI-driven, iterative conversion."
type: "article"
date: 2026-07-13T00:00:00+00:00
lastmod: 2026-07-13T00:00:00+00:00
draft: false
tags: ["GitHub", "AI", "Chainguard Containers"]
images: []
menu:
  docs:
    parent: "guardener"
weight: 050
toc: true
---

The Dockerfile migration feature converts your Dockerfiles to use Chainguard Containers. It uses AI to iteratively translate instructions, build images, compare results, and fix issues until the migrated Dockerfile works as expected.

Unlike the Guardener's [Actions Security](/chainguard/guardener/actions-security/) and [Commit Verification](/chainguard/guardener/commit-verification/) features, Dockerfile migration does not run through the GitHub App or the `.chainguard/` configuration directory. Instead, you drive it locally through `chainctl agent dockerfile` commands. The AI runs server-side and scans your workspace to perform its analysis, while Docker builds and file access remain local to your machine.

{{< beta feature="The Guardener" >}}

This page is a reference for the `chainctl agent dockerfile` commands. For a full walkthrough — including prerequisites, a step-by-step migration, available optimizers, a before-and-after example, and FAQ — see the [Dockerfile migration guide](/chainguard/migration/the-guardener/).

## How it works

The migration agent runs on Chainguard's servers, but it never touches your machine directly. Every file read, Docker build, and command is *requested* by the agent and mediated by `chainctl` on your machine. The local client evaluates each request, and only performs and returns the ones it deems acceptable — so you stay in control of what the agent can do and what data is sent back.

```text
   Your machine (client)                       Chainguard (server)
 ┌───────────────────────────┐               ┌──────────────────────┐
 │ chainctl                  │◀── request ───│   Migration agent    │
 │                           │  read a file, │        (AI)          │
 │  Dockerfile               │  run a build, │                      │
 │  build context            │  run a command│                      │
 │  Docker                   │               │                      │
 │        ▼                  │               │                      │
 │  evaluate request:        │               │                      │
 │  allowed?                 │               │                      │
 │        ▼                  │─── result ───▶│  analyzes result,    │
 │  perform locally,         │  (only for    │  plans next step     │
 │  return result            │   approved    │                      │
 │                           │   requests)   │                      │
 └───────────────────────────┘               └──────────────────────┘
```

Because every action is mediated by the local client, the agent can't read a file, run a build, or execute a command unless `chainctl` approves the request first.

## IAM access

Access to Dockerfile migration is governed by Chainguard IAM roles:

| Action                                                                                                   | Minimum role                 |
| -------------------------------------------------------------------------------------------------------- | ---------------------------- |
| Accepting the Guardener legal terms for your organization (required once before anyone can run sessions) | `guardener.admin` or `owner` |
| Running Dockerfile migration sessions                                                                    | `guardener.user`             |

See the [Built-in Roles and Capabilities Reference](/chainguard/administration/iam-organizations/roles-role-bindings/capabilities-reference/) for details.

## Commands

`chainctl agent dockerfile` includes the following subcommands:

| Command    | What it does                                          |
| ---------- | ----------------------------------------------------- |
| `build`    | Migrate a Dockerfile to a Chainguard equivalent image |
| `optimize` | Optimize an already-migrated Dockerfile               |
| `upgrade`  | Upgrade package versions in a Dockerfile              |
| `validate` | Validate a migrated Dockerfile                        |

To run a basic migration, provide the path to your Dockerfile and a target image tag:

```shell
chainctl agent dockerfile build -f Dockerfile \
  -t myapp:chainguard
```

For CI environments or automated workflows, use the `--non-interactive` flag to skip prompts and automatically select the first suggestion:

```shell
chainctl agent dockerfile build -f Dockerfile \
  --non-interactive
```

To optimize an already-migrated Dockerfile, run the `optimize` subcommand. Pass a comma-separated list to `--optimizers` to run only specific optimizers:

```shell
chainctl agent dockerfile optimize -f Dockerfile \
  --optimizers=cache,security
```

To upgrade outdated packages in a Dockerfile without modifying any files, combine `upgrade` with `--dry-run`:

```shell
chainctl agent dockerfile upgrade -f Dockerfile \
  --dry-run
```

For the complete set of usage examples, see [Usage examples](/chainguard/migration/the-guardener/#usage-examples) in the migration guide.

## Agent access

The Dockerfile migration agent runs server-side, but its access to your environment is scoped to what it needs to analyze and migrate a single Dockerfile:

- **Workspace analysis.** The agent scans your workspace to understand your Dockerfile and [build context](https://docs.docker.com/build/concepts/context/).
- **Analysis tools.** During a migration, the agent has access to tools for:
    - Searching `APKINDEX`.
    - Finding which package provides a given binary or library.
    - Comparing installed packages and filesystem layers between the original and migrated images.
    - Running commands in built images.
    - Reading build context files such as `requirements.txt`, `package.json`, and similar.
- **Interactive guidance.** If the agent cannot resolve an issue automatically, it prompts you for guidance with suggested alternatives. In `--non-interactive` mode it skips these prompts and automatically selects the first suggestion.

## Next steps

- **[Dockerfile migration guide](/chainguard/migration/the-guardener/)** — Full walkthrough, prerequisites, optimizers, and FAQ.
- **[Actions Security](/chainguard/guardener/actions-security/)** — Recommend and migrate GitHub Actions to hardened, SHA-pinned equivalents.
- **[Commit Verification](/chainguard/guardener/commit-verification/)** — Require cryptographically signed commits in pull requests.
