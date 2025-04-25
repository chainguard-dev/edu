---
title: "Subscribing to Chainguard CloudEvents"
linktitle: "Subscribe to Events"
type: "article"
description: "."
date: 2025-04-24T15:22:20+01:00
lastmod: 2025-04-25T15:22:20+01:00
draft: false
tags: ["Product", "CloudEvents", "Procedural"]
images: []
menu:
  docs:
    parent: "cloudevents"
weight: 010
toc: true
---

Chainguard implements [CloudEvents](/chainguard/administration/cloudevents/events-reference/), a specification for a standard format for events data. This means developers can use events (generated based on interactions with Chainguard resources) to initiate processes and thus automate certain actions. For example, you could set up infrastructure to listen for push events to an organization's private registry and [mirror any new Chainguard Containers in the registry to a third-party repository](/chainguard/administration/cloudevents/image-copy-gcr/).

This article includes an example of how to use `chainctl` to create an event subscription. It also includes details on how to validate events from Chainguard and highlights some potential use cases for them. This article is primarily focused on Registry `push` and `pull` events. *Push* events occur when an image in your entitlement is added or updated. *Pull* events occur when an image is pulled from your Chainguard repository. Be aware, though, that there are also events related to IAM, such as user creation and adding identity providers. 


## Subscribing to Events

To subscribe to Chainguard events for your account, use the following `chainctl` command:

```shell
chainctl events subscriptions create https://<Your webhook URL>
```

