# Writing Clearly and Concisely

A skill that applies William Strunk Jr. and E.B. White's timeless writing principles to produce clearer, stronger, more professional prose while avoiding common AI writing patterns.

## Purpose

This skill helps you write better prose for human readers. It draws from two sources:

1. **The Elements of Style** (Strunk, 1918) - Time-tested rules for clear, forceful writing. This book is sometimes referred to as "Strunk and White".
2. **AI Pattern Avoidance** - Research-backed guidance on avoiding generic, puffy language that LLMs tend to produce

Whether you're writing documentation, commit messages, error messages, or any text humans will read, this skill helps you cut fluff and say what you mean.

## When to Use

Use this skill whenever you write prose for humans:

- **Documentation** - README files, API docs, technical explanations
- **Git workflow** - Commit messages, pull request descriptions
- **User-facing text** - Error messages, UI copy, help text, tooltips
- **Code comments** - Inline documentation, docstrings
- **Reports and summaries** - Status updates, analysis, explanations
- **Editing** - Improving clarity of existing text

**Trigger phrases:**
- "Write documentation for..."
- "Draft a README"
- "Edit this for clarity"
- "Make this more concise"
- "Review this commit message"

## How It Works

1. **Load the skill** when writing prose for human readers
2. **Apply Strunk's core principles** - active voice, positive form, concrete language, cut needless words
3. **Avoid AI patterns** - no puffery, no empty phrases, no promotional adjectives
4. **Reference detailed guides** when needed for specific rules

### Context-Efficient Approach

The skill uses progressive disclosure to save context:

- **SKILL.md** (~1,000 tokens) loads first with the core rules
- **Reference files** (1,000-4,500 tokens each) load only when needed
- **Most tasks need only one file**: `03-elementary-principles-of-composition.md`

For tight context situations, dispatch a subagent with your draft and the relevant section file.

## Key Features

### Strunk's Core Rules

The skill emphasizes these principles from *The Elements of Style*:

| Rule | Principle |
|------|-----------|
| 10 | Use active voice |
| 11 | Put statements in positive form |
| 12 | Use definite, specific, concrete language |
| 13 | Omit needless words |
| 16 | Keep related words together |
| 18 | Place emphatic words at end of sentence |

### AI Pattern Detection

The skill identifies and eliminates common LLM writing patterns:

- **Puffery**: pivotal, crucial, vital, testament, enduring legacy
- **Empty "-ing" phrases**: ensuring reliability, showcasing features
- **Promotional adjectives**: groundbreaking, seamless, robust, cutting-edge
- **Overused AI vocabulary**: delve, leverage, multifaceted, foster, realm, tapestry
- **Formatting overuse**: excessive bullets, emoji decorations, bold on every other word

## Reference Files

| Section | File | Tokens | Content |
|---------|------|--------|---------|
| Grammar & punctuation | `02-elementary-rules-of-usage.md` | ~2,500 | Comma rules, possessives, sentence structure |
| Composition principles | `03-elementary-principles-of-composition.md` | ~4,500 | Active voice, concision, paragraph structure |
| Formatting | `04-a-few-matters-of-form.md` | ~1,000 | Headings, quotations, formatting conventions |
| Word choice | `05-words-and-expressions-commonly-misused.md` | ~4,000 | Common errors, word selection |
| AI patterns | `signs-of-ai-writing.md` | ~1,000 | Summary of Wikipedia editors' field guide to AI writing |

## Usage Examples

### Example 1: Tightening a Commit Message

**Before:**
> This commit implements the functionality for ensuring that user authentication is properly handled, showcasing robust error handling capabilities.

**After:**
> Add user authentication with error handling

### Example 2: Rewriting Documentation

**Before:**
> This groundbreaking feature leverages cutting-edge technology to deliver a seamless experience, fostering better engagement and driving impactful results.

**After:**
> This feature uses WebSocket connections to update the dashboard in real time.

### Example 3: Fixing Passive Voice

**Before:**
> The configuration file is read by the application at startup.

**After:**
> The application reads the configuration file at startup.

### Example 4: Removing Hedging

**Before:**
> It is important to note that the API might potentially return an error in certain situations.

**After:**
> The API returns an error when the token expires.

## Best Practices

1. **Be specific, not grandiose** - Say what it actually does, not how important it is
2. **Cut first, add later** - Remove words until meaning suffers, then add back what's needed
3. **Prefer active voice** - "The function returns X" beats "X is returned by the function"
4. **State positively** - "He forgot" beats "He did not remember"
5. **Use concrete language** - "The server crashed" beats "An issue occurred"
6. **Load reference files sparingly** - Most tasks need only `03-elementary-principles-of-composition.md`

## Directory Structure

```
writing-clearly-and-concisely/
  SKILL.md                 # Main skill definition
  README.md                # This file
  signs-of-ai-writing.md   # Summary of AI writing patterns
  LICENSE                  # MIT license from the original skill
  NOTICE                   # Sources and their licenses
  elements-of-style/
    01-introductory.md
    02-elementary-rules-of-usage.md
    03-elementary-principles-of-composition.md
    04-a-few-matters-of-form.md
    05-words-and-expressions-commonly-misused.md
```

## Installation

In the [chainguard-dev/edu](https://github.com/chainguard-dev/edu) repository, this skill loads automatically. To use it in other projects, copy this directory into your agent's user skills directory: `~/.agents/skills/` for Codex, Cursor, GitHub Copilot, and Gemini CLI, or `~/.claude/skills/` for Claude Code.

## Attribution

- Original skill by @joshuadavidthomas from [joshuadavidthomas/agent-skills](https://github.com/joshuadavidthomas/agent-skills) (MIT)
- Adapted from [obra/the-elements-of-style](https://github.com/obra/the-elements-of-style)
- Writing principles from *The Elements of Style* by William Strunk Jr. (1918)
- AI pattern summary based on [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (CC BY-SA 4.0)
