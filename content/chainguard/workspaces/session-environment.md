---
title: "Configure a Chainguard Workspaces session's environment"
linktitle: "Session environment"
description: "Choose the packages, tools, and network access a Chainguard Workspaces session gets, from your repository's .chainguard/ci.yaml file, a file of your own, or the default environment."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-08T00:00:00+00:00
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

A session's environment is fixed when the session is created. If your repository's `.chainguard/ci.yaml` file changes afterward, existing sessions keep the environment they started with, and `chainctl` reminds you when you return to them. To use the new environment, open a new session with `chainctl develop --new`.

## How a session chooses its environment

When `chainctl develop` creates a session, it chooses the environment in the following order:

1. The environment you choose with `--env`, if any: a file, `default`, or `generate`.
2. Your repository's `.chainguard/ci.yaml` file, if it has one.
3. The default environment.

If your repository has no `.chainguard/ci.yaml` file and you don't pass `--env`, `chainctl` opens the session on the default environment and tells you so. When you run `chainctl develop` with `--non-interactive`, it refuses instead, so pass `--env default` explicitly in scripts.

`chainctl` never writes to your directory. To find out which environment a session uses, read `/etc/chainguard/session.yaml` in the session. To see each session's environment from your laptop, run `chainctl develop list -o wide`.

## The default environment

The default environment is a general-purpose shell with the following packages:

- `bash`, `coreutils`, `make`, `curl`, and `git`
- `apk-tools`, so you can install more packages from the shell
- `claude`, the Claude Code CLI
- `gh`, `jq`, `ripgrep`, `less`, and `vim`
- `google-cloud-sdk`
- `chainctl`

The default environment reaches the open internet. To open a session on the default environment even when your repository has a `.chainguard/ci.yaml` file, pass `--env default`:

```shell
chainctl develop --env default --parent $ORGANIZATION
```

The default environment doesn't include language toolchains. To add one to the current session, install it with `apk`. This example installs Python 3.13:

```shell
apk add python-3.13
```

Packages you install with `apk` last for the life of the session, including when it parks and resumes, but new sessions don't get them. To install packages in every new session, list them in a `.chainguard/ci.yaml` file.

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
  test:
    cmd: go test ./...
    network:
      egress: [proxy.golang.org, sum.golang.org]
```

A session opened on this repository installs the packages listed under `environment`. In the session, `run-ci` runs the `vet` and `test` checks against your working tree. Refer to the [Chainguard Checks configuration reference](/chainguard/checks/configuration/) for the full file format.

Keep the following in mind when you write the file for sessions:

- Every session also gets `git`, `gh`, `curl`, `busybox`, and `gnutar`, whatever the file lists. Nothing else is installed unless you list it, including Claude Code (`claude`).
- A session uses the environment of a check named `develop` if the file has one. Otherwise, it uses the file's top-level `environment`.
- To open a session with a specific check's environment, including that check's network access, pass `--check` with the check's name. In the example, `chainctl develop --check test` opens a session that can reach only the Go module proxy and checksum database.
- The `run-ci` command runs every check in the session's own environment, not in the environment each check declares.
- If your repository uses the `.chainguard/ci/` directory layout instead of a single file, a session opened from a local directory doesn't read it, and opens on the default environment. The `run-ci` command in that session still finds the checks the directory defines, but runs them without the toolchains they declare, so add those packages with `apk` or pass an `--env` file.

## Use a separate environment file

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

## Generate an environment

If your repository doesn't have a `.chainguard/ci.yaml` file, `chainctl` can generate an environment from your directory's toolchain files, such as `go.mod` or `package.json`. To try it, pass `--env generate`:

```shell
chainctl develop --env generate --parent $ORGANIZATION
```

To generate the environment, `chainctl` uploads your directory, without its `.git` directory, to an agent that Chainguard hosts. The generated environment starts from the default environment's packages, adds the toolchains your directory needs, such as `go-1.24` for a Go module, and reaches the open internet. If your repository already has a `.chainguard/ci.yaml` file, `--env generate` ignores it and says so. The option works only with a local directory, not with a repository URL.

The generated environment applies to the new session only, and `chainctl` doesn't add it to your repository. To keep it, copy it from `/etc/chainguard/session.yaml` in the session. Before you commit it as `.chainguard/ci.yaml`, give the `develop` check a `cmd`, because Chainguard Checks refuses a check that runs nothing. Also review its `network` key: the generated `develop` check allows every host, which would give that check open network access on pull requests.

## Network access

A session's network access depends on its environment:

| Environment | Network access |
| ----------- | -------------- |
| The default environment | The open internet |
| A file's top-level `environment`, with no check selected | The open internet |
| A check with no `network` key, selected with `--check` or named `develop` | The open internet |
| A check with `network.egress`, selected with `--check` or named `develop` | Only the hosts in `egress` |

That's different from Chainguard Checks, where a check with no `network` key has no network access at all. In a session, only an `egress` list restricts the network.

A session never reaches cloud metadata endpoints, loopback addresses, or private IP ranges, whatever its environment allows.

When a session tries to reach a host outside its `egress` list, Chainguard refuses the connection and the session keeps running. A check can declare `policy: destroy` to stop its VM on a refused connection instead, but in a session, `destroy` is treated as `deny`.

The `egress` list doesn't affect the session's credential endpoints, such as `http://github/` and `http://claude/`. A session with a narrow `egress` list can still push to GitHub and use Claude Code. Refer to [Manage session credentials](/chainguard/workspaces/credentials/) to control those.

## Resources

By default, each session has 4 vCPUs, 16 GB of memory, and a 50 GB disk. The `/tmp` directory is an in-memory file system limited to a quarter of the session's memory, which is 4 GB by default. Put large files, such as model weights, build caches, or virtual environments, under `/var/tmp` or `/work`, which are on disk.
