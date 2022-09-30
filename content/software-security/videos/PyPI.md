---
title: "WTF happened with the PyPI phishing attack?"
lead: ""
description: "The PyPI phishing attack and multi-factor authentication"
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

{{< youtube IvxWXk5jSsc >}}

<br>
On 8/24/22, PyPI, an open source repository of software for the Python programming language, announced an active phishing campaign targeting PyPI users. How did it happen and how can we prevent future attacks? Let’s recap: 

Before we cover the phishing attack, it’s worthwhile to mention that on July eighth, PyPI announced it would require the implementation of two-factor authentication (2FA) for projects deemed critical — that is, any project in the top 1% of downloads of the past 6 months. It is a huge step forward for open source security, and as of August twenty-fourth (today/yesterday), nearly ~30k PyPI maintainers have 2FA enabled. 

About a month and a half later, on August, twenty-fourth, PyPI tweeted that they had reports of phishing, or fake emails, that appeared to be from PyPI requiring a mandatory validation process which led users to a fake login page. When the user went to enter credentials, they were stolen. 

Legitimate projects have been compromised, and malware published as the latest release for those projects. PyPI has already taken down several hundred typosquats of the malicious releases. 

It’s important to note that accounts protected by hardware security keys, the strongest form of 2FA, are not vulnerable. It is currently unclear if timed-based one-time passwords (for example a one-time use SMS pin) were affected. 

What happens now?

PyPI is actively reviewing reports of new malicious releases, and ensuring that they are removed and the maintainer accounts restored. They are also recommending to reset passwords and 2FA recovery codes if you have entered your credentials to the phishing site. 

This attack highlights the importance of MFA, especially hardware or WebAuthn 2FA. 
Hardware keys are not vulnerable to these types of attacks because, in order to authenticate with it, you physically have to have the key, which makes it impossible for attackers to get the information they need to log in from afar. [Dan to show a Yubikey]. 

PyPI is run largely by volunteer maintainers who are working to make the open source ecosystem more secure. Having checks in place that may require a small amount of time for individual maintainers to set up can have an outsized impact on the overall wellness of the software supply chain. 

If you haven’t already, enable 2FA at https://pypi.org/2fa/ and shout out to the PyPI team for their transparency and their continued efforts toward keeping open source more secure! 
