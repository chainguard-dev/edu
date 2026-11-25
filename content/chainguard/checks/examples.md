---
title: "Chainguard Checks examples"
date: 2026-11-12T14:46:46+00:00
lastmod: 2026-11-12T14:46:46+00:00
linktitle: "Examples"
description: "Complete Chainguard Checks configurations for Java with Maven, Rust, container image builds with Docker, a monorepo, and checks that use Postgres and Redis."
type: "article"
draft: false
tags: ["Chainguard Checks", "Configuration", "Examples"]
images: []
menu:
  docs:
    parent: "checks"
toc: true
weight: 33
---

This page gives complete Chainguard Checks configurations for common kinds of projects. Copy the one closest to your project, then change its packages, commands, and network access to match. Each example passes `chainctl checks validate`. For what each key does, refer to the [Chainguard Checks configuration reference](/chainguard/checks/configuration/), and for services and caches, refer to [Variations, inputs, services, and caches](/chainguard/checks/variations-services-caches/).

Keep the following in mind when you adapt an example:

- A check reaches only the hosts in its `network.egress` list. If your build downloads from somewhere else, such as a private package registry, add that host. Refer to [Find the hosts a check needs](/chainguard/checks/migrate-from-github-actions/#find-the-hosts-a-check-needs).
- A cache does nothing until your default branch's `.chainguard/ci/identities.yaml` file defines cache pools, as described in [Set up cache pools](/chainguard/checks/variations-services-caches/#set-up-cache-pools). The examples that use caches also run after merging, with `trigger: [presubmit, postsubmit]`, so that runs on your default branch fill the cache that pull requests start from.
- Chainguard Workspaces sessions can use these files for their packages, but they don't start services or mount caches other than `gobuild`. Refer to [Configure a Chainguard Workspaces session's environment](/chainguard/workspaces/session-environment/).

## Java with Maven {#java-with-maven}

This file installs a JDK and Maven, and runs the build's tests with `mvn verify`:

```yaml {title=".chainguard/ci.yaml"}
version: 1
environment:
  packages: [openjdk-21-default-jdk, maven-3.9]
  caches:
    java: {}
checks:
  test:
    cmd: mvn --batch-mode verify
    trigger: [presubmit, postsubmit]
    network:
      egress: [repo.maven.apache.org]
```

The example works as follows:

