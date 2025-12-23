---
title: "Updating Container Images with Renovate (and no PATs!)"
linktitle: "Renovate Video Tutorial"
type: "article"
lead: "Learn how to use Renovate with Octo STS to update container images without Personal Access Tokens"
description: "Video tutorial showing how to set up Renovate as a GitHub Action with Octo STS to eliminate the need for Personal Access Tokens"
date: 2025-12-23T09:30:00+01:00
lastmod: 2025-12-23T09:30:00+01:00
tags: ["octo-sts", "Renovate", "Video", "Tutorial", "GitHub Actions"]
draft: false
images: []
menu:
  docs:
    parent: "open-source"
weight: 105
toc: true
---

In this video, Chainguard Staff Developer Relations Engineer Adrian Mouat shows you how you can update container images using Renovate with Octo STS, eliminating the need for Personal Access Tokens.

## Video

{{< youtube I0hWRMtdUyI >}}

## What You'll Learn

- How to set up Renovate as a GitHub Action
- Using Octo STS to eliminate Personal Access Tokens
- Configuring trust policies for automated workflows
- Setting up assumable identities for private registries
- Automating container image and GitHub Actions updates

## Transcript

In this video, I'm going to show you how you can use Renovate to update container images and GitHub actions. At Chainguard, we do talk a lot about the need to keep software up to date. And in my opinion, it's essential you do that for both security and maintainability. So, if you stay on an old version of a package for too long, there's a strong chance that you'll be bitten by an unpatched vulnerability. But also, the longer you stay on an old version, the harder updating becomes. So, it's much better to do frequent small updates than it is to occasionally be forced into having to do major breaking updates.

Another thing we talk a lot about is getting rid of long-lived tokens. So, long-lived tokens always come up when you look at reports on how cyber attacks occurred. And if you're a current Renovate user, I'm willing to bet that you probably gave it a PAT or personal access token for GitHub. And I'm going to show you how you can get rid of that PAT by using an open-source tool from Chainguard called Octo STS.

Do know in this video I'll be focusing on container images and updating container images, not packages. So the FROM lines in your Dockerfiles, not the APK add lines.

### Setting Up the Demo

Okay, let's jump to the demo. What I'm going to do is fork this demo application and set up Renovate to run as a GitHub action to update everything. And this demo application's a little bit old, so I know it needs updates to both the Dockerfiles and the GitHub action workflows. There is this version Dockerfile, and this one's interesting as it uses the cgr.dev organization. So that's going to require OAuth. So we'll see how to set up OAuth so Renovate can check out if there's new images available in this repo.

Yeah, let's just go ahead and try forking this. So click this big fork button. Could do it at the command line, but I'm here. We're going to call it "production builds renovate" and okay.

And then we're going to clone this and use GitHub CLI and we'll jump to the terminal. First thing: `git brief clone`.

I also want to set the default. I don't want to push up to the original project right now. So, we want this to be our mode production build with renovate. Good.

And now I do have some files we're going to copy over to set up Renovate.

### Configuring Renovate

Okay, so here's the `renovate.json` file. This is the configuration file for Renovate. We're basically going to use the default configuration. I have added a few things here. This one I'd really recommend trying: `pinDigests` equals true. That will add digests for any images or actions that don't have digests. And you'll see what that means later.

I've added these—this is just so that by default, Renovate will try not to overwhelm you and will only give you a couple of PRs at a time to update things. But we're saying here, hey, give us everything at once. And that's just sort of the purposes of this demo. So, I don't recommend you do that in your own projects.

The other thing I should say at this point is we're going to be running Renovate from a GitHub action. There are multiple ways to run Renovate. This is GitHub action on a schedule, which is great for small projects like this. For larger projects, you might want to look at running Renovate self-hosted, so it runs continuously or using a hosted service from the creators at Mend, which is a really great option as well.

We have some workflows for building images. There's also an old one for the Jester bot that we're not going to worry about in this talk. Dependabot does do something similar to Renovate and it helps you update image digests. So, do take a look at it if you're interested, but this video is going to focus on Renovate.

### The Renovate Workflow

And we're going to copy our Renovate workflow over here. So let's take a look at that. Yeah. So, we schedule it to run at 3:00 a.m. every morning. It runs on Ubuntu latest. Because we're doing stuff with the GitHub token, we need to ask for write permissions to ID token. I know "write" sounds a bit weird, but that's the way GitHub does it and write permissions to the repo.

So, first thing we do is set up chainguard. This is to auth to the cgr.dev registry so that we can check for new versions of images in the cgr.dev organization. This identity is wrong. It's from a previous workflow. So, I'll show you how to update that in a second.

And then we've got Octo STS, which is the magic that allows us to get rid of the personal access token for Renovate. Finally, yeah, down here is basically where we run Renovate. A bit of magic to set up the password for cgr.dev. The Renovate token—that's actually a GitHub token. So maybe not the best named variable ever, but that's what they call it. I quite often have to set log level to debug to figure out what's going on. For this demo, hopefully we'll be able to leave it here.

Oh yeah. So that's about the Renovate JSON. Let's jump back.

### Setting Up Chainguard Identity

