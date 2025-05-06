## Chaindocs
This tool is designed to help with docs maintenance for Chainguard Academy. It provides functionality to audit documentation articles, check for deprecated content, and generate reports based on analytics data.

## Installation
You can use the included `make` command to create a chaindocs container. This will land you in a container with the chaindocs tool installed, where you can run the commands listed in the Usage section.

From the root of the Academy repository, run:
```shell
make chaindocs
```
You'll get output similar to this:

```shell
Building Chaindocs...
docker  build tools/chaindocs -t chaindocs.local
[+] Building 0.1s (8/8) FINISHED                                                                         docker:default
 => [internal] load build definition from Dockerfile                                                               0.0s
 => => transferring dockerfile: 426B                                                                               0.0s
 => [internal] load metadata for cgr.dev/chainguard/php:latest-dev                                                 0.0s
 => [internal] load .dockerignore                                                                                  0.0s
 => => transferring context: 78B                                                                                   0.0s
 => [internal] load build context                                                                                  0.0s
 => => transferring context: 3.19kB                                                                                0.0s
 => [1/3] FROM cgr.dev/chainguard/php:latest-dev                                                                   0.0s
 => CACHED [2/3] COPY . /app                                                                                       0.0s
 => CACHED [3/3] RUN cd /app &&     composer install --no-progress --no-dev --prefer-dist                          0.0s
 => exporting to image                                                                                             0.0s
 => => exporting layers                                                                                            0.0s
 => => writing image sha256:c398ae028e2f446430a123a2d2e2dd1b76ac49b6e9ff9bef79390967e319356b                       0.0s
 => => naming to docker.io/library/chaindocs.local                                                                 0.0s
Running Chaindocs...
docker run --rm \
-v $PWD/content:/app/content \
-e CONTENT_DIR=/app/content \
-it --entrypoint /bin/sh \
chaindocs.local
/app $ 

```

You can now run the `chaindocs` command from within the container:

```shell
./chaindocs help
```

The `CONTENT_DIR` environment variable is set to `/app/content`, which is where the documentation content is located.

### Manual Installation
If you prefer to install chaindocs manually, you can do so by following these steps - this will require a PHP 8.2+ environment.

```shell
cd tools/chaindocs
composer install
```
## Usage

### Audit Summary

```shell
./chaindocs audit
```

### Get deprecated articles

```shell
./chaindocs audit --deprecated
```

### Get articles with invalid timestamps

```shell
./chaindocs audit --invalid
```

### Get top articles from analytics csv

```shell
./chaindocs audit topcontent data=input.csv
```

To get only deprecated articles from the csv, ordered by number of views:

```shell
./chaindocs audit topcontent data=input.csv --deprecated
```

### Export audit csv

Invalid
```shell
./chaindocs audit report --invalid output=audit.csv
```

Deprecated
```shell
./chaindocs audit report --deprecated output=audit.csv
```

Deprecated from CSV list, ordered by number of views
```shell
./chaindocs audit report --topcontent data=input.csv output=audit.csv
```
