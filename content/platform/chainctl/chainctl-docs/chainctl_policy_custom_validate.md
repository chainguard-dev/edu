---
date: 2026-09-04T19:05:48Z
title: "chainctl policy custom validate"
slug: chainctl_policy_custom_validate
url: /platform/chainctl/chainctl-docs/chainctl_policy_custom_validate/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policy custom validate

Validate a custom policy manifest or expression without persisting it.

### Synopsis

Validate a policy without creating it to catch problems.

Two modes are supported:

  --file: validates a full policy manifest (YAML). Expression and
  parameters are both checked.

  --expression: validates just a Rego expression (a raw .rego file).
  Useful during authoring for a fast parse + compile check. Pass
  --resource-type to say which resource types the expression is for; a
  manifest declares its own.

An expression is validated against the input document its resource type is
evaluated with, so the same expression can be valid for one type and read an
undefined field under another. A manifest naming several types is checked
against each, and a diagnostic that holds for only some of them names those.

Prints structured diagnostics on errors, indicating if the policy is
invalid. Expression errors include the line and column in the Rego
source; parameter-schema errors identify the offending field
(e.g. parameter_schemas[0].name).

Policy expressions must be declared under `package chainguard.policies` and
must define an `allow` rule; validation rejects a module that defines neither.

```
chainctl policy custom validate --file POLICY.yaml | --expression POLICY.rego [flags]
```

### Examples

```

# Check an existing policy layout for reference
chainctl policy describe --policy cooldown --parent example.com -o json

# Validate a manifest before creating the policy
chainctl policy custom validate --file policy.yaml

# Validate just the Rego expression
chainctl policy custom validate --expression policy.rego --resource-type registry.chainguard.dev/Repo@v1

# Validate an expression for several library ecosystems at once
chainctl policy custom validate --expression policy.rego \
  --resource-type libraries.chainguard.dev/NPMPackage@v1 \
  --resource-type libraries.chainguard.dev/PythonPackage@v1

```

### Options

```
  -e, --expression string           Path to a Rego expression (.rego) file. Validates the expression only; skips parameters.
  -f, --file string                 Path to a policy manifest YAML file.
      --resource-type stringArray   Resource type to validate the expression against (e.g. registry.chainguard.dev/Repo@v1). Required with --expression, repeat for several, and rejected with --file.
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

* [chainctl policy custom](/platform/chainctl/chainctl-docs/chainctl_policy_custom/)	 - Manage your custom policies.

