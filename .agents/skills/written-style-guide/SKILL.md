---
name: written-style-guide
description: Review Chainguard-facing copy for voice, tone, product naming, and brand-mechanics compliance. Use whenever the user asks you to check, edit, review, proofread, polish, or give feedback on copy a Chainguard audience will read — product UI strings, marketing and landing pages, docs, blog posts, social, email, sales materials, release notes, taglines, or campaign copy. Also use whenever the user mentions "Chainguard style guide," "Chainguard voice," "Linky-approved," or asks whether something is on-brand. This is a brand-compliance layer on top of `writing-clearly-and-concisely` — load both when reviewing Chainguard-facing prose; this skill assumes the universal clarity rules are already being applied. Default behavior is to flag issues with suggested fixes, not to rewrite wholesale unless asked. Err on the side of triggering whenever Chainguard-facing text is involved — do not skip it because the text "looks fine."
---

# Chainguard Style Guide Reviewer

This skill reviews text for alignment with Chainguard's brand voice, tone, and style guide. The default mode is **review** — flag problems with concrete fixes. Rewrite the full text only when the user explicitly asks.

## Relationship to `writing-clearly-and-concisely`

This skill is the **Chainguard brand layer**. It assumes the universal writing rules from `writing-clearly-and-concisely` (Strunk: active voice, positive form, concrete language, omit needless words; plus AI-pattern avoidance) are already being applied. For any prose review, load `writing-clearly-and-concisely` first as the foundation, then use this skill to add Chainguard-specific checks: voice and tone calibration, product naming, word-list terms, and brand mechanics (Oxford comma, em dashes with spaces, sentence case, no exclamation points). If you only load this skill, you'll catch brand violations but miss general clarity problems.

## When this skill triggers

Trigger on any of these signals:

- The user pastes or attaches copy and asks for a check, review, edit, proofread, polish, or feedback, in a context where Chainguard is the brand (Chainguard product names mentioned, Chainguard employee context, or the user explicitly says "for Chainguard")
- The user asks whether something is "on-brand," "in Chainguard's voice," or "Linky-approved"
- The user asks about a specific Chainguard style rule (product naming, capitalization, etc.)
- The user is drafting Chainguard-facing copy and wants help

If the user asks you to **write** something from scratch for Chainguard, apply the rules silently as you write, and offer a brief style note at the end if you made any non-obvious choices (e.g., "I used 'engineers' rather than 'developers' per Chainguard style").

## Core workflow for a review

1. **Identify the channel and tone target.** Ask or infer:
   - Is this marketing copy, product UI, docs, social, email, a tagline, or something else?
   - Chainguard tone moves on a spectrum — playful/quirky for social, campaigns, top-of-funnel blogs, and brand experiences; direct/credible for docs, data-driven guides, executive thought leadership, and sales enablement. Calibrate feedback accordingly: don't tell a LinkedIn post to be more formal, and don't tell a docs page to loosen up.

2. **Read the text end-to-end before commenting.** Voice and tone are holistic. A sentence that reads stiff in isolation may be right for the piece.

