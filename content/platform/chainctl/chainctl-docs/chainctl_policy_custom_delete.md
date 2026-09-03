---
date: 2026-09-02T22:28:18Z
title: "chainctl policy custom delete"
slug: chainctl_policy_custom_delete
url: /platform/chainctl/chainctl-docs/chainctl_policy_custom_delete/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl policy custom delete

Delete a custom policy.

### Synopsis

Delete a custom policy by name or UIDP. Use --force to skip the
confirmation prompt.

Deletion is permanent, once a policy is deleted it cannot be recovered.

Deletion cascades: every binding that referenced the policy is removed,
and every override waiving this policy is removed as well. It is
reported the number of bindings and overrides that will be affected
before you confirm.

If the target policy's name is not unique within the organization
(more than 1 policy can share a name when their resource types
differ), pass --resource-type to disambiguate. Ignored when --policy
is given by UIDP.

```
chainctl policy custom delete --policy NAME_OR_ID [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--force] [flags]
```

### Examples

```

# Delete a custom policy by name
chainctl policy custom delete --policy cooldown-30 --parent example.com

# Delete by UIDP, skipping confirmation
chainctl policy custom delete --policy 720a...c81 --force

# Disambiguate a policy name shared across resource types
chainctl policy custom delete --policy cooldown-30 --resource-type Python --parent example.com

```

### Options

```
      --force                  Skip the confirmation prompt.
      --parent string          The name or id of the organization the policy belongs to. Defaults to the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
      --policy string          The name or UIDP of the custom policy to delete.
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

* [chainctl policy custom](/platform/chainctl/chainctl-docs/chainctl_policy_custom/)	 - Manage your custom policies.

