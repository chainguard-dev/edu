#!/usr/bin/env python3
"""Content checks for Hugo markdown, run as pre-commit hooks.

Two modes, selected with --mode:

  tags   Validate frontmatter tags against the approved taxonomy. Blocks the
         commit on errors (e.g. an all-caps tag that is not a known acronym).
         Runs locally and in CI.

  spell  Spell-check prose with aspell, skipping code blocks, shortcodes and
         URLs. Advisory only: it reports misspellings but never fails. Runs
         locally; the CI job skips it via SKIP=content-spellcheck.

Filenames are provided by pre-commit; only content/*.md paths are considered.
Date/lastmod stamping is intentionally NOT here -- that stays in the
.githooks/pre-commit git hook so it can auto-restage into the same commit.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

# Approved tags from TAG_GUIDELINES.md
APPROVED_TAGS = {
    # Product Tags
    "Chainguard Containers",
    "Chainguard Libraries",
    "chainctl",
    "Enforce",
    "Chainguard OS",
    # Action-Oriented Tags
    "Migration",
    "Integration",
    "Configuration",
    "Monitoring",
    "Debugging",
    "Performance",
    "Automation",
    "Troubleshooting",
    # Problem-Solving Tags
    "FAQ",
    "Recommended Practices",
    # Content Type Tags
    "Overview",
    "Procedural",
    "Conceptual",
    "Reference",
    "Video",
    "Learning Labs",
    "Workshop",
    # Lifecycle Tags
    "Installation",
    "Upgrade",
    "Deprecation",
    "Getting Started",
    # Platform/Tool Tags
    "AWS",
    "GCP",
    "Azure",
    "Multi-Cloud",
    "JFrog Artifactory",
    "Sonatype Nexus Repository",
    "Cloudsmith",
    "GitHub",
    "GitLab",
    "Jenkins",
    "Harbor",
    "Docker Hub",
    "Terraform",
    "Kubernetes",
    "OIDC",
    # Topic Tags
    "Security",
    "SBOM",
    "CVE",
    "VEX",
    "Compliance",
    "Standards",
    "SLSA",
    "OCI",
    "AI",
    # Language/Framework Tags
    "Python",
    "Java",
    "Go",
    "Node.js",
    "JavaScript",
    "Ruby",
    "PHP",
    "Rust",
    ".NET",
    # Tool-Specific Tags
    "apko",
    "melange",
    "Wolfi",
    "Cosign",
    "Rekor",
    "Fulcio",
    # Compliance Standards
    "CMMC 2.0",
    "PCI DSS 4.0",
    # Other existing tags
    "Product",
}

# Tags allowed to be all-caps (acronyms / product names).
ACRONYM_TAGS = {
    "CVE",
    "SBOM",
    "FAQ",
    "OCI",
    "SLSA",
    "VEX",
    "AI",
    "OIDC",
    "AWS",
    "GCP",
    "CMMC 2.0",
    "PCI DSS 4.0",
    ".NET",
}

TECH_TERMS = {
    "chainguard",
    "chainctl",
    "kubernetes",
    "docker",
    "terraform",
    "yaml",
    "json",
    "api",
    "cli",
    "sdk",
    "oauth",
    "oidc",
    "jwt",
    "sbom",
    "cve",
    "vex",
    "slsa",
    "oci",
    "cosign",
    "rekor",
    "fulcio",
    "apko",
    "melange",
    "wolfi",
    "distroless",
    "cgr",
    "dev",
    "dockerfile",
    "github",
    "gitlab",
    "jenkins",
    "artifactory",
    "npm",
    "pip",
    "maven",
    "gradle",
    "cargo",
    "rustup",
    "aws",
    "gcp",
    "azure",
    "eks",
    "gke",
    "aks",
    "https",
    "http",
    "url",
    "uri",
    "uuid",
    "sha",
    "md",
    "config",
    "repo",
    "env",
    "vars",
    "auth",
    "creds",
    "namespace",
    "pod",
    "configmap",
    "deployment",
    "ingress",
    "frontend",
    "backend",
    "middleware",
    "webhook",
    "async",
    "boolean",
    "string",
    "int",
    "float",
    "struct",
    "enum",
    "stdin",
    "stdout",
    "stderr",
    "regex",
    "grep",
    "sed",
    "ci",
    "cd",
    "devops",
    "gitops",
    "mlops",
    "devsecops",
    "lts",
    "eol",
    "semver",
    "changelog",
    "readme",
    "grype",
    "apks",
    "glibc",
    "musl",
    "unpatched",
    "sla",
    "slas",
    "chainguard's",
    "bazel",
    "apk",
    "nano",
    "lastmod",
    "netrc",
    "iam",
}


def content_markdown(paths):
    """Filter args down to existing content/*.md files."""
    return [
        p
        for p in paths
        if p.endswith(".md") and p.startswith("content/") and Path(p).exists()
    ]


def extract_tags(filepath):
    try:
        content = Path(filepath).read_text(encoding="utf-8")
    except OSError as exc:
        print(f"Error reading {filepath}: {exc}")
        return []
    match = re.search(r"^tags:\s*\[(.*?)\]", content, re.MULTILINE)
    if not match:
        return []
    return re.findall(r'"([^"]+)"', match.group(1))


def validate_tags(paths):
    """Return exit code: 1 if any blocking tag errors found, else 0."""
    had_error = False
    for filepath in content_markdown(paths):
        tags = extract_tags(filepath)
        if not tags:
            continue
        warnings, errors = [], []
        if len(tags) > 5:
            warnings.append(
                f"  ⚠️  Too many tags ({len(tags)}). Maximum recommended: 5"
            )
        for tag in tags:
            if tag not in APPROVED_TAGS and tag not in ACRONYM_TAGS:
                warnings.append(f"  ⚠️  Tag not in approved list: '{tag}'")
            if tag not in ACRONYM_TAGS and tag.isupper():
                errors.append(f"  ❌  Tag should use Title Case: '{tag}'")
        if warnings or errors:
            print(f"\n📄 {filepath}")
            print(f"   Tags: {', '.join(tags)}")
            for line in warnings + errors:
                print(line)
        if errors:
            had_error = True
    if had_error:
        print("\n❌ Commit blocked due to tag errors. See TAG_GUIDELINES.md.")
        return 1
    return 0


def check_spelling(paths):
    """Advisory spell check. Always returns 0 (never blocks)."""
    if subprocess.run(["which", "aspell"], capture_output=True).returncode != 0:
        print(
            "ℹ️  aspell not installed; skipping spell check "
            "(brew install aspell / apt install aspell)."
        )
        return 0

    personal_dict = Path(__file__).resolve().parent.parent.parent / ".aspell.en.pws"
    for filepath in content_markdown(paths):
        lines = Path(filepath).read_text(encoding="utf-8").splitlines()
        frontmatter_end = 0
        if lines and lines[0].strip() == "---":
            for i, line in enumerate(lines[1:], 1):
                if line.strip() == "---":
                    frontmatter_end = i + 1
                    break

        misspelled_by_word = {}
        in_code_block = False
        for line_num, line in enumerate(lines, 1):
            if line_num <= frontmatter_end:
                continue
            if line.strip().startswith("```"):
                in_code_block = not in_code_block
                continue
            if in_code_block:
                continue
            cleaned = re.sub(r"\{\{[</%].*?[>/%]\}\}", "", line)
            cleaned = re.sub(r"`[^`]+`", "", cleaned)
            cleaned = re.sub(r"https?://[^\s\)]+", "", cleaned)
            if not cleaned.strip():
                continue
            cmd = ["aspell", "list", "--mode=markdown", "--lang=en_US"]
            cmd.extend(
                ["--personal", str(personal_dict)]
                if personal_dict.exists()
                else ["--personal=/dev/null"]
            )
            result = subprocess.run(cmd, input=cleaned, capture_output=True, text=True)
            for word in result.stdout.split():
                if len(word) <= 2 or word.lower() in TECH_TERMS or word.isupper():
                    continue
                if re.match(r"^[a-z]+[A-Z]", word) or re.match(
                    r"^[A-Z][a-z]+[A-Z]", word
                ):
                    continue
                misspelled_by_word.setdefault(word, []).append(line_num)

        if misspelled_by_word:
            print(f"\n📝 Possible spelling issues in {filepath}:")
            for word, line_nums in list(misspelled_by_word.items())[:10]:
                shown = ", ".join(map(str, line_nums[:5]))
                if len(line_nums) > 5:
                    shown += f", ... (+{len(line_nums) - 5})"
                print(f"     - '{word}' on line(s): {shown}")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", required=True, choices=["tags", "spell"])
    parser.add_argument("files", nargs="*")
    args = parser.parse_args()

    paths = content_markdown(args.files)
    if not paths:
        return 0
    return validate_tags(paths) if args.mode == "tags" else check_spelling(paths)


if __name__ == "__main__":
    sys.exit(main())
