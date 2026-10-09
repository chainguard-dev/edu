---
title: "Chainguard Checks configuration reference"
linktitle: "Configuration reference"
description: "Reference for the .chainguard/ci.yaml file that defines Chainguard Checks: packages, commands, network access, conditions, triggers, and resources."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-09T00:00:00+00:00
draft: false
tags: ["Chainguard Checks", "Configuration", "Reference"]
images: []
menu:
  docs:
    parent: "checks"
    identifier: "Checks Configuration Reference"
toc: true
weight: 30
---

You define your checks in YAML configuration files in your repository's `.chainguard/` directory. This page describes the file format: where the files go, the packages and commands each check gets, and the options that control when and how checks run.

The same files also set up [Chainguard Workspaces](/chainguard/workspaces/overview/) sessions, and `run-ci` in a session runs the checks they define.

## File layouts

Chainguard Checks reads its configuration from one of two layouts. A repository uses one or the other, not both.

| Layout | Use it when |
| ------ | ----------- |
| A single `.chainguard/ci.yaml` file | You're getting started, or all your checks share one set of packages. |
| A `.chainguard/ci/` directory | You want to split checks into several files, or give checks different environments. |

Chainguard Checks reads only files with the `.yaml` extension. A `.chainguard/ci.yml` file doesn't turn on Chainguard Checks, and in a repository that uses Chainguard Checks, a `.yml` file in `.chainguard/` makes the configuration invalid. In the single-file layout, the `.chainguard/` directory can hold only `.yaml` files and their `.lock` files, so a file such as `.chainguard/README.md` also makes the configuration invalid.

In the directory layout, each `<name>.yaml` file in `.chainguard/ci/` holds a group of checks, and the file's name becomes part of each check's name on GitHub. For example, a `test` check in `.chainguard/ci/go.yaml` appears as `presubmit / go / test`. Checks in the single-file layout appear as `presubmit / ci / <check>`. The directory layout can also hold the following:

- `env/<name>.yaml` files, each defining a named environment that checks can share. A check that names no environment uses `env/default.yaml`.
- `env/develop.yaml`, an optional environment for [Chainguard Workspaces](/chainguard/workspaces/overview/) sessions that you open from the repository's URL, such as `chainctl develop github.com/acme/app`. Without it, those sessions open on the Workspaces default environment, not `env/default.yaml`. Sessions that you open from a local directory don't read it. A check uses it only if the check names it with `environment: develop`.
- `resources.yaml`, which replaces the built-in resource classes with your own.

