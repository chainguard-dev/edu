---
title: "Troubleshooting Tips"
aliases:
- /chainguard/chainguard-enforce/chainguard-enforce-kubernetes/troubleshooting-tips/
type: "article"
description: "Troubleshooting tips for Chainguard Enforce"
date: 2023-03-06T15:22:20+01:00
lastmod: 2023-07-05T15:22:20+01:00
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

## Installation

If you're encountering an issue with installation, we have a few recommendations to check, and guidance on using Rancher.

### Verify cluster is installed

The `remoteId` in `chainctl cluster install` is the UUID of the Gulfstream namespace; this will help identify whether a cluster is installed or not. You can learn more about installation in our [Installing the Chainguard Enforce Agent](/chainguard/chainguard-enforce/installation/alternative-installation-methods/) tutorial.

You can get the ID for Gulfstream with `kubectl`, as in the next command.

```sh
kubectl get namespace gulfstream -o json | jq .metadata.uid
```

You'll receive the ID.

```
"B501db05-3702-4403-81b5-c74a55976597"
```

With `chainctl cluster list`, you can also get this ID by passing the group ID.

```sh
chainctl cluster list --group $GROUP_ID -o json | jq -r .items[0].remoteId
```

The output here will also be the remote ID. 

```
b501db05-3702-4403-81b5-c74a55976597
```

You can review more options in the [`chainctl` docs](/chainguard/chainctl/chainctl-docs/chainctl_clusters_list/).

### Cluster OIDC configuration exit status

You may encounter an exit status due to being unable to fetch the OIDC configuration. This can occur when running the `chainctl cluster install` command.

```sh
chainctl cluster install --group=$GROUP --private --context demo 
```

The error will be similar to the following.

```
...
Installing Chainguard agent...
couldn't fetch cluster OIDC configuration exit status 1
```

The cause of this may be due to the `openid-configuration` and `jwks` being inaccessible within the Kubernetes API. You can determine this with `kubectl`.

First, check whether the issue is with the `openid-configuration`.

```sh
kubectl get --raw /.well-known/openid-configuration
```

If this is the issue, you'll receive an error as output.

```
Error from server (NotFound): the server could not find the requested resource
```

Next, you can check if the issue is related to `jwks`.

```sh
kubectl get --raw /openid/v1/jwks
```

If `jwks` being inaccessible is the issue, you'll receive an error here.

```
Error from server (NotFound): the server could not find the requested resource
```

This output reveals that the endpoints are not available to `chainctl`, whcih may be due to an auth proxy between `chainctl` and the control plane.

To solve for this issue, you'll need an OpenID Connect Well-Known Configuration Endpoint, which should be available at the `/.well-known/openid-configuration` path, This will enable you to use `chainctl` for installation and to register an identity. You can check that the file is there with `kubectl`.

```sh
kubectl get --raw /.well-known/openid-configuration
```

