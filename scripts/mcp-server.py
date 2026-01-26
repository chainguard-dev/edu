#!/usr/bin/env python3
"""
Chainguard AI Documentation MCP Server

A Model Context Protocol server that provides AI assistants with searchable
access to Chainguard documentation including container images, security info,
and tooling guides.
"""

import json
import logging
import os
import re
from typing import Any, Dict, List, Optional

# MCP SDK imports
try:
    from mcp.server import Server
    from mcp.types import (
        Tool,
        TextContent,
        ImageContent,
        EmbeddedResource,
    )
    import mcp.server.stdio
except ImportError:
    import sys
    print("Error: MCP SDK not installed. Install with: pip install mcp", file=sys.stderr)
    sys.exit(1)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("chainguard-ai-docs-mcp")

# Documentation file path
DOCS_PATH = os.getenv("DOCS_PATH", "/docs/chainguard-ai-docs.md")


class ChaguardDocsIndex:
    """Index of Chainguard documentation sections for efficient retrieval."""

    def __init__(self, docs_content: str):
        self.content = docs_content
        self.sections = self._parse_sections()
        self.images = self._extract_images()

    def _parse_sections(self) -> Dict[str, str]:
        """Parse markdown into logical sections."""
        sections = {}
        current_section = None
        current_content = []

        for line in self.content.split('\n'):
            # Top-level headers indicate new sections
            if line.startswith('# '):
                if current_section:
                    sections[current_section] = '\n'.join(current_content)
                current_section = line[2:].strip()
                current_content = [line]
            elif current_content:
                current_content.append(line)

        # Add last section
        if current_section:
            sections[current_section] = '\n'.join(current_content)

        # Also parse individual container images as separate sections
        # Find the Container Images section and extract individual image docs
        container_images_match = re.search(r'^## Container Images\n', self.content, re.MULTILINE)
        if container_images_match:
            start_pos = container_images_match.end()
            section_content = self.content[start_pos:]

            # Use regex to find all image sections (### header followed by content until next separator or end)
            # Pattern: ### image-name followed by content until <!-- IMAGE_SEPARATOR --> or end of string
            image_pattern = r'### ([a-z0-9\-]+)\n(.*?)(?=\n<!-- IMAGE_SEPARATOR -->|\Z)'
            for match in re.finditer(image_pattern, section_content, re.DOTALL):
                image_name = match.group(1)
                image_content = f'### {image_name}\n{match.group(2).strip()}'
                sections[f'image:{image_name}'] = image_content

        return sections

    def _extract_images(self) -> List[str]:
        """Extract list of container image names from docs."""
        images = set()

        # Find the "## Container Images" section and extract all ### headers with simple names
        container_images_match = re.search(r'^## Container Images\n', self.content, re.MULTILINE)

        if container_images_match:
            # Start from the Container Images section
            start_pos = container_images_match.end()
            # Get content from Container Images section to the end
            section_content = self.content[start_pos:]

            # Extract all ### headers that match image name pattern
            # Image names are simple: lowercase letters, numbers, and hyphens
            image_pattern = r'\n### ([a-z0-9\-]+)\n'
            for match in re.finditer(image_pattern, section_content):
                images.add(match.group(1))

        # Fallback: also look for cgr.dev references if no images found from headers
        if not images:
            pattern = r'cgr\.dev/chainguard/([a-z0-9\-]+)'
            for match in re.finditer(pattern, self.content):
                images.add(match.group(1))

        return sorted(list(images))

    def search(self, query: str, max_results: int = 5) -> List[Dict[str, str]]:
        """Search documentation for relevant content."""
        query_lower = query.lower()
        results = []

        for section_name, section_content in self.sections.items():
            # Simple relevance scoring based on query term frequency
            content_lower = section_content.lower()
            score = content_lower.count(query_lower)

            if score > 0:
                # Extract a relevant snippet
                lines = section_content.split('\n')
                snippet_lines = []
                for line in lines[:50]:  # First 50 lines of section
                    if query_lower in line.lower():
                        snippet_lines.append(line)
                        if len(snippet_lines) >= 5:
                            break

                results.append({
                    'section': section_name,
                    'score': score,
                    'snippet': '\n'.join(snippet_lines[:5]),
                    'full_content': section_content[:2000]  # First 2000 chars
                })

        # Sort by relevance and return top results
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:max_results]

    def get_image_docs(self, image_name: str) -> Optional[str]:
        """Get documentation for a specific container image."""
        # First, try to find the image-specific section (with image: prefix)
        image_key = f'image:{image_name}'
        if image_key in self.sections:
            return self.sections[image_key]

        # Fallback: try without exact match (case-insensitive)
        for section_name, section_content in self.sections.items():
            if section_name.startswith('image:') and image_name.lower() in section_name.lower():
                return section_content

        # Last resort: search for any mention
        results = self.search(image_name, max_results=1)
        if results:
            return results[0]['full_content']

        return None

    def get_security_content(self) -> str:
        """Get security and CVE related content."""
        security_terms = ['security', 'cve', 'vulnerability', 'sbom', 'signature']
        relevant_sections = []

        for section_name, section_content in self.sections.items():
            if any(term in section_name.lower() for term in security_terms):
                relevant_sections.append(f"# {section_name}\n\n{section_content}")

        if relevant_sections:
            return '\n\n---\n\n'.join(relevant_sections)

        return "No specific security documentation found."

    def get_tool_docs(self, tool_name: str) -> Optional[str]:
        """Get documentation for Chainguard tools (wolfi, apko, melange, chainctl)."""
        tool_lower = tool_name.lower()

        for section_name, section_content in self.sections.items():
            if tool_lower in section_name.lower():
                return section_content

        # Fallback to search
        results = self.search(tool_name, max_results=1)
        if results:
            return results[0]['full_content']

        return None


