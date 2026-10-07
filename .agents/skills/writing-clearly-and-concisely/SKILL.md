---
name: writing-clearly-and-concisely
description: Use whenever you write prose a human will read — documentation, commit messages, code comments, error messages, reports, internal notes, or any explanation. Applies Strunk's timeless rules for clearer, stronger prose and flags common AI writing patterns. This is the foundation skill for all writing; if the prose is also Chainguard-facing (product UI, marketing, docs, blog, social, sales, release notes), load `written-style-guide` alongside it for brand compliance.
---

# Writing Clearly and Concisely

## Overview

Write with clarity and force. This skill covers what to do (Strunk) and what not to do (AI patterns).

### Relationship to `written-style-guide`

This skill covers universal writing quality. For Chainguard-facing copy — anything a Chainguard customer, prospect, or community member will read (product UI, docs, marketing, blog posts, social, sales, release notes, taglines) — also load `written-style-guide`. Apply this skill first for clarity and concision, then layer the Chainguard brand rules on top. `written-style-guide` deliberately doesn't re-state universal writing rules; it assumes this skill is doing that work.

## When to Use This Skill

Use this skill whenever you write prose for humans:

- Documentation, README files, technical explanations
- Commit messages, pull request descriptions
- Error messages, UI copy, help text, comments
- Reports, summaries, or any explanation
- Editing to improve clarity

**If you're writing sentences for a human to read, use this skill.**

## Limited Context Strategy

When context is tight:

1. Write your draft using judgment
2. Dispatch a subagent with your draft and the relevant section file
3. Have the subagent copyedit and return the revision

Loading a single section (~1,000-4,500 tokens) instead of everything saves significant context.

## Elements of Style

William Strunk Jr.'s *The Elements of Style* (1918) teaches you to write clearly and cut ruthlessly.

### Rules

**Elementary Rules of Usage (Grammar/Punctuation)**:

1. Form possessive singular by adding 's
2. Use comma after each term in series except last
3. Enclose parenthetic expressions between commas
4. Comma before conjunction introducing co-ordinate clause
5. Don't join independent clauses by comma
6. Don't break sentences in two
7. Participial phrase at beginning refers to grammatical subject

**Elementary Principles of Composition**:

8. One paragraph per topic
9. Begin paragraph with topic sentence
10. **Use active voice**
11. **Put statements in positive form**
12. **Use definite, specific, concrete language**
13. **Omit needless words**
14. Avoid succession of loose sentences
15. Express co-ordinate ideas in similar form
16. **Keep related words together**
17. Keep to one tense in summaries
18. **Place emphatic words at end of sentence**

### Reference Files

The rules above are summarized from Strunk's original text. For complete explanations with examples:

| Section | File | ~Tokens |
|---------|------|---------|
| Grammar, punctuation, comma rules | `02-elementary-rules-of-usage.md` | 2,500 |
| Paragraph structure, active voice, concision | `03-elementary-principles-of-composition.md` | 4,500 |
| Headings, quotations, formatting | `04-a-few-matters-of-form.md` | 1,000 |
| Word choice, common errors | `05-words-and-expressions-commonly-misused.md` | 4,000 |

**Most tasks need only `03-elementary-principles-of-composition.md`** — it covers active voice, positive form, concrete language, and omitting needless words.

## AI Writing Patterns to Avoid

LLMs regress to statistical means, producing generic, puffy prose. Avoid:

- **Puffery:** pivotal, crucial, vital, testament, enduring legacy
- **Empty "-ing" phrases:** ensuring reliability, showcasing features, highlighting capabilities
- **Promotional adjectives:** groundbreaking, seamless, robust, cutting-edge
- **Overused AI vocabulary:** delve, leverage, multifaceted, foster, realm, tapestry
- **Formatting overuse:** excessive bullets, emoji decorations, bold on every other word

Be specific, not grandiose. Say what it actually does.

For a fuller list of these patterns and why they occur, see `signs-of-ai-writing.md`, a summary of the field guide Wikipedia editors use to spot AI-generated submissions.

## Bottom Line

Writing for humans? Load the relevant section from `elements-of-style/` and apply the rules. For most tasks, `03-elementary-principles-of-composition.md` covers what matters most.
