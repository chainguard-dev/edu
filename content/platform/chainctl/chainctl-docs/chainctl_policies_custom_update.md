---
date: 2026-08-11T17:12:41Z
title: "chainctl policies custom update"
slug: chainctl_policies_custom_update
url: /platform/chainctl/chainctl-docs/chainctl_policies_custom_update/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policies custom update

Update a custom policy.

### Synopsis

Update a custom policy in one of two modes:

  --file: full replacement from a YAML manifest. The manifest supplants
  the entire policy definition. The resulting policy is exactly what
  the manifest declares (name, description, expression,
  supported_resource_type, and parameters).

  Flag mode: partial update via individual flags. Only the fields you
  pass are changed; everything else is preserved. Flag mode is
  restricted to policies that do NOT declare parameter schemas. For
  parameterized policies, use --file.

The supported resource type is immutable. A --file update whose
manifest declares a different resource type than the current policy is
rejected.

If the target policy's name is not unique within the organization
(more than 1 policy can share a name when their resource types
differ), pass --resource-type to disambiguate. Ignored when --policy
is given by UIDP.

See `chainctl policies custom create --help` for the manifest fields and the
required Rego package and `allow` rule.

```
chainctl policies custom update --policy NAME_OR_ID --file POLICY.yaml | [--name NAME] [--description DESC] [--expression FILE.rego] [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--output=json|table] [flags]
```

### Examples

```

# Full replacement from a manifest
chainctl policies custom update --policy cooldown-30 --file policy.yaml --parent example.com

# Rename only
chainctl policies custom update --policy cooldown-30 --name cooldown-strict --parent example.com

# Change just the description
chainctl policies custom update --policy cooldown-30 --description "block pulls from images newer than 30 days"

# Replace the expression from a new .rego (parameterless policies only)
chainctl policies custom update --policy cooldown-30 --expression new-cooldown.rego

# Disambiguate a policy name shared across resource types
chainctl policies custom update --policy cooldown-30 --resource-type Python --description "python-only variant"

```

### Options

```
      --description string     New description. Flag mode only; mutually exclusive with --file.
  -e, --expression string      Path to a new Rego expression (.rego) file. Flag mode only; mutually exclusive with --file.
  -f, --file string            Path to a policy manifest YAML file. Full replacement — supplants the entire policy definition.
      --name string            New policy name. Flag mode only; mutually exclusive with --file.
      --parent string          The name or id of the organization the policy belongs to.
      --policy string          The name or UIDP of the custom policy to update.
      --resource-type string   Resource type used to disambiguate a policy referenced by name (shorthand: Repo, Python, Java, Javascript; or a full type). Ignored when the policy is given by UIDP.
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

