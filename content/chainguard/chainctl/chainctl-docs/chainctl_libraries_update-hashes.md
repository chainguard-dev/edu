---
date: 2026-04-30T18:48:24Z
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
```

### Options

```
      --cuda string             CUDA variant to include alongside python (e.g. "cu124", "cu130")
      --dry-run                 Show what would change without writing
      --ecosystem string        Ecosystem: "auto", "js", or "python" (default "auto")
      --ecosystems-url string   URL for the Ecosystems Proxy (defaults to https://libraries.cgr.dev)
      --no-color                Disable colored output
      --parent string           Parent organization for authentication
      --remediated              Use python-remediated registry (Python only)
      --replace                 Replace integrity hashes instead of appending (no-op for formats that only support replacement)
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