And what we're going to do is start by setting up chainctl. This is only for people—for Chainguard customers—that need to access a private registry. If you're just using a free tier of Chainguard images, you don't need this because you don't need to auth to the registry.

So, what we're going to do now is create something called an assumable identity that the GitHub action can use to access the cgr.dev repo. So what we're doing here is `chainctl create` this identity called `pb-renovate` and it's going to look at the GitHub token and it's going to say, "Is the GitHub repo that's asking for this identity amouat/production-builds-with-renovate?" If so, it's okay. And is the ref the main branch? So only the main branch on this repo can assume this identity. And yeah, here's the project we're using cgr.dev view.

Yes. Okay. So, that's created our identity and here is the ID. So, we can now put that into our workflow.

So, it's going to replace this one.

So, that should be all we need to set up the assumed identity.

### Setting Up Octo STS

Next thing we're going to look at is setting up Octo STS. So let's jump back to the web browser so I can show you that. So this is the GitHub app page for Octo STS and it describes a bit about what it is, what it does, you know getting rid of personal access tokens, which is exactly what we're doing in this use case. Certain workload trust, trust policies, etc., and federating a token, which is exactly what we're going to be doing here. And some more low-level stuff. Also a link to the Octo STS page where you can go and look at all the source code. It's a relatively small project so you can actually look at the source code and understand what's going on and what's happening.

Now up here you'll see "install" in your case, probably—in my case it's "configure" so I can select which repositories can be used with Octo STS and things like that. In this case I've already set it up.

So the next thing we do is set up the trust policy for Octo STS. So we'll see here we've got given it this identity "renovate." So what that's going to mean is it's going to look in this directory `.github/chainguard` and it's going to look for a `renovate.sts.yaml` file. And it's going to use the values in that and compare it to the token it's given. So we need to create this value. I'm going to copy an existing file from earlier.

And this is what it looks roughly like. Now this is changed. Our repo name's different. So, `production-builds-with-renovate`. Got to make sure you get this right or it will break.

Right. So, issuer is the GitHub token issuer and the repo is `amouat/production-builds-renovate` and the refs is the main branch. So what we're saying here is issuer token has to be from GitHub and it has to be for this repo and it has to be for the main branch. You can use regex here. So you can be a bit more flexible in what the matches are.

And then we're going to say the permissions we are asking for. So in this case we're asking for quite a lot of permissions, which is all the stuff that Renovate needs for creating pull requests and checking projects etc. And that's about it.

### Testing the Setup

So, I think the next step is just to check in this code and push it back up to the repo.

So, we'll add all these files.

If something looked a bit funny there, that was just me using git sign to sign this commit. Okay, there we go. So, I'm going to jump back to the GitHub repo now and see what that looks like. So, here's the repo. I did just push to main, which I know is dangerous, but it's just a demo.

Yeah, and you can see it's got this "configure renovate" PR. So, let's take a look in actions. We see a bunch of stuff for building images that was already there, but you've also got this Renovate one there. And I'm very hopeful if we click "run workflow," something will happen.

So if you go into it, you can see a bit more of what's happening. We can see Octo STS works. So it got the token. That's really good. It looks like it also got access to cgr.dev. And Renovate is running. It's downloaded the Renovate image.

It's looking at Dockerfile, GitHub actions, and Go dependencies. And there we go. So, that's run successfully. Let's go and take a look at what PRs it's created.

### Results

Yeah, a whole bunch here. So, I'm extremely happy this has worked. So, we have ones for our actions, for example. So, it's saying we're using an old version of the Cosign installer. We should update that.

But it also has things like here we have—you know this version of the static image—we're using an old version. So it's updated that by looking at what is the latest digest for or what's the newest digest for the latest tag.

And what else do we have? Where's cgr.dev?

Here. So we can see it's updated cgr.dev from 1.25.3 to 1.25.5 and it's pinned it to a digest. So that's both good for security and reproducibility and keeping everything up to date. So I'm really happy what's going on here.

One thing to note is I do have 15 PRs here which is a little bit hard to deal with because one problem is if I start merging some of these you'll probably get conflicts and because of that there is this really useful—if you want to rebase, retry this PR, click this checkbox which should kick off another build. Okay, so let's try merging this one.

Yeah, it looked like that works. It successfully updated our version of Go here. And we really did it with just a few clicks. So you can see it's really powerful, relatively easy to use once it's set up. We're using it here without the need for a PAT via Octo STS, which makes me very happy indeed. So please try it out. Let me know how you get on.

## Key Takeaways

- Renovate can automatically update container images and GitHub Actions
- Octo STS eliminates the need for Personal Access Tokens by using OIDC federation
- Trust policies provide fine-grained control over what workloads can access
- Regular small updates are better than occasional large breaking updates
- Pinning to digests improves both security and reproducibility

## Related Resources

- [Getting Started with Octo STS](/open-source/octo-sts/getting-started-with-octo-sts/)
- [Using Octo STS with GitHub Actions](/open-source/octo-sts/how-to-use-octo-sts-with-github-actions/)
- [Trust Policy Reference](/open-source/octo-sts/trust-policy-reference/)
- [Octo STS GitHub Repository](https://github.com/octo-sts/app)
- [Renovate Documentation](https://docs.renovatebot.com/)
