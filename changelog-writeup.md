# Chainguard Academy Changelog — Build Summary

## What was built

A new changelog section at `content/chainguard/chainguard-images/changelog/` with the following structure:

```
changelog/
  _index.md       — section landing page with links to year pages
  2026.md         — all 2026 entries
```

Each year lives in a single file (e.g., `2026.md`). Entries within a year are ordered newest-first, grouped under date headings.

Two supporting files were also added:

- **`layouts/shortcodes/changelog-label.html`** — a shortcode that renders a colored badge for the entry type (e.g., Breaking Change, New Feature, Security Advisory)
- **`assets/scss/components/_changelog.scss`** — styles for the badges and their spacing relative to entry headings; imported via `app.scss`

---

## Entry format

Each entry in a year file follows this pattern:

```markdown
## Month Day Year

{{</* changelog-label "Label Type" */>}}

#### Entry title summarizing the change

One or two sentences describing what changed and, if applicable, what the reader needs to do.
```

Supported label types and their colors:

| Label | Color |
|---|---|
| `Breaking Change` | Red |
| `Update` | Brand aqua |
| `New Feature` | Brand purple |
| `Deprecation` | Orange |

---

## Adding real entries

1. **New entry in an existing year** — open the relevant year file (e.g., `2026.md`) and add the entry at the top, under a new or existing date heading. Update the `lastmod` field in the frontmatter to today's date.

2. **New year** — copy `2026.md`, rename it (e.g., `2027.md`), clear the entries, update the frontmatter dates, and add a link to it in `_index.md`.

3. **New label type** — add a CSS rule to `_changelog.scss` following the existing pattern; the shortcode will handle the class name automatically by lowercasing and hyphenating whatever string you pass in.

---

## Connecting to an API

There are two main approaches, and the right choice depends on how fresh the data needs to be:

### Option 1: Build-time fetch (Hugo `resources.GetRemote`)

Hugo can call a remote API at build time and render the response into static pages. You'd replace the hand-authored markdown entries with a Hugo template that fetches JSON from the API and loops over the results, outputting the same label/heading/description structure.

**Pros:** No JavaScript required, pages stay fully static, works with existing layout.
**Cons:** Data is only as fresh as the last site build. Requires a rebuild (and redeploy) to pick up new changelog entries.

This is the right fit if the changelog is updated infrequently (e.g., a few times a week) and your CI/CD already triggers builds on a schedule or webhook.

### Option 2: Client-side fetch

A small JavaScript snippet on the changelog page fetches from the API at page load and renders entries into the DOM. The markdown file would just be a shell with a placeholder element.

**Pros:** Always up to date without a rebuild.
**Cons:** Requires JS, adds a loading state, and the Hugo shortcode/label system wouldn't apply — you'd need to replicate the badge styling in JS-rendered HTML.

### Recommendation

Given that this is a Hugo static site and the changelog doesn't need to be real-time, **Option 1 is the cleaner fit**. The year files (`2026.md`) would become templates rather than authored content, and the `changelog-label` shortcode logic would move into the template loop.

When the API is ready, the migration path would be:
1. Agree on the JSON schema the API returns
2. Write a Hugo partial that maps API fields (change type, date, title, description) to the existing visual structure
3. Replace the authored year files with template-driven ones that call `resources.GetRemote`

---

## Proposed API JSON schema

Based on the entry structure used in the static changelog, here is a proposed schema for the API response:

```json
{
  "entries": [
    {
      "id": "2026-04-01-openssl-cve-xxxxx",
      "date": "2026-04-01",
      "change_type": "security-advisory",
      "title": "OpenSSL CVE-2026-XXXXX patched in all images",
      "description": "All Chainguard Container images containing OpenSSL have been updated to address CVE-2026-XXXXX, a high-severity vulnerability affecting TLS handshake processing. Pull the latest version of any affected image; if you are pinned to a digest, update your digest reference.",
      "affects": "All images containing OpenSSL",
      "action_required": true,
      "links": [
        {
          "label": "Learn more",
          "url": "https://edu.chainguard.dev/chainguard/chainguard-images/changelog/2026/#openssl-cve-2026-xxxxx-patched-in-all-images"
        }
      ]
    }
  ]
}
```

### Field reference

| Field | Type | Description |
|---|---|---|
| `id` | string | Unique identifier; used to generate anchor links |
| `date` | string (ISO 8601) | Date of the change |
| `change_type` | string (enum) | One of: `breaking-change`, `update`, `new-feature`, `deprecation` |
| `title` | string | Short entry title (used as the heading) |
| `description` | string | One or two sentences describing the change and any required action |
| `affects` | string | Optional. What products, images, or users are affected |
| `action_required` | boolean | Whether the reader needs to take action |
| `links` | array | Optional. Related links (docs pages, CVE records, etc.) |

The `change_type` values are intentionally aligned with the CSS class slugs already used by the `changelog-label` shortcode, so no mapping layer is needed when rendering.
