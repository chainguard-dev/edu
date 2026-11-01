---
date: 2026-10-30T14:11:50Z
title: "chainctl checks top"
slug: chainctl_checks_top
url: /platform/chainctl/chainctl-docs/chainctl_checks_top/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl checks top

Rank checks by attempts, runtime or failure rate.

### Synopsis

Rank the organization's checks over a window by how often they ran
(--by count), how long they ran in total (--by runtime, the default), or how
often they failed or errored (--by failures).

The Facts analytics API ranks the 20 checks with the most attempts, the
most total runtime and the highest failure rate, so --limit is at most 20.
Attempts count retries and partial attempts; cache hits are left out. A
failure rate is (failed + errored) / attempts, and only a check with at least
100 attempts has one, so --by failures ranks only those.

The window is the 14 days ending now by default; --since or --from/--to
choose another, of at most 31 days. The window and how fresh the data is are
printed above the table, since ingestion runs behind the checks it reads.

```
chainctl checks top [--facts-url URL] [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--repo REPO] [--since DURATION | --from TIME --to TIME] [--by count|runtime|failures] [--limit N] [--output=json|table]
```

### Examples

```
  # Where mono's CI time went in the last week
  chainctl checks top --repo chainguard-dev/mono --since 7d

  # The flakiest checks, for scripts
  chainctl checks top --by failures -o json
```

### Options

```
      --by string          The ranking: count, runtime or failures. (default "runtime")
      --facts-url string   URL of the Facts analytics API. Overridden by $CHAINCTL_FACTS_URL. (default "https://facts.chainbox.dev")
      --from string        The window's start, an RFC 3339 time; needs --to.
      --limit int          The most checks to show; at most 20. (default 20)
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

