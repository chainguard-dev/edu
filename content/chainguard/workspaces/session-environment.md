---
title: "Configure a Chainguard Workspaces session's environment"
linktitle: "Session environment"
description: "Choose the packages, tools, and network access a Chainguard Workspaces session gets, from your repository's .chainguard/develop.yaml or .chainguard/ci.yaml file, a file of your own, or the default environment."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-13T15:17:49+00:00
draft: false
tags: ["Chainguard Workspaces", "Configuration", "Reference"]
images: []
menu:
  docs:
    parent: "workspaces"
toc: true
weight: 40
---

A Chainguard Workspaces session's *environment* is the set of packages installed in its VM and the network access it has. Packages come from Chainguard OS, the same packages behind Chainguard Containers. This page explains where a session's environment comes from and how to change it.

A session's environment is fixed when the session is created. If your repository's `.chainguard/develop.yaml` or `.chainguard/ci.yaml` file changes afterward, existing sessions keep the environment they started with, and `chainctl` reminds you when you return to them. To use the new environment, open a new session with `chainctl develop --new`.

## How a session chooses its environment {#how-a-session-chooses-its-environment}

When `chainctl develop` creates a session, it chooses the environment in the following order:

1. The environment you choose with `--env`, if any: a file, `default`, or `generate`.
2. The check you name with `--check`, if it isn't `develop`. The session uses that check's environment and network access.
3. Your repository's `.chainguard/develop.yaml` file, if it has one.
4. Your repository's `.chainguard/ci.yaml` file, if it has one.
5. The default environment.

The order is the same for a session opened from a local directory and one opened from a repository URL, with one exception: from a local directory, `--check` can name only a check in `.chainguard/ci.yaml`. In a repository that uses the `.chainguard/ci/` directory layout, open the session from the repository URL to use `--check`, for example `chainctl develop github.com/acme/app --check test`. For a local directory, `chainctl` reads the files from your working tree, including changes you haven't committed. For a repository URL, the files come from the repository's default branch.

If your repository has neither a `.chainguard/develop.yaml` nor a `.chainguard/ci.yaml` file and you don't pass `--env`, `chainctl` opens the session on the default environment and tells you so. When you run `chainctl develop` with `--non-interactive`, it refuses instead, so pass `--env default` explicitly in scripts.

Whatever its environment, every session also gets `git`, `gh`, `chainctl`, `curl`, `bash`, `bash-completion`, `busybox`, and `gnutar`. Nothing else is installed unless the environment lists it, including Claude Code (`claude`). By default, the session's shell and each terminal you open from the session menu run `bash`, with completion and a history file at `~/.bash_history`. `bash` reads `~/.bashrc` last, if you create one in the session, so your own settings take precedence.

`chainctl` never writes to your directory. To find out which environment a session uses, read `/etc/chainguard/session.yaml` in the session. To see each session's environment from your laptop, run `chainctl develop list -o wide`.

## The default environment

The default environment is a general-purpose shell with the following packages:

- `bash`, `coreutils`, `make`, `curl`, and `git`
- `apk-tools`, so you can install more packages from the shell
- `claude`, the Claude Code CLI
- `gh`, `jq`, `ripgrep`, `less`, and `vim`
- `google-cloud-sdk`
- `chainctl`

The default environment reaches the open internet. To open a session on the default environment even when your repository has a `.chainguard/develop.yaml` or `.chainguard/ci.yaml` file, pass `--env default`:

```shell
chainctl develop --env default --parent $ORGANIZATION
```

The default environment doesn't include language toolchains. To add one to the current session, install it with `apk`. This example installs Python 3.13:

```shell
apk add python-3.13
```

To find a package's name, ask a coding agent in the session. Every session configures the [`cg-apk`](/platform/mcp-servers/cg-apk/) MCP server, which looks up APK packages.

Packages you install with `apk` last for the life of the session, including when it parks and resumes, but new sessions don't get them. To install packages in every new session, list them in a `.chainguard/develop.yaml` file.

## Use a .chainguard/develop.yaml file {#use-a-chainguarddevelopyaml-file}

A `.chainguard/develop.yaml` file sets up sessions and nothing else. Chainguard Checks doesn't run anything from it, so changing it doesn't change your checks.

