FROM cgr.dev/chainguard/php:latest-dev@sha256:2a16184fcd3d40f2bc475decc15f0a087f2d7135fad429f4d4d4ef551cada5e0

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
