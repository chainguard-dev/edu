---
date: 2026-06-30T00:00:55Z
title: "chainctl libraries policy create"
slug: chainctl_libraries_policy_create
url: /chainguard/chainctl/chainctl-docs/chainctl_libraries_policy_create/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries policy create

Create a custom Libraries policy.

### Synopsis

Create a CUSTOM Libraries policy for an organization.

A policy configures the gates applied when your organization pulls upstream
packages. Use --cooldown-days to quarantine newly published versions for N
days (0 disables the cooldown, 1-30 sets an explicit window, omit to inherit
the system default), --block to always deny a package, and --allow to let a
package bypass the cooldown and/or malware gates.

Packages are identified by their package URL (purl). The purl namespace
selects the ecosystem, so the same --block and --allow flags work for Python,
JavaScript, and Java:

```
Python (PyPI)      pkg:pypi/<name>
JavaScript (npm)   pkg:npm/<name>
                   pkg:npm/%40<scope>/<name>   (scoped packages)
Java (Maven)       pkg:maven/<group>/<artifact>
```

Append a version with @ to scope an entry to a single version (for example
pkg:npm/lodash@4.17.20); omit the version to match every version of the
package. --block and --allow are repeatable, so a single policy may list many
packages across ecosystems.

A newly created policy is inactive: activate it for an ecosystem with
"chainctl libraries policy enable".

```
chainctl libraries policy create --name NAME [--parent ORGANIZATION_NAME | ORGANIZATION_ID] [--cooldown-days N] [--block ...] [--allow ...] [flags]
```

### Examples

```
  # Block a specific package and apply a 14-day cooldown (Python / PyPI)
  chainctl libraries policy create --name=trusted --parent=example.com \
  --cooldown-days=14 --block=purl=pkg:pypi/evil
  
  # Block specific packages across ecosystems (repeat --block per package)
  chainctl libraries policy create --name=blocklist --parent=example.com \
  --block=purl=pkg:pypi/evil \
  --block=purl=pkg:npm/left-pad \
  --block=purl=pkg:maven/com.example/bad-lib
  
  # Block a single version, leaving other versions of the package allowed
  chainctl libraries policy create --name=pin --parent=example.com \
  --block=purl=pkg:npm/lodash@4.17.20
  
  # Allow a package to bypass the malware gate (justification required)
  chainctl libraries policy create --name=trusted --parent=example.com \
  --allow=purl=pkg:pypi/requests,bypass-malware=true,justification="vetted internally"
  
  # Allow a Java package to skip the cooldown window
  chainctl libraries policy create --name=trusted --parent=example.com \
  --allow=purl=pkg:maven/org.apache.commons/commons-lang3,bypass-cooldown=true
```

### Options

```
      --allow stringArray     A package permitted to bypass gates, as comma-separated key=value pairs: purl=<package-url>[,bypass-cooldown=true][,bypass-malware=true][,justification="..."]. justification is required with bypass-malware. Repeatable.
      --block stringArray     A package to always deny, as purl=<package-url>. The purl namespace selects the ecosystem (pkg:pypi/<name>, pkg:npm/<name>, pkg:maven/<group>/<artifact>); append @<version> to block a single version. Repeatable.
      --cooldown-days int32   The cooldown window in days (0 disables, 1-30 explicit, omit to inherit the default). (default -1)
      --description string    The description of the policy.
      --name string           The name of the policy.
      --parent string         The name or id of the organization to scope the policy to.
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

* [chainctl libraries policy](/chainguard/chainctl/chainctl-docs/chainctl_libraries_policy/)	 - Manage Libraries policies.