The file can take its environment from your checks. In a repository that uses the `.chainguard/ci/` directory layout, this example gives sessions the same environment as the checks in `.chainguard/ci/go.yaml`, and adds Claude Code:

```yaml {title=".chainguard/develop.yaml"}
version: 1
from: .chainguard/ci/go.yaml
environment:
  packages: [claude]
```

The `from` key can't name `.chainguard/ci.yaml`, so in a repository that uses the single-file layout, declare the environment in the file itself. This example also gives sessions a larger disk:

```yaml {title=".chainguard/develop.yaml"}
version: 1
environment:
  packages: [go, git, claude]
resources: {cpus: 4, memory: 16Gi, disk: 100Gi}
```

The file accepts only the following keys:

| Key | Required | Description |
| --- | -------- | ----------- |
| `version` | Yes | The format version. Must be `1`. |
| `from` | No | A check file, such as `.chainguard/ci/go.yaml`, or an environment file, such as `.chainguard/ci/env/go.yaml`. Sessions take only the file's top-level `environment`, or the environment file that it names. |
| `environment` | Unless you set `from` | Without `from`, the session's environment, in the [same format](/chainguard/checks/configuration/#environment) as a Chainguard Checks file, except that it can't name `caches`. With `from`, only `packages` to add and `vars` to set, which replace any variables with the same name. |
| `resources` | No | The session's size: `cpus`, `memory`, and `disk` together, or a resource class. Refer to [Resources](#resources). |
| `shell` | No | The shell that the session's terminals run: a program name on the session's `PATH`, such as `zsh`, or an absolute path, such as `/bin/zsh`, with no arguments. Without it, the shell is `bash`. The session's environment must include the shell's package. If the session can't find the shell, it starts `bash`. `chainctl` 0.2.382 or earlier refuses this key in a session opened from a local directory. |

Keep the following in mind when you write the file:

