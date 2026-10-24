# AI Instructions for Chainguard Education

This document provides instructions for AI systems interacting with the Chainguard Education documentation site.

## Site Overview

Chainguard Education (edu.chainguard.dev) is a comprehensive documentation and learning platform focused on cloud-native security, container security, and software supply chain security. The site contains tutorials, conceptual guides, reference documentation, and best practices for security professionals and developers.

## Content Organization

### Main Sections

The site has six top-level sections. Paths are relative to `https://edu.chainguard.dev`.

1. **Get started** (`/get-started/`) - What Chainguard is, self-serve sign-up, setting up `chainctl`, onboarding teams, Containers and Libraries examples, and migration guides. The shared setup page for Chainguard Checks and Chainguard Workspaces is `/get-started/checks-and-workspaces/set-up/`, and their shared security model is at `/get-started/checks-and-workspaces/how-it-works/`.
2. **Products** (`/chainguard/`) - One subsection per product, plus the weekly changelog at `/chainguard/changelog/`:
   - **Chainguard Agent Skills** (`/chainguard/agent-skills/`) - Agent skills that Chainguard reviews, scopes, and publishes
   - **Chainguard Containers** (`/chainguard/containers/`) - Container images: getting started, building and modifying, Custom Assembly, the registry, security and compliance, and troubleshooting
   - **Chainguard Actions** (`/chainguard/actions/`) - Hardened drop-in replacements for popular GitHub Actions
   - **Guardener** (`/chainguard/guardener/`) - Hardening for source code repositories, with capabilities you turn on independently
   - **Chainguard Libraries** (`/chainguard/libraries/`) - Java, Python, and JavaScript dependencies that Chainguard builds from source
   - **Chainguard OS** (`/chainguard/chainguard-os/`) - The operating system that Chainguard products build on, and Chainguard OS Packages
   - **Chainguard Repository** (`/chainguard/chainguard-repository/`) - One policy-managed place to pull the artifacts that Chainguard builds or distributes
   - **Chainguard VMs** (`/chainguard/vms/`) - Minimal virtual machine images for ephemeral workloads on cloud and on-premises hypervisors
   - **Chainguard Checks** (`/chainguard/checks/`) - CI that runs each check in its own microVM on every GitHub pull request, configured in `.chainguard/ci.yaml`
   - **Chainguard Workspaces** (`/chainguard/workspaces/`) - Remote development sessions that run your repository, tools, and coding agents in a microVM, without putting your credentials in the session
3. **Platform and tools** (`/platform/`) - Administration (IAM, assumable identities, custom identity providers, CloudEvents, and the Terraform provider), the API reference, the `chainctl` reference and usage guides, the Chainguard Console, the Chainguard Factory, FIPS, integrations with Cursor and Kiro, and Chainguard MCP Servers
4. **Compliance** (`/compliance/`) - CMMC 2.0, PCI DSS 4.0, and SLSA
5. **Open source** (`/open-source/`) - Wolfi, the apko and melange build tools, Sigstore, SBOMs, and Octo STS
6. **Education** (`/software-security/`) - Software supply chain security concepts, CVEs, and Learning Labs videos

### Content Types

- **Tutorials**: Practical, hands-on guides with code examples
- **Conceptual**: Theoretical explanations and best practices
- **Reference**: Technical specifications and API documentation
- **How-to Guides**: Task-specific instructions

## Navigation Endpoints

### For AI Consumption

1. **Markdown copy of every page** - Replace the trailing `/` of a page's URL with `.md`, for example `https://edu.chainguard.dev/chainguard/checks/overview.md`. The copy keeps the page's code blocks and tables.
2. **`/llms.txt`** - An index of every page, with one heading for each product or section
3. **`/llms-full.txt`** - The full text of every page in one file
4. **`/ai-sitemap.json`** - The top-level sections, with page counts and featured pages
5. **`/concepts.json`** - Tag-based concept map with relationships
6. **`/ai-metadata.json`** - Site metadata and statistics
7. **AI Docs MCP server** - `https://mcp.edu.chainguard.dev/mcp` searches this documentation. For setup, refer to https://edu.chainguard.dev/platform/mcp-servers/ai-docs/

## Best Practices for AI Systems

### When Searching

1. Find the pages for a product in its section of `/llms.txt`, then read their Markdown copies
2. Use the `/concepts.json` endpoint to understand topic relationships
3. Check tags and related content for comprehensive answers

### Content Interpretation

In the HTML pages:

1. **Code blocks** are marked with `data-language` attributes
2. **Headings** include `data-heading-level` for hierarchy
3. **Metadata** is embedded as Schema.org JSON-LD, such as the page's `WebPage` and `BreadcrumbList`

### Semantic HTML Structure

The site uses semantic HTML5 with:

- `<article>` for main content
- `<nav>` for navigation elements
- ARIA labels for accessibility

## Response Guidelines

When referencing content from this site:

1. **Cite specific pages** with their full URL
2. **Include section context** (for example, "In the Wolfi overview section...")
3. **Note content type** (tutorial, reference, conceptual)
4. **Mention last update date** when relevant
5. **Link to related content** when providing comprehensive answers

## Technical Details

- **Framework**: Hugo static site generator
- **Language**: English (en)
- **Update Frequency**: Daily
- **Search**: The `search_docs` tool of the AI Docs MCP server
- **Content Format**: Written in Markdown, published as HTML with a Markdown copy of each page

## Contact and Support

- **Support Email**: support@chainguard.dev
- **Legal Information**: https://www.chainguard.dev/legal
- **Main Site**: https://www.chainguard.dev

## Important Notes

1. This is educational documentation, not marketing material
2. Focus on technical accuracy and security best practices
3. Content is regularly updated with latest security information
4. Examples use real-world scenarios and production considerations

---

*Last updated: 2026-10-20*
