# Documentation Compilation Scripts

This directory contains scripts for compiling Chainguard documentation into a single bundle for AI assistants.

## Files

- `compile_docs.py` - Main compilation script
- `compile_docs_secure.py` - Security-enhanced version (optional)
- `quick-start-guide.md` - Template for the Quick Start Guide
- `create_compressed_docs.sh` - Shell script to create compressed versions
- `requirements.txt` - Python dependencies

## Quick Start Guide Template

The `quick-start-guide.md` file contains the content that appears at the beginning of every compiled documentation bundle. This approach provides several benefits:

### Benefits
1. **Easy Updates**: Edit the markdown file without touching Python code
2. **Version Control**: Track changes to the guide separately
3. **Markdown Preview**: See how it looks in any markdown editor
4. **Reusability**: Can be included in other documentation
5. **Collaboration**: Non-developers can edit the guide

### Editing the Guide
To update the Quick Start Guide:

1. Edit `scripts/quick-start-guide.md`
2. Run the compilation: `python3 scripts/compile_docs.py`
3. The updated guide will appear in the next compilation

### Structure
The guide should include:
- Usage tips for different AI tools
- Example prompts for common tasks
- Search strategies
- Document structure overview

## Running the Compilation

```bash
# From the edu directory
python3 scripts/compile_docs.py

# Create compressed versions
./scripts/create_compressed_docs.sh
```

## Automation

The compilation runs automatically via GitHub Actions when:
- Changes are pushed to the edu repository
- Other repositories trigger updates
- Daily at 2 AM UTC
- Manual workflow dispatch

The Quick Start Guide will always be included at the top of the compiled documentation.