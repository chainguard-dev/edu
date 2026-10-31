---
date: 2026-10-30T14:11:50Z
title: "chainctl checks migrate"
slug: chainctl_checks_migrate
url: /platform/chainctl/chainctl-docs/chainctl_checks_migrate/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl checks migrate

Draft a .chainguard/ci/migrated.yaml from a repository's GitHub Actions presubmits and prove it on the sandbox plane.

### Synopsis

Draft a .chainguard/ci/migrated.yaml from the GitHub Actions presubmits of a local git checkout (the current one by default), prove it by running it on the sandbox plane, and print the PR body.

Every workflow triggered on pull_request is read and mapped into one authored document (version: 1 and checks:). The migrator never guesses: each construct the schema cannot express is flagged in the ledger and commented at its site in the file, never approximated or silently dropped; constructs with no meaning on the target are listed once as ignored.

The proof runs the document against the checkout's HEAD (or --ref) under the sandbox instance, adopts any egress allowlist the plane drafts and proves again, and stops green or blocked. chainctl carries no repair agent: a red job the mechanics cannot fix blocks the run with the tail of its log, and repair needs the hosted migrator (`go run ./cmd/migrator` in ai-cicd/sandbox). The PR is likewise opened by the hosted migrator, as its GitHub App (`go run ./cmd/migrator pr`); chainctl has no flag for it.

The output uses .chainguard/ci/migrated.yaml so each check can retain its own environment. Do not combine it with the single-file .chainguard/ci.yaml layout.

Pass --dry to print the document and the ledger and run nothing. Dry output is hermetic until a proof run records the egress allowlist. With --output json the document, the ledger, the proof per job, and the block (if any) are printed as one object.

```
chainctl checks migrate [PATH|.] [--dry] [--ref SHA] [--max-proves N] [--parity N] [--sandbox-url URL] [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--output=json]
```

### Examples

```
  # Prove this checkout's presubmits on the sandbox plane and print the PR body
  chainctl checks migrate --parent my-org

  # Draft the document and ledger for this checkout without running anything
  chainctl checks migrate --dry

  # Prove another checkout at a given commit, as JSON
  chainctl checks migrate ~/src/repo --ref 0123456789abcdef0123456789abcdef01234567 -o json

  # Write only the document to the file it belongs in
  mkdir -p .chainguard/ci
  chainctl checks migrate --dry -o json | jq -r .document > .chainguard/ci/migrated.yaml
```

### Options

```
      --dry                  Draft .chainguard/ci.yaml and the ledger from the checkout and print them; prove nothing and open no PR.
      --max-proves int       Most proof runs to submit; every re-prove after a refusal or an egress draft counts (0 = the loop's default).
      --parent string        The organization or folder (name or ID) the proof runs are created under. Defaults to $CHAINCTL_SANDBOX_GROUP, then the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
      --parity int           After a green proof, replay the document against the heads of the last N merged pull requests (the second parents of the checkout's merge commits; a squash-merging repository yields none) and report each job's outcome beside the GitHub conclusion. chainctl has no GitHub client, so every recorded conclusion is unknown here; the hosted migrator reads them (cmd/migrator prove --parity).
      --ref string           Full commit SHA the proof runs execute. Defaults to the checkout's HEAD.
      --sandbox-url string   URL of the sandbox control plane serving the WorkflowRuns API. Overridden by $CHAINCTL_WORKFLOWRUNS_URL. (default "https://workflowruns.chainbox.dev")
      --token string         Bearer token for the sandbox host. Overrides $CHAINCTL_AUTH_TOKEN and the chainctl session. Prefer passing it via the environment to keep it out of shell history.
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

