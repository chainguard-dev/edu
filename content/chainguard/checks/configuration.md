---
title: "Chainguard Checks configuration reference"
linktitle: "Configuration reference"
description: "Reference for the .chainguard/ci.yaml file that defines Chainguard Checks: file layouts, packages, commands, network access, conditions, triggers, resources, and environment variables."
type: "article"
date: 2026-10-08T00:00:00+00:00
lastmod: 2026-10-22T14:48:15+00:00
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

You define your checks in YAML configuration files in your repository's `.chainguard/` directory. This page describes the file format: where the files go, the packages and commands each check gets, and the options that control when and how checks run. For variations, inputs and outputs, services, and caches, refer to [Variations, inputs, services, and caches](/chainguard/checks/variations-services-caches/).

The same files also set up [Chainguard Workspaces](/chainguard/workspaces/overview/) sessions, and `run-ci` in a session runs the checks they define.

## File layouts {#file-layouts}

Chainguard Checks reads its configuration from one of two layouts. A repository uses one or the other, not both.

| Layout | Use it when |
| ------ | ----------- |
| `.chainguard/ci.yaml`, with optional check files beside it | You're getting started, or each file's checks can share one environment. |
| A `.chainguard/ci/` directory | You want checks to share named environments or pick their own, or you need service definition files, your own resource classes, or Markdown descriptions of checks. |

In the directory layout, each `<name>.yaml` file in `.chainguard/ci/` holds a group of checks, and the file's name becomes part of each check's name on GitHub. For example, a `test` check in `.chainguard/ci/go.yaml` appears as `presubmit / go / test`. The directory layout can also hold the following:

