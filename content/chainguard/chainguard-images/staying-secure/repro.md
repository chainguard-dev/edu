---
title: "Reproducibility and Chainguard Images"
linktitle: "Video: Reproducibility and Chainguard Images"
aliases:
- /chainguard/chainguard-images/videos/repro/
- /chainguard/chainguard-images/staying-secure/repro/
lead: ""
description: "This video explains the importance of reproducibility and how to recreate any
Chainguard image from an attestation."
type: "article"
date: 2024-05-20T12:21:01+00:00
lastmod: 2024-05-20T12:21:01+00:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 010
toc: true
---

{{< youtube 0Qn2J89UEvI >}}

## Clarification

In this video we mention needing to keep copies of old APKs in order to be able to recreate images.
This wasn't fully accurate — in fact we do keep all our previously issued APKs, so you can build
images from months (and in the future, years) ago without issue. We currently retain all of these
package versions indefinitely (only servicing latest), but in the future we may age things out just
to manage the size of the index.

## Tools used in this video

* [cosign](https://github.com/sigstore/cosign)
* [apko](https://github.com/chainguard-dev/apko)
* [diffoci](https://github.com/reproducible-containers/diffoci)

## Commands

Retrieving the build configuration for the latest version of nginx:

```
cosign verify-attestation \
  --type https://apko.dev/image-configuration \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com \
  --certificate-identity https://github.com/chainguard-images/images/.github/workflows/release.yaml@refs/heads/main \
  cgr.dev/chainguard/nginx:latest | jq -r .payload | base64 -d | jq .predicate > latest.apko.json
```

Building the image:

```
apko publish latest.apko.json ttl.sh/nginx-repro

```

## Transcript

Okay, so I want to talk about a topic that I think is hugely important to engineering reliability and security, but doesn't get talked about very much.

And that's reproducibility.

Reproducibility is basically the idea that I run the same build twice, I should get the same thing out.

And that sounds trivial, but it's not.

For true reproducibility, we want things to be binary identical.

That is, I run the same build twice, and I get the same thing out down to the last bit.

We also want somebody else in a different time and place to be able to run the same build and get exactly the same thing out again.

So this means we need to control versioning, not just the source code and inputs, but also the build tooling.

Because if you run with a different version of your build tool, you could well get a different result.

But typically where things go wrong is you have unique IDs or timestamps somewhere in your build.

And of course, that causes a different result on each run.

Now, reproducibility is important to us at Chainguard, and I wanted to show how you can reproduce Chainguard images yourself.

So, to the terminal.

Okay, so let's start by pulling the NGINX image.

Now, the interesting bit here is this line here.

So this is the digest for the NGINX image.

The digest is basically a SHA hash of the image, so it uniquely specifies that image.

If we manage to recreate this image, we should end up with exactly the same SHA hash.

Okay, and the way we're going to try to recreate it is we're going to start by using cosign to get the apko image configuration.

So this is an attestation that includes the build config to build that image.

And what we're saying here is this attestation should have been signed using the certificate for the corresponding GitHub action, and the identity should correspond to the workflow that created this attestation.

Here we specify the image we're interested in.

So here we've got `nginx:latest`.

Of course, you can change that for whatever image you're interested in.

We could also have specified the full SHA there.

That would have made sense as well.

We then extract the payload section from the JSON that gets returned.

We deconvert that from base64, and then we pull out the predicate section to finally give us our JSON file that includes our apko.

So let's run that.

Okay, and we get some output just telling us that it has managed to successfully verify the attestation, so we know it's genuine.

And let's take a look at what it's created.

So this is our apko file.

It's a pretty simple build file.

Apko is a very simple build system.

Basically, all you can do is specify a list of APK packages to install in the image plus some metadata.

So at the top there, you saw some stuff relating to UNIX accounts to create, some annotations to add to the image, the architectures we're going to build for, the CMD line for the Docker file, and then all these lists of versioned APK dependencies.

And this is the full list of dependencies.

So it's not the case that `libgcc` is going to pull in another dependency that's not listed here.

This is the full list.

And they're all coming from `packages.wolfi.dev`, as we expect.

Also set an ENTRYPOINT and some environment stuff.

And that's about it.

Okay, so let's try running apko with that file.

We're actually going to call `apko publish`.

So what we're seeing here is `apko publish`, which is going to build from this `latest.apko.json` file.

And then it's going to publish the image that results to this repo, `ttl.sh/nginx-repro`.

So `ttl.sh`, if you've not seen it, it's basically a free to use Docker registry that you can upload anything to, but it only sits there for a short amount of time.

So it's a temporary registry for testing things if you like.

And that's from Replicated.

So thank you very much, Replicated.

Okay, so what's happening here?

I clicked run there.

And we're building images for both AMD64 and ARM64.

We see it installed in all the packages.

And in fact, you'll see that twice because, of course, we're building two images.

Also building some of the other container stuff and SBOMs for these images.

And that's about it.

Now, important bit is at the bottom here.

Here we have our SHA again.

So this is the SHA of the image it's created.

And it's `f705`.

I've forgotten what it was before.

So let's download nginx again and see if it matches.

And it does.

So that's pretty cool.

We've managed to recreate this Chainguard image bit for bit and push it to this repo.

And it's relatively unusual for build tooling to be able to do that with container images.

But here we've done it with apko and Chainguard images.

There are, however, a few things to be aware of.

So if I take a look at this `latest.apko.json`, first thing to be aware of is all these APKs are specified as specific versions that were used.

Now, Wolfi is a rolling repo.

We don't keep older versions of packages for very long.

So in six months time, I'm unlikely to be able to download some of these packages at these exact versions.

So if you want to be able to recreate this, you'd have to have access to the old packages somehow.

The second one is you may think, well, OK, but can I reproduce these packages from source?

And yes, you can.

But the issue is you won't end up with binary identical versions because the APKs themselves include signatures inside them that have been signed using Wolfi's signing key, and of course you won't have access to the private signing key.

So you're going to be unable to create a binary identical version of the APKs.

Finally, do you remember what I said earlier about build tooling?

So this created with this version of apko, which I actually built from the head of the repo.

I did originally try with a different version that was released and that actually failed to reproduce.

And I got a different digest because it handled links slightly differently.

So a minor difference in the build tooling caused the binaries to be different.

So one thing I would say is if you're playing with reproducing images, there's a really great tool called diffoci.

And you run diffoci on on your images, then it'll tell you exactly what the difference between two images are.

So if I run it here on these two images, it basically just tells me, yeah, those match.

But if I run it on different images, I'll give you a full list of which files inside the images are different and where they're different.

So a really, really useful tool there.

And it'll also allow you to filter out things like timestamp differences if you're not interested in them.

OK, so that was a long way of saying that Chainguard images are reproducible and you can even reproduce them yourselves.

Please do give us a go and let me know how you get on.
