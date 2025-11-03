# Content Management Scripts

Utility scripts for managing Chainguard Academy content taxonomy and organization.

## Overview

All content in this repository is tagged with a `contentType` field in the frontmatter:
- `product-docs` - Chainguard product documentation
- `tutorial` - Learning-oriented guides
- `how-to-guide` - Task-oriented instructions
- `integration` - Third-party integrations
- `conceptual` - Educational/explanatory content

## Scripts

### `list-by-content-type.sh`

List files by content type.

**Usage:**
```bash
# Show summary of all content types
./scripts/list-by-content-type.sh

# List all product documentation files
./scripts/list-by-content-type.sh product-docs

# List all tutorials
./scripts/list-by-content-type.sh tutorial
```

### `export-content-inventory.sh`

Export a CSV inventory of all content with metadata.

**Usage:**
```bash
# Generate CSV file
./scripts/export-content-inventory.sh > content-inventory.csv
```

The CSV includes: file path, content type, title, and last modified date.

### `content-summary-by-dir.sh`

Show content type distribution by directory.

**Usage:**
```bash
./scripts/content-summary-by-dir.sh
```

### `validate-content-types.sh`

Validate that all markdown files have a contentType tag. Useful for CI/CD.

**Usage:**
```bash
./scripts/validate-content-types.sh
```

Returns exit code 0 if all files are tagged, 1 if any are missing tags.

## Use Cases

- **Content audits**: Verify all files are properly tagged
- **Work assignment**: Generate lists for team members to review
- **Content strategy**: Understand content distribution
- **CI/CD validation**: Ensure new content has proper metadata
