---
date: 2026-06-25T19:50:48Z
title: "chainctl libraries update-hashes"
slug: chainctl_libraries_update-hashes
url: /chainguard/chainctl/chainctl-docs/chainctl_libraries_update-hashes/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries update-hashes

Update lockfile integrity hashes with Chainguard Libraries checksums

### Synopsis

update-hashes reads package lockfiles and updates integrity hashes with checksums from Chainguard Libraries.

Provide a path to a specific lockfile, or omit it to auto-detect a lockfile in the current directory.

By default, Chainguard hashes are appended alongside existing hashes in
supported formats (e.g. pip-tools, poetry). Use --replace to replace them.

Note: formats that store a single hash per artifact (uv.lock, pdm.lock, pylock.toml) always replace — --replace has no effect on them.

JavaScript formats:
  - package-lock.json (npm v2/v3)
  - yarn.lock (v1 and berry/v2+)
  - pnpm-lock.yaml
  - bun.lock

Python formats:
  - requirements.txt (pip-tools, with --hash)
  - poetry.lock
  - pdm.lock
  - uv.lock
  - pylock.toml (PEP 751)
  - Pipfile.lock

The ecosystem is auto-detected from the lockfile name. Use --ecosystem to override.

For Python, hashes are fetched from the Chainguard Libraries "python" catalog by default.
Use --remediated to fetch from "python-remediated" (CVE-patched packages), and --cuda
to also include packages from the matching CUDA variant catalog.

Authentication:
  If you log in scoped to the libraries registry
  ('chainctl auth login --audience=libraries.cgr.dev'), that session token is
  used directly — no --parent or prompt needed. A plain 'chainctl auth login'
  (console-api audience) does NOT work: the libraries registry requires a
  libraries.cgr.dev-scoped token and a console-api token cannot be re-audienced
  to it. In that case, with no other credential, update-hashes prompts for an
  organization and authenticates via 'chainctl auth pull-token'; pass --parent to
  skip the prompt. To
  authenticate without an issuer connection (e.g. from a rebuilder workflow), pass
  --token or set CHAINCTL_AUTH_TOKEN (its audience must include libraries.cgr.dev;
  mint one with 'chainctl auth token --audience libraries.cgr.dev'). To
  authenticate against a private proxy (e.g. Artifactory/JFrog) with real
  basic-auth credentials, use --username and --password (or set
  CHAINCTL_REGISTRY_USERNAME and CHAINCTL_REGISTRY_PASSWORD). Credentials are also
  read from ~/.netrc ($NETRC if set) for the registry's host; an explicit --parent
  takes precedence over a matching .netrc entry, and --ignore-netrc skips ~/.netrc
  entirely (useful when an ambient entry for npm/yarn/pip would otherwise shadow
  the Chainguard-native methods).

  To send no authentication at all (for a network-limited private registry that
  requires none and rejects any Authorization header), pass --no-auth. It overrides
  every ambient credential source — the CHAINCTL_AUTH_TOKEN / CHAINCTL_REGISTRY_USERNAME /
  CHAINCTL_REGISTRY_PASSWORD env vars, ~/.netrc, and 'chainctl auth pull-token' —
  so no credential can leak to the registry. It is
  mutually exclusive with the explicit --token and --username/--password flags
  (passing both is a contradiction and is rejected).

Custom registry URLs:
  Use --registry-url <url> to point at a private proxy whose path layout does not
  match libraries.cgr.dev (no /javascript or /python/simple suffix is appended;
  the value is used verbatim as the per-ecosystem base).

  When --registry-url is set, the Chainguard-specific token sources are not
  consulted (CHAINCTL_AUTH_TOKEN env var and 'chainctl auth pull-token') — sending
  the Chainguard JWT as a basic-auth password to a third-party host would be a
  credential leak. Authenticate with --token, --username/--password,
  $CHAINCTL_REGISTRY_USERNAME + $CHAINCTL_REGISTRY_PASSWORD, or a matching ~/.netrc
  entry instead.

```
chainctl libraries update-hashes [lockfile-path] [flags]
```

### Examples

```
  # Auto-detect lockfile in the current directory
  chainctl libraries update-hashes

  # Update hashes in a specific npm lockfile
  chainctl libraries update-hashes package-lock.json

  # Update hashes in a Python pip-tools requirements file
  chainctl libraries update-hashes path/to/requirements.txt

  # Preview changes without writing the file
  chainctl libraries update-hashes --dry-run package-lock.json

  # Replace hashes (instead of appending alongside existing ones)
  chainctl libraries update-hashes --replace uv.lock

  # Include CUDA variant packages for Python
  chainctl libraries update-hashes --cuda cu128 uv.lock

  # Query an unauthenticated private registry, sending no credentials
  chainctl libraries update-hashes --registry-url https://registry.internal/cg --no-auth uv.lock
```