The webhook URL should connect to a service that you use to process the requests. This can use whatever infrastructure works for your team, but a common choice is to use a serverless service such as [AWS Lambda](https://aws.amazon.com/lambda/) or [Google Cloud Run](https://cloud.google.com/run/docs/overview/what-is-cloud-run).

As an example, this guide will use [Webhook.site](https://github.com/webhooksite/webhook.site). This is an open-source application that will generate a URL you can use to receive, send, and transform webhooks, among other actions. Webhook.site can be self-hosted, but for the purposes of this guide you can just use the [cloud version of the application](https://webhook.site).

> **Note**: You can also try this out with alternative webhook testing sites, like [smee.io](https://smee.io/).

Once you have the webhook URL, use a `chainctl` command similar to the following to set up a subscription to events for your account:

```shell
chainctl events subscriptions create https://webhook.site/aEXAMPLE-b689-49a5-94df-f1dEXAMPLE29
```

This command will prompt you to select the organization whose events you want to subscribe to. If successful, this will return an ID for the subscription:

```
   ✔ Selected folder chainguard.edu.
                         	ID                         	|                       	SINK
------------------------------------------------------------+------------------------------------------------------------
  45a0cEXAMPLE977f050c5fb9EXAMPLEeed764595/91b3cdEXAMPLE7a6 | https://webhook.site/aEXAMPLE-b689-49a5-94df-f1dEXAMPLE29
```

In order to generate an event, try pulling an image from your organization's repository within the Chainguard registry:

```shell
docker pull cgr.dev/chainguard.edu/istio-pilot:1-dev
```

Be sure to change this command to use your own organization's repository and an image you have access to.

```
7.0.10: Pulling from chainguard.edu/istio-pilot
Digest: sha256:5a4583fb12ee4b33306a2c23ff33c9f2d04e6d1c7580703850928abf50de5dcf
Status: Image is up to date for cgr.dev/chainguard.edu/istio-pilot:1-dev
cgr.dev/chainguard.edu/istio-pilot:1-dev
```

Then, navigate back to Webhook.site. It may take a few moments, but in time an event will appear with request content like the following:

```
{
  "actor": {
    "subject": "261ea43771f4d962f17c1d206155a38b9b17ff18",
    "act": {
      "aud": "Hvqy7yoEhI8TY1zX9rPrsdcIntDz9yh2",
      "aws-acct": "",
      "aws-arn": "",
      "email": "",
      "iss": "https://auth.chainguard.dev/",
      "sub": "google-oauth2|117799788801679028930"
    }
  },
  "body": {
    "repository": "chainguard.edu/istio-pilot",
	"repo_id": "45a0cEXAMPLE977f050c5fb9EXAMPLEeed764595/e2fca7026fbaa243",
    "tag": "1-dev",
    "digest": "sha256:043446cbda630e5071e4f72736b38b5249c859d07bb14886cd93b4e36fc3402c",
    "method": "HEAD",
    "type": "manifest",
    "when": "2025-04-23T00:37:47.810899",
    "location": "",
    "remote_address": "76.169.101.202",
    "user_agent": "docker/27.3.1 go/go1.22.7 git-commit/41ca978 kernel/6.8.0-57-generic os/linux arch/amd64 UpstreamClient(Docker-Client/27.3.1 \\(linux\\))"
  }
}
```

This sample request has the following headers:

| Header | Value |
|----------|----------|
| accept-encoding   | `gzip` |
| traceparent   | `00-6f9aceb3276e8c60676cf04099d8818d-dd75e26d099ef057-00`|
| original-traceparent   | `00-6f9aceb3276e8c60676cf04099d8818d-dd75e26d099ef057-00` |
| content-type   | `application/json` |
| ce-type   | `dev.chainguard.registry.pull.v1` |
| ce-time   | `2025-04-23T00:37:47Z` |
| ce-subject   | `45a0c61ea6fd977f050c5fb9ac06a69eed764595/7214b8ddd5ce879d` |
| ce-specversion   | `1.0` |
| ce-source   | `cgr.dev` |
| ce-id   | `188888b6-27d2-4a80-8ad5-c7450ab89c0c` |
| ce-group   | `45a0c61ea6fd977f050c5fb9ac06a69eed764595` |
| ce-audience   | `customer` |
| ce-actor   | `enforce-prod-registry-jzjewxe4@prod-enforce-fabc.iam.gserviceaccount.com` |
| authorization   | `Bearer …` |
| content-length   | `721` |
| user-agent   | `Chainguard Enforce bd6a3e9-dirty` |
| host  | `webhook.site`   |

This shows that you have successfully subscribed the test service to Chainguard Events.


## Filtering Events

The webhook will get all events for your organization. You will need to filter them to only the events you are interested in, which can be done using the `ce-type` header. For pull events the type is `dev.chainguard.registry.pull.v1` and push events are of type `dev.chainguard.registry.push.v1`.

A full description of all events and their types is [available on Chainguard Academy](/chainguard/administration/cloudevents/events-reference/).


## Validating Events

Before processing an event from Chainguard, you should ensure that it is valid. Every Chainguard event has a JSON Web Token (JWT) formatted OIDC ID token in its Authorization header. For authorization purposes, there are two important fields to validate:

* Use the `iss` field to ensure that the issuer is Chainguard, specifically `https://issuer.enforce.dev`.
* Use the `sub` field to check that the event matches your configured Chainguard identity. For example, assuming a UIDP ID of `0475f6baca584a8964a6bce6b74dbe78dd8805b6`, the `sub` field's value will resemble the following: `webhook:0475f6baca584a8964a6bce6b74dbe78dd8805b6`. If the subscription is in a sub-group, then the value will have the corresponding group SUID appended to the path.

Validating these fields before processing the JWT token using a verification library can save resources, as well as alert you about suspicious traffic or misconfigured Chainguard organization settings.

## Use Cases

Events can be used to drive a wide range of processing scenarios, including the following:

* Copying images to another registry when an image is updated
* Kicking off an image rebuild process when a base image is updated
* Logging new image availability to a Slack channel
* Logging pulls and user creation to check for unexpected or unauthorized usage

Chainguard's [platform-examples](https://github.com/chainguard-dev/platform-examples) repository contains example code for implementing workflows based on events. Most examples are based on Terraform and work with the Google Cloud Platform, but should be portable to other environments.

## Learn More

This article outlined details on what Chainguard Events are, how to use them, and some common use cases. For more information on CloudEvents, you can refer to [cloudevents.io](http://cloudevents.io/). You can also find more details in [Chainguard's CloudEvents reference documentation](/chainguard/administration/cloudevents/).
