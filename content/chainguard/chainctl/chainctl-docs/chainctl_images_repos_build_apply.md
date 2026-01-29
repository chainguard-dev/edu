---
date: 2026-01-28T21:39:13Z
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

Apply a build config from a file

### Synopsis


Apply a pre-written YAML configuration file to customize a Chainguard image.

You can use Custom Assembly to customize any image you are entitled to by
adding packages from Chainguard's repository, setting environment variables,
adding OCI annotations, customizing user accounts and groups, or including
custom certificates. The customized image is built automatically without
requiring you to fork images or maintain custom build pipelines.

This command applies Custom Assembly configurations from a YAML file without
opening an interactive editor. Use this for automated workflows, CI/CD pipelines,
or when you have configuration files managed in version control.

Finally, you can create variants by choosing to save the customized configuration
as a new repository instead of modifying the existing one.

How it works:

You customize the image by applying a YAML configuration file. Provide the file
using the --file flag. The command reads the file, validates the configuration,
and displays a diff comparing it to the current repository configuration (or an
empty baseline for new repositories).

After reviewing the diff, you confirm the changes. The command then updates the
repository configuration and starts a custom build automatically.

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
    Certificates must be defined in the YAML manifest.
    NOTE: This is a Beta feature that requires enrollment. Contact your Customer
    Success Team to enable this feature.


```
chainctl images repos build apply [flags]
```

### Examples

```

# Apply configuration from a file
chainctl images repos build apply --repo=my-custom-python --file=config.yaml

# Apply and save as a new repository
chainctl images repos build apply --repo=my-custom-python --file=config.yaml --save-as=my-new-python

# Apply with automatic confirmation (for CI/CD)
chainctl images repos build apply --repo=my-custom-python --file=config.yaml --yes

# Apply to interactively selected repository
chainctl images repos build apply --file=config.yaml

```

### Options

```
  -f, --file string      The name of the file containing the build config.
  -h, --help             help for apply
      --parent string    The name or id of the parent location to apply build config.
      --repo string      The name or id of the repo to apply build config.
      --save-as string   Create a new repo with the edited configuration instead of updating the existing one.
  -y, --yes              Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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
  -o, --output string      Output format. One of: [csv, env, go-template, id, json, markdown, none, table, terse, tree, wide]
  -v, --v int              Set the log verbosity level.
```

### SEE ALSO

* [chainctl images repos build](/chainguard/chainctl/chainctl-docs/chainctl_images_repos_build/)	 - Manage custom image builds

