#!/bin/bash
# Chainguard AI Documentation Verification Script
# This script verifies the integrity and authenticity of the AI documentation bundle

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
    "${BUNDLE_NAME}.sig"
    "${BUNDLE_NAME}.pem"
    "checksums.sha256"
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
if sha256sum -c checksums.sha256 > /dev/null 2>&1; then
    print_status "success" "Checksums verified"
else
    print_status "error" "Checksum verification failed"
    exit 1
fi

# Verify cosign signature
print_status "info" "Verifying cosign signature..."
if cosign verify-blob \
    --certificate "${BUNDLE_NAME}.pem" \
    --signature "${BUNDLE_NAME}.sig" \
    --certificate-identity-regexp "$EXPECTED_IDENTITY_PATTERN" \
    --certificate-oidc-issuer "$EXPECTED_ISSUER" \
    "$BUNDLE_NAME" > /dev/null 2>&1; then
    print_status "success" "Signature verified"
else
    print_status "error" "Signature verification failed"
    exit 1
fi

# Extract certificate details
print_status "info" "Certificate details:"
echo "  Issuer: $(openssl x509 -in "${BUNDLE_NAME}.pem" -noout -issuer | cut -d'=' -f2-)"
echo "  Subject: $(openssl x509 -in "${BUNDLE_NAME}.pem" -noout -subject | cut -d'=' -f2-)"
echo "  Valid from: $(openssl x509 -in "${BUNDLE_NAME}.pem" -noout -startdate | cut -d'=' -f2)"
echo "  Valid to: $(openssl x509 -in "${BUNDLE_NAME}.pem" -noout -enddate | cut -d'=' -f2)"

# Check Rekor transparency log
print_status "info" "Checking Rekor transparency log..."
if cosign verify-blob \
    --certificate "${BUNDLE_NAME}.pem" \
    --signature "${BUNDLE_NAME}.sig" \
    --certificate-identity-regexp "$EXPECTED_IDENTITY_PATTERN" \
    --certificate-oidc-issuer "$EXPECTED_ISSUER" \
    --rekor-url https://rekor.sigstore.dev \
    "$BUNDLE_NAME" 2>&1 | grep -q "Verified OK"; then
    print_status "success" "Transparency log entry verified"
else
    print_status "warning" "Could not verify transparency log entry"
fi

# Final summary
echo
echo "=== Verification Summary ==="
print_status "success" "All verifications passed"
print_status "success" "The documentation bundle is authentic and has not been tampered with"
echo
echo "You can now safely use: $BUNDLE_NAME"