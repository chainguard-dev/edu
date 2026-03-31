---
title: "The Guardener Dockerfile Agent"
linktitle: "The Guardener Dockerfile Agent"
type: "article"
description: "How to use The Guardener Dockerfile Agent to migrate your Dockerfiles to Chainguard Images using AI-driven iterative conversion"
date: 2026-03-30T00:00:00+00:00
lastmod: 2026-03-30T00:00:00+00:00
draft: false
tags: ["Guardener", "AI", "Chainguard Containers"]
images: []
menu:
  docs:
    parent: "migration"
weight: 030
toc: true
---

The Guardener migrates your Dockerfiles to use Chainguard Containers. It uses AI to iteratively convert instructions, build images, compare results, and fix issues until the Dockerfile works as expected.

You interact with it through `chainctl agent dockerfile` commands. The AI runs server-side, but all Docker builds and file access happen on your machine. Your source code never leaves your local environment.

> **Note:** The Guardener Dockerfile Agent is currently in beta. Features and behavior may change before general availability.


## Prerequisites

While The Guardener is in beta, your organization will need to sign up to use it. You can sign up for the beta from [The Guardener landing page](https://www.chainguard.dev/guardener).

Additionally, you will need the following in order to use The Guardener:

- `chainctl` installed on your local machine. Refer to our [installation guide](/chainguard/chainctl-usage/how-to-install-chainctl/) to set this up if you haven't already done so
- [Docker installed](https://docs.docker.com/engine/install/) and running locally
- You must have the `repo.create` capability within your Chainguard organization. Refer to our [Built-in Roles and Capabilities Reference](/chainguard/administration/iam-organizations/roles-role-bindings/capabilities-reference/) for more information
- Your Dockerfile and build context (source code and other inputs) must be present on the same machine where you run The Guardener

If you encounter permission errors, check your available groups and verify role bindings:

```shell
chainctl iam organizations list -o table

chainctl iam role-bindings create --parent <group-id> --identity <identity> --role <role-with-repo.create>
```


## Usage examples

`chainctl agent dockerfile` includes the following subcommands which you can use to interact with The Guardener:

| Command | What it does |
|---------|--------------|
| `build` | Migrate a Dockerfile to a Chainguard equivalent image |
| `optimize` | Optimize an already-migrated Dockerfile |
| `upgrade` | Upgrade package versions in a Dockerfile |
| `validate` | Validate a migrated Dockerfile |

The following examples demonstrate common usage of each subcommand.

To run a basic migration, provide the path to your Dockerfile and a target image tag:

```shell
chainctl agent dockerfile build -f Dockerfile \
  -t myapp:chainguard \
  --group <group-id>
```

If your image requires build arguments, pass them with `--build-arg`:

```shell
chainctl agent dockerfile build -f Dockerfile \
  -t myapp:chainguard \
  --build-arg VERSION=1.0 \
  --group <group-id>
```

For CI environments or automated workflows, you can use the `--non-interactive` flag to skip prompts and automatically select the first suggestion:

```shell
chainctl agent dockerfile build -f Dockerfile \
  --non-interactive \
  --group <group-id>
```

To resume a migration from a previously saved local state, use `--resume`:

```shell
chainctl agent dockerfile build -f Dockerfile \
  --resume \
  --group <group-id>
```

To optimize an already-migrated Dockerfile:

```shell
chainctl agent dockerfile optimize -f Dockerfile \
  --group <group-id>
```

To run only specific optimizers, pass a comma-separated list with `--optimizers`:

```shell
chainctl agent dockerfile optimize -f Dockerfile \
  --optimizers=cache,security \
  --group <group-id>
```

To upgrade outdated packages in a Dockerfile:

```shell
chainctl agent dockerfile upgrade -f Dockerfile \
  --group <group-id>
```

To preview what an upgrade would change without modifying any files, use the `--dry-run` flag:

```shell
chainctl agent dockerfile upgrade -f Dockerfile \
  --dry-run \
  --group <group-id>
```

To validate a migrated Dockerfile:

```shell
chainctl agent dockerfile validate -f Dockerfile \
  --group <group-id>
```


## What happens during a migration

During a migration, The Guardener performs the following steps:

1. **Parse** — reads your original Dockerfile.
2. **Translate** — the agent generates Chainguard equivalents for each instruction.
3. **Build & Compare** — builds both original and migrated images and compares them with [`syft`](https://github.com/anchore/syft) (an open source SBOM generator).
4. **Iterate** — if differences are found, the agent adjusts and retries.
5. **Validate** — runs functional tests to verify equivalence.

During this loop, the agent has access to tools for searching the Wolfi `APKINDEX`, finding which package provides a binary or library, comparing installed packages and filesystem layers, running commands in built images, and reading build context files (`requirements.txt`, `package.json`, etc.).

If the agent cannot resolve an issue automatically, it prompts you for guidance with suggested alternatives.

The entire loop can take from five to more than thirty minutes to complete, depending on the complexity of the Dockerfile.


## Available optimizers

When running the `optimize` subcommand, you can specify one or more of the following optimizers:

- `cache` — Reorders instructions for better layer caching. The order of instructions determines where the build cache is invalidated. Reordering to take better advantage of layer caching leads to faster builds and reduced CI consumption.
- `cleanup` — Removes duplicate and redundant instructions. For example, copying one file vs `COPY .`.
- `layers` — Combines `RUN` commands and merges package installs. Reducing the number of layers results in a smaller image, faster pull times, and lower CI minute consumption.
- `security` — Adds `--no-cache` to `apk`, flags secrets, and suggests a non-root `USER`. Skipping the `apk` cache layer reduces image size, and using a non-root user limits root access to the host and removes the ability to install new packages at runtime.
- `multi-stage` — Transforms the Dockerfile into a multi-stage build using Chainguard runtime images. Chainguard containers come in a `-dev` variant with a package manager and shell, and a distroless runtime variant. Splitting into multiple stages produces a smaller runtime image with a reduced attack surface.
- `native-packages` — Replaces `curl`/`bash` installs with native `apk` packages, ensuring full provenance of packages rather than just the resulting binary.


## Before and after example

The Guardener has been tested with Python, Go, Node.js, Java, Spring Boot (UBI-based), and multi-stage Argo CD builds. The following example shows a simple Ubuntu-based Dockerfile converted to use `cgr.dev/chainguard/wolfi-base:latest`.

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

You will need Docker installed and running locally, `chainctl` installed and authenticated, and a Chainguard organization that has joined the beta program.

### Can I run this in CI?

Yes. Use `--non-interactive` to skip all prompts, and ensure your CI environment has Docker and a `chainctl` authentication token.

### How long does it take?

The Guardener's `chainctl` commands can take anywhere from five to more than thirty minutes depending on the size and complexity of the Dockerfile. For example, the `optimize` subcommand takes longer than `build` because it performs a more in-depth analysis.

### Why did I get different results on a second run?

The Guardener is an AI-based tool, which means its behavior is inherently non-deterministic. You may see slightly different results across runs, even with the same inputs. This is expected.

The agent makes probabilistic decisions based on patterns in the data rather than following a fixed set of rules. As a result, it can take different but equally valid paths when analyzing a Dockerfile, choosing optimizations, or resolving build issues. The overall outcome should be consistent across runs, but the exact steps, suggestions, or ordering may vary.

### My session ended unexpectedly

A network interruption causes the bidirectional gRPC stream to terminate, ending the session immediately.

The `--resume` flag only resumes from locally saved migration state, not from the live session. The server-side agent, its conversation history, and any in-flight work are lost when the connection drops. There is currently no server-side session recovery.

### What if I don't have Docker?

Docker is required, since all builds happen on your local machine. A fully managed headless mode with server-side builds is planned for a future release.