# Initialize MCP server
app = Server("chainguard-ai-docs")

# Load and index documentation
logger.info(f"Loading documentation from {DOCS_PATH}")
try:
    with open(DOCS_PATH, 'r') as f:
        docs_content = f.read()
    docs_index = ChaguardDocsIndex(docs_content)
    logger.info(f"Indexed {len(docs_index.sections)} documentation sections")
    logger.info(f"Found {len(docs_index.images)} container images")
except Exception as e:
    logger.error(f"Failed to load documentation: {e}")
    docs_index = None


@app.list_tools()
async def list_tools() -> List[Tool]:
    """List available MCP tools."""
    return [
        Tool(
            name="search_docs",
            description="Search across all Chainguard documentation for relevant content",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query (e.g., 'python image security', 'CVE management')"
                    },
                    "max_results": {
                        "type": "integer",
                        "description": "Maximum number of results to return (default: 5)",
                        "default": 5
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="get_image_docs",
            description="Get documentation for a specific Chainguard container image",
            inputSchema={
                "type": "object",
                "properties": {
                    "image_name": {
                        "type": "string",
                        "description": "Image name (e.g., 'python', 'node', 'nginx')"
                    }
                },
                "required": ["image_name"]
            }
        ),
        Tool(
            name="list_images",
            description="List all available Chainguard container images",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="get_security_docs",
            description="Get security-related documentation including CVE management and SBOMs",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="get_tool_docs",
            description="Get documentation for Chainguard tools (wolfi, apko, melange, chainctl)",
            inputSchema={
                "type": "object",
                "properties": {
                    "tool_name": {
                        "type": "string",
                        "description": "Tool name: wolfi, apko, melange, or chainctl"
                    }
                },
                "required": ["tool_name"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> List[TextContent]:
    """Handle tool calls."""

    if docs_index is None:
        return [TextContent(
            type="text",
            text="Error: Documentation not loaded. Please check server logs."
        )]

    try:
        if name == "search_docs":
            query = arguments.get("query", "")
            max_results = arguments.get("max_results", 5)

            results = docs_index.search(query, max_results)

            if not results:
                return [TextContent(
                    type="text",
                    text=f"No results found for query: {query}"
                )]

            response = f"# Search Results for: {query}\n\n"
            for i, result in enumerate(results, 1):
                response += f"## Result {i}: {result['section']}\n\n"
                response += f"{result['snippet']}\n\n"
                response += "---\n\n"

            return [TextContent(type="text", text=response)]

        elif name == "get_image_docs":
            image_name = arguments.get("image_name", "")
            docs = docs_index.get_image_docs(image_name)

            if docs:
                return [TextContent(
                    type="text",
                    text=f"# Documentation for {image_name}\n\n{docs}"
                )]
            else:
                return [TextContent(
                    type="text",
                    text=f"No documentation found for image: {image_name}"
                )]

        elif name == "list_images":
            images_list = "\n".join([f"- {img}" for img in docs_index.images])
            return [TextContent(
                type="text",
                text=f"# Available Chainguard Container Images\n\n{images_list}"
            )]

        elif name == "get_security_docs":
            security_docs = docs_index.get_security_content()
            return [TextContent(type="text", text=security_docs)]

        elif name == "get_tool_docs":
            tool_name = arguments.get("tool_name", "")
            docs = docs_index.get_tool_docs(tool_name)

            if docs:
                return [TextContent(
                    type="text",
                    text=f"# {tool_name.title()} Documentation\n\n{docs}"
                )]
            else:
                return [TextContent(
                    type="text",
                    text=f"No documentation found for tool: {tool_name}"
                )]

        else:
            return [TextContent(
                type="text",
                text=f"Unknown tool: {name}"
            )]

    except Exception as e:
        logger.error(f"Error handling tool call {name}: {e}")
        return [TextContent(
            type="text",
            text=f"Error: {str(e)}"
        )]


async def main():
    """Run the MCP server."""
    logger.info("Starting Chainguard AI Docs MCP Server")

    # Run with stdio transport (for Claude Desktop, etc.)
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
