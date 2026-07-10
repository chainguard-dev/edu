---
title: "Manage Your chainctl configuration"
linktitle: "Manage Your chainctl configuration"
aliases:
- /chainguard/chainctl-usage/manage-chainctl-config/
- /chainguard/chainguard-enforce/manage-chainctl-config/
- /chainguard/administration/manage-chainctl-config
type: "article"
date: 2023-07-07T05:56:52-07:00
lastmod: 2026-07-07T00:00:00+00:00
draft: false
tags: ["chainctl"]
images: []
menu:
  docs:
    parent: "administration"
toc: true
weight: 030
---

Chainguard's `chainctl` keeps a local configuration file that controls how the CLI behaves: which Chainguard environment it talks to, how it logs you in, the defaults it applies when you omit an argument, and how it formats output. This page explains the commands that manage that file, where it lives, and every setting you can configure.

## chainctl config commands

`chainctl config` groups the commands that read and write the local configuration file. To list them, run:

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

Each command is covered below. The full command reference is available on the [`chainctl config` reference page](/chainguard/chainctl/chainctl-docs/chainctl_config/).

## View your current configuration

To print the configuration chainctl is currently using, run:

```shell
chainctl config view
```

You'll receive output similar to this:

```output
# Base Config file: /home/erika/.config/chainctl/config.yaml
auth:
    mode: browser
default:
    active-within: 24h0m0s
    autoclose: true
    autoclose-timeout: "10"
    group: ""
    log-level: ""
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
        info: ""
        highlight: ""
        secondary: ""
        special: ""
    silent: false
platform:
    api: https://console-api.enforce.dev
    audience: https://console-api.enforce.dev
    console: https://console.chainguard.dev
    issuer: https://issuer.enforce.dev
    registry: https://cgr.dev
```

`view` prints the effective values after defaults, the file, and any environment variables are combined. If you have `CHAINGUARD*` environment variables set, they are listed below the file contents. Add `--diff` to compare the effective configuration against what is written on disk.

## Where your configuration lives

chainctl looks for a configuration file in three locations and uses the first one it finds:

1. `./chainctl/config.yaml` (relative to your current directory)
2. `<config-dir>/chainctl/config.yaml`
3. `~/.chainguard/config.yaml`

`<config-dir>` is your operating system's user configuration directory: `~/Library/Application Support` on macOS, and `$XDG_CONFIG_HOME` (usually `~/.config`) on Linux. Passing `--config FILE` (or setting the `CHAINCTL_CONFIG` environment variable) points chainctl at a specific file and bypasses this search. When chainctl writes a file itself (for example with `save` or `edit`), it uses `<config-dir>/chainctl/config.yaml`.

## Edit the chainctl configuration

Settings are resolved in order of precedence, where a higher source overrides a lower one:

```
┌──────────────────────┐
│ command-line flags   │  highest
└──────────┬───────────┘
           │
┌──────────▼───────────┐
│ CHAINGUARD_ env vars │
└──────────┬───────────┘
           │
┌──────────▼───────────┐
│ config file          │
└──────────┬───────────┘
           │
┌──────────▼───────────┐
│ built-in defaults    │  lowest
└──────────────────────┘
```

## Override settings with environment variables

Any setting can be overridden with an environment variable without editing the file. Prefix the property name with `CHAINGUARD_`, uppercase it, and replace the dots with underscores:

```shell
export CHAINGUARD_PLATFORM_API=https://console-api.enforce.dev
export CHAINGUARD_DEFAULT_GROUP=<group-id>
export CHAINGUARD_OUTPUT_SILENT=true
```

Environment variables take precedence over the file, so they are useful for CI jobs or for temporarily targeting a different environment.

## Configurable properties

Properties are addressed with dot-delimited, lowercase names (for example `output.color.pass`) and fall into four groups. The tables below list every property, its default, and what it does.

### Platform endpoints

The `platform` keys tell chainctl which Chainguard environment to use. The defaults target Chainguard's production environment, so you normally only change these when working against a different environment. Each value must be a valid URL; an invalid value is discarded and the default is restored.

