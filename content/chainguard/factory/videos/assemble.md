---
title: "Inside the Chainguard Factory - Assemble 2025"
linktitle: "Inside the Chainguard Factory"
type: "article"
description: "Inside the Chainguard Factory as presented by Dustin Kirkland at the Assemble conference in 2025."
date: 2025-07-31T16:00:00+00:00
lastmod: 2025-08-02T05:01:45+00:00
draft: false
tags: ["Chainguard Factory", "Video", "Overview"]
images: []
menu:
  docs:
    parent: "chainguard-factory-videos"
weight: 100
toc: true
---

{{< youtube iU9hmW6hrGs >}}

## Transcript

**Sam (Introduction)**: We're very fortunate our Vice President of Engineering, Dustin Kirkland, is going to be walking us through the Chainguard Factory, which you would have heard a little bit about during the keynote today. So I'll go ahead and turn things over to Dustin. We will have time at the end for questions, so keep that in mind. Thank you.

**Dustin Kirkland**: All right, thank you Sam. Cool, so thank you for joining us. This is the technical session we can call it a factory tour. I once went on a factory tour when I was, I don't know, a teenager or so to the Corvette factory in Bowling Green, Kentucky, and I still think back to that—what a cool experience that was. Once upon a time, we've got a lot of analogies in here that, you know, sort of point to what we build is a lot like a modern automotive factory.

### Overview

So just an overview of what we're going to talk about and hopefully what you can take away from this. We've built a new operating system distro designed from the ground up, completely modern, overwhelmingly using cloud technologies and automation in a way that has provided tremendous advantages and opportunities to scale this and secure the entire software supply chain. That's a bold statement, but I'm going to walk you through some of how that comes together.

At the heart of that is a factory, and we really call it that because flowing through the factory constantly is a ton of inputs: source code, open source code, third-party libraries, compilers, tool chains, scripting languages, runtimes—all of that assimilates together into a software system that our customers can then build and depend on, build their own software on top of and depend on in production. And then we're going to pull all of that together with what we call the Chainguard Operating System, and it truly is an OS from end to end. I would say now that we have added this capability to run full operating systems inside of virtual machine environments and then stripe that across other OSs with our libraries product.

Just a little bit about my background: I have spent two halves of my career—one as an engineer and a second as a product manager. I've also spent two halves of my career—one with some of the world's biggest companies (IBM, Google, and Goldman Sachs) and then another in startups and growth mode. And so with that comes a lot of experience and a real personal interest in solving the operating system Linux distro security problem and fitting that into the overall mission of Chainguard to secure the software supply chain.

### Our SLA: The Foundation

All right, we're going to kick this off and start with our SLA—our service level agreement. This is what it says, this is on our website. Not everyone publishes their SLA on the website—we do publish our SLA on the website, and this is the fine print. This says that Chainguard will remediate security vulnerabilities that are rated critical within seven calendar days and highs, mediums, and lows within 14 calendar days. Seven and 14—we remediate criticals within seven, highs, mediums, and lows within 14.

Where did those numbers come from? That actually came from FedRAMP, believe it or not. Is anyone here subject to FedRAMP requirements directly or indirectly? Have you read the FedRAMP spec? Yes, exactly. I'll zoom into the most important piece, which is 30, 90, and 180. This is what FedRAMP says: if you are a vendor selling software or services to the government, you've got 30, 90, or 180 days to remediate those vulnerabilities. This is the piece on page 97 1.5 where this comes into focus.

What this actually looks like from a Chainguard perspective is this right here: an nginx image that is completely free of CVEs as of 15 hours ago when these screenshots were taken. And there's a bit of data in here in terms of when the image was updated—less than a week before that—and it was scanned on a daily or an hourly basis constantly. So if you care about, say, nginx, you're not worried about meeting those 30, 90, or 180-day obligations. As long as you're using the latest Chainguard image, you will have those CVEs remediated for you.

Now I said seven and 14. In actuality, it takes us less than two days typically to remediate a CVE that we even know exists. And I want to add that last asterisk in there: there are hundreds of CVEs that are remediated that you never even see, that we never even see, that are getting fixed upstream before the scanner is able to find that inside of a Chainguard image—it's gone. I'm not even waiting, using those effectively zeros that would stack that histogram even more. Our average time to remediate any CVE that we know about is actually under two.

