---
date: 2023-04-18T22:50:50Z
title: "chainctl clusters install"
slug: chainctl_clusters_install
url: /chainguard/chainctl/chainctl-docs/chainctl_clusters_install/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl clusters install

Install Chainguard into the current kubernetes context.

```
chainctl clusters install [--name NAME] [--description DESCRIPTION] [--group GROUP_NAME|GROUP_ID | --invite-code INVITE_CODE | --skip-invite | --managed={eks,gke} --cluster=CLUSTER_NAME | --private]
```

### Examples

```
  # Install Chainguard on a GKE cluster using a managed agent, and linking it
  # under GROUP_ID in the Chainguard resource hierarchy.
  chainctl cluster install --group=GROUP_ID --managed=gke --cluster=gke_project-id_us-central1_cluster-name
  
  # Install or Update the chainguard agent on a cluster.
  chainctl cluster install --skip-invite
  
  # Install or Update the chainguard agent on a cluster with private API endpoint
  chainctl cluster install --private
  
  # Install the Chainguard agent with an explicit invite code.
  chainctl cluster install --invite-code=INVITE_CODE
  
  # Install the Chainguard agent using a temporary invite code under the group
  # with ID "GROUP_ID".
  chainctl cluster install --group=GROUP_ID
  
  # Install the Chainguard agent enabling a fail open policy mode.
  chainctl cluster install --opt=webhook_fail_open=true
  
  # Install the Chainguard agent using a temporary invite code under a group
  # determined via an interactive prompt.
  chainctl cluster install
```

### Options

```
      --context string                   Indicates the name of the context (in kubectl) to be connect to Chainguard.
  -d, --description string               The description of the resource.
      --gcp-serviceaccount-file string   The path to a GCP service account JSON key file.
      --group string                     The group under which to create a temporary invite code and install the cluster.
  -h, --help                             help for install
      --invite-code string               An invite code to use for joining this cluster into the IAM hierarchy.
      --managed string                   Indicates the cluster's agent should be managed by Chainguard.  The value indicates the provider of the cluster, e.g. gke
  -n, --name string                      Given name of the resource.
      --opt strings                      extra key=value pairs to define enforcer profile options
      --private                          Kubernetes API endpoint isn't publicly accessible. Cannot be used with managed clusters.
      --profiles stringArray             The names of Chainguard profiles to install into the cluster.
      --skip-invite                      When specified we perform installation without an invite code.
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

* [chainctl clusters](/chainguard/chainctl/chainctl-docs/chainctl_clusters/)	 - Cluster related commands for the Chainguard platform.

