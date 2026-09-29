FROM cgr.dev/chainguard/php:latest-dev@sha256:3c122a93a2a0145719694e1b6269f93675c2e284a0dbc243483f7c1adf14cb48

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
