---
date: 2026-10-26T19:49:34Z
title: "chainctl checks trends"
slug: chainctl_checks_trends
url: /platform/chainctl/chainctl-docs/chainctl_checks_trends/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl checks trends

Show how long the slowest checks take, hour by hour.

### Synopsis

Show the median, 95th and 99th percentile durations of checks for every
hour of a window, with how many attempts each hour sampled.

The Facts analytics API reports trends for the ten checks with the most total
attempt runtime in the window. --check shows one of them, by name; a check
outside those ten has no trend. An hour with no timed attempt is absent
rather than zero. Cache hits are left out.

The window is the 14 days ending now by default; --since or --from/--to
choose another, of at most 31 days. The window and how fresh the data is are
printed above the table, since ingestion runs behind the checks it reads.

```
chainctl checks trends [--facts-url URL] [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--repo REPO] [--since DURATION | --from TIME --to TIME] [--check CHECK] [--output=json|table]
```

### Examples

```
  # How go-test's duration moved over the last three days
  chainctl checks trends --repo chainguard-dev/mono --check go-test --since 3d

  # Every trend, for scripts
  chainctl checks trends -o json
```

### Options

```
      --check string       Only this check, by name.
      --facts-url string   URL of the Facts analytics API. Overridden by $CHAINCTL_FACTS_URL. (default "https://facts.chainbox.dev")
      --from string        The window's start, an RFC 3339 time; needs --to.
      --parent string      The organization or folder (name or ID) the checks ran in. Defaults to $CHAINCTL_SANDBOX_GROUP, then the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
      --repo string        Only checks of this repository: owner/repo for GitHub, or host/path.
      --since string       The window ending now, such as 7d or 36h; at most 31d. Defaults to 14d.
      --to string          The window's end, an RFC 3339 time, exclusive; needs --from.
      --token string       Bearer token for the Facts host. Overrides $CHAINCTL_AUTH_TOKEN and the chainctl session. Prefer passing it via the environment to keep it out of shell history.
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

* [chainctl checks](/platform/chainctl/chainctl-docs/chainctl_checks/)	 - Inspect and manage a repository's Checks on the Chainguard sandbox plane.

