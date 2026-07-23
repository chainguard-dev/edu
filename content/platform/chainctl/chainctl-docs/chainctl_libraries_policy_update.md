---
date: 2026-07-22T19:49:10Z
title: "chainctl libraries policy update"
slug: chainctl_libraries_policy_update
url: /platform/chainctl/chainctl-docs/chainctl_libraries_policy_update/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries policy update

Update a custom Libraries policy.

### Synopsis

Update a CUSTOM Libraries policy for an organization.

By default --block, --allow, and --blocked-license ADD to the policy's
existing lists: a new --block purl or --blocked-license identifier is appended
(duplicates are ignored) and a new --allow purl replaces any existing allow
entry for the same purl. Use --remove-block, --remove-allow, and
--remove-blocked-license to drop entries, or --replace-block, --replace-allow,
and --replace-blocked-licenses to replace an entire list with the flag's
entries (pass a replace flag with no entries to clear that list).

Packages are identified by their package URL (purl); see
"chainctl libraries policy create --help" for the supported purl formats and
the blocked-license matching semantics.

```
chainctl libraries policy update POLICY [--cooldown-days N] [--block ...] [--allow ...] [--blocked-license ...] [--remove-block ...] [--remove-allow ...] [--remove-blocked-license ...] [--replace-block] [--replace-allow] [--replace-blocked-licenses] [flags]
```

### Examples

```
  # Add a package to the existing block list (other entries are kept)
  chainctl libraries policy update trusted --parent=example.com \
  --block=purl=pkg:pypi/evil
  
  # Add or update an allow-list override for a package
  chainctl libraries policy update trusted --parent=example.com \
  --allow=purl=pkg:npm/left-pad,override-cooldown=true
  
  # Remove entries from the block and allow lists by purl
  chainctl libraries policy update trusted --parent=example.com \
  --remove-block=pkg:pypi/evil \
  --remove-allow=pkg:npm/left-pad
  
  # Replace the entire block list, discarding the previous entries
  chainctl libraries policy update trusted --parent=example.com \
  --replace-block --block=purl=pkg:pypi/only-this
  
  # Clear the allow list entirely
  chainctl libraries policy update trusted --parent=example.com --replace-allow
  
  # Add a license to the blocked-licenses list (existing entries are kept)
  chainctl libraries policy update no-copyleft --parent=example.com \
  --blocked-license=SSPL-1.0
  
  # Remove a license from the blocked-licenses list
  chainctl libraries policy update no-copyleft --parent=example.com \
  --remove-blocked-license=GPL-3.0
  
  # Clear the blocked-licenses list entirely
  chainctl libraries policy update no-copyleft --parent=example.com \
  --replace-blocked-licenses
```

### Options

```
      --allow stringArray                    A package permitted to override gates, as comma-separated key=value pairs: purl=<package-url>[,override-cooldown=true][,override-malware=true][,justification="..."]. Added to the existing allow list, replacing any existing entry for the same purl (use --replace-allow to replace the whole list instead). Repeatable.
      --block stringArray                    A package to always deny, as purl=<package-url> (pkg:pypi/<name>, pkg:npm/<name>, pkg:maven/<group>/<artifact>); append @<version> to block a single version. Added to the existing block list (use --replace-block to replace it instead). Repeatable.
      --blocked-license stringArray          An SPDX license identifier to add to the blocked-licenses list (e.g. GPL-3.0). Added to the existing list (use --replace-blocked-licenses to replace it instead). Repeatable.
      --cooldown-days int32                  The cooldown window in days (0 disables, 1-30 explicit, omit to inherit the default). (default -1)
      --description string                   The updated description of the policy.
      --parent string                        The name or id of the organization that owns the policy.
      --remove-allow stringArray             A package to remove from the allow list, as a purl or purl=<package-url> (match the purl shown by 'describe'). Repeatable.
      --remove-block stringArray             A package to remove from the block list, as a purl or purl=<package-url> (match the purl shown by 'describe'). Repeatable.
      --remove-blocked-license stringArray   An SPDX license identifier to remove from the blocked-licenses list (case-insensitive). Repeatable.
      --replace-allow                        Replace the entire allow list with the --allow entries instead of adding to it; pass with no --allow to clear the allow list.
      --replace-block                        Replace the entire block list with the --block entries instead of adding to it; pass with no --block to clear the block list.
      --replace-blocked-licenses             Replace the entire blocked-licenses list with the --blocked-license entries instead of adding to it; pass with no --blocked-license to clear the list.
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

* [chainctl libraries policy](/platform/chainctl/chainctl-docs/chainctl_libraries_policy/)	 - Manage Libraries policies.

