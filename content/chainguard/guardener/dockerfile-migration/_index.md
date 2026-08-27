---
title: "Chainguard Guardener Dockerfile migration"
linktitle: "Dockerfile migration"
description: "Use Chainguard Guardener to migrate, optimize, upgrade, and validate your Dockerfiles against Chainguard Containers with AI-driven, iterative conversion."
aliases:
- /chainguard/migration/the-guardener/
- /get-started/migration/the-guardener/
type: "article"
date: 2026-07-13T00:00:00+00:00
lastmod: 2026-08-11T00:00:00+00:00
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

Unlike the Guardener's [Hardened Actions](/chainguard/guardener/github/actions-security/) and [Commit Verification](/chainguard/guardener/github/commit-verification/) features, Dockerfile migration does not run through the GitHub App or the `.chainguard/` configuration directory. Instead, you drive it locally through `chainctl agent dockerfile` commands. The AI runs server-side and scans your workspace to perform its analysis, while Docker builds and file access remain local to your machine.

{{< beta feature="The Guardener" >}}

## Prerequisites

While Dockerfile migration is in beta, your organization needs to join the waitlist. Chainguard will notify you once registration becomes available. You can sign up on [The Guardener landing page](https://www.chainguard.dev/guardener).

You also need the following:

- `chainctl` installed on your local machine. Refer to our [installation guide](/chainguard/chainctl-usage/how-to-install-chainctl/) to set this up if you haven't already done so.
- [Docker installed](https://docs.docker.com/engine/install/) and running locally.
- Your Dockerfile and build context (source code and other inputs) present on the same machine where you run the migration.
- A user with permission to accept the Guardener legal terms must accept them for your organization before anyone can run a session. Refer to [IAM access](#iam-access) below for the roles involved.

If you encounter permission errors, check your available groups and verify role bindings:

```shell
chainctl iam organizations list -o table

chainctl iam role-bindings create --parent <group-id> --identity <identity> --role <role-with-repo.create>
```

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

### Migration steps

During a migration, the agent performs the following steps:

1. **Parse** — reads your original Dockerfile.
2. **Translate** — generates Chainguard equivalents for each instruction.
3. **Build and compare** — builds both the original and migrated images and compares them with [`syft`](https://github.com/anchore/syft), an open source SBOM generator.
4. **Iterate** — if differences are found, adjusts and retries.
5. **Validate** — runs functional tests to verify equivalence.

If the agent cannot resolve an issue automatically, it prompts you for guidance with suggested alternatives.

The entire loop takes from five to more than thirty minutes, depending on the complexity of the Dockerfile.

## IAM access

Access to Dockerfile migration is governed by Chainguard IAM roles:

| Action                                                                                                   | Minimum role                 |
| -------------------------------------------------------------------------------------------------------- | ---------------------------- |
| Accepting the Guardener legal terms for your organization (required once before anyone can run sessions) | `guardener.admin` or `owner` |
| Running Dockerfile migration sessions                                                                    | `guardener.user`             |

Refer to the [Built-in roles and capabilities reference](/chainguard/administration/iam-organizations/roles-role-bindings/capabilities-reference/) for details.

## Commands

`chainctl agent dockerfile` includes the following subcommands:

| Command    | What it does                                          |
| ---------- | ----------------------------------------------------- |
| `build`    | Migrate a Dockerfile to a Chainguard equivalent image |
| `optimize` | Optimize an already-migrated Dockerfile               |
| `upgrade`  | Upgrade package versions in a Dockerfile              |
| `validate` | Validate a migrated Dockerfile                        |

### Usage examples

To run a basic migration, provide the path to your Dockerfile and a target image tag:

```shell
chainctl agent dockerfile build -f Dockerfile \
  -t myapp:chainguard
```

If your image requires build arguments, pass them with `--build-arg`:

```shell
chainctl agent dockerfile build -f Dockerfile \
  -t myapp:chainguard \
  --build-arg VERSION=1.0
```

For CI environments or automated workflows, use the `--non-interactive` flag to skip prompts and automatically select the first suggestion:

```shell
chainctl agent dockerfile build -f Dockerfile \
  --non-interactive
```

To resume a migration from a previously saved local state, use `--resume`:

```shell
chainctl agent dockerfile build -f Dockerfile \
  --resume
```

To optimize an already-migrated Dockerfile:

```shell
chainctl agent dockerfile optimize -f Dockerfile
```

To run only specific optimizers, pass a comma-separated list with `--optimizers`:

```shell
chainctl agent dockerfile optimize -f Dockerfile \
  --optimizers=cache,security
```

To upgrade outdated packages in a Dockerfile:

```shell
chainctl agent dockerfile upgrade -f Dockerfile
```

To preview what an upgrade would change without modifying any files, use the `--dry-run` flag:

```shell
chainctl agent dockerfile upgrade -f Dockerfile \
  --dry-run
```

To validate a migrated Dockerfile:

```shell
chainctl agent dockerfile validate -f Dockerfile
```

## Available optimizers

When running the `optimize` subcommand, you can specify one or more of the following optimizers:

- `cache` — Reorders instructions for better layer caching. The order of instructions determines where the build cache is invalidated. Reordering to take better advantage of layer caching leads to faster builds and reduced CI consumption.
- `cleanup` — Removes duplicate and redundant instructions. For example, copying one file vs `COPY .`.
- `layers` — Combines `RUN` commands and merges package installs. Reducing the number of layers results in a smaller image, faster pull times, and lower CI minute consumption.
- `security` — Adds `--no-cache` to `apk`, flags secrets, and suggests a non-root `USER`. Skipping the `apk` cache layer reduces image size, and using a non-root user limits root access to the host and removes the ability to install new packages at runtime.
- `multi-stage` — Transforms the Dockerfile into a multi-stage build using Chainguard runtime images. Chainguard containers come in a `-dev` variant with a package manager and shell, and a distroless runtime variant. Splitting into multiple stages produces a smaller runtime image with a reduced attack surface.
- `native-packages` — Replaces `curl`/`bash` installs with native `apk` packages, ensuring full provenance of packages rather than just the resulting binary.

## Agent access

The migration agent runs server-side, but its access to your environment is scoped to what it needs to analyze and migrate a single Dockerfile:

- **Workspace analysis.** The agent scans your workspace to understand your Dockerfile and [build context](https://docs.docker.com/build/concepts/context/).
- **Analysis tools.** During a migration, the agent has access to tools for:
    - Searching the Wolfi `APKINDEX`.
    - Finding which package provides a given binary or library.
    - Comparing installed packages and filesystem layers between the original and migrated images.
    - Running commands in built images.
    - Reading build context files such as `requirements.txt`, `package.json`, and similar.
- **Interactive guidance.** If the agent cannot resolve an issue automatically, it prompts you for guidance with suggested alternatives. In `--non-interactive` mode it skips these prompts and automatically selects the first suggestion.

## Before and after example

Dockerfile migration has been tested with Python, Go, Node.js, Java, Spring Boot (UBI-based), and multi-stage Argo CD builds. The following example shows a simple Ubuntu-based Dockerfile converted to use `cgr.dev/chainguard/wolfi-base:latest`.

### Before

```Dockerfile
FROM ubuntu:22.04
RUN apt-get update && apt-get install -y curl git python3
WORKDIR /app
COPY . .
CMD ["python3", "app.py"]
```

### After

```Dockerfile
FROM cgr.dev/chainguard/wolfi-base:latest
RUN apk add --no-cache curl git python3
WORKDIR /app
COPY . .
CMD ["python3", "app.py"]
```

## FAQ

### What do I need to get started?

You need Docker installed and running locally, `chainctl` installed and authenticated, and a Chainguard organization that has joined the beta program.

### Can I run this in CI?

Yes. Use `--non-interactive` to skip all prompts, and ensure your CI environment has Docker and a `chainctl` authentication token.

### How long does it take?

The `chainctl agent dockerfile` commands can take anywhere from five to more than thirty minutes depending on the size and complexity of the Dockerfile. For example, the `optimize` subcommand takes longer than `build` because it performs a more in-depth analysis.

### Why did I get different results on a second run?

Dockerfile migration is AI-based, which means its behavior is inherently non-deterministic. You may see slightly different results across runs, even with the same inputs. This is expected.

The agent makes probabilistic decisions based on patterns in the data rather than following a fixed set of rules. As a result, it can take different but equally valid paths when analyzing a Dockerfile, choosing optimizations, or resolving build issues. The overall outcome should be consistent across runs, but the exact steps, suggestions, or ordering may vary.

### My session ended unexpectedly

A network interruption causes the bidirectional gRPC stream to terminate, ending the session immediately.

The `--resume` flag only resumes from locally saved migration state, not from the live session. The server-side agent, its conversation history, and any in-flight work are lost when the connection drops. There is currently no server-side session recovery.

### What if I don't have Docker?

Docker is required, since all builds happen on your local machine. A fully managed headless mode with server-side builds is planned for a future release.

## Next steps

- **[Migrating to Chainguard Containers](/chainguard/containers/migration/)** — Manual migration guidance, compatibility charts, and per-language guides.
- **[Dockerfile Converter (dfc)](/chainguard/containers/migration/dockerfile-conversion/)** — A deterministic, open source alternative for converting Dockerfiles.
- **[Hardened Actions](/chainguard/guardener/github/actions-security/)** — Recommend and migrate GitHub Actions to hardened, SHA-pinned equivalents.
- **[Commit Verification](/chainguard/guardener/github/commit-verification/)** — Require cryptographically signed commits in pull requests.
