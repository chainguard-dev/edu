FROM cgr.dev/chainguard/php:latest-dev@sha256:946e8d5323835458bcd47a6ad79ae0dd14e1d2e9479373fc554e2c323402f2e7

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
