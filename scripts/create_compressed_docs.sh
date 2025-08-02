#!/bin/bash
# Create compressed versions of the documentation

cd /Users/ltagliaferri/Documents/GitHub/edu

# Run the Python script to compile docs
python3 scripts/compile_docs.py

# Create compressed versions
cd static/downloads

# Create gzip version
gzip -k chainguard-complete-docs.md

# Create zip version
zip chainguard-complete-docs.zip chainguard-complete-docs.md

# Create tar.gz version
tar -czf chainguard-complete-docs.tar.gz chainguard-complete-docs.md

# Show file sizes
echo "Documentation bundle created:"
ls -lh chainguard-complete-docs.*