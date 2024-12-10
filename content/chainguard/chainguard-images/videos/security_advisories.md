---
title: "How to use Chainguard Security Advisories and the Diff API"
linktitle: "Chainguard Security Advisories & Diff API"
lead: ""
description: "How to use security advisories and the diff API to investigate vulnerabilities
affecting Chainguard images"
type: "article"
date: 2024-01-18T01:21:01+00:00
lastmod: 2024-12-06T15:16:50+01:00
draft: false
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 030
toc: true
---

{{< youtube ExZxIWmnm1s >}}

## Updated Written Article

You may wish to refer to the up-to-date written article covering the same material as this video:

 [How to Use Chainguard Security Advisories](/chainguard/chainguard-images/security-advisories/)



## Tools used in this video

* [Chainguard Security Advisories](https://images.chainguard.dev/security?utm_source=cg-academy&utm_medium=website&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-videos-security_advisories)
* [chainctl](/chainguard/administration/how-to-install-chainctl/)
* [Docker](https://docker.com)
* [Docker Scout](https://docs.docker.com/scout/)

## Transcript

<a href="https://youtu.be/ExZxIWmnm1s?t=5" target="_blank">0:05</a> So a question we sometimes get asked is how to investigate vulnerabilities found in Chainguard images and how you can figure out if there's a fix

<a href="https://youtu.be/ExZxIWmnm1s?t=15" target="_blank">0:15</a> so thanks to a new website and some new tooling this is pretty

<a href="https://youtu.be/ExZxIWmnm1s?t=19" target="_blank">0:19</a> straightforward so in this example we're

<a href="https://youtu.be/ExZxIWmnm1s?t=21" target="_blank">0:21</a> going to look at a slightly old golang

<a href="https://youtu.be/ExZxIWmnm1s?t=23" target="_blank">0:23</a> image and if we run Docker Scout or a

<a href="https://youtu.be/ExZxIWmnm1s?t=26" target="_blank">0:26</a> similar scanner we do get some results

<a href="https://youtu.be/ExZxIWmnm1s?t=31" target="_blank">0:31</a> so you can see in this image we found 11


<a href="https://youtu.be/ExZxIWmnm1s?t=35" target="_blank">0:35</a> vulnerabilities and we're going to

<a href="https://youtu.be/ExZxIWmnm1s?t=37" target="_blank">0:37</a> investigate this one 2023

<a href="https://youtu.be/ExZxIWmnm1s?t=42" target="_blank">0:42</a> 44487 and we can see we're interested in

<a href="https://youtu.be/ExZxIWmnm1s?t=45" target="_blank">0:45</a> the nghttp2 package so I'm going to

<a href="https://youtu.be/ExZxIWmnm1s?t=50" target="_blank">0:50</a> copy that and I'm going to move to a

<a href="https://youtu.be/ExZxIWmnm1s?t=56" target="_blank">0:56</a> browser and here I have opened images.chainguard.dev/security and I can search by

<a href="https://youtu.be/ExZxIWmnm1s?t=62" target="_blank">1:02</a> that cve so that comes up. If I click

<a href="https://youtu.be/ExZxIWmnm1s?t=66" target="_blank">1:06</a> into this I can filter by packages so if

<a href="https://youtu.be/ExZxIWmnm1s?t=69" target="_blank">1:09</a> I put in nghttp2

<a href="https://youtu.be/ExZxIWmnm1s?t=72" target="_blank">1:12</a> we can see that comes up

<a href="https://youtu.be/ExZxIWmnm1s?t=75" target="_blank">1:15</a> here and interestingly we can see see

<a href="https://youtu.be/ExZxIWmnm1s?t=79" target="_blank">1:19</a> the status is fixed it's fixed in

<a href="https://youtu.be/ExZxIWmnm1s?t=81" target="_blank">1:21</a> version 1.57 point0 r0 um and this

<a href="https://youtu.be/ExZxIWmnm1s?t=85" target="_blank">1:25</a> happened a while ago on October the 11th

<a href="https://youtu.be/ExZxIWmnm1s?t=89" target="_blank">1:29</a> so now now I'm fairly

<a href="https://youtu.be/ExZxIWmnm1s?t=94" target="_blank">1:34</a> sure that that vulnerability will be

<a href="https://youtu.be/ExZxIWmnm1s?t=96" target="_blank">1:36</a> gone because the image will have been

<a href="https://youtu.be/ExZxIWmnm1s?t=97" target="_blank">1:37</a> updated and indeed there we see there's

<a href="https://youtu.be/ExZxIWmnm1s?t=100" target="_blank">1:40</a> no vulnerabilities detected but we can

<a href="https://youtu.be/ExZxIWmnm1s?t=102" target="_blank">1:42</a> do bit more than that with a new diff

<a href="https://youtu.be/ExZxIWmnm1s?t=104" target="_blank">1:44</a> API we can actually look into the

<a href="https://youtu.be/ExZxIWmnm1s?t=106" target="_blank">1:46</a> differences between the 121.2 image and

<a href="https://youtu.be/ExZxIWmnm1s?t=109" target="_blank">1:49</a> the 121.5 image um this will take a

<a href="https://youtu.be/ExZxIWmnm1s?t=113" target="_blank">1:53</a> little moment to run note that I've

<a href="https://youtu.be/ExZxIWmnm1s?t=115" target="_blank">1:55</a> piped this through jq to format the

<a href="https://youtu.be/ExZxIWmnm1s?t=117" target="_blank">1:57</a> output and I've also saved it out to

<a href="https://youtu.be/ExZxIWmnm1s?t=119" target="_blank">1:59</a> file um so we can scroll through it and

<a href="https://youtu.be/ExZxIWmnm1s?t=122" target="_blank">2:02</a> see the output and look at it a little

<a href="https://youtu.be/ExZxIWmnm1s?t=124" target="_blank">2:04</a> bit easier so if I open this

<a href="https://youtu.be/ExZxIWmnm1s?t=128" target="_blank">2:08</a> file and we look at the bottom what we

<a href="https://youtu.be/ExZxIWmnm1s?t=131" target="_blank">2:11</a> have here is a list of the

<a href="https://youtu.be/ExZxIWmnm1s?t=133" target="_blank">2:13</a> vulnerabilities that have been removed

<a href="https://youtu.be/ExZxIWmnm1s?t=135" target="_blank">2:15</a> between the two versions of the image so

<a href="https://youtu.be/ExZxIWmnm1s?t=138" target="_blank">2:18</a> in this list I should see that 4487

<a href="https://youtu.be/ExZxIWmnm1s?t=140" target="_blank">2:20</a> indeed it's here we're saying this cve was


<a href="https://youtu.be/ExZxIWmnm1s?t=144" target="_blank">2:24</a> addressed and also if we search for NG

<a href="https://youtu.be/ExZxIWmnm1s?t=148" target="_blank">2:28</a> http2 we find it here and we see the

<a href="https://youtu.be/ExZxIWmnm1s?t=152" target="_blank">2:32</a> version has been updated so in the in

<a href="https://youtu.be/ExZxIWmnm1s?t=156" target="_blank">2:36</a> this version of the image we're running

<a href="https://youtu.be/ExZxIWmnm1s?t=159" target="_blank">2:39</a> on a newer version of
nghttp2

<a href="https://youtu.be/ExZxIWmnm1s?t=162" target="_blank">2:42</a> which is why that vulnerability has gone

<a href="https://youtu.be/ExZxIWmnm1s?t=164" target="_blank">2:44</a> away so there you have it that's how you

<a href="https://youtu.be/ExZxIWmnm1s?t=167" target="_blank">2:47</a> can investigate CVEs and find out how

<a href="https://youtu.be/ExZxIWmnm1s?t=170" target="_blank">2:50</a> they were addressed and Chainguard

<a href="https://youtu.be/ExZxIWmnm1s?t=171" target="_blank">2:51</a> images please do give this a go and let

<a href="https://youtu.be/ExZxIWmnm1s?t=174" target="_blank">2:54</a> me know how you get on
