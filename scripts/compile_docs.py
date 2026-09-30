#!/usr/bin/env python3
"""
Compile Chainguard documentation from multiple sources into a single markdown file
for developers to use with AI assistants.
"""

import os
import re
import json
from pathlib import Path
from html.parser import HTMLParser
from datetime import datetime


class HTMLToMarkdown(HTMLParser):
    """Convert HTML to Markdown"""

    def __init__(self):
        super().__init__()
        self.markdown = []
        self.in_pre = False
        self.in_code = False
        self.list_stack = []
        self.current_text = []

    def handle_starttag(self, tag, attrs):
        if tag == "p":
            if self.current_text:
                self.markdown.append("".join(self.current_text))
            self.current_text = []
        elif tag == "h1":
            self.current_text = ["# "]
        elif tag == "h2":
            self.current_text = ["## "]
        elif tag == "h3":
            self.current_text = ["### "]
        elif tag == "h4":
            self.current_text = ["#### "]
        elif tag == "strong" or tag == "b":
            self.current_text.append("**")
        elif tag == "em" or tag == "i":
            self.current_text.append("*")
        elif tag == "code":
            self.in_code = True
            self.current_text.append("`")
        elif tag == "pre":
            self.in_pre = True
            self.current_text.append("\n```\n")
        elif tag == "ul":
            self.list_stack.append("ul")
        elif tag == "ol":
            self.list_stack.append("ol")
        elif tag == "li":
            indent = "  " * (len(self.list_stack) - 1)
            if self.list_stack and self.list_stack[-1] == "ul":
                self.current_text.append(f"\n{indent}- ")
            elif self.list_stack and self.list_stack[-1] == "ol":
                self.current_text.append(f"\n{indent}1. ")
        elif tag == "a":
            for attr in attrs:
                if attr[0] == "href":
                    self.current_text.append("[")
                    self._link_url = attr[1]
        elif tag == "br":
            self.current_text.append("\n")
        elif tag == "table":
            self.current_text.append("\n")
        elif tag == "tr":
            self.current_text.append("\n|")
        elif tag == "td" or tag == "th":
            self.current_text.append(" ")

    def handle_endtag(self, tag):
        if tag in ["p", "h1", "h2", "h3", "h4"]:
            self.markdown.append("".join(self.current_text))
            self.markdown.append("\n")
            self.current_text = []
        elif tag == "strong" or tag == "b":
            self.current_text.append("**")
        elif tag == "em" or tag == "i":
            self.current_text.append("*")
        elif tag == "code":
            self.in_code = False
            self.current_text.append("`")
        elif tag == "pre":
            self.in_pre = False
            self.current_text.append("\n```\n")
        elif tag == "ul" or tag == "ol":
            if self.list_stack:
                self.list_stack.pop()
        elif tag == "a":
            self.current_text.append(f"]({self._link_url})")
        elif tag == "tr":
            self.current_text.append(" |")
        elif tag == "td" or tag == "th":
            self.current_text.append(" |")

    def handle_data(self, data):
        if self.in_pre:
            self.current_text.append(data)
        else:
            self.current_text.append(data.strip())

    def get_markdown(self):
        if self.current_text:
            self.markdown.append("".join(self.current_text))
        return "\n".join(self.markdown)


def clean_markdown_content(content):
    """Remove HTML comments and clean up markdown content"""
    if not content:
        return content

    # Remove HTML comments like <!--monopod:start-->, <!--overview:end-->, etc.
    content = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)

    # Replace example secrets with sanitized versions to avoid GitHub alerts
    # This preserves the documentation structure while removing false positive alerts
    content = re.sub(
        r'tskey-client-[^\s\'"]+', "tskey-client-EXAMPLE_KEY_REPLACED", content
    )

    # Remove multiple consecutive blank lines
    content = re.sub(r"\n\s*\n\s*\n", "\n\n", content)

    # Strip leading/trailing whitespace
    content = content.strip()

    return content


