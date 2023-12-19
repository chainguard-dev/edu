---
date: 2023-12-19T19:01:04Z
title: "chainctl sigstore ca create"
slug: chainctl_sigstore_ca_create
url: /chainguard/chainctl/chainctl-docs/chainctl_sigstore_ca_create/
draft: false
tags: ["chainctl", "Reference", "Product"]
images: []
type: "article"
toc: true
---
## chainctl sigstore ca create

Create a certificate authority instance.

```
chainctl sigstore ca create --group GROUP_NAME | GROUP_ID {--ca googleca --googleca-ref RESOURCE | --ca kmsca --kms-key-ref RESOURCE --kms-cert-chain CERT} [--description DESCRIPTION] [--name NAME] [--output table|json|id] [flags]
```

### Options

```
      --ca string               certificate authority type: [ kmsca | googleca ]
  -d, --description string      The description of the resource.
      --generate-cert-chain     [experimental] generate a root certificate with a KMS key for temporary testing or experimentation
      --googleca-ref string     CA service resource, in the format projects/<project>/locations/<location>/<name>
      --group string            The parent group name or id of the sigstore instance.
  -h, --help                    help for create
      --kms-cert-chain string   Path to file containing PEM-encoded root certificate and chain
      --kms-key-ref string      KMS key resource, prefixed with gcpkms://
  -n, --name string             Given name of the resource.
```

### Options inherited from parent commands

```
      --api string                   The url of the Chainguard platform API. (default "https://console-api.enforce.dev")
      --audience string              The Chainguard token audience to request. (default "https://console-api.enforce.dev")
      --config string                A specific chainctl config file. Uses CHAINCTL_CONFIG environment variable if a file is not passed explicitly.
      --console string               The url of the Chainguard platform Console. (default "https://console.enforce.dev")
      --issuer string                The url of the Chainguard STS endpoint. (default "https://issuer.enforce.dev")
  -o, --output string                Output format. One of: ["", "json", "id", "table", "terse", "tree", "wide"]
      --timestamp-authority string   The url of the Chainguard Timestamp Authority endpoint. (default "https://tsa.enforce.dev")
  -v, --v int                        Set the log verbosity level.
```

### SEE ALSO

* [chainctl sigstore ca](/chainguard/chainctl/chainctl-docs/chainctl_sigstore_ca/)	 - Sigstore commands related to certificate authorities

