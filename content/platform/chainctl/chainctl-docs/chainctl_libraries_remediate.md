---
date: 2026-09-18T19:27:05Z
title: "chainctl libraries remediate"
slug: chainctl_libraries_remediate
url: /platform/chainctl/chainctl-docs/chainctl_libraries_remediate/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries remediate

Discover and apply Chainguard -cgr.N CVE remediations for a JavaScript project

### Synopsis

remediate finds the highest installable Chainguard remediation (-cgr.N) for each
package in a JavaScript project's resolved dependency tree, then writes the
direct-dependency pins and package-manager overrides that deliver it.

Provide a project directory, or omit it to use the current directory. The
package manager is detected from the lockfile: package-lock.json (npm),
pnpm-lock.yaml (pnpm), yarn.lock (Yarn Classic and Berry), bun.lock/bun.lockb
(Bun), or deno.lock (Deno).

For Deno projects, chainctl requires Deno 2.7 or later, package.json, and deno.lock.
It uses npm overrides in package.json to pin dependencies to -cgr.N versions.
It rejects Deno projects with deno.json or deno.jsonc in the project root.

A -cgr.N prerelease is never matched by a normal range such as ^1.3.1, so
adoption is always deliberate: delivery is an exact pin plus a package-manager
override, never a silent substitution.

Modes:
  - No flag: plan only. Reports what would change and writes nothing.
  - --apply: write the planned changes, then synchronize the lockfile with the real package manager in an isolated copy of the project. The project is left untouched until the selected -cgr.N artifacts and the unchanged unrelated dependencies are both verified.
  - --check: CI gate. Writes nothing and exits non-zero when any package in the tree has a remediation available that the project has not adopted.

--apply additionally needs a project .npmrc pointing at the Chainguard registry,
because the lockfile synchronization resolves the -cgr.N artifacts through it.
Run 'chainctl auth configure-npm' once per project to write one. Neither the
default plan mode nor --check needs it.

Discovery is registry-highest: for each exactly resolved version it selects the
greatest -cgr.N published for that base version. Packages resolved from a
non-public registry, and those whose lockfile entry cannot be proven to resolve
through a public registry, are excluded.

Authentication matches 'chainctl libraries update-hashes': a libraries-scoped
session ('chainctl auth login --audience=libraries.cgr.dev') is used directly;
otherwise pass --token, --username/--password, or --parent to authenticate via
'chainctl auth pull-token'. With no credential source and no --parent, remediate
prompts for an organization.

```
chainctl libraries remediate [project-dir] [flags]
```

### Examples

```
  # Show the remediations available for the project in the current directory
  chainctl libraries remediate

  # Apply them and synchronize the lockfile
  chainctl libraries remediate --apply

  # Fail a CI job when an unadopted remediation exists
  chainctl libraries remediate --check

  # Machine-readable plan for a project in another directory
  chainctl libraries remediate --check --format json ./services/api
```

### Options

```
      --apply                   Write the planned pins and overrides and synchronize the lockfile. Mutually exclusive with --check.
      --check                   Report available remediations and exit non-zero if any are unapplied, without writing changes. Use as a CI gate. Mutually exclusive with --apply.
      --ecosystems-url string   URL for the Ecosystems Proxy (defaults to https://libraries.cgr.dev). The /javascript path segment is appended automatically. Candidates are still validated against tarball URLs under https://libraries.cgr.dev/javascript, so only production or a proxy that preserves those URLs will yield remediations.
      --format string           Output format alias for --output: "json" or "none". Takes precedence over --output when both are set.
      --ignore-netrc            Do not read credentials from ~/.netrc ($NETRC).
      --no-auth                 Send no authentication when discovering remediations. Overrides all ambient credential sources. Does not affect --apply, whose lockfile synchronization still authenticates to the registry with the project .npmrc. Mutually exclusive with the explicit --token and --username/--password flags.
      --no-color                Disable colored output
      --parent string           Parent organization for authentication via 'chainctl auth pull-token'. Not needed when --token, --username/--password, the CHAINCTL_AUTH_TOKEN/CHAINCTL_REGISTRY_USERNAME env vars, or a matching ~/.netrc entry provides credentials.
      --password ps             Basic-auth password. Must be paired with --username. Also readable from $CHAINCTL_REGISTRY_PASSWORD. Prefer the env-var form to avoid leaking the value via ps or shell history.
      --token string            Literal bearer token to use as the basic-auth password (username is set to "token-user"). Mutually exclusive with --username/--password.
      --username string         Basic-auth username. Must be paired with --password. Also readable from $CHAINCTL_REGISTRY_USERNAME.
```

### Options inherited from parent commands

```
      --api string         The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string    The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string      A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string     The url of the Chainguard platform Console. (default "https://console.chainguard.dev")
      --force-color        Force color output even when stdout is not a TTY.
  -h, --help               Help for chainctl
      --issuer string      The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
      --log-level string   Set the log level (debug, info) (default "ERROR")
  -o, --output string      Output format. One of: [csv, env, go-template, id, json, markdown, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl libraries](/platform/chainctl/chainctl-docs/chainctl_libraries/)	 - Ecosystem library related commands.

