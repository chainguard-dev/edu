# Package Name Mappings Documentation System - Session Notes

**Purpose:** This README provides context for AI assistants to pick up where this implementation left off.

**Session Date:** October 23, 2025
**Primary Goal:** Create package/image name mappings documentation optimized for LLM consumption (AEO - AI Engine Optimization)

## Context & Decision History

### Initial Request
User wanted to publish documentation about how Chainguard remaps package names from upstream distributions. Key requirement: **maximize AEO** - make it easy for LLMs to understand Chainguard's package naming.

### Key Decisions Made

1. **Option 2 Chosen: Full Content Embedded**
   - REJECTED: Brief doc with link to GitHub (bad for LLMs - external link)
   - ACCEPTED: Full mappings list embedded in page with Hugo data templates
   - Reason: LLMs need content in-page, not external

2. **Automatic Updates on Every Build**
   - Initially planned: Scheduled GitHub Action (weekly)
   - User pivoted: "I want it to update automatically when the site is built"
   - Final: Fetch mappings in CI/CD workflows before every build
   - NO scheduled automation, NO manual updates needed

3. **Package Mappings BEFORE Image Mappings**
   - User requested: Reorder sections (package mappings are more important)
   - Final order: Debian packages → Fedora packages → Alpine note → Image mappings

4. **Collapsible Tables for UX**
   - Problem: 200+ mappings = huge page, overwhelming
   - Solution: Bootstrap collapse components
   - User requested: Start collapsed (not expanded)

5. **Option 1 for LLM Optimization**
   - User asked: "Is this well-suited for LLMs?"
   - Trade-off identified: `<details>` tags might be deprioritized by some LLMs
   - Solution: Use Bootstrap collapse (CSS-hidden) instead of `<details>` (DOM-hidden)
   - Result: Content fully in HTML DOM for LLMs, but visually collapsed for users

**Live URL:** `/chainguard/chainguard-images/about/package-name-mappings/`

## What Was Built

### 1. Main Documentation Page
**Location:** `/content/chainguard/chainguard-images/about/package-name-mappings.md`

Comprehensive guide with:
- Why Chainguard remaps package names (consistency, simplification, semantic clarity)
- Container Image Name Conventions section
- How to use with dfc (Dockerfile Converter)
- Three collapsible tables (package mappings FIRST, then images)
- Auto-update notice: "automatically updated... every time this site is built"

**Important:** Section order matters - user specifically requested packages before images

### 2. Automatic Data Updates
**Key Feature:** Mappings are fetched fresh from the dfc repository on every site build.

Modified workflows:
- `.github/workflows/cloud-run.yaml` - Production deploys
- `.github/workflows/autodocs-platform.yaml` - Platform docs builds

Both workflows now include this step before `npm run build`:
```yaml
- name: Fetch latest package mappings
  run: |
    echo "Fetching latest package mappings from dfc repository..."
    curl -sL https://raw.githubusercontent.com/chainguard-dev/dfc/main/pkg/dfc/builtin-mappings.yaml \
      -o data/package-mappings.yaml
    echo "Package mappings updated successfully"
    ls -lh data/package-mappings.yaml
```

### 3. Hugo Data & Templates System
**Data File:** `/data/package-mappings.yaml`
- Fetched automatically during CI/CD builds
- Not committed to git (in `.gitignore`)
- Source of truth: https://github.com/chainguard-dev/dfc/blob/main/pkg/dfc/builtin-mappings.yaml

**Hugo Shortcodes:** `/layouts/shortcodes/package-mappings/`
- `image-mappings.html` - Renders 150+ container image mappings
- `debian-packages.html` - Renders 60+ Debian/Ubuntu package mappings
- `fedora-packages.html` - Renders Fedora/RedHat/UBI package mappings

All shortcodes use Bootstrap 5 collapse components for collapsible tables.

