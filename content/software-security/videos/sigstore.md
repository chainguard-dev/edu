---
title: "WTF is Sigstore?"
lead: ""
description: "Sigstore explained in 2 minutes"
type: "article"
date: 2022-08-01T15:21:01+02:00
lastmod: 2022-08-01T15:21:01+02:00
draft: false
tags: ["VIDEO", "CONCEPTUAL"]
images: []
menu:
  docs:
    parent: "software-security"
weight: 10
toc: true
---

{{< youtube veiCVgDpYcY >}}
<br>
Let’s talk about software supply chain security. 

Vulnerabilities and attacks in software have been increasing in recent years, and the U.S. government recently passed a Bill in the House that would forbid the Department of Defense (DoD) from procuring any software applications that contain a single security vulnerability or CVE (short for common vulnerability or exposure). Attacks and other security issues can exist all across the software supply chain, from the dependencies or packages you leverage in your code, to the code you write, to your deployment and integration strategy, to your packaging. 

With so many opportunities for attack vectors and vulnerability risks, what can software developers do?

Luckily there is an open source solution that can help with mitigating some of these security concerns. It’s called Sigstore, and it offers a suite of tools that provides a new standard for signing, verifying and protecting software. Sigstore handles digital signing, verification and checks for the provenance needed to make it safer to distribute and use open source software.

So what does that all mean? Let’s use a in real life example:
If you’re going to a concert that has an age restriction, or you want to open a new bank account, someone is going to ask you for your ID. Neither the concert venue nor the bank issued you this ID, probably a national or local governmental body did. But your ID still attests to your identity and the venue or bank will accept this ID as your identity because of the trust root that exists with this ID-issuing authority. In the case of the bank account, once you open it, your bank account number will now be part of a database or log that is connected to your identity. This is similar to how Sigstore works, bringing identity (your ID), a certificate authority (the governmental body that issued your ID), and a transparency log (bank account database) together to enable verification and trust to exist at each step of the software supply chain.

We’ll break down how this happens with each part of the Sigstore project (Cosign, Rekor, Fulcio, and Gitsign) in upcoming videos so follow for more!

Cosign
Cosign is a tool that helps make software more secure. Part of the Sigstore project, Cosign supports container signing, verification, and storage in an OCI (open container images) registry. Cosign makes it so that code signatures can be a part of invisible infrastructure.

If we think about something physical that we want to keep secure, we may think of keys and a lock. Cosign lets developers generate a key pair with a private signing key that only you have access to, and a public verification key that can be stored with the software or in a transparency log. These keys are attached to the software artifact as a signature when it is released (whether that’s as a package, binary, container, whatever). Once that software is out in the world, another developer or user can verify the claims of the signature by checking that the public key matches up with the claims. 

We can also think about Cosign as like a wax seal on old paper letters. When someone — say a queen or public official — wrote a letter that needed to be secured, they would close up the letter and drip wax on it, then stamp into it with their seal or emblem. This would let the person who receives the letter know that the letter is from whom it claims to be from, and also that that letter wasn’t tampered with, which the recipient would know if the wax seal was broken. 

Another neat thing about Sigstore is that it enables keyless signing, meaning you don’t need to generate a key pair but can use an OIDC (OpenID Connect) protocol to authenticate your identity instead. This can currently be done through Google, GitHub, or Microsoft, and it will tie your identity — based on an email address or username — to the code you are signing.

We’ll go into the rest of the Sigstore suite soon — including certificates, transparency logs, and signing Git commits — so follow for more!
