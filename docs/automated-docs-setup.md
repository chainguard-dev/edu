# Automated Documentation Compilation Setup

This guide explains how to set up automated updates for the compiled documentation bundle.

## Overview

The documentation bundle will be automatically updated when:
1. Changes are pushed to the edu repository (content or scripts)
2. Changes are pushed to the courses repository (HTML content)
3. Changes are pushed to the images-private repository (README files)
4. Daily at 2 AM UTC (scheduled update)
5. Manually triggered via GitHub Actions

## Setup Instructions

### 1. Enable GitHub Actions

Ensure GitHub Actions are enabled for all three repositories:
- edu
- courses  
- images-private

### 2. Create a Personal Access Token (PAT)

For cross-repository triggers to work, you need to create a PAT with appropriate permissions:

1. Go to GitHub Settings > Developer settings > Personal access tokens
2. Generate a new token with these scopes:
   - `repo` (full control of private repositories)
   - `workflow` (update GitHub Actions workflows)
3. Name it `CROSS_REPO_TOKEN`

### 3. Add the PAT as a Secret

Add the PAT to each repository:

1. Go to repository Settings > Secrets and variables > Actions
2. Add a new repository secret named `CROSS_REPO_TOKEN`
3. Paste your PAT as the value
4. Repeat for all three repositories

### 4. Deploy the Workflows

#### For the edu repository:
- The workflows are already in place:
  - `.github/workflows/compile-docs.yml` (scheduled and on push)
  - `.github/workflows/compile-docs-on-webhook.yml` (triggered by other repos)

#### For the courses repository:
1. Create `.github/workflows/trigger-docs-compile.yml`
2. Copy the content from `edu/docs/webhook-setup-courses.yml`

#### For the images-private repository:
1. Create `.github/workflows/trigger-docs-compile.yml`
2. Copy the content from `edu/docs/webhook-setup-images.yml`

## How It Works

### Direct Updates (edu repository)
When content in the edu repository changes, the `compile-docs.yml` workflow:
1. Checks out all three repositories
2. Runs the Python compilation script
3. Creates compressed versions
4. Commits the updated files back to the repository

### Cross-Repository Updates
When content in courses or images-private changes:
1. The trigger workflow sends a repository dispatch event to edu
2. The `compile-docs-on-webhook.yml` workflow in edu runs
3. It compiles documentation from all three repositories
4. Updates are committed to the edu repository

### Scheduled Updates
Every day at 2 AM UTC:
1. The scheduled job runs automatically
2. Ensures documentation stays fresh even without manual changes
3. Captures any missed updates

## Manual Triggers

You can manually trigger the documentation compilation:

1. Go to the edu repository on GitHub
2. Click on "Actions" tab
3. Select either workflow:
   - "Compile Documentation Bundle" (main workflow)
   - "Compile Docs on Repository Update" (webhook workflow)
4. Click "Run workflow"

## Monitoring

To monitor the compilation process:
1. Check the Actions tab in the edu repository
2. Look for workflow runs with these names
3. Review logs if any failures occur

## Troubleshooting

### Common Issues

1. **Permission Denied**: Ensure the PAT has correct permissions
2. **Workflow Not Triggering**: Check that paths in workflow files match your changes
3. **Compilation Errors**: Review Python script logs in the workflow run
4. **Large File Issues**: The compiled file might exceed GitHub's limits (100MB)

### File Size Management

If the documentation grows too large:
- Consider splitting into multiple files by category
- Increase compression
- Exclude certain verbose sections
- Use Git LFS for large files

## Local Testing

To test the compilation locally:

```bash
cd /path/to/edu
python3 scripts/compile_docs.py
./scripts/create_compressed_docs.sh
```

## Security Considerations

- PATs should have minimal required permissions
- Rotate PATs periodically
- Use repository secrets, never commit tokens
- Review workflow permissions regularly