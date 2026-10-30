FROM cgr.dev/chainguard/php:latest-dev@sha256:7da679f4e05ec5f6322cc50c3d064f67154ddc73e115b25c48475fa9a3e20061

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
