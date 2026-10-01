# Translations

Chainguard Academy can serve pages in languages other than English. Brazilian Portuguese (`pt-br`) is the pilot language. Its pages live at `/pt-br/`, and English stays at the site root.

## How the site handles languages

- Each language has its own content directory. English pages live in `content/`, and Portuguese pages live in `content-pt-br/`. Hugo pairs a translation with its English page by file path, so `content-pt-br/get-started/get-support.md` is the translation of `content/get-started/get-support.md`.
- A page exists in a language only when someone translates it. Links in a translated page go to the translated page when one exists and to the English page otherwise. Hugo's built-in link handling does this; write links with English paths, such as `/get-started/get-support/`.
- On a translated page, the sidebar shows the full English navigation. Entries with a translation link to it and show its title.
- A translated section page lists every page in the English section, linking to translations where they exist. Hugo turns each top-level directory into a section, so translating a page under `chainguard/` or `platform/` also needs a translated `_index.md` for that top-level section.
- A translated page's back button points to its English parent section, or that section's translation if one exists.
- Interface text, such as "On this page" and the feedback widget, comes from `i18n/en.toml` and `i18n/pt-br.toml`. Templates read it with `{{ T "key" }}`.
- A page with a translation lists the other versions in its `<head>` with `hreflang` links.

## How readers choose a language

Every page has a language menu in the sidebar, under Ask AI. English is the default.

- Choosing a language saves it in the reader's browser (`localStorage`, key `academy-language`). Opening any non-English page saves that page's language too.
- On an English page, a reader whose saved language is Portuguese goes straight to the page's Portuguese translation, if one exists. A script in `<head>` does the redirect before the page renders. The script is `layouts/partials/i18n/language-preference.html`.
- When a page has no translation, the reader stays on the English page. The menu labels the missing translation, and a note under the menu, in the reader's language, says the page hasn't been translated yet. The note's text is the `untranslatedNotice` param in `config/_default/languages.toml`.
- A reader with no saved language always gets English. The site doesn't detect the browser's language.
- Search engines don't run the redirect, so they index each language's URLs separately.
- Search returns English results on every page. Ask AI answers in the language of the question and cites English sources.
- Tag pages exist only in English.

## Translate a page

1. Copy the English file to the same path under `content-pt-br/`.
1. Translate the front matter `title`, `linktitle`, `lead`, and `description`, and the body. Keep `date`, `weight`, `type`, and `tags` as they are. Drop `aliases`.
1. Set `lastmod` to today.
1. Add a `translation` block that records the English page's `lastmod` at the time you translated it:

   ```yaml
   translation:
     sourceLastmod: 2026-09-28T14:00:04+00:00
     reviewed: false
   ```

1. Set `reviewed: true` after a native speaker reviews the translation.

Leave these in English:

- Code blocks, commands, flags, file paths, and image names.
- Product names, such as Chainguard Containers, Chainguard Libraries, and chainctl.
- Labels from the Chainguard Console, such as **Settings > Users**, because the Console is in English.
- Shortcodes. Shared blurbs, such as `{{< blurb/noproxy >}}`, render in English.

## Keep translations current

Every translated page shows a notice that links to the English original. When the English page's `lastmod` is later than the translation's `sourceLastmod`, the notice warns readers that the translation may be out of date, and the build logs a warning that names both files:

```text
WARN  translation out of date: [pt-br] get-started/get-support.md was translated from [en] get-started/get-support.md at lastmod 2026-01-01T00:00:00Z, and the source lastmod is now 2026-09-28T14:00:04Z
```

To clear the warning, update the translation and set `sourceLastmod` to the English page's current `lastmod`.

## Add interface text

When a template needs new interface text:

1. Add the key and the English string to `i18n/en.toml`.
1. Add the same key with the translated string to `i18n/pt-br.toml`.
1. In the template, use `{{ T "your_key" }}`.

A key missing from `pt-br.toml` falls back to English. To list missing keys, run `hugo --printI18nWarnings`.

## Build locally

Hugo compiles the site's SCSS with Dart Sass. If Dart Sass isn't on your `PATH`, Hugo reuses the CSS cached in `resources/_gen` without warning, so style changes don't appear. The repository's npm dependencies include Dart Sass:

```shell
PATH="$PWD/node_modules/.bin:$PATH" npm run start
```

## Add a language

1. Add a block to `config/_default/languages.toml`, modeled on `[pt-br]`. Set `kapaLanguage` to the language's code in [Kapa's supported languages](https://docs.kapa.ai/integrations/website-widget/configuration/behavior), or leave it out to keep the Ask AI widget's built-in text in English. If the translated `ask_ai` string doesn't fit the floating Ask AI button, set `kapaButtonWidth`; the default is `4.5rem`.
1. Create its content directory, with an `_index.md` for the home page. Copy `content-pt-br/_index.md`, which limits the home page's outputs to HTML and the sitemap. The site-wide files, such as redirects and the AI Docs exports, come from the English home page only.
1. Add `i18n/<language>.toml` with every key from `i18n/en.toml`.
