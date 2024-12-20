---
title: "Debugging Distroless Images with Kubectl Debug and CDebug"
linktitle: "Video: Debugging with Kubectl and CDebug"
aliases:
- /chainguard/chainguard-images/videos/kubectl_cdebug/
- /chainguard/chainguard-images/troubleshooting/kubectl_cdebug/
lead: ""
description: "This video explains how to use the Kubectl and cdebug tools to investigate
failing containers. It focuses on how to debug distroless images with no shell
where traditional 'exec' commands don't work."
type: "article"
date: 2024-05-21T15:21:01+00:00
lastmod: 2024-05-22T15:21:01+00:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 015
toc: true
---

{{< youtube LQUZGE_w-20 >}}

## Tools used in this video

* [kubectl](https://kubernetes.io/docs/reference/kubectl/)
* [cdebug](https://github.com/iximiuz/cdebug)

## Transcript

So a while back I did a video on using Docker Debug to debug distroless containers.

Docker Debug is fantastic, but you do need a Docker Desktop Pro license to take advantage of it.

So I want to show a couple of other alternatives.

First up we're going to look at `kubectl debug`.

So to the terminal.

Okay, so the main reason tooling becomes important when debugging distroless containers is because there's no shell in a distroless container.

So you can't just exec in to see what's going on like you would with a debian or alpine container.

And that means we need the tooling to do some extra work to make this possible.

And normally that means creating a temporary container that shares the file and process namespaces with the target container.

So let's see how this looks with `kubectl debug`.

So I have a kind cluster running locally.

There's no pods currently.

But I have this nginx YAML which will start a `cgr.dev/chainguard/nginx` image. The container is called nginx but the pod is called nginx-pod.

Okay so let's try and get that running.

Looks good.

Okay now say we want to debug this pod.

Maybe it's throwing an error or displaying the wrong text etc.

So if it was a regular container you'd expect to do something like this.

But because it's distroless we get `/bin/sh` no such file directory.

And that's where `kubectl debug` comes in.

So I can run a command like this.

And what we're saying is `kubectl debug -it` for interactive terminal.

Then we give it the image.

The image is the debug container image.

So typically you want something with a shell and you're able to install more debugging tools.

So in this case we said alpine.

We've then given it the name of the pod so the `nginx-pod` but also the container we're interested in.

So this one's caught me out a few times.

You do want to pass `--target` and the name of the container you need so that you get access to the target container namespace or process namespace.

Okay so I run that.

Okay I've got a shell and if I run `ps` I see the nginx processes.

So that's excellent and it looks like it's all worked.

Unfortunately it's not as easy as that.

So if I do `ls` I see a container file system but this isn't the file system for my target container.

It's the file system for the debug container.

Yep so we're in an alpine container at the minute.

And say I want to debug this `/etc/nginx/nginx.conf` file.

Well that's not in this container it's in the target container.

Now I can or should be able to get to that namespace via the proc file system.

I get permission denied which you might think is odd because I am root but this is to do with namespaces and permissions and things not being quite as they seem in containers.

So I can't actually access the container file system in this case.

And there's actually a second problem as well.

If I was to run this pod again and we're going to call it pod 2 and this time we've got security context that says you can't run continuous as root.

Now you can probably guess what the problem is going to be here.

So I'll start with the second pod and if we try to do this the exact same command as did before well it's going to pause for a while and then eventually it should give me a warning but it never actually connects to the container because of this rule of not running as root which of course the alpine container wants to run as root by default.

Okay so there's a second issue there and they're both kind of related issues.

What you really want to do in this case is run your containers not as the root user but as different user -- as the Chainguard nginx image runs.

So the Chainguard nginx defines a non-root user that's running that and that's you know security best practice.

And what we want is we want our debug container to also run as the same user.

So how can we do that?

So in this case we've used alpine image but we can change to use a different image.

So I could also create a dockerfile and with a USER statement it changes the user.

Unfortunately there's no `--user` command to pass to `kubectl debug` which would be really useful but what I can do is use not the nginx `latest` image but the `latest-dev` image.

The `latest-dev` image includes a shell and package manager so I can use this as a as a good debugging image.

I'm also sure it's gonna have the same user because it's just a variant of the nginx image.

Okay so hopefully this will work.

Yes so now I am in the container.

I run `ps`.

Yes I see the nginx processes.

Now again I still need to figure out where the file system is.

Oh of course I've got my development image so this file exists but I'm still in the debug container I'm not in the proper container namespace but I can get there.

There you go.

So that's the actual `nginx.conf` from my target container.

Okay so to fix both of those problems with `kubectl debug` what we did was we started a container that runs as the same user.

So yeah top tip there and the other top tip is remember this `target` command.

That's the two things that trip me up with `kubectl debug`.

`kubectl debug` does have a couple more powerful things that I'm not going to go through now but I do want to mention what I thought was particularly useful is it has a `--copy` command so you can create a copy of a container and modify that to see what's going on with how affecting your production image. So that's quite cool.

The other tool I want to show you is cdebug by Ivan Velichko and I also want to say thanks to Ivan as it was a conversation with him that inspired this video and helped me understand the user problems with `kubectl debug`.

So we still have our kubectl pods running and we're going to try accessing them with cdebug.

Here we're saying `exec -it` so interactive terminal as per usual but we've added this `--privileged` flag that cdebug accepts and we're targeting the Kubernetes pod nginx pod and the container nginx inside.

Okay and that's worked straight away so that's great.

We can see the processes as before but we can also access the file system and if we take a look to leave out the slash and we can even edit files in the file system because we're privileged in this case.

Let's put blank space in so we don't break anything.

Okay so that's even better we can see the file system we can see the processes and can even change files and play with things.

But what happens if we try it with our other pod?

So we've got this `nginx-pod2`.

Well it does kind of work but because we can't run as root it changes to the user 1000 which makes sense.

But I don't want to do that in this case what we're going to do is pass `--user` so cdebug does take a `--user` flag and in this case we can use it to set our user to the same user as the container.

Okay so that's worked and we haven't got any warnings about user.

Type `ps` I can still see my processes.

Now what happens if I access the file system this time?

Looks like I can't see it but if I open the file, no I put a slash in my mistake.

So I can look at the file but in this case I can't edit it.

But still a pretty good result all I had to do is pass the `--user` flag.

Okay so that was both cdebug and `kubectl debug` which are both great utilities for debugging distroless containers.

Please do try them out and let me know how you get on.

Thank you.
