---
date: 2026-02-19T21:14:08Z
title: "chainctl libraries verify"
slug: chainctl_libraries_verify
url: /chainguard/chainctl/chainctl-docs/chainctl_libraries_verify/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl libraries verify

A tool to analyze the use of Chainguard Libraries in various artifacts

### Synopsis

verify analyzes various artifacts
(directories, archives, packages) to analyze how much was built from source by Chainguard,
based on SBOM data, signatures, and artifact inspection.

You can specify one or more paths to analyze multiple artifacts in a single command.

For container images, you can use:
  - Registry references (e.g., cgr.dev/chainguard/nginx:latest)
  - Local single-part images (e.g., redis:latest, nginx:alpine)
  - Docker archive format (docker-archive:/path/to/image.tar)
  - Local images with prefixes (localhost/myapp:latest)

```
chainctl libraries verify [path...] [flags]
```

### Examples

```
  # Analyze a local JAR file
  chainctl libraries verify myapp.jar

  # Analyze multiple files
  chainctl libraries verify build/libs/*.jar build/libs/*.war

  # Analyze a local Python virtual environment
  chainctl libraries verify ./venv/

  # Analyze with JSON output
  chainctl libraries verify -o json build/libs/*.jar

  # Analyze container images
  chainctl libraries verify cgr.dev/chainguard/maven:latest

  # Analyze remote artifact
  chainctl libraries verify remote:example.com/maven2/org/apache/commons/commons-lang3/3.12.0/commons-lang3-3.12.0.jar
```

### Options

```
  -d, --detailed                Show detailed per-artifact results
      --ecosystems-url string   URL for the Ecosystems Proxy (defaults to https://libraries.cgr.dev)
      --no-color                Disable colored output
  -o, --output string           Output format (text, json, yaml) (default "text")
      --parent string           Parent organization for authentication
      --verbose                 Enable verbose output
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
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl libraries](/chainguard/chainctl/chainctl-docs/chainctl_libraries/)	 - Ecosystem library related commands.

