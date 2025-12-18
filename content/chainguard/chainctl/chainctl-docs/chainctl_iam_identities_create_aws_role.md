---
date: 2025-12-17T18:32:17Z
title: "chainctl iam identities create aws role"
slug: chainctl_iam_identities_create_aws_role
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_identities_create_aws_role/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl iam identities create aws role



```
chainctl iam identities create aws role NAME --aws-account-id=ACCOUNT --aws-role-name=NAME [--aws-role-id=ID] [--aws-partition=PARTITION] [--parent=PARENT] [--description=DESC] [--role=ROLE,ROLE,...] [--output=id|json|table]
```

### Examples

```
  # Create an assumable identity for an AWS IAM role.
  chainctl iam identities create aws role my-aws-identity --aws-account-id=123456789012 --aws-role-name=my-role
  
  # Create an assumable identity for an AWS IAM role. Bind it to the registry.pull role.
  chainctl iam identities create aws role my-aws-identity --aws-account-id=123456789012 --aws-role-name=my-role --role=registry.pull
  
  # Provide the unique ID of an AWS IAM role. This prevents the identity from being assumed if the role is deleted and then recreated with the same name.
  chainctl iam identities create aws role my-aws-identity --aws-account-id=123456789012 --aws-role-name=my-role --aws-role-id=AROAEXAMPLEC2UL7LUB
  
  # Create an assumable identity for an AWS IAM role in the aws-us-gov partition.
  chainctl iam identities create aws role my-aws-identity --aws-partition=aws-us-gov --aws-account-id=123456789012 --aws-role-name=my-role
```

### Options

```
      --aws-account-id string   The ID of the AWS account.
      --aws-partition string    The partition in which the role is located. For instance: aws, aws-cn or aws-us-gov. (default "aws")
      --aws-role-id string      The unique ID of the IAM role.
      --aws-role-name string    The name of the IAM role.
  -d, --description string      The description of the resource.
  -h, --help                    help for role
  -n, --name string             Given name of the resource.
      --parent string           The name or id of the parent location to create this identity under.
      --role strings            A comma separated list of names or IDs of roles to bind this identity to (optional).
  -y, --yes                     Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively.
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

* [chainctl iam identities create aws](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities_create_aws/)	 - Create a new identity for an AWS IAM resource.

