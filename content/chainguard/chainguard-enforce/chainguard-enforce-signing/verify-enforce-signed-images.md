
---
title: "Example Policy for Enforce Signed Images"
type: "article"
description: "Verify images signed by Chainguard Enforce"
date: 2022-07-15T15:22:20+01:00
lastmod: 2022-11-29T15:22:20+01:00
draft: false
tags: ["ENFORCE", "REFERENCE", "POLICY", "PRODUCT"]
images: []
menu:
  docs:
    parent: "chainguard-enforce-signing"
weight: 100
toc: true
---

Chainguard Enforce for Kubernetes allows users to create their own security policies that they can enforce in their clusters. 

Here is an example of a policy template used to verify images that has been signed by our Enforce signing feature.

```yaml
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: enforce-signed-keyless
spec:
  images:
  - glob: image/*
  authorities:
  - keyless:
      trustRootRef: my-sigstore-keys
      url: https://<my-enforce-sigstore-hostname-instance>
      identities:
        - issuer: 'https://auth.chainguard.dev/'
          subject: 'foo@example.com'
      insecureIgnoreSCT: true # In Enforce Signing, there isn't any proof of inclusion in a certificate transparency log.
    rfc3161timestamp:
      trustRootRef: my-sigstore-keys
```

This policy verifies that certain images satifying the glob pattern need to be signed using a specific trust root and a list of defined identities.

In the following, we detail the purpose of the different fields:

* `keyless.insecureIgnoreSCT` is enabled due to the lack of a certificate transparency log in the Enforce signing infrastructure.

* `keyless.url` sets the URL of the Enforce Sigstore instance used to sign the images. You can obtain the value by getting the `hostname` of your instace using the command `chainctl sigstore ca describe $ENFORCE_CA_NAME`. Replace `$ENFORCE_CA_NAME` with the name of your Sigstore CA.

* `keyless.trustRootRef` refers to the TrustRoot resource created to store the base64 format of the `SIGSTORE_ROOT_FILE` or sigstore root certificate of your sigstore instance.

* `keyless.trustRootRef` refers to the TrustRoot resource created to store the base64 format of the `COSIGN_TIMESTAMP_CERTIFICATE_CHAIN`. This certificate chain can be obtained from the timestamp server url. It can be found as an environment variable `COSIGN_TIMESTAMP_SERVER_URL` when running `chainctl sigstore env $ENFORCE_CA_NAME`. Once you got the url, you just need to call the following endpoint of your timestamp authority server to return the certificate chain. 

```bash
curl https://tsa.enforce.dev/api/v1/timestamp/certchain
```

If we now look at the configuration of TrustRoot resource:

```yaml
apiVersion: policy.sigstore.dev/v1alpha1
kind: TrustRoot
metadata:
  name: my-sigstore-keys
spec:
  sigstoreKeys:
    certificateAuthorities:
    - subject:
        organization: <my-organization>
        commonName: <my-common-name>
      uri: https://<my-enforce-sigstore-hostname-instance>
      certChain: |-
        SIGSTORE_ROOT_CA_BASE_64
    timestampAuthorities:
    - subject:
        organization: chainguard.dev
        commonName: chainguard-tsa
      uri: https://tsa.enforce.dev
      certChain: |-
         COSIGN_TIMESTAMP_CERTIFICATE_CHAIN_BASE_64
```

With these two resources, we enforce all matching container images must be signed using our sigstore instance and our timestamp authority service.