- `openjdk-21-default-jdk` installs OpenJDK 21 and sets `JAVA_HOME`, which Maven needs. For another Java version, use its package, such as `openjdk-25-default-jdk`.
- `--batch-mode` keeps Maven's download progress out of the check's log.
- Maven downloads plugins and dependencies from Maven Central, `repo.maven.apache.org`. Add any other repositories that your `pom.xml` or `settings.xml` names.
- The `java` cache keeps the files that Maven downloads, so later runs download only new ones. For Gradle builds, which still ask each repository for checksums, refer to [Cache types](/chainguard/checks/variations-services-caches/#cache-types).

## Rust {#rust}

This file installs a Rust toolchain and runs the project's tests:

```yaml {title=".chainguard/ci.yaml"}
version: 1
environment:
  packages: [rust-1.99, build-base]
  caches:
    cargo: {}
checks:
  test:
    cmd: cargo test --locked
    trigger: [presubmit, postsubmit]
    network:
      egress: [index.crates.io, static.crates.io]
```

The example works as follows:

- `rust-1.99` installs `rustc` and `cargo`. Choose the package for the Rust version your project uses. Chainguard Checks installs the toolchain from the package, not with `rustup`.
- `build-base` installs a C compiler and linker, which `rustc` uses to link binaries, and which crates with C code need.
- `--locked` makes the check fail if `Cargo.lock` doesn't match `Cargo.toml`, so commit `Cargo.lock`.
- Cargo reads the crates.io index from `index.crates.io` and downloads crates from `static.crates.io`.
- The `cargo` cache keeps downloaded crates and the build output in `target/`, so later runs rebuild only what changed. Refer to [Cache types](/chainguard/checks/variations-services-caches/#cache-types).

## Build a container image {#build-a-container-image}

To build an image from your repository's `Dockerfile`, run the Docker daemon as a service. This example uses the directory layout, with the `docker` service from [Run Docker](/chainguard/checks/variations-services-caches/#run-docker) in `.chainguard/ci/services/docker/`. Copy both of that section's files, `docker.yaml` and `docker.sh`. Then add a check file that uses the service:

```yaml {title=".chainguard/ci/image.yaml"}
version: 1
environment:
  services: [docker]
checks:
  build:
    script: |
      docker build --tag example:ci .
      docker run --rm example:ci
    network:
      egress:
        - cgr.dev
        - 9236a389bd48b984df91adc1bc924620.r2.cloudflarestorage.com
```

The check builds the image and then runs it once, so a container that can't start fails the check. The check appears on pull requests as `presubmit / image / build`.

The two hosts in `egress` serve images from `cgr.dev`, such as a `FROM cgr.dev/chainguard/wolfi-base` line in your `Dockerfile`. If your `Dockerfile` pulls from another registry or downloads files while it builds, add those hosts too. The Docker daemon needs root, so a check that uses the service must run as `root`, the default.

## A monorepo {#a-monorepo}

In a repository that holds several projects, give each project its own check file, and run each check only when its project changes. This example has a Go service in `services/api/` and a Node.js application in `web/`, and uses the directory layout:

```text
.chainguard/ci/
├── api.yaml
├── web.yaml
└── env/
    ├── go.yaml
    └── node.yaml
```

Each project's environment goes in its own file in `env/`:

```yaml {title=".chainguard/ci/env/go.yaml"}
version: 1
environment:
  packages: [go]
  caches:
    gobuild: {}
    gomod: {}
```

```yaml {title=".chainguard/ci/env/node.yaml"}
version: 1
environment:
  packages: [nodejs-22, npm]
```

Each check file names its environment, the project's directory, and the files that should run it:

```yaml {title=".chainguard/ci/api.yaml"}
version: 1
checks:
  test:
    environment: go
    cmd: go test ./...
    workdir: services/api
    trigger: [presubmit, postsubmit]
    when:
      changed: ["services/api/**", ".chainguard/ci/api.yaml", ".chainguard/ci/env/go.yaml"]
    network:
      egress: [proxy.golang.org, sum.golang.org]
```

```yaml {title=".chainguard/ci/web.yaml"}
version: 1
checks:
  test:
    environment: node
    workdir: web
    steps:
      - name: install
        cmd: npm ci
      - name: test
        cmd: npm test
    when:
      changed: ["web/**", ".chainguard/ci/web.yaml", ".chainguard/ci/env/node.yaml"]
    network:
      egress: [registry.npmjs.org]
```

The example works as follows:

- The checks appear on pull requests as `presubmit / api / test` and `presubmit / web / test`, so each project's result is separate.
- `workdir` runs each check's commands in its project's directory, relative to the repository's root.
- `when.changed` runs a check only when a pull request changes a file that matches one of its patterns. Each list includes the check's own configuration files, so a change to a check runs it. Refer to [Run when files change](/chainguard/checks/configuration/#run-when-files-change).
- Every check names its environment, so the directory needs no `env/default.yaml`.
- Only the Go check runs after merging, because only its environment has caches to fill.

## Postgres and Redis {#postgres-and-redis}

A check can start several services, such as a database and a cache, before its commands run. This example runs a Go project's integration tests against Postgres and Redis, in the directory layout:

```text
.chainguard/ci/
├── integration.yaml
└── services/
    ├── postgres/
    │   ├── postgres.yaml
    │   └── postgres.sh
    └── redis/
        ├── redis.yaml
        └── redis.sh
```

For the `postgres` service, copy both files from [Services](/chainguard/checks/variations-services-caches/#services). Define the `redis` service beside it:

```yaml {title=".chainguard/ci/services/redis/redis.yaml"}
version: 1
name: redis
packages: [busybox, redis-8.8, redis-cli-8.8]
cmd: [sh, ./redis.sh]
timeout: 60s
exports:
  REDIS_URL: redis://127.0.0.1:6379
```

The script starts Redis without saving data to disk, waits until it answers, prints `::service-ready::`, and then waits on Redis:

```shell {title=".chainguard/ci/services/redis/redis.sh"}
#!/bin/sh
set -eu
redis-server --bind 127.0.0.1 --port 6379 --save "" --appendonly no &
daemon=$!
trap 'kill "$daemon" 2>/dev/null || true' EXIT
trap 'exit 1' HUP INT TERM
until redis-cli -h 127.0.0.1 -p 6379 ping >/dev/null 2>&1; do
  kill -0 "$daemon" 2>/dev/null || exit 1
  sleep 0.1
done
printf '\n::service-ready::\n'
wait "$daemon"
exit 1
```

The check names both services in its environment:

```yaml {title=".chainguard/ci/integration.yaml"}
version: 1
environment:
  packages: [go]
  services: [postgres, redis]
checks:
  integration:
    cmd: go test ./integration/...
    network:
      egress: [proxy.golang.org, sum.golang.org]
```

The example works as follows:

- The check's commands start after both services print `::service-ready::`.
- The services' `exports` give the check's commands `PGHOST`, `PGUSER`, and `REDIS_URL`, so your tests can read their connection details from the environment.
- Both services listen on `127.0.0.1`, inside the check's VM, so the check needs no `egress` entry to reach them. Its `egress` list covers only the Go module downloads.
- The `redis-8.8` and `redis-cli-8.8` packages come from Chainguard's Extra Packages repository. Keep the two packages on the same version.
