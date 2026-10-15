FROM cgr.dev/chainguard/php:latest-dev@sha256:ae4dc60934570107eefeec80f1406e357eeff18363bf04968db06308bd9e0bc2

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
