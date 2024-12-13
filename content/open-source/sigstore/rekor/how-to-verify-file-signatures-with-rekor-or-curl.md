---
title: "How to Verify File Signatures with Rekor or curl"
type: "article"
description: "Use Rekor or curl to verify non-container software artifacts"
lead: "Rekor or curl can verify software artifacts beyond containers"
date: 2022-12-21T15:22:20+01:00
lastmod: 2024-12-12T15:22:20+01:00
draft: false
tags: ["Rekor", "Procedural"]
images: []
menu:
  docs:
    parent: "rekor"
weight: 005
toc: true
---


You can use the `rekor-cli` tool to verify signatures of artifacts other than container images. For example, you can verify the signature of a binary file that has been signed using a keyless signature as part of its release process. By querying the [Rekor transparency log](/open-source/sigstore/rekor/an-introduction-to-rekor/#transparency-log), you can verify that the binary file you downloaded matches the one that was signed using Cosign. If you prefer, you can also query the Rekor API directly using `curl`.

In this tutorial, we'll demonstrate how to verify a binary file using `rekor-cli` and `curl`. We'll use [apko](/open-source/apko/overview/) as an example, since all its releases are signed with Cosign. The methods in this tutorial apply to any blob file that Cosign has signed with a keyless signature.

## Preparation
To follow up with all commands in this tutorial, you need to have `curl` and the `rekor-cli` tool installed. You can install it by following our [How to Install the Rekor CLI](/open-source/sigstore/rekor/how-to-install-rekor/) guide. Alternatively, you can follow the [official docs](https://docs.sigstore.dev/logging/installation/#build-rekor-cli-manually) for instructions on how to build Rekor CLI from source. You also need to have the `jq` utility installed to parse the output of `rekor-cli` and `curl`.

### Download the Example File
We'll use the `apko_0.20.1_linux_amd64.tar.gz` tar archive from the apko [GitHub Release v0.20.1 page](https://github.com/chainguard-dev/apko/releases/tag/v0.20.1) for the examples in this tutorial. You can download the file using `curl` or your browser:

```shell
curl -L -O https://github.com/chainguard-dev/apko/releases/download/v0.20.1/apko_0.20.1_linux_amd64.tar.gz
```

Then, set up a shell variable to store the SHA256 hash of the `apko_0.20.1_linux_amd64.tar.gz` release file:

```sh
SHASUM=$(shasum -a 256 apko_0.20.1_linux_amd64.tar.gz |awk '{print $1}')
```

You can verify that the variable has been set correctly by running:

```shell
echo $SHASUM
```

You should get output similar to this:

```shell
442d8baafc0c3a873b21a3add32f5c65f538fb5cbcf4a4a69ba098a2b730c5d2
```

With this environment variable set up, you can proceed to the rest of this guide.

## Verifying a Binary with `rekor-cli`

We'll now use the `rekor-cli` tool to verify the signature of the `apko_0.20.1_linux_amd64.tar.gz` binary file. First, we'll search the Rekor log for the hash of the binary file. Then, we'll retrieve the Rekor log entry for the hash and extract the signature and public key to verify the binary file.

To search for the hash in the Rekor log using `rekor-cli`, run the following command:

```shell
rekor-cli search --sha "${SHASUM?}"
```
You will receive output like the following:

```
Found matching entries (listed by UUID):
108e9186e8c5677a8d6736bdd79170adf94bd127aea751274d1d62504e88b058af7552d91dea0f26
```

Set a shell variable called `UUID` to the returned entry:

```shell
UUID="108e9186e8c5677a8d6736bdd79170adf94bd127aea751274d1d62504e88b058af7552d91dea0f26"
```

Now you can use the returned UUID to retrieve the associated Rekor log entry:

```shell
rekor-cli get --uuid "${UUID?}"
```

This will return a long payload that you can parse using `jq` in order to extract the relevant fields. You can skip to the [Fetching a Signature and Public Certificate](#fetching-a-signature-and-public-certificate) section to learn how to verify your binary matches what is in the Rekor log.

## Verifying a Binary with `curl`
To query the Rekor API directly for the hash using `curl`, you'll need to make a POST request to the `https://rekor.sigstore.dev/api/v1/index/retrieve` endpoint, passing along the hash as a JSON payload. You can then use the returned UUID to retrieve the associated Rekor log entry.

Run the following command to query the Rekor API for the hash:

```shell
curl -X POST -H "Content-type: application/json" 'https://rekor.sigstore.dev/api/v1/index/retrieve' --data-raw "{\"hash\":\"sha256:$SHASUM\"}"
```
You will get output like this:

```shell
["108e9186e8c5677a8d6736bdd79170adf94bd127aea751274d1d62504e88b058af7552d91dea0f26"]
```

Next, set a shell variable called `UUID` to the returned entry:

```shell
UUID="108e9186e8c5677a8d6736bdd79170adf94bd127aea751274d1d62504e88b058af7552d91dea0f26"
```

Now you can use the returned UUID to retrieve the associated Rekor log entry:

```shell
curl -X GET "https://rekor.sigstore.dev/api/v1/log/entries/${UUID?}"
```

This will return a long payload that you can parse using `jq` in order to extract the relevant fields. To verify the signature and decode the data, you'll also need `base64` and `openssl`.

## Fetching a Signature and Public Certificate

If you would like to extract the signature and public key to verify your binary matches what is in the Rekor log, you will need to parse the output. You will need to use tools like `base64` to decode the data, `jq` to extract the relevant fields, and `openssl` to verify the signature.

### If you're using `rekor-cli`

The following commands will fetch the Rekor entry for a release using `rekor-cli`, parse and extract the signature and public certificate using `jq`, and decode it using `base64`:

```shell
rekor-cli get --uuid "${UUID?}" --format json \
  | jq -r '.Body .HashedRekordObj .signature .content' \
  | base64 -d > apko_0.20.1_linux_amd64.tar.gz.sig
```
```shell
rekor-cli get --uuid "${UUID?}" --format json \
  | jq -r '.Body .HashedRekordObj .signature .publicKey .content' \
  | base64 -d > apko_0.20.1_linux_amd64.tar.gz.crt
```

### If you're using `curl`

The following commands will fetch the Rekor entry for a release using `curl`, parse and extract the signature and public certificate using `jq`, and decode it using `base64`:

```shell
curl -s -X GET "https://rekor.sigstore.dev/api/v1/log/entries/${UUID?}" \
  | jq -r '.[] | .body' \
  | base64 -d |jq -r '.spec .signature .content' \
  | base64 -d > apko_0.20.1_linux_amd64.tar.gz.sig
```

```shell
curl -s -X GET "https://rekor.sigstore.dev/api/v1/log/entries/${UUID?}" \
  | jq -r '.[] | .body' \
  | base64 -d |jq -r '.spec .signature .publicKey .content' \
  | base64 -d > apko_0.20.1_linux_amd64.tar.gz.crt
```

## Verifying a signature using `openssl`

After running both commands from the previous section and whether you used `rekor-cli` or `curl`, you should have two new files in your current directory: `apko_0.20.1_linux_amd64.tar.gz.sig` and `apko_0.20.1_linux_amd64.tar.gz.crt`. These are the signature and public certificate files for the apko release, respectively. We can now use `openssl` to verify the binary file against the signature.

First, extract the public key portion of the `apko_0.20.1_linux_amd64.tar.gz.crt` certificate file:

```shell
openssl x509 -in apko_0.20.1_linux_amd64.tar.gz.crt -noout -pubkey > apko_0.20.1_linux_amd64.tar.gz.pubkey.crt
```

Now you can use `openssl` to verify the signature against your local apko binary. Run the following command:

```shell
openssl sha256 -verify apko_0.20.1_linux_amd64.tar.gz.pubkey.crt -signature apko_0.20.1_linux_amd64.tar.gz.sig apko_0.20.1_linux_amd64.tar.gz
```

If your `apko_0.20.1_linux_amd64.tar.gz` download matches the one that was signed using Cosign, you will receive the following line of output:

```Output
Verified OK
```

This output indicates that your `apko_0.20.1_linux_amd64.tar.gz` version is authentic and was signed by the ephemeral private key corresponding to the public certificate that you retrieved from the Rekor log.
