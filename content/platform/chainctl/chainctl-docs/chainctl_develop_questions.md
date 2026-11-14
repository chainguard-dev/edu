---
date: 2026-11-13T20:36:51Z
title: "chainctl develop questions"
slug: chainctl_develop_questions
url: /platform/chainctl/chainctl-docs/chainctl_develop_questions/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl develop questions

List and answer the questions agents in your development sessions ask.

### Synopsis

An agent working in one of your sessions asks you a question with its ask tool, and waits for the answer. List the open ones, read one in full, then answer or dismiss it; the agent's waiting call returns what you said. A question is named by the short id the list prints. Only you, with your own login, can answer a question about your session: the agent's own credential, inside the session, is refused.

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

* [chainctl develop](/platform/chainctl/chainctl-docs/chainctl_develop/)	 - Open or resume a cloud development session.
* [chainctl develop questions answer](/platform/chainctl/chainctl-docs/chainctl_develop_questions_answer/)	 - Answer a question an agent asked.
* [chainctl develop questions describe](/platform/chainctl/chainctl-docs/chainctl_develop_questions_describe/)	 - Show a question in full.
* [chainctl develop questions dismiss](/platform/chainctl/chainctl-docs/chainctl_develop_questions_dismiss/)	 - Close a question without answering it.
* [chainctl develop questions list](/platform/chainctl/chainctl-docs/chainctl_develop_questions_list/)	 - List the open questions about your sessions.

