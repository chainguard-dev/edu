---
date: 2026-09-02T22:28:18Z
title: "chainctl policy decision list"
slug: chainctl_policy_decision_list
url: /platform/chainctl/chainctl-docs/chainctl_policy_decision_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policy decision list

List policy decisions.

### Synopsis

List recorded policy decisions to see which image digests a policy
allowed or denied at pull time.

Each decision shows the repository, the digest, the policy that
evaluated it, the mode, the outcome, and when it was pulled.

Decisions are scoped to one organization: pass --parent, or omit it to
use your configured default group, or (with no default configured) the
single organization you can access — you are prompted when several are
available. Within that scope, filter by --repo for a single repository,
by --policy for a single policy, by --mode or --result for a subset of
outcomes, and by --since for a time window.

Decisions are listed most recent first. By default the 20 most recent
are shown; use --limit (1-100) to change how many are returned.

For a multi-arch image the DIGEST column may show the index digest,
while pulls are enforced against the per-platform child manifest; run
"chainctl policy check" to find the child digest an override must
target.

With -o json the output is an object with an "items" array (one entry
per decision) and a string "totalCount"; read .items[] rather than
treating the output as a top-level array.

```
chainctl policy decision list [--parent ORG] [--repo REPO] [--policy POLICY] [--mode MODE] [--result RESULT] [--since Nd] [--limit N] [--output=json|table] [flags]
```

### Examples

```
  # List decisions for your default (or only) organization
  chainctl policy decision list
  
  # List decisions for a specific organization
  chainctl policy decision list --parent=engineering
  
  # List what the cooldown policy would have blocked in the last day
  chainctl policy decision list --parent=engineering --policy=cooldown --result=DENIED --since=1d
  
  # List all decisions recorded for a single repository
  chainctl policy decision list --parent=engineering --repo=nginx
  
  # Show the 50 most recent decisions
  chainctl policy decision list --parent=engineering --limit=50
  
  # List decisions as JSON for scripting; the payload is an object, so read .items[]
  chainctl policy decision list --parent=engineering -o json | jq '.items[]'
```

### Options

```
      --limit int              Maximum number of decisions to return, most recent first (1-100). (default 20)
      --mode string            Only show decisions evaluated in this mode (ENFORCE or DRY_RUN; the POLICY_MODE_ prefixed value from -o json is also accepted).
      --parent string          The name or id of the organization to list decisions for.
      --policy string          Only show decisions for this policy (name or UIDP).
      --repo string            Only show decisions for this repository.
      --resource-type string   Resource type used to disambiguate a policy referenced by name (shorthand: Repo, Python, Java, Javascript; or a full type). Ignored when the policy is given by UIDP.
      --result string          Only show decisions with this outcome (ALLOWED, DENIED, or ERROR; the RESULT_ prefixed value from -o json is also accepted).
      --since string           Only show decisions pulled within a window given as a positive whole number of days followed by d, e.g. 7d.
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

* [chainctl policy decision](/platform/chainctl/chainctl-docs/chainctl_policy_decision/)	 - Inspect policy decisions.