- `env/<name>.yaml` files, each defining a named environment that checks can share, and their `.lock` files. A check that names no environment uses `env/default.yaml`.
- `resources/`, which holds one file for each resource class of your own. Refer to [Define your own resource classes](#define-your-own-resource-classes).
- `<name>.md` files that explain checks in more detail. Chainguard Checks never reads them as configuration. Refer to [Describe a check](#describe-a-check).
- `services/<name>/<name>.yaml` files, each defining a service, with any files the service needs beside it. Refer to [Services](/chainguard/checks/variations-services-caches/#services).

The single-file layout is named for `.chainguard/ci.yaml`, whose checks appear as `presubmit / ci / <check>`, but it can also hold other check files directly in `.chainguard/`, such as `.chainguard/lint.yaml`. Each one needs `version: 1` and its own `environment`, and its checks appear under the file's name, such as `presubmit / lint / test`.

Either layout can declare workload identities and cache pools in `.chainguard/ci/identities.yaml`. Refer to [Workload identities and trust](/chainguard/checks/identity-and-trust/) and [Set up cache pools](/chainguard/checks/variations-services-caches/#set-up-cache-pools).

Chainguard Checks reads configuration only from files with the `.yaml` extension, so a `.chainguard/ci.yml` file doesn't turn it on. The following table shows how each layout treats the files in `.chainguard/`:

| File | Single-file layout | Directory layout |
| ---- | ------------------ | ---------------- |
| `.chainguard/ci.yaml` | Required | Makes the configuration invalid |
| `.chainguard/ci/identities.yaml` | Allowed | Allowed |
| Other files in `.chainguard/ci/` | Make the configuration invalid | Allowed if they're among the files listed earlier. Any other file, such as a `.yml` file, makes the configuration invalid. |
| `.chainguard/develop.yaml` and `.chainguard/deps.yaml` | Allowed, unless the file has a `checks` or `plans` key | Allowed |
| `.chainguard/actions.yaml`, `.chainguard/images.yaml`, and `.chainguard/source.yaml` | Ignored | Ignored |
| Another `.yaml` file directly in `.chainguard/`, such as `.chainguard/lint.yaml` | Read as a check file if it has a top-level `version`, `environment`, `resources`, `checks`, `plans`, or `uses` key. Otherwise ignored. | Makes the configuration invalid if it has any of those keys. Otherwise ignored. |
| `.chainguard/README.md`, a `.yml` file, or another file that isn't a `.yaml` or `.lock` file, directly in `.chainguard/` | Makes the configuration invalid | Ignored |

If another tool keeps its own `.yaml` file in `.chainguard/`, make sure the file has no top-level `version`, `environment`, `resources`, `checks`, `plans`, or `uses` key, or move it out of `.chainguard/`.

A `.chainguard/develop.yaml` file sets up [Chainguard Workspaces](/chainguard/workspaces/session-environment/) sessions. Chainguard Checks runs nothing from it, so changing it doesn't change your checks. Put checks in `.chainguard/ci.yaml` or `.chainguard/ci/` instead. Sessions don't read `.chainguard/ci/env/develop.yaml`, which is an environment like any other that a check can name with `environment: develop`. A pull request that changes `.chainguard/develop.yaml` also gets a **Chainguard Checks / develop-environment** check, as described in [How results appear](/chainguard/checks/github/#how-results-appear).

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
    network:
      egress: [proxy.golang.org, sum.golang.org]
  test:
    cmd: go test ./...
    timeout: 15m
    network:
      egress: [proxy.golang.org, sum.golang.org]
  lint:
    script: |
      gofmt -l . > /tmp/unformatted
      cat /tmp/unformatted
      test ! -s /tmp/unformatted
    advisory: true
  build:
    steps:
      - name: compile
        cmd: [go, build, ./...]
      - name: package
        cmd: make dist
    needs: [test]
    network:
      egress: [proxy.golang.org, sum.golang.org]
  docs:
    cmd: make docs
    when:
      changed: ["docs/**"]
```

This file installs four packages in every check's VM and defines five checks:

- `vet` runs `go vet`, and can reach the Go module proxy and checksum database to download modules.
- `test` runs `go test`, can reach the same hosts, and fails if it runs longer than 15 minutes.
- `lint` runs a shell script. Because it's advisory, it reports its result but never blocks merging.
- `build` runs two steps in order, can reach the Go module hosts, and runs only after `test` passes.
- `docs` runs only when a pull request changes a file under `docs/`.

The rest of this page describes each option.

## Top-level keys {#top-level-keys}

A configuration file has the following top-level keys:

| Key | Required | Description |
| --- | -------- | ----------- |
| `version` | Yes | The format version. Must be `1`. |
| `environment` | Yes, in the single-file layout | The packages and variables every check in the file gets. Refer to [Environment](#environment). |
| `resources` | No | The default resource class for the file's checks. Refer to [Resources](#resources). |
| `checks` | Yes | A map from each check's name to its definition. |
| `plans` | No | Named commands that compute a check's `foreach` variations during the run. Refer to [Compute variations during a run](/chainguard/checks/variations-services-caches/#compute-variations-during-a-run). |
| `requested_checks_agent` | No | `off` (default), `comment`, or `agent`. Turns on an agent that requests checks for each pull request. Set it only in `.chainguard/ci.yaml`, or in `.chainguard/ci/env/default.yaml` in the directory layout. In any other file, it makes the configuration invalid. Refer to [Let an agent request checks](/chainguard/checks/github/#let-an-agent-request-checks). |

Chainguard Checks refuses any other top-level key with an error that names the key. That includes GitHub Actions keys such as `jobs`, `on`, and `name`.

## Environment {#environment}

The `environment` key sets up the VM each check runs in:

| Key | Description |
| --- | ----------- |
| `packages` | A list of packages to install, such as `go` or `nodejs-22`. |
| `vars` | A map of environment variables to set for every check. |
| `services` | Services, such as a database, to start in each check's VM before the check's commands run. Refer to [Services](/chainguard/checks/variations-services-caches/#services). |
| `caches` | Caches that carry build output and downloaded packages from earlier runs into each check's VM. Refer to [Caches](/chainguard/checks/variations-services-caches/#caches). |

Every check's VM starts from a minimal base with BusyBox, GNU tar, and nothing else. Anything a check needs, including `git`, `bash`, `make`, `curl`, or a language toolchain, must be in `packages`. Chainguard Checks installs them from Chainguard's public Wolfi and Extra Packages repositories, and from your organization's Private APK Repository, which adds the packages your organization is entitled to. Refer to [Overview of Chainguard's package repositories](/chainguard/containers/building-and-modifying/packages/package-model/).

Package names often include a version, such as `go-1.24`, `nodejs-22`, or `python-3.13`. To pin a more specific version, add a version constraint after a tilde, such as `go-1.24~1.24.3`.

To find a package's name, use the [`cg-apk`](/platform/mcp-servers/cg-apk/) MCP server, which looks up APK packages. You can also search Wolfi's packages from a container, as described in [Searching for packages](/chainguard/containers/migration/migrating-to-chainguard-images/#searching-for-packages).

In the directory layout, a check can name a different environment with its own `environment` key, either by name, such as `environment: node` for `env/node.yaml`, or as an inline mapping.

## Check keys

Each entry under `checks` defines one check. The key is the check's name. A check must have exactly one of `cmd`, `script`, or `steps`, and can have any of the other keys:

| Key | Description |
| --- | ----------- |
| `cmd` | A command to run without a shell. Refer to [Commands](#commands). |
| `script` | A script to run with a shell. Refer to [Commands](#commands). |
| `shell` | The shell for `script`. Defaults to `sh -e`. A check with `cmd` or `steps` can't set it, but each step can set its own. Refer to [The script key](#the-script-key). |
| `steps` | A list of commands to run in order. Refer to [Commands](#commands). |
| `network` | The hosts the check can reach. Refer to [Network access](#network-access). Defaults to no network access. |
| `timeout` | How long the check can run, as a duration such as `10m` or `1h30m`. Refer to [Timeouts](#timeouts). |
| `needs` | A list of checks in the same file that must pass before this one runs. Refer to [Advisory checks](#advisory-checks), [Run on request](#run-on-request), and [Triggers](#triggers) for limits. |
| `when` | Conditions under which the check runs. Refer to [Conditions](#conditions). |
| `trigger` | `presubmit`, `postsubmit`, or a list of both. Refer to [Triggers](#triggers). Defaults to `presubmit`. |
| `advisory` | If `true`, the check reports its result but never blocks merging. Defaults to `false`. |
| `description` | What the check covers and when it's worth running. Refer to [Describe a check](#describe-a-check). |
| `docs` | The name of a Markdown file beside the check file that explains the check in more detail. Directory layout only. Refer to [Describe a check](#describe-a-check). |
| `vars` | A map of environment variables for this check. |
| `workdir` | The directory to run in, relative to the repository's root. Defaults to the root, which is `/work` in the VM. |
| `inputs` | Files to add to the check's VM from another check's output or from another repository. Refer to [Inputs and outputs](/chainguard/checks/variations-services-caches/#inputs-and-outputs). |
| `outputs` | Directories that the check produces for later checks in the same run. Refer to [Inputs and outputs](/chainguard/checks/variations-services-caches/#inputs-and-outputs). |
| `resources` | The check's resource class. Refer to [Resources](#resources). |
| `foreach` | A list of variations to run the check once for each, such as one per package directory, or `plans.<name>` to compute the variations during the run. Refer to [Run a check once per variation](/chainguard/checks/variations-services-caches/#run-a-check-once-per-variation). |
| `parallelism` | How many `foreach` variations can run at once. Refer to [Run a check once per variation](/chainguard/checks/variations-services-caches/#run-a-check-once-per-variation). |
| `user` | The name of an account to run the check's commands as, such as `build`. Defaults to `root`. Refer to [Run as another user](/chainguard/checks/variations-services-caches/#run-as-another-user). |
| `identity` | A workload identity for the check. Refer to [Credentials](#credentials). |

Chainguard Checks refuses keys it doesn't recognize, including GitHub Actions keys such as `runs-on`, `env`, `if`, and `timeout-minutes`. For some of them, such as `if` and `on`, the error names the key to use instead. Refer to [Migrate from GitHub Actions](/chainguard/checks/migrate-from-github-actions/) for a full mapping.

### Check names {#check-names}

A check's name can use letters, digits, spaces, `_`, and `-`, and must start and end with a letter or digit. It can't contain `.` or `/`. Two checks in the same file can't have names that differ only in case, because [request labels](#run-on-request) ignore case.

A check's full name joins its file's name and its own, such as `ci/test` or `go/test`. Each `foreach` variation's full name adds the variation's name, such as `go/test/api`. Every full name can be up to 128 characters. If a name has a character that isn't allowed, the error says only that the name must fit the 128-character limit, so check its characters too.

## Commands

A check runs a single command, a script, or a list of steps.

### The cmd key {#the-cmd-key}

The `cmd` key runs one command without a shell. You can write it as a string or as a list of arguments:

```yaml
checks:
  test:
    cmd: go test ./...
  test-short:
    cmd: [go, test, -short, ./...]
```

Chainguard Checks splits a string `cmd` into arguments on whitespace and runs it without a shell. Quotes and backslashes work the way they do in a shell, so `cmd: find . -name '*.go'` passes `*.go` to `find` as it is. Chainguard Checks refuses a string `cmd` that contains any of the following:

- An unquoted `|`, `&`, `;`, `<`, `>`, `(`, `)`, `$`, `` ` ``, `*`, `?`, `[`, `]`, `{`, or `}`.
- An argument that starts with an unquoted `#` or `~`.
- A `$` or a backtick inside double quotes.

For pipes, redirection, variables, or globs, use `script`, or run a shell yourself, such as `cmd: [sh, -c, "go vet ./... && go test ./..."]`.

### The script key {#the-script-key}

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

To use a different interpreter, set `shell` to the interpreter's package name, such as `bash`, `python-3.13`, or `nodejs-22`, and list that same package in the environment. The BusyBox `sh` is always available. Chainguard Checks passes the whole script to the interpreter as one argument:

| Interpreter | Runs the script with |
| ----------- | -------------------- |
| BusyBox `sh` (default) | `sh -e -c` |
| Bash | `bash -e -c` |
| Python | `python3 -c` |
| Node.js | `node -e` |
| Ruby | `ruby -e` |
| Perl | `perl -e` |

Neither `sh -e` nor `bash -e` sets `pipefail`, so a pipeline succeeds whenever its last command does. For example, `go test ./... | tee test.log` passes even when tests fail. To make a pipeline fail when any of its commands fails, set `shell: bash` and start the script with `set -o pipefail`, or use a `cmd` such as `[bash, -eo, pipefail, -c, "go test ./... | tee test.log"]`. Either way, list `bash` in the environment's packages.

### The steps key

The `steps` key runs a list of commands in order, in the same VM, and stops at the first one that fails. Each step has a `cmd` or a `script`, and can also have the following keys:

| Key | Description |
| --- | ----------- |
| `name` | A name that appears in the check's results. |
| `shell` | The shell for the step's `script`, the same as a check's `shell`. |
| `id` | An identifier for the step in the check's logs. |

For example:

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

### How commands run {#how-commands-run}

The following applies to a check's `cmd` or `script`, and to each of its steps:

- Standard input is empty, so a command that reads it gets end-of-file. Commands don't run in a terminal, but Chainguard Checks sets `TERM` to `xterm-256color`.
- When a command or script exits, Chainguard Checks stops every background process that the command or script left running. A process that one step starts isn't running in the next step, so to keep a process, such as a database, running for a check's commands, use a [service](/chainguard/checks/variations-services-caches/#services).
- A background process that still has the command's standard output or standard error open keeps the step running until that process exits, so a server started with a plain `&` can keep the check running until it times out. To run a server while the rest of a script runs, redirect its output, as in `./server > server.log 2>&1 &`.
- When a check reaches its `timeout` or the run's [two-hour limit](#timeouts), or its run is canceled, Chainguard Checks stops the check's VM without signaling its processes first. Cleanup that a script sets up, such as a `trap` on `EXIT` or `TERM`, doesn't run.
- If a signal ends a command, its exit code is 128 plus the signal's number, such as `137` for `SIGKILL`.

## Network access {#network-access}

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

When a check with network access makes an HTTPS request, Chainguard Checks verifies the host's own certificate, then presents the check with a certificate signed by a certificate authority that it creates for that check's VM alone. Chainguard Checks doesn't replace the host's certificate in the following cases:

- The connection goes to a port other than 443, such as 8443.
- The host requires a client certificate.
- The host's certificate doesn't verify.
- The client's TLS handshake offers only protocols other than HTTP.

The VM's system certificate bundle and Java truststore already trust the certificate authority, and Chainguard Checks points the certificate variables listed in [Variables that Chainguard Checks sets](#variables-that-chainguard-checks-sets) at the bundle, so most tools work without changes. A tool that keeps its own list of trusted certificates and doesn't read these variables rejects the connection instead. Refer to [A check fails with a certificate error](/chainguard/checks/troubleshooting/#a-check-fails-with-a-certificate-error).

To see which hosts a check tried to reach and whether Chainguard Checks allowed each one, open the check's run page from its **Details** link. Refer to [A check can't reach a host](/chainguard/checks/troubleshooting/#a-check-cant-reach-a-host).

## Conditions {#conditions}

The `when` key limits when a check runs. A check without `when` runs on every pull request. An empty `when` makes the configuration invalid, so to run a check every time, leave out `when`.

### Run when files change {#run-when-files-change}

To run a check only when a pull request changes certain files, list glob patterns under `when.changed`:

```yaml
checks:
  docs:
    cmd: make docs
    when:
      changed: ["docs/**", "mkdocs.yml"]
```

`changed` must list at least one pattern. Patterns match file paths as follows:

- A pattern is relative to the repository's root, such as `docs/**` or `cmd/*/main.go`. A pattern that starts with `/` or `./` never matches.
- `*` matches any characters except `/`, and `?` matches any one character except `/`. A set in brackets, such as `[abc]` or `[a-z]`, matches one character from the set.
- `**` matches any number of directories, including none, but only as a whole segment between slashes. `docs/**` matches every file under `docs/`, and `**/*.go` matches every Go file in the repository. `**.go` works like `*.go`, so it matches only Go files at the root.
- `!`, braces such as `{a,b}`, and `+` have no special meaning, and there's no `when.unchanged`, so you can't exclude files. List the paths that should run the check instead.

`chainctl checks validate` refuses a malformed pattern, such as one with an unclosed `[`, but not a pattern that can never match, such as `/docs/**`.

For a pull request, Chainguard Checks compares the pull request's changes against its base branch. For a run after merging, it compares the new commit against its first parent, as described in [Run checks after merging](/chainguard/checks/github/#run-checks-after-merging).

### Run when an expression is true {#run-when-an-expression-is-true}

To run a check based on the pull request, write a [Common Expression Language (CEL)](https://cel.dev/) expression under `when.expr`. The expression can read the following fields:

| Field | Description |
| ----- | ----------- |
| `context.trigger` | The run's trigger. Compare it to the unquoted constants `presubmit` and `postsubmit`, such as `context.trigger == postsubmit`. |
| `context.github.pull_request.number` | The pull request's number. |
| `context.github.pull_request.title` | The pull request's title. |
| `context.github.pull_request.body` | The pull request's description as it was when the run started, or an empty string if it has none. |
| `context.github.pull_request.html_url` | The pull request's URL on GitHub. |
| `context.github.pull_request.draft` | Whether the pull request is a draft. |
| `context.github.pull_request.labels` | The pull request's labels. |
| `context.github.pull_request.head_ref` | The pull request's branch name. |
| `context.github.pull_request.head_repository` | The repository the pull request's branch is in, which differs from yours for a pull request from a fork. |
| `context.github.pull_request.author.login` | The GitHub login of the pull request's author. |
| `context.github.pull_request.author.id` | The numeric GitHub account ID of the pull request's author. |
| `context.github.pull_request.author.type` | The type of the author's GitHub account: `User`, `Bot`, or `Organization`. |

For example, this check skips draft pull requests:

```yaml
checks:
  e2e:
    cmd: make e2e
    when:
      expr: "!context.github.pull_request.draft"
```

A run after merging has no pull request, and reading a `context.github.pull_request` field in that run is an error that fails the run. For a check that also runs after merging, guard the field with `has()`, such as `expr: "!has(context.github.pull_request) || !context.github.pull_request.draft"`.

If you set both `changed` and `expr`, the check runs only when both are true. To combine changed files with other conditions in other ways, call `changed()` in the expression with a list of patterns, which match files the same way as `when.changed`. For example, this check runs when a pull request changes a file under `docs/` or has the `docs` label:

```yaml
checks:
  docs:
    cmd: make docs
    when:
      expr: 'changed(["docs/**"]) || "docs" in context.github.pull_request.labels'
```

An expression can be up to 2,048 characters, and Chainguard Checks refuses one whose estimated cost to evaluate is over its limit.

Chainguard Checks evaluates conditions when it creates a run, against the pull request as it is then. If the run passes while a condition skipped a check, and you then change the pull request, such as its title or labels, the commit runs again. A passed run of a pull request that changes your Chainguard Checks configuration also runs again after such a change, whether or not a condition skipped a check. Refer to [Reruns when a pull request changes](/chainguard/checks/github/#reruns-when-a-pull-request-changes).

A pull request's author sets its `draft`, `title`, `head_ref`, and `body` fields, and anyone who can label it sets its `labels`. If a condition on one of these fields skips a blocking check, those people decide whether the check runs, and the summary check can pass without it. `chainctl checks explain` adds a note to each blocking check whose condition reads one of these fields.

### Run on request {#run-on-request}

A check with `when: {requested: true}` runs only when someone asks for it. Use this for slow or expensive checks that most pull requests don't need:

```yaml
checks:
  e2e-full:
    cmd: make e2e-full
    description: The full end-to-end suite against every supported database. Run it for changes to the storage layer or to database migrations.
    when:
      requested: true
```

A check that runs on request follows these rules:

- It must have a [`description`](#describe-a-check) that says what it covers and when it's worth running.
- `requested` can only be `true`, and the same `when` can't also set `changed` or `expr`.
- Its name can be at most 43 characters, so that its label fits GitHub's 50-character limit. When two files have a check with the same name, the label includes the file's name, such as `ci/run:go/e2e-full`, and the limit counts the file's name and the `/` after it too.
- A check that doesn't run on request can't need one that does, because it would then run only when the other check is requested.

To run the check on a pull request, add the label `ci/run:<check>`, such as `ci/run:e2e-full`. Refer to [Run a check on request](/chainguard/checks/github/#run-a-check-on-request) for details. A run after merging never runs a check on request.

A pull request can't make its own checks run only on request. The change takes effect after it merges, as described in [Change checks in a pull request](/chainguard/checks/github/#change-checks-in-a-pull-request).

## Describe a check {#describe-a-check}

A check's `description` says what the check covers and when it's worth running, in up to 1,024 characters.

In the directory layout, a check can also point to a longer explanation with `docs`, which names a Markdown file beside the check file:

```yaml {title=".chainguard/ci/e2e.yaml"}
version: 1
checks:
  e2e-full:
    cmd: make e2e-full
    description: The full end-to-end suite against every supported database. Run it for changes to the storage layer or to database migrations.
    docs: e2e-full.md
    when:
      requested: true
```

The file, `.chainguard/ci/e2e-full.md` in this example, must be directly in `.chainguard/ci/` and can be up to 1 MiB. Its name must end in `.md`, can use letters, digits, `.`, `_`, and `-`, and can be up to 128 bytes. If the file is missing or larger than 1 MiB, the configuration is invalid. Set `docs` on the check, not on a `foreach` entry. The single-file layout doesn't support `docs`.

If you turn on `requested_checks_agent`, the agent reads each check's `description` and `docs` to decide which checks to request. Refer to [Let an agent request checks](/chainguard/checks/github/#let-an-agent-request-checks).

## Advisory checks {#advisory-checks}

A check with `advisory: true` reports its real result on the pull request, with `(advisory)` in its title, but never makes the **Chainguard Checks (presubmit)** summary check fail. Use it for a check you want to see but not enforce yet, such as a new linter.

A blocking check can't need an advisory check, either with `needs` or by taking an [input](/chainguard/checks/variations-services-caches/#pass-files-between-checks) from it. If the advisory check failed, the blocking check wouldn't run, and the summary check would fail. Make both checks advisory, or both blocking.

A pull request can't make its own checks advisory. The change takes effect after it merges, as described in [Change checks in a pull request](/chainguard/checks/github/#change-checks-in-a-pull-request).

## Triggers {#triggers}

The `trigger` key sets which events run a check:

| Trigger | When the check runs |
| ------- | ------------------- |
| `presubmit` (default) | On each pull request, against the pull request merged into its base branch. |
| `postsubmit` | On each new commit on your default branch, after a change merges. |

To run a check at both times, list both:

```yaml
checks:
  test:
    cmd: go test ./...
    trigger: [presubmit, postsubmit]
```

Postsubmit results appear on the commit on your default branch, in a summary check named **Chainguard Checks (postsubmit)**.

A check can need another check, either with `needs` or by taking an [input](/chainguard/checks/variations-services-caches/#pass-files-between-checks) from it, only if the other check runs on every trigger that the first check runs on. The other check can run on more triggers. For example, a check without `trigger` runs on pull requests, so it can need a check with `trigger: [presubmit, postsubmit]`, but not one with only `trigger: postsubmit`. If a check breaks this rule, `chainctl checks validate` reports it, and on GitHub, the summary check for the missing trigger, such as **Chainguard Checks (presubmit)**, fails with **Run creation failed**.

## Timeouts {#timeouts}

By default, a check has no time limit of its own. A whole run can take up to two hours, and a check still running at that point fails. To fail a check sooner, set `timeout` to a duration, such as `10m` or `1h`. A check that times out gets no chance to clean up, as described in [How commands run](#how-commands-run).

## Resources {#resources}

By default, each check's VM has 2 vCPUs, 8 GB of memory, and a 14 GB disk. To give a check more, set `resources` to one of the following classes:

| Class | vCPUs | Memory | Disk |
| ----- | ----- | ------ | ---- |
| `medium` | 4 | 16 GB | 40 GB |
| `large` | 8 | 32 GB | 40 GB |
| `xlarge` | 16 | 64 GB | 40 GB |

On pull requests, a class without a suffix can run on either CPU architecture, and usually runs on arm64. Each built-in class also has `-amd64` and `-arm64` variants, such as `large-amd64`, that pin the architecture. With the built-in classes, use an `-amd64` class for a check that needs x86-64, such as one that downloads an x86-64 binary.

Chainguard Checks takes each check's class from the first of these that sets `resources`: the `foreach` entry, the check, the check's file, and `env/default.yaml` in the directory layout. If none of them sets `resources`, the check gets the default class.

Your organization's allowance sets the largest class you can use. With the Starter allowance, the largest is `medium`. If any check in a run asks for `large` or `xlarge`, the whole run fails before any check starts, and the summary check shows **Run failed**.

In each check's VM, `/tmp` is held in memory, and can hold up to a quarter of the VM's memory: about 2 GB with the built-in default, and 4 GB with `medium`. Files in `/tmp` use memory that the check's processes would otherwise have. Put large files, such as a virtual environment or build output, under `/var/tmp` or `/work`, which are on the VM's disk.

A check's VM has no KVM device, so tools that run their own VMs with KVM, such as Firecracker or QEMU with hardware acceleration, don't work in a check.

### Define your own resource classes {#define-your-own-resource-classes}

In the directory layout, each file in `.chainguard/ci/resources/` defines one resource class, named after the file. For example, the following file defines a class named `compute`:

```yaml {title=".chainguard/ci/resources/compute.yaml"}
version: 1
cpus: 8
memory: 16Gi
disk: 40Gi
platform:
  os: linux
  architecture: arm64
```

A check selects the class by name, such as `resources: compute`. Your classes add to the built-in classes, so checks can still name `medium` or `large-amd64`. Each class file follows these rules:

- The file's name, without `.yaml`, is the class's name. It uses lowercase letters, digits, and `-`, starts with a letter, and can be up to 63 characters. It can't be the name of a built-in class, such as `medium`, or the reserved names `default` and `auto`.
- Each file needs `version: 1` and `cpus`. `memory` and `disk` are whole numbers of `Mi` or `Gi`, such as `512Mi` or `16Gi`. A class without `memory` gets 4 GiB, and a class without `disk` gets 5 GiB.
- Only `platform` pins a class to an architecture, with `os: linux` and `architecture` set to `amd64` or `arm64`. A class without `platform` can run on either architecture, whatever its name.
- The single-file layout doesn't support your own classes, because a `.chainguard/ci/` directory beside `.chainguard/ci.yaml` makes the configuration invalid.

To give every check one of your classes unless it names another, set `resources` in `.chainguard/ci/env/default.yaml`:

```yaml {title=".chainguard/ci/env/default.yaml"}
version: 1
environment: {}
resources: compute
```

#### Replace the built-in classes with resources.yaml {#replace-the-built-in-classes-with-resources-yaml}

An older form, a single `.chainguard/ci/resources.yaml` file, lists classes under `resource_classes` and replaces the built-in classes with them. It must define a class named `default`, which a check gets when nothing sets its `resources`, and checks can't name `medium` or any other built-in class unless the file defines a class with that name. Its classes follow the same rules as class files.

A repository can't have both `resources.yaml` and a `resources/` directory. To move to class files, put each class in its own file under `.chainguard/ci/resources/`, delete `resources.yaml`, and set the class that its `default` defined in `env/default.yaml`, as in the earlier example.

Your organization's allowance limits your own classes too. If any check in a run asks for more vCPUs, memory, or disk than the allowance allows, the whole run fails before any check starts.

## Environment variables {#environment-variables}

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
      GOFLAGS: -tags=integration
```

In a check's `vars` or a `foreach` entry's `vars`, but not in `environment.vars`, a variable's value can also come from the pull request, with a binding such as `"${{ context.github.pull_request.number }}"`. The binding must be the variable's whole value, and it reads the same fields as [`when.expr`](#run-when-an-expression-is-true). Chainguard Checks fills in bindings when it creates the run:

- A list, such as `labels`, becomes a JSON array, such as `["bug","docs"]`.
- `context.trigger` becomes `presubmit` or `postsubmit`.
- A run after merging has no pull request, so a binding to a `context.github.pull_request` field leaves the variable unset. To tell an unset variable from an empty one in a script, test it with `${VAR+set}`.

A binding to `context.github.pull_request.body` works as follows:

- It sets the variable to the pull request's description as it was when the run started, line breaks included.
- Only the check's commands get the variable, not its [services](/chainguard/checks/variations-services-caches/#services).
- To pick up an edited description, use **Re-run** or push a new commit.
- The variable can't be `CHAINGUARD_BASE_REVISION`, `GOOGLE_APPLICATION_CREDENTIALS`, `GITHUB_TOKEN`, or `GOFLAGS`, which Chainguard Checks can set itself.
- The description can be up to 65,536 bytes, and can't contain a NUL character. A character outside ASCII takes more than one byte.

If a binding breaks these rules, the run fails, as described in [The summary check says the run couldn't be created or failed](/chainguard/checks/troubleshooting/#the-summary-check-says-the-run-couldnt-be-created-or-failed).

### Variables that Chainguard Checks sets {#variables-that-chainguard-checks-sets}

Chainguard Checks sets the following variables for each check's commands:

| Variable | Value |
| -------- | ----- |
| `PATH` | `/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin` |
| `HOME` | `/root`, or `/home/<name>` for a check that [runs as another user](/chainguard/checks/variations-services-caches/#run-as-another-user). |
| `USER` and `LOGNAME` | `root`, or the account's name for a check that runs as another user. |
| `TERM` | `xterm-256color` |
| `SSL_CERT_FILE`, `REQUESTS_CA_BUNDLE`, `PIP_CERT`, `CURL_CA_BUNDLE`, `NODE_EXTRA_CA_CERTS`, and `HEX_CACERTS_PATH` | `/etc/ssl/certs/ca-certificates.crt`, the VM's certificate bundle, which trusts the certificate authority described in [Network access](#network-access). |
| `CHAINGUARD_BASE_REVISION` | The SHA of the run's base commit, if the run has one. |
| `CG_CPUS`, `CG_MEMORY_MIB`, and `CG_DISK_MIB` | The VM's vCPUs, and its memory and disk in MiB, from the check's [resource class](#resources). |

For a pull request, the base commit is the base branch commit that the run merges the pull request into. For a run after merging, it's the new commit's first parent. Your repository's history is in the VM, so with `git` in your packages, a check can compare against it, such as with `git diff "$CHAINGUARD_BASE_REVISION"`.

In a pull request's check, `HEAD` is the commit that merges the pull request into its base branch. Chainguard Checks creates that commit for the run, and it's never pushed to GitHub, so a command that looks `HEAD` up on GitHub fails, such as a call to GitHub's API or a `git fetch` of the commit. Use `HEAD^2` for the pull request's own head commit, and `CHAINGUARD_BASE_REVISION`, which is `HEAD^1`, for the base commit.

A check that uses a [cache](/chainguard/checks/variations-services-caches/#cache-types) also gets the variables that its type sets, such as `GOCACHE` for `gobuild`. A check that uses a Google Cloud [workload identity](#credentials) also gets `GOOGLE_APPLICATION_CREDENTIALS`.

A variable that you set in `vars` replaces the value in the table, except `CHAINGUARD_BASE_REVISION`, which Chainguard Checks discards if you set it, and `CG_CPUS`, `CG_MEMORY_MIB`, and `CG_DISK_MIB`, which Chainguard Checks always sets. If you set one of the certificate variables, point it at a bundle that includes the certificates in `/etc/ssl/certs/ca-certificates.crt`, or HTTPS connections from the tools that read the variable fail.

Chainguard Checks doesn't set `CI`, `TMPDIR`, `LANG`, `TZ`, or any `GITHUB_` variables. Without `TMPDIR`, most tools write temporary files to `/tmp`, which is [held in memory](#resources). To use the VM's disk instead, set `TMPDIR` to `/var/tmp` in `vars`.

Variables specific to Chainguard Checks start with `CHAINGUARD_` or `CG_`, such as `CHAINGUARD_BASE_REVISION`, `CG_CPUS`, and the `CG_PLAN` variable that a [planner](/chainguard/checks/variations-services-caches/#compute-variations-during-a-run) gets. Don't start the names of your own variables with these prefixes.

## Report errors and annotations {#report-errors-and-annotations}

A check can print special lines to its output that Chainguard Checks turns into annotations and summaries on the pull request, or uses to protect its log:

| Line | What it does |
| ---- | ------------ |
| `::error file=main.go,line=12::message` | Reports an error as an annotation on that file and line. |
| `::warning file=main.go,line=12::message` | Reports a warning as an annotation on that file and line. |
| `::notice file=main.go,line=12::message` | Reports a notice as an annotation on that file and line. |
| `::sandbox-summary::`, then `::end-sandbox-summary::` | Adds the Markdown between the two lines to the check's output on GitHub. Refer to [Add a Markdown summary](#add-a-markdown-summary). |
| `::add-mask::value` | Hides `value` wherever it appears later in the check's log. |

An `::error`, `::warning`, or `::notice` line with a `file` becomes an annotation at that level. Without a `file`, the line appears in the check's output only. The `file` path must be relative to the repository's root, not to the check's `workdir`. A line can also set `endLine`, `col`, `endColumn`, and `title`. Without `line`, the annotation goes on line 1 of the file. Columns apply only to an annotation on a single line.

Chainguard Checks reads these lines only when `::` starts the line, and only from the last 1 MiB of a check's log, so a check with a long log should print them near the end. Chainguard Checks shows up to 50 annotations for each check, and annotations don't change whether a check passes.

The annotation lines use the same format as GitHub Actions workflow commands, so many linters that support GitHub Actions output work without changes.

### Add a Markdown summary {#add-a-markdown-summary}

In place of the `GITHUB_STEP_SUMMARY` file in GitHub Actions, a check can add a summary in Markdown to its output on GitHub, such as a list of the problems it found. Print the summary between a `::sandbox-summary::` line and a `::end-sandbox-summary::` line:

```yaml
checks:
  fmt:
    script: |
      gofmt -l . > /tmp/unformatted
      if [ -s /tmp/unformatted ]; then
        echo '::sandbox-summary::'
        echo 'These files need `gofmt`:'
        echo
        sed 's/^/- /' /tmp/unformatted
        echo '::end-sandbox-summary::'
        exit 1
      fi
```

A summary works as follows:

- Each marker must be on a line of its own. The summary appears in the check's output, above the end of the check's log.
- If a check prints several summaries, they appear together, in the order the check printed them.
- A summary ends with the step that prints it. If the step ends before `::end-sandbox-summary::`, the summary appears as far as it went, with a note.
- HTML appears as text, except the `<details>`, `<summary>`, and `<br>` tags.
- Links and images stay only if they point into your repository on GitHub, under `https://github.com/<owner>/<repo>/`, or to the run pages that a check's **Details** link opens. Other links become plain text.
- An `@` mention in a summary doesn't notify anyone.
- GitHub limits the size of a check's output, so Chainguard Checks cuts a summary longer than about 53 KiB and links to the full log. In a check with `foreach`, each variation's summary can be up to 8 KiB.

## Git in a check's VM {#git-in-a-checks-vm}

A check's `/work` directory is a Git repository that holds the commit under test and its full history, but it isn't set up like a clone of your repository. Some common Git commands and tools fail in it:

- `HEAD` is detached at the commit under test, and the repository has no branches or tags. Commands that read tags, such as `git describe`, fail, and tools that compute a version from tags, such as GoReleaser and setuptools-scm, fail or report the wrong version.
- The `origin` remote points to your repository's URL on GitHub, without a credential. Because the repository has no remote branches, a command that compares against a remote branch, such as `git diff origin/main`, fails.
- Git has no `user.name` or `user.email` set, so `git commit` fails.

To work around these differences:

- To compare against the base branch, use the commit in `CHAINGUARD_BASE_REVISION`, such as `git diff --name-only "$CHAINGUARD_BASE_REVISION" HEAD`. Refer to [Variables that Chainguard Checks sets](#variables-that-chainguard-checks-sets).
- To read tags from a public repository, add `github.com` to the check's `network.egress`, and run `git fetch --tags origin` before the command that reads them. During the beta, a check can't fetch tags from a private repository, because it gets no GitHub credential. Refer to [Credentials](#credentials).
- To create a commit, set a Git identity first, such as with `git config user.name ci` and `git config user.email ci@example.com`.

A check that runs as another user doesn't own the `.git` directory, so it can't fetch tags or create commits. Refer to [Run as another user](/chainguard/checks/variations-services-caches/#run-as-another-user).

## Credentials {#credentials}

A check runs without credentials by default. Its `/work` directory holds your repository's tracked files and history at the commit it tests, so most checks need none. Submodule directories are empty, and files that Git LFS tracks hold their pointer files instead of their content. During the beta, a check gets no GitHub credential, so it can't fetch from private GitHub repositories, such as private Go modules or submodules, or private Git LFS content. To add files from a public repository, use a [`git` input](/chainguard/checks/variations-services-caches/#check-out-another-repository).

A check that must authenticate to Google Cloud, AWS, Azure, or Chainguard, such as to pull private images from `cgr.dev`, can use a *workload identity*. You declare workload identities in `.chainguard/ci/identities.yaml`, and a check requests one by name with `identity`. Workload identities need setup on the provider's side as well, as described in [Set up the provider](/chainguard/checks/identity-and-trust/#set-up-the-provider).

Unless `identities.yaml` on your default branch has a `trust` section, any open pull request can get an identity, including one from a fork. Refer to [Workload identities and trust](/chainguard/checks/identity-and-trust/) for the file's format, which pull requests get an identity, and how to limit them.

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
      python3 -m venv /var/tmp/venv
      . /var/tmp/venv/bin/activate
      pip install -r requirements.txt
      pytest
    network:
      egress: [pypi.org, files.pythonhosted.org]
```

The script creates a virtual environment so that `pip` installs packages for the check alone. It puts the environment in `/var/tmp`, on the VM's disk, because [`/tmp` is held in memory](#resources). Both `pypi.org` and `files.pythonhosted.org` are in `egress`, because pip reads the package index from the first and downloads files from the second.