Here's a pie chart of all of the CVEs that we've known about since January 1st of this year. So this is year to date with 65% within two days, 28% within seven, the pink within 14—6% within 14. What's that last sliver? Less than a half a percent. These are CVEs that are either still awaiting an upstream fix typically, at which point we work as quickly as possible to patch and remediate that, rebuild that as soon as upstream has that fix available.

### How We Do It: The Factory

How do we do that? It's the factory. We are continuously rebuilding the entirety of the Chainguard OS. So let's dig into some of those pieces.

First of all, this is the hard part: we build from source. Yes, everything, constantly. I want to make that part abundantly clear, especially for anyone who's maybe new to the Chainguard story. We are not a derivative of any other operating system. We don't start with Debian or Fedora or Alpine or any other Linux and harden that. And that's a little bit different than some of the other alternatives to Chainguard's technology. We literally start at the source code—the tarballs or the git checkouts—and build everything from scratch, including the compilers. We've bootstrapped the actual tool chain itself all the way down to GCC.

And so a change in GCC, the C compiler that underpins almost everything including Python, including Java and C bindings—we rebuild everything up from that. That takes a lot of, first of all, expertise, but a whole lot of automation in order to do that.

### The Wolfi OS Repository

So this is just one piece of our OS. This is the Wolfi Dev OS. This is a snapshot from GitHub. You can see that this gigantic mono repo had 2,600 entries, and it shows a thousand but there's another 2,600. These are our source packages. And it's just for the piece that we call Wolfi, which is this open source core, with 63,000 commits, and that's going up by a couple hundred commits per day. Many of those are driven by our automation. Our automation is a bot that we call Octos, and it's what enables us to securely do this in GitHub and GitHub Actions itself.

### Package Building Example: sed

Securely, this is what a single package looks like to build, and this is a lot simpler. I've long been a packager of Debian packages and Fedora packages. The fact that we can define the entirety of the sed package—my favorite editor, I don't know, anyone else a sed fan? If I need to edit a file, this is the way I'm going to do it.

This is sed 4.9, which is the latest version. You can see the version, the name, the epoch, the build, and then the URI—the URL where to get that from. And this is a GNU package, the tarball and the expected SHA. If that changes—and we have monitors that are constantly watching this—as soon as that changes upstream, our automation will kick in and download the new tarball. We'll apply these same build rules, the build configure rules, the test against it. We'll then, if it passes, we'll republish that, and then we'll restart building all the images that might include sed inside of it.

### Vim Example

For those who are not sed fans for editing their files, we've also got a Vim example. All of 77 lines. And again, to compare this to another distro's package manager, that's going to be dozens of files in a directory. It's going to be probably hundreds of lines of code and a stack of carried patches. There are no carried patches against either of these, so this is farm-to-market pure, straight from the upstream source with easy to view build rules, configure build rules.

And you can see some of these have, you know, security implications. Without X, this is going to be a command line-only Vim that cuts out a whole bunch of code and vulnerabilities that might come along with code that's not necessarily needed. There's also a handful of tests, so every almost every one of our packages itself includes tests that have to run and execute and succeed at the package build time, or else the package itself doesn't get published, which means that, you know, we'll hold that back and that will need to get attention from one of our engineers who's going to dig into what we need to fix in order to satisfy that build or those tests.

### Git-based Packages

So this one is just slightly different in that we're not fetching a tarball. We actually prefer, much prefer to fetch directly from a git repo at a particular tagged version. And again, we will check that expected commit and that hash. Again, we've got these watchers—event-driven automation that's constantly watching for a new commit to, or sorry, a new tagged release from any of the 6,000 source packages that we're monitoring. As soon as that happens, within minutes we trigger a whole new build, which then creates this entire directed acyclic graph, a DAG tree of all the other things that we're going to need to do based on the success criteria of each of those.

