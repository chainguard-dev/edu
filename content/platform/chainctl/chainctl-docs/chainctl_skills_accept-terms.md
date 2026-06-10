---
date: 2026-06-08T21:00:27Z
title: "chainctl skills accept-terms"
slug: chainctl_skills_accept-terms
url: /chainguard/chainctl/chainctl-docs/chainctl_skills_accept-terms/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl skills accept-terms

Accept legal terms required to publish skills.

### Synopsis

Accept the legal documents required to publish skills to skills.cgr.dev.

An org owner must run this once per org before any 'chainctl skills push' will
succeed. Re-running after acceptance is a no-op. --group accepts either the
org name (e.g. "acme.com") or its UIDP; omit it for an interactive picker.

For CI use cases where an interactive TUI isn't available, pass --yes. By
using --yes you confirm you have read and agreed to the legal documents
referenced in https://www.chainguard.dev/legal/agent-skills-disclosure.

```
chainctl skills accept-terms [flags]
```

### Options

```
      --group string   Name or UIDP of the org to accept terms for
      --yes            Accept legal terms non-interactively. By using this flag you confirm you have read and agreed to the documents referenced in https://www.chainguard.dev/legal/agent-skills-disclosure.
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

* [chainctl skills](/chainguard/chainctl/chainctl-docs/chainctl_skills/)	 - Skills registry related commands.

