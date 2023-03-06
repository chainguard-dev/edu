---
title: "Troubleshooting Tips"
type: "article"
description: "Troubleshooting tips for Chainguard Enforce"
date: 2023-03-06T15:22:20+01:00
lastmod: 2023-03-06T15:22:20+01:00
draft: false
images: []
menu:
  docs:
	parent: "chainguard-enforce-kubernetes"
weight: 900
toc: true
---

This page contains tips for troubleshooting problems that one may encounter when working with Chainguard Enforce. 


## How to disable admission control

There may be emergency situations where having admission control enabled is not desirable. For example, it could be preventing the cluster from functioning correctly or may be getting in the way of the operator.

In cases like this, you can completely disable the Chainguard Enforce admission webhook with the following commands.

```sh
kubectl delete validatingwebhookconfiguration enforcer
kubectl delete mutatingwebhookconfiguration enforcer
```

After your emergency is over, reinstall Enforce in your cluster to restore the webhook to its normal operation.


## Chainguard Enforce is unable to parse a given SBOM

One problem that may come up when working with Chainguard Enforce is that it won't correctly ingest an SBOM. This section outlines several potential causes for this issue and how you can address them.



### Check your permissions

Chainguard Enforce needs access to your images in order to parse the associated SBOMs. If your image is in a private repository, check out [our guide on setting up cloud account associations](https://edu.chainguard.dev/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/cloud-account-associations/) to grant Enforce read access to the image.


### SBOMs using older versions of CycloneDX

For CycloneDX, Chainguard Enforce currently only supports version 1.4.

    
### SBOM included as an in-toto attestation

We are in the process of changing Chainguard Enforce to be able to parse SBOM attestations out of the box. In the meantime, though, they can only be parsed if there is a policy covering them.

You can create a policy covering your image [through the Chainguard Enforce console](https://edu.chainguard.dev/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/chainguard-policies-ui/) or [using the `chainctl` command line tool](https://edu.chainguard.dev/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/chainguard-policies-cli/). Additionally, you can check out our [policy catalog](https://console.enforce.dev/policies/catalog) for our collection of example policies.


## Policy does not cover a given image as expected

One common `ClusterImagePolicy` issue is that the glob wildcard `*` does not cover the `/` character. For example, a glob pattern like `gcr.io/foo/*` will cover paths like `gcr.io/foo/bar` or `gcr.io/foo/blah`, but not `gcr.io/foo/bar/baz`.

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