Vim is a little bit interesting in that the way that this open source project is set up, with every single commit, Vim auto-tags a new release, which is kind of crazy to think about. But typically within 30 minutes of the upstream Vim developer making a commit to Vim, we've already built and tested and published a whole new version of that package. Now this, of course, is a, you know, human interactive thing. This isn't making its way typically into your production containers, but to me it's just a great example of how fast we've taken that farm to market from that upstream open source developer straight to, you know, this distro itself and tested it.

### Automated Updates

And this is what an update looks like. This was merged by Octos—that's our automated bot. This is all it took to bump the Vim package from version 9.1.189 to 9.1.194: a change in the version which affected the variable of the tag itself and then the difference in commit. With that, this package automatically rebuilt, retested, and made its way through the entirety of the process.

So this is a very, very important key point: we typically don't, except for exceptional circumstances, we typically don't backport patches from some cherry-pick from head of the open source project and try to munge that and make that work with a codebase that's months or potentially years and years old. Instead, we bring everything forward, fast forward to the latest and greatest release. And in doing so, that's how we solve many security vulnerabilities that will go unpatched in other distros because it's just not practical, possible, or feasible to backport that really complicated patch to an older codebase.

That's largely how we solve the lows and mediums, right? The highs and criticals are, you know, maybe possible with excessive effort to backport, but the lows and mediums you can't even fix typically in open source code without moving the entire codebase forward. So that's how we solve that.

Now we can and do carry patches when we have to, but it's typically for a very small period of time. It's usually just until that upstream maintainer tags a new release, then we can discard that patch and get right back onto the vanilla interpretation of that upstream maintainer's code. For the most part, you know, we have really good signals from maintainers who really prefer this approach. We're not creating some Frankenstein of the code that they've put their heart and soul into developing and building and maintaining. What we've done is really just taken a secure snapshot of that, and we keep it moving forward.

### Real-world Impact

So this is like a random two-hour window from a couple of weeks ago of our backend build system catching new releases. And you can see that Grafana had a fix, had a new release going from 10.4 to 10.4.16 that addressed a CVE. You can see GitLab, you can see Helm and Argo and GCP and Azure. This was just like one little piece of one page during one hour of the automation doing its work, and you can see it fixing CVEs along the way.

In fact, you can zoom in a little bit and you can see the majority of these are happening by the Octos. So the actual bot that's constantly pushing the factory and pushing the factory forward. I'll actually zoom into the status of a couple of these, and you can see that for this snapshot, these three were in progress, not yet done—that's with the amber light, five of six tests complete. You can see the ones that completed successfully, checks all the way across the board. And then you can see some ones that needed a little bit more attention. This meant that five out of the six passed, but there was something else failing in the process. That's when we get a member of our sustaining team, an engineer who has expertise in this type of problem, to dig in and figure out, you know, what's gone wrong. But we estimate almost 90% of the time this is flowing through without any human interaction whatsoever.

### Security Advisories

So we start minimal, we fast forward, the third piece of the puzzle is publishing advisories—and a lot of them. We've got a couple of different advisory repositories. This is the one that maps to Wolfi, which was the open source package repository that I showed you before. Here we have some 1,200 files which are the advisory files. These are constantly growing YAML files with something like 17,000 commits and growing every single day.

This is what an advisory looks like, and these files can go on for hundreds and hundreds of lines. But I grabbed one for containerd. Containerd will have this stanza that tags a particular unique vulnerability. You can see this is 2023 CVE-2023-45283. There's a timestamp for when it was first found. Our research—and this one did involve human research—was that it was a false positive determination, and we documented why. This particular vulnerability only affects code in Windows. This is a container that is not running—this is not containerd running on Windows. Therefore, we provide this, we publish this, we attest this, and then we feed that information to the scanners. The scanners read these advisory files, and the scanner itself is able to provide you, the customer, the user of containerd scanning containerd with better information on is this actually a vulnerability. Because it's no good if you just get this fire hose of information that is, you know, unreadable. You know, if you're overwhelmed by false positives, you really stop trusting the value of your scanner itself.

### Scanner Partnerships

This is something that you can't just DIY. You know, we're often asked, "Look, I've got a team," you know, we may be talking to a director of platform engineering, "Hey, I've got a team, they handle the vulnerability fixes." Well, what do they do? "Well, they're constantly apt-get update, apt-get upgrading our distro, and you know, we've got all the patches that the upstream distro has provided." Yeah, but what about the false positives? "Well, I mean, those we just kind of have to ignore."

