---
title: "Manage Your chainctl Configuration"
linktitle: "Manage Your chainctl Configuration"
aliases:
- /chainguard/chainguard-enforce/manage-chainctl-config/
- /chainguard/administration/manage-chainctl-config
type: "article"
date: 2023-07-07T05:56:52-07:00
lastmod: 2024-12-12T05:56:52-07:00
draft: false
tags: ["chainctl", "Product"]
images: []
menu:
  docs:
    parent: "administration"
toc: true
weight: 030
---

The Chainguard command line interface (CLI) tool, `chainctl`, will help you interact with the account model that Chainguard provides, and enable you to make queries into what's available to you on the Chainguard platform.

## chainctl config CLI

`chainctl` has a local configuration you can manage. To get a list of all options available, you can run:

```shell
chainctl config -h
```

You'll receive output like the following:

```
Local config file commands for chainctl.

Usage:
  chainctl config [command]

Available Commands:
  edit        Edit the current chainctl config file.
  reset       Remove local chainctl config files and restore defaults.
  save        Save the current chainctl config to a config file.
  set         Set an individual configuration value property.
  unset       Unset a configuration property and return it to default.
  validate    Run diagnostics on local config.
  view        View the current chainctl config.

Flags:
  -h, --help   help for config

Global Flags:
      --api string        The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string   The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string     A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string    The url of the Chainguard platform Console. (default "https://console.chainguard.dev")
      --issuer string     The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string     Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
  -v, --v int             Set the log verbosity level.

Use "chainctl config [command] --help" for more information about a command.
```

To view your current `chainctl` config, run:

```shell
chainctl config view
```

You'll receive output similar to this:

```shell
# Base Config file: /home/erika/.config/chainctl/config.yaml
auth:
    mode: browser
    device-flow: ""
default:
    active-within: 24h0m0s
    autoclose: true
    autoclose-timeout: "10"
    group: ""
    identity-provider: ""
    org-name: ""
    skip-auto-login: false
    skip-version-check: false
    social-login: google-oauth2
    use-refresh-token: true
output:
    color:
        fail: '#ff0000'
        pass: '#00ff00'
        warn: '#ffa500'
    silent: false
platform:
    api: https://console-api.enforce.dev
    audience: https://console-api.enforce.dev
    console: https://console.enforce.dev
    issuer: https://issuer.enforce.dev
    registry: https://cgr.dev
```

The full documentation for the `chainctl config` command is available on the relevant [reference page](/chainguard/chainctl/chainctl-docs/chainctl_config/).

## Edit the chainctl Configuration

You can edit the `chainctl` config directly with an editor. The following command will open your default command line text editor (typically `nano`) where you can edit the local `chainctl` config.

```shell
chainctl config edit
```

Alternatively, you can update one attribute at a time with the `set` option, as demonstrated in the next command:

```shell
chainctl config set platform.api=https://console-api.enforce.dev
```

You can review the `chainctl config set` options on the relevant [docs page](/chainguard/chainctl/chainctl-docs/chainctl_config_set/).

## Reset the Configuration

If you run into issues with your `chainctl` configuration, you can use the following command to reset it to the default state:

```shell
chainctl config reset
```

You can review all the available `chainctl` commands in our [`chainctl` reference documentation](/chainguard/chainctl/chainctl-docs/chainctl/).
