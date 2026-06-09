---
title: "Chainguard Agent Skills overview"
linktitle: "Overview"
description: "Learn what Chainguard Agent Skills are, the supply chain risk they address, and how Chainguard hardens skills before you install them."
type: "article"
date: 2026-06-05T08:48:45+00:00
lastmod: 2026-06-05T08:48:45+00:00
draft: false
tags: ["Agent Skills", "Overview"]
images: []
menu:
  docs:
    parent: "agent-skills"
toc: true
weight: 001
---

Chainguard Agent Skills is a catalog of hardened AI agent skills that Chainguard reviews, scopes, and publishes with a full audit trail. It lets teams extend their AI agents without extending their attack surface.

{{< beta feature="Chainguard Agent Skills" access="Chainguard Containers customers who sign up for the beta program. You can sign up by visiting the [Chainguard Agent Skills product page](https://www.chainguard.dev/agent-skills) and clicking **Join the beta**" >}}

## What is an agent skill?

An agent skill is a small, modular instruction set — typically a single `SKILL.md` file — that extends what an AI agent can do. Agents such as Claude Code use skills to perform tasks like browser automation, database management, and code generation.

Skills are the newest class of third-party software dependency, much like npm packages or container images. Like any dependency, a skill you install runs in your environment with whatever permissions and shell access its author gave it.

## The problem with skill registries

Community skill registries are growing quickly, but most have no review process, no permission scoping, no integrity verification, and no audit trail. A skill can ship with broad tool permissions, unrestricted shell access, or a vague description that causes an agent to invoke it in the wrong context. Recent supply chain attacks have used malicious skills to direct agents into installing credential-stealing malware.

Every skill installed without review is an unaudited dependency with arbitrary permissions running where your agent runs.

## How Chainguard hardens skills

Chainguard applies the same model it brings to container images and language libraries — hardened defaults, continuous updates, and verifiable provenance — to agent skills:

- **Ingest and review.** Chainguard pulls popular skills from community registries and reviews each one against a security and quality ruleset.
- **Target real attack vectors.** The ruleset addresses how attackers exploit the agent-skill trust relationship, including unrestricted shell access, overly broad tool permissions, and vague descriptions that enable mis-invocation.
- **Harden with an audit trail.** An automated agentic pipeline applies fixes one at a time, committing each change individually. Every published skill links to a pull request with a full diff showing what changed and why.
- **Reconcile continuously.** Rather than scanning once, the catalog runs a persistent loop that compares each skill against the current rules. When an upstream source changes or a new rule is added, affected skills are re-evaluated and re-hardened, so the catalog doesn't go stale.

The security work happens upstream, before you or your agent ever touches the skill. To install a hardened skill, you just need to add its `SKILL.md` to your agent; there's no new toolchain or configuration required.

## Public catalog and private registries

Chainguard Agent Skills involves two registries, both served from `skills.cgr.dev`:

- **The public catalog**, maintained by Chainguard at `skills.cgr.dev/chainguard/<skill>`. This is the hardened catalog described above. Anyone can pull from it, and the skills in it are reviewed and re-hardened on an ongoing basis.
- **Your organization's private registry**, available to customers with access, at `skills.cgr.dev/<your-org>/<skill>`. You can use it to publish, manage, and distribute your own skills scoped to your organization, and you control who can push and install them.

To interact with either of these registries, use the [`chainctl skills` commands](/chainguard/chainctl/chainctl-docs/chainctl_skills/).

## Next steps

To install and run a skill hardened by Chainguard, check out our guide on [Getting started with the Chainguard Agent Skills public catalog](/chainguard/agent-skills/public-catalog/). Alternatively, to publish, push, and run skills in your organization's private registry, refer to our guide on [Getting started with the Chainguard Skills Registry](/chainguard/agent-skills/skills-registry/).
