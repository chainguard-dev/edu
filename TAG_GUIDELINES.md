# Tag Guidelines for Hugo Documentation

## Overview
This document defines the approved tag taxonomy and usage guidelines for the Hugo documentation site. Following these guidelines ensures consistent categorization and improved discoverability of content.

## Tag Usage Rules

1. **Maximum tags per document**: 4-5 tags
2. **Required tags**:
   - One product tag (if applicable)
   - 1-2 action-oriented or lifecycle tags
   - 1-2 platform tags (if relevant)
   - 1-2 topic tags as needed

3. **Format requirements**:
   - Use Title Case for regular words (e.g., "Compliance", "Standards")
   - Keep acronyms in uppercase (e.g., "CVE", "SBOM", "FAQ")
   - Maintain version numbers as-is (e.g., "CMMC 2.0", "PCI DSS 4.0")

## Approved Tag Taxonomy

### Product Tags
- **Chainguard Containers** - For all container/image content
- **Chainguard Libraries** - For library-specific content
- **chainctl** - CLI tool documentation
- **Enforce** - Enforcement product docs
- **Chainguard OS** - Operating system documentation

### Action-Oriented Tags
- **Migration** - Moving from other solutions
- **Integration** - Connecting with other tools
- **Configuration** - Setup and customization
- **Monitoring** - Observability, metrics, logging
- **Debugging** - Error investigation and fixes
- **Performance** - Optimization and tuning
- **Automation** - Scripts, workflows, CI/CD
- **Troubleshooting** - Problem resolution guides

### Problem-Solving Tags
- **FAQ** - Common questions
- **Recommended Practices** - Best practices and recommendations

### Content Type Tags
- **Overview** - High-level introductions
- **Procedural** - Step-by-step guides
- **Conceptual** - Theoretical/background content
- **Reference** - API docs, command references
- **Video** - Video content
- **Learning Labs** - Interactive tutorials
- **Workshop** - Workshop materials

### Lifecycle Tags
- **Installation** - Initial setup
- **Upgrade** - Version updates
- **Deprecation** - Sunset features/APIs
- **Getting Started** - Onboarding content

### Platform/Tool Tags
- **AWS** - Amazon Web Services specific content
- **GCP** - Google Cloud Platform specific content
- **Azure** - Microsoft Azure specific content
- **Multi-Cloud** - Cross-cloud strategies
- **JFrog** - JFrog Artifactory integration
- **Cloudsmith** - Cloudsmith registry integration
- **GitHub** - GitHub and GitHub Actions content
- **GitLab** - GitLab and GitLab CI content
- **Jenkins** - Jenkins CI/CD integration
- **Harbor** - Harbor registry integration
- **Docker Hub** - Docker Hub registry content
- **Terraform** - Terraform provider and IaC content
- **Kubernetes** - K8s-specific content
- **OIDC** - OpenID Connect authentication

### Topic Tags
- **Security** - Security-focused content
- **SBOM** - Software Bill of Materials
- **CVE** - CVE/vulnerability content
- **VEX** - Vulnerability Exploitability eXchange
- **Compliance** - Standards and compliance
- **Standards** - Industry standards
- **SLSA** - Supply-chain Levels for Software Artifacts
- **OCI** - Open Container Initiative
- **AI** - Artificial Intelligence related content

### Language/Framework Tags
- **Python** - Python-specific content
- **Java** - Java-specific content
- **Go** - Go language content
- **Node.js** - Node.js content
- **Ruby** - Ruby content
- **PHP** - PHP content
- **Rust** - Rust content
- **.NET** - .NET framework content

### Tool-Specific Tags
- **apko** - apko tool documentation
- **melange** - melange tool documentation
- **Wolfi** - Wolfi Linux distribution
- **Cosign** - Cosign signing tool
- **Rekor** - Rekor transparency log
- **Fulcio** - Fulcio CA

## Examples of Proper Tag Usage

### Example 1: Chainguard Images Getting Started Guide
```yaml
tags: ["Chainguard Containers", "Getting Started", "Overview"]
```

### Example 2: Debugging CVEs in Python Images
```yaml
tags: ["Chainguard Containers", "Python", "CVE", "Debugging"]
```

### Example 3: Terraform Provider Reference
```yaml
tags: ["Terraform", "Reference", "Configuration"]
```

### Example 4: SBOM Generation with Cosign
```yaml
tags: ["Cosign", "SBOM", "Procedural", "Security"]
```

## Adding New Tags

If you need a tag that isn't in the approved list:
1. Check if an existing tag could work instead
2. Consider if the content truly needs a unique categorization
3. Submit a PR to update this guidelines document with justification
4. Wait for approval before using the new tag

## Validation

A pre-commit hook validates tags against this approved list and checks spelling. The hook will:

### Tag Validation:
- Warn on tags not in the approved list
- Check tag count doesn't exceed 5
- Verify proper case formatting

### Spell Checking:
- Check for spelling errors in content (requires `aspell` to be installed)
- Ignore code blocks, URLs, and technical terms
- Use custom dictionary in `.aspell.en.pws` for project-specific terms

To install aspell:
```bash
# macOS
brew install aspell

# Ubuntu/Debian
sudo apt install aspell

# RHEL/CentOS/Fedora
sudo yum install aspell
# or
sudo dnf install aspell

# Alpine Linux
apk add aspell

# Arch Linux
sudo pacman -S aspell
```

To bypass the pre-commit hook temporarily:
```bash
git commit --no-verify
```