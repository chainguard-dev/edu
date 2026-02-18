---
date: 2026-02-17T20:03:25Z
title: "chainctl images advisories list"
slug: chainctl_images_advisories_list
url: /chainguard/chainctl/chainctl-docs/chainctl_images_advisories_list/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images advisories list

List security advisories for packages in an image.

### Synopsis

List security advisories for APK packages in a container image.

This command fetches the SBOM attestation from the image registry,
extracts the list of APK packages, and queries the Chainguard advisory
database for each package.

The image reference can be any valid OCI image reference that has
SBOM attestations attached.

```
chainctl images advisories list {IMAGE_REF} [--platform=PLATFORM] [--status=STATUS,...]
```

### Examples

```
  # List advisories for a Chainguard image
  chainctl images advisories list cgr.dev/chainguard/nginx:latest

  # List advisories for a specific platform
  chainctl images advisories list cgr.dev/chainguard/python:latest --platform=linux/arm64

  # Filter by status (e.g., only show detected vulnerabilities)
  chainctl images advisories list cgr.dev/chainguard/go:latest --status=detected

  # Filter by multiple statuses (comma-separated or multiple flags)
  chainctl images advisories list cgr.dev/chainguard/go:latest --status=detected,pending-upstream
  chainctl images advisories list cgr.dev/chainguard/go:latest --status=detected --status=pending-upstream

  # Output as JSON
  chainctl images advisories list cgr.dev/chainguard/go:latest -o json
```

### Options

```
      --platform string   Platform to fetch SBOM for (e.g., linux/amd64, linux/arm64) (default "linux/amd64")
      --status strings    Filter advisories by status; can be specified multiple times or comma-separated (e.g., --status=detected,pending-upstream)
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

* [chainctl images advisories](/chainguard/chainctl/chainctl-docs/chainctl_images_advisories/)	 - Security advisory commands for images.

