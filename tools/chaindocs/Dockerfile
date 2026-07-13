FROM cgr.dev/chainguard/php:latest-dev@sha256:dafab8620b0ad5c627fcdc6475461313cce970462212a6383263058b79c60771

COPY . /app
RUN cd /app && \
    composer install --no-progress --no-dev --prefer-dist

USER root
RUN ln -s /app/chaindocs /usr/bin/chaindocs
USER php

ENTRYPOINT [ "php", "/app/chaindocs" ]
