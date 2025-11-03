---
title: "Getting Started with the MinIO Chainguard Container"
type: "article"
linktitle: "MinIO"
description: "Learn how to deploy MinIO object storage with Chainguard's secure, minimal container images for S3-compatible storage solutions with reduced vulnerabilities"
date: 2025-10-27T11:07:52+02:00
lastmod: 2025-10-27T11:07:52+02:00
tags: ["Chainguard Containers"]
draft: false
images: []
menu:
  docs:
    parent: "getting-started"
weight: 065
toc: true
contentType: "tutorial"
---

MinIO is a high-performance, S3-compatible object storage system that has become widely adopted across the cloud-native ecosystem, with over 1 billion pulls on Docker Hub. It's used for testing, local development, and production deployments across on-premises and cloud environments. MinIO's solid S3 compatibility has made it a common choice for developers who need S3-compatible storage without AWS dependencies, and it's integrated into popular open source projects like Trino and Apache Spark for backup and archival, AI/ML workloads, data lakes, and application data storage.

On October 23, 2025, the MinIO project stopped publishing the free, community edition of their Docker container image to Docker Hub and Quay repositories, requiring developers to build and maintain their own containers from source code. This change has impacted countless build pipelines and CI/CD workflows. Additionally, a new vulnerability, [CVE-2025-62506](https://www.cve.org/CVERecord?id=CVE-2025-62506), was reported in MinIO containers, which the maintainers declined to patch in the community edition.

To help the community maintain secure and up-to-date MinIO deployments without additional complexity, Chainguard has made our [MinIO container image](https://images.chainguard.dev/directory/image/minio/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-chainguard-images-getting-started-minio) publicly available and free to all users. Built with a distroless design and minimal attack surface, Chainguard's production-ready MinIO image is continuously rebuilt from source in our SLSA L3 hardened infrastructure, providing zero-CVE images that are updated daily with new releases and security fixes.

In this guide, we'll demonstrate how to deploy and use MinIO with Chainguard Containers through two practical examples. These examples show you how to replace existing MinIO deployments with Chainguard's more secure alternative while maintaining compatibility with your existing S3 workflows. The first example covers basic deployment for testing and development environments. The second example demonstrates how to build applications that interact with MinIO programmatically, which is relevant for CI/CD pipelines, automated backup systems, data processing workflows, and any application that requires object storage capabilities.

{{< details "What is distroless" >}}
{{< blurb/distroless >}}
{{< /details >}}

{{< details "What is Wolfi" >}}
{{< blurb/wolfi >}}
{{< /details >}}

{{< details "Chainguard Images" >}}
{{< blurb/images >}}
{{< /details >}}

## Preparation
This tutorial requires Docker to be installed on your local machine. If you don't have Docker installed, you can download and install it from the [official Docker website](https://docs.docker.com/get-docker/).

### Cloning the Demos Repository
Start by cloning the demos repository to your local machine:

```shell
git clone https://github.com/chainguard-dev/edu-images-demos.git
```

Navigate to the `minio` folder in the repository:

```shell
cd edu-images-demos/minio
```

This directory contains Docker Compose configurations and a sample Python application that we'll use in this guide.

## Example 1: Running MinIO with Docker Compose

This example demonstrates how to deploy MinIO for local development and testing environments. This setup is useful when you need S3-compatible storage for developing applications locally, running integration tests, or testing data pipelines before deploying to production. By using Docker Compose, you can spin up a complete object storage environment that mimics production S3 behavior without requiring cloud resources or complex configuration.

The MinIO Chainguard Container can be used directly without requiring a custom Dockerfile. The image comes pre-configured and ready to run with minimal setup.

For reference, here is the relevant section from the `docker-compose.yml` file:

```yaml
services:
  minio:
    image: cgr.dev/chainguard/minio:latest
    container_name: minio-server
    ports:
      - "9000:9000"
      - "9001:9001"
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin123
    command: server /data --console-address ":9001"
    volumes:
      - minio-data:/data
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9000/minio/health/live"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s
    networks:
      - minio-net

volumes:
  minio-data:
    driver: local

networks:
  minio-net:
    driver: bridge
```

This configuration will:

1. Pull the `cgr.dev/chainguard/minio:latest` image directly from the Chainguard registry;
2. Expose port 9000 for the MinIO API and port 9001 for the web console;
3. Set up admin credentials using environment variables;
4. Configure MinIO to serve data from the `/data` directory with the console on port 9001;
5. Create a persistent volume to store MinIO data;
6. Include a health check to monitor the server status.

To start the MinIO server, run:

```shell
docker compose up -d minio
```

Once the service is running, you can access:
- **MinIO API**: http://localhost:9000
- **MinIO Console**: http://localhost:9001

Open your web browser and navigate to http://localhost:9001. Log in using the credentials defined in the compose file:
- **Username**: `minioadmin`
- **Password**: `minioadmin123`

The MinIO console provides a graphical interface where you can create buckets, upload files, and manage your object storage. You can also interact with MinIO programmatically using the S3 API, which we'll demonstrate in the next example.

To stop the MinIO server, run:

```shell
docker compose down
```

Note that the data will persist in the `minio-data` volume even after stopping the container. To remove the volume and all stored data, add the `-v` flag:

```shell
docker compose down -v
```

## Example 2: Building a Python Client Application with Multi-Stage Build

This example demonstrates how to build containerized applications that interact with MinIO programmatically using the S3 API. This pattern is common in production systems for automated workflows such as CI/CD pipelines that upload build artifacts, data processing jobs that read and write large datasets, backup systems that archive files to object storage, or microservices that store and retrieve user-generated content.

The example uses a multi-stage Docker build with Chainguard Python images, which reduces the final container size and attack surface by separating build dependencies from runtime requirements. This approach is recommended for production deployments where security and efficiency are priorities.

The demo includes a Python script that performs the following operations:
- Connecting to the MinIO server with retry logic
- Creating buckets
- Uploading objects (files and data)
- Listing objects in a bucket
- Downloading objects
- Deleting objects

### Step 1: Understanding the Application Structure

The application consists of three main files:

1. **requirements.txt** - Python dependencies:
   ```
   minio==7.2.8
   urllib3==2.2.3
   ```

2. **main.py** - The Python application demonstrating MinIO operations
3. **Dockerfile** - Multi-stage build configuration

Let's examine the key parts of the Python application. The script uses the MinIO Python SDK to interact with the object storage server:

```python
from minio import Minio
from minio.error import S3Error

def get_minio_client():
    """Create and return a MinIO client instance"""
    endpoint = os.getenv("MINIO_ENDPOINT", "localhost:9000")
    access_key = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
    secret_key = os.getenv("MINIO_SECRET_KEY", "minioadmin123")
    secure = os.getenv("MINIO_SECURE", "false").lower() == "true"

    return Minio(
        endpoint,
        access_key=access_key,
        secret_key=secret_key,
        secure=secure
    )
```

The application includes functions for common operations like creating buckets, uploading objects, and listing contents. It demonstrates best practices such as connection retry logic and proper error handling.

### Step 2: Understanding the Multi-Stage Dockerfile

The `Dockerfile` uses a multi-stage build to keep the final image minimal and secure:

```Dockerfile
# Multi-stage build using Chainguard images
# Stage 1: Build stage with Python dev image to install dependencies
FROM cgr.dev/chainguard/python:latest-dev as builder

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime stage with minimal Python image
FROM cgr.dev/chainguard/python:latest

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /home/nonroot/.local/lib/python3.*/site-packages /home/nonroot/.local/lib/python3.13/site-packages

# Copy application code
COPY main.py .

# Run as non-root user (already set in base image)
USER nonroot

# Set Python path to include user-installed packages
ENV PYTHONPATH=/home/nonroot/.local/lib/python3.13/site-packages

CMD ["main.py"]
```

This Dockerfile will:

1. Start a build stage based on the `python:latest-dev` container image with build tools and pip;
2. Install the MinIO Python SDK and its dependencies;
3. Start a new runtime stage based on the minimal `python:latest` distroless image;
4. Copy only the installed packages and application code from the builder stage;
5. Run as a non-root user for enhanced security;
6. Set the application as the container's entry point.

### Step 3: Running the Complete Example

The `docker-compose.yml` file includes both the MinIO server and the Python application:

```yaml
services:
  minio:
    image: cgr.dev/chainguard/minio:latest
    container_name: minio-server
    ports:
      - "9000:9000"
      - "9001:9001"
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin123
    command: server /data --console-address ":9001"
    volumes:
      - minio-data:/data
    networks:
      - minio-net

  app:
    build:
      context: ./app
      dockerfile: Dockerfile
    container_name: minio-app
    depends_on:
      - minio
    environment:
      MINIO_ENDPOINT: minio:9000
      MINIO_ACCESS_KEY: minioadmin
      MINIO_SECRET_KEY: minioadmin123
      MINIO_SECURE: "false"
    networks:
      - minio-net
```

First, ensure the MinIO server is running:

```shell
docker compose up -d minio
```

Wait a few seconds for MinIO to fully start, then build and run the Python application:

```shell
docker compose up app
```

You should see output similar to this:

```
============================================================
MinIO Sample Application with Chainguard Container
============================================================

Waiting for MinIO server to be ready...
MinIO server is ready!

1. Creating bucket 'demo-bucket'...
✓ Created bucket: demo-bucket

2. Listing all buckets...
  - demo-bucket (created: 2025-10-27 14:23:45.123456+00:00)

3. Uploading sample objects...
✓ Uploaded object: hello.txt to bucket: demo-bucket
✓ Uploaded object: data.json to bucket: demo-bucket
✓ Uploaded object: info.txt to bucket: demo-bucket

4. Listing objects in bucket 'demo-bucket'...
  - hello.txt (size: 18 bytes)
  - data.json (size: 62 bytes)
  - info.txt (size: 53 bytes)

5. Downloading and displaying 'hello.txt'...
✓ Downloaded object: hello.txt from bucket: demo-bucket
   Content: Hello from MinIO!

6. Deleting 'info.txt'...
✓ Deleted object: info.txt from bucket: demo-bucket

7. Listing objects in bucket 'demo-bucket' after deletion...
  - hello.txt (size: 18 bytes)
  - data.json (size: 62 bytes)

============================================================
Demo completed successfully!
============================================================
```

The application demonstrates a complete workflow for working with MinIO object storage. You can also view the created bucket and uploaded objects through the MinIO console at http://localhost:9001.

To stop all services, run:

```shell
docker compose down
```

### Step 4: Extending the Application for Your Use Case

This demo application provides a foundation for building production object storage workflows. You can extend it to meet specific requirements such as:

- Uploading files from disk for backup or archival systems
- Implementing bucket policies and access control for multi-tenant environments
- Adding versioning and lifecycle management for compliance requirements
- Integrating with data processing pipelines or application services

The MinIO Python SDK supports the full S3 API, enabling you to implement any S3-compatible functionality required for your use case. This makes it a suitable replacement for AWS S3 in development environments, or for production deployments where you need control over your storage infrastructure.

## Using MinIO Images from Docker Hub

The demo repository includes alternative configurations using the older Docker Hub images (`minio/minio:latest` and `python:3.13-slim`) for comparison purposes. However, these images are no longer recommended for production use.

To use the Docker Hub images:

```shell
docker compose -f docker-compose.dockerhub.yml up
```

**Important Note**: As of October 23, 2025, MinIO stopped publishing container images to Docker Hub and Quay. The images that remain are no longer maintained and contain known vulnerabilities, including CVE-2025-62506, which the maintainers have declined to patch. We recommend using Chainguard's MinIO image instead, which provides:

- **Minimal attack surface** - Distroless design with only essential components
- **Zero CVEs** - Regular security updates to maintain a clean vulnerability profile
- **Non-root by default** - Enhanced security posture
- **Smaller image size** - Faster deployments and reduced storage requirements
- **SBOM included** - Complete software bill of materials for compliance
- **Free and publicly available** - No authentication required to pull the image

## Video Walkthrough: Multi-Stage Build and Image Scanning

This video demonstrates the workflow covered in Example 2, showing how to build the Python client application using a multi-stage Docker build with Chainguard images. The walkthrough also includes scanning both the Chainguard MinIO image and the Docker Hub alternative with Grype to compare their security profiles, illustrating the vulnerability differences between maintained and unmaintained container images.

{{< youtube iaEvQdZ9gh4 >}}


