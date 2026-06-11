FROM cgr.dev/chainguard/php:latest-dev@sha256:08f331cce07f47a5fbfa68c70cf9b1dd7c670db964f5ae79bb0766837b48fe3e

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
