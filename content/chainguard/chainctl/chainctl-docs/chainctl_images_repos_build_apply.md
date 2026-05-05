---
date: 2026-05-04T16:59:58Z
title: "chainctl images repos build apply"
slug: chainctl_images_repos_build_apply
url: /chainguard/chainctl/chainctl-docs/chainctl_images_repos_build_apply/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images repos build apply

Apply a build config

### Synopsis


Apply a pre-written YAML configuration file and/or custom certificates to customize one or more Chainguard images.

You can use Custom Assembly to customize any image you are entitled to by
adding packages from Chainguard's repository, setting environment variables,
adding OCI annotations, customizing user accounts and groups, or including
custom certificates. The customized image is built automatically without
requiring you to fork images or maintain custom build pipelines.

This command applies Custom Assembly configurations without opening an interactive
editor. Use this for automated workflows, CI/CD pipelines, or when you have
configuration files managed in version control.

You can create variants by choosing to save the customized configuration as a
new repository instead of modifying the existing one (single-repo only).

How it works:

You can customize the image by providing configuration through a YAML file,
certificates, or both.

At least one of --file or --with-certificates must be provided. When --file is
used alone, the YAML configuration from the file is applied as-is. When
--with-certificates is used alone, only the certificates will be applied to
the image. When both flags are provided, the certificates are merged with the
configuration from the file.

The command validates the resulting configuration and displays a diff comparing
it to the current repository configuration (or an empty baseline for new
repositories). After reviewing the diff, you confirm the changes. The command
then updates the repository configuration and starts a custom build automatically.

Batch mode:

Apply the same config to multiple repos by passing --repo multiple times, or by using a wildcard pattern. Supported syntax: * matches any string, ? matches a single character, [abc] matches a character class:

  - --repo=nginx --repo=redis   Target explicit repos
  - --repo="nginx*"             Match repos whose name starts with "nginx"
  - --repo="*"                  Match all repos under the group
  - --repo="*fips*"             Match repos containing "fips" in the name

In batch mode the command shows per-repo diffs, then asks for a single confirmation before applying all matched repos in parallel (up to 10 concurrent). Results are printed as a summary at the end. --save-as is not available in batch mode.

Dry-run mode:

Pass --dry-run to preview changes without applying them. No confirmation is requested and no changes are made. Exits with a non-zero code if changes would be applied, suitable for CI drift detection.

Customizable sections:

  contents.packages
    Add additional packages to install in the image (e.g., development tools,
    utilities). Packages must be available in Chainguard's package repository.

  environment
    Set environment variables that will be available in the image. Variables
    with the 'CHAINGUARD_' prefix are reserved and cannot be used.

  annotations
    Add custom OCI annotations to the image for tracking build information,
    compliance, or metadata. Keys with the 'dev.chainguard' prefix are reserved
    and cannot be used.

  accounts
    Customize image users and groups. You can define custom users with specific
    UIDs/GIDs, home directories, and group memberships. You can also specify
    which user the image should run as.

  certificates
    Provide custom certificates that will be merged with the default certificate
    bundle in the image. This is useful for adding internal CA certificates.
    Certificates can be defined in the YAML manifest or loaded from files using
    the --with-certificates flag (can be specified multiple times). Both methods
    can be combined and all certificates are merged together.
    NOTE: This is a Beta feature that requires enrollment. Contact your Customer
    Success Team to enable this feature.

Notice: Customer shall not provide Chainguard any personal data (or similarly regulated data)
as part of the Custom Assembly tool, other than the personal data that Chainguard collects in
the ordinary course of business, as further detailed in its
[Privacy Notice](https://www.chainguard.dev/legal/privacy-notice).

```
chainctl images repos build apply [flags]
```

### Examples

```

# Apply configuration from a file (interactive repo selection)
chainctl images repos build apply --file=config.yaml

# Apply to a specific repository
chainctl images repos build apply --repo=my-custom-python --file=config.yaml

# Apply and save as a new repository
chainctl images repos build apply --repo=my-custom-python --file=config.yaml --save-as=my-new-python

# Apply with automatic confirmation (for CI/CD)
chainctl images repos build apply --repo=my-custom-python --file=config.yaml --yes

# Add only custom certificates (no config file needed)
chainctl images repos build apply --repo=my-custom-python --with-certificates=ca1.pem --with-certificates=ca2.pem

# Add custom certificates alongside a config file
chainctl images repos build apply --repo=my-custom-python --file=config.yaml --with-certificates=ca1.pem --with-certificates=ca2.pem

# Apply to all repos under a group (batch mode)
chainctl images repos build apply --parent=my-org --repo="*" --file=config.yaml

# Apply to repos matching a wildcard pattern (batch mode)
chainctl images repos build apply --parent=my-org --repo="nginx*" --file=config.yaml

# Apply to multiple explicit repos (batch mode)
chainctl images repos build apply --repo=nginx --repo=nginx-fips --file=config.yaml

# Batch apply with automatic confirmation (for CI/CD)
chainctl images repos build apply --parent=my-org --repo="*" --file=config.yaml --yes

# Dry-run: preview changes without applying (exits 1 if diff detected)
chainctl images repos build apply --repo=my-custom-python --file=config.yaml --dry-run

# Dry-run across all repos (useful for CI drift detection)
chainctl images repos build apply --parent=my-org --repo="*" --file=config.yaml --dry-run

```

### Options

```
      --dry-run                     Print the diff without applying changes. Exits with a non-zero code if changes would be made.
  -f, --file string                 The name of the file containing the build config.
      --parent string               The name or id of the parent location to apply build config.
      --repo stringArray            The name or id of the repo to apply build config. Supports wildcards (*, ?, [abc]). Can be specified multiple times.
      --save-as string              Create a new repo with the edited configuration instead of updating the existing one.
      --with-certificates strings   Comma separated list of files to read the custom certificates from.
  -y, --yes                         Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

* [chainctl images repos build](/chainguard/chainctl/chainctl-docs/chainctl_images_repos_build/)	 - Manage custom image builds

