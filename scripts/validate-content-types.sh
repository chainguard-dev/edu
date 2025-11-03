#!/bin/bash
# Validate that all markdown files have a contentType tag
# Exit code 0 = all valid, 1 = some files missing contentType

EXIT_CODE=0
MISSING_COUNT=0

echo "🔍 Validating contentType tags..."
echo ""

# Find all markdown files without contentType
while IFS= read -r file; do
    if ! grep -q "^contentType:" "$file"; then
        if [ $MISSING_COUNT -eq 0 ]; then
            echo "❌ Files missing contentType tag:"
            echo ""
        fi
        echo "   $file"
        MISSING_COUNT=$((MISSING_COUNT + 1))
        EXIT_CODE=1
    fi
done < <(find content -name "*.md" -type f)

if [ $EXIT_CODE -eq 0 ]; then
    TOTAL=$(find content -name "*.md" -type f | wc -l | tr -d ' ')
    echo "✅ All $TOTAL markdown files have contentType tags!"
else
    TOTAL=$(find content -name "*.md" -type f | wc -l | tr -d ' ')
    TAGGED=$((TOTAL - MISSING_COUNT))
    echo ""
    echo "📊 Summary: $TAGGED/$TOTAL files tagged ($MISSING_COUNT missing)"
    echo ""
    echo "Valid contentType values:"
    echo "  - product-docs"
    echo "  - tutorial"
    echo "  - how-to-guide"
    echo "  - integration"
    echo "  - conceptual"
fi

exit $EXIT_CODE
