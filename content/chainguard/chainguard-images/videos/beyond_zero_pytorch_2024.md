---
title: "Beyond Zero: Eliminating Vulnerabilities in PyTorch Container Images (PyTorch 2024)"
linktitle: "Beyond Zero at PyTorch 2024"
lead: ""
description: "Video and transcript of presentation at PyTorch 2024 on eliminating CVEs in the PyTorch image, drawing on best practices from Chainguard Images"
type: "article"
date: 2024-09-07T01:21:01+00:00
lastmod: 2024-09-07T01:21:01+00:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 400
toc: true
---

{{< youtube 1klynk1dxYA >}}

---

Recording of [Beyond Zero: Eliminating Vulnerabilities in PyTorch Container Images](https://pytorch2024.sched.com/event/1fHmE/lightning-talk-beyond-zero-eliminating-vulnerabilities-in-pytorch-container-images-patrick-smyth-dan-fernandez-srishti-hegde-chainguard) presented by Dan Fernandez, Srishti Hegde, and Patrick Smyth at [PyTorch 2024](https://pytorch.org/blog/pytorch-conference-2024-recap/)

## Session Description

Container images are increasingly the future of production applications at scale, providing reproducibility, robustness, and transparency. As PyTorch images get deployed to production, however, security becomes a major concern. PyTorch has a large attack surface, and building secure PyTorch images can be a challenge. Currently, the official PyTorch runtime container image has 1 CVEs (known vulnerabilities) rated critical and 5 CVE rated high. Improving this situation could secure many deployments that incorporate PyTorch for cloud-based inference or training. In this fast-paced session, we tooka deep dive on the official PyTorch image from a vulnerability mitigation perspective, looking hard at included packages, executables, and active CVE. We identify low-hanging fruit for increasing security, including stripping bloat and building fresh. We also talk about the next level of security practiced in Chainguard's PyTorch image builds, such as including SBOMs and going distroless. Finally, we consider emerging tools and approaches for analyzing AI artifacts such as models and how these systems can benefit PyTorch in production.

## Resources from this Video

- [PyTorch Chainguard Image](https://images.chainguard.dev/directory/image/pytorch/overview)
- [Course: Securing the AI/ML Supply Chain](https://courses.chainguard.dev/securing-ai) <!--  -->
- [Learning Lab: Chainguard's AI Images](https://www.chainguard.dev/events/chainguards-ai-images)
- [Chainguard Academy: Getting Started with the PyTorch Chainguard Image](https://edu.chainguard.dev/chainguard/chainguard-images/getting-started/pytorch/)
- [Overview: Chainguard's AI Images](https://www.chainguard.dev/solutions/ai-images)

## Transcript

(Dan Fernandez) Good afternoon everyone and thank you for joining us. We're going to be presenting Beyond zero: eliminating vulnerabilities in the pie torch container image. This is a an effort that concluded a couple months ago that focuses on minimizing vulnerabilities in the PyTorch container image. But first my name is Dan Fernandez, I'm a product manager at a company called Chainguard today I'm joined by Patrick Smith who's a staff developer relations engineer at Chainguard and Srishti Hegde who is a delivery engineer.

We wanted to start by going over a little bit about why containers are also ideal for AI applications just like they are for other applications and it has to do with a few of their properties such as their portability so you have a consistent development and production environment. They also offer efficiency, allowing you to scale with growing demands and lastly they offer some isolation (not full isolation) and this encapsulation of apps in general that is consistent across environments also allows for the possibility of hybrid workloads which a lot of large organizations are starting or continuing to transition into. We also wanted to share some metrics around the overall adoption of containers for AI applications. As of the end of 2023 there was a 58% increase  of GPU instance hours usage. This was by a report from data dog and this has to do with the increase in the need for both training and inference workloads associated with GenAI applications.

There's also an interesting metric here, and this is more of a forecast, but while AI components have not made it to every Enterprise application (even though it sure feels like it has) it is estimated by 2025 90% of most Enterprise applications will have some AI component within them. And lastly the hosting or the spend for cloud resources associated with Cloud applications is estimated to be $200 billion dollars by the end of 2030, this was by a Cloud Revenue estimate offered by Goldman Sachs.

So this kind of gives you an idea of why we decided to focus on this, but obviously we're at the PyTorch conference and we wanted to highlight that really the the important part here is that PyTorch has a key role in the AI supply chain and this is because it has widespread use for both deploying and developing models. The flexibility, the strength of the community, and the ease of use has made it one of the most popular container images across the board and that that means that it has now become the foundation to a lot of libraries and projects.

Due to the far-reaching scope and use cases for this specific technology, it now also means that the attack surface for AI applications via PyTorch has also increased significantly over time. So any organization or any Enterprise that is deploying an AI application that is concerned with data privacy also now has to be concerned with maintaining all the components, in this case container images, making sure that they're up to date. And that's what we're going to focus on the rest of this presentation. Patrick is going to walk us through some of the metrics around vulnerabilities associated with the PyTorch image

(Patrick Smyth) All right, thanks Dan! So PyTorch has been downloaded over 10 million times in the last year and so you know this is an application that really matters because if you secure the PyTorch container image you're securing literally millions of deployments across the planet. So let's dig a little bit into to PyTorch in terms of security.

The last build of the PyTorch container image had 1 critical, 5 high, 40 mediumand over 50 low CVEs. You might be like hey that sounds like a lot. That's actually not that far off industry standard which is you know maybe even slightly unfortunate. <laughs>

Unfortunately, CVEs do really matter. What are CVEs? They are Common Vulnerabilities and Exposures. They are known vulnerabilities in software that actually affect the security posture of that software and CVEs can be looked up in a database so these are vulnerabilities that can, should,  and in some cases must (in the case of for example fed ramp compliance) be remediated. So if you're doing FedRAMP you need to fix them within a month. 

So unfortunately there's an upstream problem. If you're someone who wants to run a model in inference, wants to develop an application, then probably about maybe 2% of the CVEs that are in that application, that code, or that production deployment might be introduced by your team. The rest come from Upstream, whether they be language runtimes or whether they be OSes. As the person at the end of that you're responsible for it. 

But how do you fix all of that? It becomes very difficult. You have to employ cve remediation teams and so on. So at chain guard we create low to no, frequently zero, CVE images. And how do we do that? We do a couple of different things. We build fresh. We patch when needed. We issue advisories and we really strive for the images to be as minimal as possible. And when you're aiming for zero every removed package really matters because every package is a potential source of CVS that could pop up literally any day.

So in terms of zero—well, is zero just a marketing thing? I mean maybe some of you have used CVE scanners. Maybe you've played around with this or maybe you're responsible for this. You may never have actually seen a scan comeb back zero CVS. When I joined Chainguard I was like is this just marketing? But actually we work really hard at this. We do it every day, and we actually do get to zero CVEs, which is kind of remarkable. And I'm still surprised by it. But it's possible. <laughs>

So let's get a little into the nitty-gritty. So just to talk about "minimal" for a minute. This is a comparison of the attac surface of the current PyTorch image versus the recently built Chainguard PyTorch image. I'm speaking specifically about the runtime PyTorch image here. So if you look  we have about 75 packages in the Chainguard PyTorch image versus about 200 in the current PyTorch image and we have about 400 executables versus 1400 in the current PyTorch image. I'm going to hand things over to Srishti so she can go into a little more detail.


(Srishti Hegde) Thank you. So talking about the minimal set of packages, what it really means is a reduction in the image size. And, case in point, our Chainguard PyTorch image is actually only half the size of the Upstream image you see there. 

So talking about how we arrived there, there are a couple of things. We ship a prod and a Dev variant of the image, and within our prod variant we've stripped a lot of things. That's your shell, development utilities, diagnostic tools, and Network libraries. We've also tried to greatly reduce the complexities introduced by package managers by stripping them down to the bare minimum. 

But not all use cases are production use cases. There are cases where you need to have access to development tools.  So you can always use the dev variant of our image, which has access to a larger set of Dev utilities. I think one of the biggest challenges we had in arriving at this place is the very complex version Matrix of all the components that together constitute torch. And as many of you might know, most of them are quite tightly coupled and it's down to the tool chain that's actually used to build torch. There's a lot of back and forth involved. I think as of now the Upstream PyTorch Cuts a release every 5 weeks or so. Every time a new release comes out Chainguard Builds an image for this particular variant in all versions of Python that's supported. These images are constantly scanned and patched whenever there's a CVE that shows up. And our images are built nightly, so really they're fresh as they come.

In addition to zero CV and minimal images we also build FIPS- compliant images. So a number of you might have a requirement for these images as well. Though we have a very minimal set of packages it's always good to know what's actually running in your system. To that end the PyTorch image that we ship out comes with an SBOM that tells you what's in the image.

The PyTorch image, just like all the other Chainguard images, is compliant with the SLSA standards, which means that you get a verifiable history of the build, giving you information about how the image was built, including the dependencies that went into it, the source code, and the build system itself.

(Patrick Smyth) We wanted to provide you with a couple of starting places. So if you're interested in taking a a test drive of the recently built zero CVE PyTorch image, you can take a look at this QR code on the left, that's our PyTorch image there in our image catalog. Another great place to start is the recently released Securing the AI/ML Supply Chain course, which has seven modules that cover all sorts of different things from the compliance ecosystem to tooling and scanning and also some training and inference. It's a great place to start. Similarly, we do a monthly Learning Lab focused on different secure application Frameworks and language runtimes. I just did one on our AI images including PyTorch. If you want to check out the next one coming up you can scan this QR code. 

This is Wolfi, the tiniest octopus in the world. (We go for minimal here.) You can see him going into his hole. Before we get to questions, I'll just say that the techniques we've discussed here, from building fresh (going from every five weeks to every night), including SBOMs, going minimal—these are all things that could be applied to the current PyTorch image to make it more secure. And that could really affect security in production environments around the world. Thank you all.
