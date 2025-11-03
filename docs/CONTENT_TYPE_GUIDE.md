# Content Type Taxonomy Guide

## Overview

All content pages in Chainguard Academy are categorized using a `contentType` field in the frontmatter. This taxonomy helps organize content, assign work to team members, and ensure the right type of content is created for each use case.

The content type system is based on the [Diátaxis documentation framework](https://diataxis.fr/), which organizes documentation by user intent and content purpose.

## Content Type Field

Add this field to your markdown frontmatter:

```yaml
---
title: "Your Page Title"
type: "article"
description: "..."
draft: false
tags: ["Tag1", "Tag2"]
contentType: "product-docs"
---
```

## Content Type Definitions

### `product-docs` - Product Documentation

**Purpose**: Reference documentation for Chainguard products and services.

**Characteristics**:
- API specifications and endpoints
- CLI command reference
- Configuration options and parameters
- Architecture documentation
- Product feature descriptions
- Technical specifications

**When to use**:
- Documenting APIs, CLIs, or SDKs
- Explaining product features and capabilities
- Providing configuration references
- Describing system architecture

**Examples**:
- `content/chainguard/administration/api.md`
- `content/chainguard/chainctl/chainctl-docs/chainctl_auth.md`
- `content/chainguard/libraries/overview.md`

---

### `tutorial` - Learning-Oriented Guides

**Purpose**: Help newcomers to a specific subject learn by successfully completing a meaningful project.

**Characteristics**:
- Takes learners step-by-step from start to finish
- Teaches concepts while doing
- Provides a safe, repeatable learning experience
- Explains "why" along with "how"
- Assumes little to no prior knowledge
- Builds something complete from scratch

**When to use**:
- Getting started guides
- First-time user onboarding
- Teaching new concepts through practice
- Building example projects

**Examples**:
- `content/chainguard/chainctl-usage/getting-started-with-chainctl.md`
- `content/chainguard/chainguard-images/about/getting-started-distroless.md`
- `content/open-source/build-tools/melange/getting-started-with-melange.md`

**Naming convention**: Often starts with "Getting Started with..." or "Introduction to..."

---

### `how-to-guide` - Task-Oriented Instructions

**Purpose**: Show how to solve a specific problem or accomplish a specific goal.

**Characteristics**:
- Focused on achieving a particular task
- Assumes some prior knowledge
- Gets straight to the point with minimal explanation
- Like a recipe - follows steps to reach a goal
- May skip background information
- Doesn't necessarily teach concepts

**When to use**:
- Installation instructions
- Configuration guides
- Specific task completion
- Problem-solving procedures
- Troubleshooting steps

**Examples**:
- `content/open-source/sigstore/cosign/how-to-install-cosign.md`
- `content/chainguard/administration/cloudevents/image-copy-gcr/index.md`
- `content/chainguard/chainguard-images/tooling/debugging-distroless-images.md`

**Naming convention**: Often starts with "How to..."

---

### `integration` - Third-Party Integration Guides

**Purpose**: Document how to use Chainguard products with third-party tools and platforms.

**Characteristics**:
- Combines Chainguard products with external systems
- Platform-specific implementations
- Often includes both setup and usage
- May involve authentication/authorization flows

**When to use**:
- CI/CD platform integrations (GitHub Actions, GitLab CI, Jenkins)
- Identity provider integrations (OIDC, SAML)
- Container registry integrations
- Policy enforcement tools (Kyverno, OPA Gatekeeper)
- Cloud platform integrations (AWS, GCP, Azure)

**Examples**:
- `content/chainguard/administration/assumable-ids/identity-examples/github-identity/index.md`
- `content/chainguard/chainguard-images/staying-secure/enforcement/kyverno/index.md`
- `content/chainguard/chainguard-images/how-to-use/use-with-openshift.md`

---

### `conceptual` - Educational/Explanatory Content

**Purpose**: Explain concepts, provide context, and help users understand the "why" behind technologies.

**Characteristics**:
- Theoretical and explanatory
- Provides background information
- Helps readers understand concepts
- Often includes comparisons and examples
- Not task-oriented

**When to use**:
- "What is..." explanations
- Security concepts and best practices
- Standards and compliance information
- Architectural overviews
- Background information
- FAQs and glossaries

**Examples**:
- `content/software-security/selecting-a-base-image.md`
- `content/open-source/sbom/what-is-an-sbom.md`
- `content/open-source/wolfi/overview.md`
- `content/compliance/slsa/slsa-levels.md`

**Naming convention**: Often starts with "What is..." or "Understanding..."

---

## Decision Tree: Which Content Type?

```
Is this about a Chainguard product?
├─ Yes → Is it reference documentation (API, CLI, features)?
│   ├─ Yes → product-docs
│   └─ No → Continue...
└─ No → Continue...

Does it teach beginners through a complete example?
├─ Yes → tutorial
└─ No → Continue...

Does it solve a specific task or problem?
├─ Yes → Is it integrating with a third-party tool?
│   ├─ Yes → integration
│   └─ No → how-to-guide
└─ No → conceptual
```

## Quick Reference Table

| Content Type | User Question | Example Title |
|--------------|---------------|---------------|
| **product-docs** | "What can this do?" | "chainctl auth Commands" |
| **tutorial** | "Can you teach me?" | "Getting Started with Distroless Images" |
| **how-to-guide** | "How do I...?" | "How to Install Cosign" |
| **integration** | "How do I use X with Y?" | "Using Chainguard Images with GitHub Actions" |
| **conceptual** | "What is this?" | "What is an SBOM?" |

## Examples by Directory

### `/content/chainguard/`
- **administration/** → mostly `product-docs`
- **chainctl/chainctl-docs/** → all `product-docs` (CLI reference)
- **chainctl-usage/** → mix of `tutorial` and `how-to-guide`
- **libraries/** → `product-docs`
- **factory/** → `product-docs`
- **chainguard-images/getting-started/** → `tutorial`
- **chainguard-images/how-to-use/** → `how-to-guide`
- **migration/** → `how-to-guide`

### `/content/open-source/`
- **wolfi/overview.md** → `conceptual`
- **wolfi/hello-wolfi.md** → `tutorial`
- **sigstore/cosign/how-to-*.md** → `how-to-guide`
- **sigstore/cosign/an-introduction-to-*.md** → `conceptual`
- **sbom/what-is-*.md** → `conceptual`

### `/content/software-security/`
- Most files → `conceptual` (educational content)

### `/content/compliance/`
- All files → `conceptual` (standards and frameworks)

## Adding Content Type to New Content

When creating new content, add the `contentType` field to your frontmatter:

```yaml
---
title: "How to Configure Authentication"
type: "article"
description: "Step-by-step guide to configuring authentication"
date: 2025-01-15T10:00:00+00:00
draft: false
tags: ["Authentication", "Configuration"]
contentType: "how-to-guide"
---
```

## Validation

Use the validation script to ensure all content has a contentType:

```bash
./scripts/validate-content-types.sh
```

This script will:
- Check all markdown files for the `contentType` field
- Report any missing tags
- Return exit code 0 if valid, 1 if errors found

## Management Scripts

See [`scripts/README.md`](scripts/README.md) for available content management tools:

- `list-by-content-type.sh` - List files by content type
- `export-content-inventory.sh` - Generate CSV inventory
- `content-summary-by-dir.sh` - Show distribution by directory
- `validate-content-types.sh` - Validate all files are tagged

## Valid Values

Only these five values are allowed for `contentType`:

- `product-docs`
- `tutorial`
- `how-to-guide`
- `integration`
- `conceptual`

## Questions?

If you're unsure which content type to use:

1. Review the decision tree above
2. Look at similar existing content in the same directory
3. Ask yourself: "What is the user trying to accomplish?"
4. Consult with the content team

## Further Reading

- [Diátaxis Framework](https://diataxis.fr/) - The framework this taxonomy is based on
- [TAG_GUIDELINES.md](TAG_GUIDELINES.md) - Hugo tag taxonomy (different from contentType)
- [scripts/README.md](../scripts/README.md) - Content management tools
