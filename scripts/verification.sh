#!/bin/bash
# Chainguard AI Documentation Verification Script
# This script verifies the integrity and authenticity of the AI documentation bundle
# using cosign v3 bundle format (.bundle files)

set -euo pipefail

# Configuration
BUNDLE_NAME="chainguard-complete-docs.md"
EXPECTED_ISSUER="https://token.actions.githubusercontent.com"
EXPECTED_IDENTITY_PATTERN=".*github.com/chainguard-dev/edu.*"

echo "=== Chainguard AI Documentation Verification ==="
echo

# Function to print status
print_status() {
    local status=$1
    local message=$2
    case "$status" in
        "success")
            echo "[PASS] $message"
            ;;
        "error")
            echo "[FAIL] $message"
            ;;
        "warning")
            echo "[WARN] $message"
            ;;
        *)
            echo "[INFO] $message"
            ;;
    esac
}

# Check if cosign is installed
if ! command -v cosign &> /dev/null; then
    print_status "error" "cosign is not installed"
    echo "Please install cosign: https://docs.sigstore.dev/cosign/installation/"
    exit 1
fi
print_status "success" "cosign is installed"

# Check if required files exist
FILES_TO_CHECK=(
    "$BUNDLE_NAME"
    "${BUNDLE_NAME}.bundle"
    "checksums.txt"
    "checksums.txt.bundle"
)

for file in "${FILES_TO_CHECK[@]}"; do
    if [ ! -f "$file" ]; then
        print_status "error" "Missing file: $file"
        exit 1
    fi
done
print_status "success" "All required files present"

# Verify checksums
print_status "info" "Verifying checksums..."
if sha256sum -c checksums.txt > /dev/null 2>&1; then
    print_status "success" "Checksums verified"
else
    print_status "error" "Checksum verification failed"
    exit 1
fi

# Verify cosign signature on documentation bundle
print_status "info" "Verifying documentation signature..."
if cosign verify-blob \
    --bundle "${BUNDLE_NAME}.bundle" \
    --certificate-identity-regexp "$EXPECTED_IDENTITY_PATTERN" \
    --certificate-oidc-issuer "$EXPECTED_ISSUER" \
    "$BUNDLE_NAME" > /dev/null 2>&1; then
    print_status "success" "Documentation signature verified"
else
    print_status "error" "Documentation signature verification failed"
    exit 1
fi

# Verify cosign signature on checksums
print_status "info" "Verifying checksums signature..."
if cosign verify-blob \
    --bundle "checksums.txt.bundle" \
    --certificate-identity-regexp "$EXPECTED_IDENTITY_PATTERN" \
    --certificate-oidc-issuer "$EXPECTED_ISSUER" \
    checksums.txt > /dev/null 2>&1; then
    print_status "success" "Checksums signature verified"
else
    print_status "error" "Checksums signature verification failed"
    exit 1
fi

# Final summary
echo
echo "=== Verification Summary ==="
print_status "success" "All verifications passed"
print_status "success" "The documentation bundle is authentic and has not been tampered with"
echo
echo "You can now safely use: $BUNDLE_NAME"