### 4. Maintenance Documentation
**Location:** `/docs/PACKAGE_MAPPINGS_UPDATE.md`

Documents:
- How the automatic updates work
- Local development setup
- Troubleshooting tips
- Hugo template structure

## How It Works

### Build-Time Flow
```
1. GitHub Action triggers (push to main or daily schedule)
   ↓
2. Workflow fetches latest package-mappings.yaml from dfc repo
   ↓
3. Saves to /data/package-mappings.yaml
   ↓
4. Hugo reads YAML into $.Site.Data
   ↓
5. Shortcodes iterate over data and generate HTML tables
   ↓
6. Site deploys with fresh, up-to-date mappings
```

### User Experience
- **Tables collapsed by default** - Page loads fast, not overwhelming
- **Bootstrap 5 collapse** - Smooth animations, accessible
- **Click to expand** - Tables expand on demand
- **Full content in DOM** - All data present for search/LLMs

### AI/LLM Optimization
- ✅ **All 200+ mappings in HTML** - Fully present in the DOM
- ✅ **No JavaScript required** - Content is physically there, just CSS-hidden
- ✅ **Semantic structure** - Proper tables with headers
- ✅ **Fully indexable** - Search engines and LLMs can read everything

## What Gets Mapped

### Container Image Names (150+)
Examples:
- `alpine` → `chainguard-base:latest`
- `golang*` → `go`
- `nodejs*` → `node`
- `debian` → `chainguard-base:latest`
- `mongo` → `mongodb`

### Debian/Ubuntu Packages (60+)
Examples:
- `build-essential` → `build-base`
- `python3` → `python-3`
- `google-chrome-stable` → `chromium`
- `ssh` → `openssh-client`, `openssh-server`

### Fedora/RedHat Packages (2)
Examples:
- `shadow-utils` → `shadow`
- `libpq-devel` → `postgresql-devel`

## File Structure

```
/
├── .github/workflows/
│   ├── cloud-run.yaml              # Modified - fetches mappings
│   └── autodocs-platform.yaml      # Modified - fetches mappings
├── .gitignore                       # Modified - ignores package-mappings.yaml
├── content/chainguard/chainguard-images/about/
│   └── package-name-mappings.md    # Main documentation page
├── data/
│   └── package-mappings.yaml       # Auto-fetched, not in git
├── layouts/shortcodes/package-mappings/
│   ├── image-mappings.html         # Image name table template
│   ├── debian-packages.html        # Debian package table template
│   └── fedora-packages.html        # Fedora package table template
└── docs/
    └── PACKAGE_MAPPINGS_UPDATE.md  # Maintenance documentation
```

## Local Development

### First Time Setup
1. Fetch the mappings data:
   ```bash
   curl -sL https://raw.githubusercontent.com/chainguard-dev/dfc/main/pkg/dfc/builtin-mappings.yaml \
     -o data/package-mappings.yaml
   ```

2. Build the site:
   ```bash
   npm run build
   # or for development server:
   npm run start
   ```

3. Navigate to: `/chainguard/chainguard-images/about/package-name-mappings/`

### Making Changes

#### To Update the Documentation Content
Edit `/content/chainguard/chainguard-images/about/package-name-mappings.md`

#### To Change Table Layout/Styling
Edit the shortcodes in `/layouts/shortcodes/package-mappings/`

**Important:** The shortcodes use Bootstrap 5 syntax:
- `data-bs-toggle="collapse"`
- `data-bs-target="#elementId"`

Don't use Bootstrap 4 syntax (`data-toggle`, `href="#id"`).

#### To Manually Update Mappings
```bash
curl -sL https://raw.githubusercontent.com/chainguard-dev/dfc/main/pkg/dfc/builtin-mappings.yaml \
  -o data/package-mappings.yaml
npm run build
```

## Technical Details & Gotchas

