FROM cgr.dev/chainguard/php:latest-dev@sha256:006f3c23eb5a069d5850fbc787ebd0422a4c743e4610edb0e0eebfd4e62ecc28

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
