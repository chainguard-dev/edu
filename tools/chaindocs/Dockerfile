FROM cgr.dev/chainguard/php:latest-dev@sha256:677da59f3e878a774d28da1ac0e43cdd2d021607b147a1f198e446f6fb7961bb

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
