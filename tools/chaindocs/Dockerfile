FROM cgr.dev/chainguard/php:latest-dev@sha256:6497ff719dc0633e4f5135a1b0e5ee8ac46cf1ec85f03c430e01af58a67ba87e

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
