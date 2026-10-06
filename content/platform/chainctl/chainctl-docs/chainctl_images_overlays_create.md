---
date: 2026-10-06T09:26:34Z
title: "chainctl images overlays create"
slug: chainctl_images_overlays_create
url: /platform/chainctl/chainctl-docs/chainctl_images_overlays_create/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images overlays create

Create a Custom Assembly overlay.

### Synopsis

Create a Custom Assembly overlay under an organization or folder.

Pass the overlay configuration either as repeated --package flags, or as
a YAML file with --file in the same shape that "chainctl images repos
build apply" accepts. Certificates, runtime APK repositories, and
runtime APK signing keys can also be read from files with
--with-certificates, --with-runtime-repositories, and
--with-runtime-keys; they merge into the --package or --file
configuration. Creating an overlay does not change any image; attach it
to a repo with "chainctl images overlays attach".

```
chainctl images overlays create <NAME> [flags]
```

### Examples

```
  # Create an overlay from packages
  chainctl images overlays create my-overlay --parent my-org --package curl --package jq

  # Create an overlay from a configuration file
  chainctl images overlays create my-overlay --parent my-org -f overlay.yaml

  # Create an overlay carrying custom CA certificates from a PEM bundle
  chainctl images overlays create my-overlay --parent my-org --with-certificates ca-bundle.pem
```

### Options

```
  -f, --file chainctl images repos build    The name of the YAML file containing the overlay configuration, the same shape chainctl images repos build accepts. Takes precedence over --package.
      --package strings                     Package to include (repeatable).
      --parent string                       Parent group name or UIDP under which to create the overlay. Defaults to the default.group config value (env: CHAINGUARD_DEFAULT_GROUP).
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

