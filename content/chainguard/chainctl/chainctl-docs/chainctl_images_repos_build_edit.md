---
date: 2026-02-02T09:25:35Z
title: "chainctl images repos build edit"
slug: chainctl_images_repos_build_edit
url: /chainguard/chainctl/chainctl-docs/chainctl_images_repos_build_edit/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl images repos build edit

Edit a build config, optionally creating a new repo with --save-as

### Synopsis


Extend a Chainguard image with custom packages, environment variables, and
certificates.

You can use Custom Assembly to customize any image you are entitled to by
adding packages from Chainguard's repository, setting environment variables,
adding OCI annotations or customizing user accounts and groups.

Furthermore, Custom Assembly allows you to include any additional custom
certificates in the image. They will be merged with the default certificate
bundle, enabling the image to trust non-standard certificate authorities and
connect to services secured with custom TLS certificates.

Finally, you can create variants by choosing to save the customized
configuration as a new repository instead of modifying the existing one.

How it works:

You customize the image by editing a YAML configuration manifest. The command
opens your editor with the current repository configuration (or a template for
new repositories). To skip the interactive editor, use the --filename flag to
provide a pre-written configuration file.

After editing, the command displays a diff of your changes for review. Upon
confirmation, it updates the repository configuration and starts a custom build
automatically.


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
chainctl images repos build edit [flags]
```

### Examples

```

# Edit a repository interactively (prompts for repo selection)
chainctl images repos build edit

# Edit a specific repository
chainctl images repos build edit --repo=my-custom-python

# Edit and save as a new repository
chainctl images repos build edit --repo=my-custom-python --save-as=my-new-python

# Apply configuration from a file
chainctl images repos build edit --repo=my-custom-python --file=config.yaml

# Apply configuration from a file and save as new repository
chainctl images repos build edit --file=config.yaml --save-as=my-new-python

# Add custom certificates (interactive mode)
chainctl images repos build edit --repo=my-custom-python --with-certificates=ca1.pem --with-certificates=ca2.pem

# Combine file-based config with certificates
chainctl images repos build edit --file=config.yaml --with-certificates=internal-ca.pem

```

### Options

```
  -f, --file string                 The name of the file containing the build config.
  -h, --help                        help for edit
      --parent string               The name or id of the parent location to apply build config.
      --repo string                 The name or id of the repo to apply build config.
      --save-as string              Create a new repo with the edited configuration instead of updating the existing one.
      --with-certificates strings   Comma separated list of files to read the custom certificates from.
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

