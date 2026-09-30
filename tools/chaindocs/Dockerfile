FROM cgr.dev/chainguard/php:latest-dev@sha256:49f22a93e4d8c84a6de9054ee012a000b07740e1bf9fb30738328a1b8488a758

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
