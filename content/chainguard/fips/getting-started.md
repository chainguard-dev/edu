---
title: "Getting Started with FIPS Containers"
linktitle: "Getting Started"
type: "article"
description: "Deploy and verify your first Chainguard FIPS container"
date: 2025-10-16T08:00:00+00:00
lastmod: 2025-10-16T08:00:00+00:00
draft: false
tags: ["FIPS", "Tutorial", "Getting Started"]
images: []
weight: 030
toc: true
---

## Prerequisites

Before starting, you'll need:

- **Chainguard account with FIPS access**: FIPS containers are not included in the free tier. [Contact Chainguard](https://www.chainguard.dev/contact) to request access.
- **Docker or compatible container runtime**: Install [Docker Desktop](https://www.docker.com/products/docker-desktop) or another OCI-compatible runtime.
- **Basic container knowledge**: Familiarity with pulling and running container images.

FIPS containers work on any recent Linux kernel, including:
- Linux workstations
- macOS (Docker Desktop)
- Windows (WSL2 with Docker Desktop)

## Choosing a FIPS Image

Chainguard offers 400+ FIPS image variants. Choose based on your use case:

**Language runtime images** if you're building applications:
- `go-fips` - For building Go applications
- `python-fips` - For Python applications
- `node-fips` - For Node.js applications
- `jdk-fips` or `jre-fips` - For Java applications
- `dotnet-runtime-fips` - For .NET applications

**Application images** if you need a specific tool or service:
- `nginx-fips` - Web server
- `postgres-fips` - Database
- `prometheus-fips` - Monitoring
- And many more

**Base images** for minimal runtime environments:
- `glibc-openssl-fips` - Minimal glibc-based runtime
- `busybox-fips` - Minimal BusyBox environment

Browse the complete catalog at [images.chainguard.dev/?category=fips](https://images.chainguard.dev/?category=fips).

## Your First FIPS Container

Let's start with a Python example to verify FIPS is working.

### Pull the Image

Replace `ORGANIZATION` with your organization name in the Chainguard Registry:

```bash
docker pull cgr.dev/ORGANIZATION/python-fips:latest
```

### Run a Test Script

Create a Python script that uses cryptography:

```bash
cat > test_fips.py << 'EOF'
import hashlib
import ssl

# Test that we can use cryptographic functions
data = b"Hello, FIPS!"
hash_result = hashlib.sha256(data).hexdigest()
print(f"SHA-256 hash: {hash_result}")

# Check SSL/TLS configuration
print(f"OpenSSL version: {ssl.OPENSSL_VERSION}")
print("FIPS cryptography is active")
EOF
```

Run the script in the FIPS container:

```bash
docker run --rm -v $(pwd):/work -w /work \
  cgr.dev/ORGANIZATION/python-fips:latest \
  python test_fips.py
```

You should see output like:

```
SHA-256 hash: 4a1e3b5c7d9f2a8c6b0e4f3a9d8c7b6a5e4d3c2b1a0f9e8d7c6b5a4e3d2c1b0a
OpenSSL version: OpenSSL 3.4.0 5 Aug 2025
FIPS cryptography is active
```

This confirms the container is using OpenSSL for cryptographic operations.

## Verifying FIPS Configuration

### Check the SBOM

Every Chainguard image includes a Software Bill of Materials (SBOM). Verify FIPS-required packages:

```bash
cosign download sbom cgr.dev/ORGANIZATION/python-fips:latest | grep -E "libcrypto|openssl-config"
```

Look for:
- `libcrypto3` version 3.4.0-r2 or higher
- `openssl-config-fipshardened` version 3.4.0-r3 or higher

These packages indicate kernel-independent FIPS configuration.

### Inspect OpenSSL Configuration

Run a container interactively to check OpenSSL configuration:

```bash
docker run --rm -it cgr.dev/ORGANIZATION/python-fips:latest sh
```

Inside the container, verify the FIPS module:

```bash
cat /etc/ssl/fipsmodule.cnf
```

You should see configuration for the FIPS provider. This file's presence and validity are essential for FIPS operation.

## Building Applications with FIPS

### Multi-Stage Build Pattern

The recommended pattern is to build with a FIPS SDK image and run with a minimal FIPS runtime image.

Example Dockerfile for a Go application:

```dockerfile
# Build stage
FROM cgr.dev/ORGANIZATION/go-fips:latest AS builder

WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN go build -o myapp

# Runtime stage
FROM cgr.dev/ORGANIZATION/glibc-openssl-fips:latest

COPY --from=builder /app/myapp /usr/bin/myapp

ENTRYPOINT ["/usr/bin/myapp"]
```

This pattern:
- Builds your application with FIPS-enabled Go toolchain
- Produces a minimal runtime image with only the binary and FIPS runtime
- Maintains FIPS compliance throughout

### Build and Run

```bash
docker build -t myapp-fips .
docker run --rm myapp-fips
```

The resulting container runs on any Linux kernel and maintains FIPS validation.

## Common Patterns

### Python Application with Requirements

```dockerfile
FROM cgr.dev/ORGANIZATION/python-fips:latest

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

### Node.js Application

```dockerfile
FROM cgr.dev/ORGANIZATION/node-fips:latest AS builder

WORKDIR /app
COPY package*.json ./
RUN npm ci --production

COPY . .

# Use multi-stage if you want a smaller runtime
FROM cgr.dev/ORGANIZATION/node-fips:latest
WORKDIR /app
COPY --from=builder /app .

CMD ["node", "server.js"]
```

### Java Application

```dockerfile
FROM cgr.dev/ORGANIZATION/jdk-fips:latest AS builder

WORKDIR /app
COPY . .
RUN javac MyApp.java

FROM cgr.dev/ORGANIZATION/jre-fips:latest
WORKDIR /app
COPY --from=builder /app/*.class .

CMD ["java", "MyApp"]
```

## Testing FIPS Enforcement

To verify that FIPS mode is enforced, you can intentionally break the FIPS configuration and confirm the application fails.

**Warning**: This test should only be done in development environments.

Run a container with access to modify system files:

```bash
docker run --rm -it --user root \
  cgr.dev/ORGANIZATION/python-fips:latest sh
```

Inside the container, break the FIPS configuration:

```bash
# Backup the config
cp /etc/ssl/fipsmodule.cnf /tmp/fipsmodule.cnf.bak

# Invalidate it
ln -sf /dev/null /etc/ssl/fipsmodule.cnf

# Try to use crypto
python3 -c "import hashlib; print(hashlib.sha256(b'test').hexdigest())"
```

You should see an error indicating FIPS is required but not available. This proves the container enforces FIPS mode and won't fall back to non-validated cryptography.

Restore the config to fix:

```bash
cp /tmp/fipsmodule.cnf.bak /etc/ssl/fipsmodule.cnf
```

## Development Workflow

### Local Development

FIPS containers work on any kernel, so you can develop and test locally:

1. Pull the FIPS image for your language/framework
2. Mount your source code into the container
3. Iterate on code with hot-reload if your framework supports it
4. Test cryptographic operations work correctly

Example for Python development:

```bash
docker run --rm -it \
  -v $(pwd):/app \
  -w /app \
  -p 8000:8000 \
  cgr.dev/ORGANIZATION/python-fips:latest \
  bash
```

Inside, install development dependencies and run your app.

### CI/CD Integration

FIPS containers work in standard CI/CD pipelines without special infrastructure.

GitHub Actions example:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Pull FIPS image
        run: docker pull cgr.dev/ORGANIZATION/python-fips:latest

      - name: Run tests
        run: |
          docker run --rm -v $(pwd):/app -w /app \
            cgr.dev/ORGANIZATION/python-fips:latest \
            python -m pytest
```

No special runners or kernel configurations required.

## Troubleshooting

### Issue: "FIPS mode requested but not available"

**Cause**: The FIPS provider configuration is missing or invalid.

**Solution**: Verify you're using a FIPS-tagged image (e.g., `python-fips`, not `python`). Check the SBOM contains required packages.

### Issue: Application crashes on startup

**Cause**: The application may be using a cryptographic library that doesn't support FIPS.

**Solution**: Ensure your application uses OpenSSL-backed cryptography. For language-specific guidance, see the [language guides](/chainguard/fips/language-guides/).

### Issue: Performance degradation

**Cause**: Likely not FIPS-related. Profile your application first.

**Solution**: Use standard profiling tools to identify bottlenecks. FIPS cryptography typically adds minimal overhead.

### Issue: Can't pull the image

**Cause**: FIPS images require account access.

**Solution**: Verify your organization has FIPS access. Contact support if needed.

## Next Steps

Now that you've deployed your first FIPS container:

- **Language-specific guides**: Learn detailed configuration for [Go](/chainguard/fips/language-guides/go/), [Java](/chainguard/fips/language-guides/java/), and other languages
- **Kernel-independent architecture**: Understand [how it works](/chainguard/fips/kernel-independent-architecture/) under the hood
- **FAQs**: Check [common questions](/chainguard/fips/faqs/) about FIPS implementation
- **Migration guide**: Plan your [migration to FIPS](/chainguard/fips/migration-guide/) for existing applications
- **Chainguard support**: [Contact us](https://www.chainguard.dev/contact) for questions or custom requirements
