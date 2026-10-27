FROM cgr.dev/chainguard/php:latest-dev@sha256:c6e789fe3cb862fd0b2aaef6d44d61afd01996bed33d358217aa5b5d45341d6e

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
