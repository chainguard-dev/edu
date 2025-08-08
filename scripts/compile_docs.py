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
        if tag == 'p':
            if self.current_text:
                self.markdown.append(''.join(self.current_text))
            self.current_text = []
        elif tag == 'h1':
            self.current_text = ['# ']
        elif tag == 'h2':
            self.current_text = ['## ']
        elif tag == 'h3':
            self.current_text = ['### ']
        elif tag == 'h4':
            self.current_text = ['#### ']
        elif tag == 'strong' or tag == 'b':
            self.current_text.append('**')
        elif tag == 'em' or tag == 'i':
            self.current_text.append('*')
        elif tag == 'code':
            self.in_code = True
            self.current_text.append('`')
        elif tag == 'pre':
            self.in_pre = True
            self.current_text.append('\n```\n')
        elif tag == 'ul':
            self.list_stack.append('ul')
        elif tag == 'ol':
            self.list_stack.append('ol')
        elif tag == 'li':
            indent = '  ' * (len(self.list_stack) - 1)
            if self.list_stack and self.list_stack[-1] == 'ul':
                self.current_text.append(f'\n{indent}- ')
            elif self.list_stack and self.list_stack[-1] == 'ol':
                self.current_text.append(f'\n{indent}1. ')
        elif tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.current_text.append('[')
                    self._link_url = attr[1]
        elif tag == 'br':
            self.current_text.append('\n')
        elif tag == 'table':
            self.current_text.append('\n')
        elif tag == 'tr':
            self.current_text.append('\n|')
        elif tag == 'td' or tag == 'th':
            self.current_text.append(' ')
            
    def handle_endtag(self, tag):
        if tag in ['p', 'h1', 'h2', 'h3', 'h4']:
            self.markdown.append(''.join(self.current_text))
            self.markdown.append('\n')
            self.current_text = []
        elif tag == 'strong' or tag == 'b':
            self.current_text.append('**')
        elif tag == 'em' or tag == 'i':
            self.current_text.append('*')
        elif tag == 'code':
            self.in_code = False
            self.current_text.append('`')
        elif tag == 'pre':
            self.in_pre = False
            self.current_text.append('\n```\n')
        elif tag == 'ul' or tag == 'ol':
            if self.list_stack:
                self.list_stack.pop()
        elif tag == 'a':
            self.current_text.append(f']({self._link_url})')
        elif tag == 'tr':
            self.current_text.append(' |')
        elif tag == 'td' or tag == 'th':
            self.current_text.append(' |')
            
    def handle_data(self, data):
        if self.in_pre:
            self.current_text.append(data)
        else:
            self.current_text.append(data.strip())
            
    def get_markdown(self):
        if self.current_text:
            self.markdown.append(''.join(self.current_text))
        return '\n'.join(self.markdown)


def clean_markdown_content(content):
    """Remove HTML comments and clean up markdown content"""
    if not content:
        return content
    
    # Remove HTML comments like <!--monopod:start-->, <!--overview:end-->, etc.
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    
    # Replace example secrets with sanitized versions to avoid GitHub alerts
    # This preserves the documentation structure while removing false positive alerts
    content = re.sub(r'tskey-client-[^\s\'"]+', 'tskey-client-EXAMPLE_KEY_REPLACED', content)
    
    # Remove multiple consecutive blank lines
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    
    # Strip leading/trailing whitespace
    content = content.strip()
    
    return content