- The file has no `network` key, so a session that uses it reaches the open internet. To limit a session to an `egress` list, open it with `--check` on a check that has one. In the `.chainguard/ci/` layout, do this from a repository URL. Refer to [Network access](#network-access).
- If your repository uses Chainguard Checks, a pull request that changes the file gets an advisory check that tests it, as described in [File layouts](/chainguard/checks/configuration/#file-layouts).

## Use your repository's .chainguard/ci.yaml file

If your repository uses [Chainguard Checks](/chainguard/checks/overview/), its `.chainguard/ci.yaml` file already declares the packages your checks need, and sessions use the same packages. If your repository doesn't use Chainguard Checks, you can still add the file to give sessions the right tools.

This example `.chainguard/ci.yaml` file installs Go, `git`, and Claude Code, and defines two checks:

```yaml {title=".chainguard/ci.yaml"}
version: 1
environment:
  packages: [go, git, claude]
checks:
  vet:
    cmd: go vet ./...
    network:
      egress: [proxy.golang.org, sum.golang.org]
  test:
    cmd: go test ./...
    network:
      egress: [proxy.golang.org, sum.golang.org]
```

A session opened on this repository installs the packages listed under `environment`. In the session, `run-ci` runs the `vet` and `test` checks against your working tree. Refer to the [Chainguard Checks configuration reference](/chainguard/checks/configuration/) for the full file format.

Keep the following in mind when you write the file for sessions:

- A session uses the environment of a check named `develop` if the file has one. Otherwise, it uses the file's top-level `environment`.
- To open a session with a specific check's environment, including that check's network access, pass `--check` with the check's name. In the example, `chainctl develop --check test` opens a session that can reach only the Go module proxy and checksum database.
- The `run-ci` command runs your checks in the session's own environment, not in the environment each check declares, and skips checks that only a pull request can run, as described in [How run-ci differs from a pull request run](/chainguard/checks/run-checks/#how-run-ci-differs-from-a-pull-request-run).
- If your repository uses the `.chainguard/ci/` directory layout instead of a single file, add a `.chainguard/develop.yaml` file whose `from` key names the check file or environment file that sessions should use, as described in [Use a .chainguard/develop.yaml file](#use-a-chainguarddevelopyaml-file). Without one, a session opens on the default environment, and `run-ci` runs your checks without the packages they declare.
- Sessions don't read `.chainguard/ci/env/develop.yaml`. If your repository has that file for sessions, name it in `.chainguard/develop.yaml` with `from: .chainguard/ci/env/develop.yaml`.

## Use a separate environment file {#use-a-separate-environment-file}

To give sessions an environment that's different from the one your checks use, without changing your repository, write it in a file of your own and pass the file with `--env`. A value for `--env` that contains a `/` or ends in `.yaml` is treated as a path.

This example creates a file that defines a session environment that can reach only the Go module proxy and checksum database:

```shell
cat > session-env.yaml <<EOF
version: 1
environment:
  packages: [bash, coreutils, curl, git, go, claude]
checks:
  develop:
    network:
      egress: [proxy.golang.org, sum.golang.org]
EOF
```

The `develop` check sets the session's network access. It has no command, which a session accepts but a pull request check doesn't, so keep files like this one out of your repository's `.chainguard/` directory.

To open a session with the file, pass its path with `--env`:

```shell
chainctl develop --env ./session-env.yaml --parent $ORGANIZATION
```

The session shows the file's contents in `/etc/chainguard/session.yaml`.

## Generate an environment {#generate-an-environment}

If your repository has neither a `.chainguard/develop.yaml` nor a `.chainguard/ci.yaml` file, `chainctl` can generate an environment from your directory's toolchain files, such as `go.mod` or `package.json`. To try it, pass `--env generate`:

```shell
chainctl develop --env generate --parent $ORGANIZATION
```

To generate the environment, `chainctl` uploads your directory to an AI agent that Chainguard hosts. The generated environment starts from the default environment's packages, adds the toolchains your directory needs, such as `go-1.24` for a Go module, and reaches the open internet. If your repository already has a `.chainguard/develop.yaml` or `.chainguard/ci.yaml` file, `--env generate` ignores it and says so. The option works only with a local directory, not with a repository URL.

In a git checkout, the upload includes tracked files and untracked files that `.gitignore` doesn't exclude, so files that `.gitignore` excludes, such as a `.env` file, stay on your laptop. In a directory that isn't a git checkout, the upload includes every file, so move secrets out of the directory before you pass `--env generate`. Either way, the upload leaves out symbolic links and every directory with one of the following names, at any depth: `.git`, `node_modules`, `vendor`, `target`, `dist`, `build`, `.venv`, `venv`, `__pycache__`, `.tox`, `.mypy_cache`, `.pytest_cache`, `.gradle`, `.idea`, and `.vscode`. `chainctl` releases older than the [minimum version](/get-started/checks-and-workspaces/#install-or-update-chainctl) also upload files that `.gitignore` excludes, so update `chainctl` before you pass `--env generate` in a checkout that holds secrets.

The upload can be at most 32 MiB and 50,000 files. If it's over either limit, `chainctl develop` fails before it creates a session. Open the session with `--env default` or an `--env` file instead.

The generated environment applies to the new session only, and `chainctl` doesn't add it to your repository. To keep it, copy it from `/etc/chainguard/session.yaml` in the session. Before you commit it as `.chainguard/ci.yaml`, give the `develop` check a `cmd`, because Chainguard Checks refuses a check that runs nothing. Also review its `network` key: the generated `develop` check allows every host, which would give that check open network access on pull requests.

## Start with a warm Go build cache {#start-with-a-warm-go-build-cache}

If your checks keep a Go build cache, a session can start with it, so `go build` and `go test` reuse what your checks already built on your default branch. To ask for the cache, open a session from a repository URL with `--cache`:

```shell
chainctl develop github.com/acme/app --check test --cache --parent $ORGANIZATION
```

The session mounts the Go build cache that your checks write after merging, as it was when the session started, and sets `GOCACHE` to it. Go can add to the cache in the session, but nothing the session builds goes back to your repository's cache. The session also adds `-count=1` to `GOFLAGS`, so `go test` always runs your tests instead of reporting cached results.

The cache mounts only when all of the following are true:

- You open the session from a repository URL. A session opened from a local directory gets no cache, even with `--cache`.
- The session's environment names a `gobuild` cache, as described in [Build caches](/chainguard/checks/variations-services-caches/#build-caches). Pass `--check` with a check whose environment names one, or, in the single-file layout, name it in your `.chainguard/ci.yaml` file's `environment`. A `.chainguard/develop.yaml` file can't give a session a cache, so in a repository that has one, pass `--check`. Sessions don't mount other cache types.
- On your default branch, the `trust` section of `.chainguard/ci/identities.yaml` has a cache pool whose `rings` is exactly `[2]`, the ring of checks that run after merging. Refer to [Set up cache pools](/chainguard/checks/variations-services-caches/#set-up-cache-pools).

The cache holds what passing checks built after merging, so it's empty until a check that names `gobuild` passes on your default branch. If any of these conditions isn't met, the session starts without a cache. `chainctl` doesn't report whether the cache mounted. To check, run `echo $GOCACHE` in the session, which prints nothing when no cache mounted.

Because `--cache` applies only when a session is created, it opens a new session, as `--new` does. To ask for the cache in every new session, set `CHAINCTL_DEVELOP_CACHE=true`. Unlike `--cache`, the variable doesn't make `chainctl develop` open a new session instead of returning to an existing one.

## Network access {#network-access}

A session's network access depends on its environment:

| Environment | Network access |
| ----------- | -------------- |
| The default environment | The open internet |
| A `.chainguard/develop.yaml` file | The open internet |
| A file's top-level `environment`, with no check selected | The open internet |
| A check with no `network` key, selected with `--check` or named `develop` | The open internet |
| A check with `network.egress`, selected with `--check` or named `develop` | Only the hosts in `egress` |

That's different from Chainguard Checks, where a check with no `network` key has no network access at all. In a session, only an `egress` list restricts the network.

A session never reaches cloud metadata endpoints, loopback addresses, or private IP ranges, whatever its environment allows.

When a session tries to reach a host outside its `egress` list, Chainguard refuses the connection and the session keeps running. A check can declare `policy: destroy` to stop its VM on a refused connection instead, but in a session, `destroy` is treated as `deny`.

The `egress` list doesn't affect the session's credential endpoints, such as `http://github/` and `http://claude/`. A session with a narrow `egress` list can still push to GitHub and use Claude Code. Refer to [Manage session credentials](/chainguard/workspaces/credentials/) to control those.

## Resources {#resources}

By default, each session has 4 vCPUs, 16 GB of memory, and a 50 GB disk, and runs on x86-64. To change a session's size, set `resources` in the file that sets its environment:

| Environment | Where the size comes from |
| ----------- | ------------------------- |
| A `.chainguard/develop.yaml` file | The file's `resources` key, not the one in the file that `from` names |
| A check, selected with `--check` or named `develop` | The check's `resources` key, or, if the check has none, its file's top-level `resources` key |
| A file's top-level `environment`, with no check selected | The file's top-level `resources` key |
| The default environment or a generated one | Always the default size |

The `resources` key takes either of the following:

- A resource class, such as `medium`. The built-in classes, listed in the [Chainguard Checks configuration reference](/chainguard/checks/configuration/#resources), each have a 40 GB disk, which is less than a session gets by default.
- An exact size, with `cpus`, `memory`, and `disk` together, such as `{cpus: 4, memory: 16Gi, disk: 100Gi}`. Sizes for `memory` and `disk` are whole numbers of `Gi` or `Mi`. Only a `.chainguard/develop.yaml` file and an `--env` file accept an exact size. Chainguard Checks refuses one in `.chainguard/ci.yaml`.

In an `--env` file, put an exact size on a check, because a file's top-level `resources` key takes only a class:

```yaml {title="session-env.yaml"}
version: 1
environment:
  packages: [bash, coreutils, curl, git, go, claude]
checks:
  develop:
    resources: {cpus: 4, memory: 16Gi, disk: 100Gi}
```

Unless Chainguard has raised your organization's limit, a session can have at most 4 vCPUs, 16 GB of memory, and a 100 GB disk, which rules out the `large` and `xlarge` classes. A session that asks for more doesn't start, and its error says that it's `larger than this organization's largest resource class`.

A session whose class ends in `-arm64`, such as `medium-arm64`, runs on arm64. Every other session runs on x86-64, including one whose class has no suffix. On pull requests, by contrast, a class without a suffix usually runs on arm64.

The `/tmp` directory is an in-memory file system limited to a quarter of the session's memory, which is 4 GB by default. Put large files, such as model weights, build caches, or virtual environments, under `/var/tmp` or `/work`, which are on disk.
