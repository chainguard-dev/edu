---
date: 2026-10-28T16:22:54Z
title: "chainctl checks validate"
slug: chainctl_checks_validate
url: /platform/chainctl/chainctl-docs/chainctl_checks_validate/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl checks validate

Lint a repository's checks configuration offline.

### Synopsis

Lint a repository's checks configuration against the rules the sandbox plane enforces, with no VM, network, or API call.

PATH is a repository root, an authored file under .chainguard/, or a standalone authored YAML file. With no PATH, the command finds the checkout root and validates its authored configuration, including a single .chainguard/ci.yaml. An authored file selects its repository's complete configuration, so references and layout conflicts are checked as they are on a pull request.

A repository's authored configuration (.chainguard/ci/, or the v1 .chainguard/*.yaml layout) is parsed the way the planner reads a pull request's; any problem the parser refuses is reported with its file and position. Each resolved workflow is then checked against the executor contract.

The presubmit, postsubmit, and cron dependency graphs are checked first: every check a job needs, or reads a tree from, must run under each trigger the job runs under. The document is then checked against the executor's lowering rules. Warnings name fields the executor ignores; refusals are what the plane would reject. Git refs are resolved at admission; offline validation warns about unresolved refs without checking repository access or ref existence. The command exits non-zero when there is any parse problem, refusal or graph error.

```
chainctl checks validate [PATH] [--output=json]
```

### Examples

```
  # Lint the checkout's checks configuration
  chainctl checks validate

  # Lint another repository's
  chainctl checks validate ../app

  # Every refusal and warning of a drafted document, as JSON
  chainctl checks validate workflow.yaml -o json
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

