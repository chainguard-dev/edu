FROM cgr.dev/chainguard/php:latest-dev@sha256:b5d5980e4379a2fc6b15f2e541b448234b05537beee2a745997795a01ab97098

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
