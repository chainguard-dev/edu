---
title: "Variations, inputs, services, and caches in Chainguard Checks"
linktitle: "Variations, services, and caches"
description: "Run a Chainguard Checks check once per variation, pass files between checks, check out another repository, start services such as a database, run checks as another user, and reuse Go build output with caches."
type: "article"
date: 2026-10-12T00:00:00+00:00
lastmod: 2026-10-13T00:00:00+00:00
draft: false
tags: ["Chainguard Checks", "Configuration", "Reference"]
images: []
menu:
  docs:
    parent: "checks"
toc: true
weight: 32
---

Most checks need only the keys that the [Chainguard Checks configuration reference](/chainguard/checks/configuration/) describes. This page describes the keys for checks that need more: running a check once for each of several variations, passing files between checks, starting services such as a database, running as an unprivileged account, and reusing build output from earlier runs.

## Run a check once per variation

The `foreach` key runs a check once for each entry in a list, each in its own VM. All of a check's variations report as one GitHub check. For example, this check runs three variations, two at a time:

```yaml
checks:
  test:
    script: go test -tags "$TAGS" ./...
    vars:
      TAGS: unit
    network:
      egress: [proxy.golang.org, sum.golang.org]
    parallelism: 2
    foreach:
      - name: api
        workdir: api
      - name: api-integration
        workdir: api
        vars:
          TAGS: integration
        timeout: 30m
      - name: cli
        workdir: cli
        resources: medium
```

The `parallelism` key sets how many variations can run at once. Each entry can set the following keys. Any other key, such as `cmd` or `needs`, makes the configuration invalid.

| Key | Description |
| --- | ----------- |
| `name` | The variation's name. Every entry's name must be different. |
| `vars` | Variables that override the check's `vars` with the same names. Each value can be up to 1,024 bytes. |
| `workdir` | The directory to run in, in place of the check's `workdir`. |
| `resources` | The resource class, in place of the check's. |
| `timeout` | The time limit, in place of the check's. |
| `when` | Conditions for the variation, which apply after the check's own `when`. They can't use `requested`. |
| `network` | An `egress` list that replaces the check's for this variation. It can list only hosts that the check's `egress` allows, and `egress: []` gives the variation no network access. Without it, the variation uses the check's `network`. |

An entry's values reach the check's commands only as environment variables and as the working directory. A `cmd` doesn't expand variables, so read them in a `script`, as in the example. An entry without a `name` is named after its `vars` values, sorted by variable name and joined with `-`. Set `name` when a value has characters that a name can't have, such as `:`, `=`, or `@`, or when it doesn't start and end with a letter or digit. `foreach: []` runs no variation.

### Compute variations during a run

To compute the variations during the run, such as one for each module in your repository, define a planner under the top-level `plans` key and set the check's `foreach` to `plans.<name>`:

```yaml {title=".chainguard/ci.yaml"}
version: 1
environment:
  packages: [go]
plans:
  modules:
    environment:
      packages: [bash, git]
    cmd: ./ci/list-modules.sh
checks:
  test:
    foreach: plans.modules
    cmd: go test ./...
    network:
      egress: [proxy.golang.org, sum.golang.org]
```

The planner runs once, before the checks that use it, and writes its variations as JSON to the file that the `CG_PLAN` environment variable names. Each variation can have the same keys as a `foreach` entry, except that its `when` can hold only `changed`. For example, `ci/list-modules.sh` could write the following:

```json
[{"name": "api", "workdir": "api"}, {"name": "cli", "workdir": "cli"}]
```

A planner works as follows:

- It needs its own `environment` and a `cmd`, and can have a `network`. Its environment can't name caches. Without `network`, it has no network access.
- It runs in a VM with your repository, with `CHAINGUARD_BASE_REVISION` set the same way as for a check, and can run for up to five minutes.
- It can write a JSON array of variations, or an object of named arrays, such as `{"unit": [...], "integration": [...]}`. A check uses one array with `foreach: plans.<name>.<group>`, such as `plans.modules.unit`.
- A variation's `network` can only narrow the check's, as for a `foreach` entry.
- A variation without a `name` is named `shard-1`, `shard-2`, and so on. An empty array runs no variation of the check.
- Its output can be up to 1 MiB, with up to 1,000 variations across all arrays and names up to 128 bytes. If the planner fails or writes output that breaks these rules, the checks that use it don't run and report a failed dependency. If every check that uses it is advisory, a failed planner doesn't block merging.
- A check can use a planner only from the same file. Planner names use letters, digits, `_`, and `-`, start with a letter, and can be up to 128 characters.

