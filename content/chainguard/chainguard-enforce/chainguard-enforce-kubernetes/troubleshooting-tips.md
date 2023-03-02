---
title: "Troubleshooting tips"
type: "article"
description: "Troubleshooting tips for Chainguard Enforce"
date: 2022-07-15T15:22:20+01:00
lastmod: 2022-11-29T15:22:20+01:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-enforce-kubernetes"
weight: 100
toc: true
---

# Enforce troubleshooting FAQs:

## Emergency

There may be emergency situations where admission control is not desirable,
either by preventing the cluster from functioning correctly or getting in
the way of the operator, the Enforce admission webhook can be completely 
disabled. Run the following command to disable it


```
kubectl delete validatingwebhookconfiguration enforcer
kubectl delete mutatingwebhookconfiguration enforcer
```

After your emergency is over, reinstall Enforce in your cluster to have the
webhook restored to its normal operation.

## Enforce did not parse my SBOM

### Check your permission:

Enforce scans your images from our SAAS and will need access to your images
in order to parse the SBOM. If your image is in a private repository, check out
this [doc](https://edu.chainguard.dev/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/cloud-account-associations/)
to grant Enforce the read access to your image.

### My SBOM is CycloneDX version 1.3 or older:
   
Currently, for CycloneDX we only support version 1.4. 
    
### My SBOM is included as an in-toto attestation: 
    
We are in the process of changing Enforce to parse SBOM attestation out of 
the box, however in the meantime they are only parsed if there is a policy 
covering them. Please follow our docs (like [this one](https://edu.chainguard.dev/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/chainguard-policies-ui/),
or [this one](https://edu.chainguard.dev/chainguard/chainguard-enforce/chainguard-enforce-kubernetes/chainguard-policies-cli/))
to create a policy covering your image. Please also check out our
[policy catalog](https://console.enforce.dev/policies/catalog).

## I create a policy but it does not cover my image:

One common issues is that in ClusterImagePolicy, the glob wildcard `*` does
not cover the `/` character: For example, a glob pattern like `gcr.io/foo/*`
will only cover `gcr.io/foo/bar`, `gcr.io/foo/blah`, but not `gcr.io/foo/bar/baz`.
To match _everything including the / character_, please use the `**` wildcard
instead. 
    
## Enforce does not actually block a Pod creation:

The first thing to check is whether you labeled your namespace with
`policy.sigstore.dev/include=true`. Please use the exact string, variations like
`included` won’t work.
   
Sometimes Enforce was installed using the observer profile. What this means is
that Enforce has only read-only permission for discovery of workload in your
clusters but not enforcing policies. You can run `chainctl cluster ls` to know
what profile the cluster is using.