def read_markdown_file(filepath):
    """Read a markdown file and extract frontmatter and content"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract frontmatter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter = parts[1].strip()
                main_content = parts[2].strip()
                
                # Parse title from frontmatter
                title_match = re.search(r'title\s*:\s*"([^"]+)"', frontmatter)
                title = title_match.group(1) if title_match else None
                
                # Clean the content
                main_content = clean_markdown_content(main_content)
                
                return {
                    'title': title,
                    'frontmatter': frontmatter,
                    'content': main_content
                }
        
        # Clean content even if no frontmatter
        content = clean_markdown_content(content)
        
        return {
            'title': None,
            'frontmatter': None,
            'content': content
        }
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
    content_path = edu_path / 'content'
    docs = []
    
    for root, dirs, files in os.walk(content_path):
        for file in files:
            if file.endswith('.md'):
                filepath = Path(root) / file
                doc = read_markdown_file(filepath)
                if doc and doc['content']:
                    relative_path = filepath.relative_to(content_path)
                    # Ensure content is cleaned
                    cleaned_content = clean_markdown_content(doc['content'])
                    if cleaned_content:  # Only add if content remains after cleaning
                        docs.append({
                            'path': str(relative_path),
                            'title': doc['title'] or file.replace('.md', ''),
                            'content': cleaned_content
                        })
    
    return docs


def process_courses(courses_path):
    """Process course content from the courses repository"""
    courses = []
    
    for course_dir in courses_path.iterdir():
        if course_dir.is_dir() and not course_dir.name.startswith('.'):
            # Read course details
            details_file = course_dir / 'details.json'
            if details_file.exists():
                with open(details_file, 'r') as f:
                    details = json.load(f)
                    course_name = details.get('title', course_dir.name)
            else:
                course_name = course_dir.name.replace('-', ' ')
            
            # Process lessons
            lessons_dir = course_dir / 'lessons'
            if lessons_dir.exists():
                lessons = []
                for lesson_dir in sorted(lessons_dir.iterdir()):
                    if lesson_dir.is_dir():
                        # Find HTML content file
                        for html_file in lesson_dir.glob('content-*.html'):
                            with open(html_file, 'r', encoding='utf-8') as f:
                                html_content = f.read()
                            
                            # Convert HTML to Markdown
                            markdown_content = convert_html_to_markdown(html_content)
                            
                            # Extract lesson name from directory
                            lesson_name = lesson_dir.name.split('-', 1)[1].replace('-', ' ')
                            
                            lessons.append({
                                'name': lesson_name,
                                'content': markdown_content
                            })
                
                if lessons:
                    courses.append({
                        'name': course_name,
                        'lessons': lessons
                    })
    
    return courses


def process_images_readmes(images_path):
    """Process README files from images-private repository"""
    readmes = []
    images_dir = images_path / 'images'
    
    if images_dir.exists():
        for image_dir in images_dir.iterdir():
            if image_dir.is_dir() and not image_dir.name.startswith('.'):
                readme_file = image_dir / 'README.md'
                if readme_file.exists():
                    doc = read_markdown_file(readme_file)
                    if doc and doc['content']:
                        readmes.append({
                            'name': image_dir.name,
                            'content': doc['content']
                        })
    
    return readmes


def compile_documentation(output_path=None):
    """Main function to compile all documentation"""
    # Define paths - support both local and CI environments
    if os.environ.get('GITHUB_ACTIONS'):
        # GitHub Actions environment
        base_path = Path('.')
        edu_path = base_path / 'edu'
        courses_path = base_path / 'courses'
        images_path = base_path / 'images-private'
    else:
        # Local development environment
        current_dir = Path(__file__).parent.parent
        if current_dir.name == 'edu':
            edu_path = current_dir
            base_path = edu_path.parent
            courses_path = base_path / 'courses'
            images_path = base_path / 'images-private'
        else:
            # Fallback to absolute path
            base_path = Path('/Users/ltagliaferri/Documents/GitHub')
            edu_path = base_path / 'edu'
            courses_path = base_path / 'courses'
            images_path = base_path / 'images-private'
    
    # Initialize the compiled documentation
    compiled_md = []
    
    # Add header
    compiled_md.append("# Chainguard Documentation Bundle")
    compiled_md.append(f"\n_Compiled on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_\n")
    compiled_md.append("This document contains Chainguard documentation compiled from multiple sources.\n")
    
    # Add Quick Start Guide for AI Tools
    quick_start_file = Path(__file__).parent / 'quick-start-guide.md'
    if quick_start_file.exists():
        with open(quick_start_file, 'r', encoding='utf-8') as f:
            quick_start_content = f.read()
        compiled_md.append(quick_start_content)
    else:
        # Fallback if template file is missing
        compiled_md.append("## Usage Guide\n")
        compiled_md.append("_Note: Usage guide template not found at scripts/quick-start-guide.md_\n")
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
        compiled_md.append(doc['content'])
        compiled_md.append("\n---\n")
    
    # Process courses
    if courses_path.exists():
        print("Processing additional content...")
        courses = process_courses(courses_path)
        for course in courses:
            compiled_md.append(f"### {course['name']}\n")
            for i, lesson in enumerate(course['lessons'], 1):
                compiled_md.append(f"#### {lesson['name']}\n")
                compiled_md.append(lesson['content'])
                compiled_md.append("\n")
    
    # Process image READMEs
    if images_path.exists():
        print("Processing additional documentation...")
        image_readmes = process_images_readmes(images_path)
        for readme in image_readmes:
            compiled_md.append(f"### {readme['name']}\n")
            compiled_md.append(readme['content'])
            compiled_md.append("\n---\n")
    
    # Save the compiled documentation
    if output_path:
        output_file = Path(output_path)
    else:
        output_file = edu_path / 'static' / 'downloads' / 'chainguard-complete-docs.md'
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(compiled_md))
    
    print(f"Documentation compiled successfully to: {output_file}")
    return output_file


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Compile Chainguard documentation for AI assistants')
    parser.add_argument('--output', type=str, help='Output file path (default: static/downloads/chainguard-complete-docs.md)')
    args = parser.parse_args()
    
    compile_documentation(args.output)