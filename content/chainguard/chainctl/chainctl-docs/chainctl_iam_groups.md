---
date: 2023-04-14T15:52:13Z
title: "chainctl iam groups"
slug: chainctl_iam_groups
url: /chainguard/chainctl/chainctl-docs/chainctl_iam_groups/
draft: false
images: []
type: "article"
toc: true
---
## chainctl iam groups

IAM Group resource interactions.

### Options

```
  -h, --help   help for groups
```

### Options inherited from parent commands

```
      --api string                   The url of the Chainguard platform API. (default "http://api.api-system.svc")
      --audience string              The Chainguard token audience to request. (default "http://api.api-system.svc")
      --config string                A specific chainctl config file.
      --console string               The url of the Chainguard platform Console. (default "http://console-ui.api-system.svc")
      --issuer string                The url of the Chainguard STS endpoint. (default "http://issuer.oidc-system.svc")
  -o, --output string                Output format. One of: ["", "table", "tree", "json", "id", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "http://tsa.timestamp-authority.svc")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl iam](/chainguard/chainctl/chainctl-docs/chainctl_iam/)	 - IAM related commands for the Chainguard platform.
* [chainctl iam groups check-aws](/chainguard/chainctl/chainctl-docs/chainctl_iam_groups_check-aws/)	 - Checks that the given group has been properly configured for OIDC federation with AWS.
* [chainctl iam groups check-gcp](/chainguard/chainctl/chainctl-docs/chainctl_iam_groups_check-gcp/)	 - Checks that the given group has been properly configured for OIDC federation with GCP.
* [chainctl iam groups create](/chainguard/chainctl/chainctl-docs/chainctl_iam_groups_create/)	 - Create a new group or add a group under an existing group.
* [chainctl iam groups delete](/chainguard/chainctl/chainctl-docs/chainctl_iam_groups_delete/)	 - Delete group
* [chainctl iam groups describe](/chainguard/chainctl/chainctl-docs/chainctl_iam_groups_describe/)	 - Describe a group.
* [chainctl iam groups list](/chainguard/chainctl/chainctl-docs/chainctl_iam_groups_list/)	 - List groups.
* [chainctl iam groups remove-aws](/chainguard/chainctl/chainctl-docs/chainctl_iam_groups_remove-aws/)	 - Remove any configured AWS account association for this IAM Group.
* [chainctl iam groups remove-gcp](/chainguard/chainctl/chainctl-docs/chainctl_iam_groups_remove-gcp/)	 - Remove any configured GCP account association for this IAM Group.
* [chainctl iam groups set-aws](/chainguard/chainctl/chainctl-docs/chainctl_iam_groups_set-aws/)	 - Set the AWS account association for this IAM Group.
* [chainctl iam groups set-gcp](/chainguard/chainctl/chainctl-docs/chainctl_iam_groups_set-gcp/)	 - Set the GCP project association for this IAM Group.
* [chainctl iam groups update](/chainguard/chainctl/chainctl-docs/chainctl_iam_groups_update/)	 - Update a group.

