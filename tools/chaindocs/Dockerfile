FROM cgr.dev/chainguard/php:latest-dev@sha256:935d57f8a5a9601da2a30fbc3c86a27135d2d6a08c9c1bac40b505dba9e3409f

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
