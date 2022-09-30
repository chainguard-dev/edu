---
title: "WTF is a Typo Squatting Attack?"
lead: "What really happened with GitHub’s typo squatting attack?"
description: "GitHub’s typo squatting attack"
type: "article"
date: 2022-08-01T15:21:01+02:00
lastmod: 2022-08-01T15:21:01+02:00
draft: false
images: []
menu:
  docs:
    parent: "software-security"
weight: 10
toc: true
---

{{< youtube nB3xw3Nazgc >}}

<br>
Hi, I’m Dan Lorenc, CEO & Co-founder of Chainguard and I’ve been working in the open source software supply chain security space for a long time.

Today, we’re going to recap the massive typo squatting attack that was carried out against a bunch of open source projects on GitHub on August 3, 2022. 

Typosquatting is a type of attack where an attacker changes the name of a real project subtly to make it look like that project but it's not actually the same repository or package and it is really hard to detect because there are a lot of subtle ways to do it. You can change underscores to hyphens, mess around with Unicode characters, plurals, just to name a few. 

On August 3, a tweet went viral about over 35,000 fake repositories created cloning after real projects, things like Kubernetes, cryptography, libraries, and programming languages, all designed with very similar names. This got a little bit over sensationalized because of the scale of the attack until everyone found out what really happened. 

Fortunately, this was caught early, so no malicious commits are actually found in real projects. That's where a lot of the confusion came from. Only malicious code slipped into these imposter repositories. Typically, there's a second phase of these attacks where developers may unknowingly use the malicious fake repository’s code, thinking it was the real one, thus compromising their project. Thankfully, though, this one was caught in the middle, so nothing bad actually happened. 

But we don't know how bad this one really could have been if it hadn't been noticed and played out for longer. This attack was the largest and most advanced I've seen so far. The scale of over 35,000 repositories showed some clear automation. The malicious commands were slipped in and hidden inside of real ones and they were all semantically correct, too. So it'd be tough to catch, if you were just casually looking around. 

So what can you do to protect yourself against stuff like this?  
There's a couple of different ways:

As an end user, pay very close attention to your dependencies, it's going to be hard to notice typosquatting attacks like this, but these are all very recently created repositories with very few stars and little activity as a maintainer. 

To prevent someone from creating an imposter repository, the only protection really available today is to sign your commits. There's a bunch of different tooling to do this, including a new one called Gitsign, it's part of the Sigstore project. None of these are perfect and solve it completely. But if you pay enough attention, and if enough people start signing their commits, it will be easier for us to detect these across the open source ecosystem at scale.