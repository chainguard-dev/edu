FROM cgr.dev/chainguard/php:latest-dev@sha256:438ca5f8ed93d7b5ba3bf852709b86c84221e8b03a21874b7fa4c27f34b15465

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
