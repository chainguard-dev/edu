---
date: 2026-06-30T03:10:49Z
title: "chainctl policies decision list"
slug: chainctl_policies_decision_list
url: /chainguard/chainctl/chainctl-docs/chainctl_policies_decision_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies decision list

List policy decisions.

### Synopsis

List recorded policy decisions to see which image digests a policy
allowed or denied at pull time.

Each decision shows the digest, the policy that evaluated it, the mode,
the outcome, and the reason when one is available. Filter by --parent
for a specific organization, by --repo for all decisions recorded on a
single repository, by --policy for a single policy, by --mode or
--result for a subset of outcomes, and by --since for a time window.

```
chainctl policies decision list [--parent ORG] [--repo REPO] [--policy POLICY] [--mode MODE] [--result RESULT] [--since DAYS] [--output=json|table] [flags]
```

### Examples

```
  # List decisions for an organization
  chainctl policies decision list --parent=engineering
  
  # List what the cooldown policy would have blocked in the last day
  chainctl policies decision list --parent=engineering --policy=cooldown --result=DENIED --since=1d
  
  # List all decisions recorded for a single repository
  chainctl policies decision list --parent=engineering --repo=nginx
  
  # List decisions in JSON format for scripting
  chainctl policies decision list --parent=engineering -o json
```

### Options

```
      --mode string     Only show decisions evaluated in this mode (ENFORCE or DRY_RUN).
      --parent string   The name or id of the organization to list decisions for.
      --policy string   Only show decisions for this policy (name or UIDP).
      --repo string     Only show decisions for this repository.
      --result string   Only show decisions with this outcome (ALLOWED, DENIED, or ERROR).
      --since string    Only show decisions pulled within this many days, e.g. 7d.
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

* [chainctl policies decision](/chainguard/chainctl/chainctl-docs/chainctl_policies_decision/)	 - Inspect policy decisions.

