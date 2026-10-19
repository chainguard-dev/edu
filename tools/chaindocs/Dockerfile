FROM cgr.dev/chainguard/php:latest-dev@sha256:5b8d50f736252705e3199f36102515018200dbb0417269b3aeb5f43a97fa48d6

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