Becoming a trusted source of advisory data to the actual scanner itself—that's a very privileged position. And we're delighted to partner with Snyk and Wiz and Grype and Trivy and X-Ray and Prisma amongst others as well and provide those advisories to them in a machine-readable format that's able to make the quality of that scanner information even better. If your favorite scanner isn't up here, please do come talk to the product team. We've definitely got people busy working on the right partnerships and ensuring that our trusted advisory data is accessible to them as well.

### The Build and Test Pipeline

Okay, so with all of that, we're able to build, test, sign, publish packages as soon as any upstream project tags a release. And so this is what happens. I showed you the first piece—this is what's actually happening inside of the testing. You can see these are 19 checks and growing that we run. And you can see the Wiz scanners are running, we've got Malcontent, which is running looking for malicious data that might have been injected in the build. We've got static analysis, lint analysis, as well as the actual build process. I showed you the testing that we actually execute those binaries. We check the libraries, we check the SO files, we ensure that Python modules are loadable, Ruby modules are loadable and listable. And then, you know, we've got logs that we can drill into.

### Testing at Scale

Now I really want to double down on the testing—the testing part. If I really have to talk about, you know, the place that we've invested most heavily, once we completed the initial build—build is great, but man, how do you trust a rolling distro? A distro that every time an upstream maintainer presses a release button that worked for them on their laptop, how do you trust that that's going to make its way through the Chainguard automation into production in your environment? And that is the testing.

So hopefully some people perked up at the quality part of the discussion. So I showed you some YAML files. We were going to pull GCC, all right, so a compiler. This one's now, this is a bigger build, this is 400 lines, but arguably one of the most important core critical pieces of an entire distro. We're going to zoom into this entire test section, which goes on for pages and pages. And I just pulled out one little piece for easily readable bit of C code, right? Hash includes stdio, int main, print, return zero. Doesn't do a whole lot, but this has to compile in order, you know, for the entire build to succeed. And that's not much, and there's a whole bunch of other things, but if this breaks, boy, I really don't want to get into, you know, what else is going to break. So let's fail early and fail often.

This is just one example. We've got, you know, somewhere around 3,500 open source package specifications in Wolfi itself, the vast majority of which have, you know, various degrees of testing. But that's just the functional verification—that's the FVT on the package itself.

### Image Testing

If we go into the actual image testing, this is what an image test file is going to look like. And I'll zoom into, you know, once we've actually put that image together, we go and docker run that. And this is RabbitMQ, so we're actually running the RabbitMQ image and running it through its own tests—one, two, three, four shown right here. And we do that for every single image, and we ensure that that goes all the way through before we publish that image.

In some other cases, we've actually got to start up an entire Kubernetes, and we'll use K3s or we'll use EKS in Amazon. We've got to spin up a whole Kubernetes to test some of these images. And some of these image tests take orders of magnitude longer than the actual build. We may be able to build it within the first five or 10 or 15 minutes, but it may take a couple of hours to really put a core and critical image through full testing.

### The Results: Our Image Catalog

All right, so how does that work in practice? And for those of you who might be prospects and not yet customers, maybe that sounds great, but you know, you don't believe us yet. Dan mentioned in the keynote we've got over 1,200 images. Again, these images were taken a couple of weeks ago—this was at 1,254 images, 1,200 and counting. There's a handful of different types of images that we've sort of grouped things into. We've got some customers who are more interested in the AI front, others are more interested in the base or the starter front. We've got, you know, some customers who use a single image and they start there. We've got others that leverage a handful, five or 10 images and get started. And then we've got some other customers who've gone all in on this, and Chainguard is the only way that their developers are allowed to build on, or they're encouraged to use.

### Public Image View: PostgreSQL FIPS Example

All right, so it's the factory that enables all of this at scale. Now let me show you what this looks like publicly. You could see this on images.chainguard.dev. This is PostgreSQL FIPS. This is the PostgreSQL database, this is with FIPS encryption enabled. So this is compiled against our OpenSSL FIPS libraries and ensures that if you're storing data and doing any cryptographic transactions on that data in PostgreSQL, you're doing so in accordance with the FIPS cryptography standard.

