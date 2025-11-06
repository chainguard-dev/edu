---
date: 2025-11-04T19:15:55Z
title: "chainctl libraries inventory"
slug: chainctl_libraries_inventory
url: /chainguard/chainctl/chainctl-docs/chainctl_libraries_inventory/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries inventory

Generate artifact inventory from a repository

### Synopsis

Generate an artifact inventory from supported repositories.
The inventory contains package information in a format compatible with Chainguard source builders.

For Java artifacts, this includes GAV coordinates (groupId:artifactId:version).
For Python artifacts, this includes package name and version.

Supported repository types:
- JFrog Artifactory (jfrog:url)
- Cloudsmith (cloudsmith:org/repo)
- Generic remote repositories (remote:url)

Examples:
  # Generate Java inventory from JFrog
  chainver inventory --ecosystem java jfrog:example.jfrog.io/artifactory/maven-libs

  # Generate Python inventory from Cloudsmith
  chainver inventory --ecosystem python cloudsmith:myorg/python-repo

  # Generate inventory from Maven Central
  chainver inventory --ecosystem java remote:repo1.maven.org/maven2/org/apache/commons


```
chainctl libraries inventory [repository-url] [flags]
```

### Options

```
  -e, --ecosystem string   Ecosystem type (java, python)
  -h, --help               help for inventory
  -o, --output string      Output file path for inventory (default "inventory.json")
```

### Options inherited from parent commands

```
      --api string         The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string    The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string      A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string     The url of the Chainguard platform Console. (default "https://console.chainguard.dev")
      --force-color        Force color output even when stdout is not a TTY.
      --issuer string      The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
      --log-level string   Set the log level (debug, info) (default "ERROR")
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl libraries](/chainguard/chainctl/chainctl-docs/chainctl_libraries/)	 - Ecosystem library related commands.

