---
title: "Infamous Software Vulnerabilities"
description: "An overview a few of the most critical, widespread, and impactful known software vulnerabilities"
lead: "An overview a few of the most critical, widespread, and impactful known software vulnerabilities"
type: "article"
date: 2023-07-21T19:16:39+00:00
lastmod: 2023-07-21T19:36:09+00:00
contributors: ["Michelle McAveety"]
draft: false
tags: ["Overview"]
images: []
menu:
  docs:
    parent: "cves"
weight: 003
toc: true
---

[Software vulnerabilities](/software-security/cves/cve-intro/) vary in their severity – some are difficult to exploit and have minimal implications, while others can be exploited easily and give an attacker significant leverage over a computer system. In cases where widely-implemented software contains high-severity vulnerabilities, the damage caused by their exploitation can affect millions of developers and services worldwide.

In this article, you will learn how the KEV Catalog tracks known exploited software vulnerabilities, and how it serves as a tool for developers and federal agencies. In addition, you will explore Log4Shell, Heartbleed, and Shellshock, three infamous software vulnerabilities which have had major impacts on software security worldwide.


## CISA KEV Catalog

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) operates the Known Exploited Vulnerabilities (KEV) Catalog, which is populated with CVEs that have existing exploits “in the wild”. The KEV Catalog serves as a tool for developers as it identifies CVEs that need to be prioritized for remediation because of their exploitability status. Federal civilian executive branch agencies [must remediate vulnerabilities](https://www.cisa.gov/news-events/directives/binding-operational-directive-22-01) present in the KEV Catalog by a due date specified by the CISA. Focusing on patching out these vulnerabilities limits the ability of attackers to find a potential known route into a system.

Some of the vulnerabilities in the KEV Catalog are infamous for the impacts of their exploitation. When a vulnerability affects a piece of software present in an array of systems, its exploitation can reach far and wide, and efforts to remediate it can be difficult to fully implement. The following vulnerabilities are present in the KEV Catalog and serve as examples of how damaging ubiquitous software vulnerabilities can be.


### Log4Shell (CVE-2021-44228)

[Log4Shell](https://nvd.nist.gov/vuln/detail/CVE-2021-44228) is a vulnerability impacting the Apache Log4j Java logging utility, a popular library used on millions of devices worldwide. The vulnerability allows an attacker to perform a remote code execution (RCE) attack by logging code that runs a Java Naming and Directory Interface (JNDI) endpoint lookup. An attacker can exploit this behavior by performing a JNDI lookup to a server under their control containing malicious code. This vulnerability was patched out with the release of Log4j version 2.16.0.

Due to the popularity of Log4j, Log4Shell was extremely pervasive, impacting a variety of services such as those offered by [Amazon Web Services](https://aws.amazon.com/security/security-bulletins/AWS-2021-006/) and [IBM](https://www.ibm.com/support/pages/apache-log4j2-cve-2021-44228-security-vulnerability), among others. Its widespread use makes this vulnerability difficult to completely remediate as it may be unknown if a vulnerable version of Log4j is present on a system, such as in the case of [a federal network being affected](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-320a) months after the vulnerability was first documented.

To learn more about Log4Shell, check out its listing on the [Apache Log4j Security Vulnerabilities](https://logging.apache.org/log4j/2.x/security.html#fixed-in-log4j-2-15-0-java-8) page.


### Heartbleed (CVE-2014-0160)

[Heartbleed](https://nvd.nist.gov/vuln/detail/CVE-2014-0160) is a buffer over-read vulnerability in OpenSSL, a popular cryptographic library commonly used for encrypting SSL/TLS communications on the internet. The vulnerability allows an attacker to read the memory of a system without detection. As a result, cryptographic keys, credentials, and other content can be silently extracted from a server’s memory.

Heartbleed was discovered about two years after the vulnerability was first introduced to OpenSSL. Due to its undetectable nature, determining if it was exploited against a particular server is difficult. It was estimated at the time of discovery that around [half a million websites](https://www.netcraft.com/blog/half-a-million-widely-trusted-websites-vulnerable-to-heartbleed-bug/) may have been vulnerable to the bug.

To learn more about the Heartbleed vulnerability, check out the [Heartbleed website](https://heartbleed.com/).


### Shellshock (CVE-2014-6271)

[Shellshock](https://nvd.nist.gov/vuln/detail/CVE-2014-6271) is an arbitrary code execution vulnerability which went unnoticed for 25 years, existing in Bash since 1989 and first being publicly reported in 2014. The vulnerability allows for commands that should be inaccessible to be executed through Bash’s function export feature. Following the initial CVE report, further CVEs were soon filed addressing additional related vulnerabilities.

As Shellshock was not discovered for over two decades after its inception, the scope of its influence is significant, with it [still being leveraged against systems today](https://securityintelligence.com/articles/shellshock-vulnerability-in-depth/). Soon after the vulnerability was uncovered, large-scale [attacks using botnets](https://www.itnews.com.au/news/first-shellshock-botnet-attacks-akamai-us-dod-networks-396197) were deployed against high-profile entities like the U.S. Department of Defense.

To learn more about Shellshock and its related vulnerabilities, check out [the CISA’s Shellshock alert](https://www.cisa.gov/news-events/alerts/2014/09/25/gnu-bourne-again-shell-bash-shellshock-vulnerability-cve-2014-6271).


## Learn More

In this article, you learned how the CISA’s KEV Catalog tracks exploited vulnerabilities, and how the catalog is used by developers and federal agencies to prioritize vulnerability remediation. You also explored three infamous software vulnerabilities: Log4Shell, Heartbleed, and Shellshock, and learned how they have impacted systems across the world.

To learn more about these vulnerabilities and other exploited vulnerabilities, dive further into [the KEV Catalog](https://www.cisa.gov/known-exploited-vulnerabilities), or check out [the full CVE database](https://cve.mitre.org/cve/search_cve_list.html).