Here, starting on this page, you can see the versions. We've of course got multiple versions of that PostgreSQL FIPS image available. The latest and latest-dev are floating tags that move. You can see the dotted versions, you can see 17, 17.4, 16.8, all the way back to 15.12. You can see the last time those changed. And you know, the 24/7 rebuilding means that something inside of that PostgreSQL image changed, which meant that we had to rebuild that image because there was probably a security vulnerability somewhere in that image that needed to be addressed, and we addressed that by sucking in a newer version of that.

### Beyond Containers: Virtual Machines

Now what we heard from a number of customers over the last year was, "You know, that thing that you've done for containers, can you do that for our virtual machines and our libraries?" In particular on the virtual machine front, we had some customers who said, "Look, this is great. We've deployed Chainguard everywhere we can deploy it inside of the containers, but those containers are running on Amazon Linux hosts in AWS or EKS. They're a couple of years old, there's hundreds of unpatched vulnerabilities. I feel great about my container estate, but what about the thing running under my containers? And I've got hundreds of thousands of those."

So the first one to mention is that same factory—everything that I've talked about that powers the packages and the images front—we've extended to also produce virtual machine images. That meant that we had to add a couple of packages we didn't have before: a package called linux.yaml, which tracks Greg Kroah-Hartman (Greg KH)—he's the maintainer of the security stable tree, the LTS and the stable tree in the Linux kernel. Within minutes of Greg tagging a new release of Linux the kernel that fixes a CVE, our automation catches that and rebuilds that kernel on two different architectures across three clouds, as well as VMware and QEMU—so five different environments—and is constantly rebuilding that and applying, you know, multiple different kernel configs, hardened kernel configs on it.

We also had to add systemd, which is how a Linux system typically boots and manages the processes on it. And then for our initial target use case for this virtual machine image, we've targeted the container runner. So back to that customer feedback: "You've helped us with all of our container images, what about the thing running under the containers?"

So as of today, we've announced we have a Chainguard virtual machine running in Amazon EKS. You can bring your own node running Chainguard VM with a Chainguard hardened kernel, systemd, containerd, the cloud agents, the Amazon agents as well. And the other clouds are works in progress right now, as well as other formats.

### Libraries: Starting with Java

The other piece are our libraries. And we started very much with Java. The signal that we got was Java was the biggest pain point in some of the enterprise, especially financial services, healthcare, government organizations. And this idea that everything that these technologists are getting from a trusted source is great, but there's this other realm of dependencies that aren't as well understood yet, perhaps by the scanners number one, and by their developers number two. But I can guarantee you that the malicious actors out there in the world absolutely know about this. And you know, there's a long list of bodies, a trail of bodies where pulling in code from an untrusted third party has created real vulnerabilities.

So we've started rebuilding Java itself—Java archives, JARs—from source. To date, we've got 20,000 JARs, which include from our analysis the most heavily depended upon JARs across the last five years. And this covers about 98, 99% of the most used JARs over the last five years in dependencies. If it's not on the list, we can—we have a process by which we can add others as well. Java is the start. We're working on Python next. PyPI is the next target. That's a work in progress, and definitely come talk to us if you're interested in that.

### The Chainguard Operating System

So that's containers, VMs, libraries, all built from source the hard way. It's that same factory that I've spent the last 30, 40 minutes talking about cranking through that. And then ultimately it's the Chainguard operating system that's powering all of this. It's at the core of it. It's not the value that we project as, you know, the thing that we've built, but it's the thing behind what we've built that enables all of this to go and go really fast.

### A Personal Story

So I thought I would tell you one little story, and this is pretty much the end of the presentation. I grew up in South Louisiana, and I was about 10 or 11 years old, and my uncle invited me to come help him dig a well—a water well. And I remember this like it was yesterday. Has anyone ever dug a well before? Wow, okay. I'm going to tell you how digging a well in South Louisiana works.

