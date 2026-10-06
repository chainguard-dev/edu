---
date: 2026-10-06T09:26:34Z
title: "chainctl images overlays update"
slug: chainctl_images_overlays_update
url: /platform/chainctl/chainctl-docs/chainctl_images_overlays_update/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images overlays update

Update a Custom Assembly overlay's name or configuration.

### Synopsis

Update a Custom Assembly overlay's name, configuration, or both.

--package and --file replace the stored configuration wholesale; they do
not merge with it. The --with-* flags merge into that replacement when
--package or --file is also given; passed alone, they merge into the
stored configuration instead, as "chainctl images repos build edit"
merges them into a repo's current build config. Repos the overlay is
attached to are rebuilt with the new configuration. An update that would
conflict with another overlay attached to the same tags is rejected.

```
chainctl images overlays update <UID|NAME> [flags]
```

### Examples

```
  # Rename an overlay
  chainctl images overlays update my-overlay --name my-renamed-overlay

  # Replace an overlay's configuration from a file
  chainctl images overlays update my-overlay -f overlay.yaml

  # Add custom CA certificates to an overlay's stored configuration
  chainctl images overlays update my-overlay --with-certificates ca-bundle.pem
```

### Options

```
  -f, --file chainctl images repos build    The name of the YAML file containing the overlay configuration, the same shape chainctl images repos build accepts. Replaces the stored config wholesale and takes precedence over --package.
      --name string                         New overlay name.
      --package strings                     Package to include (repeatable). Declares the FULL replacement set; the stored config is replaced wholesale.
      --with-certificates strings           Comma separated list of files to read the custom certificates from.
      --with-runtime-keys strings           Comma separated list of files to read customer APK signing public keys from. Each file becomes a key in /etc/apk/keys named after the file's basename, which must match the filename referenced by the repository's APKINDEX signature (.SIGN.RSA256.<name>).
      --with-runtime-repositories strings   Comma separated list of runtime APK repository URLs to write to /etc/apk/repositories in the image.
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

* [chainctl images overlays](/platform/chainctl/chainctl-docs/chainctl_images_overlays/)	 - Manage Custom Assembly overlays and the repos they are attached to.

