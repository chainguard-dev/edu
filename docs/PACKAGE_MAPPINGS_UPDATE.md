# Package Mappings Update Guide

This document explains how the package and image mappings are automatically maintained on the [Package Name Mappings](/chainguard/chainguard-images/about/package-name-mappings/) documentation page.

## Overview

The package mappings are **automatically fetched** from the [dfc repository](https://github.com/chainguard-dev/dfc/blob/main/pkg/dfc/builtin-mappings.yaml) every time the site is built. They are stored temporarily in `/data/package-mappings.yaml` and rendered dynamically by Hugo shortcodes at build time.

## How Automatic Updates Work

The mappings are fetched during every site build through GitHub Actions workflows:

1. **Cloud Run Deployment** (`.github/workflows/cloud-run.yaml`):
   - Triggers on every push to `main` branch
   - Fetches latest mappings before building the site
   - Deploys to production with fresh data

2. **Platform Docs Build** (`.github/workflows/autodocs-platform.yaml`):
   - Runs daily and on push to `platform-docs` branch
   - Fetches latest mappings before building
   - Creates PR with updated platform documentation

Both workflows include this step before `npm run build`:
```yaml
- name: Fetch latest package mappings
  run: |
    echo "Fetching latest package mappings from dfc repository..."
    curl -sL https://raw.githubusercontent.com/chainguard-dev/dfc/main/pkg/dfc/builtin-mappings.yaml \
      -o data/package-mappings.yaml
    echo "Package mappings updated successfully"
    ls -lh data/package-mappings.yaml
```

## Local Development

When working locally, you'll need to fetch the mappings once:

```bash
curl -sL https://raw.githubusercontent.com/chainguard-dev/dfc/main/pkg/dfc/builtin-mappings.yaml \
  -o data/package-mappings.yaml
```

Then build the site:
```bash
npm run build
# or for development server:
npm run start
```

Navigate to `/chainguard/chainguard-images/about/package-name-mappings/` to verify the tables render correctly.

## Hugo Shortcodes

The mappings are rendered using three Hugo shortcodes located in `/layouts/shortcodes/package-mappings/`:

1. `image-mappings.html` - Renders the container image name mappings
2. `debian-packages.html` - Renders Debian/Ubuntu package mappings
3. `fedora-packages.html` - Renders Fedora/RedHat/UBI package mappings

These shortcodes read from `$.Site.Data.package_mappings` (Hugo automatically converts hyphens to underscores in data file names).

## Testing Changes

After updating the mappings:

1. Build the site locally: `npm run build`
2. Check for any Hugo errors in the output
3. Verify the tables render correctly with updated data
4. Ensure all shortcodes are working properly

## Troubleshooting

### Tables not rendering
- Check that the YAML file is valid: `yq eval . data/package-mappings.yaml`
- Verify the file structure matches what the shortcodes expect
- Check Hugo build logs for template errors

### Data not updating
- Clear Hugo's cache: `npm run clean`
- Rebuild: `npm run build`
- Check that the data file name matches the shortcode references

## Related Files

- Documentation: `/content/chainguard/chainguard-images/about/package-name-mappings.md`
- Data file: `/data/package-mappings.yaml`
- Shortcodes: `/layouts/shortcodes/package-mappings/*.html`
- This guide: `/docs/PACKAGE_MAPPINGS_UPDATE.md`
