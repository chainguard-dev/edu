---
title: "How to Install chainctl"
type: "article"
description: "Install the chainctl command line tool to work with Chainguard Enforce and Images"
date: 2022-09-22T15:56:52-07:00
lastmod: 2022-12-13T15:56:52-07:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-enforce-kubernetes"
toc: true
---

> _This documentation is related to Chainguard Enforce. You can request access to the product selecting **Chainguard Enforce for Kubernetes** on the [inquiry form](https://www.chainguard.dev/get-demo?utm_source=docs)._

The Chainguard Enforce command line interface (CLI) tool, `chainctl`, will help you interact with the account model that Chainguard Enforce provides, and enable you to make queries into the state of your clusters and policies registered with the platform.

The tool uses the familiar `<context> <noun> <verb>` style of CLI interactions. For example, to list groups within the context of Chainguard Identity and Access Management (IAM), you can run `chainctl iam groups list` to receive relevant output.

Before we begin, let’s move into a temporary directory that we can work in. Be sure you have curl installed, which you can achieve through visiting the [curl download docs](https://curl.se/download.html) for your relevant operating system.

```sh
mkdir ~/tmp && cd $_
```

There are currently two ways to install `chainctl`, depending on your operating system and preferences.

## Install `chainctl` with Homebrew

You can install `chainctl` for macOS and Linux with the package manager [Homebrew](https://brew.sh/).

First, use `brew tap` to bring in Chainguard's repositories.

```sh
brew tap chainguard-dev/tap
```

Next, install `chainctl` with Homebrew.

```sh
brew install chainctl
```

You are now ready to use the `chainctl` command. You can verify that it works correctly in the final section of this guide.

## Install with `curl`

A platform agnostic approach to installing `chainctl` is through using `curl`, which you can achieve with the following command.

```bash
curl -o chainctl "https://dl.enforce.dev/chainctl/latest/chainctl_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m)"
```

Move `chainctl` into your `/usr/local/bin` directory and elevate its permissions so that it can execute as needed.

```sh
sudo install -o $UID -g $GID 0755 chainctl /usr/local/bin/chainctl
```

Finally, alias its path so that you can use `chainctl` on the command line.

```sh
alias chainctl=/usr/local/bin/chainctl
```

At this point, you'll be able to use the `chainctl` command.

## Verify installation

You can verify that everything was set up correctly by checking the `chainctl` version.

```sh
chainctl version
```

You should receive output similar to the following.

```
   ____   _   _      _      ___   _   _    ____   _____   _
  / ___| | | | |    / \    |_ _| | \ | |  / ___| |_   _| | |
 | |     | |_| |   / _ \    | |  |  \| | | |       | |   | |
 | |___  |  _  |  / ___ \   | |  | |\  | | |___    | |   | |___
  \____| |_| |_| /_/   \_\ |___| |_| \_|  \____|   |_|   |_____|
chainctl: Chainguard Control

GitVersion:    0.1.42
GitCommit:     badf10d2d89c83c6f1366008ffc3936d1e4c36f4
GitTreeState:  clean
BuildDate:     2022-12-12T22:10:55Z
GoVersion:     go1.19.4
Compiler:      gc
Platform:      darwin/arm64
```

If you received different output, check your bash profile to make sure that your system is using the expected PATH. 

### Verifying the `chainctl` binary with Cosign and Rekor

All `chainctl` binaries are released with [keyless signatures using Cosign](https://edu.chainguard.dev/open-source/sigstore/cosign/an-introduction-to-cosign/#keyless-signing). You can verify the signature for a `chainctl` binary using the `cosign` tool directly, or by calculating the SHA256 hash of the release and finding the corresponding Rekor transparency log entry.

The following steps will work for both `curl` and `brew` installations of `chainctl`.

#### Verifying `chainctl` using Cosign keyless signatures

To verify a `chainctl` binary using Cosign, first ensure you have the latest versin of Cosign installed by following our [How to Install Cosign guide](https://edu.chainguard.dev/open-source/sigstore/cosign/how-to-install-cosign/).

Next, run `chainctl version --json` to output the version information. You should receive output like the following:

```json
{
  "gitVersion": "0.1.42",
  "gitCommit": "badf10d2d89c83c6f1366008ffc3936d1e4c36f4",
  "gitTreeState": "clean",
  "buildDate": "2022-12-12T22:10:55Z",
  "goVersion": "go1.19.4",
  "compiler": "gc",
  "platform": "darwin/arm64"
}
```

Now set an environment variable to the version shown in the `gitVersion` field, which is `0.1.42` in this example.

```sh
CHAINCTL_VERSION="0.1.42"
```

Run the following commands to create two URL environment variables. These URLs will point to the correct version of the `chainctl` signature and public certificate files respectively:

```sh
SIGNATURE_URL="https://dl.enforce.dev/chainctl/${CHAINCTL_VERSION?}/chainctl_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m).sig"
CERTIFICATE_URL="https://dl.enforce.dev/chainctl/${CHAINCTL_VERSION?}/chainctl_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m).cert.pem"
```

Check your environment variables for correctness using `echo`:

```sh
echo "$SIGNATURE_URL\n$CERTIFICATE_URL\n$CHAINCTL_VERSION"
```

You should receive output like the following, which shows the correct version, operating system, and CPU architecture for your system values in the computed URLs:

```
https://dl.enforce.dev/chainctl/0.1.42/chainctl_darwin_arm64.sig
https://dl.enforce.dev/chainctl/0.1.42/chainctl_darwin_arm64.cert.pem
0.1.42
```

Now you can verify the binary by running the following `cosign verify-blob` command:

```sh
COSIGN_EXPERIMENTAL=1 cosign verify-blob --signature $SIGNATURE_URL --certificate $CERTIFICATE_URL $(which chainctl)
```

You should receive the following output:

```
tlog entry verified with uuid: 1a481ce6eeee6306dffbba9fef701a21623ca0b07780b32b009395c905f7df7a index: 8959219
Verified OK
```

If you the signature or certificate URLs are incorrect, if there is a problem with your `chainctl` binary, or if your `$CHAINCTL_VERSION` doesn't match the version output by `chainctl version --json`, you will receive an error like the following:

```
Error: verifying blob [/usr/local/bin/chainctl]: invalid signature when validating ASN.1 encoded signature
. . .
```

Check the environment variables that you set for correctness, and ensure that the path reported by `$(which chainctl)` points to the version of `chainctl` that you downloaded and installed. 

For completeness, you can use the following script to check `chainctl` binaries using Cosign. It is a combination of the previous steps into one script with some additional checks for missing tools, and error handling.

```bash
#!/bin/bash
set -Eeuo pipefail
export COSIGN_EXPERIMENTAL=1

trap 'cmd_error $LINENO "${BASH_COMMAND}"' ERR
function cmd_error() {
  echo "error running command on line $1"
  echo "command is: $2"
}

function check_signature {
    chainctl_version=$(chainctl version 2>&1 |awk '/GitVersion/ {print $2}')
    chainctl_os_arch="chainctl_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m)"
    sig_url="https://dl.enforce.dev/chainctl/${chainctl_version?}/${chainctl_os_arch?}.sig"
    cert_url="https://dl.enforce.dev/chainctl/${chainctl_version?}/${chainctl_os_arch?}.cert.pem"
    cosign verify-blob --signature "${sig_url?}" --cert "${cert_url?}" "$(command -v chainctl)"
}

function check_executable {
    status=0
    executable_name="${1?}"
    command -v "${executable_name?}" > /dev/null || status=$?
    if [[ "${status?}" -ne 0 ]]; then
        echo "${executable_name?} not found"
        exit 1
    fi
}

check_executable "cosign"
check_executable "chainctl"
check_signature
```

#### Verifying `chainctl` using the Rekor Transparency Log

You can look up the Rekor entry for your version of `chainctl` by searching the log for the SHA256 hash of `chainctl`. You can use the `rekor-cli` tool or `curl` to find matching Rekor entries. If you need to install `rekor-cli`, follow our guide [How to Install the Rekor CLI](https://edu.chainguard.dev/open-source/sigstore/rekor/how-to-install-rekor/). When using either tool, ensure that you have the `jq` utility installed so that you can parse their output.

To search Rekor, set a shell variable to the SHA256 hash of your `chainctl` binary:

```sh
SHASUM=$(shasum -a 256 $(which chainctl) |awk '{print $1}')
```

If you are using the `rekor-cli` client, search for the hash with the following command:

```sh
rekor-cli search --sha "${SHASUM?}"
```

If you are using `curl`, run the following:

```sh
curl -X POST -H "Content-type: application/json" 'https://rekor.sigstore.dev/api/v1/index/retrieve' --data-raw "{\"hash\":\"sha256:$SHASUM\"}"
```

If there is an entry for your version of `chainctl` you will receive output like the following:

```
# rekor-cli output
Found matching entries (listed by UUID):
24296fb24b8ad77a1a481ce6eeee6306dffbba9fef701a21623ca0b07780b32b009395c905f7df7a

# curl output
["24296fb24b8ad77a1a481ce6eeee6306dffbba9fef701a21623ca0b07780b32b009395c905f7df7a"]
```

Set a shell variable called `UUID` to the returned entry:

```sh
UUID="24296fb24b8ad77a1a481ce6eeee6306dffbba9fef701a21623ca0b07780b32b009395c905f7df7a"
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
  | base64 -d > /tmp/chainctl.sig
rekor-cli get --uuid "${UUID?}" --format json \
  | jq -r '.Body .HashedRekordObj .signature .publicKey .content' \
  | base64 -d > /tmp/chainctl.cert.pem
```

##### Fetch a signature and public certificate using `curl`

The following commands will fetch the Rekor entry for a release using `curl`, parse and extract the signature and public certificate using `jq`, and decode it using `base64`:

```sh
curl -s -X GET "https://rekor.sigstore.dev/api/v1/log/entries/${UUID?}" \
  | jq -r '.[] | .body' \
  | base64 -d |jq -r '.spec .signature .content' \
  | base64 -d > /tmp/chainctl.sig
curl -s -X GET "https://rekor.sigstore.dev/api/v1/log/entries/${UUID?}" \
  | jq -r '.[] | .body' \
  | base64 -d |jq -r '.spec .signature .publicKey .content' \
  | base64 -d > /tmp/chainctl.cert.pem
```

##### Verifying a signature using `openssl`

Now that you have downloaded the signature and public certificate corresponding to your `chainctl` version, you can verify the binary's signature using `openssl`.

First, extract the public key portion of the `/tmp/chainctl.cert.pem` certificate file:

```sh
openssl x509 -in /tmp/chainctl.cert.pem -noout -pubkey > /tmp/chainctl.pubkey.pem
```

Now you can use `openssl` to verify the signature against your local `chainctl` binary. Run the following command:

```sh
openssl dgst -sha256 -verify /tmp/chainctl.pubkey.pem -signature /tmp/chainctl.sig $(which chainctl)
```

If your `chainctl` binary matches the one that was signed using Cosign, you will receive the following line of output:

```
Verified OK
```

This output indicates that your `chainctl` version is authentic and was signed by the ephemeral private key corresponding to the public certificate that you retrieved from the Rekor log.

## Updating `chainctl`

When your version of `chainctl` is a few weeks old or older, you may consider updating it to make sure that your version is the most up to date. You can update `chainctl` by running the `update` command.

```sh
sudo chainctl update
```

Keeping `chainctl` up to date will ensure that you are using the most up to date version.