def read_markdown_file(filepath):
    """Read a markdown file and extract frontmatter and content"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract frontmatter
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                frontmatter = parts[1].strip()
                main_content = parts[2].strip()

                # Parse title from frontmatter
                title_match = re.search(r'title\s*:\s*"([^"]+)"', frontmatter)
                title = title_match.group(1) if title_match else None

                # Clean the content
                main_content = clean_markdown_content(main_content)

                return {
                    "title": title,
                    "frontmatter": frontmatter,
                    "content": main_content,
                }

        # Clean content even if no frontmatter
        content = clean_markdown_content(content)

        return {"title": None, "frontmatter": None, "content": content}
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None


def convert_html_to_markdown(html_content):
    """Convert HTML content to Markdown"""
    parser = HTMLToMarkdown()
    parser.feed(html_content)
    markdown_content = parser.get_markdown()

    # Clean the converted markdown
    return clean_markdown_content(markdown_content)


def process_edu_content(edu_path):
    """Process content from the edu repository"""
    content_path = edu_path / "content"
    docs = []

    for root, dirs, files in os.walk(content_path):
        for file in files:
            if file.endswith(".md"):
                filepath = Path(root) / file
                doc = read_markdown_file(filepath)
                if doc and doc["content"]:
                    relative_path = filepath.relative_to(content_path)
                    # Ensure content is cleaned
                    cleaned_content = clean_markdown_content(doc["content"])
                    if cleaned_content:  # Only add if content remains after cleaning
                        docs.append(
                            {
                                "path": str(relative_path),
                                "title": doc["title"] or file.replace(".md", ""),
                                "content": cleaned_content,
                            }
                        )

    return docs


# The dfc mapping data renders as tables on this page of the site, so its bundle
# section links there. The title differs from the page's own ("Package and image
# name mappings"), which the bundle also carries, so neither section overwrites
# the other in the MCP server's index.
DFC_SECTION_TITLE = "DFC package and image mapping data"
DFC_SECTION_PATH = "chainguard/containers/reference/package-name-mappings.md"


def read_dfc_mappings(edu_path):
    """Return dfc's builtin-mappings.yaml as committed in edu, or None if missing.

    The nightly autodocs-platform workflow copies the file from chainguard-dev/dfc
    into data/package-mappings.yaml, so the bundle and the MCP server's package
    catalog read the same copy (DOCS-174).
    """
    mappings_file = edu_path / "data" / "package-mappings.yaml"
    if not mappings_file.exists():
        return None
    with open(mappings_file, "r", encoding="utf-8") as f:
        return f.read()


def compile_documentation(output_path=None):
    """Main function to compile all documentation"""
    # This script lives in <edu>/scripts/, locally and in CI alike.
    edu_path = Path(__file__).resolve().parent.parent

    # Initialize the compiled documentation
    compiled_md = []

    # Add header
    compiled_md.append("# Chainguard Documentation Bundle")
    compiled_md.append(
        f"\n_Compiled on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_\n"
    )
    compiled_md.append(
        "This document contains Chainguard documentation compiled from multiple sources.\n"
    )

    # Add Quick Start Guide for AI Tools
    quick_start_file = Path(__file__).parent / "quick-start-guide.md"
    if quick_start_file.exists():
        with open(quick_start_file, "r", encoding="utf-8") as f:
            quick_start_content = f.read()
        # Cleaned like every page, which strips the file's markdownlint
        # directive. The guide sits under the bundle's own H1, so it starts at
        # '##' and its lint config has to exempt it from first-line-h1.
        compiled_md.append(clean_markdown_content(quick_start_content))
    else:
        # Fallback if template file is missing
        compiled_md.append("## Usage Guide\n")
        compiled_md.append(
            "_Note: Usage guide template not found at scripts/quick-start-guide.md_\n"
        )
        compiled_md.append("---\n")

    # Add table of contents
    compiled_md.append("## Table of Contents\n")
    compiled_md.append("1. [Usage Guide](#usage-guide)")
    compiled_md.append("2. [Documentation Content](#documentation-content)\n")

    # Process edu content
    print("Processing documentation...")
    compiled_md.append("---\n")
    compiled_md.append("## Documentation Content\n")

    edu_docs = process_edu_content(edu_path)
    for doc in edu_docs:
        compiled_md.append(f"### {doc['title']}")
        compiled_md.append(f"_Path: {doc['path']}_\n")
        compiled_md.append(doc["content"])
        compiled_md.append("\n---\n")

    # Add the dfc mappings as one more page, in the same '### <title>' plus
    # '_Path:' form, so the MCP server indexes and links it like any other.
    dfc_mappings = read_dfc_mappings(edu_path)
    if dfc_mappings:
        compiled_md.append(f"### {DFC_SECTION_TITLE}")
        compiled_md.append(f"_Path: {DFC_SECTION_PATH}_\n")
        compiled_md.append(
            "Mappings from upstream images and packages to their Chainguard "
            "equivalents, used by the Dockerfile Converter (dfc).\n"
        )
        compiled_md.append("```yaml")
        compiled_md.append(dfc_mappings)
        compiled_md.append("```\n")
        print("DFC mappings added")
    else:
        # A missing source should not look like a healthy one (DOCS-174).
        print(
            "WARNING: data/package-mappings.yaml not found; "
            "the bundle has no DFC mappings"
        )

    # Save the compiled documentation
    if output_path:
        output_file = Path(output_path)
    else:
        output_file = edu_path / "static" / "downloads" / "chainguard-complete-docs.md"
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(compiled_md))

    print(f"Documentation compiled successfully to: {output_file}")
    return output_file


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Compile Chainguard documentation for AI assistants"
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Output file path (default: static/downloads/chainguard-complete-docs.md)",
    )
    args = parser.parse_args()

    compile_documentation(args.output)
