FROM cgr.dev/chainguard/php:latest-dev@sha256:a0280d8bba88b9032b185b0cb939ad768a0f59bcd507a8eeb50e0c995bd80fe4

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
