---
date: 2026-10-09T15:36:02Z
title: "chainctl skills validate"
slug: chainctl_skills_validate
url: /platform/chainctl/chainctl-docs/chainctl_skills_validate/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl skills validate

Check a local skill directory's format (not its authenticity) without making network calls.

### Synopsis

Check a local skill directory for spec compliance without making network calls.

validate checks format only: SKILL.md frontmatter, the name, description,
compatibility, and allowed-tools fields, the directory size, and which files
would be published. It does not check authenticity, and a passing result says
nothing about who published a skill. To check that Chainguard signed a
published skill, run `chainctl skills verify <ref>`.

```
chainctl skills validate [<path>] [flags]
```

### Options

```
      --strict   Also report warnings for optional recommended fields.
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

* [chainctl skills](/platform/chainctl/chainctl-docs/chainctl_skills/)	 - Skills registry related commands.

