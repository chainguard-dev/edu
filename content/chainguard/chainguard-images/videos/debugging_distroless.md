---
title: "Debugging Distroless Containers with Docker Debug"
linktitle: "Debugging Distroless Containers"
lead: ""
description: "How to use the Docker Debug feature to debug Distroless and minimal containers"
type: "article"
date: 2024-01-26T01:21:01+00:00
lastmod: 2024-12-12T15:21:01+00:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 070
toc: true
---

{{< youtube ELxIBB2Uy2E >}}

## Tools used in this video

* [Docker Desktop](https://docker.com) (Note a paid subscription is required.)

## Transcript

Hey folks, I wanted to record a short video explaining how you can debug container images, even distroless ones.

One of the problems with distroless images is that they can be difficult to debug.

Now if you're using Kubernetes, please try out ephemeral containers, but in this video I want to talk about something else.

In Docker desktop 4.27 they have a beta feature called debug, and I'm going to demonstrate that now.

So I'm going to start a Chainguard nginx image.

Note that Chainguard nginx images run on port 8080 for security reasons.

Now that should be running in the background, so if I switch to my browser and we hit reload, yep nginx is there and running.

So say I want to debug this nginx container, say it's not displaying the right content or it can't reach another container, something like that.

So typically what you might want to do is use `docker exec` to get a shell into the container.

But if I try to run bash, I get told there is no bash, and I get told there is no sh.

And even if I get the full path, it doesn't work.

Because this is a distroless container, there's no shell available to me.

There are also very few utils.

So I can't even run `ping` for example.

So the only way to debug this container at the minute is from the outside, if you like.

Or is it?

Because with Docker 4.27, I now have this `debug` command.

So if I run `docker debug debug test`, this is what happens.

And suddenly I have a shell into the container.

Basically what's happened is it's side loaded a Nix environment into the container.

And from here I can install tools to debug things.

It also has a linting tool to check the entry point.

So you can see the entry point here is fine.

It does have editors, et cetera.

I believe `ping` is here.

Yep.

So what can we do?

We can also look at the container file system and edit it live.

So for example, if I do `/etc/nginx`, and autocomplete works, and here's the default conf, and there's the location of the nginx files.

So let's take a look at these nginx files.

And here's index.html.

And this is welcome to nginx.

So let's try live editing this.

Okay.

I saved that.

Now let's go back to our browser and reload it.

Yeah.

So there we are.

I've live edited a distroless container that had no shell and no editor inside it.

So there is more you can do.

You can install further tooling, but like I said, it does have some basic tooling with it.

But like say, I don't know if you want to install a different editor, you can definitely do that.

So here we go.

There's install emacs.

Note this is a beta version.

So I have noticed this error coming up a few times or warning.

I do believe it's actually innocuous and hopefully that will be changed in newer versions, but it has actually installed emacs there.

Now I don't use emacs.

So I always have to struggle to escape.

Is it control?

Oh, no.

There we go.

Okay.

So there you go.

That's how you can debug a distroless container using the new Docker debug feature.

Please do give it a go and let me know how you get on.

## Relevant Resources

- [Debugging Distroless Images with Kubectl Debug and CDebug](https://edu.chainguard.dev/chainguard/chainguard-images/videos/kubectl_cdebug/) (Video)
- [Debugging Distroless Images](https://edu.chainguard.dev/chainguard/chainguard-images/debugging-distroless-images/) (Article)
