---
title: "Manage Policies with chainctl"
linktitle: "chainctl Policy Management"
aliases:
- /chainguard/chainguard-enforce/chainguard-enforce-kubernetes/chainguard-policies-cli/
type: "article"
description: "Creating and managing policies with chainctl, the Chainguard command line tool"
date: 2022-11-1511T11:07:52+02:00
lastmod: 2022-11-15T11:07:52+02:00
draft: false
tags: ["Enforce", "Product", "Procedural", "Policy", "Reference"]
images: []
menu:
  docs:
    parent: "policies"
weight: 005
toc: true
---

{{< tabs >}}
  {{< tab title="CLI" active=true url="/chainguard/chainguard-enforce/policies/chainguard-policies-cli/" >}}
  {{< tab title="Console" active=false url="/chainguard/chainguard-enforce/policies/chainguard-policies-ui/" >}}
{{</ tabs >}}

Chainguard Enforce allows you to define and apply policies to your Kubernetes clusters, ensuring that only those deployments that satisfy a given policy are successful. This guide outlines how to create and manage policies using `chainctl`, the Chainguard Enforce command line interface. You must already have an account with Chainguard to follow this guide. You can request access for **Chainguard Enforce** on the [inquiry form](https://www.chainguard.dev/contact?utm_source=docs).

To review sample policies that you may want to leverage, please check out our page on [Chainguard Enforce Policy Examples](/chainguard/chainguard-enforce/policies/chainguard-enforce-policy-examples/). If you would like to use the [Chainguard Enforce UI](https://console.enforce.dev) to work with policies, check out our guide on [How to create policies in the Chainguard Enforce Console](/chainguard/chainguard-enforce/policies/chainguard-policies-ui/).


## Prerequisites

In order to follow along with the examples in this guide, you will need `chainctl` installed on your local machine. Follow our guide on [How To Install `chainctl`](/chainguard/chainguard-enforce/how-to-install-chainctl/) to set this up.


## Authenticate to the Chainguard Enforce platform

To begin, you will need to authenticate to the Chainguard Enforce platform from your local machine with the following command.

```sh
chainctl auth login
```

A web browser window will open prompting you to log in using the [OIDC protocol](/software-security/glossary/#oidc). Once authenticated, you can begin using `chainctl` to manage and delegate your Chainguard Enforce policies.


## Apply a new policy

You can apply a policy to every cluster managed by a given group with the `policies apply` subcommand. Assuming that you have a policy file named `enforce-policy.yaml` in your current working directory, you could apply a policy with the following command.

```sh
chainctl policies apply -f enforce-policy.yaml
```

After running a `policies apply` command like this, an interactive menu will appear in your terminal prompting you to select the group that the policy should apply to. Chainguard Enforce provides a rich [Identity and Access Management (IAM) model](/chainguard/chainguard-enforce/iam-groups/overview-of-enforce-iam-model/) similar to those used by AWS and GCP. Each Chainguard policy needs to be associated with a group, and will be effective for that group as well as all the groups descending from it.

The `-f` option in this command tells `chainctl` the location of the policy file to use to apply a new policy to a cluster. Note that all Chainguard Enforce policies must be written in YAML. If you don't include this option followed by a policy file, `chainctl` will open your default text editor for you to enter a policy manually.

The `policies apply` subcommand accepts the `--group` option. When followed by the name or identification number of an existing Chainguard Enforce IAM group and combined with the `-f` flag and policy file, this option allows you to avoid using the interactive menu. This is useful in situations where you would prefer to take a more declarative approach to manage your policies.

```sh
chainctl policies apply -f enforce-policy.yaml --group my-group
```

In this example, the group is named `my-group`. When you run this command on your own setup, be sure to replace this with the relevant group's name or identification number. You can retrieve a list of all your groups' names and ID numbers with this command:

```sh
chainctl iam groups list -o table
```

Lastly, `policies apply` also accepts the `-d` option which allows you to add a description of your policy.

```sh
chainctl policies apply -f enforce-policy.yaml -d "This is a description of my policy"
```

Adding a description like this can be helpful in cases where you need to differentiate or organize multiple policies that have been applied to the same group.


## Inspect existing policies

If you've already configured one or more policies, you can review them by running the `chainctl policies list` command.

```sh
chainctl policies list
```

This will return a table with information about all of your active policies, including the policy's unique identification number, its name, and description if one has been added.

```
                             ID                             |      NAME      |       DESCRIPTION
------------------------------------------------------------+----------------+--------------------------
  d22957f0271ef73221005f8c11bb027888829e09/2eb7b5401728bd9f | sample-policy  | This is a sample policy
  d22957f0271ef73221005f8c11bb027888829e09/6c559b7225e889f9 | my-policy      | My policy
  d22957f0271ef73221005f8c11bb027888829e09/f7253a47e09f3bf0 | enforce-policy |
```

However, this output only provides some high-level information about your policies. In order to inspect the contents of a given policy, you can run the `policies view` subcommand.

```sh
chainctl policies view
```

A menu will appear, prompting you to select the policy you'd like to inspect. To avoid using the interactive menu, you can follow the `view` subcommand with the name or identification number of the policy you want to inspect. In this example, we are passing the example policy name `enforce-policy`.

```sh
chainctl policies view enforce-policy
```

This will output the contents of the chosen policy directly.


## Edit policies

`chainctl` includes the `policies edit` subcommand, allowing you to modify existing policies.

```sh
chainctl policies edit
```

As with `policies view`, when you run `policies edit` without any arguments it will open an interactive menu from which you can select the policy that you want to edit. You can also append the name or the identification number Chainguard Enforce uses to refer to the policy to avoid having to select the policy, as in this example that is passing the `enforce-policy` policy name.

```sh
chainctl policies edit enforce-policy
```

Regardless of how you run this command, it will open your default text editor where you can edit the specified policy's contents. After saving your changes and closing the editor, `chainctl` will prompt you to confirm whether you want to save the changes to the active policy. If you do confirm, the updated policy will be saved and applied automatically.

> **Note:** When you use a YAML file as the basis for a Chainguard Enforce policy, Enforce ingests the file's content and stores it internally as a policy. If later you run the `edit` subcommand to update a policy, it will not edit the original YAML file; it will only edit the policy as it exists within Chainguard Enforce.

`chainctl` also includes the `update` subcommand. Rather than updating the policy itself, this allows you to update the description of a policy.

The `policies update` subcommand requires a few arguments in order to run. Specifically, you must include the name or identification number of the policy whose description you want to update, the `--description` option, and the policy's new description. This example updates the description of the `enforce-policy` policy's description to read "A description of my policy."

```sh
chainctl policies update enforce-policy --description "A description of my policy."
```

You can remove a policy's description by updating it to an empty string.

```sh
chainctl policies update enforce-policy --description ""
```

Essentially, this example command deletes the `enforce-policy` policy's description.

## Policy versions

Policy versions enable you to gradually test and roll out policy changes to your cluster over time, without losing the historical context of how a given policy has changed. Versions also increase your visibility into when and by whom policies were updated. With policy versions, you can quickly rollback to a stable version in the event of the inevitable typo or unintended consequence discovered too late.

### Reviewing policy versions in chainctl

‍No special action is needed to create a new version of a policy; any change to the policy document will automatically create a new version. Note that updates to a policy’s description will not create a new version. Differences between versions can be inspected through either `chainctl` or the Console.

Listing policies with the `-o wide` or `--output=wide` flag shows some new policy metadata, including created and updated timestamps, the currently enforced version of the policy, and the author of the enforced version.

```sh
chainctl policy ls -o wide
```

If you scroll horizontally across the output below, you'll be able to view `ENFORCED VERSION`, `CREATED`, and `UPDATED` metadata.

```
                             ID                             |           NAME            |          DESCRIPTION           |   MODE   | ENFORCED VERSION | CREATED | UPDATED |         AUTHOR           
------------------------------------------------------------+---------------------------+--------------------------------+----------+------------------+---------+---------+--------------------------
  0bed35fb980e8f8ba6d0757e01c950974cfd2593/928966789defb685 | allow-gke-policy          | GKE policy                     | ENFORCED | f8389e3524686185 | 3d      | 2d      | inky@chainguard.dev  
  7e145ac5c2e877cfad4315525402bfd564c00ec4/04bc993bbb964648 | sigstore-demo             |                                | ENFORCED |                  | 1d      | 1d      |                          
  99070fadb9e03ee46ebb5c3d635a8c40c92670ad/ee76b4dc8b3b8c2b | vuln-warning-message-rego | Vulnerability attestation with | WARN     | cdb3d1526d6acaf3 | 6d      | 4d      | inky@chainguard.dev      
                                                            |                           | Warn for attestations          |          |                  |         |         |                          
                                                            
```

If you were already a Chainguard Enforce User, you’ll notice legacy policies are missing some of this metadata. Legacy policies are still fully supported and can be versioned just like newly applied policies. These data will be populated as policies are updated.

‍To bring up a list of all versions of a named policy, you can run:

```sh
chainctl policy versions ls
```

This will sort policies by creation date.

### Managing versions of policies

‍Once a policy exists in Chainguard Enforce, updates to the policy document automatically create a new version. Policy documents can be updated, hence creating a new version, with either `chainctl policy apply` or `chainctl policy edit`.

To view versions to compare a version against the active version.

```sh
chainctl policy versions view
```

In order to review diffs of two versions of a policy, you can use the following command:

```sh
chainctl policy versions diff
```

Diffs can be viewed regardless of the active version.

‍You can accomplish a rollback to a previous policy version with:

```sh
chainctl policy versions activate
```

To confirm the rollback, use the `chainctl policy ls -owide` command to inspect the version.

## Delete policies

If you would like to delete a policy, run the `policies delete` subcommand.

```sh
chainctl policies delete
```

As with the commands outlined previously, if you don't include any other arguments this command will open an interactive menu where you can select the policy you want to delete. It will then prompt you to confirm whether you want to delete the selected policy by pressing `Y` and then `ENTER`.

To run this command non-interactively, you can append the name or identification number of the policy you want to delete.

```sh
chainctl policies delete enforce-policy
```

You can follow this command with the `-y` flag to automatically answer "yes" to the confirmation prompt.

## Aliases for policy management commands

Similar to other CLI tools, `chainctl` accepts aliases for many of its subcommands, including the suite of commands related to managing policies.

For example, `chainctl` will accept either `policy` or `pol` in place of `policies`, meaning that the following three commands are equivalent.

```sh
chainctl policies list
chainctl policy list
chainctl pol list
```

Likewise, the following `chainctl policies` subcommands have these equivalent alises:

| Subcommand      | Alias |
| ----------- | ----------- |
| `apply`      | `create`       |
| `delete`   | `rm`        |
| `list`      | `ls`       |
| `update`   | `set` |


If you forget these aliases or you just aren't sure about how one of these commands works, you can follow `policies` with the `-h` flag (short for the `--help` option).

```sh
chainctl policies -h
```

```
Policy related commands for the Chainguard platform.

Usage:
  chainctl policies [command]

Aliases:
  policies, policy, pol

Available Commands:
  apply       Create or update a policy described by file or stdin.
  delete      Delete a policy.
  edit        Edit a policy document.
  list        List policies.
  update      Update the description of a policy.
  view        View a policy.

Flags:
  -h, --help   help for policies

Global Flags:
      --api string        The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string   The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string     A specific chainctl config file.
      --console string    The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string     The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string     Output format. One of: ["", "table", "tree", "json", "id", "wide"]

Use "chainctl policies [command] --help" for more information about a command.
```

For additional guidance on using `chainctl`, review our [full reference documentation](/chainguard/chainctl/).