| Property | Default | Description |
|---|---|---|
| `platform.api` | `https://console-api.enforce.dev` | Chainguard platform API endpoint. |
| `platform.console` | `https://console.chainguard.dev` | Chainguard Console URL. |
| `platform.issuer` | `https://issuer.enforce.dev` | Token issuer (STS) endpoint used at login. |
| `platform.registry` | `https://cgr.dev` | Registry endpoint. |
| `platform.audience` | same as `platform.api` | Token audience requested at login. |

### Authentication

The `auth` key controls the login flow.

| Property | Default | Description |
|---|---|---|
| `auth.mode` | `browser` | Login flow. One of `browser` (opens a browser) or `headless` (for environments without one). |

### Defaults

The `default` keys supply values chainctl uses when a command needs one and you do not pass it explicitly.

| Property | Default | Description |
|---|---|---|
| `default.group` | (empty) | Group or folder ID used as the parent when a command needs one and you do not specify it. |
| `default.org-name` | (empty) | Organization name to log in to. |
| `default.social-login` | (empty) | Default social login provider. One of `email`, `github`, `gitlab`, or `google`. |
| `default.identity-provider` | (empty) | ID of a custom identity provider to authenticate through. Using it to select a social provider is deprecated; use `default.social-login` instead. |
| `default.active-within` | `24h` | Default time window for commands that filter by recent activity (the `--active-within` flag). Must be a positive duration. |
| `default.autoclose` | `true` | Whether the browser "login successful" page closes itself. |
| `default.autoclose-timeout` | `10` | Seconds before the login-success page closes. |
| `default.use-refresh-token` | `true` | Whether login stores a refresh token so you are prompted to re-authenticate less often. |
| `default.skip-auto-login` | `false` | When `true`, chainctl does not start a login flow automatically. |
| `default.skip-version-check` | `false` | Skip the check for a newer chainctl release. |
| `default.log-level` | (empty) | Log verbosity for chainctl. |

### Output

The `output` keys control console output and coloring.

| Property | Default | Description |
|---|---|---|
| `output.silent` | `false` | Suppress informational messages (printed to standard error). |
| `output.color.pass` | (empty) | Color for success text. |
| `output.color.fail` | (empty) | Color for failure text. |
| `output.color.warn` | (empty) | Color for warnings. |
| `output.color.info` | (empty) | Color for informational text. |
| `output.color.highlight` | (empty) | Highlight color. |
| `output.color.secondary` | (empty) | Secondary text color. |
| `output.color.special` | (empty) | Special-case color. |

Color values accept a hex code such as `#00ff00` or a CSS color name such as `green`. Regardless of these settings, chainctl disables color when the `NO_COLOR` environment variable is set, when output is piped or redirected (not a terminal), or when `TERM=dumb`.

## Change a setting

You can edit the configuration file directly in an editor. The following command opens it in your default command-line text editor (typically `nano`; set the `EDITOR` environment variable to choose another), then prompts you to save your changes:

```shell
chainctl config edit
```

To change a single property instead, use `set` with the property name and value as two separate arguments:

```shell
chainctl config set platform.api https://console-api.enforce.dev
```

To return a property to its default, use `unset`:

```shell
chainctl config unset output.color.pass
```

Both `set` and `unset` write to the configuration file immediately. See the [`chainctl config set` reference page](/chainguard/chainctl/chainctl-docs/chainctl_config_set/) for more detail.

## Save a configuration file

If you do not have a configuration file yet, `save` writes the current effective configuration (defaults plus any overrides) to disk so you have a file to edit:

```shell
chainctl config save
```

Without `--config`, it writes to the default location, `<config-dir>/chainctl/config.yaml`.

## Validate your configuration

`validate` runs connectivity diagnostics rather than checking the file's contents. It confirms that the platform and required supporting domains resolve, and tests that the API and issuer endpoints are reachable:

```shell
chainctl config validate
```

Use it to diagnose networking or endpoint problems, for example when login fails behind a proxy or firewall.

## Reset your configuration

If you run into issues with your configuration, reset it to the default state:

```shell
chainctl config reset
```

This deletes the configuration files chainctl manages in the default locations and restores default values. Files you passed explicitly with `--config` are not deleted. You can review all available commands in the [`chainctl` reference documentation](/chainguard/chainctl/chainctl-docs/chainctl/).