3. **Check against the rules below in this order**, flagging every issue found:
   - **Voice** (does it sound confident, quirky-where-appropriate, empowering, practical/peer-to-peer?)
   - **Product naming and capitalization** (the highest-risk category — Chainguard is strict here. See `references/product-names.md`.)
   - **Word list terms** (CVEs, FIPS, STIGs, etc. — see `references/word-list.md`)
   - **Grammar and mechanics** (Chicago Manual of Style, US English, Oxford comma, em dashes, numbers, dates — see `references/grammar-mechanics.md` for the full list)
   - **Inclusivity** (gendered language, stereotypes, global readability)
   - **Audience framing** (does it speak to the reader's problem, or does it focus on the product?)

4. **Present feedback** in this format, with issues grouped by impact:
   - **Overall read:** one or two sentences on whether the piece lands, and for what channel.
   - **High-impact issues:** the things that change how the copy reads or lands — wrong product names, voice/tone problems, product-vs-problem framing, unsupported boastful claims, passive voice in high-visibility spots, inclusivity issues, factual errors. For each: quote the offending phrase in `inline code`, say what's wrong, and give the suggested fix, also in `inline code`. Use a numbered list. If there are no high-impact issues, say so explicitly ("No high-impact issues — this reads well for the channel") and move on.
   - **Mechanical fixes:** the smaller rule-enforcement fixes — capitalization, commas, ampersands, en/em dashes, number formatting, date/time formatting, URL formatting, etc. Group these as a single bulleted list (not numbered), one line per fix, so they're easy to scan and apply in bulk. Use the format `` `original` → `replacement` `` with inline code on both sides. If several fixes are the same type (e.g., three `ChainGuard` → `Chainguard` corrections), collapse them into one line with a count. **Only include things that need to change.** Don't list items just to confirm they're correct — move positive observations to the Strengths section. If there are no mechanical fixes, omit the section entirely rather than saying "none."
   - **Strengths:** one short bullet list of what's working, so the author knows what to preserve.
   - **Offer a rewrite:** end with "Want me to apply these fixes and return a clean version?" Do not rewrite unprompted.

   The inline code formatting makes the before/after jump out visually and makes it obvious which text is being quoted from the source versus which is your suggestion. Always use it for quoted phrases and replacement text, even in the high-impact section.

   The point of the split is so the author sees the serious issues first and isn't overwhelmed by a long numbered list where issue #2 is "wrong product name" and issue #9 is "missing Oxford comma." If high-impact and mechanical issues are mixed, the mechanical ones dilute the signal.

5. **If the user then asks for a rewrite**, apply all the fixes you flagged, preserve the author's structure and any voice choices that were working, and return the revised text. Don't silently change things you didn't flag in the review — if you spot something new, call it out separately.

## The non-negotiables (check these every time)

These are the rules most commonly broken. Always check them:

- **"Chainguard"** is always capitalized. Never "ChainGuard," never "CG."
- **Product names** are capitalized proper nouns; generic descriptions are lowercase. "Chainguard Containers is…" (singular verb, capitalized) vs. "Chainguard offers container images…" (lowercase, plural). This distinction is the single biggest source of style errors. When in doubt, check `references/product-names.md`.
- **Oxford comma**, always.
- **Em dashes have spaces on either side** — like this. (Chainguard's house style; note this differs from Chicago's default.)
- **Sentence case for web H1/H2/H3 and buttons/CTAs.** Title case for report/PDF H1/H2 only. Navigation uses title case.
- **No ampersands** (except in proper nouns like "H&M").
- **No exclamation points** (avoid them).
- **Active voice.** Watch for "by" and "is/was \_\_\_ed."
- **Spell out numbers zero through nine**; numerals for 10+. Ranges always use numerals.
- **Contractions are encouraged** (he's, can't, would've) — they're part of the voice.
- **US English, Merriam-Webster** (color not colour, organize not organise).
- **"Engineers" or "software engineers"** is preferred over "developers."
- **"Open source"** is never hyphenated, adjective or noun.
- **No "i.e." or "e.g."** — write it out (global readability).
- **Avoid "In today's modern world"** and other generic AI-sounding fluff.

## When to consult the reference files

The reference files hold the full detail. Load the relevant one when:

- **`references/product-names.md`** — any time the text mentions a Chainguard product or feature. This includes Chainguard Containers, Chainguard Libraries, Chainguard VMs, Chainguard OS Packages, Chainguard Actions, Chainguard Agent Skills, Guardener, Chainguard Repository, Chainguard Commercial Builds, Chainguard Catalog Starter, Custom Assembly, EOL Grace Period, Private APK Repositories, the Chainguard Factory, Chainguard OS, and the Images Catalog. Product naming has the most specific rules and the most common errors.
- **`references/word-list.md`** — any time the text uses CVEs, FIPS, STIGs, FedRAMP, NIS2, PCI DSS, SBOMs, "Zero CVEs," "Assemble" (the conference), or similar acronyms/technical terms.
- **`references/grammar-mechanics.md`** — for detailed rules on dates, times, numbers, punctuation, hyphens/dashes, lists, quotation marks, parentheses, URLs, and capitalization edge cases.
- **`references/voice-and-tone.md`** — when the user asks about voice, tone, or whether something is "on-brand," or when writing longer pieces where voice calibration matters more than mechanics.

Always read the relevant reference file fully before giving feedback that depends on it — don't guess at the detail.

## A note on being useful, not pedantic

The goal is to help the author write better Chainguard copy, not to catalog every micro-infraction. If a piece has ten serious issues, lead with those; don't bury them under twenty comma notes. If a piece is basically clean, say so, and keep the feedback tight.

Chainguard's voice is "practical, straightforward, a trusted peer who's been there with you before." The review should sound that way too.
