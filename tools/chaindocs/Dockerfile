FROM cgr.dev/chainguard/php:latest-dev@sha256:08dee0cb16ab3ceb36f9b776df7d6935f39d4de6c4f4f2cdbd55590f51d60502

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
