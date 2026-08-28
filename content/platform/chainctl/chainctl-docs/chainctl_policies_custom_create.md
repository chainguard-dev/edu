---
date: 2026-08-27T20:49:25Z
title: "chainctl policies custom create"
slug: chainctl_policies_custom_create
url: /platform/chainctl/chainctl-docs/chainctl_policies_custom_create/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies custom create

Create a custom policy.

### Synopsis

Create a custom policy from a YAML manifest, or from a raw Rego
expression as a shortcut for parameterless policies.

Two modes are supported:

  --file: creates a policy from a full YAML manifest (name, description,
  expression, supported_resource_type, and optional parameters). Use
  this when your policy declares parameters.

  --expression: creates a parameterless policy directly from a raw .rego
  file. --name and --resource-type are required in this mode;
  --description is optional. Policies with parameters must be authored as
  a manifest and passed via --file.

Policy expressions must be declared under `package chainguard.policies` and
must define an `allow` rule (start from `default allow := false` and
add an `allow if { ... }` block); validation rejects a module defining neither.

A minimal manifest looks like:

```yaml
name: my-policy
description: What this policy enforces.
supported_resource_type: registry.chainguard.dev/Repo@v1
expression_type: EXPRESSION_TYPE_REGO
parameters:                       # optional; omit for parameterless policies
  - name: days
    type: PARAMETER_TYPE_INTEGER  # STRING | INTEGER | BOOLEAN | STRING_LIST
    description: Minimum age in days.
    default: 7
    minimum: 1
    maximum: 365
expression: |
  package chainguard.policies
  import rego.v1

  default allow := false

  allow if {
    # replace with your real conditions
    input.parameters.days >= 1
  }
```

Each parameter accepts: name, type (a PARAMETER_TYPE_* value), description,
default, minimum, maximum, allowed_values, required, deprecated.

--resource-type accepts a shorthand (Repo, Java, Javascript, Python) or a
full type:
  - Repo       -> registry.chainguard.dev/Repo@v1
  - Java       -> libraries.chainguard.dev/JavaPackage@v1
  - Javascript -> libraries.chainguard.dev/NPMPackage@v1
  - Python     -> libraries.chainguard.dev/PythonPackage@v1

The resource type is set at create time and cannot be changed later.
Within an organization, (name, resource type) is unique. The same name
may be reused across different resource types.

For an authoritative live example, inspect a system policy with
`chainctl policies describe --policy <name> -o json`.

```
chainctl policies custom create --file POLICY.yaml | --expression POLICY.rego --name NAME --resource-type TYPE [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--output=json|table] [flags]
```

### Examples

```

# Create a custom policy from a full manifest
chainctl policies custom create --file policy.yaml --parent example.com

# Create a parameterless policy from a raw Rego expression
chainctl policies custom create --expression allow.rego --name allow-all \
  --resource-type Repo --parent example.com

```

### Options

```
      --description string     Human-readable description of the policy. Only valid with --expression.
  -e, --expression string      Path to a Rego expression (.rego) file. Shortcut for parameterless policies; requires --name and --resource-type.
  -f, --file string            Path to a policy manifest YAML file.
      --name string            Policy name. Required with --expression.
      --parent string          The name or id of the organization to create the policy under. Defaults to the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
      --resource-type string   The resource type the policy applies to (shorthand: Repo, Python, Java, Javascript; or a full type). Required with --expression.
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

* [chainctl policies custom](/platform/chainctl/chainctl-docs/chainctl_policies_custom/)	 - Manage your custom policies.

