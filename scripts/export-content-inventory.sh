#!/bin/bash
# Export content inventory to CSV
# Usage: ./export-content-inventory.sh > content-inventory.csv

echo "File Path,Content Type,Title,Last Modified"

find content -name "*.md" -type f | while read -r file; do
    # Extract contentType
    content_type=$(grep -m 1 "^contentType:" "$file" | sed 's/contentType: "\(.*\)"/\1/' | tr -d '\n')

    # Extract title
    title=$(grep -m 1 "^title:" "$file" | sed 's/title: "\(.*\)"/\1/' | sed 's/title: \(.*\)/\1/' | tr -d '\n')

    # Get last modified date
    if [[ "$OSTYPE" == "darwin"* ]]; then
        last_modified=$(stat -f "%Sm" -t "%Y-%m-%d" "$file")
    else
        last_modified=$(stat -c "%y" "$file" | cut -d' ' -f1)
    fi

    # Only output if contentType exists
    if [ -n "$content_type" ]; then
        echo "\"$file\",\"$content_type\",\"$title\",\"$last_modified\""
    fi
done | sort -t',' -k2,2 -k1,1
