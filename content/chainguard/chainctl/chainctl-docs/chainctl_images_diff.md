---
date: 2025-04-03T19:10:23Z
title: "chainctl images diff"
slug: chainctl_images_diff
url: /chainguard/chainctl/chainctl-docs/chainctl_images_diff/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images diff

Diff images.

### Synopsis

Diffs 2 images together, based on their SBOM and Vulnerability scan.

SBOM packages are diffed based on their PURL (https://github.com/package-url/purl-spec) and version.
PURLs are grouped without their @version component. If identical PURLs are found, the first one found is used.
If an SBOM package contains multiple PURLs, results will contain multiple entries for the same package name based on the purl type.

Vulnerability scans are done via grype, which must be available on the system PATH.


```
chainctl images diff FROM_IMAGE TO_IMAGE [flags]
```

### Options

```
  -t, --artifact-types strings   Specifies the purl artifact types to diff. If "-" is provided, all types are included. (default [apk])
  -h, --help                     help for diff
      --platform string          Specifies the platform in the form os/arch (e.g. linux/amd64, linux/arm64) (default "linux/amd64")
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
  -o, --output string      Output format. One of: [csv, id, json, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl images](/chainguard/chainctl/chainctl-docs/chainctl_images/)	 - Images related commands for the Chainguard platform.

