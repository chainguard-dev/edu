FROM cgr.dev/chainguard/php:latest-dev@sha256:cbdc744b0223b764be62fef892c02e8be2b76f9387f7433b1abbeb0d4643831e

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
