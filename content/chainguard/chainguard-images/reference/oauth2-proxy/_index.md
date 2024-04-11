---
title: "Image Overview: oauth2-proxy"
linktitle: "oauth2-proxy"
type: "article"
layout: "single"
description: "Overview: oauth2-proxy Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu: 
  docs: 
    parent: "images-reference"
weight: 500
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/oauth2-proxy/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/oauth2-proxy/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/oauth2-proxy/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/oauth2-proxy/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[OAuth2 Proxy](https://oauth2-proxy.github.io/oauth2-proxy/) is a reverse proxy that provides authentication with Google, Azure, OpenID Connect and many more identity providers.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/oauth2-proxy:latest
```


<!--body:start-->
## Use It!

This section provides a brief overview of how you can use Chainguard's `oauth2-proxy` Image to set up a proxy that can intercept a call to a specified endpoint. A complete end-to-end test would require a GitHub account (or an account with another OIDC Auth provider), a trusted domain, and an OAuth application; this example will be useful to test that the image works but it will not be able to verify authentication or properly redirect users.

Run the following command.

```shell
docker run --detach --name oidc-test -p 8080:8080 cgr.dev/chainguard/oauth2-proxy:latest \
  --cookie-secure=false \
  --cookie-secret=RYC2VBUYWQ6aenOkoN6jELQsrjtmwb23a7NdtrLI0ao= \
  --upstream=file:///dev/null \
  --http-address=0.0.0.0:8080 \
  --redirect-url=http://localhost:8080/oauth2/callback \
  --client-id=sample-id \
  --client-secret=sample-secret \
  --email-domain="*" \
  --provider=github \
  --scope=user:email
```

This `docker` command runs the `oauth2-proxy` Image while passing a number of configuration options to it. Most of these are sample values intended to get a working example proxy up and running. One particularly important option you should be aware of is the `--redirect-url`, which points to the OAuth application's callback URL. In order to set up an example locally, this example uses `http://localhost:8080` here.

Note that you can alternatively define these options in a configuration file or through environment variables. You can check out the [OAuth2 Proxy Overview](https://oauth2-proxy.github.io/oauth2-proxy/docs/configuration/overview/) for more details on these options.

After running this command, navigate to [`http://localhost:8080`](http://localhost:8080) in your web browser. There, you'll be presented with the OAuth2 Proxy sign-in screen.

Please refer to [the official documentation](https://oauth2-proxy.github.io/oauth2-proxy/docs/) for more information on how to work with OAuth2 Proxy.

<!--body:end-->

