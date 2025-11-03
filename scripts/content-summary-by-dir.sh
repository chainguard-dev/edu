#!/bin/bash
# Show content type distribution by directory
# Usage: ./content-summary-by-dir.sh

echo "=== Content Type Distribution by Directory ==="
echo ""

for dir in content/chainguard content/open-source content/software-security content/compliance content/vulnerabilities content/contributors; do
    if [ -d "$dir" ]; then
        dirname=$(basename "$dir")
        echo "📁 $dirname"
        echo "   ├─ product-docs:  $(grep -r 'contentType: "product-docs"' "$dir" --include="*.md" 2>/dev/null | wc -l | tr -d ' ')"
        echo "   ├─ tutorial:      $(grep -r 'contentType: "tutorial"' "$dir" --include="*.md" 2>/dev/null | wc -l | tr -d ' ')"
        echo "   ├─ how-to-guide:  $(grep -r 'contentType: "how-to-guide"' "$dir" --include="*.md" 2>/dev/null | wc -l | tr -d ' ')"
        echo "   ├─ integration:   $(grep -r 'contentType: "integration"' "$dir" --include="*.md" 2>/dev/null | wc -l | tr -d ' ')"
        echo "   └─ conceptual:    $(grep -r 'contentType: "conceptual"' "$dir" --include="*.md" 2>/dev/null | wc -l | tr -d ' ')"
        echo ""
    fi
done

echo "=== Chainguard Subdirectories ==="
echo ""
for subdir in content/chainguard/*/; do
    if [ -d "$subdir" ]; then
        subdirname=$(basename "$subdir")
        total=$(find "$subdir" -name "*.md" -type f | wc -l | tr -d ' ')
        if [ "$total" -gt 0 ]; then
            echo "📂 chainguard/$subdirname ($total files)"
        fi
    fi
done