### Options

```
      --cuda string                    CUDA variant to include alongside python (e.g. "cu124", "cu130")
      --dry-run                        Show what would change without writing
      --ecosystem string               Ecosystem: "auto", "js", or "python" (default "auto")
      --ecosystems-url string          URL for the Ecosystems Proxy (defaults to https://libraries.cgr.dev). Paths /javascript/{name}/{version} (JS) and /{python,python-remediated,cu###}/simple (Python) are appended automatically. Mutually exclusive with --registry-url.
      --fallback-registry-url string   Registry URL used to synthesize tarball URLs for JS packages not found in Chainguard Libraries (e.g. https://registry.npmjs.org). Empty (the default) disables fallback synthesis; if any package requires a fallback URL, the command fails with a list of offenders. WARNING: pointing this at a public registry such as https://registry.npmjs.org can cause installation of malicious packages — prefer a private/internal registry you trust.
      --ignore-netrc                   Do not read credentials from ~/.netrc ($NETRC). Use this to keep an ambient .netrc entry (e.g. one configured for npm/yarn/pip) from shadowing the Chainguard-native methods: with this set, a stale or unrelated .netrc entry for the registry host is ignored, so authentication falls through to 'chainctl auth pull-token' (with --parent) or the interactive organization prompt.
      --include-all-scopes             Ignore per-scope registries configured in .npmrc and reroute every package to Chainguard. JavaScript only. Mutually exclusive with --include-scope.
      --include-scope strings          npm scope(s) (e.g. @myorg) to reroute to Chainguard even when .npmrc configures them to a different registry. By default, packages in a scope that .npmrc pins to a non-Chainguard registry are left untouched. Repeatable and/or comma-separated. JavaScript only.
      --no-auth                        Send no authentication to the registry. Use for a network-limited private registry that requires none and rejects any Authorization header. Overrides all ambient credential sources ($CHAINCTL_AUTH_TOKEN, $CHAINCTL_REGISTRY_USERNAME/$CHAINCTL_REGISTRY_PASSWORD, ~/.netrc, and 'chainctl auth pull-token'). Mutually exclusive with the explicit --token and --username/--password flags.
      --no-color                       Disable colored output
      --parent string                  Parent organization for authentication via 'chainctl auth pull-token'. Not needed when --token, --username/--password, the CHAINCTL_AUTH_TOKEN/CHAINCTL_REGISTRY_USERNAME env vars, or a matching ~/.netrc entry provides credentials.
      --password ps                    Basic-auth password. Must be paired with --username. Also readable from $CHAINCTL_REGISTRY_PASSWORD. Prefer the env-var form to avoid leaking the value via ps or shell history.
      --registry-url string            Full base URL of the registry to query, used verbatim (no /javascript or /python/simple suffix is appended). Use this when pointing at a private proxy (Artifactory/JFrog) whose path layout differs from libraries.cgr.dev. Mutually exclusive with --ecosystems-url, --remediated, --cuda. NOTE: when this flag is set, Chainguard-specific token sources (CHAINCTL_AUTH_TOKEN, 'chainctl auth pull-token') are NOT consulted, to avoid leaking the Chainguard JWT to a third-party host. Authenticate with --token, --username/--password, $CHAINCTL_REGISTRY_USERNAME/$CHAINCTL_REGISTRY_PASSWORD, or ~/.netrc.
      --remediated                     Use python-remediated registry (Python only)
      --replace                        Replace integrity hashes instead of appending (no-op for formats that only support replacement)
      --token string                   Literal bearer token to use as the basic-auth password (username is set to "token-user"). Against libraries.cgr.dev this behaves like setting CHAINCTL_AUTH_TOKEN; under --registry-url, only --token is honored (the env var is ignored to avoid leaking the Chainguard JWT to a third-party host). Mutually exclusive with --username/--password.
      --username string                Basic-auth username. Must be paired with --password. Use for private proxies (Artifactory/JFrog) that require real credentials. Also readable from $CHAINCTL_REGISTRY_USERNAME.
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

* [chainctl libraries](/chainguard/chainctl/chainctl-docs/chainctl_libraries/)	 - Ecosystem library related commands.