First of all, it's a lot of people, and this was very manual labor. It starts with a drill bit that's about this big and probably cost $20,000, okay? And then you attach to that drill bit a galvanized pipe, 10 foot long galvanized pipe, and you attach two pipe wrenches to it at 180 degrees, and you have two people that walk around in a circle and make that go down 10 feet. And when it goes down 10 feet, guess what you do? You take a galvanized coupler, you put another 10-foot pipe on the top of that, and you attach the pipe wrenches and walk around in a circle. And you do that 20 times because you need to go 200 feet deep to get to water, the water table in South Louisiana.

Now, thankfully we're drilling through swamp and not mud, and so that's why two humans can walk around in a circle. When you're done, you're not done, because remember that $20,000 bit I told you about? You got to get that back out of the ground. How do you get it back out of the ground? You walk all 20 of those pipes up, and then you replace the bit with—I forgot the name of it—but the filter you put at the bottom, and then you go right back down. It's a little easier going the second time around.

What I learned from this is that there are some things in life I love doing myself, and there are some things in life I do not love doing myself. And accessing drinkable water is one of those. The other one is security. Security is definitely something that I think if you can trust someone who's really good at doing what they do, you'll end up in a much better place. I hope that we, Chainguard, can be that for you. That's the end of my talk. 

[Applause]

### Q&A Session

**Sam**: Thank you, Dustin. We got about 10 minutes for questions. I believe we have somebody with a microphone, so I'll go ahead and open up the floor if anybody has any questions on what you just heard. We got some in the front here.

**Question 1**: Short and sweet—Twistlock. I didn't see it on the slide. I think there's a ton of presence in APAC. We'd love to see support for that.

**Dustin**: Twistlock, yes, on the scanners for sure. Very familiar with it. I know that we have some customers—we've got a list of things that we typically require doing in order to ensure that we can fully certify that. But Twistlock is definitely a common one. I think the driving reason was that I think Go series were not getting captured by active scan, and then a lot of time Twistlock was picking them up. Okay, one of the reasons. Noted.

**Question 2**: How do you skip some of those vulnerabilities from the scanners? Like you have mentioned that some of the vulnerabilities you are making some modifications which will—the scanners will not be able to find those, right? So one of that file which you are showing...

**Dustin**: So we ingest the CVE and the GHSA from GitHub and the National Vulnerability Database, so those are feeds that we consume. We run that through—I guess I didn't show that part of the factory—but yes, there's an ingestion piece. As soon as a vulnerability, especially a Go vulnerability gets published, we take that. That does typically hit a person, you know, hits a human who analyzes that. We'll rescore it. You know, there are places where things are certainly more severe than they're thought to be upstream. There are places where it might be super severe on Windows but is not applicable to us, so you know, we can raise and lower that. That's what drives the CVE automation side of things is consuming information from those feeds. The scanners also consume that information as well, and then what they have to do is map that against a whole bunch of different operating systems and versions and so forth. So part of working with Twistlock is ensuring that Twistlock understands Chainguard, our packaging system, our versioning system, and then ultimately our advisory feed format.

**Question 3**: Nice job, Dustin. The testing—so the unit tests and all the automated tests you showed, is that something you guys are maintaining yourselves or you're deriving from open source or some combination? Maybe you can talk through how you're building up the tests over time?

**Dustin**: Great question. Bit of both. Where there is an upstream test harness, we should be running that. And sometimes it's configure, make, make install, make test. We can do that, and that would fail at the build step. The runtime tests are largely things that we've generated or written ourselves. Some of it's automatically generated. If you had eagle eyes and you could see many of those were running whatever the binary is --help and --version, which doesn't do a whole lot functionally, but you know what has to happen in order for that thing to run? The linker, the loader, all of that had to work. And there are certainly cases where if you don't compile a thing right, running foo --version is just going to fail out. So we call those sniff tests. A couple of scripts that we created generated thousands of those, and that gave us at least a starting point to know that you can run vim --help. Now that's actually not editing a file, but in order for vim --help to work, it has to link against all of those binaries. There's a whole bunch of others that are much more sophisticated that configure, make file—sorry, that GCC hello world file. There are a bunch of others that, you know, with a little bit of sophistication you can test it out, you can run a thing and grep for some output, and we've created a bunch of those manually as well.