If you receive an error that the requested resource was not found, make sure you are using the `--private` option on installation. You can review guidance on this option in the [Configuring Enforcer Options](/chainguard/chainguard-enforce/installation/configure-enforcer-options-during-installation/#install-with-chainctl) guide.

If you are using Rancher, you'll be able to generate “direct access” kubeconfigs that bypass the auth proxy and go directly to the cluster. Please follow the [Rancher documentation to create a new kubeconfig file](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/manage-clusters/access-clusters/use-kubectl-and-kubeconfig#authenticating-directly-with-a-downstream-cluster).

### Installing Enforce with Rancher

If you're using Rancher for Kubernetes, you'll need to point directly to your kubeconfig file:

```sh
KUBECONFIG=/etc/rancher/rke2/rke2.yaml chainctl cluster install --group=$GROUP --private
```

If you cannot reach the OIDC endpoint, this will cause issues for a cluster install, review the [previous section](#cluster-oidc-configuration-exit-status) for guidance on troubleshooting this. 

Additionally, you'll need direct access to the authorized endpoint and not the Rancher proxy URL. When you run `kubectl config view`, you should receive something like the output below, without the Rancher URL.

```
clusters:
- cluster:
    server: <direct-url-to-cluster>
```

## Issues logging in with chainctl

Ensure that you're pointing to production. You can check the `chainctl` config.

```sh
chainctl config view 
```

The config should be pointing to the production environment, as in the next output.

```
platform:
    api: https://console-api.enforce.dev
    audience: https://console-api.enforce.dev
    console: https://console.enforce.dev
    issuer: https://issuer.enforce.dev
    registry: https://cgr.dev
    timestamp-authority: https://tsa.enforce.dev
```

For more guidance on working with the `chainctl` config, review our guide on [How to Manage `chainctl` Configuration](/chainguard/chainguard-enforce/manage-chainctl-config/).

## Policies 

If you're running into issues with policies, this section has some tips for recovery.

### Policy does not cover a given image as expected

When working with the `ClusterImagePolicy`, note that the glob wildcard `*` does not cover the `/` character. For example, a glob pattern like `gcr.io/apple/*` will cover paths like `gcr.io/apple/yak` or `gcr.io/apple/zebra`, but not `gcr.io/apple/banana/cashew`.

To match _everything_ — including the `/` character — use the `**` wildcard instead.

### Check that the cluster image policy is in the ConfigMap

You can ensure that a cluster image policy is in the [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/) with the following `kubectl` command:

```sh
kubectl get cm config-image-policies -n cosign-system 
```

A describe of the ConfigMap will show the full policy. 

```
kubectl describe  cm config-image-policies -n cosign-system 
Name:         config-image-policies
Namespace:    cosign-system
Labels:       <none>
Annotations:  gulfstream.dev/resync: 10s

Data
====
demo-custom-metric-usage-dev:
----
{"uid":"b98f9309-01df-4590-82a0-afb05314b828",REDACTED}
rego-hostnetworking:
----
{"uid":"02d60b97-5d22-48c2-bd92-684025377e53",REDACTED}

BinaryData
====

Events:  <none>
```

### Check that the cluster image policy is deployed to cluster

You can use the following `kubectl` command to make sure that the cluster image policy is deployed to your cluster.

```sh
kubectl get cip
```

You should get output similar to the following.

```
NAME                              AGE
demo-custom-metric-usage-dev      7h24m
rego-hostnetworking               5h45m
```

## Disable admission control

There may be urgent situations where having admission control enabled is not desirable. For example, it could be preventing the cluster from functioning correctly or may be getting in the way of the operator.

In cases like this, you can completely disable the Chainguard Enforce admission webhook with the following commands.

```sh
kubectl delete validatingwebhookconfiguration enforcer
kubectl delete mutatingwebhookconfiguration enforcer
```

After your urgent situation is over, [reinstall Enforce in your cluster](/chainguard/chainguard-enforce/installation/alternative-installation-methods/) to restore the webhook to its normal operation.


## Verify that namespace is labeled for enforcement

You can check that the namespace is labeled for enforcement with the following command:

```sh
kubectl label namespaces $NAME_SPACE policy.sigstore.dev/include=true
```

To label an individual namespace, or set the option to on install to label all namespaces.

```sh
chainctl install cluster --opt=namespace_enforcement_mode=opt-in
```

You can read more information about installation options in Chainguard Enforce in [our guide](/chainguard/chainguard-enforce/installation/configure-enforcer-options-during-installation/#enforcer-options).

## Unable to parse an SBOM

One issue that may come up when working with Chainguard Enforce is that it won't ingest an SBOM as expected. This section outlines several potential causes for this issue and how you can address them.

### Check your permissions

Chainguard Enforce needs access to your images in order to parse the associated SBOMs. If your image is in a private repository, check out [our guide on setting up cloud account associations](/chainguard/chainguard-enforce/cloud-account-associations/) to grant Enforce read access to the image.


### SBOMs using older versions of CycloneDX

For CycloneDX, Chainguard Enforce currently only supports version 1.4.


### SBOM included as an in-toto attestation

We are in the process of updating Chainguard Enforce so it can readily parse SBOM attestations out of the box. In the meantime, you can parse SBOMs through implementing specific policies that cover this use case.

You can create a policy covering your image [through the Chainguard Enforce console](/chainguard/chainguard-enforce/policies/chainguard-policies-ui/) or [using the `chainctl` command line tool](/chainguard/chainguard-enforce/policies/chainguard-policies-cli/). Additionally, you can check out our [policy catalog](https://console.enforce.dev/policies/catalog) for our collection of policies that work directly with Chainguard Enforce.

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

## Debugging with `chainctl`

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