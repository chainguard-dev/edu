---
title: "How to Verify File Signatures with Rekor or curl"
type: "article"
description: "Use Rekor or curl to verify non-container software artifacts"
lead: "Rekor or curl can verify software artifacts beyond containers"
date: 2022-12-21T15:22:20+01:00
lastmod: 2022-12-21T15:22:20+01:00
draft: false
tags: ["Rekor", "Procedural"]
images: []
menu:
  docs:
    parent: "rekor"
weight: 005
toc: true
---

The `rekor-cli` tool or `curl` can be used to verify anything with a signature on a [Rekor transparency log](/open-source/sigstore/rekor/an-introduction-to-rekor/#transparency-log). This tutorial assumes you have the `rekor-cli` tool installed, which you can achieve by following our [How to Install the Rekor CLI](/open-source/sigstore/rekor/how-to-install-rekor/) guide. When verifying a signature using either tool, ensure that you have the `jq` utility installed so that you can parse their output.

We’ll verify a binary artifact, in this case, a copy of [apko](/open-source/apko/overview/), which is a tool for building container images using a declarative language based on YAML. The methods in this tutorial apply to any blob file that Cosign has signed with a keyless signature.

### Verifying a binary with rekor-cli

All apko releases are released with [keyless signatures using Cosign](/open-source/sigstore/cosign/an-introduction-to-cosign/#keyless-signing). You can verify the signature for an apko release by searching for the SHA256 hash of the release and finding the corresponding Rekor transparency log entry.

We'll use the `apko_0.6.0_linux_arm64.tar.gz` tar archive from the apko [GitHub Release v0.6.0 page](https://github.com/chainguard-dev/apko/releases/tag/v0.6.0) in this example.

First, download the file using curl or your browser:

```sh
curl -L -O https://github.com/chainguard-dev/apko/releases/download/v0.6.0/apko_0.6.0_linux_amd64.tar.gz
```






To search Rekor, set a shell variable to the SHA256 hash of the `apko_0.6.0_linux_amd64.tar.gz` release file:

```sh
SHASUM=$(shasum -a 256 apko_0.6.0_linux_amd64.tar.gz |awk '{print $1}')
```

If you are using the `rekor-cli` client, search for the hash with the following command:

```sh
rekor-cli search --sha "${SHASUM?}"
```

If you are using `curl`, run the following:

```sh
curl -X POST -H "Content-type: application/json" 'https://rekor.sigstore.dev/api/v1/index/retrieve' --data-raw "{\"hash\":\"sha256:$SHASUM\"}"
```

You will receive output like the following:

```
# rekor-cli output
Found matching entries (listed by UUID):
24296fb24b8ad77a9ec23abb6326ebbaa6932f720847080e8f5e0b2925a1643b63962691917c8137

# curl output
["24296fb24b8ad77a9ec23abb6326ebbaa6932f720847080e8f5e0b2925a1643b63962691917c8137"]
```

Set a shell variable called `UUID` to the returned entry:

```sh
UUID="24296fb24b8ad77a9ec23abb6326ebbaa6932f720847080e8f5e0b2925a1643b63962691917c8137"
```

Now you can use the returned UUID to retrieve the associated Rekor log entry. If you are using `rekor-cli` run the following:

```sh
rekor-cli get --uuid "${UUID?}"
```

If you are using `curl` then run this command:

```sh
curl -X GET "https://rekor.sigstore.dev/api/v1/log/entries/${UUID?}"
```

In both cases, if you would like to extract the signature and public key to verify your binary matches what is in the Rekor log, you will need to parse the output. You will need to use tools like `base64` to decode the data, `jq` to extract the relevant fields, and `openssl` to verify the signature. 

##### Fetch a signature and public certificate using `rekor-cli`

The following commands will fetch the Rekor entry for a release using `rekor-cli`, parse and extract the signature and public certificate using `jq`, and decode it using `base64`:

```sh
rekor-cli get --uuid "${UUID?}" --format json \
  | jq -r '.Body .HashedRekordObj .signature .content' \
  | base64 -d > apko_0.6.0_linux_amd64.tar.gz.sig
rekor-cli get --uuid "${UUID?}" --format json \
  | jq -r '.Body .HashedRekordObj .signature .publicKey .content' \
  | base64 -d > apko_0.6.0_linux_amd64.tar.gz.crt
```

##### Fetch a signature and public certificate using `curl`

The following commands will fetch the Rekor entry for a release using `curl`, parse and extract the signature and public certificate using `jq`, and decode it using `base64`:

```sh
curl -s -X GET "https://rekor.sigstore.dev/api/v1/log/entries/${UUID?}" \
  | jq -r '.[] | .body' \
  | base64 -d |jq -r '.spec .signature .content' \
  | base64 -d > apko_0.6.0_linux_amd64.tar.gz.sig
curl -s -X GET "https://rekor.sigstore.dev/api/v1/log/entries/${UUID?}" \
  | jq -r '.[] | .body' \
  | base64 -d |jq -r '.spec .signature .publicKey .content' \
  | base64 -d > apko_0.6.0_linux_amd64.tar.gz.crt
```

##### Verifying a signature using `openssl`

Now that you have downloaded the signature and public certificate corresponding to your `chainctl` version, you can verify the binary's signature using `openssl`.

First, extract the public key portion of the `apko_0.6.0_linux_amd64.tar.gz.crt` certificate file:

```sh
openssl x509 -in apko_0.6.0_linux_amd64.tar.gz.crt -noout -pubkey > apko_0.6.0_linux_amd64.tar.gz.pubkey.crt
```

Now you can use `openssl` to verify the signature against your local `chainctl` binary. Run the following command:

```sh
openssl sha256 -verify apko_0.6.0_linux_amd64.tar.gz.pubkey.crt -signature apko_0.6.0_linux_amd64.tar.gz.sig apko_0.6.0_linux_amd64.tar.gz
```

If your `apko_0.6.0_linux_amd64.tar.gz` download matches the one that was signed using Cosign, you will receive the following line of output:

```
Verified OK
```

This output indicates that your `apko_0.6.0_linux_amd64.tar.gz` version is authentic and was signed by the ephemeral private key corresponding to the public certificate that you retrieved from the Rekor log.