**Question 4**: So you've mentioned a lot of manual efforts around all these packages and writing the tests and making sure the CVEs rescore—that's like a lot of humans in the loop. How do you actually scale that, or do you even plan to trust AI/LLMs? How much do you trust them to do all of this work?

**Dustin**: Yeah, it may seem like a lot of humans. It's not. I mean, the entire engineering team at Chainguard is just about a hundred people. I think we're doing the work of 10,000 people using the automation. I would compare that to, you know, Debian, another distro that I've been involved in for a very long time. There are one or more human maintainers tied to every single Debian package. There's 25, 30,000 Debian packages with 25 or 30,000 or more emails associated with every one of those packages. And only a maintainer whose key has been signed as a Debian maintainer in the, you know, GPG root of trust in Debian can upload. That's not how we've designed Chainguard the OS. We've designed it without an individual being responsible for any package. Do we have people who are experts at what they do? Yes, absolutely. If there's a GCC FIPS bug, it's going to be Dmitri or Luca Cage who fixes that. For sure, we love them for it, but their name is not exclusively tied to that. So yeah, I appreciate the question, but I mean, I think the automation that we have is overwhelmingly driving what we do. 

The second part of the question though, I think is smart though, and we are leaning into AI in certain places, especially for the debugging. So when something fails, Octos is able to query a couple of the AI engines, Gemini especially, and it looks at it and often makes suggestions on how to fix it. So the first thing a sustaining engineer does when they're looking at a build failure is look at what our trained models tell us could be the problem. And when it's right, we give it a thumbs up, and that retrains and improves the model. When it's wrong, we can give it a thumbs down, and you know, we can bury that suggestion in the future.

**Question 5**: Hi, my question is related to testing again. When you're building a Docker image, maybe depends on a bunch of packages, libraries. So how do you detect the incompatibility between the software versions, and then when you detect it, how do you fix—what, how do you find the right combination?

**Dustin**: Yeah, so I actually didn't go into—if we go back to the factory analogy—I didn't go into the order intake side of things, which is when a customer comes with a list of images, Docker images that they need that we don't have. So I showed you the 1,254 and counting that we do have, but that's not all of them that we need. And so we'll end up with a customer or prospect who says, "Yeah, you've got these, but we have all of these that we don't have yet."

So what happens is we take those requests, and those go to a different engineering team we call it the delivery team. And that team looks at the customer's request for images that we don't have and we've maybe never seen before—maybe we've seen it, it's on our backlog, but we might have never seen. And then that delivery engineer—it is a very human process to build an image the first time. Sometimes that means packaging software that we've never packaged before and creating an image for something that we've never created an image for. In some cases, there's a reference Docker image that we can go and look at at Docker Hub or somewhere else. In other cases, it's just a git repo. A customer says, "Look, we start with an Alpine base or Debian base, and our developers are git cloning this thing that we don't know anything about, but we would love to have a hardened image and resilient against CVEs."

So the human creates it for the first time, and after that it's constantly rebuilding, and the automation takes care of that. Only when it fails does a human have to get involved the second time. And the testing—we have continued to raise the standards on what it takes to publish that image the first time and ensure that the testing is in place. It's—that's a hard one. It's complicated, and we're not able to automate all of that yet.

**Question 6**: Yeah, so you guys are building like a lot of images and packages like all the time. What's your underlying build system? Is it all GitHub Actions or Surface CI?

**Dustin**: Yeah, good question. It's a lot of GitHub Actions. The builds—or excuse me, are you self-hosting those or using just GitHub's built-in?

We use GitHub. The builds actually take place in GCP largely. The tests happen in various clouds—AWS, EKS—where we need it. The libraries product is using a lot of Argo CI, you know, to build those at scale. We test with Cloudsmith there. Cloudflare is typically the CDN side of things for images. Yeah, I didn't get into some of the underlying tech, but yeah, happy to tell you more if you need it.

**Sam**: Cool, thank you. Will you be at the expert table?

**Dustin**: Yeah, sure.

**Sam**: Thank you. If we just want to give Dustin one more round of applause.

[Applause]
