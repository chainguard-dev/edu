---
date: 2026-11-27T13:55:02Z
title: "chainctl libraries storage delete"
slug: chainctl_libraries_storage_delete
url: /platform/chainctl/chainctl-docs/chainctl_libraries_storage_delete/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries storage delete

Delete a version your organization uploaded to Libraries.

### Synopsis

Delete one version that your organization uploaded to Chainguard Libraries,
with all of its files. Chainguard-built and mirrored upstream artifacts cannot
be deleted.

The version stays reserved: a later upload of the same version is refused, so
the same version can never point at different files. A version whose upload
never completed is not reserved.

ECOSYSTEM is one of go, java, python, javascript or dotnet. NAME is the
package name as the ecosystem spells it: groupId:artifactId for Java, the npm
name (with its @scope/ if any), the Python project name, the Go module path or
the NuGet package ID. The server stores the name and version in a normal form
(for example, Python 1.0.0 becomes 1), and the command prints that form as the
ecosystem's clients spell it.

Deleting needs the ecosystem's delete capability, for example
libraries.javascript.delete, bound at the organization itself. The built-in
owner role holds it for every ecosystem.

```
chainctl libraries storage delete ECOSYSTEM NAME VERSION [--parent ORG] [--yes] [--output=json|table] [flags]
```

### Examples

```
  # Delete version 1.2.3 of the npm package @acme/widget from example.com
  chainctl libraries storage delete javascript @acme/widget 1.2.3 --parent=example.com
  
  # Delete a Java version without asking to confirm
  chainctl libraries storage delete java com.example:app 1.0 --parent=example.com --yes
```

### Options

```
      --parent string   Name or UIDP of the organization that uploaded the version.
  -y, --yes             Delete without asking to confirm.
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

* [chainctl libraries storage](/platform/chainctl/chainctl-docs/chainctl_libraries_storage/)	 - Show and delete your organization's uploads in Libraries.