### Hugo Data Access
**CRITICAL:** Hugo has issues with hyphenated data file names. Must use `index` function:
```go
{{ index $.Site.Data "package-mappings" "images" }}
{{ index $.Site.Data "package-mappings" "packages" "debian" }}
{{ index $.Site.Data "package-mappings" "packages" "fedora" }}
```

**DO NOT USE:** `$.Site.Data.package_mappings` (doesn't work reliably)

### Bootstrap 5 Syntax - CRITICAL
**Site uses Bootstrap 5.1** - this caused a bug during implementation!

**CORRECT Bootstrap 5 syntax:**
```html
<a data-bs-toggle="collapse" data-bs-target="#tableId">
```

**WRONG Bootstrap 4 syntax (DO NOT USE):**
```html
<a data-toggle="collapse" href="#tableId">
```

**Bug Story:** Initially implemented with Bootstrap 4 syntax. Tables rendered but wouldn't expand when clicked. Had to update all three shortcodes to use `data-bs-toggle` and `data-bs-target`. Check `package.json` shows `"bootstrap": "^5.1"`.

### Why Bootstrap Collapse, Not `<details>`?
Initially tried `<details open>` → User wanted collapsed by default → Changed to `<details>` without `open`

Then user asked: "Is this well-suited for LLMs?"
- Problem: `<details>` might be ignored/deprioritized by some LLMs
- Solution: Bootstrap collapse - content is in DOM (good for LLMs), just CSS-hidden (good for UX)
- Best of both worlds

Tables are collapsed by default (no `show` class), but all content is in the HTML DOM for LLMs.

## Known Issues & Solutions

### Issue: Tables Not Expanding (HAPPENED DURING DEV)
**Symptom:** Tables render but clicking button does nothing
**Cause:** Using Bootstrap 4 syntax (`data-toggle`, `href`) instead of Bootstrap 5
**Solution:** Use `data-bs-toggle="collapse"` and `data-bs-target="#id"`
**Check:** Verify in browser inspector that buttons have `data-bs-toggle` attribute

### Issue: Empty Table Bodies (HAPPENED DURING DEV)
**Symptom:** Tables render but have no rows, `<tbody>` is empty
**Cause:** Wrong Hugo data access syntax
**Solution:** Use `{{ index $.Site.Data "package-mappings" "packages" "debian" }}`
**Verification:** Check source HTML has table rows with `<code>` tags

### Issue: Mappings Not Updating
**Check:**
1. GitHub Actions logs for "Fetch latest package mappings" step
2. Verify curl succeeded and file size looks right (~9KB)
3. Check `/data/package-mappings.yaml` created before Hugo build
4. Confirm data file is NOT in git (it's in `.gitignore`)

### Issue: Build Failures Locally
**Cause:** Missing `/data/package-mappings.yaml` (it's not in git)
**Solution:**
```bash
curl -sL https://raw.githubusercontent.com/chainguard-dev/dfc/main/pkg/dfc/builtin-mappings.yaml \
  -o data/package-mappings.yaml
```
Then rebuild: `npm run build`

## Current State & Next Steps

### ✅ Completed & Working
- [x] Main documentation page created with comprehensive explanations
- [x] Three Hugo shortcodes for collapsible tables (Debian, Fedora, Images)
- [x] Automatic data fetching in two GitHub Actions workflows
- [x] Bootstrap 5 collapse working correctly
- [x] Tables collapsed by default, expand on click
- [x] All 200+ mappings embedded in HTML DOM (LLM-friendly)
- [x] Data file ignored in git (`.gitignore`)
- [x] Build tested successfully locally
- [x] Section order: Packages first, then Images

### 🎯 Design Constraints to Remember
1. **Must maximize AEO** - This is the PRIMARY goal
2. **Content must be in HTML** - Not external links
3. **Bootstrap 5 syntax only** - Site is on v5.1
4. **Auto-update every build** - No scheduled jobs
5. **Collapsed by default** - User preference for UX

### 💡 If You Need to Extend This

**Add a new package type (e.g., "Alpine packages" with actual mappings):**
1. Upstream YAML would need new section under `packages:`
2. Create new shortcode: `/layouts/shortcodes/package-mappings/alpine-packages.html`
3. Copy structure from `debian-packages.html`
4. Update main doc to include new section
5. Ensure unique ID for collapse div

**Change table styling:**
- Edit shortcodes in `/layouts/shortcodes/package-mappings/`
- Tables use: `class="table table-striped"`
- Buttons use: `class="btn btn-sm btn-outline-secondary"`
- Bootstrap classes already available

**If upstream YAML structure changes:**
1. Compare new structure to current at `/data/package-mappings.yaml`
2. Update Hugo template syntax in shortcodes
3. Test locally before pushing

### 🔍 Verification Commands
```bash
# Check mappings are in HTML
grep -c "<code>build-base</code>" public/chainguard/chainguard-images/about/package-name-mappings/index.html

# Check Bootstrap 5 syntax
grep "data-bs-toggle" public/chainguard/chainguard-images/about/package-name-mappings/index.html

# Count collapse sections
grep -c 'class=collapse' public/chainguard/chainguard-images/about/package-name-mappings/index.html
# Should output: 3 (or more if minified HTML adds extra classes)

# Verify data file exists and is fresh
ls -lh data/package-mappings.yaml
# Should be ~9KB
```

## Important Reminders for Future AI Assistants

1. **The user cares deeply about AEO** - Always optimize for LLM consumption
2. **Don't suggest external links** - Content must be embedded
3. **Bootstrap 5, not 4** - Check the version before suggesting code
4. **Section order matters** - User specifically wanted packages before images
5. **Data file not in git** - It's fetched at build time, intentionally in `.gitignore`
6. **User prefers collapsed tables** - Better UX, still LLM-friendly via DOM
7. **Test locally requires manual fetch** - `curl` the YAML first, then build

## Session Summary for Context

### What User Asked For (In Order)
1. "Document how Chainguard maps package names, ideal for LLMs to understand"
2. Chose hybrid approach: full content embedded + Hugo templates
3. "I want it to update automatically when the site is built" (not scheduled)
4. "Can you draft the PR comment for the last commit?" (separate task, completed)
5. "Package mappings should come before image mappings"
6. "Can tables be collapsible?"
7. "Can they be collapsed by default?"
8. "Is this well-suited for LLMs?" → Led to Bootstrap collapse optimization
9. "Tables aren't expanding" → Fixed Bootstrap 5 syntax issue
10. "Create README for AI assistant context" → This document

### Conversation Flow & Pivots
- Started with scheduled automation → User wanted build-time automation
- Started with `<details open>` → User wanted collapsed → Then optimized for LLMs
- Had Bootstrap 4 bug → Fixed to Bootstrap 5

### Final Deliverables
1. Documentation page: `/content/chainguard/chainguard-images/about/package-name-mappings.md`
2. Three shortcodes: `/layouts/shortcodes/package-mappings/*.html`
3. Modified workflows: `.github/workflows/cloud-run.yaml` and `autodocs-platform.yaml`
4. Maintenance docs: `/docs/PACKAGE_MAPPINGS_UPDATE.md`
5. This README for AI assistant handoff

## References

- **Source YAML:** https://github.com/chainguard-dev/dfc/blob/main/pkg/dfc/builtin-mappings.yaml
- **dfc Tool:** https://github.com/chainguard-dev/dfc
- **Bootstrap 5 Collapse:** https://getbootstrap.com/docs/5.1/components/collapse/
- **Hugo Data Templates:** https://gohugo.io/templates/data-templates/
- **Hugo Index Function:** https://gohugo.io/functions/index-function/

---

**Session Date:** October 23, 2025
**System Status:** ✅ Complete & Operational
**Next AI Assistant:** You have everything you need to pick this up. Good luck! 🚀
