---
date: 2026-09-21T22:21:18Z
title: "chainctl libraries verify"
slug: chainctl_libraries_verify
url: /platform/chainctl/chainctl-docs/chainctl_libraries_verify/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries verify

A tool to analyze the use of Chainguard Libraries in various artifacts

### Synopsis

verify analyzes various artifacts
(directories, archives, packages) to analyze how much was built from source by Chainguard,
based on SBOM data, signatures, and artifact inspection.

You can specify one or more paths to analyze multiple artifacts in a single command.

For container images, you can use:
  - Registry references (e.g., cgr.dev/chainguard/nginx:latest)
  - Local single-part images (e.g., redis:latest, nginx:alpine)
  - Docker archive format (docker-archive:/path/to/image.tar)
  - Local images with prefixes (localhost/myapp:latest)

JavaScript package manager caches (npm, pnpm, Yarn Classic) are auto-detected
in container images and local directories by their structure.

Passing a JavaScript lockfile (package-lock.json, npm-shrinkwrap.json,
pnpm-lock.yaml, yarn.lock, bun.lock) reports which of its registry entries carry
a digest covered by a Chainguard attestation, using the integrity hashes the
lockfile records. No install or package cache is required.

An entry counts as verified only when the attested digest is bound to the
tarball bytes the entry permits — that is, when any install honoring the entry's
integrity constraint must use the attested bytes. A lone integrity hash binds:
the package manager rejects any tarball that does not match it. An entry listing
several hashes does not, since any of them may be satisfied — those are reported
as attested but not bound, unless the resolved URL names the same package on
Chainguard's built route (libraries.cgr.dev/javascript/), which fixes the
source. The upstream proxy route serves upstream bytes and does not bind.

A lockfile rewritten by "libraries update-hashes" in its default append mode
keeps the original registry hash alongside the Chainguard one. Such entries
verify only while resolved points at the Chainguard built route, so behind a
private proxy or custom --registry-url they report as not bound. Use
"libraries update-hashes --replace" to record a single Chainguard hash per
entry, which binds regardless of where the entry resolves from.

No downloaded bytes are examined, and platform, optional dependencies, overrides,
and registry configuration still affect what a package manager selects. Entries
with no usable digest — linked and git dependencies, and Yarn Berry's non-SRI
checksums — are reported at zero coverage.

Entries the registry could not answer for — an outage, or rejected credentials —
are reported as unchecked rather than unverified, since a service problem is not
a provenance finding. Requests are retried before an entry is called unchecked.

This report is informational: the exit status does not reflect coverage. Coverage
counts entries Chainguard built from source, so a package that is simply not
built from source is not a defect, and gating a build on the percentage is not
the intended use. Per-entry results are available with "-o json --detailed".

Remediated (CVE-patched) Java artifacts, whose versions carry a "-0.cgr.<rev>" suffix
(e.g. 3.5.0-0.cgr.2), are resolved from the java-remediated repository; other Java
artifacts are resolved from the java repository.

```
chainctl libraries verify [path...] [flags]
```

### Examples

```
  # Analyze a local JAR file
  chainctl libraries verify myapp.jar

  # Analyze multiple files
  chainctl libraries verify build/libs/*.jar build/libs/*.war

  # Analyze a local Python virtual environment
  chainctl libraries verify ./venv/

  # Analyze with JSON output
  chainctl libraries verify -o json build/libs/*.jar

  # Analyze container images
  chainctl libraries verify cgr.dev/chainguard/maven:latest

  # Analyze remote artifact
  chainctl libraries verify remote:example.com/maven2/org/apache/commons/commons-lang3/3.12.0/commons-lang3-3.12.0.jar

  # Verify a lockfile without installing anything
  chainctl libraries verify package-lock.json
  chainctl libraries verify pnpm-lock.yaml

  # Per-entry results for machine consumption
  chainctl libraries verify package-lock.json -o json --detailed

  # Verify npm cache (auto-detected by _cacache/index-v5/ structure)
  chainctl libraries verify "$(npm config get cache)"

  # Verify pnpm store (auto-detected; supports pnpm 10+ index dirs and the
  # pnpm 11 SQLite index, and the versioned path reported by newer pnpm)
  chainctl libraries verify "$(pnpm store path)"

  # Verify Yarn Classic (v1.x) cache
  chainctl libraries verify yarn:
  chainctl libraries verify yarn:~/Library/Caches/Yarn/v6
```

### Options

```
      --concurrency int         Number of artifacts verified in parallel: nested archives within a single input, or inputs across a multi-path run (0 = default of 16)
  -d, --detailed                Show detailed per-artifact results
      --ecosystems-url string   URL for the Ecosystems Proxy (defaults to https://libraries.cgr.dev)
      --no-color                Disable colored output
  -o, --output string           Output format (text, json, yaml) (default "text")
      --parent string           Parent organization for authentication
      --verbose                 Enable verbose output
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
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl libraries](/platform/chainctl/chainctl-docs/chainctl_libraries/)	 - Ecosystem library related commands.

