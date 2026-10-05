FROM cgr.dev/chainguard/php:latest-dev@sha256:7c577b1f1858a21d0f31d60ffad2cc83ca77acd4e7d0ad7cb868d6268decf2cf

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
