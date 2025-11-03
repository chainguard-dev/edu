#!/bin/bash
# List files by contentType
# Usage: ./list-by-content-type.sh [contentType]
# Example: ./list-by-content-type.sh product-docs

CONTENT_TYPE="${1:-all}"

if [ "$CONTENT_TYPE" = "all" ]; then
    echo "=== All Content Types ==="
    echo ""
    for type in "product-docs" "tutorial" "how-to-guide" "integration" "conceptual"; do
        count=$(grep -r "contentType: \"$type\"" content --include="*.md" | wc -l | tr -d ' ')
        echo "$type: $count files"
    done
    echo ""
    echo "Usage: $0 [product-docs|tutorial|how-to-guide|integration|conceptual]"
else
    echo "=== Files tagged as: $CONTENT_TYPE ==="
    echo ""
    grep -r "contentType: \"$CONTENT_TYPE\"" content --include="*.md" -l | sort
    echo ""
    count=$(grep -r "contentType: \"$CONTENT_TYPE\"" content --include="*.md" | wc -l | tr -d ' ')
    echo "Total: $count files"
fi
