---
title: "Create, View, and Delete chainctl Events"
lead: ""
description: "A simple introduction to chainctl events usage"
type: "article"
date: 2025-05-06T08:49:15+00:00
lastmod: 2025-05-06T08:49:15+00:00
draft: false
tags: ["chainctl", "events", "Product"]
images: []
weight: 050
---

This page shows you the basic usage of `chainctl events` commands. For a full reference of all commands with details and switches, see [chainctl Reference](/chainguard/chainctl/).

Chainguard events use the [CloudEvents](https://cloudevents.io/) specification for describing event data.

Chainguard Academy has several deeper guides on [Chainguard CloudEvents](/chainguard/administration/cloudevents/). You may find our guide on [Subscribing to Chainguard CloudEvents](/chainguard/administration/cloudevents/events-example/) to be particularly useful for understanding how to work with events from Chainguard while [Chainguard Events](https://edu.chainguard.dev/chainguard/administration/cloudevents/events-reference/) provides a deeper dive into the content and make up of events.

There are three `chainctl events` commands available: `create`, `list`, and `delete`.


## Create event subscriptions

To create a new event and subscribe to events in that organization or folder, use:

```shell
chainctl events subscriptions create $SINK_URL
```

A sink is an addressable or callable resource that can receive incoming events delivered over HTTPS and will translate the delivered event into a returned response that includes promised information. The style and type of response is set by the sink.

Depending on the sink, you may be prompted to respond to some questions before this action is complete. You can add a `-y` to the command to automatically assume `yes` and run without interaction.


## View your event subscriptions

To retrieve a list of all your Chainguard account's subscriptions, use:

```shell
chainctl events subscriptions list
```

This will return a list of IDs and sinks for all of your subscriptions.


## Delete event subscriptions

To delete an existing event, use:

```shell
chainctl events subscriptions delete $SUBSCRIPTION_ID
```

Depending on the sink, you may be prompted to respond to some questions before this action is complete. You can add a `-y` to the command to automatically assume `yes` and run without interaction.