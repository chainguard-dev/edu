---
date: 2026-11-12T21:48:09Z
title: "chainctl develop questions answer"
slug: chainctl_develop_questions_answer
url: /platform/chainctl/chainctl-docs/chainctl_develop_questions_answer/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl develop questions answer

Answer a question an agent asked.

### Synopsis

Answer an open question; the first answer closes it, and the agent waiting on it receives TEXT, marked as yours. Without a flag the answer is a reply and TEXT is required. --approve tells the agent to go ahead with what it proposed, with TEXT optional; --request-changes tells it to change what it proposed, and TEXT says how.

```
chainctl develop questions answer QUESTION [TEXT] [--approve | --request-changes] [--output=json]
```

### Examples

```
  # Reply to a question
  chainctl develop questions answer 3f2a9c1e "Use the staging bucket, not prod."

  # Approve what the agent proposed
  chainctl develop questions answer 3f2a9c1e --approve
```

### Options

```
      --approve           Approve what the agent proposed.
      --request-changes   Ask the agent to change what it proposed; TEXT says how.
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
      --non-interactive    Disable prompts; fail if a session or group choice is ambiguous.
  -o, --output string      Output format. One of: [csv, env, go-template, id, json, markdown, none, table, terse, tree, wide]
      --parent string      Organization or folder name/ID (defaults to $CHAINCTL_SANDBOX_GROUP, then default.group).
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl develop questions](/platform/chainctl/chainctl-docs/chainctl_develop_questions/)	 - List and answer the questions agents in your development sessions ask.