## Inputs and outputs

A check can save a directory for later checks in the same run with `outputs`, and add files to its VM with `inputs`, either from another check's output or from another repository.

### Pass files between checks

To pass files from one check to another, declare an output on the check that writes them, and an input with `from` on the check that reads them:

```yaml
checks:
  build:
    cmd: go build -o out/ ./cmd/...
    outputs:
      bin:
        path: out
    network:
      egress: [proxy.golang.org, sum.golang.org]
  smoke:
    cmd: bin/app --version
    inputs:
      - path: bin
        from: {check: build, output: bin}
```

In this example, `build` writes its binaries to `out/`, and `smoke` runs one of them from `bin/` after `build` passes. Inputs and outputs work as follows:

- An output's `path` is a directory relative to the repository's root. It starts empty, and your repository must not have files at that path, or the run fails.
- After the producing check passes, the consuming check gets a read-only copy of the output at its input's `path`.
- `from` works like `needs`: the producing check must be in the same file and run on the same triggers, and the consuming check waits for it and doesn't run if it fails. The same limits as for `needs` apply, as described in [Advisory checks](/chainguard/checks/configuration/#advisory-checks).
- If the producing check has `foreach` variations, the input holds one subdirectory for each variation, named after the variation, with `/` written as `%2F`.
- A check that [runs as another user](#run-as-another-user) can't declare outputs.
- A check can declare up to 32 outputs and read up to 32 outputs of other checks. Each output can hold up to 10,000 files and directories and 64 MiB. Output names can't contain `.` or `/`, and inputs and outputs can't overlap each other or `.git`.

Outputs pass files only between checks in a run. You can't download them.

### Check out another repository

To add another repository's files to a check's VM, use an input with `git`:

```yaml
checks:
  integration:
    cmd: go test ./integration/...
    inputs:
      - path: fixtures
        git:
          repo: https://github.com/acme/fixtures
          ref: main
```

Chainguard Checks fetches the repository outside the VM, so the check doesn't need network access for it. The repository must be public, and `repo` must be an `https://github.com` URL. Chainguard Checks resolves `ref`, a branch, tag, or commit SHA, to a commit when it creates the run. Without `ref`, it uses the repository's default branch. The files arrive at `path` without a `.git` directory.

If the repository is private or the ref doesn't exist, the summary check shows **Run creation failed**. `chainctl checks validate` can't check either of these offline.

## Services

A service is a process, such as a database, that Chainguard Checks starts in a check's VM before the check's commands run. In the directory layout, define each service in `.chainguard/ci/services/<name>/<name>.yaml`, with the script that starts it in the same directory:

```yaml {title=".chainguard/ci/services/postgres/postgres.yaml"}
version: 1
name: postgres
packages: [busybox, postgresql-18, postgresql-18-client, su-exec]
cmd: [sh, ./postgres.sh]
timeout: 60s
inputs:
  port:
    type: integer
    default: "5432"
    env: PGPORT
exports:
  PGHOST: 127.0.0.1
  PGUSER: postgres
```

The script starts the database, waits until it accepts connections, prints `::service-ready::`, and then waits on the database:

```shell {title=".chainguard/ci/services/postgres/postgres.sh"}
#!/bin/sh
set -eu
: "${PGDATA:=/tmp/postgres}"
: "${PGPORT:=5432}"
export PGDATA PGPORT
# PostgreSQL refuses to run as root, so run it as a postgres account.
if [ "$(id -u)" = 0 ]; then
  id postgres >/dev/null 2>&1 || adduser -S -D -H -s /bin/sh postgres
  mkdir -p "$PGDATA"
  chown postgres "$PGDATA"
  chmod 700 "$PGDATA"
  exec su-exec postgres sh "$0"
fi
if [ ! -f "$PGDATA/PG_VERSION" ]; then
  initdb --no-sync --pgdata="$PGDATA" --username=postgres --auth=trust --encoding=UTF8 --locale=C
fi
postgres -D "$PGDATA" -h 127.0.0.1 -p "$PGPORT" -k "$PGDATA" &
daemon=$!
trap 'kill "$daemon" 2>/dev/null || true' EXIT
trap 'exit 1' HUP INT TERM
until pg_isready -h 127.0.0.1 -p "$PGPORT" -U postgres >/dev/null 2>&1; do
  kill -0 "$daemon" 2>/dev/null || exit 1
  sleep 0.1
done
printf '\n::service-ready::\n'
wait "$daemon"
exit 1
```

A check uses the service by naming it in its environment's `services`:

```yaml {title=".chainguard/ci/db.yaml"}
version: 1
environment:
  packages: [go]
  services: [postgres]
checks:
  integration:
    cmd: go test ./db/...
    network:
      egress: [proxy.golang.org, sum.golang.org]
```

A service works as follows:

- Chainguard Checks adds the service's `packages` to the environment, and runs its `cmd` without a shell, from the directory of the file that defines it.
- The command must stay in the foreground, and print `::service-ready::` on a line of its own to standard output when the service is ready. The check's commands start after every service is ready.
- If a service isn't ready within its `timeout`, which defaults to one minute, or its command exits while the check runs, the check fails. Chainguard Checks never restarts a service.
- The service's output appears in the check's log.
- Connections to `127.0.0.1` stay inside the VM, so a check doesn't need a `network` entry to reach its services.
- `exports` become environment variables for the check's commands and the service. `inputs` turn values that a check passes with `with` into environment variables that only the service's command gets.
- A definition can be up to 64 KiB. Service names use lowercase letters, digits, and `-`, start with a letter, and can be up to 63 characters.

To run a service under another name, or to pass it inputs, use a mapping with `uses`, `name`, and `with`:

```yaml
environment:
  packages: [go]
  services:
    - uses: postgres
      name: db
      with:
        port: "5433"
```

Services in `services/` need the directory layout. In the single-file layout, define a service inline, with the same keys as a definition file. Its command runs from the `.chainguard/` directory, which can hold only `.yaml` files, so keep its script elsewhere in your repository:

```yaml {title=".chainguard/ci.yaml"}
version: 1
environment:
  packages: [go]
  services:
    - name: postgres
      packages: [busybox, postgresql-18, postgresql-18-client, su-exec]
      cmd: [sh, ../ci/postgres.sh]
      exports:
        PGHOST: 127.0.0.1
        PGUSER: postgres
checks:
  integration:
    cmd: go test ./db/...
    network:
      egress: [proxy.golang.org, sum.golang.org]
```

## Run as another user

By default, a check's commands run as `root`. To run them as an unprivileged account, set `user` to the account's name:

```yaml
checks:
  test:
    cmd: go test ./...
    user: build
```

Chainguard Checks creates the account with UID and GID 65532 and the home directory `/home/<name>`, and makes it the owner of `/work`. A name uses lowercase letters, digits, `_`, and `-`, starts with a lowercase letter or `_`, and can be up to 32 characters.

Don't use a name that the VM already has: `bin`, `daemon`, `adm`, `lp`, `sync`, `shutdown`, `halt`, `mail`, `news`, `uucp`, `operator`, `man`, `postmaster`, `cron`, `ftp`, `sshd`, or `nobody`. `chainctl checks validate` accepts these names, but the run refuses them. A check also fails to start if one of its packages creates an account with the same name.

The account owns `/work`, but not your repository's files and `.git` directory, so `git` refuses to work in `/work` because of their ownership. For a check that runs `git`, mark the repository as safe with Git's configuration variables:

```yaml
checks:
  test:
    cmd: go test ./...
    user: build
    vars:
      GIT_CONFIG_COUNT: "1"
      GIT_CONFIG_KEY_0: safe.directory
      GIT_CONFIG_VALUE_0: "*"
```

A check that runs as another user can't declare `outputs`. A check that uses a [cache](#caches) must run as `build`.

## Caches

By default, each check starts with nothing from earlier runs, so a Go check compiles every package on every run. A check can reuse build output from earlier runs through a cache that its environment names under `caches`. During the beta, only the Go build cache, `gobuild`, stores anything. The `gomod`, `python`, `node`, and `directory` caches pass validation but cache nothing, so keep the hosts that your tools download from in `egress`.

### Build caches

To reuse Go build output, name `gobuild` in the environment, and set `user: build` on each check that uses the environment:

```yaml {title=".chainguard/ci.yaml"}
version: 1
environment:
  packages: [go]
  caches:
    gobuild: {}
checks:
  test:
    cmd: go test ./...
    user: build
    trigger: [presubmit, postsubmit]
    network:
      egress: [proxy.golang.org, sum.golang.org]
```

The cache does nothing until your default branch defines cache pools, as described in [Set up cache pools](#set-up-cache-pools). A Go build cache works as follows:

- `gobuild: {}` takes no settings, and the environment's packages must include `go` or a `go-<version>` package.
- Every check in an environment that names a cache must set `user: build`, so its commands run as an unprivileged account, as described in [Run as another user](#run-as-another-user). A command that needs root fails. In the directory layout, give the checks that use a cache an environment of their own.
- Chainguard Checks sets `GOCACHE` to the cache's directory, so don't set `GOCACHE` in `vars`.
- Chainguard Checks adds `-count=1` to `GOFLAGS`, so `go test` always runs your tests, and only build output is reused.
- A cache fills only from checks that pass. To fill the cache that pull requests start from, run the check after merging too, with `trigger: [presubmit, postsubmit]`.
- Go modules still download on every run, so keep `proxy.golang.org` and `sum.golang.org` in `egress`.

### Set up cache pools

Chainguard Checks mounts a cache only from a *cache pool*, which you define in the `trust` section of `.chainguard/ci/identities.yaml` on your default branch. Each pool lists the [rings](/chainguard/checks/identity-and-trust/#rings) whose runs share it, so pull requests from people you don't trust can't change the build output that your default branch's runs reuse. This file defines two pools:

```yaml {title=".chainguard/ci/identities.yaml"}
version: 1
trust:
  groups:
    members:
      github: {org: acme}
  subrings:
    member:
      authors: [members]
  github_token: 1.member
  cache:
    trunk:
      rings: [2]
    trusted:
      rings: [1.member]
      seed: trunk
identities: {}
```

With this file, runs after merging, which are in ring `2`, read and write the `trunk` pool. Pull requests opened by members of the `acme` GitHub organization, which are in ring `1.member`, read and write the `trusted` pool, and also start from a read-only copy of `trunk`, which `seed` names. Other pull requests are in ring `0` and get no cache, because no pool lists ring `0`.

Pools follow these rules:

- A pool's name uses lowercase letters, digits, and `-`, and starts with a letter. Each pool lists one or more `rings`, and a ring can be in at most one pool.
- A `seed` must name a pool whose `rings` are exactly `[2]`, and which has no seed of its own.
- Changing a pool's `rings`, or raising its optional `generation` number, starts the pool empty.
- Chainguard Checks reads the pools from your default branch, so the pull request that adds or changes them runs with the pools your default branch had before it.
- [Chainguard Workspaces sessions](/chainguard/workspaces/session-environment/#start-with-a-warm-go-build-cache) started with `--cache` read only a pool whose `rings` are exactly `[2]`.

A `trust` section that you add for caches also applies to workload identities, so every identity in the file then needs a `ring`. For the section's other keys, refer to [Limit which pull requests get an identity](/chainguard/checks/identity-and-trust/#limit-which-pull-requests-get-an-identity).

To see what each check would mount in each pool, run `chainctl checks explain`.

### Who can read and write a cache

Cache pools keep a pull request from changing the build output that other runs use:

- Your default branch's `identities.yaml` decides which pool a pull request's run uses, so a pull request can't change its own pool.
- A ring in no pool gets no cache. With separate pools for ring `2` and for a subring, as in the example, pull requests from members read your default branch's cache through the seed but never write to it. Put ring `2` and a subring in the same pool only if you trust every author in that subring with the cache that your default branch's runs use.
- A pool that lists ring `0` keeps a separate cache for each pull request, and runs after merging don't use it.
- Only checks that pass, and aren't canceled, add to a pool.
- A check that uses a workload identity, or whose outputs feed a check that does, never adds to a pool. It reads a pool only if every ring in the pool can get the same identities.
- Workspaces sessions never add to a pool.

If you suspect a pool holds bad output, raise its `generation` to start it empty.

### How caches fill

A pool fills and empties as follows:

- A new pool starts empty. Chainguard Checks adds the build output of passing checks to it about every 15 minutes at most, so a pool warms up over several runs.
- Each check adds up to 2 GiB and 200,000 files and directories to each cache.
- A pool holds up to about 128 GiB. Chainguard Checks drops entries that no run uses for about three weeks.
- When a pull request closes, Chainguard Checks deletes its cache in a pool that lists ring `0`.
- **Re-run** on GitHub and `chainctl checks rerun` run every check without a cache.
