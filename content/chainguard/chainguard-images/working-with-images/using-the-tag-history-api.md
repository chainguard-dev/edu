---
title: "Using the Tag History API"
linktitle: "Tag History API"
aliases:
- /chainguard/chainguard-images/using-the-tag-history-api
- /chainguard/chainguard-images/images-features/using-the-tag-history-api
type: "article"
description: "Learn how to use the Chainguard Images Tag History API to fetch the tag history of image variants."
date: 2023-05-26T08:49:31+00:00
lastmod: 2024-03-21T15:22:20+01:00
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

Before making API calls, you'll need to generate a token within the [Chainguard Registry](/chainguard/chainguard-images/registry/overview/).

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

For images that are not public, you'll need to exchange your Chainguard token for a registry token. This assumes you've set up authentication with [chainctl auth configure-docker](https://edu.chainguard.dev/chainguard/chainguard-images/registry/authenticating/):

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

## Accessing the History API for Enterprise Images

If you are a customer who would like to access the history API for Enterprise images, you must create credentials to access the API with curl and Bash.

### Create Credentials

You'll need to use credentials to access the Registry. First, authenticate with `chainctl`.

```sh
chainctl auth login
```

Next, retrieve your Organization's UIDP and store it in a variable.

```sh
chainctl iam organizations ls -o table
```
```
export ORG_ID="cc...52"
```

At this point, you can create a token for 30 days. Note that 30 days is the default, the max you can initialize a token for is 1 year.

```sh
chainctl auth configure-docker --pull-token --parent $ORG_ID --ttl 720h
```

If you would like to use this pull token in another environment, run this command with Docker.

```sh
docker login "cgr.dev" --username "cc..96" --password "eyJ...X34"
```

Be sure to keep a copy of the username and password created.

### Optional: Storing Credentials

You can use the username and password you just created if required. However, Docker's default functionality is to encode these credentials in base64 and then store them within `~/.docker/config.json`.

To set that up, following the previous example, replace the username and password value, keeping the colon (`:`) to separate the values.

```sh
echo -n "username:password" | base64
Y2M...Wc=
```

Add the base64 encoded value to `~/.docker/config.json` with the following format:

```sh
{
  "auths": {
    "cgr.dev": {
      "auth": "Y2M...Wc="
    }
  }
}
```

You can review more about Docker Configs from the [official Docker docs](https://docs.docker.com/engine/swarm/configs/).

### Access the History API with curl and Bash

Now that we have the credentials, we can use curl and Bash to access the endpoints (the following example uses jq as well). Here, you will replace `private-registry.com/apko` with your relevant Registry and Image information.

```sh
IMAGE=private-registry.com/apko
USERNAME="cc..96"
PASSWORD="eyJ...X34"
export TOKEN=$(echo -n "${USERNAME}:${PASSWORD}" | base64 | tr -d '\n\r')
curl -s -H "Authorization: Bearer \
  $(curl -s -H "Authorization: Basic $TOKEN" \
  "https://cgr.dev/token?scope=repository:${IMAGE}:pull" | jq -r .token)" \
  "https://cgr.dev/v2/${IMAGE}/_chainguard/history/latest" | jq .
```

If you have set a `~/.docker/config.json` file within the optional step, you can run the following.

```sh
IMAGE=private-registry.com/apko
curl -s -H "Authorization: Bearer \
  $(curl -s -H "Authorization: Basic \
  $(jq -r ".auths[\"cgr.dev\"].auth" < ~/.docker/config.json)" \
  "https://cgr.dev/token?scope=repository:${IMAGE}:pull" | jq -r .token)" \
  "https://cgr.dev/v2/${IMAGE}/_chainguard/history/latest" | jq .
```

Again, you would replace `private-registry.com/apko` with your relevant Registry and Image information.

## Images and Tags

Public Chainguard Images are available at no cost to users, and do not require authentication. This gives access to the `latest` and `latest-dev` tags of our public images. Other versions and tags are available through subscription to our paid enterprise images, featuring enterprise-grade patching SLAs and customer support.

To learn more about public and enterprise images, check our [Images FAQ page](/chainguard/chainguard-images/faq/#what-options-do-i-have-to-use-chainguard-images) about catalog tiers.
