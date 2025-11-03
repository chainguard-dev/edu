---
title: "Create, View, and Delete chainctl Events"
lead: "Chainguard's chainctl events commands enable CloudEvents-based monitoring and alerting for container security events and supply chain activities."
description: "Learn how to use chainctl events commands to create, view, and manage CloudEvents subscriptions for monitoring Chainguard security events and container activities"
type: "article"
date: 2025-05-06T08:49:15+00:00
lastmod: 2025-07-23T15:09:59+00:00
draft: false
tags: ["chainctl"]
images: []
weight: 050
contentType: "how-to-guide"
---

Chainguard's `chainctl events` commands provide programmatic access to security event streams using the [CloudEvents](https://cloudevents.io/) specification. These commands enable you to monitor container activities, security alerts, and supply chain events across your organization for enhanced observability and compliance.

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
