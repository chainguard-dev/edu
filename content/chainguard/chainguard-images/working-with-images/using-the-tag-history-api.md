---
title: "Using the Tag History API"
linktitle: "Tag History API"
aliases:
- /chainguard/chainguard-images/using-the-tag-history-api
- /chainguard/chainguard-images/images-features/using-the-tag-history-api
type: "article"
description: "Learn how to use the Chainguard Images Tag History API to fetch the tag history of image variants."
date: 2023-05-26T08:49:31+00:00
lastmod: 2024-08-02T15:22:20+01:00
draft: false
tags: ["Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "images-features"
weight: 040
toc: true
---

Chainguard Images have automated nightly builds, which ensures our images are always fresh including any recent patches and updated software. Even though it is important to keep your base images always updated, there will be situations where you'll want to keep using an older build to make sure nothing will change in your container environment until you feel it's safe to update.

For cases like this, it is useful to point your Dockerfile to use a specific **image digest** as base image.

An image digest is a unique identifier that is generated for each and every image build. Digests always change, even when the contents of the image remain the same.

If you have a container environment that was working fine but suddenly breaks with a new build, using a previous image build version by declaring an image digest instead of a tag is a way to keep things up and running until you're able to assert that a new version of a container environment works as expected with your application.


## Obtaining a Registry Token

Before making API calls, you'll need to generate a token within the [Chainguard Registry](/chainguard/chainguard-registry/overview/).

The Registry API endpoint for obtaining the token is:

```
https://cgr.dev/token?scope=repository:chainguard/IMAGE_NAME:pull
```

Where `IMAGE_NAME` is the name of the image that you want to pull the tag history from. It's worth noting that the token is only valid for pulling the history of that specific image.

For public images (tagged as `latest` or `latest-dev`), you can request a registry token anonymously, without providing any pre-existing auth.

The following command will obtain a token for the **Python** image and register a variable called `tok` with the resulting value, which you can use in a subsequent command to obtain the tag history:

```shell
tok=$(curl "https://cgr.dev/token?scope=repository:chainguard/python:pull" \
  | jq -r .token)
```

For images that are not public, you'll need to exchange your Chainguard token for a registry token. This assumes you've set up authentication with [chainctl auth configure-docker](https://edu.chainguard.dev/chainguard/chainguard-registry/authenticating/)):

```shell
tok=$(curl -H "Authorization: Bearer \
  $(echo 'cgr.dev' | docker-credential-cgr get)" \
  -v "https://cgr.dev/token?scope=repository:chainguard/python:pull" \
  | jq -r .token)
```

To make sure your token is set, you can run the following command:

```shell
echo $tok
```

And you should get a long string token as output.

You should now be ready to call the API, either manually or programmatically.

## Calling the API

Once you have your token available, you can run a `curl` query passing on your token within an `Authorization: bearer` header to the following endpoint:

```
https://cgr.dev/v2/chainguard/IMAGE_NAME/_chainguard/history/IMAGE_TAG
```

Where `IMAGE_NAME` is the name of the image, for instance: `python`, and `IMAGE_TAG` is the tag that you want to pull history from.

For example, this is how you can fetch the tag history of the **python:latest** Chainguard image using `curl` on the command line:

```shell
curl -H "Authorization: Bearer $tok" \
  https://cgr.dev/v2/chainguard/python/_chainguard/history/latest | jq
```

You should get output like the following:

```
{
  "history": [
	{
  	"updateTimestamp": "2023-05-12T13:46:10.555Z",
  	"digest": "sha256:81c334de6dd4583897f9e8d0691cbb75ad41613474360740824d8a7fa6a8fecb"
	},
	{
  	"updateTimestamp": "2023-05-12T20:50:19.702Z",
  	"digest": "sha256:a8724b7a80cae14263a3b55f7acb5d195fcbb24afbc8067aa5198aa2a9131cde"
	},
	...

  ]
}
```

## Using the start and end parameters

In some cases it may be helpful to specify digests created in a given time period rather than querying the entire history of a tag. For this, you can use the `start` and `end` parameters. These optional parameters can be added to requests to the Tag History API and should be specified in the `IS0 8601` format.

To illustrate how to query digests of an image created in the last week, first create a local shell variable named `timestamp`. On Ubuntu, you would create the `timestamp` variable as follows:

```shell
timestamp=$(date -d "-1 week" +%Y-%m-%dT%H:%M:%SZ)
```

And on Wolfi, you would create it like this:

```shell
timestamp=$(date -d @$(( $(date +%s ) - 604800 )) +%Y-%m-%dT%H:%M:%SZ)
```

Then to query digests of the **python:latest** Chainguard image created in the last week you would run a command like the following:

```shell
curl -s -H "Authorization: Bearer $tok" \
	"https://cgr.dev/v2/chainguard/python/_chainguard/history/latest?start=${timestamp}" | jq
```

To query digests of the **python:latest** Chainguard image created before 2024, first create a new `timestamp` variable like this:

```shell
timestamp="2024-01-01T00:00:00Z"
```

Then run the query like this:

```shell
curl -s -H "Authorization: Bearer $tok" \
	"https://cgr.dev/v2/chainguard/python/_chainguard/history/latest?end=${timestamp}" | jq
```

Both of these examples filter the `curl` command's output through [`jq`](https://jqlang.github.io/jq/), a useful tool for processing JSON on the command line.

## Page limit

Please note that the Tag History API will return a maximum of 1000 records on a single request. For tags with many digests, since the oldest digests are ordered first, it may be necessary to specify the timestamp of the desired digests - for this, the `start` and `end` parameters may be used as specified above.

## Using Image Digests within a Dockerfile

Setting up your Dockerfile to use an older build is a matter of modifying your `FROM` line to use an image digest instead of a tag. For instance, let's say you want to make sure you keep using the current latest build of the Python image. In a previous section of this page we obtained the tag history of the Python image, and the most recent build digest is listed as `sha256:81c334de6dd4583897f9e8d0691cbb75ad41613474360740824d8a7fa6a8fecb`. With that information, you can edit your Dockerfile and replace:

```
FROM cgr.dev/chainguard/python:latest
```

With:

```
FROM cgr.dev/chainguard/python@sha256:81c334de6dd4583897f9e8d0691cbb75ad41613474360740824d8a7fa6a8fecb
```

And your image will then be locked into that specific build of the `python:latest` image variant.


