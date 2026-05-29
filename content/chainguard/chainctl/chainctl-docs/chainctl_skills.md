---
date: 2026-05-28T17:13:42Z
title: "chainctl skills"
slug: chainctl_skills
url: /chainguard/chainctl/chainctl-docs/chainctl_skills/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl skills

Skills registry related commands.

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

* [chainctl](/chainguard/chainctl/chainctl-docs/chainctl/)	 - Chainguard Control
* [chainctl skills delete](/chainguard/chainctl/chainctl-docs/chainctl_skills_delete/)	 - Remove a published version of a skill.
* [chainctl skills describe](/chainguard/chainctl/chainctl-docs/chainctl_skills_describe/)	 - Show metadata for a published skill.
* [chainctl skills entitlements](/chainguard/chainctl/chainctl-docs/chainctl_skills_entitlements/)	 - Manage skills entitlements for an organization.
* [chainctl skills install](/chainguard/chainctl/chainctl-docs/chainctl_skills_install/)	 - Download a skill and install it into agent directories.
* [chainctl skills list](/chainguard/chainctl/chainctl-docs/chainctl_skills_list/)	 - List skills published by an org.
* [chainctl skills pull](/chainguard/chainctl/chainctl-docs/chainctl_skills_pull/)	 - Download a published skill to a local directory.
* [chainctl skills push](/chainguard/chainctl/chainctl-docs/chainctl_skills_push/)	 - Package a skill directory and publish it to skills.cgr.dev.
* [chainctl skills uninstall](/chainguard/chainctl/chainctl-docs/chainctl_skills_uninstall/)	 - Remove a skill from agent directories on the local machine.
* [chainctl skills validate](/chainguard/chainctl/chainctl-docs/chainctl_skills_validate/)	 - Check a skill directory for spec compliance without making network calls.
* [chainctl skills versions](/chainguard/chainctl/chainctl-docs/chainctl_skills_versions/)	 - List all published versions (tags) for a skill.

