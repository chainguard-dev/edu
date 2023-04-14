---
title: "Troubleshooting Tips"
aliases: 
- /chainguard/chainguard-enforce/chainguard-enforce-kubernetes/troubleshooting-tips/
type: "article"
description: "Troubleshooting tips for Chainguard Enforce"
date: 2023-03-06T15:22:20+01:00
lastmod: 2023-03-28T15:22:20+01:00
draft: false
tags: ["Enforce", "Product", "Troubleshooting"]
images: []
menu:
  docs:
    parent: "chainguard-enforce"
weight: 805
toc: true
---

This page contains tips for troubleshooting problems that one may encounter when working with Chainguard Enforce. 

## Debug using `chainctl`

You can run `chainctl` in debug mode using the verbose flag `-v` or `--v` and passing an integer value of `2` or larger, as in `-v=2`. 

Using this flag, you can log all requests and responses or errors.

For example, to grab all logs related to the clusters listed for a group, you can run:

```sh
chainctl cluster ls --group $DEMO_GROUP -v=2
```

The output will return log data to support you in debugging. 

```
2023/03/28 22:23:58.418086 "level"=1 "msg"="Commandline flags" "active-within"="168h0m0s" "api"="api" "audience"="audience" "config"="" "console"="api" "group"="$DEMO_GROUP" "help"="false" "issuer"="oidc" "name"="" "output"="" "registry"="registry" "timestamp-authority"="timestamp" "v"="2"
2023/03/28 22:23:59.000042 gRPC: "level"=2 "msg"="iam.Groups.List" "request"="name:'$DEMO_GROUP' "
2023/03/28 22:23:59.089459 gRPC: "level"=2 "msg"="iam.Groups.List" "response"="items:<id:'' name:'$DEMO_GROUP' description:'Root of $DEMO_GROUP ' > "
2023/03/28 22:23:59.090213 gRPC: "level"=2 "msg"="tenant.Clusters.List" "request"="active_since:<seconds:1677651909 nanos:89511000 > uidp:<descendants_of:'' > "
2023/03/28 22:23:59.177413 gRPC: "level"=2 "msg"="tenant.Clusters.List" "response"=""
  NAME | GROUP | REMOTEID | REGISTERED | K8S VERSION | AGENT VERSION | LAST SEEN | ACTIVITY
-------+-------+----------+------------+-------------+---------------+-----------+-----------
```

By default, your next command passed without the `-v` flag will revert to the standard `chainctl` experience. Alternatively, you can pass `-v=0` to your `chainctl` command for the default experience, without logging. 

## How to disable admission control

There may be urgent situations where having admission control enabled is not desirable. For example, it could be preventing the cluster from functioning correctly or may be getting in the way of the operator.

In cases like this, you can completely disable the Chainguard Enforce admission webhook with the following commands.

```sh
kubectl delete validatingwebhookconfiguration enforcer
kubectl delete mutatingwebhookconfiguration enforcer
```

After your urgent situation is over, [reinstall Enforce in your cluster](/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/alternative-installation-methods/) to restore the webhook to its normal operation.


## Chainguard Enforce is unable to parse a given SBOM

One issue that may come up when working with Chainguard Enforce is that it won't ingest an SBOM as expected. This section outlines several potential causes for this issue and how you can address them.


### Check your permissions

Chainguard Enforce needs access to your images in order to parse the associated SBOMs. If your image is in a private repository, check out [our guide on setting up cloud account associations](/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/cloud-account-associations/) to grant Enforce read access to the image.


### SBOMs using older versions of CycloneDX

For CycloneDX, Chainguard Enforce currently only supports version 1.4.

    
### SBOM included as an in-toto attestation

We are in the process of updating Chainguard Enforce so it can readily parse SBOM attestations out of the box. In the meantime, you can parse SBOMs through implementing specific policies that cover this use case.

You can create a policy covering your image [through the Chainguard Enforce console](/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/chainguard-policies-ui/) or [using the `chainctl` command line tool](/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/chainguard-policies-cli/). Additionally, you can check out our [policy catalog](https://console.enforce.dev/policies/catalog) for our collection of policies that work directly with Chainguard Enforce.


## Policy does not cover a given image as expected

When working with the `ClusterImagePolicy`, note that the glob wildcard `*` does not cover the `/` character. For example, a glob pattern like `gcr.io/apple/*` will cover paths like `gcr.io/apple/yak` or `gcr.io/apple/zebra`, but not `gcr.io/apple/banana/cashew`.

To match _everything_ — including the `/` character — use the `**` wildcard instead.


## Enforce does not block Pod creation as expected

The first thing to check is whether you labeled your namespace with `policy.sigstore.dev/include=true`. You can double check whether the `default` namespace is correctly labeled with the following command.

```sh
kubectl get ns -l policy.sigstore.dev/include=true
```

If it is indeed labeled like this, you'll receive output like the following.

```
NAME      STATUS   AGE
default   Active   24s
```

If you need to label your namespace, you can do so with the following command. Note that this example labels the `default` namespace.

```sh
kubectl label ns default policy.sigstore.dev/include=true --overwrite
```

Be sure to use the exact string, variations like `included` won’t work.

Sometimes Chainguard Enforce is installed using the `observer` profile. Essentially, this means that Enforce just has read-only permission for workload discovery, and it cannot actually enforce policies. You can run `chainctl cluster ls` to find what profile the cluster is using.
