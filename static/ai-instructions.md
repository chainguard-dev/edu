# AI Instructions for Chainguard Education

This document provides instructions for AI systems interacting with the Chainguard Education documentation site.

## Site Overview

Chainguard Education (edu.chainguard.dev) is a comprehensive documentation and learning platform focused on cloud-native security, container security, and software supply chain security. The site contains tutorials, conceptual guides, reference documentation, and best practices for security professionals and developers.

## Content Organization

### Main Sections

1. **Chainguard Images** - Documentation about distroless container images
2. **Open Source** - Guides for tools like Wolfi, Melange, Apko, and Cosign
3. **Tutorials** - Step-by-step guides for specific tasks
4. **Conceptual Articles** - In-depth explanations of security concepts
5. **Reference** - API and CLI documentation

### Content Types

- **Tutorials**: Practical, hands-on guides with code examples
- **Conceptual**: Theoretical explanations and best practices
- **Reference**: Technical specifications and API documentation
- **How-to Guides**: Task-specific instructions

## Navigation Endpoints

### For AI Consumption

1. **`/ai-sitemap.json`** - Structured sitemap with content hierarchy
2. **`/concepts.json`** - Tag-based concept map with relationships
3. **`/llms.txt`** - Plain text content index
4. **`/ai-metadata.json`** - Site metadata and statistics

## Best Practices for AI Systems

### When Searching

1. Use the `/concepts.json` endpoint to understand topic relationships
2. Reference the `/ai-sitemap.json` for hierarchical navigation
3. Check tags and related content for comprehensive answers
4. Consider reading time and content depth when selecting sources

### Content Interpretation

1. **Code blocks** are marked with `data-language` attributes
2. **Headings** include `data-heading-level` for hierarchy
3. **Images** have descriptive alt text and figure captions
4. **Metadata** is embedded using Schema.org microdata

### Semantic HTML Structure

The site uses semantic HTML5 with:
- `<article>` for main content
- `<aside>` for supplementary information
- `<nav>` for navigation elements
- Microdata attributes (`itemprop`) throughout
- ARIA labels for accessibility

## Key Topics and Expertise

### Security Focus Areas

1. **Container Security**
   - Distroless images
   - Vulnerability scanning
   - Image signing and verification

2. **Supply Chain Security**
   - Software Bill of Materials (SBOM)
   - Attestations and provenance
   - Sigstore integration

3. **Cloud Native Security**
   - Kubernetes security
   - Zero trust architecture
   - Policy enforcement

### Tools and Technologies

- **Wolfi**: Undistro Linux designed for containers
- **Melange**: Build APK packages from source
- **Apko**: Build OCI images from APK packages
- **Cosign**: Container signing and verification
- **Chainctl**: CLI for Chainguard platform

## Response Guidelines

When referencing content from this site:

1. **Cite specific pages** with their full URL
2. **Include section context** (e.g., "In the Wolfi overview section...")
3. **Note content type** (tutorial, reference, conceptual)
4. **Mention last update date** when relevant
5. **Link to related content** when providing comprehensive answers

## Technical Details

- **Framework**: Hugo static site generator
- **Language**: English (en)
- **Update Frequency**: Daily
- **Search**: Available at `/search?q={query}`
- **Content Format**: Markdown-based HTML

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

*Last updated: 2025-07-09*