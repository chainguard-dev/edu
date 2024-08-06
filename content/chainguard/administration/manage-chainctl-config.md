---
title: "How to Manage chainctl Configuration"
linktitle: "chainctl Config"
aliases: 
- /chainguard/chainguard-enforce/manage-chainctl-config/
type: "article"
date: 2023-07-07T05:56:52-07:00
lastmod: 2023-12-07T05:56:52-07:00
draft: false
tags: ["chainctl", "Product"]
images: []
menu:
  docs:
    parent: "administration"
toc: true
weight: 006
---

The Chainguard command line interface (CLI) tool, `chainctl`, will help you interact with the account model that Chainguard provides, and enable you to make queries into what's available to you on the Chainguard platform.

## chainctl config CLI 

`chainctl` has a config you can manage, `chainctl config -h` will show you all the options. 

```sh
chainctl config -h
```

You'll receive output like the following.

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

The default `chainctl` config is similar to the following.

```
Base Config file: none
default:
    active-within: 24h0m0s
output:
    color:
      fail: '#ff0000'
      pass: '#00ff00'
      warn: '#ffa500'
    records:
      notable: []
platform:
    api: https://console-api.enforce.dev
    audience: https://console-api.enforce.dev
    console: https://console.enforce.dev
    issuer: https://issuer.enforce.dev
    registry: https://cgr.dev
    timestamp-authority: https://tsa.enforce.dev
```

The full documentation for the `chainctl config` command is available on the relevant [reference page](/chainguard/chainctl/chainctl-docs/chainctl_config/).
 
## Edit chainctl config

You can edit the `chainctl` config directly with an editor. The following command will open a text editor (nano, by default) where you can edit the local `chainctl` config. 

```sh
chainctl config edit
```

Alternatively, you can update one attribute at a time with the `set` option, as demonstrated in the next command. 

```sh
chainctl config set platform.api=https://console-api.enforce.dev
```

You can review the `chainctl config set` options on the relevant [docs page](/chainguard/chainctl/chainctl-docs/chainctl_config_set/).

## Reset the configuration

If you run into issues with your `chainctl` configuration, you can use the below command to reset it to the default state.

```sh
chainctl config reset
```
 
You can review all the available `chainctl` commands on our [`chainctl` reference documentation](/chainguard/chainctl/chainctl-docs/chainctl/).