Either layout can declare workload identities in `.chainguard/ci/identities.yaml`. Refer to [Credentials](#credentials).

Most examples on this page use the single-file layout. The keys inside each check are the same in both.

## A complete example

The following `.chainguard/ci.yaml` file uses the most common options:

```yaml {title=".chainguard/ci.yaml"}
version: 1
environment:
  packages: [bash, git, go, make]
checks:
  vet:
    cmd: go vet ./...
  test:
    cmd: go test ./...
    timeout: 15m
    network:
      egress: [proxy.golang.org, sum.golang.org]
  lint:
    script: |
      gofmt -l . | tee /tmp/unformatted
      test ! -s /tmp/unformatted
    advisory: true
  build:
    steps:
      - name: compile
        cmd: [go, build, ./...]
      - name: package
        cmd: make dist
    needs: [test]
  docs:
    cmd: make docs
    when:
      changed: ["docs/**"]
```

This file installs four packages in every check's VM and defines five checks:

- `vet` runs `go vet` with no network access.
- `test` runs `go test`, can reach the Go module proxy and checksum database, and fails if it runs longer than 15 minutes.
- `lint` runs a shell script. Because it's advisory, it reports its result but never blocks merging.
- `build` runs two steps in order and runs only after `test` passes.
- `docs` runs only when a pull request changes a file under `docs/`.

The rest of this page describes each option.

## Top-level keys

A configuration file has the following top-level keys:

| Key | Required | Description |
| --- | -------- | ----------- |
| `version` | Yes | The format version. Must be `1`. |
| `environment` | Yes, in the single-file layout | The packages and variables every check in the file gets. Refer to [Environment](#environment). |
| `resources` | No | The default resource class for the file's checks. Refer to [Resources](#resources). |
| `checks` | Yes | A map from each check's name to its definition. |

Chainguard Checks refuses any other top-level key, including GitHub Actions keys such as `jobs`, `on`, and `name`, with an error that names the key.

## Environment

The `environment` key sets up the VM each check runs in:

| Key | Description |
| --- | ----------- |
| `packages` | A list of packages to install, such as `go` or `nodejs-22`. |
| `vars` | A map of environment variables to set for every check. |

Every check's VM starts from a minimal base with BusyBox, GNU tar, and nothing else. Anything a check needs, including `git`, `bash`, `make`, `curl`, or a language toolchain, must be in `packages`. Package names often include a version, such as `go-1.24`, `nodejs-22`, or `python-3.13`. To pin a more specific version, add a version constraint after a tilde, such as `go-1.24~1.24.3`.

In the directory layout, a check can name a different environment with its own `environment` key, either by name, such as `environment: node` for `env/node.yaml`, or as an inline mapping.

## Check keys

Each entry under `checks` defines one check. The key is the check's name. A check must have exactly one of `cmd`, `script`, or `steps`, and can have any of the other keys:

| Key | Description |
| --- | ----------- |
| `cmd` | A command to run. Refer to [Commands](#commands). |
| `script` | A script to run with a shell. Refer to [Commands](#commands). |
| `shell` | The shell for `script`. Defaults to `sh -e`. |
| `steps` | A list of commands to run in order. Refer to [Commands](#commands). |
| `network` | The hosts the check can reach. Refer to [Network access](#network-access). Defaults to no network access. |
| `timeout` | How long the check can run, as a duration such as `10m` or `1h30m`. Refer to [Timeouts](#timeouts). |
| `needs` | A list of checks in the same file that must pass before this one runs. |
| `when` | Conditions under which the check runs. Refer to [Conditions](#conditions). |
| `trigger` | `presubmit`, `postsubmit`, or a list of both. Refer to [Triggers](#triggers). Defaults to `presubmit`. |
| `advisory` | If `true`, the check reports its result but never blocks merging. Defaults to `false`. |
| `description` | A description of the check, up to 1,024 characters. Required for a check that runs on request. |
| `vars` | A map of environment variables for this check. |
| `workdir` | The directory to run in, relative to the repository's root. Defaults to the root, which is `/work` in the VM. |
| `resources` | The check's resource class. Refer to [Resources](#resources). |
| `foreach` | A list of variations to run the check once for each, such as one per package directory. |
| `parallelism` | How many `foreach` variations can run at once. |
| `user` | The user to run as. Defaults to `root`. |
| `identity` | A workload identity for the check. Refer to [Credentials](#credentials). |

Chainguard Checks refuses keys it doesn't recognize, including GitHub Actions keys such as `runs-on`, `env`, `if`, and `timeout-minutes`. For some of them, such as `if` and `on`, the error names the key to use instead. Refer to [Migrate from GitHub Actions](/chainguard/checks/migrate-from-github-actions/) for a full mapping.

## Commands

A check runs a single command, a script, or a list of steps.

### The cmd key

The `cmd` key runs one command without a shell. You can write it as a string or as a list of arguments:

```yaml
checks:
  test:
    cmd: go test ./...
  test-uncached:
    cmd: [go, test, -count=1, ./...]
```

Chainguard Checks splits a string `cmd` into arguments on spaces, the way a shell would split plain words, and refuses a string that needs a shell to run. That includes pipes, redirection, `&&`, variable expansion, and glob characters such as `*`. For those, use `script`.

### The script key

The `script` key runs a script with a shell. By default, the shell is `sh -e`, so the script stops at the first command that fails:

```yaml
checks:
  fmt:
    script: |
      gofmt -l . > /tmp/unformatted
      if [ -s /tmp/unformatted ]; then
        cat /tmp/unformatted
        exit 1
      fi
```

To use a different interpreter, set `shell` to the interpreter's package name, such as `bash`, `python-3.13`, or `nodejs-22`, and list that same package in the environment. Chainguard Checks supports Bash, Python, Node.js, Ruby, and Perl. The BusyBox `sh` is always available.

### The steps key

The `steps` key runs a list of commands in order, in the same VM, and stops at the first one that fails. Each step has a `cmd` or a `script`, and an optional `name` that appears in the check's results:

```yaml
checks:
  build:
    steps:
      - name: compile
        cmd: go build ./...
      - name: test
        cmd: go test ./...
      - name: smoke test
        script: ./bin/app --version | grep -q "app"
```

All steps share the check's network access and timeout.

## Network access

A check has no network access unless it has a `network` key. To let a check reach specific hosts, list them under `network.egress`:

```yaml
checks:
  test:
    cmd: npm test
    network:
      egress:
        - registry.npmjs.org
        - "*.githubusercontent.com"
      policy: deny
```

Each entry in `egress` can be one of the following:

- A hostname, such as `registry.npmjs.org`, in lowercase and without a scheme or port.
- A wildcard for a domain's subdomains, such as `*.githubusercontent.com`. A wildcard doesn't match the domain itself, so list `githubusercontent.com` too if the check needs it. A wildcard can't cover a whole top-level domain, such as `*.com`.
- An IPv4 address or CIDR range. IPv6 isn't supported.
- `*`, which allows any host.

An entry with a scheme or a port, such as `https://registry.npmjs.org` or `registry.npmjs.org:443`, passes validation but matches nothing. If you include a `network` key, `egress` must list at least one entry. To keep a check off the network, leave out `network` entirely.

The `policy` key controls what happens when the check tries to reach a host that isn't listed:

| Policy | What happens |
| ------ | ------------ |
| `deny` (default) | Chainguard Checks refuses the connection, and the check keeps running. |
| `destroy` | Chainguard Checks stops the check's VM, and the check fails. |

Whatever a check allows, it can never reach cloud metadata endpoints, loopback addresses, or private IP ranges.

## Conditions

The `when` key limits when a check runs. A check without `when` runs on every pull request.

### Run when files change

To run a check only when a pull request changes certain files, list glob patterns under `when.changed`:

```yaml
checks:
  docs:
    cmd: make docs
    when:
      changed: ["docs/**", "mkdocs.yml"]
```

A pattern of `**` matches any number of directories, so `docs/**` matches every file under `docs/`. For a pull request, Chainguard Checks compares the pull request's changes against its base branch.

### Run when an expression is true

To run a check based on the pull request, write a [Common Expression Language (CEL)](https://cel.dev/) expression under `when.expr`. The expression can read the following fields:

| Field | Description |
| ----- | ----------- |
| `context.trigger` | The run's trigger. Compare it to the unquoted constants `presubmit` and `postsubmit`, such as `context.trigger == postsubmit`. |
| `context.github.pull_request.number` | The pull request's number. |
| `context.github.pull_request.title` | The pull request's title. |
| `context.github.pull_request.draft` | Whether the pull request is a draft. |
| `context.github.pull_request.labels` | The pull request's labels. |
| `context.github.pull_request.head_ref` | The pull request's branch name. |
| `context.github.pull_request.head_repository` | The repository the pull request's branch is in, which differs from yours for a pull request from a fork. |
| `context.github.pull_request.author.login` | The GitHub login of the pull request's author. |

For example, this check skips draft pull requests:

```yaml
checks:
  e2e:
    cmd: make e2e
    when:
      expr: "!context.github.pull_request.draft"
```

A run after merging has no pull request, and reading a `context.github.pull_request` field in that run is an error that fails the run. For a check that also runs after merging, guard the field with `has()`, such as `expr: "!has(context.github.pull_request) || !context.github.pull_request.draft"`.

If you set both `changed` and `expr`, the check runs only when both are true.

### Run on request

A check with `when: {requested: true}` runs only when someone asks for it. Use this for slow or expensive checks that most pull requests don't need. A check that runs on request must have a `description`:

```yaml
checks:
  e2e-full:
    cmd: make e2e-full
    description: The full end-to-end suite against every supported database.
    when:
      requested: true
```

To run the check on a pull request, add the label `ci/run:<check>`, such as `ci/run:e2e-full`. Refer to [Run a check on request](/chainguard/checks/github/#run-a-check-on-request) for details.

## Advisory checks

A check with `advisory: true` reports its real result on the pull request, with `(advisory)` in its title, but never makes the **Chainguard Checks (presubmit)** summary check fail. Use it for a check you want to see but not enforce yet, such as a new linter.

## Triggers

The `trigger` key sets which events run a check:

| Trigger | When the check runs |
| ------- | ------------------- |
| `presubmit` (default) | On each pull request, against the commit GitHub would create by merging it. |
| `postsubmit` | On each new commit on your default branch, after a change merges. |

To run a check at both times, list both:

```yaml
checks:
  test:
    cmd: go test ./...
    trigger: [presubmit, postsubmit]
```

Postsubmit results appear on the commit on your default branch, in a summary check named **Chainguard Checks (postsubmit)**.

## Timeouts

By default, a check has no time limit of its own. A whole run can take up to 50 minutes, and a check still running at that point fails. To fail a check sooner, set `timeout` to a duration, such as `10m` or `1h`.

## Resources

By default, each check's VM has 2 vCPUs, 8 GB of memory, and a 14 GB disk. To give a check more, set `resources` to one of the following classes:

| Class | vCPUs | Memory | Disk |
| ----- | ----- | ------ | ---- |
| `medium` | 4 | 16 GB | 40 GB |
| `large` | 8 | 32 GB | 40 GB |
| `xlarge` | 16 | 64 GB | 40 GB |

On pull requests, a class without a suffix can run on either CPU architecture, and usually runs on arm64. Each class also has `-amd64` and `-arm64` variants, such as `large-amd64`, that pin the architecture. Use an `-amd64` class for a check that needs x86-64, such as one that downloads an x86-64 binary.

Your organization's plan sets the largest class you can use. During a free trial, the largest is `medium`. If any check in a run asks for `large` or `xlarge`, the whole run fails before any check starts, and the summary check shows **Run failed**.

## Environment variables

Set environment variables with `vars`, either in `environment` for every check or on a single check:

```yaml
environment:
  packages: [go]
  vars:
    CGO_ENABLED: "0"
checks:
  test:
    cmd: go test ./...
    vars:
      GOFLAGS: -count=1
```

In a check's `vars`, but not in `environment.vars`, a variable's value can also come from the pull request, with a binding such as `"${{ context.github.pull_request.number }}"`. The binding must be the variable's whole value, and it reads the same fields as [`when.expr`](#run-when-an-expression-is-true).

Chainguard Checks doesn't set `CI` or any `GITHUB_` variables. When a run has a base commit, Chainguard Checks sets `CHAINGUARD_BASE_REVISION` to that commit's SHA. For a pull request, that's the base branch commit that GitHub merged the pull request into. For a run after merging, it's the new commit's first parent. Your repository's history is in the VM, so with `git` in your packages, a check can compare against it, such as with `git diff "$CHAINGUARD_BASE_REVISION"`.

## Report errors and annotations

A check can print special lines to its output that Chainguard Checks turns into annotations on the pull request or uses to protect its log:

| Line | What it does |
| ---- | ------------ |
| `::error file=main.go,line=12::message` | Reports an error as an annotation on that file and line. |
| `::warning file=main.go,line=12::message` | Reports a warning as an annotation on that file and line. |
| `::notice::message` | Shows a notice in the check's output. |
| `::add-mask::value` | Hides `value` wherever it appears later in the check's log. |

Only `::error` and `::warning` lines with a `file` become annotations. Without a `file`, they appear in the check's output only. The `file` path must be relative to the repository's root, not to the check's `workdir`. Chainguard Checks shows up to 50 annotations for each check.

These lines use the same format as GitHub Actions workflow commands, so many linters that support GitHub Actions output work without changes.

## Credentials

A check runs without credentials by default. Most checks need none, because your repository's code is already in the VM.

A check that must authenticate to Google Cloud or to Chainguard, such as to pull private images from `cgr.dev`, can use a *workload identity*. You declare workload identities in `.chainguard/ci/identities.yaml`, and a check requests one by name with `identity`. Workload identities need setup on the provider's side as well. During the beta, contact your Chainguard account team to set them up.

## Validate your configuration

To find mistakes in your configuration without running anything, run `chainctl checks validate .` from your repository's directory. To see how Chainguard Checks interprets your configuration, run `chainctl checks explain`. Refer to [Validate your configuration offline](/chainguard/checks/run-checks/#validate-your-configuration-offline) for details.

## More examples

### Node.js

This file installs Node.js 22 and npm, installs dependencies, and runs the tests:

```yaml {title=".chainguard/ci.yaml"}
version: 1
environment:
  packages: [nodejs-22, npm]
checks:
  test:
    steps:
      - name: install
        cmd: npm ci
      - name: test
        cmd: npm test
    network:
      egress: [registry.npmjs.org]
```

The `install` and `test` steps run in the same VM, so the packages that `npm ci` installs are available to `npm test`. If your project uses packages from another registry, add that registry's host to `egress`.

### Python

This file installs Python 3.13 and pip, installs the project's requirements, and runs `pytest`:

```yaml {title=".chainguard/ci.yaml"}
version: 1
environment:
  packages: [python-3.13, py3.13-pip]
checks:
  test:
    script: |
      python3 -m venv /tmp/venv
      . /tmp/venv/bin/activate
      pip install -r requirements.txt
      pytest
    network:
      egress: [pypi.org, files.pythonhosted.org]
```

The script creates a virtual environment in `/tmp` so that `pip` installs packages for the check alone. Both `pypi.org` and `files.pythonhosted.org` are in `egress`, because pip reads the package index from the first and downloads files from the second.
