---
title: "Using the Image Diff API"
type: "article"
description: "Learn how to use the Chainguard Images Diff API to compare changes between image versions."
date: 2023-12-10T08:49:31+00:00
lastmod: 2024-01-22T08:49:31+00:00
draft: false
tags: ["Chainguard Images", "Product", "API"]
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 450
toc: true
---


The Chainguard Images Diff API generates a JSON-formatted list of package additions, removals, and detected CVEs in Chainguard Images. It is intended to provide an authenticated, machine readable, formatted list of changes between two Chainguard Image builds. Combined with the [Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/), you can use the Diff API to compare arbitrary builds of an Image over time and programmatically detect changes that might require gating a release or modifying your application code.

This guide will cover:

1. How to get an authentication token to query the Diff API
2. Identifying Image digests in a repository for comparison
3. Making authenticated API calls using `curl` and programmatically using Go
4. Parsing the results of an API call

## Prerequisites

To get started there are a few prerequisites that you will need to install.

1. First is `chainctl` to authenticate to the Chainguard Registry. Our [How to Install chainctl guide](/chainguard/administration/how-to-install-chainctl/) lists different ways to install it. Ensure that you have the [chainctl credential helper](/chainguard/chainguard-registry/authenticating/#authenticating-with-the-chainctl-credential-helper) configured as well.
2. The next tool is `crane`, which you will use to interact with the Chainguard Registry. Follow the [crane installation](https://github.com/google/go-containerregistry/blob/main/cmd/crane/README.md#installation) guide that matches your operating system.
3. You will also need `curl` or a programming language of your choice to make authenticated API calls. There is an [example using Go](#making-a-request-programmatically-to-the-diff-api-using-go) at the end of this guide.
4. Finally, the `jq` is useful to parse and filter the resulting JSON output from the API on the command line.

With these tools in place, you can begin gathering the information that you need to authenticate to and query the Diff API.

## Authenticating and Getting a Token

To get started, ensure you are authenticated to the Registry using the `chainctl auth login` command. Then locate your authentication token and create a shell variable for it.

If you are using Linux, run the following:

```sh
TOKEN=$(cat ~/.cache/chainguard/https\:--console-api.enforce.dev/oidc-token)
```

If you are using macOS, run the following:

```sh
TOKEN=$(cat ~/Library/Caches/chainguard/https:--console-api.enforce.dev/oidc-token)
```

Note that if at any point in this tutorial you receive an error like the following, your token has expired. Log in and set your `$TOKEN` shell variable again:

```
{"code":16, "message":"failed to verify token", "details":[]}
```

For the purposes of this guide, we will use the `public-images` Chainguard IAM group. Set an environment variable corresponding to the group's [UIDP](/chainguard/administration/cloudevents/events-reference/#uidp-identifiers), which will be used later on:

```sh
GROUP_UIDP=$(chainctl iam group describe public-images -ojson |jq -r '.id')
```

If you are using a private registry, be sure to substitute your IAM group name in place of `public-images` to use your specific private group UIDP identifier in your subsequent commands.

## Getting Image Digests to Compare

Now you will need to find Image digests to compare. You can compare any two arbitrary digests using the API. In this example we will use the public `cgr.dev/chainguard/nginx` repository and find digests for the `latest` and `latest-dev` tags. You can also compare Image digests for the same tag by combining data from the [Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/).

The first digest in this example will be referred to as the `FROM_DIGEST`, and the second comparison Image as `TO_DIGEST`.

Begin by creating a shell variable to hold the repository URL:

```sh
REPO_URL="cgr.dev/chainguard/nginx"
```

If you are using a private registry, be sure to replace `cgr.dev/chainguard/nginx` with your relevant private Chainguard Registry and repository name as required.

Now run the following `crane` command to get a list of tags contained in the public `cgr.dev/chainguard/nginx` repository:

```sh
crane ls "${REPO_URL}" --omit-digest-tags
```

You will receive output like the following:

```
latest
latest-dev
next
```

Since we will compare the `latest` and `latest-dev` Images in this guide, run the following to record their `digest` values as shell variables for reuse:

```sh
FROM_DIGEST=$(crane digest --platform "linux/amd64" "${REPO_URL}:latest")
TO_DIGEST=$(crane digest --platform "linux/amd64" "${REPO_URL}:latest-dev")
```

If you are using a different platform like `linux/arm64`, substitute it into the `crane` commands.

Now you can make a request to the Diff API using `curl` or programmatically with a language of your choice.

## Making a Request to the Diff API Using curl

To make API requests to the Diff API using `curl`, set a shell variable to the name of the Image repository:

```sh
REPO_NAME=$(echo $REPO_URL | cut -d'/' -f3)
```

Now you can run the following command to record the repository UIDP identifier as a variable:

```sh
REPO_UIDP=$(curl -s -X GET -H "Authorization: Bearer $TOKEN" \
  "https://console-api.enforce.dev/registry/v1/repos?name=${REPO_NAME}" | \
  jq -r ".items[] | select(.id | startswith(\"${GROUP_UIDP}\")) | .id")
```

With all of these variables set, you can call the Diff API with the following command:

```sh
curl -s -X GET -H \
  "Authorization: Bearer $TOKEN" \
  "https://console-api.enforce.dev/registry/v1/repos/${REPO_UIDP}/diff?from_digest=${FROM_DIGEST}&to_digest=${TO_DIGEST}" | \
  jq -r
```

You will receive output like the following:

```
. . .
{
"packages": {
  "added": [
    . . .
    {
      "name": "bash",
      "version": "5.2.21-r0",
      "reference": "pkg:apk/wolfi/bash@5.2.21-r0?arch=x86_64"
    },
    {
      "name": "busybox",
      "version": "1.36.1-r2",
      "reference": "pkg:apk/wolfi/busybox@1.36.1-r2?arch=x86_64"
    },
    . . .
  "removed": [
    . . .
  ]
},
"vulnerabilities": {
  . . .
}
}
```

In this example output, the list of `added` packages include things like `bash` and other helpful utilities that are packaged in the nginx development Image. If there are any vulnerabilities detected in an Image they will be listed in that section of the output.

## Making a Request Programmatically to the Diff API Using Go

If you would like to query the Diff API programmatically, there is an example Go application hosted in our [platform-examples](https://github.com/chainguard-dev/platform-examples/tree/main/image-diff) GitHub repository. The example uses the [Chainguard SDK](https://pkg.go.dev/chainguard.dev/sdk) and is a good way to learn how to interact with the API through a declarative approach.

Clone the repository, or copy the code manually. Again we're using the `cgr.dev/chainguard/nginx` Image as an example:

```sh
git clone https://github.com/chainguard-dev/platform-examples
cd platform-examples/image-diff
```

Following that, set some shell variables:

```sh
REPO_NAME=nginx
REPO_URL="cgr.dev/chainguard/${REPO_NAME}"
FROM_DIGEST=$(crane digest --platform "linux/amd64" "${REPO_URL}:latest")
TO_DIGEST=$(crane digest --platform "linux/amd64" "${REPO_URL}:latest-dev")
```

Now run the `go get` and `go run` commands to build and execute the example program:

```sh
go get
go run . $REPO_NAME $FROM_DIGEST $TO_DIGEST |jq -r
```

If you receive an error about a missing `oidc-token`, login with `chainctl auth login` and try running the program again.

You will receive output like the following:

```
. . .
{
"packages": {
  "added": [
    . . .
    {
      "name": "bash",
      "version": "5.2.21-r0",
      "reference": "pkg:apk/wolfi/bash@5.2.21-r0?arch=x86_64"
    },
    {
      "name": "busybox",
      "version": "1.36.1-r2",
      "reference": "pkg:apk/wolfi/busybox@1.36.1-r2?arch=x86_64"
    },
    . . .
  "removed": [
    . . .
  ]
},
"vulnerabilities": {
  . . .
}
}
```

Again, replace `chainguard/nginx` with your relevant private registry and Image name as required. As with the `curl` example, you can also compare Image digests for the same tag by combining data from the [Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/).
